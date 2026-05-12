import statistics as st
def solution(array):
    if len(st.multimode(array))>1:
        answer=-1
    else:
        answer = st.mode(array)
    return answer