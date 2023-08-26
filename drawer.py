import cv2
from img_process import img_process
from img2lists import img2lists
import mouse
from time import time, sleep
from sys import argv


def draw(pixel_lists, scale=1, draw_position_point=True, interlaced=True):
    initial_pos = mouse.get_position()

    def _draw_position_point():
        x, y = len(pixel_lists[0])*scale, len(pixel_lists)*scale
        points = [initial_pos, (initial_pos[0]+x, initial_pos[1]),
                  (initial_pos[0], initial_pos[1]+y), (initial_pos[0]+x, initial_pos[1]+y)]
        for point in points:
            mouse.move(point[0], point[1])
            mouse.click()
        mouse.move(initial_pos[0], initial_pos[1])

    if draw_position_point:
        print(':: Drawing position point')
        _draw_position_point()
        print(':: Start drawing officially after 3 seconds')
        sleep(3)

    def _draw(_pixel_lists):
        current_pos = initial_pos
        for row in _pixel_lists:
            current_pos = (initial_pos[0], current_pos[1] + 1 * scale)
            if row == -1:
                continue
            mouse.move(current_pos[0], current_pos[1])
            for pixel in row:
                current_pos = (current_pos[0] + 1 * scale, current_pos[1])
                mouse.move(current_pos[0], current_pos[1])
                if pixel == 1:
                    mouse.click()
                print(f"[{'x' if pixel == 1 else ' '}]{current_pos}")

    if interlaced:
        def _interlaced_blank(original_list, even_or_odd):  # 0: even, 1: odd
            modified_list = []
            for i, row in enumerate(original_list):
                if i % 2 == even_or_odd:
                    modified_list.append(-1)
                else:
                    modified_list.append(row)
            return modified_list

        even_row = _interlaced_blank(pixel_lists, 0)
        _draw(even_row)
        odd_row = _interlaced_blank(pixel_lists, 1)
        _draw(odd_row)
    else:
        _draw(pixel_lists)


if __name__ == '__main__':
    image = cv2.imread('image.png' if len(argv) == 1 else argv[1], cv2.IMREAD_GRAYSCALE)
    image_processed = img_process(image, max_size=256)  # set max size of picture
    cv2.imshow('image_processed', image_processed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    lists = img2lists(image_processed)
    print(':: Start drawing after 5 seconds')
    sleep(5)
    start_time = time()
    # set scale of drawing, switch draw_position_point, and interlaced
    draw(lists, scale=2, draw_position_point=True, interlaced=True)
    end_time = time()
    print(f"Time cost: {end_time - start_time:.3f} s")
