import os,random
from shutil import copy
images_dir = "/home/vashishtm/data/Coco/train2014/"
output_dir = "data/"
images = os.listdir(images_dir)
TRAIN_SIZE = 1000
rand_samp = random.sample(images,TRAIN_SIZE)
#rand_samp = [images_dir + x for x in rand_samp]
for x in rand_samp:
	copy(images_dir + x,output_dir) 
print "Done copying data..."

