import sys
input = sys.stdin.readline

a,b,c,d=map(int,input().split())
list1=[a,b,c,d]
list1=sorted(list1)
result1=list1[0] + list1[3]
result2=list1[1] + list1[2]
print(abs(result1 - result2)) 