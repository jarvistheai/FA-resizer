#!/usr/bin/env python3
import os
from PIL import Image

mpx = 3500

opath = input('Output directory:\n')
opath = opath.strip()
#running a loop for excetions to input valid directory
while True:
    try:
        #checking if there are whitespaces in directory
        if opath.count('\\') > 0:
            print('\n!!!Please use a path without whitespaces!!!\n')
            raise Exception('whitespaces')
        #checking if the directory is valid
        if not os.path.isdir(opath):
            print('\nPlease enter a valid path.\n')
            raise Exception('invalid path')
        break
    except:
        opath = input('Output directory:\n')
        opath = opath.strip()

ipaths = input('Input files:\n')
#running a loop for excetions to input valid files and directories
while True:
    try:
        #checking if there are whitespaces in a filename and directories
        if ipaths.count('\\ ') > 0:
            print('\n!!!Please use paths and files without whitespaces!!!\n')
            raise Exception('whitespaces')
        #checking if it is a valid file
        for ipath in ipaths:
            if not os.path.isfile(ipath):
                print('\nPlease enter valid files.\n')
                raise Exception('invalid files')
        break
    except:
        paths = input('Input files:\n')

#splitting paths into a list
plist = ipaths.split()

for path in plist:
    #split the path into path and file name
    head, tail = os.path.split(path)
    #store tail for renaming the file later
    pic = Image.open(path) #open file
    height, width = pic.size
    root, ext = os.path.splitext(tail)
    #checking if a dimension is bigger than 3500px
    if height > mpx or width > mpx:
        #checking if height or width is bigger
        if height > width:
            factor = height / mpx
            newWidth = int(width / factor)
            newHeight = mpx
        else:
            factor = width / mpx
            newHeight = int(height / factor)
            newWidth = mpx
        newsize = (newHeight, newWidth)
    #extending the filename with '_FA'
    root += '_FA.jpg'
    outfile = opath + '/' + root
    opic = pic.resize(newsize)
    opic = opic.convert("RGB")
    opic.save(outfile, "JPEG")
    print('Converting of ', root, 'is done.')
