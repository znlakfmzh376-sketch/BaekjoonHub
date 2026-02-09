import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    num =list(map(int,input().split()))
    even = []
    for j in range(len(num)):
        if num[j] % 2 ==0:
            even.append(num[j])
    print(sum(even),end=' ')
    print(min(even))
         