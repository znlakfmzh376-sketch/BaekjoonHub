import sys
input = sys.stdin.readline

N,M,K=map(int, input().split())
a = K//M
b = K%M
print(a,b)
