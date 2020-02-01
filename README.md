# class-cancellation-monitoring

![python](https://img.shields.io/github/pipenv/locked/python-version/yuto51942/class-cancellation-monitoring)
![riposize](https://img.shields.io/github/repo-size/yuto51942/class-cancellation-monitoring)
![lastcommit](https://img.shields.io/github/last-commit/yuto51942/class-cancellation-monitoring)\
![fllowme](https://img.shields.io/github/followers/yuto51942?label=FollowMe&style=social)
![twitter](https://img.shields.io/twitter/follow/cateiru?style=social)

language: [🇯🇵](README.md)   [🇺🇸](doc/README_en.md)

## 説明

大学の掲示板である`UNIVERSAL PASSPORT`(UNIPA)からAM6:00~PM21:00の間1時間ごとに休講・補講情報を取得し、新しい休講・補講情報が投稿された場合~~Twitterのアカウントにツイート~~Slackのbotに送信します。

## 注意

大学非公式です。責任は負いかねます。

## 開発環境

OS: MacOS Catalina\
Python: 3.6.9\
GoogleChrome: v79

仮想環境: Pipenv\
仮想環境の実行例:

```sh
pipenv shell
>>>
>>> # 退出する場合
>>> exit
```

## 動かす

動作環境

* Mac
* Linux(動作未確認)
* Windows
* Python 3.6.x

事前準備しておくもの

* GoogleChrome(version:79)
* Slackの[Incoming Webhook API](#Slack-Incoming-Webhook)
* 学籍番号とパスワード

```sh
# Pipenvをインストール
pip install pipenv

# Pipenvを使用し依存関係のインストール
pipenv install

# 実行
pipenv run start

# 停止は[⌘+C]or[CONTROL+C]
# 仮想環境の停止はexitと入力するか[⌘+D]
```

わからないところがあればTwitterのDMへ\
![twitter](https://img.shields.io/twitter/follow/cateiru?style=social)

## コードの静的解析

Pylint, flake8, mypyを使用しております。\
実行方法:

```sh
sh analysis.sh
```

## Slack Incoming Webhook

pythonのライブラリである`slackweb`を使用しております。

[詳しくは](https://qiita.com/shtnkgm/items/4f0e4dcbb9eb52fdf316)

## UNIPA取得方法について

pythonライブラリである`selenium`, `chromedriver-binary`を使用しております。

`chromedriver-binary`を使用する際にそのバージョンに適切なGoogleChromeが必要です。
現在、Chrome79に対応されております。他のバージョンで実行したい場合は、

```sh
pipenv install chromedriver-binary=={バージョン}
```

を使用し新たにライブラリをインストールしてください。

[参考1](https://qiita.com/syunyo/items/09cc636344212112a6fc)\
[参考2](https://qiita.com/meznat/items/b9eee3c2700731855f10)

## 更新履歴

### 1.0.0

リリース

### 1.0.1

* ディレクトリ指定時にそのディレクトリ内になにかファイルが存在しないとエラーになる問題の修正
* 鳩山キャンパスの休講・補講情報の取得に対応。
* 誤字の修正。
* READMEの説明の追加。

### 1.0.2

* [issues](https://github.com/yuto51942/class-cancellation-monitoring/issues/2#issue-542261473)を解消
  * 指定先にディレクトリがない場合はユーザーに新しく作るかを問います
* unipaの休講・補講情報のidの値が変わっていたため変更

## 1.0.3

* `'{:02d}:00'.format()`を使用し、プログラムを簡単にした。
* 英語版のREADMEを書いた。
