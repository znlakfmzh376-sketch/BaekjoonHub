import sys
input = sys.stdin.readline

s=input().strip()
cnt=[0]*10

for ch in s:
    cnt[int(ch)] +=1
    
cnt[6] = cnt[6]+cnt[9]
cnt[6] = (cnt[6]+1) //2
cnt[9] = 0
print(max(cnt))    
    
    

