import sys
input = sys.stdin.readline

N=int(input())
fib=[0,1]
for i in range(2,N+1,1):
    x=fib[i-1]+fib[i-2]
    fib.append(x)
print(fib[N])    
