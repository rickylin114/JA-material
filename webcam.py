import cv2
import numpy as np
import pandas as pd

print("=============================================")
print("=  熱鍵(請在攝像頭的視窗使用)：             =")
print("=  x: 拍攝圖片                              =")
print("=  空白鍵: 開始選取八個點                   =")
print("=============================================")

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
'''
crop_w_start = (width-w)//2
crop_h_start = (height-w)//2
'''
def CircleCallback(event,x,y,flags,param):
    n=8
    global refPt,PtBGR
    if event == cv2.EVENT_LBUTTONDOWN:
            refPt.append((x, y))
            b, g, r = img[x,y]
            PtBGR.append((b,g,r))
            print((b,g,r))
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
