import sys
input = sys.stdin.readline

N=int(input())
W=int(input())
result=0
if N==5:
    result += 120
elif N >= 3:
    result += (10*N)+20
else:
    result +=(10*N)

if W>1000:
    result -=15

print(result if result >0 else 0)            
        