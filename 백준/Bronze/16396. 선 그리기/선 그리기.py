import sys
input = sys.stdin.readline

N = int(input())
line = [0] * 10001

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, y):
        line[i] = 1

print(sum(line))