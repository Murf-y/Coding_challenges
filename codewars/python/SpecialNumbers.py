def special_number(number):
    lis=[0,1,2,3,4,5]
    for i in str(number):
        if i not in str(lis):
            return "NOT!!"  
    return "Special!!"
