import sys
input = sys.stdin.readline
p={"animal":"Panthera tigris", "flower":"Forsythia koreana", "tree":"Pinus densiflora"}

while True:
        N=input().strip()
        if N=="end":
                break
        print(p[N])
        
