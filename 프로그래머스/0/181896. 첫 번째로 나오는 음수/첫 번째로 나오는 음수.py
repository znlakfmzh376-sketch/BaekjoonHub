def solution(num_list):
    answer = 0
    count =0
    for i in num_list:
        if i<0:
            count +=1
            answer=num_list.index(i)
            break    
    if answer==0 and count ==0:
        answer=-1
    return answer