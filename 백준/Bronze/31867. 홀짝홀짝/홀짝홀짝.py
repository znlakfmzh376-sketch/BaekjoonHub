import sys
# input = sys.stdin.readlines


N = int(input())
s=input().strip()
odd=0
even=0
for i in range(N):
    if int(s[i])%2==0:
        even +=1
    else:
        odd += 1

if odd > even:
    print(1)
elif odd< even:
    print(0)
else:
    print(-1)                    