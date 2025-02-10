import seaborn as sns
import japanize_matplotlib
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np
import copy
import numpy as np
from walls import addwalls
from result_morning_latest import *

type = "result_morning"

now_string = "normal"
kabe = False

s_now_string = "s_" + now_string

normalllls = rrr["s_normal"]

now = rrr[s_now_string]
keys = ["全部", "AtoK", "BtoK", "CtoK", "KtoA", "KtoB", "KtoC", "S_AtoK", "S_BtoK", "S_CtoK", "S_KtoA", "S_KtoB", "S_KtoC"]
speeds = ["S_AtoK", "S_BtoK", "S_CtoK", "S_KtoA", "S_KtoB", "S_KtoC"]

def get_points_in_rectangles(walls):

    points = set()
    
    for wall in walls:
        # 座標を10で割って整数に変換
        x1, y1 = wall[0] // 10, wall[1] // 10
        x2, y2 = wall[2] // 10, wall[3] // 10
        
        # x1,y1からx2,y2までの範囲の全座標を生成
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                points.add((x, y))
    points_list = sorted(list(points))

    return points_list

def create_map_from_points(points_list, now, width=50, height=50, default_value=None):
    # 入力データを2次元リストとして読み込む
    original_map = []
    for line in now:
        original_map.append([int(val) if isinstance(val, str) else val for val in line])
    
    
    # 座標を0に設定
    for x, y in points_list:
        if 0 <= x < width and 0 <= y < height:
            original_map[y][x] = 0
            
    return original_map


def HeatmappingNumber(now_agents_positions, walls, fig_name):
    points_list = get_points_in_rectangles(walls)
        
    fig2, ax2 = plt.subplots(figsize=(12.0, 8.0),
                        facecolor="gainsboro")
        
    ax2.set_xlim(0, 500)
    ax2.set_ylim(0, 500)

    ax2.set_title(f"ヒートマップ: " + "BtoK + CtoK")
    

    btok = np.array(create_map_from_points(points_list, now_agents_positions["BtoK"]))
    ctok = np.array(create_map_from_points(points_list, now_agents_positions["CtoK"]))
    now = btok + ctok
    

    ax2 = sns.heatmap(now, cmap='Wistia',cbar=False, annot=False, fmt='d', annot_kws={'fontsize':4.5})
    for wall in walls:
            ax2.add_patch(Rectangle((wall[0]/10, wall[1]/10), (wall[2]-wall[0])/10, (wall[3]-wall[1])/10, fc='#696969'))
    ax2.invert_yaxis()

    if kabe:
        ax2.add_patch(Rectangle((addwalls[now_string][0]/10, addwalls[now_string][1]/10), (addwalls[now_string][2]-addwalls[now_string][0])/10, (addwalls[now_string][3]-addwalls[now_string][1])/10, fc='k'))

    # plt.show()
    fig2.savefig(f"{type}/{fig_name}/heatmap_btokctok.png", dpi=300)
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
            ax2.add_patch(Rectangle((wall[0]/10, wall[1]/10), (wall[2]-wall[0])/10, (wall[3]-wall[1])/10, fc='#696969'))
    ax2.invert_yaxis()
    # -- 壁ある時 --
    if kabe:
        ax2.add_patch(Rectangle((addwalls[now_string][0]/10, addwalls[now_string][1]/10), (addwalls[now_string][2]-addwalls[now_string][0])/10, (addwalls[now_string][3]-addwalls[now_string][1])/10, fc='k'))
    
    fig2.savefig(f"{type}/{fig_name}/gap.png", dpi=300)
    plt.close(fig2)

def GappingHeatmapNew(now_agents_positions, walls, fig_name): # 正規化, position分け
    points_list = get_points_in_rectangles(walls)
    global normalllls
    fig2, ax2 = plt.subplots(figsize=(12.0, 8.0),
                            facecolor="gainsboro")
        
    ax2.set_xlim(0, 500)
    ax2.set_ylim(0, 500)

    ax2.set_title(f"ヒートマップ: " + "BtoK CtoK Gap")


    for key in keys:
        nor = normalllls[key]
        nor = create_map_from_points(points_list, nor)
        nor = np.array(nor)
        total_normal = np.sum(nor)
        nor = nor*100/total_normal
    
        now = now_agents_positions[key]
        now = create_map_from_points(points_list, now)
        now = np.array(now)
        total_now = np.sum(now)
        now = now*100/total_now

        gap = now - nor

        gap_max = np.max(abs(gap))

        if key=="CtoK" or key=="BtoK":
            ax2 = sns.heatmap(gap, cmap='bwr',cbar=False, annot=False, fmt='.2f', annot_kws={'fontsize':4.5}, vmax=gap_max, vmin=-1*gap_max)
        else:
            continue
        for wall in walls:
            ax2.add_patch(Rectangle((wall[0]/10, wall[1]/10), (wall[2]-wall[0])/10, (wall[3]-wall[1])/10, fc='#696969'))
            ax2.invert_yaxis()

        if kabe:
            ax2.add_patch(Rectangle((addwalls[now_string][0]/10, addwalls[now_string][1]/10), (addwalls[now_string][2]-addwalls[now_string][0])/10, (addwalls[now_string][3]-addwalls[now_string][1])/10, fc='k'))
       
    

    # plt.show()
    fig2.savefig(f"{type}/{fig_name}/heatmap_gap_btokctok.png", dpi=300)
    plt.close(fig2)

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


def CountZero(now):
    # 一次変換
    now = sum(now, [])
    zero_wall = 1611
    zero_points = len(now) - np.count_nonzero(np.array(now)) - zero_wall
    print(f"{now_string}のゼロ人数通過地点: {zero_points}")



HeatmappingNumber(now, walls, now_string)
# GappingHeatmapNew(now, walls, now_string)
