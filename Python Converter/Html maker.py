from __future__ import print_function
import os

print("Wirte a direction as the example or write a name..")
path=input("Example.... C:\\name1\\name2\\....\n")

imagesfiles = []
cordenadas = ['up', 'down', 'left', 'right', 'plus', 'minus']
imagesDirection = os.walk(path)

#------------Lista De imagenes-------------
zoomlist = [2,3,2]
none = 256
for root, dirs, files in imagesDirection:

    print("root ", root)
    print("files ", files)
    for infiles in files:
        (nombreFichero, extension) = os.path.splitext(infiles)
        if (extension == ".jpg"):
            imagesfiles.append(infiles)
        elif (extension == ".jpeg"):
            imagesfiles.append(infiles)
        elif (extension == ".png"):
            imagesfiles.append(infiles)

    with open('index.html', 'w') as html:

        print('<!DOCTYPE html>')
        print('<html>')
        print('<head>')
        print('<title>Project Title</title>')
        print('<meta charset="utf-8">')
        print('<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">')
        print('<meta name="viewport" content="target-densitydpi=device-dpi, width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, minimal-ui" />')
        print('<style> @-ms-viewport { width: device-width; } </style>')
        print('<link rel="stylesheet" href="vendor/reset.min.css">')
        print('<link rel="stylesheet" href="style.css">')
        print('</head>\n')

        print('<body class="multiple-scenes view-control-buttons">\n')

        print('<div id="pano"></div>\n')

        print('<div id="sceneList">')
        print('<ul class="scenes">\n')
        print()

        for emages in imagesfiles:
            print('<a href="#" class="scene" data-id="{}">'.format(emages))
            print('<li class="text">{}</li>'.format(emages))
            print('</a>\n')

        print('</ul>')
        print('</div>\n')

        print('<div id="titleBar">')
        print('<h1 class="sceneName"></h1>')
        print('</div>\n')

        print('<a href="#" id="autorotateToggle">')
        print('<img class="icon off" src="img/play.png">')
        print('<img class="icon on" src="img/pause.png">')
        print('</a>\n')

        print('<a href="#" id="fullscreenToggle">')
        print('<img class="icon off" src="img/fullscreen.png">')
        print('<img class="icon on" src="img/windowed.png">')
        print('</a>\n')

        print('<a href="#" id="sceneListToggle">')
        print('<img class="icon off" src="img/expand.png">')
        print('<img class="icon on" src="img/collapse.png">')
        print('</a>\n')

        for nam,nem in enumerate(cordenadas):
            print('<a href="#" id="viewUp" class="viewControlButton viewControlButton-{}">'.format(nam))
            print('<img class="icon" src="img/{}.png">'.format(nem))
            print('</a>\n')

#        <a href="#" id="viewUp" class="viewControlButton viewControlButton-1">
#        <img class="icon" src="img/up.png">
#        </a>
#        <a href="#" id="viewDown" class="viewControlButton viewControlButton-2">
#        <img class="icon" src="img/down.png">
#        </a>
#        <a href="#" id="viewLeft" class="viewControlButton viewControlButton-3">
#        <img class="icon" src="img/left.png">
#        </a>
#        <a href="#" id="viewRight" class="viewControlButton viewControlButton-4">
#        <img class="icon" src="img/right.png">
#        </a>
#        <a href="#" id="viewIn" class="viewControlButton viewControlButton-5">
#        <img class="icon" src="img/plus.png">
#        </a>
#        <a href="#" id="viewOut" class="viewControlButton viewControlButton-6">
#        <img class="icon" src="img/minus.png">
#        </a>

        print('<script src="vendor/es5-shim.js"></script>')
        print('<script src="vendor/eventShim.js"></script>')
        print('<script src="vendor/classList.js"></script>')
        print('<script src="vendor/requestAnimationFrame.js" ></script>')
        print('<script src="vendor/screenfull.min.js" ></script>')
        print('<script src="vendor/bowser.min.js" ></script>')
        print('<script src="vendor/marzipano.js" ></script>\n')

        print('<script src="data.js"></script>')
        print('<script src="index.js"></script>\n')

        print('</body>')
        print('</html>')
