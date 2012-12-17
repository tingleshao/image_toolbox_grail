import sys
import getopt 
from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

__doc__ = "this is doc for math_morphology.py!"

def process(arg):
  #  el = ndimage.generate_binary_structure(2,1)
  #  eli = astype(np.int)
    im = np.zeros((64,64))
    np.random.seed(2)
    x, y = (63*np.random.random((2,8))).astype(np.int)
    im[x,y] = np.arange(8)

    bigger_points = ndimage.grey_dilation(im, size=(5,5), structure=np.ones((5,5)))

    square = np.zeros((16,16))
    square[4:-4, 4:-4] = 1
    dist = ndimage.distance_transform_bf(square)
    dilate_dist = ndimage.grey_dilation(dist, size=(3,3), structure=np.ones((3,3)))

    plt.figure(figsize=(12.5,3))
    plt.subplot(141)
    plt.imshow(im, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')
    plt.subplot(142)
    plt.imshow(bigger_points, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')
    plt.subplot(143)
    plt.imshow(dist, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')
    plt.subplot(144)
    plt.imshow(dilate_dist, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')

    plt.subplots_adjust(wspace=0, hspace=0.02, top=0.99, bottom=0.01, left=0.01, right=0.99)
    plt.show()


   
def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    for arg in args:
        process(arg) # process() is defined elsewhere

if __name__ == "__main__":
    main()


