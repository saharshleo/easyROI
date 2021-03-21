import cv2
import numpy as np
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
        
        self.quantity = 0
        
        self.brush_color_ongoing = [255, 0, 0]
        self.brush_color_finished = [0, 255, 0]
        
        self.cursor_x, self.cursor_y = -1, -1   # cursor coordinates
        
        # extra vars for drawing polygon
        self.polygon_vertices = []
        self.polygon_dblclk = False

        self.orig_frame = []
        self.last_orig_frame = []
        
        self.line_drawn = []
        self.circle_drawn = []
        self.polygon_drawn = []


    def draw_line(self, frame, quantity=1):
        if self.verbose:
            print("[DEBUG] Entered draw_line")
            print("[DEBUG] Draw {} line(s)".format(quantity))
            print("[DEBUG] Drag the cursor to draw the line")
            print("[DEBUG] Press Esc to leave the process")

        self.img = frame.copy()
        self.quantity = quantity

        window_name = "Draw {} Line(s)".format(self.quantity)
        cv2.namedWindow(window_name)
        cv2.setMouseCallback(window_name, self.draw_line_callback)    # windowName, callbackFunction

        self.last_orig_frame = deepcopy(self.img)
        self.orig_frame = deepcopy(self.img)

        self.line_drawn = [False for _ in range(self.quantity)]

        self.roi_dict['type'] = 'line'
        self.roi_dict['roi'] = dict()
        
        while True:
            cv2.imshow(window_name, self.img)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or (len(self.line_drawn)>0 and self.line_drawn[-1]):
                cv2.destroyWindow(window_name)
                self.line_drawn = []
                break

        if self.verbose and len(self.roi_dict['roi']) != self.quantity:
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

        self.roi_dict['type'] = 'rectangle'
        self.roi_dict['roi'] = dict()
        
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

            self.roi_dict['roi'][i] = {
                'tl_x': tl_x,
                'tl_y': tl_y,
                'br_x': br_x,
                'br_y': br_y,
                'w': w,
                'h':h
            }

        roi_dict_temp = self.roi_dict

        self.init_variables()

        return roi_dict_temp


    def draw_polygon(self, frame, quantity=1):
        if self.verbose:
            print("[DEBUG] Entered draw_polygon")
            print("[DEBUG] Draw {} polygon(s)".format(quantity))
            print("[DEBUG] Draw multiple lines by dragging the cursor")
            print("[DEBUG] Double Click to complete the polygon")
            print("[DEBUG] Press Esc to leave the process")

        self.img = frame.copy()
        self.quantity = quantity

        window_name = "Draw {} Polygon(s)".format(self.quantity)
        cv2.namedWindow(window_name)
        cv2.setMouseCallback(window_name, self.draw_polygon_callback)    # windowName, callbackFunction

        self.last_orig_frame = deepcopy(self.img)
        self.orig_frame = deepcopy(self.img)

        self.polygon_drawn = [False for _ in range(self.quantity)]

        self.roi_dict['type'] = 'polygon'
        self.roi_dict['roi'] = dict()
        
        while True:
            cv2.imshow(window_name, self.img)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or (len(self.polygon_drawn)>0 and self.polygon_drawn[-1]):
                cv2.destroyWindow(window_name)
                self.polygon_drawn = []
                break

        if self.verbose and len(self.roi_dict['roi']) != self.quantity:
            print("[DEBUG] Not all ROI's drawn")
            self.roi_dict = dict()

        roi_dict_temp = self.roi_dict

        self.init_variables()

        return roi_dict_temp


    def draw_cuboid(self, frame, quantity=1):
        pass


    def draw_circle(self, frame, quantity=1):
        if self.verbose:
            print("[DEBUG] Entered draw_circle")
            print("[DEBUG] Draw {} circle(s)".format(quantity))
            print("[DEBUG] Select center and drag for radius")
            print("[DEBUG] Press Esc to leave the process")

        self.img = frame.copy()
        self.quantity = quantity

        window_name = "Draw {} Circle(s)".format(self.quantity)
        cv2.namedWindow(window_name)
        cv2.setMouseCallback(window_name, self.draw_circle_callback)    # windowName, callbackFunction

        self.last_orig_frame = deepcopy(self.img)
        self.orig_frame = deepcopy(self.img)

        self.circle_drawn = [False for _ in range(self.quantity)]

        self.roi_dict['type'] = 'circle'
        self.roi_dict['roi'] = dict()
        
        while True:
            cv2.imshow(window_name, self.img)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or (len(self.circle_drawn)>0 and self.circle_drawn[-1]):
                cv2.destroyWindow(window_name)
                self.circle_drawn = []
                break

        if self.verbose and len(self.roi_dict['roi']) != self.quantity:
            print("[DEBUG] Not all ROI's drawn")
            self.roi_dict = dict()

        roi_dict_temp = self.roi_dict

        self.init_variables()

        return roi_dict_temp


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
            
            self.roi_dict['roi'][line_index] = {
                'point1': (self.cursor_x, self.cursor_y),
                'point2': (x, y)
            }
            
            self.orig_frame = deepcopy(self.img)

            self.line_drawn[line_index] = True
    

    def draw_circle_callback(self, event, x, y, flags, param):
        '''
        callback for mouse events while drawing circle roi
        '''

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.cursor_x, self.cursor_y = x, y

        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            self.img = deepcopy(self.orig_frame)

            center = np.array([self.cursor_x, self.cursor_y], dtype=np.int64)
            pt_on_circle = np.array([x, y], dtype=np.int64)
            radius = int(np.linalg.norm(pt_on_circle-center))
            
            cv2.line(self.img, (self.cursor_x, self.cursor_y), (x, y), tuple(self.brush_color_ongoing), 2)  # Draw radius
            cv2.circle(self.img, (center[0], center[1]), radius, self.brush_color_ongoing, 2)
        
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False

            # get index of circle drawn
            circle_index = -1
            for i in range(len(self.circle_drawn)):
                if not self.circle_drawn[i]:
                    circle_index = i
                    break

            center = np.array([self.cursor_x, self.cursor_y], dtype=np.int64)
            pt_on_circle = np.array([x, y], dtype=np.int64)
            radius = int(np.linalg.norm(pt_on_circle-center))
            
            cv2.line(self.img, (self.cursor_x, self.cursor_y), (x, y), tuple(self.brush_color_finished), 2)  # Draw radius
            cv2.circle(self.img, (center[0], center[1]), radius, self.brush_color_finished, 2)
            
            self.roi_dict['roi'][circle_index] = {
                'center': (self.cursor_x, self.cursor_y),
                'point2': (x, y),
                'radius': radius
            }
            
            self.orig_frame = deepcopy(self.img)

            self.circle_drawn[circle_index] = True
        

    def draw_polygon_callback(self, event, x, y, flags, param):
        '''
        callback for mouse events while drawing polygon roi
        '''

        if event == cv2.EVENT_LBUTTONDOWN:
            if self.polygon_dblclk:
                self.polygon_dblclk = False
            
            else:
                self.drawing = True

                self.polygon_vertices.append((x, y))

                if len(self.polygon_vertices) > 1:
                    prev_vertex = self.polygon_vertices[-2]
                    current_vertex = self.polygon_vertices[-1]
                    
                    cv2.line(self.img, prev_vertex, current_vertex, self.brush_color_finished, 2)
                    self.orig_frame = deepcopy(self.img)

        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            self.img = deepcopy(self.orig_frame)

            last_vertex = self.polygon_vertices[-1]
            cv2.line(self.img, last_vertex, (x, y), tuple(self.brush_color_ongoing), 2)
        
        elif event == cv2.EVENT_LBUTTONDBLCLK:
            self.drawing = False

            # Find convex hull of polygon_vertices
            hull_output = cv2.convexHull(np.array(self.polygon_vertices), False)

            self.polygon_vertices = []
            for pt in hull_output:
                self.polygon_vertices.append(tuple(pt[0]))

            # Draw convex hull polygon
            self.img = deepcopy(self.last_orig_frame)
            for v in range(1, len(self.polygon_vertices)):
                cv2.line(self.img, self.polygon_vertices[v], self.polygon_vertices[v-1], self.brush_color_finished, 2)

            cv2.line(self.img, self.polygon_vertices[0], self.polygon_vertices[-1], self.brush_color_finished, 2)


            # get index of polygon drawn
            polygon_index = -1
            for i in range(len(self.polygon_drawn)):
                if not self.polygon_drawn[i]:
                    polygon_index = i
                    break
            
            self.roi_dict['roi'][polygon_index] = {
                'vertices': self.polygon_vertices
            }
            
            self.orig_frame = deepcopy(self.img)
            self.last_orig_frame = deepcopy(self.orig_frame)

            self.polygon_drawn[polygon_index] = True
            self.polygon_dblclk = True
            self.polygon_vertices = []


    def __del__(self):
        cv2.destroyAllWindows()

        if self.verbose:
            print("Thank You!!")


    def visualize_roi(self, frame, roi_dict):
        if 'roi' not in roi_dict:
            return frame

        img = frame.copy()

        if roi_dict['type'] == 'rectangle':
            img = visualize_rect(img, roi_dict)
            
        elif roi_dict['type'] == 'line':
            img = visualize_line(img, roi_dict)

        elif roi_dict['type'] == 'circle':
            img = visualize_circle(img, roi_dict)

        elif roi_dict['type'] == 'polygon':
            img = visualize_polygon(img, roi_dict)

        elif roi_dict['type'] == 'cuboid':
            pass
        
        return img

    
    def crop_roi(self, frame, roi_dict):
        if 'roi' not in roi_dict:
            return []

        img = frame.copy()

        if roi_dict['type'] == 'rectangle':
            cropped_images = crop_rect(img, roi_dict)
            
        elif roi_dict['type'] == 'line':
            print("[ERROR] What to crop in line roi:)")

        elif roi_dict['type'] == 'circle':
            cropped_images = crop_circle(img, roi_dict)

        elif roi_dict['type'] == 'polygon':
            cropped_images = crop_polygon(img, roi_dict)

        elif roi_dict['type'] == 'cuboid':
            pass
        
        return cropped_images