import sys
input = sys.stdin.readline

s=input().strip()
ch=['A','a','b','D','d','e', 'g',
    'o','O', 'P','p','Q','q','R',"@"]
count=0
for i in range(len(s)):
    if s[i] in ch:
        count +=1
    elif s[i]=='B':
        count +=2                    

print(count)            