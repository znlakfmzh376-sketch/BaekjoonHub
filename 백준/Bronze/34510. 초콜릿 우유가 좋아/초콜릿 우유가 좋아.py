import sys
input = sys.stdin.readline

a,b,c=map(int,input().split())
N=int(input())
if N%2==0:
    result=(N*c)+(N//2)*b
    print(result)
else:
    result=(N*c)+(N//2)*b+a+b   
    print(result) 