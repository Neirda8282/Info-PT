from math import *
from pylab import *
import csv as csv 

##f1=input("nom du fichier : ")
#f1=open("Essai1.csv",'r')
#lecture = csv.reader(f1, delimiter=';')
#F=[]
#D=[]
#L=50
#S=2*12.5
#k=0
#for ligne in lecture:
    
#    if k==0:
#        LabelX=ligne[0]
#        LabelY=ligne[1]
#    else:
#        D.append(float(ligne[0])/L)
#        F.append(float(ligne[1]) /S)
#    k=1
#ylabel('Pression en Mpa')
#xlabel('allongement relatif')
#plot(D,F)
#show()
#f1.close()
F=['Essai1.csv','Essai2.csv','Essai3.csv','Essai4.csv']


def données(f):
    f1=open(f,'r')
    lecture = csv.reader(f1, delimiter=';')
    F=[]
    D=[]
    L=50
    S=2*12.5
    k=0
    for ligne in lecture:
    
        if k==0:
            LabelX=ligne[0]
            LabelY=ligne[1]
        else:
            D.append(float(ligne[0])/L)
            F.append(float(ligne[1]) /S)
        k=1
    f1.close()
    return D,F

def tracer(X,Y):
    xlabel('allongement relatif')
    ylabel ('Contrainte')
    plot(X,Y)
    show()

def lissage(X,Y,n):
    Xl=[]
    Yl=[]
    for k in range(len(X)-n):
        S=0
        T=0
        for i in range(n+1):
            S+=X[k+i]
            T+=Y[k+i]
        Xl.append(S/n)
        Yl.append(T/n)
    return Xl,Yl

def pentes(X,Y):
    R=[]
    for k in range (len(X)):
        R.append(Y[k]/X[k])
    return R

def maxcourbe(X,Y):
    return max(X),Y[index(max(X))]
def enlevezero(X,Y):
    X1=X[:]
    Y1=Y[:]
    while X[0]<10**-3:
        X1.remove()
        Y1.remove()
    return X1,Y1


def n_donne(X,Y,R):
    X1=X[:]
    Y1=Y[:]
    while Y1[0]<R:
        X1.remove(X1[0])
        Y1.remove(Y1[0])
    x=X1[0]
    y=Y1[0]
    for k in range(len(X1)):
        X1[k]=X1[k]-x
        Y1[k]=Y1[k]-y
    return X1,Y1

def moindre_carre(X,Y):
    E=[50000+10000*k for k in range(26)]
    R=[]
    for e in E:
        S=0
        M=[]
        for k in range(len(Y)):
            
            S+=(Y[k]-e*X[k])**2
            M.append(e*X[k])
                
        R.append(S)
        plot(X,M,'*',X,Y,'r')
        show()
        
    print('min de R',min(R),'index du min de R',R.index(min(R)))
    print(E[R.index(min(R))])
    Ym=[E[R.index(min(R))]*x for x in X]
    plot(X,Y,'*')
    show()
    plot(X,Y,'*')
    plot(X,Ym,'r')
    show()
    return R

def select_données(X,Y,V):
    k=0
    X1=[]
    Y1=[]
    while Y[k]<V:
        X1.append(X[k])
        Y1.append(Y[k])
        k+=1
    return X1,Y1



f='Essai3.csv'
eps,sigma=données(f)
tracer(eps,sigma)
eps2,sigma2=n_donne(eps,sigma,20)
tracer(eps2,sigma2)
eps3,sigma3=select_données(eps2,sigma2,max(sigma2)/3)
tracer(eps3,sigma3)
print(min(moindre_carre(eps3,sigma3)))


 