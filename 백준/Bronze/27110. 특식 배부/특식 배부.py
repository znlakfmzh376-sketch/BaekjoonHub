import sys

input=sys.stdin.readline

N=int(input())
A,B,C=map(int, input().split())
result=0
for ch in [A,B,C]:
    if ch>=N:
        result+=N
    else:
        result+=ch
print(result)        