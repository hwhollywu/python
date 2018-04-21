#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.22 作业
# median of two sorted array
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# there are two sorted arrays num1 and num2, size m and n.
# find the median of two sorted arrays. the overall run time
# should be O(log(m+n))

# [1,3],[2] -> 2.0
# [1,2],[3,4] -> 2。5

# combine and sort 2 arrays -> find median

import copy

def find_median_of_2_arrays(list1, list2):
	# 1. combine lists
	listy = copy.deepcopy(list1)
	listy.extend(list2) 
	# 2. sort lists -> complexity O(m+n log m+n)
	sorted_listy = merge_sort(listy)
	# 3. return median
	leng = len(sorted_listy)
	if (leng % 2 == 0):
		return (sorted_listy[leng / 2 - 1] + sorted_listy[leng / 2])/ (2 * 1.0)
	else:
		return sorted_listy[leng / 2]


def merge(left,right):
	l0 = copy.deepcopy(left)
	l1 = copy.deepcopy(right)
	merged =[]
	while l0 and l1: # stop if one of lists become empty
		if l0[0] < l1[0]:
			merged.append(l0.pop(0))
		else:
			merged.append(l1.pop(0))
	merged.extend(l0)
	merged.extend(l1)
	return merged


def merge_sort(lists):
	if len(lists) <= 1:
		return lists
	mid = len(lists) / 2
	return merge(merge_sort(lists[:mid]), merge_sort(lists[mid:]))


print(merge_sort([3,4,5,6,2,1]))
print(find_median_of_2_arrays([1,3],[2]))
print(find_median_of_2_arrays([1,2],[3,4]))





# puzzle
#  search a 2 D array
# https://leetcode.com/problems/search-a-2d-matrix/description/
# write an efficient algorithm that searches for a value 
# in mxn matrix. 