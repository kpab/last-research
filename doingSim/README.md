# doigSim 概要

シミュレーション実行ディレクトリ

壁の配置パターンは[こちら](walls.md)

### [zzzmain.py](doingSim/zzzmain.py)

python の組み込みモジュールである[subprocess](https://docs.python.org/ja/3.13/library/subprocess.html)を使い、複数のシミュレーションを同時 or 連続して実行するファイルです。

> Tips
> 複数のシミュレーションを実行したい場合、vscode で doingSim フォルダーを開き、**zzzmain.py**を実行します

```python
import subprocess

simulations = [
    "a.py",
    "b.py",
    "c.py",
]

# 並列で実行する場合
for s in simulations:
    subprocess.Popen(["python", s]) # python or python3

# 連続して実行する場合 (ただし、シミュレーション終了後にグラフが自動で消えるようにする必要があります)
for s in simulations:
    subprocess.run(["python", s]) # python or python3
```
