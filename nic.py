import os
import numpy as np
from nibabel.testing import data_path
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

example_filename = os.path.join('/home/shambhavi/Downloads/train/data', '001.nii.gz')
label = os.path.join('/home/shambhavi/Downloads/train/label', '001.nii.gz')

import nibabel as nib
img = nib.load(example_filename).get_fdata()
lab = nib.load(label).get_fdata()
print(img.shape)
print(lab.shape)

#hdr = img.header

#all = hdr.get_xyzt_units()
#print(all)
'''
for i in range(25):
    plt.subplot(5, 5,i + 1)
    plt.imshow(img[:,:,i])
    plt.gcf().set_size_inches(10, 10)
plt.show()


for i in range(25):
    #plt.subplot(5, 5,i + 1)
    plt.imshow(lab[:,:,i])
    plt.gcf().set_size_inches(10, 10)
plt.show()
'''
plt.imshow(lab[:,:,7])
plt.show()