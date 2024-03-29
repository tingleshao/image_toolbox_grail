import sys
import getopt
from scipy import misc
import numpy as np
import pylab as pl
from scipy import ndimage

__doc__ = 'this is doc!'

def process(arg):
    print "args: " + arg
    im_name = arg
    l2 = misc.imread(im_name)
    pl.imshow(l2) 
    pl.axis('off')
 
    ndimage.gaussian_filter(l2, sigma=5)
    l2 = misc.imresize(l2,(32,32),interp='nearest',mode=None)
 #   ndimage.gaussian_filter(l2, sigma=5)
   # t = otsu(l2)
    #print t[0]
    #print t[1].index(max(t[1]))
    #t[1].remove(max(t[1]))
    #print t[1].index(max(t[1]))
    #t[1].remove(max(t[1]))
    #print t[1].index(max(t[1]))
    hist = colorHistogram(l2)
    c10 = []
    for i in range(10):
        c10.append(float(hist.index(max(hist))))
        hist.remove(max(hist))
    print c10

#    im = np.zeros((100,300,3),dtype = 'uint8')
 #   im[:,0:99,0] = 32* 158.9 / 64
  #  im[:,0:99,1] =32 *( 158.9 % 64 ) / 8
   # im[:,0:99,2] = 32 * (158.9 % 8 ) 
    #im[:,100:199,0] = 32 * 335.0 / 64
 #   im[:,100:199,1] = 32 *( 335.0 % 64 )/ 8
  #  im[:,100:199,2] = 32 * (335.0 % 8 ) 
#    im[:,200:299,0] = 32 * 447.6 / 64
#    im[:,200:299,1] = 32 *( 447.6 % 64 ) / 8
 #   im[:,200:299,2] = 32 * (447.6 %  8 )  
  #  pl.imshow(im,vmin =0, vmax = 255)
   # pl.axis('off')  
    c1 = float(l2[10,10,0]/16 * 16**2 + l2[10,10,1] + l2[10,10,2]/ 16)
    print '---------------'
    print l2[0,0,0]
    print l2[0,0,1]
    print l2[0,0,2]
    c1 = c10[0]
    c2 = c10[1]
    c3 = c10[2]
    pl.figure()
    im2 = np.zeros((100,300,3),dtype='uint8')
    im2[:,0:99,0] = int(16 * c1 / 16**2)
    print '***************'
    print c1
    print int(16 * c1 / 16**2)
    im2[:,0:99,1] = int(( c1 % 16**2 ))
    im2[:,0:99,2] = int( 16 * (c1 % 16 )) 
    print l2
    print im2[0,0,0]
    print im2[0,0,1]
    print im2[0,0,2]
    im2[:,100:199,0] = int(16* c2 / 16**2)
    im2[:,100:199,1] = int( ( c2 % 16**2 ) )
    im2[:,100:199,2] = int(16* (c2 % 16 ) )
    im2[:,200:299,0] = int(16 * c3 / 16**2)
    im2[:,200:299,1] = int(( c3 % 16**2 ) )
    im2[:,200:299,2] = int(16 * (c3 %  16 )  )
    print im2
    pl.imshow(im2,vmin = 0, vmax = 255)
    pl.axis('off')
    pl.show()

def rgb2grey(imgrgb):
    imgrey = np.zeros((imgrgb.shape[0],imgrgb.shape[1]), dtype=np.uint8)
    for i in range(imgrgb.shape[0]):
       for j in range(imgrgb.shape[1]):
           imgrey[i,j] = (imgrgb[i,j,0] /3  + imgrgb[i,j,1] /3 + imgrgb[i,j,2]/3)
    ndimage.gaussian_filter(l2, sigma=5)
    return imgrey
  
def otsu(img):
    # this function calculates a maximum threshold
    hist = colorHistogram(img)
    delta_b_sq = [] 
    ts = []
    for t1 in range(1,len(hist)-3):
      for t2 in range(t1+1, len(hist)-2):
        # calculate probabilty lists
        p0 = calculateP(hist[0:t1],sum(hist))
        p1 = calculateP(hist[t1+1:t2],sum(hist))
        p2 = calculateP(hist[t2+1:len(hist)-1],sum(hist))
        # calculate weight
        w0 = sum(p0)
        w1 = sum(p1)
        w2 = sum(p2)
        # calculate mean for each group
        if w0 == 0:
            u0 = 0
        else:
            u0 = sum([a*b for a,b in zip(range(0,t1),p0)])/w0
        if w1 == 0:
            u1 = 0
        else:
            u1 = sum([a*b for a,b in zip(range(t1+1,t2),p1)])/w1
        if w2 == 0:
            u2 = 0
        else:
            u2 = sum([a*b for a,b in zip(range(t2+1,len(hist)-1),p2)])/w2
        if t1 == 2241 and t2 == 3312: 
             print 'u0: ' + str(u0)
             print 'u1: ' + str(u1) 
             print 'u2: ' + str(u2)
        delta_b_sq.append(w0*u0**2+w1*u1**2+w2*u2**2)
        ts.append([t1,t2])
    # find maximum 
#    print delta_b_sq
    th = ts[delta_b_sq.index(max(delta_b_sq))]
#    print max(delta_b_sq)
    print delta_b_sq.index(max(delta_b_sq))
    print len(delta_b_sq)
    print th
    print img.min()
    print img.max()
    return [th,hist]

def calculateP(hist,hist_sum):
    # this function calculates the probability given the histogram
    # the histogram can be a sub histogram in a larger one
    p = []
    if hist_sum == 0:
        return [0]
    else: 
        for i in range(len(hist)):
            p.append(float(hist[i]) / hist_sum)
    return p    


def histogram(img):
    im_min = 0
    im_max = 255
    hist = [0] * (im_max + 1 - im_min)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
                hist[img[i,j]-im_min] = hist[img[i,j]-im_min] + 1
    return hist
        
def colorHistogram(img):
    # this function builds the RGB color threshold of an image
    im_min = 0
    im_max = 16**3 - 1
    hist = [0] * 16 **3
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
                 index = (img[i,j][0]/16)*16**2+(img[i,j][1]/16)*16+(img[i,j][2]/16)
                 hist[index] = hist[index] +1       
    return hist

def thresImg(img, level=2):
    # this function thresholds the given image
    return

def main():
    # parse command line options
    try:
        print 'argv: '+ str(sys.argv)
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
