import sys
input = sys.stdin.readline
a=['a','e','i','o','u','A','E','I','O','U']
s=input().strip()
count =0
for ch in s:
        if ch in a:
                count+=1 
print(count)                