"""Shared CODE/PTB-XL figure renderer, adapted from CODE's plot_journal_final.py.

Render both posts: python blog/ecg_figures.py
Rebuild audited curve data from private run artifacts:
  python blog/ecg_figures.py --prepare --jev CODE_JEV.zip --gpt CODE_GPT.zip \
      --ptbxl PTBXL.jsonl

Only aggregate curves are published. No inference calls are made.
"""
import argparse
import json
import zipfile
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
from scipy.interpolate import PchipInterpolator

ROOT = Path(__file__).resolve().parent
BLUE, RED, GRAY = '#1879b8', '#d64e49', '#8b95a0'
MODELS = ('jev', 'gpt-decisions')
SPECS = {
    'system-one-ecg': ('CODE Test', ('1dAVb','RBBB','LBBB','SB','AF','ST'),
        ('First-degree AV block','Right bundle branch block','Left bundle branch block',
         'Sinus bradycardia','Atrial fibrillation','Sinus tachycardia'), 'roc_calibration'),
    'system-one-ptbxl': ('PTB-XL / GenECG', ('NORM','MI','STTC','CD','HYP'),
        ('Normal ECG','Myocardial infarction','ST-T changes','Conduction disturbance','Hypertrophy'),
        'ptbxl_roc_calibration'),
}


def grouped(y, p, edges):
    bins = np.clip(np.searchsorted(edges, p, side='right') - 1, 0, len(edges)-2)
    masks = [bins == b for b in range(len(edges)-1)]
    return (np.array([p[m].mean() for m in masks if m.any()]),
            np.array([y[m].mean() for m in masks if m.any()]))


def pchip_on_support(x, y, grid):
    values = np.full(len(grid), np.nan)
    x, idx = np.unique(x, return_index=True)
    y = y[idx]
    if len(x) >= 2:
        mask = (grid >= x.min()) & (grid <= x.max())
        values[mask] = np.clip(PchipInterpolator(x, y)(grid[mask]), 0, 1)
    return values


def supported_interval(traces):
    low = np.full(traces.shape[1], np.nan)
    high = low.copy()
    for q in range(traces.shape[1]):
        vals = traces[:,q]
        vals = vals[np.isfinite(vals)]
        if len(vals) >= .8 * len(traces):
            low[q], high[q] = np.quantile(vals, [.025, .975])
    return np.array([low, high])


def plain(value):
    if isinstance(value, np.ndarray):
        return plain(value.tolist())
    if isinstance(value, (list, tuple)):
        return [plain(v) for v in value]
    if isinstance(value, dict):
        return {k: plain(v) for k, v in value.items()}
    if isinstance(value, float) and not np.isfinite(value):
        return None
    return value


def prepare(folder, rows, bootstrap):
    from sklearn.metrics import roc_curve, roc_auc_score, brier_score_loss
    name, codes, _, _ = SPECS[folder]
    valid = []
    for row in rows:
        try:
            for model in MODELS:
                for code in codes:
                    a = row[model]['answers'][code]
                    p = a['probabilities']['YES']
                    if a['choice'] not in ('YES','NO') or not np.isfinite(p) or not 0 <= p <= 1:
                        raise ValueError('Invalid answer')
            valid.append(row)
        except (KeyError, TypeError, ValueError):
            continue
    is_ptb = folder == 'system-one-ptbxl'
    cluster_draws = None
    if is_ptb:
        patient = np.array([r['patient_id'] for r in valid])
        groups = np.unique(patient)
        indices = {v: np.flatnonzero(patient == v) for v in groups}
        rng = np.random.default_rng(20261016)
        cluster_draws = [np.concatenate([indices[v] for v in rng.choice(groups, len(groups), True)])
                         for _ in range(bootstrap)]
    data = {'dataset': name, 'n': len(valid), 'total':len(rows), 'bootstrap':bootstrap,
            'resampling': 'patient-cluster' if is_ptb else 'class-stratified',
            'classes':{}, 'grid': np.linspace(0,1,251), 'hist_edges': np.linspace(0,1,26)}
    for i, code in enumerate(codes):
        y = np.array([r['gold'][code] for r in valid])
        draws = cluster_draws
        if draws is None:
            pos, neg = np.flatnonzero(y == 1), np.flatnonzero(y == 0)
            draws = []
            for b in range(bootstrap):
                rng = np.random.default_rng(20261015+i*100000+b)
                draws.append(np.r_[rng.choice(pos,len(pos),True), rng.choice(neg,len(neg),True)])
        result = {'positives':int(y.sum())}
        for model in MODELS:
            p = np.array([r[model]['answers'][code]['probabilities']['YES'] for r in valid])
            fpr, tpr, _ = roc_curve(y,p)
            roc_samples, auc_samples, cal_samples = [], [], []
            edges = np.unique(np.quantile(p,np.linspace(0,1,9)))
            edges[0], edges[-1] = 0, 1
            x, z = grouped(y,p,edges)
            for ix in draws:
                if len(np.unique(y[ix])) == 2:
                    f,t,_ = roc_curve(y[ix],p[ix])
                    roc_samples.append(np.interp(data['grid'],f,t))
                    auc_samples.append(roc_auc_score(y[ix],p[ix]))
                cal_samples.append(pchip_on_support(*grouped(y[ix],p[ix],edges),data['grid']))
            result[model] = {'fpr':fpr, 'tpr':tpr, 'roc_band':np.quantile(roc_samples,[.025,.975],axis=0),
                'auc':float(roc_auc_score(y,p)), 'auc_ci95':np.quantile(auc_samples,[.025,.975]),
                'brier':float(brier_score_loss(y,p)), 'cal_x':x, 'cal_y':z,
                'cal_band':supported_interval(np.array(cal_samples)),
                'hist_counts':np.histogram(p,bins=data['hist_edges'])[0]}
        data['classes'][code] = result
        print(name, code, 'prepared', flush=True)
    (ROOT/folder/'chart-data.json').write_text(json.dumps(plain(data),separators=(',',':'),allow_nan=False)+'\n')
    return data


def render(folder):
    _, codes, names, basename = SPECS[folder]
    data = json.loads((ROOT/folder/'chart-data.json').read_text())
    grid = np.array(data['grid'])
    edges = np.array(data['hist_edges'])
    ncols = len(codes)
    plt.rcParams.update({'font.family':'DejaVu Serif','font.size':11,'figure.facecolor':'white',
        'axes.facecolor':'white','savefig.facecolor':'white','svg.fonttype':'none',
        'axes.linewidth':.8,'xtick.major.size':3,'ytick.major.size':3,'svg.hashsalt':'ecg-blog-shared'})
    fig = plt.figure(figsize=(4.35*ncols,13.6),layout=None)
    outer = fig.add_gridspec(2,ncols,left=.05,right=.992,bottom=.16,top=.88,
        hspace=.51,wspace=.33,height_ratios=[1,1.13])
    max_count = max(max(data['classes'][c][m]['hist_counts']) for c in codes for m in MODELS)
    hist_max = 10 ** np.ceil(np.log10(max_count))
    for i,(code,full) in enumerate(zip(codes,names)):
        result = data['classes'][code]
        roc = fig.add_subplot(outer[0,i])
        sub = outer[1,i].subgridspec(2,1,height_ratios=[3.4,1],hspace=.07)
        cal = fig.add_subplot(sub[0])
        hist = fig.add_subplot(sub[1],sharex=cal)
        for ax in (roc,cal):
            ax.plot([0,1],[0,1],'--',color=GRAY,lw=.9,zorder=1)
            ax.set(xlim=(0,1),ylim=(0,1),xticks=[0,.25,.5,.75,1],yticks=[0,.25,.5,.75,1])
            ax.tick_params(labelsize=10,pad=3)
            ax.spines[['top','right']].set_visible(False)
        roc.set_title(f'{code}\n{full}',fontsize=12.8,fontweight='bold',pad=11)
        roc.set_xlabel('False positive rate',fontsize=13)
        if i == 0:
            roc.set_ylabel('True positive rate',fontsize=13)
            cal.set_ylabel('Observed frequency',fontsize=13)
        cal.tick_params(axis='x',labelbottom=False,bottom=False)
        for model,color in zip(MODELS,(BLUE,RED)):
            v = result[model]
            band = np.asarray(v['roc_band'],dtype=float)
            roc.fill_between(grid,*band,color=color,alpha=.13,lw=0,zorder=2)
            roc.step(v['fpr'],v['tpr'],where='post',color=color,lw=1.55,zorder=3)
            band = np.asarray(v['cal_band'],dtype=float)
            cal.fill_between(grid,*band,color=color,alpha=.14,lw=0,zorder=2)
            cal.plot(grid,pchip_on_support(np.array(v['cal_x']),np.array(v['cal_y']),grid),color=color,lw=1.6,zorder=3)
            cal.scatter(v['cal_x'],v['cal_y'],s=10,color=color,zorder=4,edgecolor='white',linewidth=.3)
            hist.stairs(v['hist_counts'],edges,fill=True,color=color,alpha=.48,linewidth=.55)
        box = {'facecolor':'white','edgecolor':'none','alpha':.85,'pad':2}
        roc.text(.04,.98,f"AUROC\nJev: {result['jev']['auc']:.3f}\nGPT: {result['gpt-decisions']['auc']:.3f}",
            transform=roc.transAxes,fontsize=10,ha='left',va='top',bbox=box)
        cal.text(.04,.98,f"Brier: Jev {result['jev']['brier']:.3f}\nGPT {result['gpt-decisions']['brier']:.3f}",
            transform=cal.transAxes,fontsize=10,ha='left',va='top',bbox=box)
        hist.set(yscale='log',ylim=(.8,hist_max),yticks=10.**np.arange(int(np.log10(hist_max))+1))
        hist.tick_params(labelsize=9.5,pad=3)
        hist.spines[['top','right']].set_visible(False)
        hist.set_xlabel('Predicted probability',fontsize=13)
        if i == 0:
            hist.set_ylabel('ECGs (log)',fontsize=10)
    fig.text(.048,.968,'A  Discrimination: ROC curves',fontsize=22,fontweight='bold',ha='left')
    fig.text(.048,.927,f"{data['dataset']} | {data['n']:,} paired ECGs | Pointwise 95% {data['resampling']} bootstrap CI ({data['bootstrap']:,} resamples)",
        fontsize=13,ha='left',color='#45566a')
    fig.text(.048,.535,'B  Calibration: predicted versus observed probability',fontsize=22,fontweight='bold',ha='left')
    legend = [Line2D([0],[0],color=BLUE,lw=2,label='Jev 1.14.0'),
        Line2D([0],[0],color=RED,lw=2,label='GPT-6 Luna Decisions'),
        Line2D([0],[0],color=GRAY,lw=1,ls='--',label='Chance / perfect calibration'),
        Patch(facecolor='#7e9cae',alpha=.2,label='Pointwise 95% bootstrap interval')]
    fig.legend(handles=legend,loc='lower center',bbox_to_anchor=(.5,.084),ncol=4,frameon=False,fontsize=13)
    fig.text(.5,.046,'Calibration: PCHIP through observed quantile-bin means, without extrapolation or recalibration. Histograms show score distributions.',
        ha='center',fontsize=11,color='#465568')
    fig.text(.5,.025,'AUROC confidence intervals and Brier scores are computed from original predictions.',ha='center',fontsize=11,color='#465568')
    svg_path = ROOT/folder/(basename+'.svg')
    fig.savefig(svg_path,facecolor='white',metadata={'Date':None})
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text().splitlines())+'\n')
    fig.savefig(ROOT/folder/(basename+'.png'),dpi=170,facecolor='white')
    plt.close(fig)
    print('Rendered',folder,flush=True)


def read_zip(path):
    with zipfile.ZipFile(path) as z:
        names = [n for n in z.namelist() if n.endswith('predictions.jsonl')]
        if len(names) != 1:
            raise ValueError('Expected one predictions.jsonl')
        rows = [json.loads(s) for s in z.read(names[0]).decode().splitlines() if s]
        if len({r['image'] for r in rows}) != len(rows):
            raise ValueError('Duplicate CODE ids')
        return {r['image']:r for r in rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare',action='store_true')
    parser.add_argument('--jev',type=Path)
    parser.add_argument('--gpt',type=Path)
    parser.add_argument('--ptbxl',type=Path)
    args = parser.parse_args()
    if args.prepare:
        if not all((args.jev,args.gpt,args.ptbxl)):
            parser.error('--prepare requires --jev, --gpt and --ptbxl')
        j,g = read_zip(args.jev),read_zip(args.gpt)
        rows = []
        for key in sorted(j.keys() & g.keys()):
            if j[key]['gold'] != g[key]['gold']:
                raise ValueError('Reference labels differ: '+key)
            rows.append({'gold':j[key]['gold'],'jev':j[key],'gpt-decisions':g[key]})
        prepare('system-one-ecg',rows,1000)
        rows = [json.loads(s) for s in args.ptbxl.read_text().splitlines() if s]
        if len({r['ecg_id'] for r in rows}) != len(rows):
            raise ValueError('Duplicate PTB-XL ids')
        prepare('system-one-ptbxl',rows,300)
    for folder in SPECS:
        render(folder)


if __name__ == '__main__':
    main()
