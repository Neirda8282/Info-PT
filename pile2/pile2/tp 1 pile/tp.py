from pile import *
c1="((3*5-7)+1"
c2="((3*5)-7)+1"
c3="(3*5)-(7)+1"
print(c3)
c4="(3*(5-7)+(1"
def test_parentheses(c):
    p=creer_pile()
    L=c.split()
    for l in L:
        if l=="(":
            empiler(p,1)
        if l==')':
            if pile_vide:
                return True

            depiler(p)
    if pile_vide:
        return True 

c5=")1+2(2"
print(c5)
print(test_parentheses(c1),test_parentheses(c2),test_parentheses(c3),test_parentheses(c4),test_parentheses(c5))
