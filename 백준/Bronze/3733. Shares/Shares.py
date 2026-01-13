import sys
input = sys.stdin.readline

while True:
    line = input().split()
    if not line:
        break
    n, s = map(int, line)
    print(s // (n + 1))
