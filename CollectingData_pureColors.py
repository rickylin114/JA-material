import cv2
import numpy as np
import pandas as pd
import random


refPt = []
Serial=[]
PtBGR=[]
r1=[]
r2=[]
r3=[]
r4=[]
r5=[]
r6=[]
r7=[]
r8=[]
r9=[]
add=[]
color_name=[]
locate=[]
img=cv2.imread('104432 7.jpg',1)
h, w = img.shape[:2]
color='none'
#n= int(input("輸入取樣點數:"))


def CircleCallback(event,x,y,flags,param):
    c=0
    global refPt,PtBGR,w,h,Serial,r1,r2,r3,r4,r5,r6,r7,r8,r9,add,color
    if event == cv2.EVENT_LBUTTONDOWN:
        n=100
        for c in range(0,n):
            c+=1
            N="104432 河源7%白"
            ranx=(random.randint(0,99))
            rany=(random.randint(0,99))
            refPt.append((ranx,rany))
            Serial.append(N)
            r1.append(10)
            r2.append(44)
            r3.append(32)
            r4.append(13.8)
            r5.append(7)
            r6.append(1.2)
            r7.append(0.16)
            r8.append(0.53)
            add.append("鈦白粉(佔樹酯比例)")
            locate.append("河源")
            b, g, r = img[ranx,rany]
            PtBGR.append((b,g,r))
            Avr=round((int(b)+int(g)+int(r))/3)
            color_def(b,g,r,Avr)
            color_name.append(color)
            #print(PtBGR[0:n])
            b=[x[0] for x in PtBGR]
            g=[x[1] for x in PtBGR]
            r=[x[2] for x in PtBGR]
            if len(refPt)==n:
                df = pd.DataFrame(list(zip(Serial,r,g,b,r1,r2,r3,locate,r4,add,r5,r6,r7,r8,color_name))
                                  ,columns=['Serial no','R','G','B','40-70比例%',
                                            '70-120比例%','325比例%','砂粉產地','樹酯比例%','色粉種類','色粉比例%(樹酯)',
                                            '偶聯劑%(樹酯)','促進劑%(樹酯)','固化劑%(樹酯)','顏色'])
                print(df)
                #df.to_csv('D:/桌面/JA Material/JA-material/data base/PureColorBig.csv',index=False, mode='a', header=False,encoding="utf_8_sig")
                '''
                match(b,g,r,Avr)
                df = pd.DataFrame(list(zip(Serial,r,g,b)),
                                  columns=['Serial no','R','G','B']
                                  '''
                                  
def color_def(b,g,r,Avr):
    
        global color
        if abs(int(b)-int(g))<=1 and abs(int(b)-int(r))<=1:
              color='White'
              return color
        
        elif b>=g and b>=r:
               if b-g>5 and b-r>=5:
                      color='Blue'
                      return color
     
               elif b-g<5:
                      color='Cyan'
                      return color
    
               else:
                      color='Purple'
                      return color
   
 
        elif g>=r and g>=b:
               if g-r>5 or g-b>5:
                      color='Green'
                      return color
  
               elif g-r<5:
                      color='Yellow'
                      return color
                      
               else:
                      color='Cyan'
                      return color
  
                      
        elif r>=g and r>=b:
               if r-g>=5 and r-b>=5:
                      color='Red'
                      return color

               elif r-g<5:
                      color='Yellow'
                      return color

               else:
                      color='Purple'
                      return color
 

        else:
              color='White'
              

cv2.namedWindow('mouse_callback')

# bind the callback function to window

cv2.setMouseCallback('mouse_callback',CircleCallback)
 
def main():
    while (True):
        cv2.imshow('mouse_callback',img)
        if cv2.waitKey(20) == 27:
            break
 
    cv2.destroyAllWindows()
 
 
if __name__ == "__main__":
    main()
