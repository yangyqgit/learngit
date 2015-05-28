# -*- coding: cp936 -*-
#求最大公约数

def gcd_1(x,y):
    if(y == 0):
        return x
    else:
        return gcd_1(y, x % y)

def gcd_2(x,y):
    if(x < y):
        return gcd_2(y,x)
    if(y == 0):
        return x
    else:
        return gcd_2(x - y, y)

if(__name__ == '__main__'):
    x = 285714
    y = 999999
    z = gcd_2(x,y)
    print x / z,'/',y / z
