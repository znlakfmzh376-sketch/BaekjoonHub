import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    s=input().split(',')
    print(int(s[0])+int(s[1]))