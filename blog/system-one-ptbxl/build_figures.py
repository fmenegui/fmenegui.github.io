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
data=json.loads(zlib.decompress(base64.b64decode(AGGREGATE)))
codes=["NORM","MI","STTC","CD","HYP"]
colors={"jev":"#1879b8","gpt-decisions":"#d64e49"}
aucs={"NORM":(.702,.677),"MI":(.669,.724),"STTC":(.465,.655),"CD":(.535,.706),"HYP":(.697,.677)}
briers={"NORM":(.317,.402),"MI":(.258,.178),"STTC":(.485,.475),"CD":(.184,.187),"HYP":(.137,.142)}
plt.rcParams.update({"font.family":"DejaVu Serif","font.size":11,"svg.fonttype":"none",
                     "figure.facecolor":"white","axes.facecolor":"white"})
fig,axes=plt.subplots(2,5,figsize=(20,8.5))
for i,code in enumerate(codes):
    for row in range(2):
        ax=axes[row,i]
        ax.plot([0,1],[0,1],"--",color="#8b95a0",lw=1)
        ax.set_xlim(0,1);ax.set_ylim(0,1)
        ax.spines[["top","right"]].set_visible(False)
        ax.tick_params(labelsize=9)
    roc,cal=axes[:,i]
    roc.set_title(code,fontweight="bold",fontsize=14)
    for j,model in enumerate(colors):
        values=data[code][model]
        roc.plot(np.linspace(0,1,len(values["roc"])),values["roc"],color=colors[model],lw=2)
        points=np.array(values["cal"])
        if len(points)>1:
            points=points[np.argsort(points[:,0])]
            x,idx=np.unique(points[:,0],return_index=True)
            y=points[idx,1]
            if len(x)>1:
                grid=np.linspace(x.min(),x.max(),150)
                cal.plot(grid,np.clip(PchipInterpolator(x,y)(grid),0,1),color=colors[model],lw=2)
            cal.scatter(x,y,color=colors[model],s=14)
    roc.text(.04,.97,f"AUROC  Jev {aucs[code][0]:.3f}\\nGPT {aucs[code][1]:.3f}",
             transform=roc.transAxes,va="top",fontsize=9,bbox=dict(facecolor="white",edgecolor="none",alpha=.9))
    cal.text(.04,.97,f"Brier  Jev {briers[code][0]:.3f}\\nGPT {briers[code][1]:.3f}",
             transform=cal.transAxes,va="top",fontsize=9,bbox=dict(facecolor="white",edgecolor="none",alpha=.9))
    roc.set_xlabel("False positive rate",fontsize=10)
    cal.set_xlabel("Predicted probability",fontsize=10)
    if i==0:
        roc.set_ylabel("True positive rate",fontsize=11)
        cal.set_ylabel("Observed positive fraction",fontsize=11)
fig.suptitle("PTB-XL / GenECG: ROC (top) and calibration (bottom)",fontsize=19)
fig.text(.5,.02,"Jev (blue) and GPT Decisions (red). Calibration: quantile bins and PCHIP within observed support only.",ha="center",fontsize=10)
fig.tight_layout(rect=(0,.045,1,.94),w_pad=1.5,h_pad=2)
out=Path(__file__).parent
fig.savefig(out/"ptbxl_roc_calibration.svg",bbox_inches="tight")
fig.savefig(out/"ptbxl_roc_calibration.png",dpi=160,bbox_inches="tight")
print("Created blog figures from actual aggregated curves")
