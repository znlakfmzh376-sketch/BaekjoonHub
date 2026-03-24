import sys
input = sys.stdin.readline

N = int(input())
A, B, C, D = map(int, input().split())
S = input().strip()

if S[0] != 'a' or S[-1] != 'a':
    print("No")
elif S.count('a') > A or S.count('b') > B or S.count('c') > C or S.count('d') > D:
    print("No")
else:
    ok = True
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            ok = False
            break

    if ok:
        print("Yes")
    else:
        print("No")