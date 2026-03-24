import sys
input = sys.stdin.readline

count=0
result=[input().strip() for i in range(8)]
for i in range(8):
    for j in range(8):
        if i %2==0 and j%2==0:
            if result[i][j]=='F':
                count +=1
        elif i %2 !=0 and j%2 != 0:
            if result[i][j]=='F':
                count +=1

print(count)                
