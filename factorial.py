# -*- coding: gb2312 -*-
#����һ������һ������N����ôN�Ľ׳�N!ĩβ�ж��ٸ�0��
import sys

#�ⷨһ
def factorial_1(N):
    count = 0
    for i in range(1,N + 1):
        j = i
        while(j % 5 == 0):
            count += 1
            j /= 5
    return count

#�ⷨ��
def factorial_2(N):
    count = 0
    while(N):
        count += N / 5
        N /= 5
    return count

#�������

#�������������������1�ĸ���
#���ڶ��������ݣ�����֪��������һ��2��ԭ�������ֻ����һ��0��
#������Ĺ��������࣬��ô�ͱ�ʾ��ǰλ����һ��1

#�ⷨһ��
def count_1(N):
    count = 0;
    while(N):
        if(N % 2 == 1):
            count += 1
        N /= 2
    return count

#�ⷨ����
def count_2(N):
    count = 0
    while(N):
        count += N & 0x01
        N >>= 1
    return count

#�ⷨ����
def count_3(N):
    count = 0
    while(N):
        N &= (N - 1)
        count += 1
    return count

if(__name__ == '__main__'):
    #N = int(sys.argv[1])
    print factorial_1(10)
    print factorial_2(10)
    print count_1(10)
    print count_2(10)
    print count_3(10)



    
