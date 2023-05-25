import cv2
import numpy as np

kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
kernely = np.array([[0, -1], [1, 0]], dtype=int)
def cv_filter(kernel_x, kernel_y, grayImage):
  # 计算梯度
  x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
  y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)

  # 调用convertScaleAbs()函数计算绝对值，
  # 并将图像转换为8位图进行显示，然后进行图像融合
  absX = cv2.convertScaleAbs(x)
  absY = cv2.convertScaleAbs(y)
  Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
  return Roberts

# 使用 Numpy 构建卷积核，并对灰度图像在 x 和 y 的方向上做一次卷积运算
# Roberts 算子
def roberts(img):
  return cv_filter(kernelx, kernely, img)