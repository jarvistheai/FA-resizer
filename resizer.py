#!/usr/bin/env python3
import os
from PIL import Image

paths = input('Input files:\n')

while True:
    try:
        #checking if there are whitespaces in a filename
        if paths.count('\\') > 0:
            print('\n!!!Please use paths and files without whitespaces!!!\n')
            raise Exception('whitespaces')

        #checking if it is a file
        if paths.count('.') <= 0:
            print('\n!!!This is not a file!!!\n')
            raise Exception('not a file')

        #splitting paths into a list
        plist = paths.split()
        print(plist)

        for path in plist:
            #split the path into path and file name
            head, tail = os.path.split(path)
            #store tail for renaming the file later

        break

    except:
        paths = input('Input files:\n')
