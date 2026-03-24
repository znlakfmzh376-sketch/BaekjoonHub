import sys
input = sys.stdin.readline

gram = 0
total_count = 0

a,b,c=map(int,input().split())

a=abs(a)
b=abs(b)
if a+b>c:
    print('NO')
elif a+b==c:
    print('YES')
else:
    if (c-(a+b)) %2==0:
        print('YES')
    else:
        print('NO')            