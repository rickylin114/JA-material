import numpy as np
import cv2
import pandas as pd
import pyautogui

df= pd.read_csv('MQ-RGB.csv')
img = cv2.imread('MQ-212.jpg')
h, w = img.shape[:2]

def average_bgr(event, x, y, flags, param):
       
       '''
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
        match(BAvr,GAvr,RAvr,Avr)
        '''
def color(BAvr,GAvr,RAvr,Avr):
        if abs(BAvr-GAvr)<=1 and abs(BAvr-RAvr)<=1:
              print('White')

        elif BAvr>=GAvr and BAvr>=RAvr:
               if BAvr-GAvr>5 and BAvr-RAvr>=5:
                      print('Blue')
   
               elif BAvr-GAvr<5:
                      print('Cyan')
  
               else:
                      print('Purple')
 
              
        elif GAvr>=RAvr and GAvr>=BAvr:
               if GAvr-RAvr>5 or GAvr-BAvr>5:
                      print('Green')

               elif GAvr-RAvr<5:
                      print('Yellow')

               else:
                      print('Cyan')

        elif RAvr>=GAvr and RAvr>=BAvr:
               if RAvr-GAvr>=5 and RAvr-BAvr>=5:
                      print('Red')

               elif RAvr-GAvr<5:
                      print('Yellow')
                      color.white()
               else:
                      print('Purple')

        else:
              print(RAvr)
              print(BAvr)
              print(GAvr)
              print('White')


def match(BAvr,GAvr,RAvr,Avr):
       df['Rdef']=(abs (RAvr-df['R']))
       df['Gdef']=(abs (GAvr-df['G']))
       df['Bdef']=(abs (RAvr-df['B']))
       df['SumDef']=(df['Rdef']+df['Gdef']+df['Bdef'])
       Newdf1=df.sort_values('Rdef')
       print(Newdf1.head(1))
       Newdf2=df.sort_values('Gdef')
       print(Newdf2.head(1))
       Newdf3=df.sort_values('Bdef')
       print(Newdf3.head(1))
       Newdf4=df.sort_values('SumDef')
       print(Newdf4.head(1))
       df1=df.loc[df['color']== 'white']
cv2.namedWindow('image')
cv2.setMouseCallback('image', average_bgr)

while True:
    cv2.imshow("image", img)
    # esc键
    if cv2.waitKey(8) & 0xFF ==27:
           break
cv2.destroyAllWindows()
