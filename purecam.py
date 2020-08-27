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



def quitScreen():
    messagebox.showinfo("collecting data", "按x 拍攝,空白鍵開始")
    root2.destroy()
    root3=Tk()
    root3.destroy()
    
def getTextInput():
    global result
    result=text.get(1.0, tk.END+"-1c")

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
    
    for row in range(len(col)):
        for column in range(1):
            label=Label(tab2,width=22,height=1,text=col[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=0,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)

    for row in range(len(col)):
        for column in range(1):
            label=Label(tab2,width=22,height=1,text=row_df3[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)
            
    tablayout.add(tab2,text="配方1")

    tab3=Frame(tablayout)
    tab3.pack(fill="both")
    
    for row in range(len(col)):
        for column in range(1):
            label=Label(tab3,width=22,height=1,text=col[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=0,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)

    for row in range(len(col)):
        for column in range(1):
            label=Label(tab3,width=22,height=1,text=row_df32[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)
            
    tablayout.add(tab3,text="配方2")

    tab4=Frame(tablayout)
    tab4.pack(fill="both")
    
    for row in range(len(col)):
        for column in range(1):
            label=Label(tab4,width=22,height=1,text=col[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=0,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)

    for row in range(len(col)):
        for column in range(1):
            label=Label(tab4,width=22,height=1,text=row_df33[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)
            
    tablayout.add(tab4,text="配方3")

    tab5=Frame(tablayout)
    tab5.pack(fill="both")
    
    for row in range(len(col)):
        for column in range(1):
            label=Label(tab5,width=22,height=1,text=col[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=0,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)

    for row in range(len(col)):
        for column in range(1):
            label=Label(tab5,width=22,height=1,text=row_text[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)
            
    tablayout.add(tab5,text="最接近配方")
    
    tablayout.pack()
    
    window.mainloop()
    

       
def CircleCallback(event,x,y,flags,param):
    n=8
    global refPt,PtBGR,w,h,Serial,r1,r2,r3,r4,rate,rate2,rate3,r6,r7,r8,r9,add,add2,add3,color,b,g,r,df3,name,rate,col,row_text
    global row_df3,row_df32,row_df33,row_text2
    cv2.imshow("mouse_callback",img)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(76,201,255),2)
        refPt.append((x, y))
        b, g, r = img[x,y]
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
                cv2.destroyAllWindows()
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
                #dfread = pd.read_csv("D:\桌面\JA Material\JA-material\data base\\%s" %(result))
                dfread = pd.read_csv(".data base\\%s" %(result))
                dfread['A']= round((dfread['R'] + dfread['G'] + dfread['B'])/3)
                dfread['S'] = dfread['R'] + dfread['G'] + dfread['B']
                newdf=dfread.loc[(dfread['color']==color)|(dfread['A']==SumAvr)|(dfread['S']==SumRGB)]
    
                newdf.insert(1,'Rdif',newdf[['R']].add(-RAvr))
                newdf.insert(2,'Gdif',newdf[['G']].add(-GAvr))
                newdf.insert(3,'Bdif',newdf[['B']].add(-BAvr))
                newdf.insert(4,'Adif',abs(newdf[['A']].add(-SumAvr)))
                newdf.insert(5,'Sdif',abs(newdf[['S']].add(-SumRGB)))
                df=newdf.sort_values(by=['Sdif', 'Adif'], ascending=True).head(100)
                df.insert(1,'dalta',abs(df['Rdif']+df['Gdif']+df['Bdif']))
                df=df.sort_values(by=['dalta'],ascending=True)
                data=df[['Serial no','color']]
                group=data.groupby('Serial no')
                datacount=group.count()
                df=df.merge(datacount,left_on='Serial no',right_index=True)
                df=df.sort_values(by=['color_y'],ascending=False)
                df3=df.drop_duplicates('Serial no', keep='first', inplace=False).head()
                print(df3)

                if df3.empty ==True:
                    root=tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("失敗", "未找到符合資料")
                    #print(filtdf,Neg_filtdf)
                elif len(df3)<=2:
                    root=tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("失敗", "未找到符合資料")
                else:
                    Zero=df3.loc[(df3['Rdif']==0)&(df3['Gdif']==0)&(df3['Bdif']==0)]
                    Zero=Zero.head(3)
                    if Zero.empty==False:
                        Zero=Zero.drop(['R','G','B','dalta','Rdif','Gdif','Bdif','A','S','Adif','Sdif','color_x','color_y'],axis=1)
                        name=df3['Serial no'].tolist()
                        rate=df3['color_y'].tolist()
                        col=list(Zero.columns)
                        row_text=Zero.iloc[0].tolist()
                        df3=df3.drop(['R','G','B','dalta','Rdif','Gdif','Bdif','A','S','Adif','Sdif','color_x','color_y'],axis=1)
                        row_df3=df3.iloc[0].tolist()
                        row_df32=df3.iloc[1].tolist()
                        row_df33=df3.iloc[2].tolist()
                        Result_Print()
                        print('0')
                        print(Zero)
                    
                    else:
                        filtdf=df3.loc[(df3['A']>=SumAvr)]
                        filtdf=filtdf.sort_values(by=['Rdif','Gdif','Bdif']).head()
                        Neg_filtdf=df3.loc[(df3['A']<SumAvr)]
                        Neg_filtdf=Neg_filtdf.sort_values(by=['Rdif','Gdif','Bdif']).head()
                        #print(filtdf,Neg_filtdf)
                        if Neg_filtdf.empty==True and filtdf.empty ==True:
                            root=tk.Tk()
                            root.withdraw()
                            messagebox.showinfo("失敗", "未找到符合資料")
                        else:
                            filtdf=filtdf.drop(['R','G','B','dalta','Rdif','Gdif','Bdif','A','S','Adif','Sdif','color_x','color_y'],axis=1)
                            name=df3['Serial no'].tolist()
                            rate=df3['color_y'].tolist()
                            col=list(filtdf.columns)
                            row_text=filtdf.iloc[0].tolist()
                            df3=df3.drop(['R','G','B','dalta','Rdif','Gdif','Bdif','A','S','Adif','Sdif','color_x','color_y'],axis=1)
                            row_df3=df3.iloc[0].tolist()
                            row_df32=df3.iloc[1].tolist()
                            row_df33=df3.iloc[2].tolist()
                            Result_Print()
                            print("最接近的為1",filtdf.head(1))
                
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
              
def purecam_start():
    global class_name,refPt,PtBGR,index,cap,width,height,w,root2,text,img
    root2 = tk.Tk()
    root2.geometry("400x200")
    #n= int(input("輸入取樣點數:"))
    labelmode = tk.Label(root2,text = "請輸入讀取資料庫名稱\n ex:pure_by_cam.csv")
    labelmode.configure(font=("微軟正黑體", 10))
    labelmode.grid(row=1)
    text=tk.Text(root2, width=20,height=1)
    text.insert("insert","pure_by_cam.csv")
    text.grid(row=1,column=2)
    btnRead=tk.Button(root2, height=1, width=10, text="確定", 
                    command=getTextInput)
    btnRead.grid(row=5,column=1)
    btnRead=tk.Button(root2, height=1, width=10, text="開始", 
                    command=quitScreen)
    btnRead.grid(row=5,column=2)
    root2.mainloop()
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
    
        
purecam_start()



def main():
    while (True):
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()
 

if __name__ == "__main__":
    main()
