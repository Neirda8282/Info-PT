
#exo3
#L=[i for i in range (2,1001)]
#n=len(L)
#for i in range(n):
  
#    for j in range(n):

#        if L[j]%L[i]==0:
#            print(L)
#            L.pop(j)
#            n=n-1
#            print(L,n)
#print(L)

#corection
#si y non premier 
#si y =  k*p < n
#alors k<sqrt(n) ou p<sqrt(n)
from math import *
def premiers(n):
    c=0
    L=[k for k in range(2,n+1)]
    j=0
    x=L[j]
    while x<int(sqrt(n)):
        for i in range(2,int(n/x)+1):
            c+=1
            if x*i in L:
                L.remove(x*i)
        j+=1
        x=L[j]
    print('tour de boucle',c)
    return L
print(premiers(1000))
