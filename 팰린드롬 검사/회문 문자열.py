'''
문제

N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면 YES를 출력하고,
회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할때는 대소문자를 구분하지 않는다. 

'''

import math
import sys
sys.stdin = open("input.txt", "r")

n = int(input())

stack = []

for i in range(n):
    word = input()
    word = word.upper()

    size = len(word)

    for j in range(size//2):
        if(word[j] != word[-1-j]):
            print(i+1, "NO")
            break
            
    else:
        print(i+1, "YES")



 


    




