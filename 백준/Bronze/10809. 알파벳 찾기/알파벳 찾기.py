import sys
input = sys.stdin.readline

S= input()

Alphabet="abcdefghijklmnopqrstuvwxyz"

for i in Alphabet:
    if i in S:
        print(S.index(i), end=" ")
    else:
        print(-1, end=" ")    