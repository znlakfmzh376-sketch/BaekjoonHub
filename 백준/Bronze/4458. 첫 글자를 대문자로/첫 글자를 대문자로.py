import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    s= input().rstrip()
    s = s[0].upper() + s[1:]
    print(s)