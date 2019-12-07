import cv2 as cv
import pandas as pd

import Genetic
import SiftMach

img_gray = cv.imread("im9_t.bmp", cv.IMREAD_GRAYSCALE)
img_rgb = cv.imread("im9_t.bmp", cv.IMREAD_COLOR)
df = pd.read_csv('masks_backup.csv', sep=';', index_col=['id'])

siftmach_class = SiftMach.SiftMach(150, 40)
genetic_class = Genetic.Genetic(3, df)

while True:
    for index, gen_mask in enumerate(genetic_class.get_generation()):
        destination_gray_img = cv.filter2D(img_gray, -1, gen_mask)
        amount_of_match = siftmach_class.apply_sift(destination_gray_img, img_rgb)
        print(genetic_class.get_actual_generation_index()[index])
        df.loc[genetic_class.get_actual_generation_index()[index], "match"] = amount_of_match

        # cv.imshow("mask: " + str(index), destination_gray_img)

        print("index: {} →→ eslesen {} nokta".format(index + 1, amount_of_match))

    df.to_csv('mask.csv', sep=';', encoding='utf-8')
    if not genetic_class.selection():
        break
    else:
        if not genetic_class.generate_new_population():
            break

df_final = pd.read_csv('mask.csv', sep=';', index_col=['id'])
best_mask = genetic_class.string_to_matrix(df_final.loc[df_final['match'].idxmax()]['mask'])
print(best_mask)

destination_gray_img = cv.filter2D(img_gray, -1, best_mask)
siftmach_class.apply_sift_final(destination_gray_img, img_rgb)

cv.waitKey(0)
cv.destroyAllWindows()
