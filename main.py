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

    # Draw rectangular roi
    rect_roi = roi_helper.draw_rectangle(frame, 3)
    print("Rectangle Example:")
    pprint(rect_roi)

    frame_temp = roi_helper.visualize_roi(frame, rect_roi)
    cv2.imshow("frame", frame_temp)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    # Draw line roi
    line_roi = roi_helper.draw_line(frame, 3)
    print("Line Example:")
    pprint(line_roi)

    frame_temp = roi_helper.visualize_roi(frame, line_roi)
    cv2.imshow("frame", frame_temp)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    # cv2.imshow("frame", frame)
    # key = cv2.waitKey(0)
    # if key & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()