#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.19
# try& catch
'''
try: 
	1/0
except ZeroDivisionError: # optional error name
	print "ZeroDivisionError"
except :
	print "there is an error"
else: # when there is no error, run this
	print "NoError"
finally:
	print "finally"
'''

# python: interpreted language 只看执行的部分


# 2D array [[]] =matrix

# example question
# table, find the largest size of community (上下左右联结的点)
# DFS depth-first search：把新的element放在刚才访问的后面，
# * 用hash-table mark the visited and unvisited/把数字变成2，加neighbor,去掉本来 
# complexity -> N*4 
# complexity -> N*2 N*2 因为所有的node只会被访问一次

# BFS bread-first search: 先访问最浅的一层，新element放在最后面

# complexity 
# DFS: O(n + m) IF adjacency list,  O(n*n) IF adjacency matrix
# BFS: O(n), O(b^m) b=branching factor, m=max depth

# e.g. 想知道两个community之间有没有联通，用DFS效率更高

'''
作业：这道题：Implement DFS, BFS

If there is a matrix(2D array), with elements being 1(colored) or 0(empty).
A community is defined as a bunch of colored elements connected (up,down,right,left).
write a function that gives the largest size of the community within the matrix given.
'''

import copy

def find_largest_community(matrix):
	m = copy.deepcopy(matrix) # do not change input 
	max_c = 0 # result, the largest size of the community
	for i in xrange(len(m)):
		for j in xrange(len(m[0])):
			# case1: if ele empty, mark it as visited(2)
			if m[i][j] == 0:
				m[i][j] = 2
			# case2: if ele colored, add neighbors into community count list
			else:
				max_c = dfs(m,i,j,max_c)
	return max_c


# depth first search to explore one element
def dfs(m,i,j,max_c):
	stack = [(i,j)] # stack stores the nodes that need to be explored
	c = 1 # stores the size of current community
	while stack:
		# get the x,y and the current element from the stack
		# if already visited, no need to visit again (save steps)
		curr = stack.pop()
		while (m[curr[0]][curr[1]] == 2):
			#if stack is empty, return
			if stack:
				curr = stack.pop()
			else: 
				return max_c
		x = curr[0]
		y = curr[1]
		# mark the current element as visited
		if m[x][y] != 2:
			m[x][y] = 2
		# print x,y

		# stack extend: check neighbors and add valid ones to the stack
		# up element x,y-1
		if y-1 >= 0: # check up boundary
			if m[x][y-1] == 1: # only when the elements is colored(1), add
				c += 1
				stack.append((x,y-1)) # explore this node ....
		# down element x,y+1
		if y+1<len(m[0]):
			if m[x][y+1] == 1:
				c += 1
				stack.append((x,y+1))
		# right element x+1,y
		if x+1<len(m):
			if m[x+1][y]==1:
				c+=1
				stack.append((x+1,y))
		# left element x-1,y
		if x-1>=0:
			if m[x-1][y]==1:
				c+=1
				stack.append((x-1,y))

	if c>max_c:
		max_c=c
	return max_c


print(find_largest_community([[0,1],[1,1]])) #->3
print(find_largest_community([[0,1,1,0],[1,0,1,1],[1,0,1,0]])) #-> 5
print(find_largest_community([[1,1,1,1],[0,0,1,0],[1,0,1,1]])) #->7

# (0, 0) (0, 1) (0, 2) (1, 2) (2, 2) (2, 3) (0, 3) (2, 0)
# this approach is DFS or BFS? depend on direction -> depend on pop, this is DFS/stack, pop(0) is BFS/queue



# suggestion: 
# 1. 等于旁边要有一个空格
# 2. 用deepcopy, copy 不要改input
