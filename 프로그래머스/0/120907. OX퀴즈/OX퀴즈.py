def solution(quiz):
    answer = []
    for i in quiz:
        arr = i.split(' ')
        a = int(arr[0])
        op = arr[1]
        b = int(arr[2])
        c = int(arr[4])
        if op == '+':
            if a + b == c:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if a - b ==c:
                answer.append("O")
            else:
                answer.append("X")    
    return answer