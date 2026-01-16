import sys
input = sys.stdin.readline
a,b,c=list(map(int, input().split()))
x=[a,b,c]
x.sort()
print(x[1])