import cv2

img = cv2.imread("image.jpg")

print("Shape:", img.shape)
print("Pixel:", img[0][0])