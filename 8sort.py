#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.21 Sorting: write an algorithm to sort a random list of numbers 

# http://bigocheatsheet.com/

import copy

# 1. insertion sort O(n^2)
def insert_sort(lists):
	for i in xrange(1,len(lists)):
		key = lists[i]
		j = i - 1
		while j >= 0: 
			if lists[j] > key:
				lists[j + 1] = lists[j]
				lists[j] = key
				j -= 1
	return lists

# 2. bubble sort O(n^2)
def bubble_sort(lists):
	l = copy.deepcopy(lists)
	for i in xrange(len(l)):
		for j in xrange(i+1,len(l)):
			if l[j] > l[i]:
				t = l[j]
				l[j] = l[i]
				l[i] = t
	return l


# 3. shell sort : best O(nlogn), worst O(2nlogn) depends on gap sequence
# if gap == 1, same as insertion sort
def shell_sort(lists):
	step = 2
	group = len(lists) / step
	while group > 0:
		for i in xrange(0,group):
			j = i + group 
			while j < len(lists):
				k = j - group
				key = lists[j]
				while k >= 0:
					if lists[k] > key:
						lists[k + group] = lists[k]
						lists[k] = key
					k -= group
				j += group
			group /= step
	return lists

# 4. selection sort always O(n^2)
def selection_sort(lists):
	l = copy.deepcopy(lists)
	for i in xrange(0 , len(l)):
			mini = i
		for j in xrange(i + 1, len(l)):
			if l[i] > l[j]:
				mini = j
		t = l[i]
		l[i] = l[mini]
		l[mini] = t
	return l


# 5. merge sort time O(nlogn), space O(n)

def merge(left,right):
	l0 = copy.deepcopy(left)
	l1 = copy.deepcopy(right)
	merged =[]
	while l0 and l1: # stop if one of lists become empty
		if l0[0] < l1[0]:
			merged += l0.pop()
		else:
			merged += l1.pop()
	merged.extend(l0)
	merged.extend(l1)
	return merged


def merge_sort(lists):
	if len(lists) <= 1:
		return lists
	mid = len(lists) / 2
	return merge(mergesort(lists[:mid]),mergesort(lists[mid:]))

'''
explain: why complexity of merge sort is nlogn
[3,1,4,2] -> [1,2,3,4] cn
[3,1][4,2] -> [1,3][2,4] (cn/2)*2
[3][1][4][2] -> [3][1][4][2] (cn/4)*4
每次都是n,总共要分logn次 4个element, 2^2=4, 分两次

split O(1)
recurse 2*T(n/2)
merge O(n)
'''

# 6. quick sort time O(nlogn), space O(logn)

def partition(lists,left,right):
	i = left - 1
	pivot = lists[right]
	for j in range(left, right):
		if lists[j] <= pivot:
			i = i+1
			lists[i],lists[j] = lists[j],lists[i] # swap
	lists[i+1],lists[right] = lists[right], lists[i+1]
	return (i+1)


def quick_sort(lists,left,right):
	if left >= right:
		return lists
	pi = partition(lists,left,right)
	quick_sort(lists, left, pi-1)
	quick_sort(lists, pi+1, right)
	return lists

'''
partition O(n)
recurse 2*T(n/2)
put together O(1) 
* l.extend() complexity O(n)

example
[4,3,7,2,5,1,10]
[3,2,1,4,7,5,10]
4, [3,2,1][7,5,10]
3,[2,1],[],  7,[5],[10]
  2,[1]，[]
 3,[1,2] []  7,[5][10]
 [1,2,3],[5,7,10]
 [1,2,3,4,5,7,10]

1.
 if choose good pivot, split log n 
 if bad, split n  -> O(n^2)

2. randomized algorithm : 随便取的pivot
in-place: space O(logn)

'''


# 7. heap sort time O(nlogn), space O(1)
# max heap: full binary tree, parent node is greater than children node

def heapify(lists, n, i):
	largest = i # root 
	l = 2*i+1 # left
	r = 2*i+2 # right
	# See if left child of root exists and is 
	# greater than root
	if l < n and lists[i] < lists[l]:
		largest = l
	# See if right child of root exists and is
    # greater than root
	if r < n and lists[largest] < lists[r]:
		largest = r
	# change root if needed
	if largest != i:
		lists[i], lists[largest] = lists[largest], lists[i]
		heapify(lists, n, largest)

def heap_sort(lists):
	# build a maxheap
	for i in xrange(len(lists), -1, -1):
		heapify(lists, len(lists), i)
	# extract element
	for i in xrange(len(lists),0,-1):
		lists[i],lists[0]=lists[0],lists[i] #swap
		heapify(lists, i, 0)






