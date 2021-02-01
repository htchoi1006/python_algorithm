# 문제
# 자연수 n을 입력받았을 때, 1부터 n 까지 소수의 개수를 출력하는 프로그램을 작성하라.
# 2 <= n <= 20000 

import sys
sys.stdin = open("input.txt", "r")
n = int(input())

ch = [0]*(n+1)
cnt = 0

for i in range(2, n+1):    
    if(ch[i] == 0):
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)

