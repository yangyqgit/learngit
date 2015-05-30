# -*- coding: gb2312 -*-

def bi_search_1(L, begin, end, value):
    '''
    ����һ�����򣨲���������arr��������iʹ��arr[i]����v���������򷵻�-1
    '''
    minindex = begin
    maxindex = end
    midindex = -1
    while(minindex < maxindex -1):
        # (minindex + maxindex) / 2 ���ܻ����
        midindex = minindex + (maxindex - minindex) / 2
        if(L[midindex] <= value):
            minindex = midindex
        else:
            maxindex = midindex
    if(L[maxindex] == value):
        return maxindex
    elif(L[minindex] == value):
        return minindex
    else:
        return -1

def bi_search_2(L, begin, end, value):
    '''
    ����һ�����򣨲���������arr������С��iʹ��arr[i]����v���������򷵻�-1 
    '''
    minindex = begin
    maxindex = end
    midindex = -1
    while(minindex < maxindex -1):
        # (minindex + maxindex) / 2 ���ܻ����
        midindex = minindex + (maxindex - minindex) / 2
        if(L[midindex] < value):
            minindex = midindex
        else:
            maxindex = midindex
    if(L[minindex] == value):
        return minindex
    elif(L[maxindex] == value):
        return maxindex
    else:
        return -1

def bi_search_3(L, begin, end, value):
    '''
    ����һ�����򣨲���������arr��������iʹ��arr[i]С��v���������򷵻�-1 
    '''
    minindex = begin
    maxindex = end
    midindex = -1
    while(minindex < maxindex -1):
        # (minindex + maxindex) / 2 ���ܻ����
        midindex = minindex + (maxindex - minindex) / 2
        if(L[midindex] < value):
            minindex = midindex
        else:
            maxindex = midindex
    if(L[maxindex] < value):
        return maxindex
    elif(L[minindex] < value):
        return minindex
    else:
        return -1

def bi_search_4(L, begin, end, value):
    '''
    ����һ�����򣨲���������arr������С��iʹ��arr[i]����v���������򷵻�-1 
    '''
    minindex = begin
    maxindex = end
    midindex = -1
    while(minindex < maxindex -1):
        # (minindex + maxindex) / 2 ���ܻ����
        midindex = minindex + (maxindex - minindex) / 2
        if(L[midindex] <= value):
            minindex = midindex
        else:
            maxindex = midindex
    if(L[minindex] > value):
        return minindex
    elif(L[maxindex] > value):
        return maxindex
    else:
        return -1


if(__name__ == '__main__'):
    L = [1,3,4,5,6,6,6,7,8]
    size = len(L)
    index = bi_search_1(L, 0, size - 1, 6);
    if(index != -1):
        print 'index=',index,'value=',L[index]
    index = bi_search_2(L, 0, size - 1, 6);
    if(index != -1):
        print 'index=',index,'value=',L[index]
    index = bi_search_3(L, 0, size - 1, 6);
    if(index != -1):
        print 'index=',index,'value=',L[index]
    index = bi_search_4(L, 0, size - 1, 6);
    if(index != -1):
        print 'index=',index,'value=',L[index]
