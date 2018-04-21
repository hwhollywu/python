#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.30


'''

OOP: object oriented programming in python

class vs object
class种类 可以用很多种 human1 = Human(100) human2=Human(100)
object 只有一个 human1,human2
'''

class Human():

	weight = None #attribute

	def __init__(self, weight): #method
		self.weight = weight

	def run(self):
		weight -= 1

	def eat(self, weight_of_food):
		self.weight += weight_of_food

	def give_birth(self):
		self.weight -= 10
		return Human(10)

	# Java private - public 
	# attribute 不能直接访问 一般用getter

	# __weight__ in python : 表示private attribute

	# human.run() -- run(self)
	# 把human object当做第一个parameter pass进function

	# inheritance

# subclass
class Baby(Human):
	def __init__(self):
		super(Holly, self).__init__(30)

	# new function
	def sing(self):
		print "La La La"

	def run(self):
		super(Holly, self).init__
		

# 爬虫： 先访问一个网站，把URL放进queue里，
# 根据rule看有没有需要点进去的超链接，放进queue里面 BFS

# scrapy: framework 自己define functions

# 给你源代码，要写Parse 返回给framework 
# 内容，和要访问的超链接


'''
working trace:


1. fix the bug while installing pip scrapy
" pip install scrapy "
-> Command "python setup.py egg_info" failed with error code 1 
in /private/var/folders/v0/8tjyfvws4l32y860d9kcvd580000gn/T/pip-build-6nhPMf/Twisted/

-> have an out of date version of setuptool
" pip install --upgrade setuptools "
-> Exception Traceback (most recent call last):
 File "/Library/Python/2.7/site-pasckages/pip/basecommand.py", 
-> permission problem 
" pip install --upgrade setuptools --user python " 
完成，但之前的问题还在，白弄
https://github.com/pypa/pip/issues/3917
Apple 系统自带Python的问题？？
-> 系统升级(空间不足) 
or 下载 anaconda/miniconda 
or install in a dedicated virtualenv

- try easy_install sth
- try brew install sth
- try sudo install sth
- try install sth --user python (exception when uninstalling setup tools)


'''


