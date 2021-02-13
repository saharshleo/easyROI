# [EasyROI](https://github.com/saharshleo/easyROI)

Helper library for drawing ROI in Computer Vision Applications

![demo](https://github.com/saharshleo/easyROI/blob/main/assets/run.gif)

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [EasyROI](#easyroi)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
    - [Tech Stack](#tech-stack)
    - [File Structure](#file-structure)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Using EasyROI in your project](#using-easyroi-in-your-project)
      - [Rectangular roi](#rectangular-roi)
      - [Line Roi](#line-roi)
      - [Circle Roi](#circle-roi)
      - [Polygon Roi](#polygon-roi)
  - [Formats of roi](#formats-of-roi)
    - [Rectangle](#rectangle)
    - [Line](#line)
    - [Circle](#circle)
    - [Polygon](#polygon)
  - [Future Work](#future-work)
  - [Contributors](#contributors)
  - [Acknowledgements and Resources](#acknowledgements-and-resources)
  - [License](#license)


<!-- ABOUT THE PROJECT -->
## About The Project



### Tech Stack

* [Python](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [Numpy](https://numpy.org/)  

### File Structure 
    .  
    ├── EasyROI  
    │   ├── __init__.py  
    │   ├── easyROI.py  
    │   └── utils.py  
    ├── input
    │   ├── overpass.mp4   
    ├── output/  
    ├── dev_main.py             # Code for testing during developing phase
    ├── test_library.py         # Code for testing during testing phase
    ├── DEV_README.md           # README for developing phase 
    ├── LICENSE  
    └── README.md 
    

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* python>=3.6
* pip


### Installation
1. Create virtual environment

```sh
python3 -m venv venv_easy_roi
source venv_easy_roi/bin/activate
```

2. Install EasyROI

```sh
pip install EasyROI
```


<!-- USAGE EXAMPLES -->
## Usage

* Read the instruction in terminal while drawing roi


### Using EasyROI in your project

* Initializing

```python
from EasyROI import EasyROI

roi_helper = EasyROI(verbose=True)
```

#### Rectangular roi

![rectangle_demo](https://github.com/saharshleo/easyROI/blob/main/assets/rectangle.gif)

```python
rect_roi = roi_helper.draw_rectangle(frame, 3)  # quantity=3 specifies number of rectangles to draw

frame_temp = roi_helper.visualize_roi(frame, rect_roi)
```

* See roi format in - [Rectangle](#rectangle)


#### Line Roi

![line_demo](https://github.com/saharshleo/easyROI/blob/main/assets/line.gif)

```python
line_roi = roi_helper.draw_line(frame, 3)  # quantity=3 specifies number of lines to draw

frame_temp = roi_helper.visualize_roi(frame, line_roi)
```

* See roi format in - [Line](#line)


#### Circle Roi

![circle_demo](https://github.com/saharshleo/easyROI/blob/main/assets/circle.gif)

```python
circle_roi = roi_helper.draw_circle(frame, 3)   # quantity=3 specifies number of circles to draw

frame_temp = roi_helper.visualize_roi(frame, circle_roi)
```

* See roi format in - [Circle](#circle)


#### Polygon Roi

![polygon_demo](https://github.com/saharshleo/easyROI/blob/main/assets/polygon.gif)

```python
polygon_roi = roi_helper.draw_polygon(frame, 3) # quantity=3 specifies number of polygons to draw

frame_temp = roi_helper.visualize_roi(frame, polygon_roi)
```

* See roi format in - [Polygon](#polygon)


<!-- FORMAT OF ROI -->
## Formats of roi

### Rectangle

quantity = 1

```
{
    'roi': {   
                0: {'br_x': 573,
                    'br_y': 443,
                    'h'   : 105,
                    'tl_x': 322,
                    'tl_y': 338,
                    'w'   : 251
                }
            },

    'type': 'rectangle'
}
```

### Line

quantity = 2

```
{
    'roi': {
                0: {
                    'point1': (374, 395), 
                    'point2': (554, 438)
                },

                1: {
                    'point1': (555, 438), 
                    'point2': (830, 361)
                }
            },

    'type': 'line'
}
```

### Circle

quantity = 2

```
{
    'roi': {
                0: {
                    'center': (330, 355), 
                    'point2': (552, 375), 
                    'radius': 222
                },

                1: {
                    'center': (702, 374), 
                    'point2': (700, 475), 
                    'radius': 101
                }
            },

    'type': 'circle'
}
```

### Polygon

quantity = 2

```
{
    'roi': {
                0: {
                    'vertices': [
                        (586, 435), 
                        (534, 582), 
                        (200, 504), 
                        (356, 403)
                    ]
                },
                
                1: {
                    'vertices': [
                        (1108, 507),
                        (738, 662),
                        (709, 497),
                        (711, 494),
                        (927, 414)
                    ]
                }
            },

    'type': 'polygon'
}
```


<!-- FUTURE WORK -->
## Future Work
* See [TODO.md](TODO.md) for seeing developments of this project



<!-- CONTRIBUTORS -->
## Contributors
* [saharshleo](https://github.com/saharshleo)


<!-- ACKNOWLEDGEMENTS AND REFERENCES -->
## Acknowledgements and Resources
* [Packaging](https://www.codementor.io/@ajayagrawal295/how-to-publish-your-own-python-package-12tbhi20tf)


<!-- LICENSE -->
## [License](LICENSE)
