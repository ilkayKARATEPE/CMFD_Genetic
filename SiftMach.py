import cv2 as cv
import numpy as np


class SiftMach:

    def __init__(self, dist, resize_percentage):
        self.dist = dist
        self.resize_percentage = resize_percentage

    def apply_sift(self, img_gray, img_rgb):
        img_gray = cv.resize(img_gray, (
            int(img_gray.shape[1] * self.resize_percentage / 100),
            int(img_gray.shape[0] * self.resize_percentage / 100)))
        img_rgb = cv.resize(img_rgb, (
            int(img_rgb.shape[1] * self.resize_percentage / 100), int(img_rgb.shape[0] * self.resize_percentage / 100)))

        sift = cv.xfeatures2d.SIFT_create()
        keypoints_sift, descriptors = sift.detectAndCompute(img_gray, None)
        img = cv.drawKeypoints(img_rgb, keypoints_sift, None)
        cv.imshow(" All Keypoints ", img)

        pts1 = np.array([], np.int32)
        pts2 = np.array([], np.int32)
        eslesen_keypoint = 0

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

                if dist < self.dist:
                    eslesen_keypoint += 1
                    cv.circle(img_rgb, (round(keypoints_sift[index_dis].pt[0]), round(keypoints_sift[index_dis].pt[1])),
                              4,
                              (0, 0, 255),
                              -1)  # eslesen objeyi isaretlemek icin
                    print([round(keypoints_sift[index_dis].pt[0]), round(keypoints_sift[index_dis].pt[1])])
                    print([(keypoints_sift[index_dis].pt[0]), (keypoints_sift[index_dis].pt[1])])

                    cv.circle(img_rgb, (round(keypoints_sift[index_ic].pt[0]), round(keypoints_sift[index_ic].pt[1])),
                              4,
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
        return eslesen_keypoint
