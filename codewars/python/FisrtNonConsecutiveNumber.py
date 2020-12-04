def first_non_consecutive(arr):
    for i in arr:
        if i-1 in arr:
            
            continue
        elif arr.index(i)!=0:
            return i
