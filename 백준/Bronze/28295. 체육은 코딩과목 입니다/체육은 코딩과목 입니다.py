import sys
input = sys.stdin.readline

result=0
for i in range(10):
    a=int(input())
    result+=a
    
result=result%4

if result==0:
    print("N") 
elif result==1:
    print("E") 
elif result==2:
    print("S") 
elif result==3:
    print("W")            