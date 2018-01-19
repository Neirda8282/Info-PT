from math import *
from pylab import *
 
def integrale(f,a,b,N):
    X=linspace(a,b,N)
    R=0
    h=X[0]-X[1]
    for x in X:
        R+=f(x)*h
    return R

def fx(t):
    return cos((t**2)/2)
def fy(t):
    return sin((t**2)/2)

def x(s,N):
    R=integrale(fx,0,s,N)
    return R
def y(s,N):
    R=integrale(fy,0,s,N)
    return R

def dessin(I,N):
    X=[]
    Y=[]
    T=linspace(0,I,N+1)
    for t in T:
        X.append(x(t,N+1))
        Y.append(y(t,N+1))
    plot(X,Y)
    show()
    return 

#dessin(6,6000)


def LX(I,N):
    T= linspace(0,I,N)
    X=[0]
    for k in range (1,len(T)):
        X.append(X[k-1]+integrale(fx,T[k-1],T[k],N))
    return X



#Corection 
s=linspace(0,6,6001)
#s[k+1]-s[k]=1/1000 = pas 
#x(s[k+1])=x(s[k]) + rectangle(hauteur cos((s[K+1]**2)/2) largeur = pas)
pas=1/1000
x=[0 for k in range(6001)]
y=[0 for k in range(6001)]
for k in range(1,6001):
    x[k]=x[k-1]+pas*cos((s[k]**2)/2)
    y[k]=y[k-1]+pas*sin((s[k]**2)/2)
plot(x,y)
axis("equal")

Xp=[x[1000*k] for k in range(7)]
Yp=[y[1000*k] for k in range(7)]
plot(Xp,Yp,'ro')
show()