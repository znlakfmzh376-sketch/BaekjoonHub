import sys
input = sys.stdin.readline
x=int(input())
s ="UOS"

print(s[(x-1)%len(s)])
