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

def inversion(image):
	image = Image.open(image)
#	image.show()
	px = image.load()
	width, height = image.size
	for y in range(height):
		for x in range(width):
			pxnew = []
			list(px[x,y])
			for i in range(3):
				pxnew.append(cambio(px[x,y][i]))
			px[x,y] = (pxnew[0],pxnew[1],pxnew[2])
			tuple(px[x,y])
	image.save("{} - inversion.jpg".format(random.randrange(100)))

def cambio(value):
	new_value = 255 - value
	return new_value

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

file = input("Ingrese la direccion de la imagen : ")
inversion(file)

