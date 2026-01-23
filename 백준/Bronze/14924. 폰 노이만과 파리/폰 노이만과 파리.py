import sys
input = sys.stdin.readline

S,T,D=map(int, input().split())
time= D/(2*S)
distance=T*time
print(int(distance)) 