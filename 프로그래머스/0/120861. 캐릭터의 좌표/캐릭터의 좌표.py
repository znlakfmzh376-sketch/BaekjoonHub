def solution(keyinput, board):
    answer = []
    x=0
    y=0
    restrict_x=board[0]//2
    restrict_y=board[1]//2
    for i in keyinput:
        if i=='left':
            if x== (-restrict_x):
                pass
            else:
                x -= 1
            
        elif i=='right':
            if x== restrict_x:
                pass
            else:
                x +=1
            
        elif i=='up':
            if y== restrict_y:
                pass
            else:
                y +=1
    
        elif i=='down':
            if y== (-restrict_y):
                pass
            else:
                y -=1
    answer.append(x)
    answer.append(y)
    return answer