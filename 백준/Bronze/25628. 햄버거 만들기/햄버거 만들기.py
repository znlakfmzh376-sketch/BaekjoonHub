import sys
input = sys.stdin.readline

A,B=map(int,input().split())

a=A//2
x=[a,B]
print(min(x))