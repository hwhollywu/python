#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.17
# 写一个优秀的hash function，把一个任意长度的字符串map到0-10里.
# hash function can't be easily reversed

'''
ramdonly generate 0-10:
from random import randint
randint(0, 9)
'''

# 1 随机：按首字母 随机分
# 2 优秀：按字符串长度平均分配 比如最长的放到最短的里

def hash_1(chars):
	num = ord(chars[0].lower()) # to 1-26
	return (num-1)%10 # to 0-10 不平均因为25%10不整除。。

def hash_2(chars): # s1*1+s2*2+...sn*n=sum %10 -> result
	sum = 0
	for c in chars:
		sum +=ord(c)
	return sum % 10



# https://en.wikipedia.org/wiki/Hash_function
# The ideal hash function has three main properties:
# It is extremely easy to calculate a hash for any given data.
# It is extremely computationally difficult to calculate an alphanumeric text that has a given hash.
# It is extremely unlikely that two slightly different messages will have the same hash.

# 3.17

# 贝德尔不完备定律？每个数学公理都有一个


# module : library
# e.g. brew is a module -> brew list
# easy_install
# pip install jupyter

jupyter notebook

# import numpy as np
# import matplotlib.pyplot



#------------------
# array/list: read, write, O(1) add, remove O(n)
# hashtable/set/dict: read, write, add, remove O(1)

# how to decide the number of buckets in hashtable
# when too many elements are in the hashtable, resize the hashtable
# complexity of rehashing: O(n) 
# build a larger hashtable, Put each element into the new hashtable

# amortized cost analysis: 把On的cost分配到之前的O(1)操作里


# ------------------
# pip install flask
# flask is a web app framework
# other: Django,
'''
 library vs framework: 
 library -> utility function & constants e.g.math.pi(), math.sqrt()
 framework-> an entity that u work upon
'''

from flask import Flask
app = Flask(__name__)

@app_route("/")
def hello():
	...

vim hello.py
FLASK_APP=hello.py flask run --host-0.0.0.0 
ngrok工具：把自己电脑的网络连到ngrok公司的服务器
# (make sure the port is the same as ngrok)
./ngrok http 8000

--> 127.0.0.1:5000 端口
