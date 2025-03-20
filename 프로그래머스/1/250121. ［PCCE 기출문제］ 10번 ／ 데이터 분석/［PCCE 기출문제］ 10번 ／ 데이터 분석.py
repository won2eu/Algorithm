def solution(data, ext, val_ext, sort_by):
    dict = {"code":0, "date":1, "maximum":2, "remain":3}
    new_data = []
    
    idx = dict[ext] #idx에는 데이터의 위치가 담겨있음.
    
    for dat in data:
        if dat[idx] < val_ext:
            new_data.append(dat)
    
    #new_data를 sort_by를 기준으로 정렬하기
    new_data.sort(key=lambda x: x[dict[sort_by]])
    
    return new_data
    