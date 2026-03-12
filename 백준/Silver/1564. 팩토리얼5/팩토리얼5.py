import sys
import math
input = sys.stdin.readline

N=int(input())
result=1
for i in range(1,N+1,1):
    result *=i
    while result % 10 == 0:
        result //=10  
        
    result %= 10**12        


print(str(result % 100000).zfill(5))    