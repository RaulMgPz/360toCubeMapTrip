from __future__ import print_function
import os

print("Wirte a direction as the example or write a name..")
path=input("Example.... C:\\name1\\name2\\....\n")

imagesfiles = []
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
        print('</head>')

        print('<body class="multiple-scenes view-control-buttons">')

        print('<div id="pano"></div>')

        print('<div id="sceneList">')
        print('<ul class="scenes">')
        print()

        for emages in imagesfiles:
            print('\n<a href="#" class="scene" data-id="{}">'.format(emages))
            print('<li class="text">{}</li>'.format(emages))
            print('</a>\n')

#        </ul>
#        </div>

#        <div id="titleBar">
#        <h1 class="sceneName"></h1>
#        </div>

#        <a href="#" id="autorotateToggle">
#        <img class="icon off" src="img/play.png">
#        <img class="icon on" src="img/pause.png">
#        </a>

#        <a href="#" id="fullscreenToggle">
#        <img class="icon off" src="img/fullscreen.png">
#        <img class="icon on" src="img/windowed.png">
#        </a>

#        <a href="#" id="sceneListToggle">
#        <img class="icon off" src="img/expand.png">
#        <img class="icon on" src="img/collapse.png">
#        </a>

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

#        <script src="vendor/es5-shim.js"></script>
#        <script src="vendor/eventShim.js"></script>
#        <script src="vendor/classList.js"></script>
#        <script src="vendor/requestAnimationFrame.js" ></script>
#        <script src="vendor/screenfull.min.js" ></script>
#        <script src="vendor/bowser.min.js" ></script>
#        <script src="vendor/marzipano.js" ></script>

#        <script src="data.js"></script>
#        <script src="index.js"></script>

#        </body>
#        </html>