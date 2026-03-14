import sys
input = sys.stdin.readline

n = int(input())

MOD = 1000000
PISANO = 1500000

n %= PISANO

fib = [0,1]

for i in range(2, n+1):
    fib.append((fib[i-1] + fib[i-2]) % MOD)

print(fib[n])