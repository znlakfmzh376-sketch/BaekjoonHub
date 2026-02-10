import sys
input = sys.stdin.readline

N,M,A,B=map(int,input().split())

result= ((3*N)-M)*A+B
print(result if 3*N-M>0 else 0)