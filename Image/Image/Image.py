import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Im

imagec=Im.open("image_couleurs.jpg")

#2
imagec.show()

#1
mode_imagec=imagec.mode
largeur,hauteur = imagec.size
image_format = imagec.format

#Cretation d'une image vide 

L=list(imagec.getdata())
#print(L)

tab=np.array(imagec)

image_gris=imagec.convert("L")
image_gris.show()

New=Im.new("L",(largeur,hauteur))
New.show()
tab2=np.array(image_gris)
New.putdata(list(image_gris.getdata()))
New.show()