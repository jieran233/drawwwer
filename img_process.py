import cv2


def img_process(input_image, max_size):

    # 获取原图像尺寸
    height, width = input_image.shape

    # 计算缩放比例
    scale = min(max_size / width, max_size / height)

    # 缩放图像（不使用插值算法）
    resized_image = cv2.resize(input_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)

    # 反色处理
    inverted_image = cv2.bitwise_not(resized_image)

    # 自适应阈值处理
    binary_image = cv2.adaptiveThreshold(inverted_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, 2)

    return binary_image


if __name__ == '__main__':
    image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
    image_processed = img_process(image)
    # 显示处理后的图像
    cv2.imshow('Binary Image', image_processed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
