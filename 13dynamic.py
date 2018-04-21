#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.27

'''

https://www.cs.cmu.edu/~15451/lectures/lec08-dp1.pdf


dynamic programming: 
solving a complex problem by breaking it down into a collection of simpler subproblems
and save the solutions for subproblems (recursion)
== divide and conquer

'the curse of dimensionality': 要使Model可信，data必须exponentially增长，但是很难

'dynamic' Bellman 比较优美/文学素养
requirement: 比较少的subproblems


https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
e.g. Fibonacci program Time Complexity: T(n) = T(n-1) + T(n-2)

Functional: Haskell
OOP: java
'''

'''
e.g. Longest Common Subsequence

ABAZDC
BACBAD
return ABAD 长度4

最后两个是一样的情况 


def LCS(i,j): # i,j len of list1,list2
# case 0: i or j =0, =0
# case 1: 如果末尾不一样，A-C, 看AB-BAC, ABA-BA两者之间的最优解
# case 2: 如果末尾一样，A-A, 前面的最优解+1 
# 建立长度的 2D array ,如果结尾字母不一样上走或左走(一样的长度)，
# 字母一样的话就左上跳着走,记录match的结尾字母

# 思路：Botton-Up VS Top-Down
# 思路：用2Darray 记下来subproblems 的 solution

complexity: O(mn)
'''

listy1 = "ABAZDC"
listy2 = "BACBAD" # should return ABAD

# input: String1, length of string1, string2, length of string2
def LCS(l1,i,l2,j,arr):
	# base case
	if (i == 0) or (j == 0): 
		return 0
	# use 2D matrix to record the solutions
	# return solution directly instead of continue recursing
	if arr[i][j]:
		return arr[i][j]
	# case 1: same end
	if l1[i - 1] == l2[j - 1]: # list index = len - 1
		result = 1 + LCS(l1,i-1,l2,j-1,arr)
	# case 2: different end
	else:
		result = max(LCS(l1,i-1,l2,j,arr),LCS(l1,i,l2,j-1,arr))
	# record sub-solutions
	arr[i][j] = result
	# print arr
	return result

def LCS_init(l1,l2):
	# initialize 2D array with 0
	matrix = [[0 for x in range(len(l1) + 1)] 
					for y in range(len(l2) + 1)]
	# fill the array with length of LCS
	LCS(l1, len(l1), l2, len(l2), matrix)
	
	list_result = []
	# reverse the array to find matching endings 
	i = len(l1)
	j = len(l2)
	while i > 0 and j > 0:
		curr = matrix[i][j]
		# case 1: if char in l1 and l2 matches:
		if l1[i-1] == l2[j-1]:
			# add char
			list_result.append(l1[i-1])
			i -= 1
			j -= 1
		# case 2: does not match, move leftwards 
		elif matrix[i-1][j] > matrix[i][j-1]:
			i -= 1
		# case 2: does not match, move upwards 
		else: 
			j -= 1

	# list to string
	string_result = ''.join(list_result)
	# reverse the string
	return string_result[::-1]


print(LCS_init(listy1,listy2))



'''
e.g. The Knapsack problem
value-size
价值=value/size

2^n 次复杂度 要不要放

given time

return total value

V(k,b) k代表前k个物品，B代表bag的大小

'''

# input: list of lists [name, value, time]
k1=[[A,7,3],[B,9,4],[C,5,2],[D,12,6],[E,14,7],[F,6,3],[G,12,5]]




