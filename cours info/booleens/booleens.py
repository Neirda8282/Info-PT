def plus1(x):
    r=0
    if type(x)==type('a'):
        r=x+'1'
        return r
    if type(x)==type(1) or type(x)==type(0.1):
        r=x+1
        return r
    if type(x)==type(True):
        return bool(x+1)
    if type(x)==type([1]):
        r=x+[1]
        return r
    print('operation impossible')

#corectrion 
def ajout_un(x):
    T=type(x)
    if T==float or T==int:
        return(x+1)
    elif T==string:
        return(x+'1')
    elif T==list:
        return (x+[1])
    elif T==bool:
        return(bool(x+1))
    else:
        print('TypeError : cannot add 1 to object')

# exo 2 
def bisextile(a):
    if a%400==0:
        return True
    elif a%4==0 and (not a%100==0):
        return True
    else :
        return False

# corection 
def bissextile2(an):
    B=(an%400==0) or (an%4==0 and an%100!=0)
    return(B)
Mc=[2,4,6,9,11]
Ml=[1,3,5,7,8,10,12]
def jouran(date):
    j=date[0]+(date[1]-1)*31 # tous les mois de 31 jours 
    for k in Mc:
        if k<date[1]: #on retranche 1 pour les mois courts
            j=j-1
        if date[1]>2:
            if bissextile2(date[2]): #on retranche 1 ou 2 pour les bisextiles
                j=j-1
            else:
                j=j-2
    return j

def revolutionlune():
    #reponse 29,531228 en realité 29,53059
    D=[4,11,2017]
    P=[15,1,1900]
    T=jouran(D)
    c=1900
    while c!=D[2]:
        if bissextile2(c):
            T+=366
        else :
            T+=365
        c+=1
    T=T-jouran(P)
    return T/1458

print(revolutionlune())

