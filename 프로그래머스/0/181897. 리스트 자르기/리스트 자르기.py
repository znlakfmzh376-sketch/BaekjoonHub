def solution(n, slicer, num_list):
    answer = []
    a,b,c=slicer[0],slicer[1],slicer[2]
    if n ==1:
        for i in range(0,b+1,1):
            answer.append(num_list[i])
    elif n==2:
        for i in range(a,len(num_list),1):
            answer.append(num_list[i])
        
    elif n==3:
        for i in range(a,b+1,1):
            answer.append(num_list[i])
    elif n==4:
        for i in range(a,b+1,c):
            answer.append(num_list[i])
        
    return answer