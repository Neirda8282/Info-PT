def creer_pile():
    """cretation de la pile acomme une liste vide"""
    L=[]
    return L
def empiler(p,e):
    """ajoute l'élement e a la pile p"""
    p.append(e)
    
def sommet(p):
    """ renvoie le somet de la pilie p """
    r=p[-1]
    return r
def depiler(p):
    """enleve le sommet de la pile"""
    if  not pile_vide(p):
        return p.pop()

def hauteur(p):
     """renvoie la haiteur de la pile"""
     r=len(p)
     return r
def pile_vide(p):
    """renvoie true si la pile est vide false sinon"""
    if hauteur(p)==0:
        return True
  
