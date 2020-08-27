import cv2
import numpy as np
import pandas as pd
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Scale,Tk
from tkinter.ttk import Notebook


refPt = []
PtBGR=[]
#n= int(input("輸入取樣點數:"))
root = tk.Tk()
root.geometry("400x200")

def quitScreen():
    messagebox.showinfo("collecting data", "按x 拍攝,空白鍵開始")
    root.destroy()
    root2=Tk()
    root2.destroy()
    
def getTextInput():
    global result2
    result2=text2.get(1.0, tk.END+"-1c")


labelmode2 = tk.Label(root,text = "請輸入讀取資料庫名稱\n ex:MQdata.csv")
labelmode2.configure(font=("微軟正黑體", 10))
labelmode2.grid(row=1)
text2=tk.Text(root, width=20,height=1)
text2.insert("insert","Muti_by_cam.csv")
text2.grid(row=1,column=2)

btnRead=tk.Button(root, height=1, width=10, text="確定", 
                    command=getTextInput)

btnRead.grid(row=5,column=1)

btnRead=tk.Button(root, height=1, width=10, text="開始", 
                    command=quitScreen)

btnRead.grid(row=5,column=2)

root.mainloop()

def Result_Print():
    window=Tk()
    window.title("Results")
    window.geometry("600x800")
    frame2=Frame(window)
    frame2.pack(fill="both")
    tablayout=Notebook(frame2)
    
    tab1=Frame(tablayout)
    tab1.pack(fill="both")
    for row in range(len(name)):
        for column in range(1):
            label=Label(tab1,width=25,height=2,text=name[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)
    for row in range(len(name)):
        for column in range(1):
            label=Label(tab1,width=5,height=2,text="%s" %rate[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)

    for row in range(len(name)):
        for column in range(1):
            label=Label(tab1,width=12,height=2,text="%   相似程度",bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=2,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)
    tablayout.add(tab1,text="配方分析結果")

    tab2=Frame(tablayout)
    tab2.pack(fill="both")
    
    for row in range(len(name2)):
        for column in range(1):
            label=Label(tab2,width=22,height=1,text=name2[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=0,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)

    for row in range(len(name2)):
        for column in range(1):
            label=Label(tab2,width=22,height=1,text=many[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)
            
    tablayout.add(tab2,text="詳細資料")
    
    tablayout.pack()
    window.mainloop()
    
    
def CircleCallback(event,x,y,flags,param):
    c=0
    global refPt,PtBGR,w,h,Serial,name,rate,name2,many
    cv2.imshow("mouse_callback",img)
    if event == cv2.EVENT_LBUTTONDOWN:
        n=500
        for c in range(0,n):
            c+=1
            ranx=(random.randint(0,499))
            rany=(random.randint(0,499))
            refPt.append((ranx,rany))
            b, g, r = img[ranx,rany]
            PtBGR.append((b,g,r))             
            #print(PtBGR[0:n])
            b=[x[0] for x in PtBGR]
            g=[x[1] for x in PtBGR]
            r=[x[2] for x in PtBGR]
            if len(refPt)==n:
                #df = pd.read_csv("D:\桌面\JA Material\JA-material\data base\\%s" %(result2))
                df = pd.read_csv(".data base\\%s" %(result2))
                df_test = pd.DataFrame(list(zip(r,g,b)),columns=['R','G','B'])
                loan=pd.merge(df_test,df)
                group=loan.groupby('Serial no')
                Newdf=group.count()
                Newdf['P']=round((Newdf['R']/Newdf['R'].sum())* 100)
                Newdf=Newdf.sort_values(by=['R'],ascending=False)
                Newdf.columns = [' '.join(col).strip() for col in Newdf.columns.values]
                df2=pd.DataFrame(Newdf.to_records())
                df3=df2.head(10)
                name2=df3['Serial no'].tolist()
                many=df3['R'].tolist()
                df2=df2.head()
                rate=df2['P'].tolist()
                name=df2['Serial no'].tolist()
                Result_Print()

            
def purecam_start():
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
            cv2.namedWindow('mouse_callback',0)
            break
    cv2.setMouseCallback("mouse_callback",CircleCallback)
    
        
purecam_start()



def main():
    while (True):
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()
 

if __name__ == "__main__":
    main()
