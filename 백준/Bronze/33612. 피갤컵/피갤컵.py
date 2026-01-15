import sys
input = sys.stdin.readline

N=int(input())
t=(N-1)*7
y=t//12
if N==1:
        m=0
else:
        m=t%12        
if m+8>12:
        print(y+2024+1, m+8-12)
else:
        print(y+2024, m+8)        
