# class-cancellation-monitoring

## language

[English](doc/README_en.md)

## 説明

大学の`UNIVERSAL PASSPORT`、通称UNIPAをAM6:00~PM21:00の間1時間ごとに情報を取得し、新しい休講情報が投稿された場合Twitterのアカウントにツイートします。

## 注意

大学非公式です。責任は負いかねます。

## 開発環境

OS: MacOS Catalina 10.15.2~  
Python: 3.6.9  

仮想環境: Pipenv  
実行例:

```sh
pipenv shell

>>> exit
```

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

ﾏﾀﾞﾂｸｯﾃﾅｲ…
