# 朝ラ�?シュ用定数
# ------------------------
FRAME_COUNT = 100300
SKIP_RESULT_COUNT = 300 # 結果にカウントしな�?フレー�?数
BORN_RATE = 0.4
FUTINOBE_RATE = 0.3 # 淵野辺�?

MAX_SPEED = 2.5 # ?��
MAX_MAX_SPEED = [3.0, 0.5] # 上振れ最高速度, 確�?
MIN_MAX_SPEED = [2.0, 0.1] # 下振れ最高速度, 確�?

# -------------------------

START_HUMAN_COUNT = 10 # 初期?�?skipするけどね?�?

# -- エージェント�?�力系定数(固�?) --
HITO_SIYA_LEVEL = 16.0 # ?��?�?
WALL_SIYA_LEVEL = 16.0 # ?��?�?
SEKKATI = 0.3
YASASISA = 0.08 # 人回避の重み
AVOID_WALL_WEIGHT = 0.1 # 壁回避の重み
MIDDLE_RANGE = 10 # 中間地点到達確認�?囲
SLOWING_RANGE = 30 # 減速�?囲(ゴール-現在地<SLOWING_RANGEで減�?)
SLOW_LEVEL = 20
# -- マップ系定数 --
WIDTH = 500
HEIGHT = 500
WIDTH_HEATMAP = int(WIDTH/10)
HEIGHT_HEATMAP = int(HEIGHT/10)

# 壁置く時:全部False
# シミュレーション回す時、�?�部True

PERFECT_FAKE = True # �?�?
HIDE = True # シミュレーション�?すか
BACKGROUND = True # Background�?
# ----------------
LOG_NAME = "normalyuru.txt"
