import sys
input = sys.stdin.readline
a=int(input())        
b=int(input())        
c=int(input())        
d=int(input())        
e=int(input())        
x=[a,b,c]
y=[d,e]
x.sort()
y.sort()
print(x[0]+y[0]-50)
