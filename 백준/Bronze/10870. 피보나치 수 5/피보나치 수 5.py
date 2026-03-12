import sys
import math
input = sys.stdin.readline

fib=[0,1]
N=int(input())

for i in range(2,N+1,1):
    result=fib[i-2]+fib[i-1]
    fib.append(result)

print(fib[N])    
  