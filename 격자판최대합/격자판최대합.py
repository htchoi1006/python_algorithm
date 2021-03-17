'''
문제

5*5 격자판에 다음과 같은 숫자가 적혀있다.

10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력한다.



'''


import sys
sys.stdin = open("input.txt", "r")


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]  #격자판의 한 줄을 리스트로 읽어들이는걸 n번 반복


ans = -2147000000

for i in range(5):  #행끼리 / 열끼리 덧셈하는 for문
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]  #한 행 덧셈
        sum2 += a[j][i]  #한 열 덧셈
        
    if(sum1 > ans):
        ans = sum1
    if(sum2 > ans):
        ans = sum2


sum1 = sum2 = 0

for i in range(n):   #대각선 덧셈하는 for문
    sum1 += a[i][i]  #왼쪽 위 -> 오른쪽 아래 대각선
    sum2 += a[i][n-i-1]  #오른쪽 위 -> 왼쪽 아래 대각선

    if(sum1 > ans):
        ans = sum1
    if(sum2 > ans):
        ans = sum2


print(ans)
 


    




