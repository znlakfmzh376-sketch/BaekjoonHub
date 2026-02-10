import sys
input = sys.stdin.readline

x=int(input())
a=list(map(int,input().split()))
diff=(max(a)-min(a))//(x-1)
print(max(a)+diff) 