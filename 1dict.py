#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#python 3.14


# 例题
#在一个list里面，如果有一个数字出现了50%次以上，
#就返回那个数字，否则就返回-1.
#e.g.[1,1,1,1,4,5] ->1，[2,2,3,4] -> -1。

#fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
list1 = [1,1,1,1,4,5] # list1 should return 1
list2 = [2,2,3,4] 
list3 = [1,1,1,4,5,6]

# data type: dictionary: key-value的组合 
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# tel -> {'sape': 4139, 'guido': 4127, 'jack': 4098}
# del tel['sape'] tel-> { 'guido': 4127, 'jack': 4098}
# dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) ->
# -> {'sape': 4139, 'jack': 4098, 'guido': 4127}


def majority(listy):
	# l: half of the length of the list
	l = len(listy)/2
	# build a dict based on listy
	dicty={}
	for x in listy:
		# print x
		if x in dicty:
			dicty[x] = dicty[x]+1
		else:
			dicty[x]=1
	# print dicty
	# iterate over a dict
	# for k in dict: 
	for k,v in dicty.items():
		# print(k,v)
		if v > l:
			print k
			return
	print -1

majority(list1)
majority(list2)
majority(list3)


# 好像也可以？？
def majority2(listy):
	l = len(listy)/2
	for x in listy:
		if listy.count(x)>l: #list.count too complex
			print x
			return
	print -1

majority2(list1)
majority2(list2)
majority2(list3)


# 作业：Given a list of integers and a target integer, 
# return true if any two integer in the list sum up to the target, 
# else return false e.g. [1,2,3],4 -> true, [2,3,4],2->false

# rest function: first, rest = l[0], l[1:]

def sumup(listy,n):
	# count number of iteration
	count=1
	for x in listy:
		# rest of the list
		rest = listy[count:]
		count+=1
		for y in rest:
			print(x,y)
			if (x+y)==n:
				#print (x,y)
				print True
				return
	print False

# 不需要print -> 直接return
# count extra index

def sumup1(lst,n):
	for i in xrange(len(lst)): 
		for j in xrange(i+1, len(lst)): 
			if lst[i]+lst[j]==n:
				return True
	return False


sumup([1,2,3],4)
sumup([2,3,4],2)
sumup([1,1,2,5],4)





