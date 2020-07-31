import cv2
import numpy as np
import pandas as pd

df= pd.read_csv("D:/桌面/JA Material/JA-material/data base/MQdata.csv")
refPt = []
PtBGR=[]

#n= int(input("輸入取樣點數:"))


def CircleCallback(event,x,y,flags,param):
    n=8
    global refPt,PtBGR
    if event == cv2.EVENT_LBUTTONDOWN:
            refPt.append((x, y))
            b, g, r = img[x,y]
            PtBGR.append((b,g,r))
            #print(refPt[0:n])
            #print(PtBGR[0:n])
            b=[x[0] for x in PtBGR]
            g=[x[1] for x in PtBGR]
            r=[x[2] for x in PtBGR]
            cv2.circle(img,(x,y),5,(76,201,255),2)
            if len(refPt)==8:
                BAvr=(round(sum(b[0:n])/n))
                GAvr=(round(sum(g[0:n])/n))
                RAvr=(round(sum(r[0:n])/n))
                print((RAvr,GAvr,BAvr))
                Avr=round((BAvr+GAvr+RAvr)/3)
                color(BAvr,GAvr,RAvr,Avr)
                #match(BAvr,GAvr,RAvr,Avr)

                
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
                     
               else:
                      print('Purple')

        else:
              print(RAvr)
              print(BAvr)
              print(GAvr)
              print('White')

'''
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
'''
#cv2.namedWindow('image')
#cv2.setMouseCallback('image', average_bgr)
            
img=cv2.imread('MQ236.jpg',1)
print(img.dtype)
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
