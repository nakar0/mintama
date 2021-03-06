# みんたま
> URL : [mintama.work](http://mintama.work)

## 目次
- [概要](#概要)
- [アプリ説明](#説明)
- [開発環境](#開発環境)
- [開発について](#開発について)
- [各機能について](#各機能について)

***
## 概要
私はこれまで独学でプログラミングの学習を進めてきました。その中で得た効率的な独学の仕方などをアプリを通して伝えられたらと思い、当アプリを作成しました。

主な機能は、アウトプット機能、分散学習機能、勉強のTODO管理機能です。他にもいろいろな機能（コミュニティ機能やチャット機能など）を追加したかったのですが、思った以上に開発に手間取り、現在の機能のみでデプロイしています。

***

## アプリ説明
### ■　ホーム
ホームは左と右（スマートフォンでは、上と下）で機能が分かれています。<br>
左は、効率的な分散学習をするためのものです。詳細については、[こちら](http://www.singakukai.com/column/8610.html)を見ていただきたいのですが、簡単に説明すると、ノート機能で保存したノートを一番復習するのに良い時期に、表示させてくれる機能です。<br>
右は、ボード機能で作成したボードを一つデフォルトのボードとしてセットし、ホーム画面でも簡単に目を通すことができるようにした機能です。

デフォルトボードの設定は、<ホームに表示させるボードを選択する>ボタン押下　->　ボードを選択　->　<確定>ボタン押下　でできます。

### ■　TODO
カスタマイズしたTODO管理ボードを作成することができます。<br>

【ボード一覧画面】<br>
自分の全てのボードを確認するができます。<br>
- 右下の＜+＞ボタンを押すことで新規ボードの作成が行えます。
- 各ボードの<ボードに入る>ボタンでボードの操作画面に移動ますし。
- ボード作成ダイアログの＜デフォルトのボードを作成＞ボタンは、私が「こんなボードあったりいいな」と思ったボードを自動で作成してくれます。<br><br>
デフォルトのボードについて
    - リスト<br>
    下記のリストが自動で作成されます。デフォルトでは、「することすべて」と「完了したこと全て」以外は自動切り替えがON、切り替え時間0:00になっています。

        - することすべて<br>
        自動切り替え先：今日すること

        - 今日すること<br>
        自動切り替え先：前からの持ち越し
        - 今日完了したこと<br>
        自動切り替え先：完了したこと全て

        - 前からの持ち越し<br>
        自動切り替え先：することすべて

        - 完了したことすべて<br>
        自動切り替え先：なし


    - 運用<br>
    まず、「することすべて」に全てのタスクを書き出す。その中から今日することだけ「今日すること」に移動する。
    「今日すること」のカードから順にタスクを完了させていき、順次「今日完了したこと」に移動させていく。
    一日の終わりに「今日完了したこと」を元に、ノート機能でノートを作成する。<br>
    次の日には自動で、「今日完了したこと」→「完了したことすべて」、「今日すること」→「前からの持ち越し」、「前からの持ち越し」→「することすべて」に移動される。
    

【ボード操作画面】<br>
リストとカードを使用して、自分でカスタマイズさせたTODO管理ボードを作成することができます。単純なTODO管理だけでなく、決まった時間にカードを自動で移動させたりすることもできます。

- ボードの名前<br>
ボードの名前をクリックすることにより、ボードの名前を変更することができます。

- リスト・カードについて<br>
ドラッグ&ドロップで自由に移動させることができます。


- 右上メニューボタン<br>
ボードの全体的な操作を行うことができます。メニューの各ボタンについては、ボタンの名前の通りの動作をしますので、説明は省きます。
- リストのペンボタン<br>
リストの編集。以下、各項目について。
    - このリストのカードを次に移動<br>
    切り替え先リストが指定されている状態でこのボタンを押すと、該当リストの全てのカードが次のリスト移動します。

    - ✖︎ボタン<br>
    編集画面を閉じます。

    - リスト名<br>
    リストの名前を入力します。
    
    - 切り替え先リスト<br>
    自動切り替え時の切り替え先のリストを選択します。

    - 自動切り替え<br>
    自動切り替えのON/OFFを選択します。

    - 切り替え時間<br> 
    自動切り替えのポイントとなる時間を指定します。切り替え先リストが選択され、自動切り替えがONの状態の場合、この時間を跨ぐとカードが自動で次のリストに切り替わります。デフォルトは、0:00です。

    - アーカイブ<br>
    該当リストをアーカイブします。（データは残りますが、表示はされないようになります。）

    - 削除<br>
    リストを削除します。削除するリストに含まれるカードも全て削除されます。

    - 保存<br>
    変更を反映させます。

- カードのペンボタン<br>
カードの編集。以下、各項目について。
    - カード名<br>
    リストの名前を入力します。

    - 詳細<br>
    カードの詳細を入力します。

    - アーカイブ<br>
    該当リストをアーカイブします。（データは残りますが、表示はされないようになります。）

    - 削除<br>
    リストを削除します。削除するリストに含まれるカードも全て削除されます。

    - 保存<br>
    変更を反映させます。

- 右下＜＋＞ボタン<br>
新規リストの作成をすることができます。作成画面の各項目については、上記「リストのペンボタン」に同じ。

### ■　ノート
学んだことを記録します。

- 新規ノートの作成<br>
新しくノートを作成します。以下、各項目について。

    - タイトル<br>
    タイトルを入力します。

    - 見出し<br>
    セクションの見出しを入力します。

    - ごみ箱ボタン<br>
    セクションを削除します。

    - 内容<br>
    セクションの詳細を入力します。

    - カテゴリー<br>
    セクションのカテゴリーを選択します。

    - 参考資料<br>
    自分が登録した参考資料から選択します。

    - ＜＋＞ボタン<br>
    セクションを追加します。

    - ＜作成＞ボタン<br>
    ノートを保存します。

- 自分のノート一覧<br>
自分が作成したノートの一覧を表示させます。ノートをクリックすることにより、ノートの詳細が見れます。<br>
検索窓でキーワード検索をすることもできます。

- みんなのノート一覧<br>
自分と他の人のノートの一覧を見ることができます。

- ノートの詳細画面<br>
ノートの詳細を確認できます。＜編集＞ボタンを押すと、ノートを編集できます。


### ■　リファレンス
参考にしたサイトなどを登録し、閲覧することができます。登録したリファレンスはノートに紐づけることができます。

### ■　アカウント
自分のプロフィールを閲覧設定することができます。以下、プロフィール設定項目。
- ユーザー名<br>
- メールアドレス<br>
- 性別<br>
- 居住地<br>
- ひび割れ度<br>
もともと、各ユーザーに独学者としてのレベルをつけるつもりでした、実装には至りませんでした。

- 学習開始時期<br>
- プロフィール画像<br>
- 自己紹介<br>
### 
***
## 開発環境
- PC
    - Windows10 -> 現在、Mac Book Pro
- 言語
    - Python
    - JavaScript ( node.js )
- フレームワーク
    - Django
    - Rest framework
    - Vue.js
- サーバー
    - AWS
***
## 開発について
### ■　アーキテクチャ
- M : Django.Models
- V : Vue.js
- C : Rest framework , Django.Views

### ■　要件定義
ポートフォリオを作成しようと思った段階で、プログラミングスクールに通っている人がどんな風にしてポートフォリオを作っているのかが気になり、Twitterやブログなどを見ると、まず最初に要件定義やER図なるものを作成してから、アプリ開発に取り掛かっていることを知りました。私もとりあえずそれを真似て、要件定義やER図を作成してみることにしました。<br>
ネット記事を参考に、うまくできたとは言えませんが一応作成することはできました。ファイルは以下のリンクにアップしています。
- [企画書](https://mintama-bucket.s3-ap-northeast-1.amazonaws.com/dev/%E4%BC%81%E7%94%BB%E6%9B%B8.numbers)
- [サイトマップ](https://mintama-bucket.s3-ap-northeast-1.amazonaws.com/dev/%E3%82%B5%E3%82%A4%E3%83%88%E3%83%9E%E3%83%83%E3%83%95%E3%82%9A.xmind)
- [独学について（アイデア抽出）](https://mintama-bucket.s3-ap-northeast-1.amazonaws.com/dev/%E7%8B%AC%E5%AD%A6%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%EF%BC%88%E3%82%A2%E3%82%A4%E3%83%86%E3%82%99%E3%82%A2%E6%8A%BD%E5%87%BA%EF%BC%89.xmind)


実装機能の確認やModel作成時に少し確認する程度でしたが、初めの段階でおおまかな全体像をイメージすることができたので、作成してよかっと思います。

### ■　API
データのやり取りはDjango Rest frameworkを使用したAPIを作成し、Vue.js × axiosを使用して表示させています。<br>
主にSerializers（データの正規化をするところ）で躓きましたが、技術ブログやリファレンス、Rest frameworkの生のコードを読みなどして何とか実装出来ました。<br>
最初の方は知識不足で、URL設計などはよくわからないことになっていますが、当アプリをある程度作成し終えた後に、「[Webを支える技術](https://www.amazon.co.jp/Web%E3%82%92%E6%94%AF%E3%81%88%E3%82%8B%E6%8A%80%E8%A1%93-HTTP%E3%80%81URI%E3%80%81HTML%E3%80%81%E3%81%9D%E3%81%97%E3%81%A6REST-WEB-PRESS-plus/dp/4774142042/ref=sr_1_1?adgrpid=52846719243&gclid=Cj0KCQjw9fntBRCGARIsAGjFq5GNiCKen-zALwjIl16KB8UXULN2Ay2ep5YvfaDT_OjN4b7o42qn6aYaAlBwEALw_wcB&hvadid=338558549746&hvdev=c&hvlocphy=1009507&hvnetw=g&hvpos=1t1&hvqmt=e&hvrand=16511819965943856419&hvtargid=aud-759242200046%3Akwd-333749887651&hydadcr=16039_11170864&jp-ad-ap=0&keywords=web%E3%82%92%E6%94%AF%E3%81%88%E3%82%8B%E6%8A%80%E8%A1%93&qid=1572823341&sr=8-1)」を読むと、内容がすんなり入ってきて、Restfulの重要性やどのようにしてAPIを設計するべきなのかが少しはわかりました。


### ■　Django
Django本来の機能を使用した箇所は、Model、Form、サインアップ、ログインなどです。Djangoで簡略化されている機能については、甘えさせてもらい使わせてもらっています。大半の機能はRest frameworkで実装しているため、Django自体の記述量は比較的少ないです。

### ■　Vue.js
View側はVue.js, vuetifyを使用しました。最初の開発環境構築（webpack）の段階でエラーが出まくり2週間ほど苦戦していました。このときは本当につらかったです😭<br>
結局、webpackの基礎をudemyで勉強しなおし、一から実装することによって乗り越えました。やっぱり基礎は大事！
Vuexについては、vuetifyを使ったことにより、componentのネストがほぼほぼなくなり、あまり使わなかったです。<br>
メモリの消費量などは気にせずコードを記述しているので、次からはそういうことにも目を向けてコードを書いていきたいです
Vue.jsを使用した感想は、おもしろい！です。難しくなく、直観的に動作してくれるのでそう感じました。

### ■　AWS
WEBサーバーは、EC2内でDjango、nginx、uwsgiで動かしています。データベースはMariaDBです。静的ファイルはS3にアップロードをする仕様にし、CloudFrontを介して取得をします。<br>
AWSは主にudemyの「[AWS：ゼロから実践するAmazon Web Services。手を動かしながらインフラの基礎を習得](https://www.udemy.com/course/aws-and-infra/learn/lecture/15463490#overview)」で勉強しました。そこではネットワークの基礎知識についても触れられていて、AWSとネットワークを一緒に学習できたことで、より理解が深まりました。また、Django用のEC2サーバー構築をする中でも、Linuxやより深いネットワークの知識に触れることができ、とても勉強になりました。

### ■　データベース
Djangoでは、データの保存にオブジェクト思考のModelを使用するため、直接SQLの記述をすることはありませんでしたが、初めの方に「[SQL 第2版 ゼロからはじめるデータベース操作](https://www.amazon.co.jp/SQL-%E7%AC%AC2%E7%89%88-%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E6%93%8D%E4%BD%9C-%E3%83%9F%E3%83%83%E3%82%AF-ebook/dp/B01HD5VWWO/ref=sr_1_1_sspa?adgrpid=61747762268&gclid=Cj0KCQjw9fntBRCGARIsAGjFq5EcJ6mq0e6OdRs2RCg03QV-Vj0L9xwjXs-7eGHrSAnnMZefbIhL1wsaAmiSEALw_wcB&hvadid=338568407012&hvdev=c&hvlocphy=1009507&hvnetw=g&hvpos=1t1&hvqmt=e&hvrand=11218410178420634383&hvtargid=aud-759242200046%3Akwd-335126078348&hydadcr=27266_11561145&jp-ad-ap=0&keywords=%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E5%A7%8B%E3%82%81%E3%82%8B%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9&qid=1572827167&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRFdEOERVMjFSVDdUJmVuY3J5cHRlZElkPUEwMDA1Mjc2MVlQQVlZMzE3TTM2SCZlbmNyeXB0ZWRBZElkPUEyWk1PMVZWM05MMERZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)」などでデータベースの概念を勉強していたので、「ここではWHERE区を使ってるんだ」などのある程度のイメージを持って、Model作成や操作をすることができました。

### ■　テスト
要件定義段階では、テスト駆動開発を行おうと考えていましたが、そもそもテストコード自体をそんなに書いたことがなかったため、テスト駆動開発をどのように進めていけば分からず、結局、開発の最後にテストコードを書くことにしました。<br>
テストコードを書くことは、あまり楽しいものではなかったですが、テストを行っていくなかで、やっぱり意図しない動作をするところがあったため、テストは大事だなと改めて思いました。

### ■　リファクタリング
テストが終わった後、ざっとリファクタリングを行ってみたのですが、簡素化できる箇所や読みにくい箇所が多々ありました。これから、他の人が書いたコードや「[リーダブルコード](https://www.amazon.co.jp/%E3%83%AA%E3%83%BC%E3%83%80%E3%83%96%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89-%E2%80%95%E3%82%88%E3%82%8A%E8%89%AF%E3%81%84%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E6%9B%B8%E3%81%8F%E3%81%9F%E3%82%81%E3%81%AE%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%A7%E5%AE%9F%E8%B7%B5%E7%9A%84%E3%81%AA%E3%83%86%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF-Theory-practice-Boswell/dp/4873115655/ref=sr_1_1?adgrpid=56076398369&gclid=Cj0KCQjw9fntBRCGARIsAGjFq5GAI8jR6fxoxdjWLtOh9ItjM8Y6O94SlwU8_IbuDOYe_UTK3O_eIiEaAoWPEALw_wcB&hvadid=338571512561&hvdev=c&hvlocphy=1009507&hvnetw=g&hvpos=1t1&hvqmt=e&hvrand=12114735990637356485&hvtargid=aud-759242200046%3Akwd-334758528225&hydadcr=27298_11561624&jp-ad-ap=0&keywords=%E3%83%AA%E3%83%BC%E3%83%80%E3%83%96%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89&qid=1572828633&sr=8-1)」を読み返して、自分も他人も読みやすいコードを書いていきたいです。また、まだ自分のコードを他の人に見てもらったという経験がないので、そういう経験もどんどんしていきたいです。

***
## 工夫点
工夫したところを紹介します。

### ■　サインアップ
非同期に「ユーザー名」と「パスワード」の入力データを送信し、サーバー側のバリデーション結果を返す仕様にしています。
サーバー側のバリデーションはDjangoで用意されているものを使用しました。

▽バリデーション例
- ユニークなユーザー名であるか
- 簡単なパスワードでないか

### ■　ノート・リファレンスのキーワード検索
クライアント側では、ユーザーが空白区切り入力したキーワードをカンマ区切りに変換し、リクエストします。
サーバー側では、カンマ区切りのクエリパラメータを分解し、各キーワードが一つでも含まれるデータを抽出します。データの検索範囲は、リレーションしているデータまで対象です。

▽SQLイメージ
1. INNER JOINでリレーションデータを結合
2. 各カラムに対して、キーワード検索し当てはまるものを抽出
3. GROUP BYで重複をなくす

### ■　Twitter自動投稿
ノート作成時、自動でTwitterに投稿できる仕様にしています。
実装についてはQiitaにまとめたので、そちらを見てください。

[DjangoとTwitterを連携させ、Twitterへ自動投稿する](https://qiita.com/nakar0/items/b51261a4b7862d1cab0e)



