import sys
import math
input = sys.stdin.readline

A, B=map(int,input().split())

C=math.lcm(A, B)
print(C)
    