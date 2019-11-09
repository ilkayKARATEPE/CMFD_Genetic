import SiftMach
import cv2 as cv
import numpy as np
import pandas as pd

img_gray = cv.imread("im41_t.bmp", cv.IMREAD_GRAYSCALE)
img_rgb = cv.imread("im41_t.bmp", cv.IMREAD_COLOR)

siftmach = SiftMach.SiftMach(150, 40)

df = pd.read_excel("masks.xlsx", index_col=0)
print(df)

x = siftmach.apply_sift(img_gray, img_rgb)
print(x)

cv.waitKey(0)
cv.destroyAllWindows()
