import sys
input = sys.stdin.readline
a,b,c,d,e,f= map(int, input().split())
x=[a,b,c,d,e,f]
result=0
for i in range(len(x)):
        result=result + (x[i]*5)
print(result)        