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
root.geometry("365x170")

def quitScreen():
    messagebox.showinfo("建立多色資料庫", "點擊視窗開始建立")
    root.destroy()
    root2=Tk()
    root2.destroy()
    
def getTextInput():
    global result,result2,result3
    
    result=text.get(1.0, tk.END+"-1c")
    result2=text2.get(1.0, tk.END+"-1c")
    result3=text3.get(1.0, tk.END+"-1c")

    
labelmode = tk.Label(root,text = "請輸入圖片完整名稱\n ex:MQ719.jpg")
labelmode.configure(font=("微軟正黑體", 10))
labelmode.grid(row=0)
text=tk.Text(root, width=20,height=1)
text.insert("insert",".jpg")
text.grid(row=0,column=2)

labelmode2 = tk.Label(root,text = "請輸入編號\n ex:MQ719")
labelmode2.configure(font=("微軟正黑體", 10))
labelmode2.grid(row=1)
text2=tk.Text(root, width=20,height=1)
text2.grid(row=1,column=2)

labelmode3 = tk.Label(root,text = "輸入存取資料庫\n")
labelmode3.configure(font=("微軟正黑體", 10))
labelmode3.grid(row=2)
text3=tk.Text(root, width=20,height=1)
text3.grid(row=2,column=2)
text3.insert("insert","MQdata.csv")


btnRead=tk.Button(root, height=1, width=10, text="確定", 
                    command=getTextInput)

btnRead.grid(row=5,column=1)

btnRead=tk.Button(root, height=1, width=10, text="開始", 
                    command=quitScreen)

btnRead.grid(row=5,column=2)

root.mainloop()


def CircleCallback(event,x,y,flags,param):
    c=0
    global refPt,PtBGR,w,h,Serial
    if event == cv2.EVENT_LBUTTONDOWN:
        n=1000
        for c in range(0,n):
            c+=1
            N=result2
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
                #df.to_csv("D:\桌面\JA Material\JA-material\data base\\%s" %(result3),index=False, mode='a', header=False,encoding="utf_8_sig")
                df.to_csv(".data base\\%s" %(result3),index=False, mode='a', header=False,encoding="utf_8_sig")
                root2=Tk()
                root2.withdraw()
                messagebox.showinfo("純色板建立資料庫", "成功")
                BAvr=(round(sum(b[0:c])/c))
                GAvr=(round(sum(g[0:c])/c))
                RAvr=(round(sum(r[0:c])/c))
                #print((RAvr,GAvr,BAvr))
                Sum=BAvr+GAvr+RAvr
                


cv2.namedWindow('mouse_callback')
cv2.setMouseCallback('mouse_callback',CircleCallback)
 
def main():
    while (True):
        global img
        #img=cv2.imdecode(np.fromfile(r"D:\桌面\JA Material\JA-material\multi\%s" % (result),dtype=np.uint8),-1)
        img=cv2.imdecode(np.fromfile(r".multi\%s" % (result),dtype=np.uint8),-1)
        h, w = img.shape[:2]
        cv2.imshow('mouse_callback',img)
        
        if cv2.waitKey(20) == 27:
            break
 
    cv2.destroyAllWindows()
 
 
if __name__ == "__main__":
    main()
