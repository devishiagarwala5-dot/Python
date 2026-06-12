import cv2
#preparing the image to load into the memory and it'll be saved as a numpy array
IMAGE=cv2.imread('IMAGE.jpeg')
#creating a window so the image can be loaded into it
cv2.namedWindow('My first image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('My first image', 800,500)
cv2.imshow('My first image',IMAGE)
cv2.waitKey(0)
cv2.destroyAllWindows()