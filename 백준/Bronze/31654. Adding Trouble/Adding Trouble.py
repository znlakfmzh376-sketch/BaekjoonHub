import sys
input = sys.stdin.readline

A,B,C=map(int,input().split())
result=A+B
if C==result:
    print("correct!")
else:
    print("wrong!")    