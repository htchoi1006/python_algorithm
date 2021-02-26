'''
문제

오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하라.

- 입력설명
첫번째 줄에 첫번째 리스트의 크기 n이 주어진다.
두번째 줄에 n 개의 리스트 원소가 오름차순으로 주어진다.
세번째 줄에 두번째 리스트의 크기 m이 주어진다.
네번째 줄에 m 개의 리스트 원소가 오름차순으로 주어진다. 
각 리스트의 원소는 int형 변수의 크기를 넘지 않는다. 

- 출력설명
오름차순으로 정렬된 리스트를 출력한다.

'''
# ---------버전 1 ---------# 
# sorted 함수 사용

# import sys
# sys.stdin = open("input.txt", "r")


# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))


# print(sorted(a+b))



# ---------버전 2 ---------#
# 리스트 내의 인덱스 사용

# import sys
# sys.stdin = open("input.txt", "r")

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# p1 = p2 = 0
# c = []

# while p1<n and p2<m:
#     if(a[p1] <= b[p2]):
#         c.append(a[p1])
#         p1 += 1 
#     else:
#         c.append(b[p2])
#         p2 += 1


# if(p1 < n):
#     c = c + a[p1:]

# if(p2 < m):
#     c = c + b[p2:]

# for i in c:
#     print(i, end=' ')
        

 


    




