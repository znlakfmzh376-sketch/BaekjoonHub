import sys
input = sys.stdin.readline

A,T = map(int,input().split())
result = 10 + 2*(25-A+T)
if result<=0:
        print(0)
else:
        print(result)        