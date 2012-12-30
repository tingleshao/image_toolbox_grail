import sys
import getopt
from scipy import misc
import pylab as pl

__doc__ = 'this is doc!'

def process(arg):
    print "args: " + arg
    l2rgb = misc.imread('me.jpeg')
    l2 = l2rgb[:,:,0]
    pl.imshow(l2rgb[:,:,0],cmap=pl.cm.gray) 

    t = otsu(l2)
    print t 
    for i in range(l2.shape[0]):
        for j in range(l2.shape[1]):
            if l2[i,j] <= t:
                l2[i,j] = 0
            else:
                l2[i,j] = 255
    pl.imshow(l2,cmap=pl.cm.gray)
    pl.axis('off')
    pl.show()
  

def otsu(img):
    # this function outputs a threshold
    hist = histogram(img)
    delta_b_sq = [] 
    for t in range(1,len(hist)):
        p0 = calculateP(hist[0:t],sum(hist))
        p1 = calculateP(hist[t:len(hist)],sum(hist))
        w0 = sum(p0)
        w1 = sum(p1)
        u0 = sum([a*b for a,b in zip(range(0,t),p0)])
        u1 = sum([a*b for a,b in zip(range(t,len(hist)-1),p1)])
        delta_b_sq.append(w0*w1*((u0-u1)**2)) 
    # find maximum 
    t = delta_b_sq.index(max(delta_b_sq))
    return t

def calculateP(hist,hist_sum):
    # this function calculates the probability given the histogram
    # the histogram can be a sub histogram in a larger one
    p = []
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


