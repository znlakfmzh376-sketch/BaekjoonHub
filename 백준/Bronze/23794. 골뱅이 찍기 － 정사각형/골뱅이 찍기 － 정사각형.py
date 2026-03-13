import sys
input = sys.stdin.readline

N=int(input())

print('@'*(2+N))
for i in range(N):
    print('@'+(' '*N)+'@')
print('@'*(2+N))      