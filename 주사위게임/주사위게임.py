'''
문제

1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

규칙1) 같은 눈이 3개가 나오면 10,000원+(같은눈)*1,000원의 상금을 받는다.
규칙2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은눈)*100원의 상금을 받는다.
규칙3) 모두 다른 눈이 나오는 경우에는 (그중 가장 큰 눈)*100원의 상금을 받는다.

N명이 주사위게임에 참여했을 때, 가장 많은 상금을 받는 사람의 상금을 출력하는 프로그램을 작성하시오.
'''

import math
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)

    if(a == b and b == c):
        money = 10000 + a*1000
    elif(a == b or a == c):
        money = 1000 + a*100
    elif(b == c):
        money = 1000 + b*1000
    else:
        money = c*100

    if(money > res):
        res = money


print(res)


    




