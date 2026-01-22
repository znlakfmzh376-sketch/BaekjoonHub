import sys
input = sys.stdin.readline

N=int(input())
a,b=map(int,input().split())

result= a//2 +b
if result>=N:
    print(N)
else:
    print(result)    