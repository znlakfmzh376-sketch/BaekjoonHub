import sys
input=sys.stdin.readline

a=input().strip()
b=input().strip()
c=input().strip()
s=[a[0],b[0],c[0]]
if sorted(s) == ['k','l','p']:
    print('GLOBAL')
else:
    print("PONIX")    