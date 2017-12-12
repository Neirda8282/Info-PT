#Vigné Adrien 
#Dm maths 11/12/17


from math import *

gam=0.5772156649015328606 # constante donnée par wikipédia

def gamma(n):
    """ fonction qui calcul la constante d'Euler-Mascheroni pour un certain rang n a l'aide des series """
    C=[132,-240,256,-120,12] # liste des coefficient des division de la series
    a=1
    R=0
    for k in range(2,n+1): # calcul des 1/k
        a+=1/k
    R=a-log(n)-1/(2*n) # gamma calculer a la fin de la question e 
    for c in C:
        D=(1/c)*1/(n**2) # calcul des autres termes de la series pour mininimiser le temps de calcul
    R=R+D
    return R

#comparaison de la constante calcul avec la constante donnée 
print(gamma(100)-gam)
#8.33293434254756e-11
print(gamma(4000)-gam)
#-2.886579864025407e-14