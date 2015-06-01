# -*- coding: gb2312 -*-
import sys
import random
import datetime
def max_heapify(L, i, N):
	temp = L[i]
	l = 2 * i + 1
	while(l < N):
		if(l + 1 < N and L[l + 1] > L[l]):
			l += 1
		if(L[l] <= temp):
			break
		L[i] = L[l]
		i = l
		l = 2 * i + 1
	L[i] = temp

def build_max_heap(L):
	'''
	当用数组表示存储了n个元素的堆时,叶子结点的下标是floor(n/2) + 1,floor(n/2) + 2,...,n
	'''
	for i in range(size / 2 - 1, -1, -1):
		max_heapify(L, i, size)


def heap_sort(L):
	size = len(L)
	if(size > 0):
		build_max_heap(L)
		for i in range(size - 1, -1, -1):
			temp = L[0]
			L[0] = L[i]
			L[i] = temp
			max_heapify(L, 0, i)

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
	print '---------------------------------------'
	print 'unsort:',L
	start = datetime.datetime.now()
	heap_sort(L)
	end = datetime.datetime.now()
	print '---------------------------------------'
	print 'sorted:',L
	print '---------------------------------------'
	print 'heap_sort time escape:',(end - start).microseconds, 'microseconds'
	print '---------------------------------------'

