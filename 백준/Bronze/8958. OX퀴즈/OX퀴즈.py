import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    result=0
    count=0
    s=input()
    for i in range(len(s)):
        if s[i]=="O":
            count +=1
            result += count
        else:
            count =0    
    print(result)