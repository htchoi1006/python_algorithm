import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))



def digit_sum(x):
    sum = 0
    while(True):
        sum += x%10
        x = x//10
        if(x < 10):
            sum += x
            break
    
    return sum

def digitSum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


result = 0
answer = 0

for i in a:
    tmp = digit_sum(i)
    if(result < digit_sum(i)):
        result = tmp
        answer = i

print(answer)






