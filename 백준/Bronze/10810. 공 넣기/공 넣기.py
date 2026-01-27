import sys

input=sys.stdin.readline

N,M=map(int,input().split())
xlist=[0]*N
for a in range(M):
    i, j, k=map(int,input().split())
    for b in range(i-1,j):
        xlist[b]=k
print(*xlist[:])       