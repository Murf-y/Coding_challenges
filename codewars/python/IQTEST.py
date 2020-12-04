def iq_test(numbers):
    bool_number = list(map(lambda i: i%2==0, map(lambda i: int(i), numbers.split(" ")))) 

    if bool_number.count(True) == 1:
        return bool_number.index(True)+1
    else:
        return bool_number.index(False)+1
