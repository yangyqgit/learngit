import math

def probability2(origin, current, sum, L):
    if(current == 1):
        L[sum - origin] += 1
    else:
        for i in range(1, 7):
            probability2(origin, current - 1, i + sum, L)

def probability1(number, L):
    for i in range(1, 7):
        probability2(number, number,  i,  L)

    
def printprobability(number):
    if(number < 1):
        return
    min_sum = number
    max_sum = 6 * number
    L = [0 for x in range(0, max_sum - min_sum + 1)]
    total = math.pow(6, number)
    probability1(number, L)
    for x in range(min_sum, max_sum + 1):
        print x, ':' ,L[x - number] / total * 100, '%'


if( __name__== '__main__'):
    printprobability(5)
