from pylab import *

def factIter(n):
    """ modele itératif base sur le modele 
    n!=1*2*3*4....*n"""
    p=1
    for i in range(1,n+1):
        p*=i
    return i

def factRec(n):
    """modele dit recursif s'appel lui meme sur le principe de 0!=1 et n!=n*(n-1)!
    """
    if n==0:
        return 1
    else : 
        return n*factRec(n-1)

#print(factRec(1000))
#y=factRec(250)*(0.0108**250)  #calcul impossible car il ne peut pas converitr un entier trop grand en flotant
#print(y)

def yn(n):
    if n==0:
        return 1
    return (n*(0.0108))*yn(n-1)
#print(yn(250))
#print(int(yn(250)))

def pgcd(n,m):
    """renvoie pgcd(a,b) = pgcd(b,r) avec r reste de la divison euclidienne dansle pgcd"""
    n,m=max([n,m]),min([n,m])
    if n%m==0:
        if m!=0:
            return m 
        return n
    return pgcd(m,n%m)

#print(pgcd(1080,92))
#print(pgcd(92,1080))

## corection pgcd

#def pgcd(a,b):
#    if a<b:
#       return pgcd(b,a)
#    if b==0:
#        return a
#    return pgcd(b,a%b)

def beppo(p,x,y):
    """ renvoie la valeur du polynome P avec p les coef du polynome 
    ici p=2x^3 -7x^2 + 3x + 1 cette algorithme est l'algorithme de "horner"
    """

    y+=p[-1] #donne la dernier valeur de p
    if len(p)==1: # renvoie du cas de base
        return y  # cas de base 
    y=x*y 
    return beppo(p[:-1],x,y)  #recursivité 

#p=[1,3,-7,2]
#y=0
#x=7
#print(beppo(p,x,y))



#X=linspace(0,200,201)
#Y=[beppo(p,t,0) for t in X]



#def f(x):
#    return 2*(x**3)-7*(x**2)+3*x +1

#Y2=[f(t) for t in X]
#plot(X,Y,'rx',X,Y2,'b+')
#show()




def fibo(n):
    """ suite de fibonacci par recursivité"""
    if n==0 or n==1 : 
        return 1
    return fibo(n-1)+fibo(n-2)

#print(f(30))

# temps de calcul : Trecursif environ alphe * phi ^n 
def temps_rec(n):
    """temps de calcul recursif """
    p=3  # A ajuster : nombre de calcul
    from time import clock
    t0=clock()
    for k in range (p):
        fibo(n)
    t1=clock()
    return (t1-t0)/p
from math import *
from pylab import *

def courbe_alpha():
    """visualiser alpha"""
    
    x=[k for k in range(10,30)]
    phi = (1-sqrt(5))/2
    y=[(temps_rec(k)/(phi**k)) for k in x ]
    plot(x,y)
    show()


#print(temps_rec(10))
#courbe_alpha()


def fiboiteratif(n):
    """calcul iteratif de fibon"""
    a=1
    b=1
    for k in range(2,n+1):
        c=a+b
        a=b
        b=c
    return b

def temps_iter(n):
    """temps de calucl itératif de fibo"""
    p=100 # a ajuster en fonction du pc
    from time import clock
    t0=clock()
    for k in range(p):
        fiboiteratif(k)
    t1=clock()
    return (t1-t0)/p
def courbe_ite():
    """visualiser courbe"""
    x=[k for k in range(10,500)]
    y=[log(temps_iter(k))-log(k) for k in x]
    plot(x,y)
    show()

courbe_ite()