import sys
input = sys.stdin.readline

R,C=map(int, input().split())
one_list=[list(map(int, input().split())) for _ in range(C)]
two_list=[list(map(int, input().split())) for _ in range(R)]
sum=0
for i in range(R):
    for j in range(C):
        if one_list[j][i] == two_list[i][C-j-1]:
            sum+=1

ok = """|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|"""

bad = '''|>___/|     /}
| O O |    / }
( =0= )""""  \\
| ^  ____    |
|_|_/    ||__|'''

if sum == R*C:
    print(ok)
else:
    print(bad)