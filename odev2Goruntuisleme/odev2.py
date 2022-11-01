import cv2
import numpy as np

lionIsPhoto = cv2.imread("lion.jpg",0)
cv2.imshow("lion Photo",lionIsPhoto)

satir,sutun=lionIsPhoto.shape

for i in range(satir):
    for j in range(sutun):
        lionIsPhoto[i,j]=np.max(lionIsPhoto)-lionIsPhoto[i,j]

cv2.imshow("Ters lion Photo",lionIsPhoto)


cv2.waitKey(0)
cv2.destroyAllWindows()