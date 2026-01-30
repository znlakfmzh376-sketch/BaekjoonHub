import sys
input = sys.stdin.readline

N=int(input())
menu_list=[]
result=0
for i in range(N):
    menu=int(input())
    menu_list.append(menu)
M=int(input())
for i in range(M):
    order=int(input())
    result += menu_list[order-1]
print(result)    