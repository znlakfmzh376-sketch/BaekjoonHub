def solution(numbers, direction):
    answer = []
    if direction =='right':
        for i in range(-1,len(numbers)-1,1):
            answer.append(numbers[i])            
    else:
        for i in range(1,len(numbers),1):
            answer.append(numbers[i])
        answer.append(numbers[0])    
        
    return answer