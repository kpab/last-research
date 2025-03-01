# やっておいてよかったことについて

レベルに応じて紹介します

> [!NOTE]
> レベルは個人的な評価です
> テーマにもよると思います

## 必須

### class の使い方

[輪講について](src/point.md)に記載した教材で学習後、自分で作って動かしてみると良いと思います

### ログをファイルに出力する

`print`文でターミナルに出力された結果をコピーして蓄える...みたいなのは手間ですし、いつか消えて困ることになります

- 本研究では、[こんな感じ](https://github.com/kpab/last-research/blob/main/futinobe/doingSim/a01/modules/Simulation.py#L208-L215)でログ出力を追加しました
- [このように](https://github.com/kpab/last-research/blob/main/futinobe/doingSim/a01/a01.txt)、時間や区切り線も出力するといいと思います

- 処理速度[(参考)](https://js2iiu.com/2024/11/11/python-logging-comparison/)から、`f.write()`を使いましたが、[`logging`](https://docs.python.org/ja/3.13/howto/logging.html)パッケージを使うのもいいと思います

## おすすめ

### github

- dropbox にあげるでもいいと思いますが、github が使えるとかっこいいです

- 個人的に、教室のデスクトップを使うときに重宝しました

### ファイルの並行・連続実行

[subprocess](https://docs.python.org/ja/3.13/library/subprocess.html)を使い、python ファイルを並行 or 連続で実行することです ([詳細](https://github.com/kpab/last-research/tree/main/futinobe/doingSim#zzzmainpy))
