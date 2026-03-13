import sys
input = sys.stdin.readline

N=int(input())

for i in range(N):
    print('@@@@@'*N)
for i in range(3*N):
    print('@'*N)
for i in range(N):
    print('@@@@@'*N)        