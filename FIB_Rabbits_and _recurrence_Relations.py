# n years k pairs per mature rabbit

n=5
k=3

def fibo(n,k):
    if n<=2:
        return 1
    else:
        return fibo(n-1,k)+k*fibo(n-2,k)
    
print(fibo(36,2))