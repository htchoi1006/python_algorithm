'''
문제

임의의 N개의 숫자가 입력으로 주어진다. 
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한개의 수인 M이 주어지면 
이분검색으로 M이 정렬된 상태에서 몇번째에 있는지 구하는 프로그램을 작성하라.


'''


import sys
sys.stdin = open("input.txt", "r")

n, num = map(int, input().split())
a = list(map(int, input().split()))
a.sort()


lt, rt = 0, len(a)-1
mid = (lt+rt)//2
answer = 0

while(True):
    if num == a[mid] :
        answer = mid + 1
        break

    elif num < a[mid]:
        rt = mid - 1
        mid = (lt+rt)//2

    else:
        lt = mid + 1
        mid = (lt+rt)//2


print(answer)




    



 




