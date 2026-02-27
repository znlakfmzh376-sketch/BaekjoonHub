import sys
input = sys.stdin.readline

L=int(input())
s=input().strip()
A=s.count('A')
C=s.count('C')
G=s.count('G')
T=s.count('T')
print(A*C*G*T % 1000000007)