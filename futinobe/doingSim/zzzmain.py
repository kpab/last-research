# メイン使用
import subprocess

# 相対パス
normalpy = "./normal/main.py"
normalyurupy = "./normalyuru/main.py"

wall01py = "./wall01/main.py"
wall02py = "./wall02/main.py"
wall03py = "./wall03/main.py"
wall04py = "./wall04/main.py"
wall05py = "./wall05/main.py"
wall06py = "./wall06/main.py"
wall07py = "./wall07/main.py"
wall08py = "./wall08/main.py"
wall09py = "./wall09/main.py"
wall10py = "./wall10/main.py"
wall11py = "./wall11/main.py"
wall12py = "./wall12/main.py"
wall13py = "./wall13/main.py"
wall14py = "./wall14/main.py"
wall15py = "./wall15/main.py"
wall16py = "./wall16/main.py"
wall17py = "./wall17/main.py"

a01py = "./a01/main.py"
a02py = "./a02/main.py"
a03py = "./a03/main.py"
a04py = "./a04/main.py"
a05py = "./a05/main.py"
a06py = "./a06/main.py"
a07py = "./a07/main.py"

aw01py = "./aw01/main.py"
aw02py = "./aw02/main.py"
aw03py = "./aw03/main.py"
aw04py = "./aw04/main.py"
aw05py = "./aw05/main.py"
aw06py = "./aw06/main.py"
aw07py = "./aw07/main.py"
aw08py = "./aw08/main.py"
aw09py = "./aw09/main.py"
aw10py = "./aw10/main.py"
aw11py = "./aw11/main.py"
aw12py = "./aw12/main.py"
aw13py = "./aw13/main.py"
aw14py = "./aw14/main.py"
aw15py = "./aw15/main.py"
aw16py = "./aw16/main.py"
aw17py = "./aw17/main.py"
aw18py = "./aw18/main.py"
aw19py = "./aw19/main.py"
aw20py = "./aw20/main.py"



pys = [
    normalpy,
    # normalyurupy

    # wall01py,
    # wall02py,
    # wall03py,
    # wall04py,
    # wall05py,
    # wall06py,
    # wall07py,
    # wall08py,
    # wall09py,
    # wall10py,
    # wall11py,
    # wall12py,
    # wall13py,
    # wall14py,
    # wall15py,
    # wall16py,
    # wall17py,

    # a01py,
    # a02py,
    # a03py,
    # a04py,
    # a05py,
    # a06py,
    # a07py

    # aw01py,
    # aw02py,
    # aw03py,
    # aw04py,
    # aw05py,
    # aw06py,
    # aw07py,
    # aw08py,
    # aw09py,
    # aw10py,
    # aw11py,
    # aw12py,
    # aw13py,
    # aw14py,
    # aw15py,
    # aw16py,
    # aw17py,
    # aw18py,
    # aw19py,
    # aw20py,
]

# subprocess.run(["python3", n])

# for _ in range(8):
#     subprocess.run(["python3", wall_2py])

# for py in pys:
#     subprocess.run(["python", py])


# 並列でやる時
for py in pys:
    doing = subprocess.Popen(["python", py])
