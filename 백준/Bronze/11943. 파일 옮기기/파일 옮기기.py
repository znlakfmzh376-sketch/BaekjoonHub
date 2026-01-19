import sys
input = sys.stdin.readline

A,B=map(int,input().split())
C,D=map(int,input().split())
if (A+D)>(B+C):
    print(B+C)
elif (A+D)<(B+C):
    print(A+D)
else:
    print(A+D)      