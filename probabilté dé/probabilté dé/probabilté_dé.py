def Sn(n):
    S=[0]+ [1/6]*6+[0]*6*(n-1)
 
    for N in range (1,n):
        for k in range(6*n,0,-1):
            S[k]=sum(S[max([0,k-6]):k])*1/6
            
        
    return S

print(Sn(4))
## corection 
#def S(n):
#    L=[0]+[1/6]*6+[0]*6*(n-1)
#    for p in range(2,n+1):
#        for k in range(6*n,0,-1):
#            L[k]=sum(L[max(k-6,0):k])*1/6
#    return L

def espe(X):
    R=0
    for k in range(len(X)):
        R+=k*X[k]
    return R

def especarre(X):
    R=0
    for k in range(len(X)):
        R+=(k**2)*X[k]
    return R

def var(X):
    return especarre(X)-(espe(X)**2)

N=[5,10,50]

def tracer(N):
    for n in N:
        T=linspace(0,2)
        Y=
        for t in T:

    legend()
    show()