import sys
input = sys.stdin.readline

N=int(input())
result1=0
result2=0
for i in range(1,N+1,1):
    result1 += i
print(result1)
print(result1**2)
for i in range(1,N+1,1):
    result2 += (i**3) 
print(result2)    