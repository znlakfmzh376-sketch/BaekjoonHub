import sys
input = sys.stdin.readline

arr=[list(map(int,input().split())) for i in range(9)]
temp=arr[0][0]
x=1
y=1
for i in range(9):
    for j in range(9):
        if arr[i][j]>temp:
            temp=arr[i][j]
            x=i+1
            y=j+1
print(temp)
print(x,y)            
            

        