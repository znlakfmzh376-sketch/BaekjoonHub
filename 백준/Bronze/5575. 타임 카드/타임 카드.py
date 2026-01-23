import sys
input = sys.stdin.readline
#A=list(map(int,input().split()))
#B=list(map(int,input().split()))
#C=list(map(int,input().split()))
#time1 = ((A[3]*3600)+(A[4]*60)+A[5])-((A[0]*3600)+(A[1]*60)+A[2])
#time2 = ((B[3]*3600)+(B[4]*60)+B[5])-((B[0]*3600)+(B[1]*60)+B[2])
#time3 = ((C[3]*3600)+(C[4]*60)+C[5])-((C[0]*3600)+(C[1]*60)+C[2])
for i in range(3):
    A=list(map(int,input().split()))
    time1 = ((A[3]*3600)+(A[4]*60)+A[5])-((A[0]*3600)+(A[1]*60)+A[2])
    h=time1//3600
    m=time1//60-(60*h) 
    s=time1% 60
    print(h,m,s)
#print(time1)
#print(time1)
#print(time1)