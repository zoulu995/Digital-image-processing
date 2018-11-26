# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img1=cv2.imread('lena1.png',0)
# dft=cv2.dft(np.float32(img1),flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift=np.fft.fftshift(dft)
# magnitude_spectrum=20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
# plt.subplot(1,2,1),plt.imshow(img1)
# plt.title('input image'),plt.xticks([]),plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(magnitude_spectrum)
# plt.title('magnitude spectrum'),plt.xticks([]),plt.yticks([])
# plt.show()

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img1=cv2.imread('lena1.png',0)
# f=np.fft.fft2(img1)
# fshift=np.fft.fftshift(f)
# rows,cols=img1.shape
# crow,ccol=np.ceil(rows/2),np.ceil(cols/2)
# crow,ccol=np.int(crow),np.int(ccol)
# #注意fshift是用来与原图像进行掩模操作的但是具体的，我也看着很抽象。这一部分与低通的有些相对的意思。
# fshift[crow-30:crow+30,ccol-30:ccol+30]=0
# f_ishift=np.fft.ifftshift(fshift)
# img_back=np.fft.ifft2(fshift)
# img_back=np.abs(img_back)
# plt.subplot(1,2,1),plt.imshow(img1)
# plt.title('input image'),plt.xticks([]),plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(img_back)
# plt.title('image after HPF'),plt.xticks([]),plt.yticks([])
# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt
img1=cv2.imread('lena.png',0)
f=np.fft.fft2(img1)
fshift=np.fft.fftshift(f)
rows,cols=img1.shape
crow,ccol=np.ceil(rows/2),np.ceil(cols/2)
crow,ccol=np.int(crow),np.int(ccol)
#fshift是用来与原图像进行掩模操作
fshift[crow-30:crow+30,ccol-30:ccol+30]=0
f_ishift=np.fft.ifftshift(fshift)
img_back=np.fft.ifft2(fshift)
img_back=np.abs(img_back)
plt.subplot(1,2,1),plt.imshow(img1)
plt.title('input image'),plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img_back)
plt.title('image after HPF'),plt.xticks([]),plt.yticks([])
plt.show()

