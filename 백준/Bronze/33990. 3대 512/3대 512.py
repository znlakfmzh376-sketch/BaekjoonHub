import sys
input = sys.stdin.readline
one_rm_list=[]
N = int(input())
for _ in range(N):
    b,s,d=map(int,input().split())
    one_rm=b+s+d
    one_rm_list.append(one_rm)
    
result=max(one_rm_list)
for i in range(len(one_rm_list)):

    if 512 <=one_rm_list[i] and one_rm_list[i] <=result:
        result=one_rm_list[i]
    else:
        continue    
            
if result<512:
    print(-1)
else:
    print(result)        