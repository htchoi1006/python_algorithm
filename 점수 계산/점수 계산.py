'''
문제

여러개의 OX 문제로 만들어진 시험에서 연속적으로 답을 맞히는 경우에는 가산점을 주기 위해서 다음과 같이 점수 계산을 하기로 했다. 
1번 문제가 맞는 경우에는 1점으로 계산한다. 앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산한다. 
또한 연속으로 문제의 답이 맞는 경우에서 두번째 문제는 2점, 세번째 문제는 3점, K번째 문제는 k점으로 계산한다. 틀린 문제는 0점으로 계산한다.


시험 문제의 채점 결과가 주어졌을 때, 총 점수를 계산하는 프로그램을 작성하시오.
'''

import math
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))

score = 0
cnt = 0

for i in a:
    if(i == 0):
        cnt = 0
    else:
        cnt += 1
        score += cnt

print(score)

 


    




