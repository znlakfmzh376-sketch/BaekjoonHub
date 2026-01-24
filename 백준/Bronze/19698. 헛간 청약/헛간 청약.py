import sys
input = sys.stdin.readline

N,W,H,L=map(int,input().split())
width=W//L
length=H//L
num=width*length
x=[N,num]
x=sorted(x)
print(x[0])
