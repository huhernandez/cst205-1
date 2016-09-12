## Name: Hugo Hernandez
## Date: 9/9/16
## Purpose: This program uses PIL to modify 9 images by applying two different alternating filters (B&W and Blur)


from __future__ import print_function
from PIL import Image
from PIL import ImageFilter

def bwFilter(img):     #This function will apply the black and white filter
    img = img.convert('1')
    img.show()
    
theImages = []

imagePath = "/Users/Hugo/Desktop/cstproj1/project1images/"

#/Users/Hugo/Desktop/cstproj1/project1images/1.png


for myImage in range(1,10):
    theImages.append(Image.open(imagePath + str(myImage) + ".png"))

myCounter = 0
for aImage in theImages:
    if(myCounter%2 == 1):
        bwFilter(theImages[myCounter])
    else:
        
        #bwFilter(theImages [myCounter])
        #aImage.filter(ImageFilter.BLUR)
        #aImage.filter(ImageFilter.MinFilter(3))
        #aImage.filter(ImageFilter.MinFilter)
        aImage.convert('L')
        aImage.show()
      
        
    myCounter = myCounter + 1

