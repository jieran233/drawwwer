import cv2
from img_process import img_process
from img2lists import img2lists
import mouse
from time import sleep
from sys import argv


def draw(pixel_lists, scale=1):
    initial_pos = mouse.get_position()
    current_pos = initial_pos
    for row in pixel_lists:
        current_pos = (initial_pos[0], current_pos[1] + 1*scale)
        mouse.move(current_pos[0], current_pos[1])
        for pixel in row:
            current_pos = (current_pos[0] + 1*scale, current_pos[1])
            mouse.move(current_pos[0], current_pos[1])
            if pixel == 1:
                mouse.click()
            print(f"[{'x' if pixel == 1 else ' '}]{current_pos}")


if __name__ == '__main__':
    image = cv2.imread('image.png' if len(argv) == 1 else argv[1], cv2.IMREAD_GRAYSCALE)
    image_processed = img_process(image, max_size=256)  # set max size of picture
    cv2.imshow('image_processed', image_processed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    lists = img2lists(image_processed)
    print(':: Start painting after 5 seconds')
    sleep(5)
    draw(lists, scale=2)  # set scale of drawing
