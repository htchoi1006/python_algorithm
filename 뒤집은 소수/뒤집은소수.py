'''
문제

n개의 자연수가 입력되면 각 자연수를 뒤집은 후 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하라.
뒤집는 함수인 def reverse(x)와 소수인지를 확인하는 함수 def isPrime(x)을 반드시 작성하라.
'''

import math
import sys
sys.stdin = open("input.txt", "r")

def reverse(x):
    res = 0
    while(x > 0):
        t = x%10
        res = res*10 + t 
        x = x//10
    return res


def isPrime(x):
    if(x == 1):
        return False
    cnt = 0
    for i in range(2, int(math.sqrt(x))+1):
        if(x%i == 0):
            return False
    else:
        return True
            
    

n = int(input())
a = list(map(int, input().split()))

for i in a:
    tmp = reverse(i)
    if (isPrime(tmp)):
        print(tmp)







