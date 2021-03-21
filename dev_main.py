import cv2
from pprint import pprint

from EasyROI.easyROI import EasyROI



if __name__=='__main__':
    video_path = 'input/overpass.mp4'

    # Initialize cam
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), 'Cannot capture source'
    ret, frame = cap.read()

    roi_helper = EasyROI(verbose=True)

    # DRAW RECTANGULAR ROI
    rect_roi = roi_helper.draw_rectangle(frame, 3)
    print("Rectangle Example:")
    pprint(rect_roi)

    frame_temp = roi_helper.visualize_roi(frame, rect_roi)

    # crop drawn rectangles
    cropped_rects = roi_helper.crop_roi(frame, rect_roi)
    for index, crop in cropped_rects.items():
        cv2.imshow(str(index), crop)

    cv2.imshow("frame", frame_temp)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()


    # DRAW LINE ROI
    line_roi = roi_helper.draw_line(frame, 3)
    print("Line Example:")
    pprint(line_roi)

    frame_temp = roi_helper.visualize_roi(frame, line_roi)
    cv2.imshow("frame", frame_temp)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()


    # DRAW CIRCLE ROI
    circle_roi = roi_helper.draw_circle(frame, 3)
    print("Circle Example:")
    pprint(circle_roi)

    frame_temp = roi_helper.visualize_roi(frame, circle_roi)

    # crop drawn circles
    cropped_circles = roi_helper.crop_roi(frame, circle_roi)
    for index, crop in cropped_circles.items():
        cv2.imshow(str(index), crop)

    cv2.imshow("frame", frame_temp)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()


    # DRAW POLYGON ROI
    polygon_roi = roi_helper.draw_polygon(frame, 3)
    print("Polygon Example:")
    pprint(polygon_roi)

    frame_temp = roi_helper.visualize_roi(frame, polygon_roi)

    # crop drawn polygons
    cropped_polys = roi_helper.crop_roi(frame, polygon_roi)
    for index, crop in cropped_polys.items():
        cv2.imshow(str(index), crop)

    cv2.imshow("frame", frame_temp)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()


    # # '''
    # cv2.imshow("frame", frame)
    # key = cv2.waitKey(0)
    # if key & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    # # '''