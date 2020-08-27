import cv2
import numpy as np
import pandas as pd
import tkinter as tk
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Scale,Tk
from tkinter.ttk import Notebook

refPt = []
PtBGR=[]
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
boolean=False


root = tk.Tk()
root.geometry("400x200")

def quitScreen():
    messagebox.showinfo("collecting data", "點擊視窗開始分析")
    root.destroy()
    root2=Tk()
    root2.destroy()
    
def getTextInput():
    global result,result2
    result=text.get(1.0, tk.END+"-1c")
    result2=text2.get(1.0, tk.END+"-1c")

    
labelmode = tk.Label(root,text = "請輸入圖片完整名稱\n ex:104432 w7.jpg")
labelmode.configure(font=("微軟正黑體", 10))
labelmode.grid(row=0)
text=tk.Text(root, width=20,height=1)
text.insert("insert",".jpg")
text.grid(row=0,column=2)

labelmode2 = tk.Label(root,text = "請輸入讀取資料庫名稱\n ex:PureColorBig.csv")
labelmode2.configure(font=("微軟正黑體", 10))
labelmode2.grid(row=1)
text2=tk.Text(root, width=20,height=1)
text2.insert("insert","PureColorBig.csv")
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
                BAvr=(round(sum(b[0:n])/n))
                GAvr=(round(sum(g[0:n])/n))
                RAvr=(round(sum(r[0:n])/n))
                SumRGB=(BAvr+GAvr+RAvr)
                SumAvr=(round(SumRGB/3))
                color_def(BAvr,GAvr,RAvr)
                color_name.append(color)
                AvrRGB={'R':RAvr,'G':GAvr,'B':BAvr,'Sum':SumRGB,'Avr':SumAvr,'color':color_name}
                df_test = pd.DataFrame(AvrRGB,index=[0])
                #dfread = pd.read_csv("D:\桌面\JA Material\JA-material\data base\\%s" %(result2))
                dfread = pd.read_csv(".data base\\%s" %(result2))
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
           
                elif len(df3)<=2:
                    root=tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("失敗", "請再試一次")
                    
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
              color='White'
              return color
        
        elif BAvr>=GAvr and BAvr>=RAvr:
               if BAvr-GAvr>3 and BAvr-RAvr>=3:
                      color='Blue'
                      return color
     
               elif BAvr-GAvr<3:
                      color='Cyan'
                      return color
    
               else:
                      color='Purple'
                      return color
   
 
        elif GAvr>=RAvr and GAvr>=BAvr:
               if GAvr-RAvr>3 or GAvr-BAvr>3:
                      color='Green'
                      return color
  
               elif GAvr-RAvr<3:
                      color='Yellow'
                      return color
                      
               else:
                      color='Cyan'
                      return color
  
                      
        elif RAvr>=GAvr and RAvr>=BAvr:
               if RAvr-GAvr>=3 and RAvr-BAvr>=3:
                      color='Red'
                      return color

               elif RAvr-GAvr<3:
                      color='Yellow'
                      return color

               else:
                      color='Purple'
                      return color
 

        else:
              color='White'


#img=cv2.imdecode(np.fromfile(r"D:\桌面\JA Material\JA-material\pure\%s" % (result),dtype=np.uint8),-1)          
img=cv2.imdecode(np.fromfile(r".pure\%s" % (result),dtype=np.uint8),-1)
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
