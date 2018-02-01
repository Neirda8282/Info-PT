import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Im

imagec=Im.open("image_couleurs.jpg")

##2
#imagec.show()

##1
#mode_imagec=imagec.mode
#largeur,hauteur = imagec.size
#image_format = imagec.format

##Cretation d'une image vide 

#L=list(imagec.getdata())
##print(L)

#tab=np.array(imagec)

#image_gris=imagec.convert("L")
#image_gris.show()

#New=Im.new("L",(largeur,hauteur))
#New.show()
#tab2=np.array(image_gris)
##New.putdata(list(image_gris.getdata()))
##New.show()

##for l in range (largeur):
##    for h in range(hauteur):
##        rgb=imagec.getpixel((l,h))
##        g=[0,229*rgb[0]+0,587*rgb[1]+0,114*rgb[2]]
##        new.putpixel((l,h),(g))
##new.show()
tab=np.array(imagec, dtype=np.uint8)
l,c,t=np.shape(tab)

Ig=np.zeros((l,c))
for j in range (l):
    for k in range(c):
        R,G,B=tab[j,k]
        Gris=0.229*R+0.5787*G+0.114*B
        Ig[j,k]=Gris




IMgris=Im.new("L",(c,l))
IMgris.putdata(list(Ig.flat))
IMgris.save('imagegristest.png')
IMgris.show()

def symetrie_vertical(I):
    l,c=np.shape(I)
    IN=np.zeros((l,c))
    for j in range(l):
        for k in range(c):
            IN[j,k]=I[j,-k]
    Ims=Im.new("L",(c,l))
    Ims.putdata(list(IN.flat))
    Ims.save('imagesymetrievertical.png')
    Ims.show()

def symetrie_horizontal(I):
    l,c=np.shape(I)
    IN=np.zeros((l,c))
    for j in range(l):
        for k in range(c):
            IN[j,k]=I[-j,k]
    Ims=Im.new("L",(c,l))
    Ims.putdata(list(IN.flat))
    Ims.save('imagesymetriehorizontal.png')
    Ims.show()

symetrie_horizontal(Ig)
symetrie_vertical(Ig)

def negatif(I):
    l,c=np.shape(I)
    IN=np.zeros((l,c))
    for j in range(l):
        for k in range(c):
            IN[j,k]=255-int(I[j,k])
    Ims=Im.new("L",(c,l))
    Ims.putdata(list(IN.flat))
    Ims.save('imagenegatif.png')
    Ims.show()

negatif(Ig)

def seuil(I,S):
    l,c=np.shape(I)
    IN=np.zeros((l,c))
    for j in range(l):
        for k in range(c):
            if I[j,k]>=S:
                IN[j,k]=255
            else:
                IN[j,k]=0
    Ims=Im.new("L",(c,l))
    Ims.putdata(list(IN.flat))
    Ims.save('imageseuil.png')
    Ims.show()

seuil(Ig,127)