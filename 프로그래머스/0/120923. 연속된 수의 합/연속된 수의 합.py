def solution(num, total):
    answer = []
    sum=0
    for i in range(num):
        sum += i
    start_num = (total- sum) //num
    for i in range(start_num,start_num+num):
        answer.append(i)
        
    return answer