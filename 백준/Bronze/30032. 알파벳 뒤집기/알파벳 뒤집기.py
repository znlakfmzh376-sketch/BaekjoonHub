import sys
input = sys.stdin.readline

N, D = map(int, input().split())

for _ in range(N):
    s = list(input().rstrip()) 

    for i in range(len(s)):
        if D == 1:
            if s[i] == 'd': 
                s[i] = 'q'
            elif s[i] == 'b': 
                s[i] = 'p'
            elif s[i] == 'q': 
                s[i] = 'd'
            elif s[i] == 'p':
                s[i] = 'b'
        else:
            if s[i] == 'd': 
                s[i] = 'b'
            elif s[i] == 'b':
                s[i] = 'd'
            elif s[i] == 'q': 
                s[i] = 'p'
            elif s[i] == 'p':
                s[i] = 'q'

    print(''.join(s))  
