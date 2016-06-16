import cv2

img = cv2.imread('../BoardRecognizer/tests/state1.png', 0)

clahe = cv2.createCLAHE(clipLimit=20.0, tileGridSize=(32,32))
applied = clahe.apply(img)
cv2.imshow('CLAHE applied', applied)
cv2.imshow('Without CLAHE', img)
print applied
cv2.waitKey(20)
raw_input()
