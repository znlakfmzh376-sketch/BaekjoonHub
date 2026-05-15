def solution(my_string, is_suffix):
    answer = 0
    arr=[]
    for i in range(len(my_string)):
        arr.append(my_string[i::1])
    if is_suffix in arr:
        answer=1
    else:
        answer=0
        
    return answer