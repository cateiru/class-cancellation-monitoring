# class-cancellation-monitoring

![python](https://img.shields.io/github/pipenv/locked/python-version/yuto51942/class-cancellation-monitoring)
![riposize](https://img.shields.io/github/repo-size/yuto51942/class-cancellation-monitoring)
![lastcommit](https://img.shields.io/github/last-commit/yuto51942/class-cancellation-monitoring)\
![fllowme](https://img.shields.io/github/followers/yuto51942?label=FollowMe&style=social)
![twitter](https://img.shields.io/twitter/follow/cateiru?style=social)

language: [🇯🇵](../README.md)   [🇺🇸](README_en.md)

## Description

Obtains information on classes and supplementary courses every hour from 6:00 AM to 21:00 AM from UNIVERSAL PASSPOR (UNIPA), the university bulletin board, and ~~Tweet to Twitter account~~ sends it to Slack's bot when a new class or supplementary course information is posted.

## warning

University informal. We cannot take responsibility.

## Development environment

OS: MacOS Catalina\
Python: 3.6.9\
GoogleChrome: v79

Virtual environment: Pipenv\
Execution example of virtual environment:

```sh
pipenv shell
>>>
>>> # When leaving
>>> exit
```

## move

Operating environment

* Mac
* Linux(Operation not confirmed)
* Windows
* Python 3.6.x

Things to prepare in advance

* GoogleChrome(version:79)
* Slack's [Incoming Webhook API](#Slack-Incoming-Webhook)
* Student number and password

```sh
# Install Pipenv
pip install pipenv

# Install dependencies using Pipenv
pipenv install

# Run
pipenv run start

# Stop is [⌘ + C] or [CONTROL + C]
# To stop the virtual environment, type `exit` or [⌘ + D]
```

If you have any questions, go to Twitter DM\
![twitter](https://img.shields.io/twitter/follow/cateiru?style=social)

## Static analysis of code

I use Pylint, flake8, mypy.\
Execution method:

```sh
sh analysis.sh
```

## Slack Incoming Webhook

It uses `slackweb`, a python library.

[For more information](https://qiita.com/shtnkgm/items/4f0e4dcbb9eb52fdf316)

## How to get UNIPA

It uses python libraries `selenium` and` chromedriver-binary`.

When using `chromedriver-binary`, you need the appropriate GoogleChrome for that version.
Currently, Chrome79 is supported. If you want to run on another version,

```sh
pipenv install chromedriver-binary=={version}
```

Please install a new library using.

[Reference 1](https://qiita.com/syunyo/items/09cc636344212112a6fc)\
[Reference 2](https://qiita.com/meznat/items/b9eee3c2700731855f10)

## Change log

### 1.0.0

release

### 1.0.1

* Fixed the problem that an error occurs when there is no file in the directory when the directory is specified.
* Corresponds to the acquisition of information on canceled classes and supplementary classes at Hatoyama campus.
* Correct typos.
* Added README description.

### 1.0.2

* Resolve [issues](https://github.com/yuto51942/class-cancellation-monitoring/issues/2#issue-542261473).
  * If there is no directory at the specified destination, ask the user whether to create a new one
* Changed because the value of id of the cancellation / supplementary information of unipa has changed
