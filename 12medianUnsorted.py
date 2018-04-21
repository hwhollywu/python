#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.26 
'''
find median of a unsorted list
随机算法1：quick sort
随机算法2: 只看数量多的一半，找

e.g.
[1,4,3,7,5,2,6]
6,[1,4,2,5,2][7] find 3th (median=3rd)
4,[1,3,2] [5] return 4

if find 7th
7-6=1 找到了

Complexity: 
E[len(larger segment)] = 3/4 of the whole len
T(n) <= (n-1) + T(3n/4)
等比数列： N+ 3n/4 = （3/4）^2n^2+ ... 
->(1-3/4)^(-1)*n -> 4n
T(n) <= 4n
-> complexity: O(n)


guess and check : complexity analysis
(mergesort)
T(n) = cn + 2*T(n/2)
nlogn


T(E[n]) vs E(T[n]) n is linear

'''
from numpy import median
import random
l1 = [1,4,3,7,5,2,6] # 4.0
l2 = [3,2,-1,0,2,3] # 2.0
l3 = [0,0,1,2,2,3] # 1.5
# print("l1: ", median(l1))

l4 = [0,1,2,2,2,3,4]

def find_kth(l, k):
	pivot_num = random.randint(0,len(l)-1) 
	pivot = l[pivot_num]
	lesser = []
	greater = []
	for i in xrange(0,len(l)):
		if l[i] < pivot:
			lesser.append(l[i])
	# case 1: the kth element is in the lesser part
	if len(lesser) > k:
		return find_kth(lesser, k)
	k -= len(lesser)

	# case 2: the kth element is in the pivot
	num_pivots = l.count(pivot) # if pivot is a repeated element
	if num_pivots > k:
		return pivot
	k -= num_pivots

	# case 3: the kth element is in the greater part
	for i in xrange(0,len(l)):
		if l[i] > pivot:
			greater.append(l[i])
	return find_kth(greater, k)

def find_median_kth(l):
	# if odd 
	if len(l) % 2 == 1 :
		return find_kth(l, len(l)/2)
	# if even
	else :
		result1 = find_kth(l, (len(l)-1)/2)
		result2 = find_kth(l, (len(l)+1)/2)
		return (result1 + (result2 * 1.0)) / 2

print(find_median_kth(l1))
print(find_median_kth(l2))
print(find_median_kth(l3))
print(find_median_kth(l4))


'''
高级算法
deterministic 算法： 没有随机变量
how to calculate the median of an unsorted array in a 
deterministic algorithm

https://rcoh.me/posts/linear-time-median-finding/

deterministic linear-time algorithm 

1973 by the mouthful of Blum, Floyd, Pratt, Rivest, and Tarjan.

1. Group the array into n/5 of size 5 and 
find the median of each array. n/5个median
O(n): find median in constant length
2. Recursively, find the median of medians. 
call this p.
T(n/5) : recursive要这么写
3. use p as a pivot to split the array into 
subarrays LESS and GREATER
O(n)
4. Recurse on the appropriate piece 
T(7n/10): ??

T(n) <= cn + T(n/5) + T(7n/10)

g=n/5
total number of elements smaller than p : 
3(g/2)=3n/10 一半的组有小于p的median,这些组里至少三个数<=p 
total number of elements greater than p : 
3(g/2)=3n/10 一半的组有大于p的median,这些组里至少三个数>=p 

T(n) <= cn + T(n/5) + T(7n/10)
	 <= cn + T(9n/10)
	 <= 10n

complexity: O(n)


'''


def find_kth_deterministic(l, k):
	# base case: 
	if len(l) < 5:
		return find_median_kth(l) # assume constant time
	# group into size 5 groups
	lists_in_size = []
	for i in xrange(0, len(l), 5):
		lists_in_size.append(l[i:i+5])
	# sort each group
	for li in lists_in_size:
		list.sort(li) # complexity: Best O(n), worst O(nlogn)
	# find median of medians
	medians = []
	for li in lists_in_size:
		if len(li) == 5:
			medians.append(li[2])
	pivot = find_median_deterministic(medians) # ???
	# split into two arrays by pivot and recurse
	lesser = []
	greater = []
	for i in xrange(0,len(l)):
		if l[i] < pivot:
			lesser.append(l[i])
	# case 1: the kth element is in the lesser part
	if len(lesser) > k:
		return find_kth_deterministic(lesser, k)
	k -= len(lesser)

	# case 2: the kth element is in the pivot
	num_pivots = l.count(pivot) # if pivot is a repeated element
	if num_pivots > k:
		return pivot
	k -= num_pivots

	# case 3: the kth element is in the greater part
	for i in xrange(0,len(l)):
		if l[i] > pivot:
			greater.append(l[i])
	return find_kth_deterministic(greater, k)


def find_median_deterministic(l):
	# if odd 
	if len(l) % 2 == 1 :
		return find_kth_deterministic(l, len(l)/2)
	# if even
	else :
		result1 = find_kth(l, (len(l)-1)/2)
		result2 = find_kth(l, (len(l)+1)/2)
		return (result1 + (result2 * 1.0)) / 2

print find_median_deterministic(l1)
print find_median_deterministic(l2)
print find_median_deterministic(l3)
print find_median_deterministic(l4)

# l5: [1,141] unsorted
l5 = [81,72,47,51,63,17,8,93,46,41,16,79,80,105,71,35,\
    14,127,91,66,130,94,1,21,43,6,37,24,111,50,108,118,73,\
    39,70,138,22,86,131,87,27,98,110,126,49,34,128,65,129,\
    89,62,99,52,3,68,7,95,36,69,28,121,11,2,109,120,75,42,\
    136,124,76,64,92,25,139,19,77,100,4,114,135,44,97,48,29,\
    123,20,107,141,26,74,125,113,30,116,9,106,96,140,83,122,\
    134,32,102,84,59,119,56,115,85,40,104,55,88,53,13,112,67,\
    133,54,23,15,132,38,57,10,60,61,58,31,33,101,12,78,117,18,\
    82,5,137,45,103,90]

print find_median_deterministic(l5)

