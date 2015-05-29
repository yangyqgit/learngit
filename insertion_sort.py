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
	sort_insertion(L)
	end = datetime.datetime.now()
	print '---------------------------------------'
	print 'sorted:',L
	print '---------------------------------------'
	print 'sort_insertion time escape:',(end - start).microseconds, 'microseconds'
	print '---------------------------------------'



