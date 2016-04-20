import os,random,json
from shutil import copy
images_dir = "/home/vashishtm/data/Coco/train2014/"
caption_file = "/home/vashishtm/data/Coco/annotations/captions_train2014.json"
caption_path = "data/captions/"
caption_data = json.load(open(caption_file))
output_dir = "data/images/"

caption_images = caption_data['annotations']
caption_map = {}
for c in caption_images:
	caption_map[c['image_id']] = c['caption']

images = os.listdir(images_dir)
TRAIN_SIZE = 1000
rand_samp = random.sample(images,TRAIN_SIZE)
#rand_samp = [images_dir + x for x in rand_samp]
if not os.path.exists(caption_path):
	os.mkdir(caption_path)
for x in rand_samp:
	copy(images_dir + x,output_dir)
	cap_file = x.split('.jpg')[0]
	im_id = int(x.split('.jpg')[0].split('_')[-1])
	with open(caption_path + cap_file + ".txt",'wb') as f:
		f.write(caption_map[im_id])
	f.close()
print "Done copying data..."

