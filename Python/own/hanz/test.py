import cv2

image = cv2.imread(r"./img/$8.jpg")
cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# with open('./img', 'r') as f:
#     pass
