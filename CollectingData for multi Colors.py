import cv2
import numpy as np
import pandas as pd
import random


refPt = []
Serial=[]
PtBGR=[]
img=cv2.imread('1MQ719jpg',1)
h, w = img.shape[:2]
#n= int(input("輸入取樣點數:"))


def CircleCallback(event,x,y,flags,param):
    c=0
    global refPt,PtBGR,w,h,Serial
    if event == cv2.EVENT_LBUTTONDOWN:
        n=1000
        for c in range(0,n):
            c+=1
            N="MQ719"
            ranx=(random.randint(0,999))
            rany=(random.randint(0,999))
            refPt.append((ranx,rany))
            Serial.append(N)
            b, g, r = img[ranx,rany]
            PtBGR.append((b,g,r))             
            #print(PtBGR[0:n])
            b=[x[0] for x in PtBGR]
            g=[x[1] for x in PtBGR]
            r=[x[2] for x in PtBGR]
            if len(refPt)==n:
                #print(refPt[0:c])
                df = pd.DataFrame(list(zip(Serial,r,g,b)),columns=['Serial no','R','G','B'])
                print(df)
                df.to_csv('D:/桌面/JA Material/JA-material/data base/MQdata大板.csv',mode='a', header=False,index=False)
                BAvr=(round(sum(b[0:c])/c))
                GAvr=(round(sum(g[0:c])/c))
                RAvr=(round(sum(r[0:c])/c))
                print((RAvr,GAvr,BAvr))
                Sum=BAvr+GAvr+RAvr
                
                '''
                color(BAvr,GAvr,RAvr,Avr)
                match(BAvr,GAvr,RAvr,Avr)
                    
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

#cv2.namedWindow('image')
#cv2.setMouseCallback('image', average_bgr)
            
'''

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
