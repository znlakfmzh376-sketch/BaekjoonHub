import sys
input = sys.stdin.readline

K, D, A=map(int, input().split("/"))
mask1=K+A<D
mask2=(D==0)
if (mask1 | mask2):
    print("hasu")
else:
    print("gosu")    
    


            
    