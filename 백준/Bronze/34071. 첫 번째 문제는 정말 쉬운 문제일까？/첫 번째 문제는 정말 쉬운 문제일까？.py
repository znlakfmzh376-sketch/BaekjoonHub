import sys
input = sys.stdin.readline

N=int(input())
num=[]
for i in range(N):
    a=int(input())
    num.append(a)
if min(num)==num[0]:
    print("ez")   
elif max(num)==num[0]:
    print("hard")
else:
    print("?")        

            