"""幂律变换（伽马）"""
import numpy as np
import matplotlib.pyplot as plt
import cv2


def gamma_plot(c, v):
    x = np.arange(0, 256, 0.01)
    y = c*x**v
    plt.plot(x, y, 'r', linewidth=1)
    plt.title('伽马变换函数')
    plt.xlim([0, 255]), plt.ylim([0, 255])
    plt.show()


def gamma(img, c, v):
    lut = np.zeros(256, dtype=np.float32)
    for i in range(256):
        lut[i] = c * i ** v
    output_img = cv2.LUT(img, lut)
    output_img = np.uint8(output_img+0.5)
    return output_img


img_input = cv2.imread('images/heci2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('imput', img_input)
gamma_plot(0.00000005, 4.0)
img_output = gamma(img_input, 0.00000005, 4.0)
cv2.imshow('output', img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
