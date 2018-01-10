from numpy import *
from pylab import *
### mise en place des constantes necesaire au calcul 
a=100*10**-3
b=260*10**-3
c=20*10**-3
d=324.22*10**-3
l=280*10**-3
def valeur(wm,tm):
    """renvoie les valeurs de A,B,Ap,Bp,Cp en prennant en entrée wm et thetam"""
    A=2*((a*d)-(b*c)-(d*l*cos(tm))-(c*l*sin(tm)))
    B=2*(-a*c-b*d-d*l*sin(tm)+c*l*cos(tm))
    Ap=2*l*wm*(d*sin(tm)-c*cos(tm))
    Bp=2*l*wm*(-d*cos(tm)-c*sin(tm))
    Cp=2*l*wm*(a*sin(tm)+b*cos(tm))
    return A,B,Ap,Bp,Cp

def euler(wm,Tmmax,N):
    """ fonction qui prend en entrée la vitesse de rotation moteur , l'angle moteur maxi et le nombre de point et renvoie les liste de theta et thetap """
    T=Tmmax/wm # duree d'ouverture du vantail 
    t=linspace(0,T,N+1) #vecteur temps equirepartie
    Tm=wm*t #liste de thetamoteur
    Tv=[0] #valeur initial de Theta vantail
    Tvp=[0] #valeur initial de theta point vantail
    A,B,Ap,Bp,Cp=valeur(wm,Tm)
    for k in range (len(t)-1):
       
        Coef=(Ap[k]*cos(Tv[k])+Bp[k]*sin(Tv[k])+Cp[k])/(A[k]*sin(Tv[k])-B[k]*cos(Tv[k]))
        Tvp.append(Coef)
        Tv.append(Tv[k]+t[1]*Tvp[k])
    return Tm,Tvp

Tmmax=118.2*pi/180
X,Y=euler(0.1,Tmmax,1000)
plot(X,Y)
show()
