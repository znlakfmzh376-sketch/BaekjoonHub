import sys
import math
input = sys.stdin.readline

N = int(input())
M = int(input())

sosu = []

for i in range(N, M+1):
    if i < 2:
        continue

    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        sosu.append(i)

if not sosu:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))