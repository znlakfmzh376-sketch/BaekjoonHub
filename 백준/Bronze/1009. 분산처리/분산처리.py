import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    a,b=map(int,input().split())
    c=pow(a,b,10)
    if c==0:
        print(10)
    else:
        print(c)    
