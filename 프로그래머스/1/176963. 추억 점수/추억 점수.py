def solution(name, yearning, photo):
    arr = []
    
    for i in photo:
        sum = 0
        for j in i:
            if j in name:
                idx = name.index(j)
                sum += yearning[idx]
        
        arr.append(sum)
    
    return arr
    