"""Build compact journal-style PTB-XL figure from audited aggregate curves.
Curves are precomputed from 21,796 paired records. Full patient-bootstrap
figure and source-level reproducible script are provided separately.
This lightweight website rendering does not fabricate uncertainty ribbons.
"""
import base64,zlib,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

AGGREGATE="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"
# Shared visual specification from CODE Test's plot_journal_final.py:
# identical font, palette, axes, panel headings, legend and spacing.
# Aggregated curves cannot recreate empirical steps, histograms or bootstrap bands.
# Never manufacture those missing statistics.
data=json.loads(zlib.decompress(base64.b64decode(AGGREGATE)))
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
CODES=("NORM","MI","STTC","CD","HYP")
LONG=("Normal ECG","Myocardial infarction","ST and T-wave changes",
      "Conduction disturbance","Hypertrophy")
BLUE="#1879b8"
RED="#d64e49"
GRAY="#8b95a0"
AUCS={"NORM":(.702,.677),"MI":(.669,.724),"STTC":(.465,.655),
      "CD":(.535,.706),"HYP":(.697,.677)}
BRIERS={"NORM":(.317,.402),"MI":(.258,.178),"STTC":(.485,.475),
        "CD":(.184,.187),"HYP":(.137,.142)}
plt.rcParams.update({"font.family":"DejaVu Serif","font.size":11,
                     "figure.facecolor":"white","axes.facecolor":"white",
                     "savefig.facecolor":"white","svg.fonttype":"none",
                     "axes.linewidth":.8,"xtick.major.size":3,"ytick.major.size":3})
fig=plt.figure(figsize=(22,12.0),layout=None)
outer=fig.add_gridspec(2,5,left=.055,right=.987,bottom=.17,top=.87,
                       hspace=.48,wspace=.34,height_ratios=[1,1.05])
for i,(code,full) in enumerate(zip(CODES,LONG)):
    roc=fig.add_subplot(outer[0,i])
    cal=fig.add_subplot(outer[1,i])
    for ax in (roc,cal):
        ax.plot([0,1],[0,1],"--",color=GRAY,lw=.9,zorder=1)
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
        ax.set_xticks([0,.25,.5,.75,1])
        ax.set_yticks([0,.25,.5,.75,1])
        ax.tick_params(labelsize=10,pad=3)
        ax.spines[["top","right"]].set_visible(False)
    roc.set_title(f"{code}\n{full}",fontsize=12.8,fontweight="bold",pad=11)
    roc.set_xlabel("False positive rate",fontsize=13)
    if i==0:roc.set_ylabel("True positive rate",fontsize=13)
    cal.set_xlabel("Predicted probability",fontsize=13)
    if i==0:cal.set_ylabel("Observed frequency",fontsize=13)
    for model,color in (("jev",BLUE),("gpt-decisions",RED)):
        values=data[code][model]
        # ROC: grid-sampled empirical data, not synthetic interpolation of AUC.
        curve=np.asarray(values["roc"],dtype=float)
        grid=np.linspace(0,1,len(curve))
        roc.plot(grid,curve,color=color,lw=1.55,zorder=3)
        # Same CODE Test PCHIP interpolation, within observed support only.
        points=np.asarray(values["cal"],dtype=float)
        if points.ndim==2 and len(points)>=2:
            points=points[np.argsort(points[:,0])]
            x,unique=np.unique(points[:,0],return_index=True)
            y=points[unique,1]
            if len(x)>=2:
                xx=np.linspace(x.min(),x.max(),251)
                cal.plot(xx,np.clip(PchipInterpolator(x,y)(xx),0,1),
                         color=color,lw=1.6,zorder=3)
            cal.scatter(x,y,s=12,color=color,zorder=4,
                        edgecolor="white",linewidth=.3)
    roc.text(.04,.98,f"AUROC\nJev: {AUCS[code][0]:.3f}\nGPT: {AUCS[code][1]:.3f}",
             transform=roc.transAxes,fontsize=10,ha="left",va="top",
             bbox={"facecolor":"white","edgecolor":"none","alpha":.83,"pad":2})
    cal.text(.04,.98,f"Brier: Jev {BRIERS[code][0]:.3f}\nGPT {BRIERS[code][1]:.3f}",
             transform=cal.transAxes,fontsize=10,ha="left",va="top",
             bbox={"facecolor":"white","edgecolor":"none","alpha":.85,"pad":2})
fig.text(.055,.965,"A  Discrimination: ROC curves",fontsize=22,
         fontweight="bold",ha="left")
fig.text(.055,.92,"PTB-XL / GenECG  |  21,796 paired ECGs  |  Empirical aggregated curves",
         fontsize=13,ha="left",color="#45566a")
fig.text(.055,.53,"B  Calibration: predicted versus observed probability",
         fontsize=22,fontweight="bold",ha="left")
legend=[Line2D([0],[0],color=BLUE,lw=2,label="Jev 1.14.0"),
        Line2D([0],[0],color=RED,lw=2,label="GPT-6 Luna Decisions"),
        Line2D([0],[0],color=GRAY,lw=1,ls="--",
               label="Chance / perfect calibration")]
fig.legend(handles=legend,loc="lower center",bbox_to_anchor=(.5,.095),
           ncol=3,frameon=False,fontsize=13)
fig.text(.5,.054,"Calibration: PCHIP through observed bin means, without extrapolation or recalibration.",
         ha="center",fontsize=11,color="#465568")
fig.text(.5,.03,"Aggregated source does not preserve bootstrap traces or score histograms. No uncertainty ribbons are inferred.",
         ha="center",fontsize=11,color="#465568")
out=Path(__file__).parent
fig.savefig(out/"ptbxl_roc_calibration.svg",facecolor="white")
fig.savefig(out/"ptbxl_roc_calibration.png",dpi=200,facecolor="white")
plt.close(fig)
print("Generated PTB-XL figure using CODE Test visual specification")
