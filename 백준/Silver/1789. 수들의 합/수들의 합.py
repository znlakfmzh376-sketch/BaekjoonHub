import sys
input = sys.stdin.readline
S= int(input())
sum=0
count =0
i=1
while True:
    i+=1
    sum+=i
    count += 1
    if sum>= S:
        break
print(count)
