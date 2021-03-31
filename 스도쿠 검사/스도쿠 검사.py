'''
문제

스도쿠는 매우 간단한 숫자 퍼즐이다. 
9*9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3*3 크기의 보드에 1부터 9까지의 숫자가
중복없이 나타나도록 보드를 채우면 된다. 

완성된 9*9 크기의 스도쿠가 주어지는데, 정확하게 풀었으면 YES를 잘못 풀었으면 NO를 출력하라.

'''


import sys
sys.stdin = open("input.txt", "r")

a = [list(map(int, input().split())) for _ in range(9)]  #격자판의 한 줄을 리스트로 읽어들이는걸 n번 반복

def check(a):
    #--------------------------------------
    #행과 열을 쭉 돌면서 탐색

    for i in range(9):  #9행
        ch1 = [0]*10   #행을 체크하기 위한 리스트 (1부터 9까지 숫자가 모두 있는지)
        ch2 = [0]*10   #열을 체크하기 위한 리스트
        for j in range(9):  #9열
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    #---------------------------------------

    #---------------------------------------
    #3*3 정사각형 그룹 한개씩 탐색

    #9개의 그룹을 탐색하겠다는 이중포문
    for i in range(3): 
        for j in range(3):
            ch3 = [0]*10
            
            #한 그룹 내에서 9개의 칸을 탐색하겠다는 이중포문
            for k in range(3):
                for l in range(3):
                    ch3[a[i*3 + k][j*3 + l]] = 1   #i*3+k -> 행, j*3 + l -> 열

            if sum(ch3) != 9:
                return False
    
    return True




if check(a):
    print("YES")
else:
    print("NO")

 




