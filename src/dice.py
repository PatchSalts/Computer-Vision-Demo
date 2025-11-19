import cv2 as cv
from matplotlib import pyplot as plt

def processdice(imgfname):
    img = cv.imread(imgfname, cv.IMREAD_GRAYSCALE)
    hst = cv.calcHist([img], [0], None, [256], [0, 255])
    plt.xkcd()
    plt.subplot(1, 2, 1)
    plt.title("Image")
    plt.imshow(img)
    plt.subplot(1, 2, 2)
    plt.title("Histogram")
    plt.plot(hst)
    plt.show()

if __name__ == "__main__":
    imgfnames = [ \
        "images/dice/roll1.jpg", \
        # "images/dice/roll2.jpg", \
        # "images/dice/roll3.jpg", \
        # "images/dice/roll4.jpg", \
        # "images/dice/roll5.jpg", \
        # "images/dice/roll6.jpg", \
        # "images/dice/roll7.jpg", \
        # "images/dice/roll8.jpg", \
    ]

    for imgfname in imgfnames:
        processdice(imgfname)
