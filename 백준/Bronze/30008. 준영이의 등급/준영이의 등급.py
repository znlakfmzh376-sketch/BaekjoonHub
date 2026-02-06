import sys
input = sys.stdin.readline

 
N ,K= map(int,input().split())

k_list =list(map(int, input().split()))

for i in range(K):
    
    P = (k_list[i] * 100) // N
    
    if 0 <= P <=4:
        k_list[i] = 1
        
    elif 5 <= P <=11:
        k_list[i] = 2  
        
    elif 12 <= P <=23:
        k_list[i] = 3
        
    elif 24 <= P <=40:
        k_list[i] = 4
        
    elif 41 <= P <=60:
        k_list[i] = 5
        
    elif 61 <= P <=77:
        k_list[i] = 6
        
    elif 78<= P <=89:
        k_list[i] = 7
        
    elif 90 <= P <=96:
        k_list[i] = 8
        
    else:
        k_list[i] = 9   

print(*k_list)        
                                     