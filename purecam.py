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
    messagebox.showinfo("collecting data", "按C 拍攝,空白鍵開始")
    root2.destroy()
    root3=Tk()
    root3.destroy()
    
def getTextInput():
    global result
    result=text.get(1.0, tk.END+"-1c")

def Result_Print():
    window=Tk()
    window.title("分析結果")
    window.geometry("600x900")
    
    frame2=Frame(window)
    frame2.pack(fill="both")

    
    tablayout=Notebook(frame2)
    tablayout2=Notebook(frame2)


    #交叉配對
    ntab1=Frame(tablayout2)
    ntab1.pack(fill="both")
    for row in range(len(name_n)):
        for column in range(1):
            label=Label(ntab1,width=25,height=2,text=name_n[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)
    for row in range(len(name_n)):
        for column in range(1):
            label=Label(ntab1,width=5,height=2,text="%s" %rate_n[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)

    for row in range(len(name_n)):
        for column in range(1):
            label=Label(ntab1,width=12,height=2,text="%   相似程度",bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=2,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)
    tablayout2.add(ntab1,text="交叉配對結果")

    ntab2=Frame(tablayout2)
    ntab2.pack(fill="both")
  
    for row in range(len(ncol)):
        for column in range(1):
            label=Label(ntab2,width=22,height=1,text=ncol[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=0,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)

    for row in range(len(ncol)):
        for column in range(1):
            label=Label(ntab2,width=22,height=1,text=row_nf3[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)
            
    tablayout2.add(ntab2,text="配方1")

    ntab3=Frame(tablayout2)
    ntab3.pack(fill="both")
    
    for row in range(len(ncol)):
        for column in range(1):
            label=Label(ntab3,width=22,height=1,text=ncol[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=0,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)

    for row in range(len(ncol)):
        for column in range(1):
            label=Label(ntab3,width=22,height=1,text=row_nf32[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)
            
    tablayout2.add(ntab3,text="配方2")

    ntab4=Frame(tablayout2)
    ntab4.pack(fill="both")
    
    for row in range(len(ncol)):
        for column in range(1):
            label=Label(ntab4,width=22,height=1,text=ncol[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=0,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)

    for row in range(len(ncol)):
        for column in range(1):
            label=Label(ntab4,width=22,height=1,text=row_nf33[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)
            
    tablayout2.add(ntab4,text="配方3")

    ntab5=Frame(tablayout2)
    ntab5.pack(fill="both")
    
    for row in range(len(ncol)):
        for column in range(1):
            label=Label(ntab5,width=22,height=1,text=ncol[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=0,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)

    for row in range(len(ncol)):
        for column in range(1):
            label=Label(ntab5,width=22,height=1,text=row_nf3[row],bg="black",fg="white",padx=1,pady=1)
            label.grid(row=row,column=1,sticky="nsew",padx=1,pady=1)
            ntab1.grid_columnconfigure(column,weight=1)
            
    tablayout2.add(ntab5,text="最接近配方")



    #顏色分類
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
    tablayout.add(tab1,text="顏色分類結果")
    
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
    tablayout2.pack()
    window.mainloop()
    

       
def CircleCallback(event,x,y,flags,param):
    #n=手動選取點數可改變
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
        #8=手動選取點數可改變改成n
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
                dfread = pd.read_csv(".data base\\%s" %(result))
                dfread['A']= round((dfread['R'] + dfread['G'] + dfread['B'])/3)
                dfread['S'] = dfread['R'] + dfread['G'] + dfread['B']


                #交叉比對法
                nf=pd.DataFrame(list(zip(r,g,b)),columns=['R','G','B'])
                nfread=dfread[['Serial no','R','G','B']]
                loan=pd.merge(nf,nfread)
                group=loan.groupby('Serial no')
                Newnf=group.count()
                Newnf['P']=round((Newnf['R']/Newnf['R'].sum())* 100)
                Newnf=Newnf.sort_values(by=['R'],ascending=False)
                Rate=Newnf['P'].tolist()
                Newnf.columns = [' '.join(col).strip() for col in Newnf.columns.values]
                nf2=pd.DataFrame(Newnf.to_records())
                nf2=nf2.head(5)
                
                print(nf2)
                if(len(nf2['Serial no'])==0):
                    i=0
                    j=0
                    k=0
                elif(len(nf2['Serial no'])==1):
                    i=nf2.at[0,'Serial no']
                    j=0
                    k=0
                elif(len(nf2['Serial no'])==2):
                    i=nf2.at[0,'Serial no']
                    j=nf2.at[1,'Serial no']
                    k=0
                else:
                    i=nf2.at[0,'Serial no']
                    j=nf2.at[1,'Serial no']
                    k=nf2.at[2,'Serial no']
                print(k)
                nf3=dfread.loc[(dfread['Serial no']==i)].head(1)
                nf4=dfread.loc[(dfread['Serial no']==j)].head(1)
                nf5=dfread.loc[(dfread['Serial no']==k)].head(1)
                nf3=nf3.drop(['R','G','B','color','A','S'],axis=1)
                nf4=nf4.drop(['R','G','B','color','A','S'],axis=1)
                nf5=nf5.drop(['R','G','B','color','A','S'],axis=1)
                nf=pd.concat([nf3, nf4,nf5])
                nf.to_csv(".data base\\test_result2.csv",index=False,encoding="utf_8_sig")
                print(nf)
                ncol=list(nf.columns)
                if(len(nf2['Serial no'])==0):
                    root=tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("失敗", "未找到符合資料")
                elif(len(nf2['Serial no'])==1):
                    row_nf3=nf3.iloc[0].tolist()
                    row_nf32=['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
                    row_nf33=['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']

                elif(len(nf2['Serial no'])==2):
                    row_nf3=nf3.iloc[0].tolist()
                    row_nf32=nf4.iloc[0].tolist()
                    row_nf33=['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
                    
                else:
                    row_nf3=nf3.iloc[0].tolist()
                    row_nf32=nf4.iloc[0].tolist()
                    print(row_nf32)
                    row_nf33=nf5.iloc[0].tolist()
                name_n=nf['Serial no'].tolist()
                rate_n=Rate

                #顏色分類法
                #(可以改)當需要寬鬆一點的比對，刪除下面一段的上下兩個'''
                
                '''
                newdf1=dfread.loc[(dfread['color']==color)|(dfread['A']==SumAvr)]
                newdf2=dfread.loc[(dfread['S']<=(SumRGB+2))&(dfread['S']>=(SumRGB-2))]
                newdf=pd.concat([newdf1, newdf2])
                '''

                #(可以改)當需要嚴格一點的比對，刪除下面一段的上下兩個'''
                '''
                newdf=dfread.loc[(dfread['A']==SumAvr)|(dfread['S']==SumRGB)]
                newdf=newdf.loc[(newdf['color']==color)]
                '''
                
                
                #並在下面一行的開頭加上#
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
                df3.to_csv(".data base\\test_result.csv",index=False,encoding="utf_8_sig")

               
                if df3.empty ==True:
                    root=tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("失敗", "未找到符合資料")
           
                elif len(df3)<=2:
                    root=tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("失敗", "只找到少數資料\n 請再試一次")
                    
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
                            messagebox.showinfo("失敗", "只找到少數資料\n 已存在test_result")
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
    root2.configure(background='white')
    img = PhotoImage(file="buttons/QJsmall.png")
    panel = tk.Label(root2, image = img)
    panel.grid(row=0,column=0,columnspan=3)
    labelmode = tk.Label(root2,text = "請輸入讀取資料庫名稱\n ex:pure_by_cam.csv",bg="white")
    labelmode.configure(font=("微軟正黑體", 10))
    labelmode.grid(row=1)
    text=tk.Text(root2, width=20,height=1)
    text.insert("insert","pure_by_cam.csv")
    text.grid(row=1,column=1,columnspan=2)
    text.configure(font=("微軟正黑體", 10))
    img_confirm=PhotoImage(file="buttons/confirm.png")
    img_start=PhotoImage(file="buttons/start.png")
    
    btnRead=tk.Button(root2, image=img_confirm,text=" ",relief='flat', 
                    command=getTextInput)
    btnRead.grid(row=7,column=1)
    btnRead2=tk.Button(root2, image=img_start,text=" ",relief='flat', 
                    command=quitScreen)
    btnRead2.grid(row=7,column=2)
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
 
        ret, frame = cap.read()
        cv2.namedWindow("capture",0)
        cv2.resizeWindow("capture", 800, 800)
        cv2.imshow("capture", frame)
        input = cv2.waitKey(1) & 0xFF
        if input == ord("c") or input == ord ("C"):
            cv2.imwrite(".test/%d.jpeg" % (index),
                        cv2.resize(frame, (800, 800), interpolation=cv2.INTER_AREA))
            print("%s: %d 張圖片" % (class_name, index))

        if input == ord(' '):
            img=cv2.imread(".test/%d.jpeg" % (index),1)
            cv2.namedWindow('mouse_callback',0)
            cv2.setMouseCallback("mouse_callback",CircleCallback)

    
purecam_start()



def main():
    while (True):
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()
 

if __name__ == "__main__":
    main()
