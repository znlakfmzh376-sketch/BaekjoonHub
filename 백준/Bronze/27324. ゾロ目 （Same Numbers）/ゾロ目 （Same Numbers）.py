import sys
input = sys.stdin.readline

A = int(input())
a=A//10
b=A%10
if a==b:
    print(1)
else:
    print(0)    