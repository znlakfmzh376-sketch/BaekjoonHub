import sys
input = sys.stdin.readline

cho=list(map(int,input().split()))
han=list(map(int,input().split()))

for i in range(6):
    if i==0:
        cho[i]=cho[i]*13
        han[i]=han[i]*13
    elif i==1:
        cho[i]=cho[i]*7
        han[i]=han[i]*7
    elif i==2:
        cho[i]=cho[i]*5
        han[i]=han[i]*5
    elif i==3:
        cho[i]=cho[i]*3
        han[i]=han[i]*3
    elif i==4:
        cho[i]=cho[i]*3
        han[i]=han[i]*3
    elif i==5:
        cho[i]=cho[i]*2
        han[i]=han[i]*2
        
if sum(cho)>sum(han)+1.5:
    print("cocjr0208")
else:
    print("ekwoo")            
                        

            