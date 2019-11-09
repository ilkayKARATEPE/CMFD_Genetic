import SiftMach
import cv2 as cv
import numpy as np
import pandas as pd

img_gray = cv.imread("im41_t.bmp", cv.IMREAD_GRAYSCALE)
img_rgb = cv.imread("im41_t.bmp", cv.IMREAD_COLOR)

siftmach = SiftMach.SiftMach(150, 40)

df = pd.read_excel("masks.xlsx")

read_matrix = df[['mask']].to_numpy()

filter = read_matrix[0][0]
filter1 = read_matrix[1][0]

print(np.matrix(filter))

print(np.matrix(filter1))

#x = siftmach.apply_sift(img_gray, img_rgb)
#print(x)

cv.waitKey(0)
cv.destroyAllWindows()
