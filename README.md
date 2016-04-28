## Image generation with DCGAN and word embeddings


# Modifying Number of Input Images

- go into sample_images.py
- change the TRAIN_SIZE variable
```bash
python sample_images.py
cd ../visual-semantic-embedding/
python compute_captions.py #adjusts sentence embedding for caption files
```


#Training the DCGAN

```bash
cd dcgan.torch/
DATA_ROOT=../data dataset=folder th main.lua
```

#Generating a Sample Image
```bash
gpu=0 net=[checkpoint-path] th generate.lua
```


