import sys
input = sys.stdin.readline

N = int(input())
results = []

for i in range(N):
    a, b, c = map(int, input().split())
    dice = [a, b, c]

    if a == b and b == c:
        result = 10000 + a * 1000
        results.append(result)

    elif a == b or b == c or c == a:
        if a == b or a == c:
            result = 1000 + a * 100
        else:
            result = 1000 + b * 100
        results.append(result)

    else:
        result = max(dice) * 100
        results.append(result)

print(max(results))