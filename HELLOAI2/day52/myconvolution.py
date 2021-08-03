import cv2


# original = cv2.imread(fname, cv2.IMREAD_COLOR)
gray = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
# unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

# cv2.imshow('Original', original)
cv2.imshow('black', gray)

print(len(gray))
print(len(gray[0]))
# cv2.imshow('Unchange', unchange)



cv2.waitKey(0)
cv2.destroyAllWindows()