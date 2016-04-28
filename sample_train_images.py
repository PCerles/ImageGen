import os,random,json
from shutil import copy
images_dir = "/home/vashishtm/data/Coco/train2014/"
caption_file = "/home/vashishtm/data/Coco/annotations/captions_train2014.json"
labels_file = "/home/vashishtm/data/Coco/annotations/instances_train2014.json"
caption_path = "captions/"
caption_data = json.load(open(caption_file))
label_data = json.load(open(labels_file))
output_dir = "data/images/"

LABEL_CHOICE = "food"

print "Getting category map"
categories = label_data['categories']
super_cat_map = {}
for c in categories:
	super_cat_map[c['id']] = c['supercategory']

annotations = label_data['annotations']
image_ids = []
#finding all image ids with a given label id
print "getting image ids..."
for a in annotations:
	if super_cat_map[a['category_id']] == LABEL_CHOICE:
		image_ids.append(a['image_id'])

caption_images = caption_data['annotations']
caption_map = {}
print "getting captions..."
for c in caption_images:
	if c['image_id'] in image_ids and c['image_id'] not in caption_map:
		caption_map[c['image_id']] = c['caption']
images = os.listdir(images_dir)
if not os.path.exists(caption_path):
	os.mkdir(caption_path)

print "parsing images..."
for x in images:
	cap_file = x.split('.jpg')[0]
	im_id = int(x.split('.jpg')[0].split('_')[-1])
	if im_id in caption_map.keys():
		print "Caption: " + caption_map[im_id]
		copy(images_dir + x,output_dir)
		with open(caption_path + cap_file + ".txt",'wb') as f:
			f.write(caption_map[im_id])
		f.close()
print "Done copying data..."

