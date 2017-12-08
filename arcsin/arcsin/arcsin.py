#def an(n):
#    if n==1
#    return 0
#    return (((2*n-1)**2)/((2*n)*(2*n+1)))*an(n-1)
#def coeff(n):
#    C=[]
#    for i in range (n+1):
#        C.append(an(i))
#    return C
from pylab import *

def coeff(n):
    C=[1]
    for k in range(1,n+1):
        C.append((((2*k-1)**2)/((2*k)*(2*k+1)))*C[k-1])
    return C

Coeff=coeff(100)


#def Som(x,N):
#    R=0
#    for i in range (N+1):
#        R+=Coeff[i]*(x)**(2*i+1)
#    return R

# corection pour Som

def Som(x,N):
    S=Coeff[N]
    for k in range(1,N+1):
        S=((S*x**2)+Coeff[N-k])
    S=x*S
    return S
    
from math import *
print(Som(sqrt(2)/2,100))

P=[k for k in range (1,16)]

#def liste_N():
#    N=[]
#    for j in P:
#       for i in range(101):
#            if Som(1/sqrt(2),i)-pi/4<10**(-P[j]):
#                N.append(i)
#    return N

#corection liste des entiers N

def deci(p):
    """Donner l'entier N"""
    X=1/sqrt(2)
    Y=pi/4
    N=0
    S=Som(X,0)
    while abs(S-Y)>10**(-p) and N<=100:
        N=N+1
        S=Som(X,N)
    return N

#X=[i for i in range(1,16)]
#Y=[deci(i) for i in X]

#plot(X,Y)
#show()

def arcsin(x):
    if x<=10**(-3):
        return x+Coeff[1]*x**3+Coeff[2]*x**5
    elif x<1/sqrt(2):
       N=int(((-15*log(10)+log(1-x**2))/(2*log(x)))-3/2)
       return Som(x,N)
    elif x>1/sqrt(2):
        return (pi/2)-arcsin(sqrt(1-x**2))

X=linspace(0,1)
Y1=[arcsin(x) for x in X]
Y2=[asin(x) for x in X]
Y3=[Y1[i]-Y2[i] for i in range(len(Y1))]
plot(X,Y1)
subplot(221)
plot(X,Y2)
subplot(222)
plot(X,Y3)

show()
