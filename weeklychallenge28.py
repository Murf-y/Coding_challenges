def D(b):
    for i in range(b):x=len([i for i in range(1,b+1) if not b%i])
    return x
def W(lst,i,j,s=0):
    for x in range(0,j+1):
        if lst[x]>i:s+=1
    return s
def solution(n):
    X=[]
    Z=[]
    for j in range(1,n+1):
        X.append(D(j))
    x=0
    for i in X:
        Z.append(W(X,i,x))
        x+=1
    Z.sort()
    r=[max(Z),Z.count(max(Z))]
    return r

print(solution(putanynumberhere))
#it is pretty slow
