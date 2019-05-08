from __future__ import print_function
#from PIL import Image
#from numpy import clip
#from math import pi,atan2,hypot,floor
import os
#import shutil
#import time


print("Wirte a direction as the example or write a name..")
path=input("Example.... C:\\name1\\name2\\....\n")

imagesfiles = []
imagesDirection = os.walk(path)

#------------Lista De imagenes-------------
n=0
zooms = 1
none = 255
for root, dirs,files in imagesDirection:

    print("root ", root)
    print("files ", files)
    for infiles in files:
        (nombreFichero, extension) = os.path.splitext(infiles)
        if(extension == ".jpg"):
            imagesfiles.append(infiles)
        elif(extension == ".jpeg"):
            imagesfiles.append(infiles)
        elif (extension == ".png"):
            imagesfiles.append(infiles)

    for i in files:

        print('"id": "{}-{}",'.format(n,i))
        print('"name": "{}", \n'.format(i))
        n=+1
        print("[")
        print('"levels: {\n"tileSize": {}\n"size": {}\n"fallbackOnly": true\n}"'.format(none,none))

        print("]")

    print("none")
