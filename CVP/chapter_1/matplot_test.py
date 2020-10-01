from PIL import Image
from pylab import *

def plotLine():
	im=array(Image.open("empire.jpg"))
	imshow(im)

	x=[100,100,400,400]
	y=[200,500,200,500]

	plot(x,y,"r*")
	plot(x[:2],y[:2])
	
	title('Plotting: "empire.jpg"')
	axis("off")
	show()
	
def contourImage():
	im=array(Image.open("empire.jpg").convert("L"))
	figure()
	gray()
	contour(im,origin="image")
	axis("equal")
	axis("off")
	show()

def histImage():
	im=array(Image.open("empire.jpg").convert("L"))
	figure()
	hist(im.flatten(),128)
	show()

if __name__=="__main__":
#	plotLine()
#	contourImage()
	histImage()


