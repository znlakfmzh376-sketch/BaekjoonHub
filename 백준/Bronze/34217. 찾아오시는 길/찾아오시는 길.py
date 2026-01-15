import sys
input = sys.stdin.readline

A, B=map(int, input().split())
C, D=map(int, input().split())
a=A+C
b=B+D
if a>b:
        print("Yongdap")
elif a<b:
        print("Hanyang Univ.")        
else:
        print("Either")        