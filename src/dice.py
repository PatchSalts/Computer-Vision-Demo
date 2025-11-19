import cv2 as cv
from matplotlib import pyplot as plt

def analyzedice(imgfname):
    img = cv.imread(imgfname)
    gry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    hst = cv.calcHist([gry], [0], None, [256], [0, 255])
    plt.xkcd()
    plt.subplot(1, 2, 1)
    plt.title("Image")
    plt.imshow(img)
    plt.subplot(1, 2, 2)
    plt.title("Histogram")
    plt.plot(hst)
    plt.show()

if __name__ == "__main__":
    imgfpaths = [ \
        "images/dice/roll1.jpg", \
        "images/dice/roll2.jpg", \
        # "images/dice/roll3.jpg", \
        # "images/dice/roll4.jpg", \
        # "images/dice/roll5.jpg", \
        # "images/dice/roll6.jpg", \
        # "images/dice/roll7.jpg", \
        # "images/dice/roll8.jpg", \
    ]

    for imgfpath in imgfpaths:
        analyzedice(imgfpath)
