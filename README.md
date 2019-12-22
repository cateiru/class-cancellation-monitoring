# class-cancellation-monitoring

![python](https://img.shields.io/github/pipenv/locked/python-version/yuto51942/class-cancellation-monitoring)
![riposize](https://img.shields.io/github/repo-size/yuto51942/class-cancellation-monitoring)
![lastcommit](https://img.shields.io/github/last-commit/yuto51942/class-cancellation-monitoring)
![fllowme](https://img.shields.io/github/followers/yuto51942?label=FollowMe&style=social)
![twitter](https://img.shields.io/twitter/follow/cateiru?style=social)

## language

[English](doc/README_en.md)

## 説明

大学の`UNIVERSAL PASSPORT`、通称UNIPAをAM6:00~PM21:00の間1時間ごとに情報を取得し、新しい休講情報が投稿された場合~~Twitterのアカウントにツイート~~Slackのbotに送信します。

## 注意

大学非公式です。責任は負いかねます。

## 開発環境

OS: MacOS Catalina  
Python: 3.6.9  
GoogleChrome: v79

仮想環境: Pipenv  
仮想環境の実行例:

```sh
pipenv shell

>>> exit
```

## 動かす

動作環境

* Mac
* Linux(動作未確認)
* Windows(動作未確認)

事前準備しておくもの

* GoogleChrome(version:79)
* SlackのIncoming Webhook API
* 学籍番号とパスワード

```sh
python main.py
```

わからないところがあればTwitterのDMへ  
![twitter](https://img.shields.io/twitter/follow/cateiru?style=social)

## コードの静的解析

Pylint, flake8, mypyを使用しております。  
実行方法:

```sh
sh analysis.sh
```

もしくは、

```sh
pipenv run start
```

## 更新履歴

1.0.0: リリース
