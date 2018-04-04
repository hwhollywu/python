#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.15 python
# O(1): constant complexity
#	for i in range(10):
# O(n): 
#	for i in range(n)

# O(sqrt(n)) ???
# O(n)

# dict: O(1)
# d=dict(), d={}
# set([])
# s=set()
# 和list区别：位置可以对调,无序的List
# set -> add(), remove(), O(1)
# list remove O(n)

# -> 简化two_sum function从O（n^2）到O(n)
# time complexity -> O(n),O(n^2)
# space complexity -> 内存
# -> 简化majority 从timeO(n),spaceO(n) -> spaceO(1)
# -> (用max count, curr count, max num)
# -> 用Binary search O(logn),


def sumup(lst,t): #time O(n)
	s=set([])
	for i in xrange(len(lst)):
		if (t-lst[i]) not in s:
			s.add(lst[i])
		else:
			return True
	return False


print(sumup([1,2,3],4))
print(sumup([2,3,4],2))
print(sumup([1,1,2,5],4))
print(sumup([1,0,2,1,2,5],4))


def majority_set(listy): #time O(n), space O(1)
	max_count=1
	curr_count=1
	max_number=listy[0]
	for i in xrange(1,len(listy)):
		if listy[i] != listy[i-1]:
			# print 'listy-i: ', listy[i]
			# print 'curr_count: ', curr_count
			# print 'max_c: ', max_count
			# print 'max_num', max_number
			curr_count=1
		else:
			curr_count+=1
			if curr_count > max_count:
				max_count=curr_count
				max_number=listy[i]

	if max_count > len(listy)/2:
		return max_number
	else:
		return -1


print(majority_set([1,1,1,1,4,5]))
print(majority_set([2,2,3,4]))
print(majority_set([1,1,2,2,2,2,2,3,4]))
print(majority_set([2,2,2,2]))
print(majority_set([1,1,1,4,5,6]))

def majority_bs(listy):
	# for the sets that have a majortity number,
	# the number must be at the midpoint
	mid = len(listy)/2




