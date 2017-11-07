#!/usr/bin/python
from __future__ import division
import Image
import math

def image_rotation(s,pix,ang):
	l = int(round(math.sqrt(math.pow(round(0.5*s[0]),2)+math.pow(round(0.5*s[1]),2))))
	img1 = Image.new("RGB",(2*l,2*l),"black")
	pix1 = img1.load()
	for i in range(0,s[0]):
		for j in range(0,s[1]):
			i1 = i - 0.5*s[0]
			j1 = 0.5*s[1] - j
			i2 = i1*math.cos(ang) - j1*math.sin(ang)
			j2 = i1*math.sin(ang) + j1*math.cos(ang)
			i3 = int(round(i2+l))
			j3 = int(round(l-j2))
			pix1[i3,j3] = (pix[i,j][0],pix[i,j][1],pix[i,j][2])
	img1.save("Tejas_Rotation.jpg")

def main():
	img = Image.open("/home/tejas/Downloads/Tejas.jpg")
	s = img.size
	pix = img.load()
	ang = -math.pi/2
	image_rotation(s,pix,ang)

if __name__ == '__main__':
	main()
