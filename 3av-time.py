#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# av -> autonomous vehicle

# Given a list of tuples that represent the time 
# when cars are on road, return the max number of 
# concurrent cars on road at any time of the day


# [(3, 5), (4, 6)] -> 2
# [(3, 5), (0, 24), (4, 6)] -> 3
# [(2, 5), (7, 10)] -> 1

def av(lst):
	max_c = 0
	for h in range(24): 
		c = 0
		for s in lst:
			# print 's', s, 'h', h, 's[0]<=h', s[0]<=h, 's[1]>=h', s[1]>=h
			if (s[0]<=h) & (s[1]>=h):
				# print 'enter'
				c+=1
		if c > max_c:
			max_c=c
	return max_c

print(av([(3, 5), (4, 6)]))
print(av([(3, 5), (0, 24), (4, 6)]))
print(av([(2, 5), (7, 10)]))


def av_dict(lst):
	# make a dict, count the number of cars in 24 hours, e,g. {0:0,1:0...23:0}
	dicty={}
	for i in xrange(24):
		dicty[i]=0
	# print 'init-dict', dicty
	for s in lst:
		start=s[0]
		i = start
		end=s[1]
		while i <= end:
			dicty[i]+=1
			i+=1
	# print 'load-dict', dicty
	#iterate through the dict, get the max one
	max_c = 0
	for v in dicty.values():
		if v>max_c:
			max_c=v
	return max_c


print(av_dict([(3, 5), (4, 6)]))
print(av_dict([(3, 5), (0, 23), (4, 6)]))
print(av_dict([(2, 5), (7, 10)]))


