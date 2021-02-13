import cv2


def visualize_rect(img, roi_dict, color=(0, 255, 0)):
    for index, roi in roi_dict['roi'].items():
        tl_x = roi['tl_x']
        tl_y = roi['tl_y']
        br_x = roi['br_x']
        br_y = roi['br_y']

        cv2.rectangle(img, (tl_x, tl_y), (br_x, br_y), color, 2)

    return img


def visualize_line(img, roi_dict, color=(0, 255, 0)):
    for index, roi in roi_dict['roi'].items():
        pt1 = roi['point1']
        pt2 = roi['point2']

        cv2.line(img, pt1, pt2, color, 2)

    return img


def visualize_circle(img, roi_dict, color=(0, 255, 0)):
    for index, roi in roi_dict['roi'].items():
        center = roi['center']
        radius = roi['radius']

        cv2.circle(img, center, radius, color, 2)

    return img


def visualize_polygon(img, roi_dict, color=(0, 255, 0)):
    for index, roi in roi_dict['roi'].items():
        poly_vertices = roi['vertices']

        for v in range(1, len(poly_vertices)):
            cv2.line(img, poly_vertices[v], poly_vertices[v-1], color, 2)

        cv2.line(img, poly_vertices[0], poly_vertices[-1], color, 2)

    return img