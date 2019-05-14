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
            imagesfiles.append(nombreFichero)
        elif (extension == ".jpeg"):
            imagesfiles.append(nombreFichero)
        elif (extension == ".png"):
            imagesfiles.append(nombreFichero)

    with open('index.html', 'w') as html:

        html.write('<!DOCTYPE html>\n')
        html.write('<html>\n')
        html.write('<head>\n')
        html.write('<title>Project Title</title>\n')
        html.write('<meta charset="utf-8">\n')
        html.write('<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n')
        html.write('<meta name="viewport" content="target-densitydpi=device-dpi, width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, minimal-ui" />\n')
        html.write('<style> @-ms-viewport { width: device-width; } </style>\n')
        html.write('<link rel="stylesheet" href="vendor/reset.min.css">\n')
        html.write('<link rel="stylesheet" href="style.css">\n')
        html.write('</head>\n')

        html.write('\n<body class="multiple-scenes view-control-buttons">\n')

        html.write('\n<div id="pano"></div>\n')

        html.write('\n<div id="sceneList">\n')
        html.write('  <ul class="scenes">\n')

        for nfi,nfj in enumerate(imagesfiles):
            html.write('\n      <a href="#" class="scene" data-id="{}-{}">\n'.format(nfi,nfj))
            html.write('        <li class="text">{}</li>\n'.format(nfj))
            html.write('      </a>\n')

        html.write('\n  </ul>\n')
        html.write('</div>\n')

        html.write('\n<div id="titleBar">\n')
        html.write('  <h1 class="sceneName"></h1>\n')
        html.write('</div>\n')

        html.write('\n<a href="#" id="autorotateToggle">\n')
        html.write('  <img class="icon off" src="img/play.png">\n')
        html.write('  <img class="icon on" src="img/pause.png">\n')
        html.write('</a>\n')

        html.write('\n<a href="#" id="fullscreenToggle">\n')
        html.write('  <img class="icon off" src="img/fullscreen.png">\n')
        html.write('  <img class="icon on" src="img/windowed.png">\n')
        html.write('</a>\n')

        html.write('\n<a href="#" id="sceneListToggle">\n')
        html.write('  <img class="icon off" src="img/expand.png">\n')
        html.write('  <img class="icon on" src="img/collapse.png">\n')
        html.write('</a>\n')

        for nam, nem in enumerate(cordenadas):
            if nam == 0:
                html.write('\n<a href="#" id="viewUp" class="viewControlButton viewControlButton-{}">\n'.format(nam+1))
            elif nam == 1:
                html.write('\n<a href="#" id="viewDown" class="viewControlButton viewControlButton-{}">\n'.format(nam+1))
            elif nam == 2:
                html.write('\n<a href="#" id="viewLeft" class="viewControlButton viewControlButton-{}">\n'.format(nam+1))
            elif nam == 3:
                html.write('\n<a href="#" id="viewRight" class="viewControlButton viewControlButton-{}">\n'.format(nam+1))
            elif nam == 4:
                html.write('\n<a href="#" id="viewIn" class="viewControlButton viewControlButton-{}">\n'.format(nam+1))
            elif nam == 5:
                html.write('\n<a href="#" id="viewOut" class="viewControlButton viewControlButton-{}">\n'.format(nam+1))
            html.write('  <img class="icon" src="img/{}.png">\n'.format(nem))
            html.write('</a>\n')

        html.write('\n<script src="vendor/es5-shim.js"></script>\n')
        html.write('<script src="vendor/eventShim.js"></script>\n')
        html.write('<script src="vendor/classList.js"></script>\n')
        html.write('<script src="vendor/requestAnimationFrame.js" ></script>\n')
        html.write('<script src="vendor/screenfull.min.js" ></script>\n')
        html.write('<script src="vendor/bowser.min.js" ></script>\n')
        html.write('<script src="vendor/marzipano.js" ></script>\n')

        html.write('\n<script src="data.js"></script>\n')
        html.write('<script src="index.js"></script>\n')

        html.write('\n</body>\n')
        html.write('</html>\n')
