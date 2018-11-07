#!/usr/bin/env python
#coding:utf-8
# @Time    : 2018/1/19 20:50

import itertools as its
words = "0123456789asdf"
r =its.product(words,repeat=5)

with open("pass.txt","w") as f:
    for i in r:
        f.write("".join(i) + '\n')
