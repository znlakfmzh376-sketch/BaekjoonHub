def solution(lines):
    arr1 = []
    arr2 = []
    arr3 = []
    for i in range(lines[0][0],lines[0][1]):
        arr1.append(i)
    for i in range(lines[1][0],lines[1][1]):
        arr2.append(i)
    for i in range(lines[2][0],lines[2][1]):
        arr3.append(i)    
    result = (set(arr1) & set(arr2)) | (set(arr2) & set(arr3)) | (set(arr1) & set(arr3)) 
    return len(result)