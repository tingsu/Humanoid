![humanoid_logo](res/humanoid_logo.png)

## Introduction
Humanoid explores Android apps like human. It uses deep learning techniques to borrow experiences from app usage traces generated by human.

Currently Humanoid works with [DroidBot](https://github.com/honeynet/droidbot). When DroidBot explores an Android app in model-based policy, it will generate several possible input events according to current UI state. Humanoid than sort the events such that events that will be performed by human most likely will be fired first.

## Prerequisite

- Python 3.x
- Tensorflow
- [DroidBot](https://github.com/honeynet/droidbot)
- [PyFlann](https://github.com/primetang/pyflann) (one may need to make it work under Python 3 according to its README)

Needed only if one wants to train Humanoid model from scratch:
- [RICO](http://interactionmining.org/rico) dataset

## Quick Start

**NOTES BEFORE USAGE: When used with DroidBot, Humanoid supports 1280x720, 1920x1080 and 2560x1440 screens only. Also, the Android navigation bar should be turned on.**

Humanoid is an XMLRPC service which can be shared among multiple DroidBot instances.

First, start Humanoid service by

    $ python3 agent.py -c config.json

After seeing

    === Humanoid RPC service ready at localhost:50405 ===

one can start DroidBot instances with `-humanoid localhost:50405` parameter. Now DroidBot will make use of Humanoid model when using model-based policies, such as `dfs_greedy`. See DroidBot [README](https://github.com/honeynet/droidbot) page for more usage details.

Modify `domain` and `port` values in `config.json` in the same directory to deploy Humanoid service at other addresses.


## Usefule commands to setup Humandroid by TingSU

1. install tensorflow 1.12

see [link1](https://www.liquidweb.com/kb/how-to-install-tensorflow-on-ubuntu-18-04/), [link2](https://linuxize.com/post/how-to-install-tensorflow-on-ubuntu-18-04/)

2. install additional moudles

```
pip install -U pip

pip install -U tensorflow==1.12

pip install matplotlib

pip install scipy

pip install pyflann-py3
```

