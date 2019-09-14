import cv2
img=cv2.imread('1.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,100,100)
cv2.imshow('orginal',img)
cv2.imshow('gray',gray)
cv2.imshow('canny detector',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
