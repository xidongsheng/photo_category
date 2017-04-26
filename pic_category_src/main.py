# -*- coding: UTF-8 -*-
import os
import shutil
from pic_category_src import picExif
import time
import re
import logging

def scanDirGetPic(dir):

    #get all pictures, file size should be larger than 300KB,
    picList = []
    for root, dirs, files in os.walk(dir, True, None, False):
        for f in files:
            if os.path.isfile(os.path.join(root,f)):
                ext = os.path.splitext(f)[1].lower()
                filesize = os.path.getsize(os.path.join(root,f))
                if ext in ('.jpg','.jpeg','.bmp') and filesize > 307200:
                    picList.append(os.path.join(root,f))
                    # print(os.path.join(root,f))
                    #print os.path.join(root,f)
    print('total picture number is: %d',len(picList))

    return picList


def cpFile(srcPath,destDir):
    # rename picture to a new name (createtime_model)
    fileNameRaw = os.path.basename(srcPath)
    ext = os.path.splitext(fileNameRaw)[1].lower()

    picInfo = picExif.get_exif(srcPath)
    if picInfo != None:
        createTime = picInfo['DateTimeOriginal'] if 'DateTimeOriginal' in picInfo.keys() else "1970:01:01 23:59:59"

        #if exif don't have time info, then use file modify time.
        if re.match('^[0-9]{4}:[0-9]{1,2}:[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}$',createTime):
            createTime_T = time.strptime(createTime,'%Y:%m:%d %H:%M:%S')
        else:
            createTime_T = time.localtime(os.path.getmtime(srcPath))

        createTime = time.strftime('%Y_%m_%d_%H_%M_%S',createTime_T)
        model = picInfo['Model'] if 'Model' in picInfo.keys() else "unknown_model"
        #only keep efftive characters as filename
        model = re.sub('[^a-zA-Z0-9]','',model)

        fileName = createTime+'_'+model+ext
        # dest folder is monthly folder
        destFolder = time.strftime('%Y_%m',createTime_T)

        # if dest folder don't exists, create dir
        if not os.path.exists(destDir + os.path.sep + destFolder):
            os.makedirs(destDir + os.path.sep + destFolder)

        destPath = destDir + os.path.sep + destFolder+os.path.sep + fileName
        if os.path.exists(srcPath) and not os.path.exists(destPath):
            print('cp %s %s' % (srcPath,destPath))
            shutil.copy(srcPath,destPath)

    else:
        print('%s dont have exif info' %srcPath)
        #copy to uncategory

def main():
    # dir = 'F:\\DCIM'
    dir = 'F:'
    # dir = 'F:\\photos\\2016.1 vivo\\'
    # dir = 'F:\\王娜\\照片\\本科照片\\照片\\大学的照片\\照片\\联通实习留念\\王娜'
    destDir = 'D:\\Photo_Category'
    picList = scanDirGetPic(dir)
    for pic in picList:
        cpFile(pic,destDir)

if __name__ == "__main__":
    main()
