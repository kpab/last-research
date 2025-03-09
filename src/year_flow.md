# 1 年の流れ

> [!NOTE]
> 研究テーマがどのように進んでいったか記します。
> 参考程度にしてください。

## 🔹 4 〜 5 月

テーマを決め、そのテーマに関連することを学ぶ期間でした。

- 04/09 初進捗

- テーマ決め期間: 私は論文見てテーマを探してました

  > [論文たち](papers.md)

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
  >
  > <details><summary>論文たち</summary>
  >
  > - [避難シミュレーションシステムの経路障害発生時への適用](https://www.jstage.jst.go.jp/article/aija/73/626/73_626_721/_pdf)
  > - [意思決定プロセスモデルによる群集流動シミュレーション](https://www.jstage.jst.go.jp/article/tjsai/32/5/32_AG16-H/_pdf/-char/ja)
  > - [Pedestrian lane formation and its influence on egress efficiency in the presence of an obstacle](https://www.sciencedirect.com/science/article/abs/pii/S0925753521002988)
  > - [パーソナルスペースを用いた障害物を回避する歩行者の群集流動](https://www.jstage.jst.go.jp/article/jscejd/64/4/64_4_513/_article/-char/ja/)
  > - [出口での衝突と方向転換が流動係数に及ぼす影響と障害物の効果について](https://www.jstage.jst.go.jp/article/jsiamt/19/3/19_KJ00005701709/_article/-char/ja/)
  > - [エージェントモデルによる連続的空間における人間行動シミュレータの構築及び建築計画への応用](https://www.jstage.jst.go.jp/article/aija/67/558/67_KJ00004075612/_article/-char/ja/)

  </details>

## 🔹 6 月

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

## 🔹 7 〜 9 月

Python に戻って作り始めました。
名付けるなら**A\*編**です

A star やダイクストラ法を使い、歩行者の再現に挑戦していました。

A\*編のコード https://github.com/kpab/futinobe

> 混雑度が上がった時にめり込んでしまうという問題を解決できず、別のアルゴリズムにしよう！ということで
> Boids 編が始まります

## 🔹 10 〜 1 月

**Boids 編**です。
Boids モデルの分離ルールと結合ルールを応用し、モデルを作りました

Boids 編のコードです

- [シミュレーション] https://github.com/kpab/doingSim
- [結果出力] https://github.com/kpab/plottingResult
