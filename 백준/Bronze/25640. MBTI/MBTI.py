import sys

#input=sys.stdin.readline()

mbti = input().strip()
N=int(input())
count=0
for i in range(N):
    friend_mbti=input().strip()
    if mbti==friend_mbti:
        count +=1
print(count)        
        

