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
root.geometry("400x250")
root.configure(background='white')

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
    
img = PhotoImage(file="buttons/QJsmall.png")
panel = tk.Label(root, image = img)
panel.grid(row=0,column=0,columnspan=3)

    
labelmode = tk.Label(root,text = "請輸入圖片完整名稱\n ex:MQ719.jpg",bg="white")
labelmode.configure(font=("微軟正黑體", 10))
labelmode.grid(row=1)
text=tk.Text(root, width=25,height=1)
text.insert("insert",".jpg")
text.configure(font=("微軟正黑體", 10))
text.grid(row=1,column=1,columnspan=2)

labelmode2 = tk.Label(root,text = "請輸入編號\n ex:MQ719",bg="white")
labelmode2.configure(font=("微軟正黑體", 10))
labelmode2.grid(row=2)
text2=tk.Text(root, width=25,height=1)
text2.grid(row=2,column=1,columnspan=2)
text2.configure(font=("微軟正黑體", 10))

labelmode3 = tk.Label(root,text = "輸入存取資料庫\n",bg="white")
labelmode3.configure(font=("微軟正黑體", 10))
labelmode3.grid(row=3)
text3=tk.Text(root, width=25,height=1)
text3.grid(row=3,column=1,columnspan=2)
text3.insert("insert","MQdata.csv")
text3.configure(font=("微軟正黑體", 10))


img_confirm=PhotoImage(file="buttons/confirm.png")
img_start=PhotoImage(file="buttons/start.png")
btnRead=tk.Button(root, image=img_confirm,text=" ",relief='flat', 
                    command=getTextInput)

btnRead.grid(row=7,column=1)

btnRead2=tk.Button(root, image=img_start,text=" ",relief='flat', 
                    command=quitScreen)

btnRead2.grid(row=7,column=2)

root.mainloop()


def CircleCallback(event,x,y,flags,param):
    c=0
    global refPt,PtBGR,w,h,Serial
    if event == cv2.EVENT_LBUTTONDOWN:
        #下面n代表取樣點數 一般不建議超過1000
        n=1000
        for c in range(0,n):
            c+=1
            N=result2
            
            #若n改變下面999改為n-1
            ranx=(random.randint(0,999))
            rany=(random.randint(0,999))
            refPt.append((ranx,rany))
            Serial.append(N)
            b, g, r = img[ranx,rany]
            PtBGR.append((b,g,r))             
            b=[x[0] for x in PtBGR]
            g=[x[1] for x in PtBGR]
            r=[x[2] for x in PtBGR]
            if len(refPt)==n:
                df = pd.DataFrame(list(zip(Serial,r,g,b)),columns=['Serial no','R','G','B'])
                print(df)
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
        img=cv2.imdecode(np.fromfile(r".multi\%s" % (result),dtype=np.uint8),-1)
        h, w = img.shape[:2]
        cv2.imshow('mouse_callback',img)
        
        if cv2.waitKey(20) == 27:
            break
 
    cv2.destroyAllWindows()
 
 
if __name__ == "__main__":
    main()
