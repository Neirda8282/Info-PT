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
