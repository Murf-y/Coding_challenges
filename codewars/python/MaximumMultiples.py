Maximum Multiple
def max_multiple(divisor, bound):
    result=[]
    for i in range (divisor, bound+1):
        if i % divisor == 0 and i <= bound and i > 0:
            result.append(i)
    return result[-1]   
