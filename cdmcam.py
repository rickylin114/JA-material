import cv2
import numpy as np
import pandas as pd
import random
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

refPt = []
Serial=[]
PtBGR=[]

root = tk.Tk()
root.geometry("290x145")

def quitScreen():
    messagebox.showinfo("建立多色資料庫", "按x 拍攝,空白鍵開始")
    root.destroy()
    root2=Tk()
    root2.destroy()
    
def getTextInput():
    global result,result2
    result=text.get(1.0, tk.END+"-1c")
    result2=text2.get(1.0, tk.END+"-1c")

labelmode1 = tk.Label(root,text = "請輸入存取資料庫")
labelmode1.configure(font=("微軟正黑體", 10))
labelmode1.grid(row=1,padx=5,pady=10)
text=tk.Text(root, width=20,height=1)
text.grid(row=1,column=1,padx=5,pady=10)
text.insert("insert","Muti_by_cam.csv")

labelmode2 = tk.Label(root,text = "請輸入編號\n ex:MQ719")
labelmode2.configure(font=("微軟正黑體", 10))
labelmode2.grid(row=2,padx=5,pady=10)
text2=tk.Text(root, width=20,height=1)
text2.grid(row=2,column=1,padx=5,pady=10)

btnRead=tk.Button(root, height=1, width=10, text="確定", 
                    command=getTextInput)

btnRead.grid(row=5,column=0,padx=5)

btnRead=tk.Button(root, height=1, width=10, text="開始", 
                    command=quitScreen)

btnRead.grid(row=5,column=1,padx=5)

root.mainloop()


def CircleCallback(event,x,y,flags,param):
    c=0
    global refPt,PtBGR,w,h,Serial
    cv2.imshow("mouse_callback",img)
    if event == cv2.EVENT_LBUTTONDOWN:
        n=500
        for c in range(0,n):
            c+=1
            N=result2
            ranx=(random.randint(0,499))
            rany=(random.randint(0,499))
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
                #df.to_csv("D:\桌面\JA Material\JA-material\data base\\%s" %(result))
                df.to_csv(".data base\\%s" %(result),index=False, mode='a', header=False,encoding="utf_8_sig")
                root2=Tk()
                root2.withdraw()
                messagebox.showinfo("純色板建立資料庫", "成功")
                BAvr=(round(sum(b[0:c])/c))
                GAvr=(round(sum(g[0:c])/c))
                RAvr=(round(sum(r[0:c])/c))
                #print((RAvr,GAvr,BAvr))
                Sum=BAvr+GAvr+RAvr
                

 
def multicam_start():
    global class_name,refPt,PtBGR,index,cap,width,height,w,root2,text,img
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
    while True:
        # get a frame
        ret, frame = cap.read()
        # show a frame
        #frame = frame[crop_h_start:crop_h_start+w, crop_w_start:crop_w_start+w]
        cv2.namedWindow("capture",0)
        cv2.resizeWindow("capture", 800, 800)
        cv2.imshow("capture", frame)
        input = cv2.waitKey(1) & 0xFF
        if input == ord("x") or input == ord ("X"):
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
    
        
multicam_start()


def main():
    while (True):
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()
 

if __name__ == "__main__":
    main()

