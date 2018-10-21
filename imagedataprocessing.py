import os
import pickle
import numpy as np

import PIL.Image as pii
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

filepath = os.getcwd()


cifar100_train = unpickle(filepath+'/cifar-100-python/train')
cifar100_meta = unpickle(filepath+'/cifar-100-python/meta')

image = cifar100_train[b'data']
image = image.reshape(50000, 3, 32, 32).transpose(0,2,3,1).astype("uint8")

coarse_label =  np.array(cifar100_train[b'coarse_labels'])
fine_label =  np.array(cifar100_train[b'fine_labels'])


#Visualizing CIFAR 10
fig, axes1 = plt.subplots(2,2,figsize=(5,5))
for j in range(2):
    for k in range(2):
        i = np.random.choice(range(len(image)))
        # axes1[j][k].set_axis_off()
        axes1[j][k].imshow(image[i,:])
fig.savefig('image.png')


