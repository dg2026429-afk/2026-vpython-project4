Web VPython 3.2
c_head = sphere(color=color.white,radius=1,pos=vec(0,0,0))
c_ear = sphere(color=color.white,radius=0.3,pos=vec(0.8,0.8,0))
c_ear = sphere(color=color.white,radius=0.3,pos=vec(-0.8,0.8,0))
c_eye = sphere(color=color.black,radius=0.16,pos=vec(0.26,0.2,0.8))
c_eye = sphere(color=color.black,radius=0.16,pos=vec(-0.26,0.2,0.8))
c_eye = sphere(color=color.white,radius=0.06,pos=vec(0.32,0.23,0.9))
c_eye = sphere(color=color.white,radius=0.05,pos=vec(-0.26,0.24,0.93))
c_blush = sphere(color=vec(1,204/255,229/255),radius=0.3,pos=vec(-0.26,-0.5,0.8))

Web VPython 3.2
c_head = sphere(color=color.white,radius=1,pos=vec(0,0,0))
c_ear1 = sphere(color=color.white,radius=0.3,pos=vec(0.8,0.8,0))
c_ear2 = sphere(color=color.white,radius=0.3,pos=vec(-0.8,0.8,0))
c_eye3 = sphere(color=color.black,radius=0.16,pos=vec(0.26,0.2,0.8))
c_eye4 = sphere(color=color.black,radius=0.16,pos=vec(-0.26,0.2,0.8))
c_eye5 = sphere(color=color.white,radius=0.06,pos=vec(0.32,0.23,0.9))
c_eye6 = sphere(color=color.white,radius=0.05,pos=vec(-0.26,0.24,0.93))
c_blush1 = sphere(color=vec(1,204/255,229/255),radius=0.2,pos=vec(-0.4,-0.01,0.8))
c_blush2 = sphere(color=vec(1,204/255,229/255),radius=0.2,pos=vec(0.4,-0.01,0.8))
c_mouth = box(color=color.black,size=vec(0.2,0.3,0.3),pos=vec(0,-0.1,0.9))
c_eyebrow1 = box(color=color.black,size=vec(0.04,0.11,0.3),pos=vec(0.2,0.43,0.76))
c_eyebrow2 = box(color=color.black,size=vec(0.04,0.11,0.3),pos=vec(-0.2,0.43,0.76))
c_eyebrow3 = box(color=color.black,size=vec(0.2,0.04,0.3),pos=vec(0.31,0.4,0.76))
c_eyebrow4 = box(color=color.black,size=vec(0.2,0.04,0.3),pos=vec(-0.31,0.4,0.76))
c_hand = sphere(color=color.white,radius=0.3,pos=vec(0.6,-0.5,0.8))
c_pencil1 = cone(size=vec(0.4,0.4,0.4),color=color.blue,pos=vec(1.2,-0.5,0.8))
c_pencil2 = box(color=color.blue,size=vec(0.5,0.33,0.3),pos=vec(0.94,-0.5,0.8))
chiikawa = compound([c_head,c_ear1,c_ear2,c_eye3,c_eye4,c_eye5,c_eye6,c_blush1,c_blush2,c_mouth,c_eyebrow1,c_eyebrow2,c_eyebrow3,c_eyebrow4,c_hand,c_pencil1,c_pencil2])

while True :
    rate(100)
    k = keysdown()
    if 'd' in k : 
        chiikawa.pos.x = chiikawa.pos.x + 0.1
