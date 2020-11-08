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
root = tk.Tk()
root.geometry("400x200")
root.configure(background='white')

def quitScreen():
    messagebox.showinfo("collecting data", "點擊視窗開始分析")
    root.destroy()
    root2=Tk()
    root2.destroy()
    
def getTextInput():
    global result,result2
    result=text.get(1.0, tk.END+"-1c")
    result2=text2.get(1.0, tk.END+"-1c")

    

img = PhotoImage(file="buttons/QJsmall.png")
panel = tk.Label(root, image = img)
panel.grid(row=0,column=0,columnspan=3)

labelmode = tk.Label(root,text = "請輸入圖片完整名稱\n ex:MQ 717.jpg",bg="white")
labelmode.configure(font=("微軟正黑體", 10))
labelmode.grid(row=1)
text=tk.Text(root, width=20,height=1)
text.insert("insert",".jpg")
text.configure(font=("微軟正黑體", 10))
text.grid(row=1,column=2)

labelmode2 = tk.Label(root,text = "請輸入讀取資料庫名稱\n ex:MQdata.csv",bg="white")
labelmode2.configure(font=("微軟正黑體", 10))
labelmode2.grid(row=2)
text2=tk.Text(root, width=20,height=1)
text2.insert("insert","MQdata.csv")
text2.configure(font=("微軟正黑體", 10))
text2.grid(row=2,column=2)

img_confirm=PhotoImage(file="buttons/confirm.png")
img_start=PhotoImage(file="buttons/start.png")
btnRead=tk.Button(root, image=img_confirm,text=" ",relief='flat', 
                    command=getTextInput)

btnRead.grid(row=5,column=1)

btnRead2=tk.Button(root, image=img_start,text=" ",relief='flat', 
                    command=quitScreen)

btnRead2.grid(row=5,column=2)

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
    if event == cv2.EVENT_LBUTTONDOWN:
        #下面n代表取樣點數 若n越大則越精準一般不建議超過1000
        n=500
        for c in range(0,n):
            c+=1
            #若n改變下面499改為n-1
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

            
        
img=cv2.imdecode(np.fromfile(r".multi\%s" % (result),dtype=np.uint8),-1)
cv2.namedWindow('mouse_callback')



cv2.setMouseCallback('mouse_callback',CircleCallback)
 
def main():
    while (True):
        cv2.imshow('mouse_callback',img)
        if cv2.waitKey(20) == 27:
            break
 
    cv2.destroyAllWindows()
 
 
if __name__ == "__main__":
    main()
