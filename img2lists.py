import cv2
import numpy as np


def img2lists(input_image):

    # 设置阈值，用于判断偏向黑色还是白色
    threshold = 128

    # 将图像数据转换为NumPy数组
    image_array = np.array(input_image)

    # 将图像数组中小于阈值的像素设置为1，大于等于阈值的像素设置为0
    binary_array = np.where(image_array < threshold, 1, 0)

    # 获取二维列表
    binary_list = binary_array.tolist()

    return binary_list


if __name__ == '__main__':
    image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
    lists = img2lists(image)
    print(lists)
