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

p=[1,3,-7,2]
y=0
x=7
print(beppo(p,x,y))



X=linspace(0,200,201)
Y=[beppo(p,t,0) for t in X]



def f(x):
    return 2*(x**3)-7*(x**2)+3*x +1

Y2=[f(t) for t in X]
plot(X,Y,'rx',X,Y2,'b+')
show()
