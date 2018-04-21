#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 3.20 作业
# find the deepest depth of a given tree
# e.g.  [(1,[2,7,8]),(2,[3,6]),(7,[]),(8,[9,12]),(3,[4,5]),(6,[]),(4,[]),(5,[]),(8,[9,12]),(9,[10,11]),(12,[]),(10,[]),(11,[])] ->  return 3

tree1=[(1,[2,7,8]),(2,[3,6]),(7,[]),(8,[9,12]),(3,[4,5]),(6,[]),(4,[]),(5,[]),(8,[9,12]),(9,[10,11]),(12,[]),(10,[]),(11,[])] 

def find_tree_depth(tree):
	t = dict(tree)
	stack = [tree[0]] # initiate a stack for DFS  
	max_depth = 0 # result
	dicty = {} # new dict:{node-number:depth}
	dicty[tree[0][0]] = 0 # initiate new dict with root depth = 0
	while stack:
		curr = stack.pop()
		for n in curr[1]: # for each path in a node
			dicty[n] = dicty[curr[0]] + 1 # depth of children = depth of parent + 1
			node = (n,t[n])
			stack.append(node) 
			# if max_depth < dicty[node]:
				# max_depth = dicty[node]
	# find the deepest in dicty
	for k,v in dicty.items():
		if v > max_depth:
			max_depth = v

	return max_depth


print(find_tree_depth(tree1))


# recursion version
def dfs_depth(tree, node):
	# base case: if empty leave, node[1]=[]
	if not node[1]:
		return 0
	# recursive case: 
	max_depth = 0
	for child in node[1]: # e.g. 2,7,8...
		child_depth = dfs_depth(tree, (child,tree[child])) + 1
		if child_depth > max_depth:
			max_depth = child_depth
	return max_depth


def find_tree_depth_recursion(tree):
	return dfs_depth(dict(tree), tree[0]) # dfs(tree, root node)

print(find_tree_depth_recursion(tree1))

# complexity of graph: n=node number, m=edge number
# tree is a special graph: m=n-1
# 每个Node只访问一次，所以O(n)
# random graph: both BFS& DFS O(V+E) 可证明







