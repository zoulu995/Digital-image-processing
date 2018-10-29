from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np



def gamma_plot(c, v):
    x = np.arange(0, 256, 0.01)
    y = c * x ** v
    plt.plot(x, y, 'r', linewidth=1)
    plt.title('伽马变换函数')
    plt.xlim([0, 255]), plt.ylim([0, 255])
    plt.show()


def gamma(img, c, v):
    lut = np.zeros(256, dtype=np.float32)
    for i in range(256):
        lut[i] = c * i ** v
    output_img = cv2.LUT(img, lut)
    output_img = np.uint8(output_img + 0.5)
    return output_img


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWidgets()

    def creatWidgets(self):
        self.SelecLable = Label(self, text='请选择图片：').grid(row=0, column=0, sticky=E)
        self.SelecBt = Button(self, text='选择', command=self.SelectImag).grid(sticky=W, row=0, column=1)
        self.FuncLable = Label(self, text='数字图像功能列表').grid(row=1, columnspan=2)
        self.Fun1Bt = Button(self, text='图像取反', command=self.image1).grid(row=2, column=0, sticky=E)
        self.Fun2Bt = Button(self, text='图像缩放', command=self.image2).grid(row=2, column=1, sticky=W)
        self.Fun3Bt = Button(self, text='直方图均衡', command=self.image3).grid(row=3, column=0, sticky=E)
        self.Fun4Bt = Button(self, text='幂次变换', command=self.image4).grid(row=3, column=1, sticky=W)
        self.ExitBt = Button(self, text='退出', command=self.quit).grid(row=4, columnspan=2)
        # self.Image = Canvas(self,bg='white',width=200,height=200).grid(row=5, columnspan=2)

    def SelectImag(self):
        self.File = filedialog.askopenfilename(parent=self, initialdir="C:/", title='选择一个图片.')
        print(self.File)
        self.im = Image.open(self.File)
        self.im.resize((200, 200))
        self.filename = ImageTk.PhotoImage(self.im)
        self.Image = self.filename  # <--- keep reference of your image
        self.ImagLable = Label(self, image=self.Image).grid(row=5, columnspan=2)
        # self.Image.create_image(0, 0, anchor='nw', image=self.filename)

    def cv_imread(self, filePath):
        cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
        return cv_img
    def cv_imread1(self, filePath):
        cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), 1)
        return cv_img
    #图像取反
    def image1(self):
        print("image1:" + self.File)
        name = self.cv_imread1(self.File)
        if name == None:
            print("Error: could not load image")
            os._exit(0)
        rgb_img = name
        reverse_img = 255 - rgb_img
        cv2.imshow('reverse image', reverse_img)

    # 图像缩放
    def image2(self):
        print("image2:" + self.File)
        img = self.cv_imread(self.File)
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

    # 直方图均衡化
    def image3(self):
        print("image1:" + self.File)
        name = self.cv_imread1(self.File)
        if name == None:
            print("Error: could not load image")
            os._exit(0)


    #幂次变换
    def image4(self):
        print("image4:" + self.File)
        img_input = self.cv_imread(self.File)
        if img_input == None:
            print("Error: could not load image")
            os._exit(0)
        cv2.imshow('imput', img_input)
        gamma_plot(0.00000005, 4.0)
        img_output = gamma(img_input, 0.00000005, 4.0)
        cv2.imshow('output', img_output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



app = Application()
app.master.title("北大软微数字图像课——邹宇航")
app.master.geometry('400x400+500+70')
app.mainloop()
