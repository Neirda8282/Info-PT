from math import *
from pylab import *

f1=open('essai1.csv','r')
ligne1=f1.readlines()

X1=[]
Y1=[]
k=0
for ligne in ligne1:
    ligne=ligne[:-2]
    if k>0:
        a=ligne.split(';')
        X1.append(float(a[0]))
        Y1.append(float(a[1]))
    k+=1
#plot(X1,Y1)
#show()
f1.close()

X=[(X1[k]+X1[k+1]+X1[k+2]+X1[k+3]+X1[k+4]+X1[k+5])/5 for k in range (len(X1)-6)]
Y=[(Y1[k]+Y1[k+1]+Y1[k+2]+Y1[k+3]+Y1[k+4]+Y1[k+5])/5 for k in range (len(Y1)-6)]

while X[0]==0.0:
    X.remove(0.0)
    Y.remove(Y[0])

P=[Y[k]/X[k] for k in range(len(X))]
P2=[]
for k in range(len(P)-200):
    if abs((P[k]+P[k+100]+P[k+200])/3)-P[k]<10**-3:
        P2.append(P[k])
print(P2)