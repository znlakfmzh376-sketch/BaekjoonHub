import sys
input=sys.stdin.readline
T=int(input())

for i in range(T):
    H,W,N =map(int,input().split())

    if N%H==0:
        floor = H
        room = N//H
    else:
        floor = N%H
        room = N//H + 1

    # room이 1자리면 앞에 0 붙이기
    if room < 10:
        print(str(floor) + "0" + str(room))
    else:
        print(str(floor) + str(room))