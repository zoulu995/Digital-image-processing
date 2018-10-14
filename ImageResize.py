# -*- coding: utf-8 -*-

"""
重设图像大小。
缩小图像，比例为（0.3, 0.5）
放大图像，比例为（1.6, 1.2）
"""

__author__ = 'zouyuhang'

import cv2
import os

if __name__ == '__main__':
    img = cv2.imread("images/pku.jpg", -1)
    if img == None:
        print("Error: could not load image")
        os._exit(0)

    height, width = img.shape[:2]

    # 缩小图像
    size = (int(width * 0.3), int(height * 0.5))
    shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

    # 放大图像
    fx = 1.6
    fy = 1.2
    enlarge = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)

    # 显示
    cv2.imshow("src", img)
    cv2.imshow("shrink", shrink)
    cv2.imshow("enlarge", enlarge)

    cv2.waitKey(0)