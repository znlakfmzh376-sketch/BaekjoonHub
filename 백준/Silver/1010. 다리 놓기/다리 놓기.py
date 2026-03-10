import sys
import math
input = sys.stdin.readline
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    result=math.factorial(M)//(math.factorial(N)*math.factorial(M-N))
    print(result)