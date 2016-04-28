# script to resize images in the data/images/ folder to 64x64
import os
from skimage.transform import resize
import matplotlib.pyplot as plt

image_dir = "data/images/"
files = [image_dir + x for x in os.listdir(image_dir)]

for im_path in files:
	im = plt.imread(im_path)
	im = resize(im,(64,64))
	plt.imsave(im_path,im)
print "Done resizing images..."
