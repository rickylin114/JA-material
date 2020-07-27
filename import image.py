import numpy as np
import cv2

img = cv2.imread('purple.jpg')
h, w = img.shape[:2]
'''
cv2.imshow('Myimage',img)
def click_info(event, x, y, flags, param):
    # 雙擊
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('坐標', x, y)
        b, g, r = img[y, x]     # b, g, r
        print("的bgr值", b, g, r)
        '''
def average_bgr(event, x, y, flags, param):
       if cv2.waitKey(0) == ord('p'):
        print('坐標',200, 200)
        b, g, r = img[200, 200]     # b, g, r
        print("的bgr值", b, g, r)
        b1=b
        g1=g
        r1=r
        print('坐標',200, w//2)
        b, g, r = img[200, w//2]    # b, g, r
        print("的bgr值", b, g, r)
        b2=b
        g2=g
        r2=r
        print('坐標',200, w-200)
        b, g, r = img[200, w-200]     # b, g, r
        print("的bgr值", b, g, r)
        b3=b
        g3=g
        r3=r
        print('坐標',w//2, h//2)
        b, g, r = img[w//2, h//2]     # b, g, r
        print("的bgr值", b, g, r)
        b4=b
        g4=g
        r4=r
        print('坐標',h-200, 200)
        b, g, r = img[h-200, 200]     # b, g, r
        print("的bgr值", b, g, r)
        b5=b
        g5=g
        r5=r
        print('坐標',h-200, w//2)
        b, g, r = img[h-200, w//20]     # b, g, r
        print("的bgr值", b, g, r)
        b6=b
        g6=g
        r6=r
        print('坐標',h-200, w-200)
        b, g, r = img[h-200, w-200]     # b, g, r
        print("的bgr值", b, g, r)
        b7=b
        g7=g
        r7=r
        B=[b1,b2,b3,b4,b5,b6,b7]
        print ('B=',round(sum(B)/len(B)))
        BAvr=round(sum(B)/len(B))
        G=[g1,g2,g3,g4,g5,g6,g7]
        print('G=',round(sum(G)/len(G)))
        GAvr=round(sum(G)/len(G))
        R=[r1,r2,r3,r4,r5,r6,r7]
        print('R=',round(sum(R)/len(R)))
        RAvr=round(sum(R)/len(R))
        SumRGB=[BAvr,GAvr,BAvr]
        Avr=(round(sum(SumRGB)/len(SumRGB)))
        print('平均=',Avr)
        color(BAvr,GAvr,RAvr,Avr)
        
def color(BAvr,GAvr,RAvr,Avr):
        if BAvr>=GAvr and BAvr>=RAvr:
               if BAvr-GAvr>5 and BAvr-RAvr>=5:
                      print('Blue')
               elif BAvr-GAvr<5:
                      print('Cyan')
               else:
                      print('Purple1')
              
        elif GAvr>=RAvr and GAvr>=BAvr:
               if GAvr-RAvr>5 or GAvr-BAvr>5:
                      print('Green')
               elif GAvr-RAvr<5:
                      print('Yellow')
               else:
                      print('Cyan2')
                      print(GAvr-RAvr)
                      print(GAvr-BAvr)
        elif RAvr>=GAvr and RAvr>=BAvr:
               if RAvr-GAvr>=5 and RAvr-BAvr>=5:
                      print('Red')
               elif RAvr-GAvr<5:
                      print('Yellow')
               else:
                      print('Purple')
        else:
              print(RAvr)
              print(BAvr)
              print(GAvr)
              print('White')          
cv2.namedWindow('image')
cv2.setMouseCallback('image', average_bgr)

while True:
    cv2.imshow("image", img)
    # esc键
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
