from PIL import Image, ImageOps
import random

def grey_scale(imagen):
	imagen = Image.open(imagen)
	imagen = ImageOps.grayscale(imagen)
	imagen.save("{} - Grey_Scale.jpg".format(random.randrange(100)))


file = input("Ingrese la direccion de la imagen : ")
grey_scale(file)
