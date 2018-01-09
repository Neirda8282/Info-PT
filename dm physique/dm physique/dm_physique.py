from pylab import *
from numpy import *

T0=330
Lambda=237
R=1*10**(-3)
h=100
S=pi*R**2
D=sqrt(Lambda*R/(2*h))
print(D)
X=linspace(0,0.2)
Pth=[(Lambda*S*T0/D)*exp((-1/D)*x) for x in X]
theta=[T0*exp((-1/D)*x) for x in X]
plot(X,Pth,'r',X,theta,'*')
show()

##5) D sempble realiste environ la taille d'un ventilateur de processeur 
#6) suivant la temperature un industrielle va choise L soit de l'odre de D soit plus grand suivant la temperature et la puissance à dissipé
##7) 