import seaborn as sns
import japanize_matplotlib
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np
import copy
import numpy as np
from result_yuru import *

type = "result_yuru"

now = aw16
now_string = "aw16"



def HeatmappingNumber(now_agents_positions, walls, fig_name):    
    fig2, ax2 = plt.subplots(figsize=(12.0, 8.0),
                           facecolor="gainsboro")
    
    ax2.set_xlim(0, 500)
    ax2.set_ylim(0, 500)

    ax2.set_title("~ヒートマップ~")
    ax2 = sns.heatmap(now_agents_positions, cmap='Greens',cbar=False, annot=True, fmt='d', annot_kws={'fontsize':5})
    for wall in walls:
            ax2.add_patch(Rectangle((wall[0]/10, wall[1]/10), (wall[2]-wall[0])/10, (wall[3]-wall[1])/10))
    ax2.invert_yaxis()
    # plt.show()
    fig2.savefig(f"{type}/{fig_name}/heatmap.png", dpi=300)
    plt.close(fig2)

# ヒートマップの差の出力
def GappingHeatmap(results, walls, fig_name):
    global normal
    no = copy.deepcopy(normal)
    no = np.array(no)
    results = np.array(results)
    
    gap = results - no

    fig2, ax2 = plt.subplots(figsize=(12.0, 8.0),
                           facecolor="gainsboro")
    
    ax2.set_xlim(0, 500)
    ax2.set_ylim(0, 500)

    ax2.set_title("~ヒートマップの差~")
    ax2 = sns.heatmap(gap, cmap='bwr',cbar=False, annot=True, fmt='d', annot_kws={'fontsize':4.0}, vmax=8000, vmin=-8000)
    for wall in walls:
            ax2.add_patch(Rectangle((wall[0]/10, wall[1]/10), (wall[2]-wall[0])/10, (wall[3]-wall[1])/10))
    ax2.invert_yaxis()
    # plt.show()
    fig2.savefig(f"{type}/{fig_name}/gap.png", dpi=300)



# 箱ひげ図
def GappingHakohigeHazure(results, fig_name):
    global normal
    no = copy.deepcopy(normal)
      # 二次元を一次元に変換
    results = sum(results, [])
    # 0を除去
    results = list(filter(lambda x: x!=0, results))
    results = np.array(results) # numpy配列に変換
    no = np.array(no)

    no = no.flatten()
    no = list(filter(lambda x: x!=0, no))
  
    data = (no, results)
    # 箱ひげ図のプロット
    fig, ax = plt.subplots()
    ax.boxplot(data, vert=False, showmeans=True, whis=1.4, widths=0.8)  # 横向き, 外れ値表記
    ax.set_title('箱ひげ図(外れ値あり)')
    ax.set_xlabel('通過人数')
    # ax.set_ylabel()
    ax.set_yticklabels(["normal", fig_name])
    plt.grid()
    fig.savefig(f"{type}/{fig_name}/hakogap.png")
    plt.close(fig)

def GapHist(now, fig_name):
    global normal
    no = copy.deepcopy(normal)

    # 一次変換
    no = sum(no, [])
    now = sum(now, [])

    
    # -- 0除く --
    no = list(filter(lambda x: x!=0, no))
    now = list(filter(lambda x: x!=0, now))

    # -- 平均値以下除く --
    # av_no = np.mean(no)
    # av_now = np.mean(now)
    # no = list(filter(lambda x: x>av_no, no))
    # now = list(filter(lambda x: x>av_now, now))

    # -- 第三四分位数以下除く
    # d3_no = np.percentile(no, 75)
    # d3_now = np.percentile(now, 75)
    # no = list(filter(lambda x: x>d3_no, no))
    # now = list(filter(lambda x: x>d3_now, now))

    # no = list(filter(lambda x: x>10000, no))
    # now = list(filter(lambda x: x>10000, now))

    cv_no = np.std(no)/np.mean(no)
    cv_now = np.std(now)/np.mean(now)
    print(cv_no, cv_now)

    plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    plt.hist(no, alpha=0.5, bins=12, color='#00AAFF', ec="#0000FF", label='normal')
    plt.hist(now, alpha=0.5, bins=12, color='#FF8888', ec="#FF0000", label=fig_name)
    # plt.hist(normal, alpha=0.5, color='#00AAFF', ec="#0000FF", label='normal')
    # plt.hist(now, alpha=0.5, color='#FF8888', ec="#FF0000", label=fig_name)
    #plt.xlim(0, 50000)
    #plt.ylim(0, 80)
    plt.xlabel('通過人数')
    plt.legend(loc="upper right")
    
    plt.savefig(f"{type}/{fig_name}/hist.png")
    # plt.show()
    plt.close()
    plt.figure()

    # d3_no = np.percentile(no, 97)
    # d3_now = np.percentile(now, 97)
    # no = list(filter(lambda x: x>=d3_no, no))
    # now = list(filter(lambda x: x>=d3_now, now))
    # lmax = max(max(no), max(now))
    # lmin = min(min(no), min(now))
    # plt.xlim(lmin, lmax)
    no = sorted(no, reverse=True)
    now = sorted(now, reverse=True)


    # no = list(filter(lambda x: x>=30000, no))
    # now = list(filter(lambda x: x>=30000, now))

    bins = 12
    range = (15000, 25000)
    n = 18
    y1, x1, _ = plt.hist(no[:18], alpha=0.5, bins=bins, color='#00AAFF', ec="#0000FF", label='normal', range=range)
    y2, x2, _ = plt.hist(now[:18], alpha=0.5, bins=bins, color='#FF8888', ec="#FF0000", label=fig_name, range=range)
    y_max = int(max(max(y1), max(y2))) + 1
    plt.yticks(np.arange(0, y_max))
    plt.xlabel('通過人数')
    plt.legend(loc="upper right")
    plt.savefig(f"{type}/{fig_name}/histup.png")
    plt.close()



HeatmappingNumber(normal, walls, now_string)
GappingHeatmap(now, walls, now_string)
GappingHakohigeHazure(now, now_string)
GapHist(now, now_string)