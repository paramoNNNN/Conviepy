# Conviepy
Video Converter with MoviePy


## Installation
* python3.x

* you need moviepy and pathlib

__MoviePy__
```
pip install moviepy
```

__pathlib__
```
pip install pathlib
```

## args

* **path**

_path to video_

_example: path='/home/conviepy/video.mp4'_

* **auto_res**

_Convert to different resolutions Automatically_

_example: auto_res=True_

* **res**

_if auto_res is False you can add your custom resolution_

_example: res=[300, 300]

* **thumb**

_add preview gif and jpeg_

_example: thumb=True_

* **thumb_size**

_size of thumb if thumb is True_

_example: thumb_size=[100,100]

* **logo**

_place logo in video_

_example: logo=/home/conviepy/logo.png_

## Example
```
python3 conviepy path='/home/conviepy/video.mp4' auto_res=False res=[100, 100] thumb=True thumb_size=[50, 50] logo='/home/conviepy/logo.png'
```
