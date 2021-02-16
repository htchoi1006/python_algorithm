'''
문제

문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만든다. 
만들어진 자연수와 그 자연수의 약수의 개수를 출력하라. 

만약 't0e0a1c2h0er'에서 숫자만 추출하면 0,0,1,2,0이고 이것을 자연수로 만들면 120이다. 
출력은 120을 출력하고 다음줄에 120의 약수의 개수를 출력한다.

'''

import math
import sys
sys.stdin = open("input.txt", "r")

word = input()
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
res = ""


for i in word:
    if(i in num):
        res += i
    
res = int(res)

print(res)      # 자연수 출력


l = [0]*(res+1)

test = []

cnt = 1

for i in range(2, res+1):
    if(res%i == 0):
        cnt += 1
        test.append(i)

print(test)
print(cnt)




 


    




