# POINT や注意点

学んでおくと研究に役立つことや、注意点を示します

> [!NOTE]
> 個人的な評価です<br>
> テーマにもよると思います

## 📙 必須

### 🔹 クラス の使い方

[輪講について](src/point.md)に記載したポケモンの教材で学習後、自分で作って動かしてみると良いと思います

### 🔹 ログをファイルに出力する

`print`文でターミナルに出力された結果をコピーして蓄える...みたいなのは手間ですし、いつか消えて困ることになります

- 本研究では、[こんな感じ](https://github.com/kpab/last-research/blob/main/futinobe/doingSim/a01/modules/Simulation.py#L208-L215)でログ出力を追加しました
- [このように](https://github.com/kpab/last-research/blob/main/futinobe/doingSim/a01/a01.txt)、時間や区切り線も出力するといいと思います

- 処理速度[(参考)](https://js2iiu.com/2024/11/11/python-logging-comparison/)から、`f.write()`を使いましたが、[`logging`](https://docs.python.org/ja/3.13/howto/logging.html)パッケージを使うのもいいと思います

### 🔹 調べる習慣

プログラミングは、言語のキャッチアップからコーディング、バグ修正まで、自分で調べながら進めるものです。<br>
人に質問する際も、「ここまで調べて理解できたが、ここから先が分からない」といった形で聞くと良いでしょう。

## 📙 おすすめ

### 🔹 github

https://github.com/

- dropbox にあげるでもいいと思いますが、github が使えるとかっこいいです ✨

- 個人的に、教室のデスクトップを使う際に重宝しました

### 🔹 ファイルの並行・連続実行

[subprocess](https://docs.python.org/ja/3.13/library/subprocess.html)を使い、python ファイルを並行 or 連続で実行することです ([詳細](https://github.com/kpab/last-research/tree/main/futinobe/doingSim#zzzmainpy))。

一度のファイル実行で複数のシミュレーションを実行することができます

## 📙 注意

### 🔹 AI の使用

個人的に良くないと思った AI の使い方 2024 年度の実例を示します

- Paiza の問題を AI に解かせる

  > 自分のためになりません<br>
  > その時、他のメンバーに見栄を張れても、絶対にバレます

- 研究のコードを AI に丸投げする
  > 年末の輪講でコードを見た際、ボロがでます

> [!WARNING]
> コードを書く前にノートに思考を整理すると思いますが、それができていないのに AI に頼るのはやめましょう
