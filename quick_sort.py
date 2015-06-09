# -*- coding: gb2312 -*-
import sys
import random
import datetime

def partition(L, b, e):
	i = b
	j = e
	temp = L[i]
	while(i < j):
		while(i < j and L[j] >= temp):
			j -= 1
		if(i < j):
			L[i] = L[j]
			i += 1
		while(i < j and L[i] < temp):
			i += 1
		if(i < j):
			L[j] = L[i]
			j -= 1
	L[i] = temp
	return i

def random_partition(L, b, e):
	r = random.randrange(b, e)
	L[e],L[r] = L[r],L[e]
	j = b - 1
	for i in range(b, e):
		if(L[i] <= L[e]):
			j += 1
			L[i],L[j] = L[j],L[i]
	j += 1
	L[j],L[e] = L[e],L[j]
	return j

def quick_sort(L, b, e):
	if(b < e):
		i = partition(L, b, e)
		quick_sort(L, b, i - 1)
		quick_sort(L, i + 1, e)

def random_quick_sort(L, b, e):
	if(b < e):
		i = random_partition(L, b, e)
		random_quick_sort(L, b, i - 1)
		random_quick_sort(L, i + 1, e)

if(__name__ == '__main__'):
	if(len(sys.argv) < 2):
		print '\nplease specify the size of list!\n'
		sys.exit()
	size = int(sys.argv[1])
	if(size <= 0):
		print '\nThe size of list must greater than zero!\n'
		sys.exit()
	L=[]
	for i in range(0,size):
		L.append(random.randrange(0,10000))
	M = L
	print '---------------------------------------'
	print 'unsort:',L
	time1 = datetime.datetime.now()
	quick_sort(L, 0, size - 1)
	time2 = datetime.datetime.now()
	random_quick_sort(M, 0, size - 1)
	time3 = datetime.datetime.now()
	print '---------------------------------------'
	print 'sorted:',L
	print '---------------------------------------'
	print 'time escape:',(time2 - time1).microseconds,(time3 - time2).microseconds, 'microseconds'
	print '---------------------------------------'
