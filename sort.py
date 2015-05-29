# -*- coding: gb2312 -*-
import random
import datetime
import sys


def sort_insertion(L):
	for i in range(1,len(L)):
		key = L[i]
		j = i - 1
		while(j >= 0 and L[j] > key):
			L[j + 1] = L[j]
			j = j - 1
		L[j + 1] = key

def merge(L, begin, mid, end, Temp):
	i = begin
	j = mid + 1
	k = 0
	while(i <= mid and j <= end):
		if(L[i] <= L[j]):
			Temp[k] = L[i]
			i += 1
		else:
			Temp[k] = L[j]
			j += 1
		k += 1
	while(i <= mid):
		Temp[k] = L[i]
		i += 1
		k += 1
	while(j <= end):
		Temp[k] = L[j]
		j += 1
		k += 1
	for x in range(0, k):
		L[x + begin] = Temp[x]


def sort_merge(L, begin, end, Temp):
	if(begin < end):
		mid = (end + begin) / 2
		sort_merge(L, begin, mid, Temp)
		sort_merge(L, mid + 1, end, Temp)
		merge(L, begin, mid, end, Temp)


if(__name__ == '__main__'):
	if(len(sys.argv) < 2):
		print '\nplease specify the size of list!\n'
		sys.exit()
	size = int(sys.argv[1])
	if(size <= 0):
		print '\nThe size of list must greater than zero!\n'
		sys.exit()
	L=[]
	M=[]
	T=[]
	for i in range(0,size):
		L.append(random.randrange(0,10000))
		M.append(L[i])
		T.append(0)
	print '---------------------------------------'
	#print 'unsort:',L
	start = datetime.datetime.now()
	sort_insertion(L)
	end = datetime.datetime.now()
	print '---------------------------------------'
	#print 'sorted:',L
	print '---------------------------------------'
	print 'sort_insertion time escape:',(end - start).microseconds, 'microseconds'
	print '---------------------------------------'
	start = datetime.datetime.now()
	sort_merge(M, 0, len(M) - 1, T)
	end = datetime.datetime.now()
	print '---------------------------------------'
	#print 'sorted:',M
	print '---------------------------------------'
	print 'sort_merge time escape:',(end - start).microseconds, 'microseconds'
	print '---------------------------------------'



