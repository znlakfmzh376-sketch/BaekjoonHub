def solution(code):
    answer = ''
    mode =0
    for i in range(0,len(code),1):
        if code[i] == '1':
            if mode ==0:
                mode=1
            elif mode == 1:
                mode =0
        if mode ==1:
            if i % 2 !=0 and code[i] != '1':
                answer +=code[i]
            else:
                pass
        elif mode == 0 and code[i] != '1':
            if i % 2 ==0:
                answer +=code[i]
            else:
                pass
    if len(answer) ==0:
        answer +='EMPTY'
    return answer