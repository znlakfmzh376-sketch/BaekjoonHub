import sys
input = sys.stdin.readline
A,B,C=map(int,input().split())
D=int(input())
D=D+(3600*A)+(60*B)+C
h=D//3600
m=D//60-(h*60)
s=D%60
if h>=24:
        print(h%24, m,s)
else:    
        print(h,m,s)    
