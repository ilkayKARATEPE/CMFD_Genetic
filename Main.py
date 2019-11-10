import SiftMach
import Genetic
import cv2 as cv
import numpy as np
import pandas as pd

img_gray = cv.imread("im48_t.bmp", cv.IMREAD_GRAYSCALE)
img_rgb = cv.imread("im48_t.bmp", cv.IMREAD_COLOR)

df = pd.read_csv('masks_backup.csv', sep=';', index_col=['id'])

<<<<<<< HEAD
df = pd.read_excel("masks.xlsx")

read_matrix = df[['mask']].to_numpy()

filter = read_matrix[0][0]
filter1 = read_matrix[1][0]

print(np.matrix(filter))

print(np.matrix(filter1))

#x = siftmach.apply_sift(img_gray, img_rgb)
#print(x)
=======
siftmach_class = SiftMach.SiftMach(150, 40)
genetic_class = Genetic.Genetic(3, df)

for index, gen_mask in enumerate(genetic_class.get_generation()):
    destination_gray_img = cv.filter2D(img_gray, -1, gen_mask)
    x = siftmach_class.apply_sift(destination_gray_img, img_rgb)
    cv.imshow("mask: " + str(index), destination_gray_img)
    print("index: {} →→ eslesen {} nokta".format(index + 1, x))
>>>>>>> master

cv.waitKey(0)
cv.destroyAllWindows()
