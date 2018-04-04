#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.16

'''
# scalibility 24, n av-time 这道题并不scalable 
-> to grow and manage increased demand.

# functional programming:
-> building software by composing pure functions,  
avoiding shared state, mutable data, and side-effects. It's declarative. 
e.g. haskell

object oriented programming：
-> where application state is usually shared and colocated with methods in objects.
attributes+methods
e.g. java

a programming paradigm that:
declarative:  describes the logic of a computation without describing its control flow.
(more scalable, simple,) what to do 
imperative: uses statements that change a program’s state. how to do
e.g. java (common data structures, and global variables)
'''

# 优化av-time, 标准答案 O（nlogn）  
# 1. 建立 list [(3, 5), (4, 6)] -> (3,1)(4,1）(5,-1)(6,-1)
# 2. sort Onlogn 
# 3. count On

# list.extend + list 合并list
# list.append + element 加上element
# list.sorted

# comp function def even numbers as smaller
'''
def comp(x,y):
	if x % 2 ==0:
		return -1
	return 1
sorted([1,2,3,4,5],comp) -> [4,2,1,3,5]
sorted_list = sorted(listy,key=lambda tup: tup[0])
'''

# lambda inc x: x+1
# inc(1)->2

# all fast sorting algorithm is nlogn

def av(listy):
	changes=[]
	for l in listy:
		changes.extend([(l[0],1),(l[1],-1)])
	sorted_changes = sorted(changes, key=lambda x:x[0]) #O(nlogn)
	car_count=0
	max_car_count=0
	for change in sorted_changes:
		car_count+=change[1]
		if car_count>max_car_count:
			max_car_count=car_count
	return max_car_count

print(av([(3, 5), (4, 6)]))
print(av([(3, 5), (0, 24), (4, 6)]))
print(av([(2, 5), (7, 10)]))


# hash: a function that maps objects into a number in 
# a designated integer interval
# e.g. [0-10] "123" -> 2
# collision: the hash value of two objects are the same

# 自带hash function
# import hashlib # -> 加密SHA hash






