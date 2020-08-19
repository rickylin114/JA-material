import cv2
import numpy as np
import pandas as pd
import random
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


r=[]
g=[]
b=[]
refPt = []
Serial=[]
PtBGR=[]
r1=[]
r2=[]
r3=[]
r4=[]
rate=[]
rate2=[]
rate3=[]
r6=[]
r7=[]
r8=[]
r9=[]
add=[]
add2=[]
add3=[]
color_name=[]
locate=[]
brand=[]


#n= int(input("輸入取樣點數:"))

class_name = "test"
refPt = []
PtBGR=[]

index = 1
cap = cv2.VideoCapture(0)
width = 800
height = 800
w = 1400
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

       
def CircleCallback(event,x,y,flags,param):
    n=8
    global refPt,PtBGR,w,h,Serial,r1,r2,r3,r4,rate,rate2,rate3,r6,r7,r8,r9,add,add2,add3,color,b,g,r
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(76,201,255),2)
        refPt.append((x, y))
        b, g, r = img[x,y]
        '''
        Serial.append(result2)
        r1.append(result9)
        r2.append(result10)
        r3.append(result11)
        r4.append(result14)
        rate.append(result4)
        rate2.append(result6)
        rate3.append(result8)
        r6.append(result15)
        r7.append(result16)
        r8.append(result17)
        add.append(result3)
        add2.append(result5)
        add3.append(result7)
        locate.append(result12)
        brand.append(result13)
        '''
        PtBGR.append((b,g,r))
        b=[x[0] for x in PtBGR]
        g=[x[1] for x in PtBGR]
        r=[x[2] for x in PtBGR]

        '''
        dict = {'Serial no': Serial, 'R': r, 'G':g,'B':b,'40-70比例%':r1,'70-120比例%':r2,'325比例%':r3,'砂粉產地':locate,'樹酯品牌':brand,'樹酯比例%':r4[0],
                '色粉1':add,'色粉1比例%(樹酯)':rate,'色粉2':add2,'色粉2比例%(樹酯)':rate2,'色粉3':add3,'色粉3比例%(樹酯)':rate3,'偶聯劑%(樹酯)':r6,'促進劑%(樹酯)':r7,
                '固化劑%(樹酯)':r8}
        df = pd.DataFrame(dict)
        '''
        if len(refPt)==8:
                BAvr=(round(sum(b[0:n])/n))
                GAvr=(round(sum(g[0:n])/n))
                RAvr=(round(sum(r[0:n])/n))
                SumRGB=(BAvr+GAvr+RAvr)
                SumAvr=(round(SumRGB/3))
                color_def(BAvr,GAvr,RAvr)
                color_name.append(color)
                AvrRGB={'R':RAvr,'G':GAvr,'B':BAvr,'Sum':SumRGB,'Avr':SumAvr,'color':color_name}
                df_test = pd.DataFrame(AvrRGB,index=[0])
                print(df_test)
                print(color)
                dfread = pd.read_csv('D:/桌面/JA Material/JA-material/data base/PureColorAvrtest.csv') 
                newdf=dfread.loc[(dfread['color']==color)|(dfread['A']==SumAvr)|(dfread['S']==SumRGB)]
                #df.sort_values("title")
                newdf.insert(1,'Rdif',newdf[['R']].add(-RAvr))
                newdf.insert(2,'Gdif',newdf[['G']].add(-GAvr))
                newdf.insert(3,'Bdif',newdf[['B']].add(-BAvr))
                newdf.insert(4,'Adif',abs(newdf[['A']].add(-SumAvr)))
                newdf.insert(5,'Sdif',abs(newdf[['S']].add(-SumRGB)))
                df=newdf.sort_values(by=['Sdif', 'Adif'], ascending=True)
                df2=df.head(10)
                print(df2)
                filtdf=df2.loc[(df2['Rdif']<30)&(df2['Rdif']>0)&(df2['Adif']<30)&(df2['Adif']>0)&(df2['Sdif']<30)&(df2['Sdif']>0)]
                filtdf2=filtdf.sort_values(by=['R', 'G','B']).head(2)
                Neg_filtdf=df2.loc[(df2['Rdif']>-30)&(df2['Rdif']<0)&(df2['Adif']>-30)&(df2['Adif']<0)&(df2['Sdif']>-30)&(df2['Sdif']<0)]
                Neg_filtdf2=Neg_filtdf.sort_values(by=['R', 'G','B']).head(2)
                print(Neg_filtdf2,filtdf2)
                
                a=df['色粉1比例%(樹酯)'][df['色粉1'].isin(['鈦白粉'])]
                b=df['色粉2比例%(樹酯)'][df['色粉2'].isin(['鈦白粉'])]
                c=df['色粉3比例%(樹酯)'][df['色粉3'].isin(['鈦白粉'])]
                print(a,b,c)
                
                #

                                    
def color_def(BAvr,GAvr,RAvr):
    
        global color
        if abs(int(BAvr)-int(GAvr))<=1 and abs(int(BAvr)-int(RAvr))<=1:
              color='white'
              return color
        
        elif BAvr>=GAvr and BAvr>=RAvr:
               if BAvr-GAvr>3 and BAvr-RAvr>=3:
                      color='blue'
                      return color
     
               elif BAvr-GAvr<3:
                      color='cyan'
                      return color
    
               else:
                      color='purple'
                      return color
   
 
        elif GAvr>=RAvr and GAvr>=BAvr:
               if GAvr-RAvr>3 or GAvr-BAvr>3:
                      color='green'
                      return color
  
               elif GAvr-RAvr<3:
                      color='yellow'
                      return color
                      
               else:
                      color='cyan'
                      return color
  
                      
        elif RAvr>=GAvr and RAvr>=BAvr:
               if RAvr-GAvr>=3 and RAvr-BAvr>=3:
                      color='red'
                      return color

               elif RAvr-GAvr<3:
                      color='yellow'
                      return color

               else:
                      color='purple'
                      return color
 

        else:
              color='white'
              
while True:
        # get a frame
        ret, frame = cap.read()
        # show a frame
        #frame = frame[crop_h_start:crop_h_start+w, crop_w_start:crop_w_start+w]
        cv2.namedWindow("capture",0)
        cv2.resizeWindow("capture", 800, 800)
        cv2.imshow("capture", frame)
        input = cv2.waitKey(1) & 0xFF
        if input == ord("x"):
            cv2.imwrite("%s/%d.jpeg" % (class_name, index),
                        cv2.resize(frame, (800, 800), interpolation=cv2.INTER_AREA))
            print("%s: %d 張圖片" % (class_name, index))
            # bind the callback function to window
        if input == ord(' '):
            img=cv2.imread("%s/%d.jpeg" % (class_name, index),1)
            #print(img.dtype)
            cv2.namedWindow('mouse_callback',0)     
            break
            
            
cv2.setMouseCallback("mouse_callback",CircleCallback)
def main():
    while (True):
        cv2.imshow("mouse_callback",img)
        if cv2.waitKey(20) == 27:
            break
        
    cv2.destroyAllWindows()
 

if __name__ == "__main__":
    main()

cap.release()
cv2.destroyAllWindows()
