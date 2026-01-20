import sys
input = sys.stdin.readline

a,b,c=map(int, input().split())
A,B,C=map(int, input().split())
x=A-c
y=int(B/b)
z=C-a
print(x,y,z)    