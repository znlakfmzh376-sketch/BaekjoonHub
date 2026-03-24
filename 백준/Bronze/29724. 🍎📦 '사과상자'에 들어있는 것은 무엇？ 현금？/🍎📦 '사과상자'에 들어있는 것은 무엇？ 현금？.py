import sys
input = sys.stdin.readline

gram = 0
total_count = 0

N = int(input())
for _ in range(N):
    T, W, H, L = input().split()
    W = int(W)
    H = int(H)
    L = int(L)

    count = (W // 12) * (H // 12) * (L // 12)

    if T == 'A':
        gram += 1000 + count * 500
        total_count += count
    else:
        gram += 6000

price = total_count * 4000

print(gram)
print(price)