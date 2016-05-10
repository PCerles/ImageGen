import os,shutil,random

data_dir = "/home/vashishtm/ImageGen/data/images/"
caption_dir = "/home/vashishtm/ImageGen/captions/"
cap_out_dir = "/home/vashishtm/ImageGen/captions-small/"
output_dir =  "/home/vashishtm/ImageGen/data-small/"
if not os.path.exists(output_dir):
	os.mkdir(output_dir)
output_dir = "/home/vashishtm/ImageGen/data-small/images/"
if not os.path.exists(output_dir):
	os.mkdir(output_dir)

if not os.path.exists(cap_out_dir):
	os.mkdir(cap_out_dir)



print "Getting images from dirs..."
images = [x for x in os.listdir(data_dir)]
captions = [ x for x in os.listdir(data_dir)]
SAMPLE_SIZE = 5000

rand_samp = random.sample(images,SAMPLE_SIZE)
for r in rand_samp:
	#print "Random sample: " +  r
	shutil.copy(data_dir + r, output_dir + r)
	cap_file = r.split('.')[0] + ".txt"
	shutil.copy(caption_dir + cap_file, cap_out_dir + cap_file)

print "Done moving data..."




