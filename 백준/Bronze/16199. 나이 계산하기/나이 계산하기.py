import sys
input = sys.stdin.readline

y,m,d=map(int, input().split())
sy,sm,sd=map(int, input().split())


if sy>y:
    if sm>m:
        print(sy-y)
    elif sm==m:
        if sd>=d:
            print(sy-y)
        else:
            print(sy-y-1)    
       
    else:
        print(sy-y-1)    
else:
    print(0)    
print(sy-y+1)
print(sy-y)
