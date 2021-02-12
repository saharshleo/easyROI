import cv2
from copy import deepcopy

from .utils import *


class EasyROI:
    def __init__(self, verbose=False):
        self.verbose = verbose

        if self.verbose:
            print("[DEBUG] Welcome to easyROI")

        self.init_variables()


    def init_variables(self):
        cv2.destroyAllWindows()

        # Draw roi parameters
        self.roi_dict = dict()
        
        self.drawing = False # true if mouse is pressed
        self.img = None
        
        '''
        1 ==> Draw Rectangle
        2 ==> Draw Line
        3 ==> Draw Circle
        4 ==> Draw Cuboid
        '''
        self.quantity = 0
        
        self.brush_color_ongoing = [255, 0, 0]
        self.brush_color_finished = [0, 255, 0]
        
        self.cursor_x, self.cursor_y = -1, -1   # cursor coordinates

        self.orig_frame = []
        self.pure_orig_frame = []
        
        self.line_drawn = []


    def draw_line(self, frame, quantity=1):
        if self.verbose:
            print("[DEBUG] Entered draw_line")

        self.img = frame.copy()
        self.quantity = quantity

        window_name = "Draw {} Lines".format(self.quantity)
        cv2.namedWindow(window_name)
        cv2.setMouseCallback(window_name, self.draw_line_callback)    # windowName, callbackFunction

        self.pure_orig_frame = deepcopy(self.img)
        self.orig_frame = deepcopy(self.img)

        self.line_drawn = [False for _ in range(self.quantity)]

        while True:
            cv2.imshow(window_name, self.img)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or (len(self.line_drawn)>0 and self.line_drawn[-1]):
                cv2.destroyWindow(window_name)
                self.line_drawn = []
                break

        if self.verbose and len(self.roi_dict) != self.quantity:
            print("[DEBUG] Not all ROI's drawn")
            self.roi_dict = dict()

        roi_dict_temp = self.roi_dict

        self.init_variables()

        return roi_dict_temp


    def draw_rectangle(self, frame, quantity=1):
        if self.verbose:
            print("[DEBUG] Entered draw_rectangle")

        self.img = frame.copy()
        self.quantity = quantity

        for i in range(self.quantity):
            roi_ = cv2.selectROI("Draw {} Rectangle(s)".format(self.quantity), self.img, showCrosshair=False, fromCenter=False)
            print()

            tl_x, tl_y, w, h = roi_
            br_x = tl_x + w
            br_y = tl_y + h

            if self.verbose and (not w or not h):
                print("[DEBUG] Not all ROI's drawn")
                return dict()

            self.img = cv2.rectangle(self.img, (tl_x, tl_y), (br_x, br_y), self.brush_color_finished, 2)

            self.roi_dict[i] = dict()
            self.roi_dict[i]['roi'] = {
                'tl_x': tl_x,
                'tl_y': tl_y,
                'br_x': br_x,
                'br_y': br_y,
                'w': w,
                'h':h
            }

            self.roi_dict[i]['type'] = 'rectangle'

        roi_dict_temp = self.roi_dict

        self.init_variables()

        return roi_dict_temp


    def draw_cuboid(self, frame, quantity=1):
        pass


    def draw_circle(self, frame, quantity=1):
        pass


    def draw_line_callback(self, event, x, y, flags, param): 
        '''
        callback for mouse events while drawing line roi
        '''

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.cursor_x, self.cursor_y = x, y

        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            self.img = deepcopy(self.orig_frame)
            cv2.line(self.img, (self.cursor_x, self.cursor_y), (x, y), tuple(self.brush_color_ongoing), 2)
        
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False

            # get index of line drawn
            line_index = -1
            for i in range(len(self.line_drawn)):
                if not self.line_drawn[i]:
                    line_index = i
                    break

            cv2.line(self.img, (self.cursor_x, self.cursor_y), (x, y), tuple(self.brush_color_finished), 2)
            
            self.roi_dict[line_index] = dict()
            self.roi_dict[line_index]['roi'] = {
                'point1': (self.cursor_x, self.cursor_y),
                'point2': (x, y)
            }

            self.roi_dict[line_index]['type'] = 'line'
            
            self.orig_frame = deepcopy(self.img)

            self.line_drawn[line_index] = True


    def __del__(self):
        cv2.destroyAllWindows()

        if self.verbose:
            print("Thank You!!")


    def visualize_roi(self, frame, roi_dict):
        if len(roi_dict) <= 0:
            return frame

        img = frame.copy()

        if roi_dict[0]['type'] == 'rectangle':
            img = visualize_rect(img, roi_dict)
            
        elif roi_dict[0]['type'] == 'line':
            img = visualize_line(img, roi_dict)

        elif roi_dict[0]['type'] == 'circle':
            pass

        elif roi_dict[0]['type'] == 'cuboid':
            pass
        
        return img