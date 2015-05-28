# -*- coding: gb2312 -*-
#问题一：给定一个整数N，那么N的阶乘N!末尾有多少个0？
import sys

#解法一
def factorial_1(N):
    count = 0
    for i in range(1,N + 1):
        j = i
        while(j % 5 == 0):
            count += 1
            j /= 5
    return count

#解法二
def factorial_2(N):
    count = 0
    while(N):
        count += N / 5
        N /= 5
    return count

#问题二：

#问题三：求二进制数中1的个数
#对于二进制数据，我们知道，除以一个2，原来的数字会减少一个0，
#如果除的过程中有余，那么就表示当前位置有一个1

#解法一：
def count_1(N):
    count = 0;
    while(N):
        if(N % 2 == 1):
            count += 1
        N /= 2
    return count

#解法二：
def count_2(N):
    count = 0
    while(N):
        count += N & 0x01
        N >>= 1
    return count

#解法三：
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



    
