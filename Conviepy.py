import os
import sys
import ast
from pathlib import Path
from moviepy.editor import *

### args ###
# path: path of file[string]
# auto_res: Auto Resolution[Boolean]
# res: Resolutions[list] ** when auto Resolutions is False **
# thumb: thumbnail[Boolean]
# thumbnail: thumbnail_size[list] ** when thumbnail is True **
# logo: logo[string]  ** path of logo **

args = {}
for idx, val in enumerate(sys.argv):
    if idx > 0:
        temp = val.split('=')
        args[temp[0]] = temp[1]

# Path
if 'path' not in args.keys():
    print("you must enter path \n exmaple.py path=PATH_TO_FILE")
    sys.exit()
else:
    path = args['path']

# Resolution
if 'auto_res' in args.keys():
    auto_res = args['auto_res']
else:
    auto_res = 'False'

if 'res' in args.keys():
    if auto_res == 'False':
        res = args['res']
elif auto_res == 'False':
    print("if auto_res is False you must enter res or turn auto_res to True")
    sys.exit()

# thumbnails
if 'thumb' in args.keys():
    thumb = args['thumb']
else:
    thumb = 'False'

if 'thumb_size' in args.keys():
    if thumb == "True":
        thumb_size = args['thumb_size']
elif thumb == "True":
    print('if thumb is True you must enter thumb_size or turn thumb to False')

# logo
if 'logo' in args.keys():
    logo = args['logo']


### Start Converting ###
clip = VideoFileClip(path)
clip_name = Path(path).resolve().stem

if auto_res == "True":
    # Check Resolution
    _1080p = False
    _720p = False
    _480p = False
    _360p = False
    _240p = False
    _144p = False
    if clip.size[1] >= 1080:
        _1080p = True
        _720p = True
        _480p = True
        _360p = True
        _240p = True
        _144p = True
    elif clip.size[1] >= 720:
        _720p = True
        _480p = True
        _360p = True
        _240p = True
        _144p = True
    elif clip.size[1] >= 480:
        _480p = True
        _360p = True
        _240p = True
        _144p = True
    elif clip.size[1] >= 360:
        _360p = True
        _240p = True
        _144p = True
    elif clip.size[1] >= 240:
        _240p = True
        _144p = True
    elif clip.size[1] >= 144:
        _144p = True

if 'logo' in vars():
    # Set Logo
    logo = (ImageClip(logo)
            .set_duration(clip.duration)
            .resize(height=50)  # if you need to resize...
            .margin(right=8, bottom=8)  # (optional) logo-border padding
            .set_pos(("right", "bottom")))
    final = CompositeVideoClip([clip, logo])
else:
    final = clip

if auto_res == 'True':
    # Start Convert
    if _1080p:
        final.resize(width=1920, height=1080).write_videofile(clip_name + "_1080" + ".mp4")

    if _720p:
        final.resize(width=1280, height=720).write_videofile(clip_name + "_720" + ".mp4")

    if _480p:
        final.resize(width=640, height=480).write_videofile(clip_name + "_480" + ".mp4")

    if _360p:
        final.resize(width=480, height=360).write_videofile(clip_name + "_360" + ".mp4")

    if _240p:
        final.resize(width=426, height=240).write_videofile(clip_name + "_240" + ".mp4")

    if _144p:
        final.resize(width=256, height=144).write_videofile(clip_name + "_144" + ".mp4")
else:
    res = ast.literal_eval(res)
    final.resize(width=res[0], height=res[1]).write_videofile(clip_name + "_" + str(res[1]) + ".mp4")

# Creating thumbnail & gif preview
if thumb == "True":
    # gif
    gif = []
    duration = int(final.duration)

    # part 1
    start_time = duration / 9
    end_time = duration / 7
    if end_time > start_time + 2.5:
        end_time = start_time + 2.5
    gif.append(final.subclip(start_time, end_time))

    # part 2
    start_time = duration / 3
    end_time = duration / 1
    if end_time > start_time + 2.5:
        end_time = start_time + 2.5
    gif.append(final.subclip(start_time, end_time))

    final_gif = concatenate_videoclips(gif)
    final_gif.resize(width=self.thumbnail_size[0],
                    height=self.thumbnail_size[1]).\
                    write_gif(clip_name + "_gif.gif", fps=8)

    # thumbnail
    final_thumbnail = clip.subclip(clip.duration / 2, clip.duration / 2)
    final_thumbnail.resize(width=self.thumbnail_size[0],
                          height=self.thumbnail_size[1]).\
                          save_frame(clip_name + "_thumb.jpg")
