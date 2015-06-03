# -*- coding: gb2312 -*-

import random
import datetime
import sys

def counting_sort(L, n, k):
	T = []
	for i in range(0, k):
		T.append(0)
	for i in L:
		T[i] += 1
	j = 0
	for i in range(0, k):
		while(T[i] > 0):
			L[j] = i
			T[i] -= 1
			j += 1

if(__name__ == '__main__'):
	if(len(sys.argv) < 2):
		print '\nplease specify the size of list!\n'
		sys.exit()
	size = int(sys.argv[1])
	if(size <= 0):
		print '\nThe size of list must greater than zero!\n'
		sys.exit()
	L=[]
	T=[]
	for i in range(0,size):
		L.append(random.randrange(0,100))
		T.append(0)
	print '---------------------------------------'
	print 'unsort:',L
	start = datetime.datetime.now()
	counting_sort(L, size, 100)
	end = datetime.datetime.now()
	print '---------------------------------------'
	print 'sorted:',L
	print '---------------------------------------'
	print 'time escape:',(end - start).microseconds, 'microseconds'
	print '---------------------------------------'
