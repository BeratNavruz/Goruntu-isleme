import cv2
import numpy as np

lionIsPhoto = cv2.imread("lion.jpg",0)

cv2.imshow("lion Photo",lionIsPhoto)
satir,sutun=lionIsPhoto.shape

dizi = np.zeros(256)

for i in range(satir):
    for j in range(sutun):
        pixel=lionIsPhoto[i,j]
        dizi[pixel]=dizi[pixel]+1

print(dizi)


cv2.waitKey(0)
cv2.destroyAllWindows()
