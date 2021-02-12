import cv2


def visualize_rect(img, roi_dict, color=(0, 255, 0)):
    for index, roi in roi_dict.items():
        tl_x = roi['roi']['tl_x']
        tl_y = roi['roi']['tl_y']
        br_x = roi['roi']['br_x']
        br_y = roi['roi']['br_y']

        cv2.rectangle(img, (tl_x, tl_y), (br_x, br_y), color, 2)

    return img


def visualize_line(img, roi_dict, color=(0, 255, 0)):
    for index, roi in roi_dict.items():
        pt1 = roi['roi']['point1']
        pt2 = roi['roi']['point2']

        cv2.line(img, pt1, pt2, color, 2)

    return img