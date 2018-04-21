#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.21 作业

# 看一个图能不能画圈
# DFS每一个点看能不能通过>1条edge回到自己
# DFS每一个点看能不能visit一个已经visit过且不是自己Parent的点

graph1 = [(1,[2]),(2,[1,3,4]),(3,[2,7]),(4,[2,5]),(5,[4,6]),(6,[5]),(7,[3])] # -> false
graph2 = [(1,[2]),(2,[1,3,4]),(3,[2,4,7]),(4,[2,3,5]),(5,[4,6]),(6,[5]),(7,[3])] # -> true
graph3 = [(1,[2]),(2,[1,3,4]),(3,[2,7]),(4,[2,5]),(5,[4,6]),(6,[5,7]),(7,[3,7])] # -> true


def find_loop(graph):
	g = dict(graph) 
	visited = dict() # new dict -> set
	for v in graph:
		# mark every vertex as unvisited in the beginning
		visited[v[0]] = False 
	stack = [graph[0]] # DFS start with the first vertex
	while stack:
		curr = stack.pop()
		# check if the curr vertex have been visited
		if visited[curr[0]] == False:
			visited[curr[0]] = True 
		else:
			return True
		for n in curr[1]: # for each edge
			# only append new vertex if it's not parent vertex 
			if visited[n] == False:
				node = (n, g[n])
				stack.append(node)
	return False

print(find_loop(graph1))
print(find_loop(graph2))
print(find_loop(graph3))


# recursive version
def loopy(find_loop, g, visited, vertex, parent):
	if find_loop[0]: 
		return
	# mark the current vertex as visited
	visited[vertex[0]] = True
	# for each edge in the vertex
	for n in vertex[1]:
		# base case: if visit a visited vertex and it is not the parent
		if (visited[n] == True) and (n != parent):
			find_loop[0] = True
			return 
		# recursive case:
		if not visited[n]:
			loopy(find_loop, g, visited, (n,g[n]), vertex[0])


def find_loop_recursive(graph):
	find_loop = [False] # why need to be a list??? does not work as a boolean
	visited = dict() 
	for v in graph:
		visited[v[0]] = False 
	# search each vertex
	for v in graph: 
		if not visited[v[0]]:
			# initiate parent as root
			loopy(find_loop, dict(graph), visited, v, v[0])
		if find_loop[0]:
			break
	return find_loop[0]


print(find_loop_recursive(graph1))
print(find_loop_recursive(graph2))
print(find_loop_recursive(graph3))