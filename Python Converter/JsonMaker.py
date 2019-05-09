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
zoomlist = [2,3,2]
none = 256
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

    with open('data.js', 'w') as json:

        json.write('var APP_DATA = {\n')
        json.write('"scenes": [\n')

        for n, i in enumerate(files):

            json.write('\n{')
            json.write('"id": "{}-{}",\n'.format(n,i))
            json.write('"name": "{}", \n'.format(i))
            json.write('"levels": [\n        {\n')
            json.write('           "tileSize": {},\n'.format(none))
            json.write('           "Size": {},\n'.format(none))
            json.write('           "fallbackOnly": true\n        },\n')

            for a in zoomlist:
                zon=a
                if zon > 1:
                    for idea in range(1,zon+1):
                        json.write('         {\n')
                        json.write('           "tileSize": {},\n'.format(none*2))
                        json.write('           "Size": {},\n'.format(512*idea))
                        json.write('         },\n')

                elif zon == 1:
                    json.write('         {\n')
                    json.write('           "tileSize": {},\n'.format(512))
                    json.write('           "Size": {},\n'.format(512))
                    json.write('         },\n')


                json.write("     ],\n")

                #------ Zooms ------
                json.write('     "faceSize": {},\n'.format(512*zon))
                json.write('     "initialViewParameters": {\n')
                json.write('     "pitch": 0,\n')
                json.write('     "yaw": 0,\n')
                json.write('     "fov": 1.5707963267948966\n      },\n')

                json.write('"linkHotspots": []\n')
                json.write('"infoHotspots": []\n')
                json.write('     },\n')
                break
        json.write('\n]\n}')
