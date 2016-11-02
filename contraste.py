from PIL import Image, ImageEnhance
import random

def contraste(imagen,n):
	image = Image.open(imagen)
	contrast = ImageEnhance.Contrast(image)
	contrast.enhance(n).show()
	image.save("{} - contraste - {}.jpg".format(random.randrange(100),n))

file = input("Ingrese la direccion de la imagen : ")
contrast = int(input("Ingrese la cantidad de brillo que desea : "))
contraste(file, contrast)
