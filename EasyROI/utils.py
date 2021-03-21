import cv2
import numpy as np

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


def crop_rect(img, roi_dict):
    cropped_images = {}
    
    for index, roi in roi_dict['roi'].items():
        tl_x = roi['tl_x']
        tl_y = roi['tl_y']
        br_x = roi['br_x']
        br_y = roi['br_y']

        cropped_images[index] = img[tl_y:br_y, tl_x:br_x]

    return cropped_images


def crop_circle(img, roi_dict):
    cropped_images = {}
    
    for index, roi in roi_dict['roi'].items():
        center = roi['center']
        radius = roi['radius']

        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        cv2.circle(mask, center, radius, (255, 255, 255), -1)

        _, thresh = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

        masked_image = cv2.bitwise_and(img, img, mask=mask)

        tl_x, tl_y = center[0] - radius, center[1] - radius
        br_x, br_y = center[0] + radius, center[1] + radius

        cropped_images[index] = masked_image[tl_y:br_y, tl_x:br_x]

    return cropped_images


def crop_polygon(img, roi_dict):
    cropped_images = {}
    
    num_channel = img.shape[2]
    mask_color = (255,) * num_channel

    for index, roi in roi_dict['roi'].items():
        poly_vertices = roi['vertices']
        poly_vertices = np.array(poly_vertices, dtype=np.int32)

        # print(poly_vertices)

        tl_x, tl_y = np.min(poly_vertices, axis=0)
        br_x, br_y = np.max(poly_vertices, axis=0)

        # print(tl_x, tl_y, br_x, br_y)

        mask = np.zeros(img.shape, dtype=np.uint8)

        # fill the ROI so it doesn't get wiped out when the mask is applied
        cv2.fillConvexPoly(mask, poly_vertices, mask_color)

        # apply the mask
        masked_image = cv2.bitwise_and(img, mask)

        cropped_images[index] = masked_image[tl_y:br_y, tl_x:br_x]

    return cropped_images