#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.23 作业 quick sort

import copy, random


def quick_sort(l):
	# base case: empty list
	if not l:
		return []
	# recursive case
	# l = copy.deepcopy(listy)
	pivot_num = random.randint(0,len(l)-1) 
	pivot = l[pivot_num]
	l.pop(pivot_num)
	# partition
	index = -1 # number of elements that are less than pivot
	for i in xrange(0,len(l)):
		if l[i] <= pivot:
			# differentiate index and i
			index += 1
			if i != index: 
				l[i], l[index] = l[index], l[i] #swap
	l.insert(index+1, pivot)
	lesser = l[:index+1]
	greater = l[index+2:] # pivot already inserted

	return quick_sort(lesser) + [l[index+1]] + quick_sort(greater)

print(quick_sort([3,2,1]))
print(quick_sort([4,3,7,2,5,1,10]))



