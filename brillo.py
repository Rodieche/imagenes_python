#!/usr/bin/env python

##############################################################
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##															##
##	Titulo : Procesamiento de Imagenes						##
##															##
##	Autor : Rodolfo Echenique								##
##															##
##	Materia : TV Digital y Procesamiento de Imagenes		##
##															##
##	Carrera : Ingenieria en Telecomunicaciones				##
##															##
##	Año : 2016												##
##															##
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##############################################################


from PIL import Image
import random

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#													FUNCION PARA MODIFICAR EL BRILLO
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bright(image,n):
	image = Image.open(image)
#	image.show()
	px = image.load()
	width, height = image.size
	for y in range(height):
		for x in range(width):
			pxnew = []
			list(px[x,y])
			for i in range(3):
				pxnew.append(cambio(px[x,y][i],n))
			px[x,y] = (pxnew[0],pxnew[1],pxnew[2])
			tuple(px[x,y])
	image.save("{} - brillo - {}.jpg".format(random.randrange(100),n))

def cambio(value,cambio):
	new_value = value + cambio
	if new_value > 255:
		new_value = 255
		return new_value
	elif new_value < 0:
		new_value = 0
		return new_value
	else:
		return new_value 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

file = input("Ingrese la direccion de la imagen : ")
brillo = int(input("Ingrese la cantidad de brillo que desea : "))
bright(file, brillo)

