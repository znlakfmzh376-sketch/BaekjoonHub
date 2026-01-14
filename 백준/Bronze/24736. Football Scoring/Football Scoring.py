import sys
input = sys.stdin.readline

for i in range(2):
    result=0
    a,b,c,d,e=map(int, input().split())
    result=(6*a)+(3*b)+(2*c)+(d)+(2*e)
    print(result, end=" ")
    
