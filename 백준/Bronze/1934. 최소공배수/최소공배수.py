import sys
import math
input = sys.stdin.readline
T=int(input())
for _ in range(T):
    A, B=map(int,input().split())
    C=math.lcm(A, B)
    print(C)
    
    
