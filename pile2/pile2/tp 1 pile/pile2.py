from pile import *
c1="((3*5-7)+1"
c2="((3*5)-7)+1"
c3="(3*5)-(7)+1"

c4="(3*(5-7)+(1"
def test_parentheses(c):
    p=creer_pile()
    L=list(c)
    for l in L:
        if l=="(":
            empiler(p,1)
        if l==')':
            if pile_vide(p):
                
                return False
            d=depiler(p)
    if pile_vide(p):
        return True
    else :
        
        return False 

c5=")1+2(2"

#print(test_parentheses(c1),test_parentheses(c2),test_parentheses(c3),test_parentheses(c4),test_parentheses(c5))#
 

def div2(x):
     return x//2,x%2

def decimaltobinaire(x):
    a=div2(x)
    l=creer_pile()
    while a[0]!=0:
        empiler(l,a[1])
        a=div2(a[0])
    empiler(l,a[1])
    return l

#print(decimaltobinaire(13))

def affichage(p):
    L=''
    c=1
    while not pile_vide(p):
        L+=str(depiler(p))
        if c==4:
            L+=" "
            c=0
        c+=1
    print(L)
   

affichage(decimaltobinaire(525))


