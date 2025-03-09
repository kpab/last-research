# 1 年の流れ

> [!NOTE]
> 研究テーマがどのように進んでいったか記します。
> 参考程度にしてください。

## テーマ決め編

### 4 〜 5 月

テーマを決め、そのテーマに関連することを学ぶ期間でした。

- 04/09 初進捗

- 05/02 テーマ決定

  > 没になったテーマとその理由については、[没テーマ案](src/banned_heme_plan.md)に書いておきます。

- 05/14 簡単なシミュレーションを初めて作成

  > <details><summary>簡単なシミュレーション</summary>
  >
  > https://sintyoku01.streamlit.app/
  >
  > - 歩行者はランダムな場所に同時に出現する。
  > - 歩行者は、右端に向かう
  > - 座標が被った場合、次のフレームは動かない
  > - 衝突を判定すると青 → 赤に色が変化する

</details>

- 05/16 〜 06/04 論文

  > この期間は混雑度や歩行者の動きに関する論文を読んでました。

  <details><summary>論文</summary>

  </details>

### 6 月

名付けるなら **Unity 編**です。

06/06 〜 07/02 は Unity で進めていました

<details><summary>Unity 編の最高傑作です</summary>

https://unityroom.com/games/futinobe07

> - スペースキー: 視点切り替え
> - a キー: エージェント発射
> - Up, Down: 生成頻度の操作

</details>

Unity のメソッドの中身がわからず Python に戻りました

Unity 編のコード
https://github.com/kpab/futinobe_unity

### 7 〜 9 月

Python に戻って作り始めました。
名付けるなら**A\*編**です

A star やダイクストラ法を使い、歩行者の再現に挑戦していました。

A\*編のコード https://github.com/kpab/futinobe

> 混雑度が上がった時にめり込んでしまうという問題を解決できず、別のアルゴリズムにしよう！ということで
> Boids 編が始まります

### 10 〜 1 月

**Boids 編**です。
Boids モデルの分離ルールと結合ルールを応用し、モデルを作りました

Boids 編のコードです

- [シミュレーション] https://github.com/kpab/doingSim
- [結果出力] https://github.com/kpab/plottingResult
