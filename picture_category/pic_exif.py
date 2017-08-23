from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import time
import os
import re


def get_exif(pic_file):
    # i = Image.open('F:\\DCIM\\100ANDRO\\DSC_0004.JPG')
    # i = Image.open('F:\\photos\\iphone 2016.5.22\\101APPLE\\IMG_3007.JPG')
    try:
        img = Image.open(pic_file)
        if hasattr(img, '_getexif'):
            info = img._getexif()
            if info is not None:
                return {TAGS.get(tag): value for tag, value in info.items()}
            else:
                return None
        else:
            return None
    except IOError:
        print('IOERROR:', pic_file)


def get_pic_propery(pic_file, exif):
    pic_info = {}
    # GPS
    gps = exif['GPSInfo'] if 'GPSInfo' in exif.keys() else None
    if gps is not None:
        gps_dic = {GPSTAGS.get(gpstag): value for gpstag, value in gps.items()}
        lat = gps_dic['GPSLatitude']
        latitude_d = (lat[0][0] * 1.0) / lat[0][1] + ((lat[1][0] * 1.0) / lat[1][1]) / 60.0 + ((lat[2][0] * 1.0) /
                                                                                               lat[2][1]) / 3600.0
        longi = gps_dic['GPSLongitude']
        longitude_d = (longi[0][0] * 1.0) / longi[0][1] \
                      + ((longi[1][0] * 1.0) / longi[1][1]) / 60.0 \
                      + ((longi[2][0] * 1.0) / longi[2][1]) / 3600.0

        pic_info['latitude'] = latitude_d
        pic_info['lonitude'] = longitude_d

    # make
    make = exif['Make'] if 'Make' in exif.keys() else 'unknown'
    pic_info['make'] = make

    # model
    model = exif['Model'] if 'Model' in exif.keys() else "unknown_model"
    # only keep effective characters as filename
    model = re.sub('[^a-zA-Z0-9]', '', model)
    pic_info['model'] = model

    # Picture Create Time
    create_time = exif['DateTimeOriginal'] if 'DateTimeOriginal' in exif.keys() else "1970:01:01 23:59:59"

    # if exif don't have time info, then use file modify time.
    if re.match('^[0-9]{4}:[0-9]{1,2}:[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}$', create_time):
        create_time_t = time.strptime(create_time, '%Y:%m:%d %H:%M:%S')
    else:
        create_time_t = time.localtime(os.path.getmtime(picFile))

    pic_info['createTime'] = create_time_t

    # LensModel
    lens_model = exif['LensModel'] if 'LensModel' in exif.keys() else 'unknown'
    pic_info['lensModel'] = lens_model

    # ExifImageWidth
    width = exif['ExifImageWidth'] if 'ExifImageWidth' in exif.keys() else '0'
    pic_info['width'] = width

    # ExifImageHeight
    height = exif['ExifImageHeight'] if 'ExifImageHeight' in exif.keys() else '0'
    pic_info['height'] = height

    pic_info['raw'] = exif

    return pic_info


picFile = 'F:\\photos\\iphone 2016.5.22\\101APPLE\\IMG_3007.JPG'
exif = get_exif(picFile)
get_pic_propery(picFile, exif)

# gps = exif['GPSInfo']
#
# for gpstag, value in gps.items():
#     print(GPSTAGS.get(gpstag))
#     print(value)
