a,k,n=map(int,input().split())

def double(k):
    t=0
    while True:
        if k//pow(2,t)==1:
            return t
        else:
            t+=1

def double_double(step,k):
    list_ki = [0 for i in range(step + 1)]
    for j in range (step,-1,-1):
        if k//pow(2,j)==1:
            list_ki[j]=1
            k-=pow(2,j)
    return list_ki


def multiply(a,k,n):
    step = double(k)
    list_ki=double_double(step,k)
    list_A = [0 for i in range(step + 1)]
    list_b = [0 for i in range(step + 1)]
    list_b[0]=1
    if k==0:
        return list_b[0]
    list_A[0]=a
    if list_ki[0]==1:
        list_b[0]=a
    for i in range(1,step+1):
        list_A[i]=pow(list_A[i-1],2,n)
        if list_ki[i]==1:
            list_b[i]=list_A[i]*list_b[i-1]%n
        else:
            list_b[i] =list_b[i - 1]
    print(list_ki)
    print(list_A)
    print(list_b)
    print(list_b[-1])


multiply(a,k,n)
