from PIL import Image
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
import cv

# make red flower
def makered():
    i = Image.open('flower.jpg')
    dim = np.zeros((i.size[1], i.size[0]), 'int8')
    
    img_zero = Image.fromarray(dim, 'L')
    img = Image.merge('RGB', (i, img_zero, img_zero)) # in this variant will be easy to encode
    img.save('redflower.bmp')
    # (!) important to use bmp; jpg does some image conversion while saving
    # other options to save are, e.g.:      scipy.misc.toimage(numpytable, cmin=0, cmax=255).save(stringfilename) 
makered()


def decode(im):
    imtam = plt.imread(im)
    res = ""
    for x in imtam[7]:
        if x[2] != 0:
            res += chr(x[2])
    return res

def encode(text):
    imtam = plt.imread("redflower.bmp")
    imtamc = np.copy(imtam)
    for i in range(len(text)):
        imtamc[7][i][2] = ord(text[i])

    img = Image.fromarray(imtamc)
    img.save('crypted_by_myself.bmp')
    
print(decode('crypto.bmp'))
encode("My secret text!!!")

print(decode('crypted_by_myself.bmp'))
