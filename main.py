import cv2 as cv
img = cv.imread(r'E:\Dang Nhan\Python programs\Open CV\tet.jpg',cv.IMREAD_COLOR)
cv.imshow('Result', img)
cv.waitKey()
cv.destroyAllWindows()