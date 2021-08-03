import cv2
import numpy as np
from numpy import dtype

gray = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

arr_n = np.array(gray)
print(arr_n.dtype)

filter = [[0,1],
          [1,0]]

filter_n = np.array(filter)

out_n = np.zeros((256,256), dtype=np.uint8)


for i in range(256):
    for j in range(256):
        sum = 0
        s1 = arr_n[i*2][j*2]     *  filter_n[0][0]
        s2 = arr_n[i*2][j*2+1]   *  filter_n[0][1]
        s3 = arr_n[i*2+1][j*2]   *  filter_n[1][0]
        s4 = arr_n[i*2+1][j*2+1] *  filter_n[1][1]
        sum = (s1 + s2 + s3 + s4) / 4
        
        out_n[i][j] = sum
        
        
cv2.imshow('black', out_n)
# cv2.imshow('black', arr_n)

cv2.waitKey(0)
cv2.destroyAllWindows()