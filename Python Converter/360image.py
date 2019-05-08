from __future__ import print_function
from PIL import Image
from numpy import clip
from math import pi,atan2,hypot,floor
import os
import shutil
import time
restriction=['Cancel', 'cancel', 'CANCEL', ' Cancel', ' cancel', ' CANCEL', 'Cancel ', 'cancel ', 'CANCEL ']

print("Wirte a direction as the example or write a name..")
path=input("Example.... C:\\name1\\name2\\....\n")
saver=input("Where do you want to save?...\nWrite a second path...\nif you have done a mistake, write Cancel and try again\n")

while saver in restriction:
    print("Please, try again")
    print("Wirte a direction as the example or write a name..")
    path=input("Example.... C:\\name1\\name2\\....\n")
    print("Write Cancel if you want to go back")
    saver=input("Where do you want to save?...\nWrite a second path...\n")

imagesfiles = []
imagesDirection = os.walk(path)
file_extension = ".png"
os.mkdir('360transform')

#-----------------------360 TO CUBE -----------------------------------
print("360 to Cube Image....")
def outImgToXYZ(i,j,face,edge):
    a = 2.0*float(i)/edge
    b = 2.0*float(j)/edge
    if face==0: # back
        (x,y,z) = (-1.0, 1.0-a, 3.0 - b)
    elif face==1: # left
        (x,y,z) = (a-3.0, -1.0, 3.0 - b)
    elif face==2: # front
        (x,y,z) = (1.0, a - 5.0, 3.0 - b)
    elif face==3: # right
        (x,y,z) = (7.0-a, 1.0, 3.0 - b)
    elif face==4: # top
        (x,y,z) = (b-1.0, a -5.0, 1.0)
    elif face==5: # bottom
        (x,y,z) = (5.0-b, a-5.0, -1.0)
    return (x,y,z)
def convertBack(imgIn,imgOut):

    inSize = imgIn.size
    outSize = imgOut.size
    inPix = imgIn.load()
    outPix = imgOut.load()
    edge = int(inSize[0]/4)   # the length of each edge in pixels
    for i in range(outSize[0]):
        face = int(i/edge) # 0 - back, 1 - left 2 - front, 3 - right
        if face==2:
            rng = range(0,edge*3)
        else:
            rng = range(edge,edge*2)

        for j in rng:
            if j<edge:
                face2 = 4 # top
            elif j>=2*edge:
                face2 = 5 # bottom
            else:
                face2 = face

            (x,y,z) = outImgToXYZ(i,j,face2,edge)

            theta = atan2(y,x) # range -pi to pi
            r = hypot(x,y)
            phi = atan2(z,r) # range -pi/2 to pi/2
            # source img coords
            uf = ( 2.0*edge*(theta + pi)/pi )
            vf = ( 2.0*edge * (pi/2 - phi)/pi)
            # Use bilinear interpolation between the four surrounding pixels
            ui = floor(uf)  # coord of pixel to bottom left
            vi = floor(vf)
            u2 = ui+1       # coords of pixel to top right
            v2 = vi+1
            mu = uf-ui      # fraction of way across pixel
            nu = vf-vi
            # Pixel values of four corners
            A = inPix[int(ui % inSize[0]),int(clip(vi,0,inSize[1]-1))]
            B = inPix[int(u2 % inSize[0]),int(clip(vi,0,inSize[1]-1))]
            C = inPix[int(ui % inSize[0]),int(clip(v2,0,inSize[1]-1))]
            D = inPix[int(u2 % inSize[0]),int(clip(v2,0,inSize[1]-1))]
            # interpolate
            (r,g,b) = (
                A[0]*(1-mu)*(1-nu) + B[0]*(mu)*(1-nu) + C[0]*(1-mu)*nu+D[0]*mu*nu,
                A[1]*(1-mu)*(1-nu) + B[1]*(mu)*(1-nu) + C[1]*(1-mu)*nu+D[1]*mu*nu,
                A[2]*(1-mu)*(1-nu) + B[2]*(mu)*(1-nu) + C[2]*(1-mu)*nu+D[2]*mu*nu )

            outPix[i,j] = (int(round(r)),int(round(g)),int(round(b)))

#------------Lista De imagenes-------------

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

    for infile in imagesfiles:
        print("------")
        print(infile)
        full_path = os.path.join(root, infile)
        os.mkdir('Carpet {}'.format(infile))

        imgIn = Image.open(full_path)
        inSize = imgIn.size
        imgOut = Image.new("RGB",(inSize[0],int(inSize[0]*3/4)),"black")
        convertBack(imgIn,imgOut)
        #imgOut.save("filtre.png")
        print("Cube Image Finished...")
        imgOut.save("Cube.png")

        #--------------------Map cube sort------------------------------------
        print("Cube Image Map...")
        name_map = [ \
            ["", "", "posy", ""],
            ["negz", "negx", "posz", "posx"],
            ["","", "negy", "0"]]
        image=Image.open("Cube.png")
        #print(image, image.format, "%dx%d" % image.size, image.mode)
        imSize=image.size
        cube_size = imSize[0] / 4
        for row in range(3):
            for col in range(4):
                if name_map[row][col] != "":
                    sx = cube_size * col
                    sy = cube_size * row
                    fn = name_map[row][col] + file_extension

                    images=image.crop((sx, sy, sx + cube_size, sy + cube_size))
                    if row==0 and col==2 :
                        images.save("n1.jpg")
                    elif row ==1 and col==0 :
                        images.save("n2.jpg")
                    elif row ==1 and col==1 :
                        images.save("n3.jpg")
                    elif row==1 and col==2 :
                        images.save("n4.jpg")
                    elif row==1 and col==3 :
                        images.save("n5.jpg")
                    elif row==2 and col==2 :
                        images.save("n6.jpg")
                    elif row==2 and col==3 :
                        images.save("n7.jpg")

        print("Cube map Finished....")

        #-------Crop Large image---------

        negative = Image.open("n7.jpg")
        neg = negative.resize((512, 3072), Image.ANTIALIAS)

        #------Image.paste------
        line = [2, 6, 4, 3, 5, 1]

        jack = (0, 0)
        a = 512

        for i in line:
            #print(i)
            img = Image.open("n{}.jpg".format(i))
            piece=img.resize((512, 512), Image.ANTIALIAS)

            for j in range(0,i):
                jack = (0, a*j)
            #print(jack)
            neg.paste(piece,jack)
        neg.save("cube.jpg")
        shutil.move('cube.jpg'.format(infile),'Carpet {}'.format(infile))

        #------------Image zooms binders ---------
        lectura=Image.open("n7.jpg")
        an=lectura.width
        al=lectura.height
        general=512

        pha=an/general
        ta=al/general

        if pha>ta:
            nuom=int(pha)
        elif pha<ta:
            nuom=int(ta)
        elif pha==ta:
            nuom=int(pha)

        for i in range(1,nuom+2):
            os.mkdir('z{}'.format(i))
        print("Zooms binder done")
        time.sleep(5)


        #---------------------Zooms Crop-------------------------------------
        for photo in range(1,7):
            imz=Image.open("n{}.jpg".format(photo))

            ancho=imz.width
            alto=imz.height
            general=512
            numero=0

            alpha=ancho/general
            beta=alto/general
            area=(0,0,0,0)

            if alpha>beta:
                numero=int(alpha)
            elif alpha<beta:
                numero=int(beta)
            elif alpha==beta:
                numero=int(alpha)

            print("Total Zooms..{}".format(numero+1))
            print("Zooms Process...")

            #shutil.move('{}'.format(jpgs),'Carpet {}'.format(jpgs))
            #shutil.move('Carpet {}'.format(jpgs),'{}'.format(direcction))

            for zooms in range(1,numero+2):

                if photo==1:
                    os.makedirs('u')   #1
                elif photo==2:
                    os.makedirs('b')   #2
                elif photo==3:
                    os.makedirs('l')   #3
                elif photo==4:
                    os.makedirs('f')   #4
                elif photo==5:
                    os.makedirs('r')   #5
                elif photo==6:
                    os.makedirs('d')   #6

                ex=2**zooms
                div=int(ex/2)
                y=0
                yy=0
                x=0
                xx=0

                for yi in range(1,div+1):
                    ny=alto/div
                    m=yi
                    if yi==1:
                        y=0
                        yy=alto/div
                    else:
                        y=((yi-1)*ny)
                        yy=(m*(alto/div))
                    #----------Carpetas de X-----------------
                    os.makedirs('{}'.format(yi-1))

                    for xi in range(1,div+1):
                        nx=ancho/div
                        mm=xi
                        if xi ==1:
                            x=0
                            xx=ancho/div
                        else:
                            x=((xi-1)*nx)
                            xx=(mm*(ancho/div))

                        area=(x,y,xx,yy)

                        copys=imz.crop(area)
                        copyn=copys.resize((general,general),Image.ANTIALIAS)
                        copyn.save('{}.jpg'.format(xi-1))
                        shutil.move('{}.jpg'.format(xi-1),'{}'.format(yi-1))

                    if photo==1:
                        shutil.move('{}'.format(yi-1),'u')
                    elif photo==2:
                        shutil.move('{}'.format(yi-1),'b')
                    elif photo==3:
                        shutil.move('{}'.format(yi-1),'l')
                    elif photo==4:
                        shutil.move('{}'.format(yi-1),'f')
                    elif photo==5:
                        shutil.move('{}'.format(yi-1),'r')
                    elif photo==6:
                        shutil.move('{}'.format(yi-1),'d')

                if photo==1:
                    shutil.move('u','z{}'.format(zooms))
                elif photo==2:
                    shutil.move('b','z{}'.format(zooms))
                elif photo==3:
                    shutil.move('l','z{}'.format(zooms))
                elif photo==4:
                    shutil.move('f','z{}'.format(zooms))
                elif photo==5:
                    shutil.move('r','z{}'.format(zooms))
                elif photo==6:
                    shutil.move('d','z{}'.format(zooms))
                    os.rename('z{}'.format(zooms),'{}'.format(zooms))
                    shutil.move('{}'.format(zooms),'Carpet {}'.format(infile))
        shutil.move('Carpet {}'.format(infile),'360transform')

    print("delet process.... ")
    os.mkdir('delet')
    shutil.move('cube.png','delet')
    for delet in range(1,7):
        shutil.move('n{}.jpg'.format(delet),'delet')
    time.sleep(1)
    shutil.rmtree('delet')

    try:
        shutil.rmtree('n7.jpg')
    except:
        print("Fail")

    try:
        time.sleep(1)
        shutil.move('360transform',saver)
    except:
        print("Saver Doesn´t exist")
        shutil.move('360transform',path)
    #    time.sleep(10)
    print("Zooms Finished...")
    break
