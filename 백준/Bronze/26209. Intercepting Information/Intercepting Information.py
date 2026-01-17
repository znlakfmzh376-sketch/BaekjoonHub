import sys
input = sys.stdin.readline

a,b,c,d,e,f,g,h=map(int,input().split())
bit=[a,b,c,d,e,f,g,h]
ch=[0,1]
count = 0
for i in range(len(bit)):
        if bit[i] in ch:
                count +=1
if count == 8:
        print("S") 
else:
        print("F")                       