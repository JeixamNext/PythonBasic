# Hacer un dibujo ASCII
"""
Autor: Jaime
Date: 15/6/22
"""
#import
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random
#body
def RandomFont():
    fonts=["verdanab.ttf","times.ttf","impact.ttf","arial.ttf","tahoma.ttf","calibri.ttf","corbel.ttf"]
    n=random.randrange(1,7)
    return fonts[n]

def RandomSymbol():
    symbol=["#","@","|","\\","~~","7","?","!","$","%","/","()","=","*","+","}","]","-","_",">","<","X","0","A"]
    ns=random.randrange(1,24)
    return symbol[ns]

def dibujarASCII(text,simbol,colorT,tipo,sizeT):
    myfont = ImageFont.truetype(tipo, sizeT)
    size = myfont.getsize(text)
    img = Image.new("1",size,"black")
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, colorT, font=myfont)
    #array
    pixels = np.array(img, dtype=np.uint8)
    chars = np.array([' ',simbol], dtype="U1")[pixels]
    strings = chars.view('U' + str(chars.shape[1])).flatten()
    print( "\n".join(strings))

def dibujar(texto):

    print('\n'.join([''.join([(texto[(x-y)%len(texto)]
                               if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')
                              for x in range(-30,30)])for y in range(13,-11,-1)]))

dibujar(RandomSymbol())
dibujarASCII("Jeixam",RandomSymbol(),"white",RandomFont(),16)
print("_________________________________________________________________________________________________"'\n')
#Content

