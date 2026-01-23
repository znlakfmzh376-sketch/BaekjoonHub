import sys
input = sys.stdin.readline

n=int(input())
result=n%8

if result==1:
    print(1)
elif result==0 or result==2:
    print(2)
elif result==3 or result==7:
    print(3)    
elif result==4 or result==6:
    print(4)    
elif result==5:
    print(5)                   