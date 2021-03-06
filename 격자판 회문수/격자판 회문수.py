'''
문제

1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 
격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하라.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말한다.

2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5


'''


import sys
sys.stdin = open("input.txt", "r")

a = [list(map(int, input().split())) for _ in range(7)]  #격자판의 한 줄을 리스트로 읽어들이는걸 n번 반복
cnt = 0

#---------------------------------------
#같은 행 내에서 회문 검사하기
#5자리 수끼리 묶어서 검사해야하기 때문에 0,1,2 열까지만 for문이 돈다.
for i in range(3):        #열
    for j in range(7):    #행
        tmp = a[j][i:i+5]      #다섯자리 숫자를 tmp에 입력
        if tmp == tmp[::-1]:    #[::-1]은 역순으로 배열하는 것
            cnt += 1         
#---------------------------------------
#---------------------------------------
#같은 열 내에서 회문 검사하기
        for k in range(2):    #회문이 5글자이므로 2로 나눈 몫만큼만 for문을 돈다
            if a[i+k][j] != a[i+5 -k-1][j]:    #앞에서부터 검사한 값과 뒤에서부터 검사한 값을 비교, 가운데는 중심이므로 검사할 필요 없다
                break       #회문이 아닐 경우 break
            
        else:
            cnt += 1




print(cnt)


 




