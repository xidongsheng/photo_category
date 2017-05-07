# -*- coding: UTF-8 -*-
from __future__ import absolute_import
import logging
import argparse

from picture_category import category

def main():
    parser = argparse.ArgumentParser(description="Picture Category Program")
    parser.add_argument('input',type=str,help="input directory which raw pictures store")
    parser.add_argument('output',type=str,help="ouput directory store processed pictures")
    args = parser.parse_args()
    # dir = 'F:\\DCIM'
    # dir = 'F:'
    logging.basicConfig(level=logging.INFO
                        ,format='%(asctime)s %(filename)s [line:%(lineno)d]  %(levelname)s   %(message)s'
                        ,datefmt='%Y %b %d  %H:%M:%S'
                        # ,filename='myapp.log'
                        # ,filemode='w'
                        )

    inputDir = args.input
    destDir = args.output
    # dir = 'F:\\photos\\2016.1 vivo'
    # dir = 'F:\\王娜\\照片\\本科照片\\照片\\大学的照片\\照片\\联通实习留念\\王娜'
    # destDir = 'D:\\Photo_Category'

    category.category(inputDir,destDir)

    logging.info('process done')

if __name__ == "__main__":
    main()
