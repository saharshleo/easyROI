# EasyROI


### Requirements

```
python3
cv2
numpy
```


### Running test code

* Create virtual environment and activate it

```
python3 -m venv venv_easy_roi
source venv_easy_roi/bin/activate
```

* install requirements.txt

```
pip3 install requirements.txt
```

```
git clone https://github.com/saharshleo/easyROI.git
```

```
python main.py
```


### Formats of roi

1. **Rectangle**

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

2. **Line**

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

3. **Circle**

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

4. **Polygon**

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


See progress in [TODO.md](TODO.md)