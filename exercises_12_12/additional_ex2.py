import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

img = plt.imread('noisymoonlanding.png').astype(float)
plt.figure()
plt.imshow(img, plt.cm.gray)
plt.title('Noisy')


img_smooth = ndimage.gaussian_filter(img, 3.5)
plt.figure()
plt.imshow(img_smooth, plt.cm.gray)
plt.title("Noisy but more smooth")
