'''
Ejercicio 2: Hacer un programa que pida la anchura y altura de un
rectángulo y con ayuda de una función lo dibuje con *.
'''

def dibujar(ancho,alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ",end="")
        print()


ancho = int(input("Digite el ancho: "))
alto = int(input("Digite el alto: "))

print()
dibujar(ancho,alto)
