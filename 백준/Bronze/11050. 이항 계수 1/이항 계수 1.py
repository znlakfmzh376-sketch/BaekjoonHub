import sys
input = sys.stdin.readline
N,K=map(int, input().split())
n_factorial=1
k_factorial=1   
t_factorial=1
for i in range(1,N+1,1):
    n_factorial*=i
for i in range(1,K+1,1):
    k_factorial*=i
for i in range(1,N-K+1,1):
    t_factorial*=i
result=n_factorial//(k_factorial*t_factorial)
print(result)