import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = set()
for _ in range(N):
    A.add(input().strip())

result = []

for _ in range(M):
    name = input().strip()
    if name in A:
        result.append(name)

result.sort()

print(len(result))
for name in result:
    print(name)