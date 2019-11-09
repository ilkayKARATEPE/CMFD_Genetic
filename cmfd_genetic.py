import cv2 as cv
import numpy as np


img_gray = cv.imread("im41_t.bmp", cv.IMREAD_GRAYSCALE)
img_rgb = cv.imread("im41_t.bmp", cv.IMREAD_COLOR)

img_gray = cv.resize(img_gray, (int(img_gray.shape[1] * 40 / 100), int(img_gray.shape[0] * 40 / 100)))
img_rgb = cv.resize(img_rgb, (int(img_rgb.shape[1] * 40 / 100), int(img_rgb.shape[0] * 40 / 100)))

#ret, img_gray = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

sift = cv.xfeatures2d.SIFT_create()
keypoints_sift, descriptors = sift.detectAndCompute(img_gray, None)
img = cv.drawKeypoints(img_rgb, keypoints_sift,  None)
cv.imshow(" All Keypoints ", img)

pts1 = np.array([], np.int32)
pts2 = np.array([], np.int32)

for index_dis, key_desc_dis in enumerate(descriptors):  # dist = numpy.linalg.norm(a-b)
    for index_ic in range(index_dis + 1, len(keypoints_sift)):
        point1_x = int(round(keypoints_sift[index_dis].pt[0]))
        point1_y = int(round(keypoints_sift[index_dis].pt[1]))
        point2_x = int(round(keypoints_sift[index_ic].pt[0]))
        point2_y = int(round(keypoints_sift[index_ic].pt[1]))
        if point1_x == point2_x & point1_y == point2_y:
            print("benzer keypoints")
            continue

        dist = np.linalg.norm(key_desc_dis - descriptors[index_ic])

        if dist < 200:
            cv.circle(img_rgb, (round(keypoints_sift[index_dis].pt[0]), round(keypoints_sift[index_dis].pt[1])), 4,
                      (0, 0, 255),
                      -1)  # eslesen objeyi isaretlemek icin
            print([round(keypoints_sift[index_dis].pt[0]), round(keypoints_sift[index_dis].pt[1])])
            print([(keypoints_sift[index_dis].pt[0]), (keypoints_sift[index_dis].pt[1])])

            cv.circle(img_rgb, (round(keypoints_sift[index_ic].pt[0]), round(keypoints_sift[index_ic].pt[1])), 4,
                      (255, 0, 0),
                      -1)  # eslesen objeyi isaretlemek icin
            print([round(keypoints_sift[index_ic].pt[0]), round(keypoints_sift[index_ic].pt[1])])
            print([(keypoints_sift[index_ic].pt[0]), (keypoints_sift[index_ic].pt[1])])
            print("------")

            img_line = cv.line(img_rgb,
                               (round(keypoints_sift[index_dis].pt[0]), round(keypoints_sift[index_dis].pt[1])),
                               (round(keypoints_sift[index_ic].pt[0]), round(keypoints_sift[index_ic].pt[1])),
                               (0, 255, 0), 1)

cv.imshow("Image", img_rgb)
cv.waitKey(0)
cv.destroyAllWindows()

'''
cv.circle(img_rgb, (round(keypoints_sift[index_dis].pt[0]), round(keypoints_sift[index_dis].pt[1])), 4,
                      (0, 0, 0),
                      1)  # eslesen objeyi isaretlemek icin
            cv.polylines(img_rgb, (round(keypoints_sift[index_ic].pt[0]), round(keypoints_sift[index_ic].pt[1])), 1,
                      (255, 0, 0),
                      -1)  # eslesen objeyi isaretlemek icin'''

'''
pts1 = np.append(pts1, [round(keypoints_sift[index_dis].pt[0]), round(keypoints_sift[index_dis].pt[1])])

            pts2 = np.append(pts2, [round(keypoints_sift[index_ic].pt[0]), round(keypoints_sift[index_ic].pt[1])])

    pts1 = pts1.reshape((-1, 1, 2))
    pts2 = pts2.reshape((-1, 1, 2))
    cv.polylines(img_rgb, [pts1], 1, (255, 255, 255))
    cv.polylines(img_rgb, [pts2], 1, (0, 0, 255))

'''
