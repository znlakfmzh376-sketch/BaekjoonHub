import sys
input=sys.stdin.readline

for i in range(3):
    x_list=list(map(int, input().split()))
    cnt=x_list.count(1)
    if cnt==0:
        print('D')   
    elif cnt==1:
        print('C') 
    elif cnt==2:
        print('B')  
    elif cnt==3:
        print('A')  
    elif cnt==4:
        print('E')                  