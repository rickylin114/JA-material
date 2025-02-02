import cv2
import numpy as np
import pandas as pd
import random
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

print("=============================================")
print("=  熱鍵(請在攝像頭的視窗使用)：             =")
print("=  x: 拍攝圖片                              =")
print("=  空白鍵: 開始選取八個點                   =")
print("=============================================")

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
locate=[]
brand=[]
color_list=[]
#n= int(input("輸入取樣點數:"))

root = tk.Tk()
root.geometry("600x600")
def quitScreen():
    messagebox.showinfo("建立純色資料庫",  "按C 拍攝,空白鍵開始")
    root.destroy()
    root2=Tk()
    root2.destroy()

def getTextInput():
    global result2,result3,result4,result5,result6
    global result7,result8,result9,result10,result11,result12
    global result13,result14,result15,result16,result17,result18
    #result=text.get(1.0, tk.END+"-1c")
    result2=text2.get(1.0, tk.END+"-1c")
    result3=text3.get(1.0, tk.END+"-1c")
    result4=text4.get(1.0, tk.END+"-1c")
    result5=text5.get(1.0, tk.END+"-1c")
    result6=text6.get(1.0, tk.END+"-1c")
    result7=text7.get(1.0, tk.END+"-1c")
    result8=text8.get(1.0, tk.END+"-1c")
    result9=text9.get(1.0, tk.END+"-1c")
    result10=text10.get(1.0, tk.END+"-1c")
    result11=text11.get(1.0, tk.END+"-1c")
    result12=text12.get(1.0, tk.END+"-1c")
    result13=text13.get(1.0, tk.END+"-1c")
    result14=text14.get(1.0, tk.END+"-1c")
    result15=text15.get(1.0, tk.END+"-1c")
    result16=text16.get(1.0, tk.END+"-1c")
    result17=text17.get(1.0, tk.END+"-1c")
    result18=text18.get(1.0, tk.END+"-1c")
    

labelmode2 = tk.Label(root,text = "請輸入編號\n ex:391532 河源7%白")
labelmode2.configure(font=("微軟正黑體", 10))
labelmode2.grid(row=1)
text2=tk.Text(root, width=20,height=1)
text2.insert("insert","391532 河源7%白")
text2.configure(font=("微軟正黑體", 10))
text2.grid(row=1,column=1)

labelmode3 = tk.Label(root,text = "色粉種類1\n ex:鈦白粉")
labelmode3.configure(font=("微軟正黑體", 10))
labelmode3.grid(row=2)
text3=tk.Text(root, width=20,height=1)
text3.insert("insert","鈦白粉")
text3.configure(font=("微軟正黑體", 10))
text3.grid(row=2,column=1)

labelmode4 = tk.Label(root,text = "佔樹酯比例%\n ex:0")
labelmode4.configure(font=("微軟正黑體", 10))
labelmode4.grid(row=2,column=2)
text4=tk.Text(root,width=20, height=1)
text4.insert("insert","0")
text4.configure(font=("微軟正黑體", 10))
text4.grid(row=2,column=3)

labelmode5 = tk.Label(root,text = "色粉種類2\n ex:鐵黑粉")
labelmode5.configure(font=("微軟正黑體", 10))
labelmode5.grid(row=3)
text5=tk.Text(root, width=20,height=1)
text5.insert("insert","鐵黑粉")
text5.configure(font=("微軟正黑體", 10))
text5.grid(row=3,column=1)

labelmode6 = tk.Label(root,text = "佔樹酯比例%\n ex:1")
labelmode6.configure(font=("微軟正黑體", 10))
labelmode6.grid(row=3,column=2)
text6=tk.Text(root, width=20,height=1)
text6.insert("insert","0")
text6.configure(font=("微軟正黑體", 10))
text6.grid(row=3,column=3)

labelmode7 = tk.Label(root,text = "色粉種類3\n ex:炭黑粉")
labelmode7.configure(font=("微軟正黑體", 10))
labelmode7.grid(row=4)
text7=tk.Text(root, width=20,height=1)
text7.insert("insert","無")
text7.configure(font=("微軟正黑體", 10))
text7.grid(row=4,column=1)

labelmode8 = tk.Label(root,text = "佔樹酯比例%\n ex:2")
labelmode8.configure(font=("微軟正黑體", 10))
labelmode8.grid(row=4,column=2)
text8=tk.Text(root, width=20,height=1)
text8.insert("insert","0")
text8.configure(font=("微軟正黑體", 10))
text8.grid(row=4,column=3)

labelmode9 = tk.Label(root,text = "砂粉40-70比例\n%")
labelmode9.configure(font=("微軟正黑體", 10))
labelmode9.grid(row=5)
text9=tk.Text(root, width=20,height=1)
text9.insert("insert","39")
text9.configure(font=("微軟正黑體", 10))
text9.grid(row=5,column=1)

labelmode10 = tk.Label(root,text = "砂粉70-120比例%\n")
labelmode10.configure(font=("微軟正黑體", 10))
labelmode10.grid(row=5,column=2)
text10=tk.Text(root, width=20,height=1)
text10.insert("insert","15")
text10.configure(font=("微軟正黑體", 10))
text10.grid(row=5,column=3)

labelmode11 = tk.Label(root,text = "砂粉325比例%\n")
labelmode11.configure(font=("微軟正黑體", 10))
labelmode11.grid(row=6)
text11=tk.Text(root, width=20,height=1)
text11.insert("insert","32")
text11.configure(font=("微軟正黑體", 10))
text11.grid(row=6,column=1)

labelmode12 = tk.Label(root,text = "砂粉產地\n ex:河源")
labelmode12.configure(font=("微軟正黑體", 10))
labelmode12.grid(row=6,column=2)
text12=tk.Text(root, width=20,height=1)
text12.insert("insert","河源")
text12.configure(font=("微軟正黑體", 10))
text12.grid(row=6,column=3)

labelmode13 = tk.Label(root,text = "樹酯品牌\n")
labelmode13.configure(font=("微軟正黑體", 10))
labelmode13.grid(row=7)
text13=tk.Text(root, width=20,height=1)
text13.insert("insert","亞邦樹酯")
text13.configure(font=("微軟正黑體", 10))
text13.grid(row=7,column=1)

labelmode14 = tk.Label(root,text = "樹酯比例\n")
labelmode14.configure(font=("微軟正黑體", 10))
labelmode14.grid(row=7,column=2)
text14=tk.Text(root, width=20,height=1)
text14.insert("insert","15.8")
text14.configure(font=("微軟正黑體", 10))
text14.grid(row=7,column=3)

labelmode15 = tk.Label(root,text = "偶聯劑%(樹酯)\n")
labelmode15.configure(font=("微軟正黑體", 10))
labelmode15.grid(row=8)
text15=tk.Text(root, width=20,height=1)
text15.insert("insert","1.2")
text15.configure(font=("微軟正黑體", 10))
text15.grid(row=8,column=1)

labelmode16 = tk.Label(root,text = "促進劑%(樹酯)\n")
labelmode16.configure(font=("微軟正黑體", 10))
labelmode16.grid(row=8,column=2)
text16=tk.Text(root, width=20,height=1)
text16.insert("insert","0.16")
text16.configure(font=("微軟正黑體", 10))
text16.grid(row=8,column=3)

labelmode17 = tk.Label(root,text = "固化劑%(樹酯)\n")
labelmode17.configure(font=("微軟正黑體", 10))
labelmode17.grid(row=9)
text17=tk.Text(root, width=20,height=1)
text17.insert("insert","0.53")
text17.configure(font=("微軟正黑體", 10))
text17.grid(row=9,column=1)

labelmode18 = tk.Label(root,text = "輸入存取資料庫\n")
labelmode18.configure(font=("微軟正黑體", 10))
labelmode18.grid(row=9,column=2)
text18=tk.Text(root, width=20,height=1)
text18.grid(row=9,column=3)
text18.insert("insert","pure_by_cam.csv")
text18.configure(font=("微軟正黑體", 10))

img_confirm=PhotoImage(file="buttons/confirm.png")
img_start=PhotoImage(file="buttons/start.png")
btnRead=tk.Button(root, image=img_confirm,text=" ",relief='flat', 
                    command=getTextInput)

btnRead.grid(row=12,column=2)

btnRead2=tk.Button(root, image=img_start,text=" ",relief='flat', 
                    command=quitScreen)

btnRead2.grid(row=12,column=3)

root.mainloop()

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

       
def CircleCallback(event,x,y,flags,param):
    n=8
    c=0
    cv2.imshow("mouse_callback",img)
    global refPt,PtBGR,w,h,Serial,r1,r2,r3,r4,rate,rate2,rate3,r6,r7,r8,r9,add,add2,add3,b,g,r,color_list
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(76,201,255),2)
        refPt.append((x, y))
        print(x,y)
        b, g, r = img[x,y]
        Serial.append(result2)
        r1.append(result9)
        r2.append(result10)
        r3.append(result11)
        r4.append(result14)
        rate.append(result4)
        rate2.append(result6)
        rate3.append(result8)
        r6.append(result15)
        r7.append(result16)
        r8.append(result17)
        add.append(result3)
        add2.append(result5)
        add3.append(result7)
        locate.append(result12)
        brand.append(result13)
        PtBGR.append((b,g,r))
        b=[x[0] for x in PtBGR]
        g=[x[1] for x in PtBGR]
        r=[x[2] for x in PtBGR]
        rr=int(r[len(refPt)-1])
        gg=int(g[len(refPt)-1])
        bb=int(b[len(refPt)-1])
        color_def(rr,gg,bb)
        color_list.append(color)
        dict = {'Serial no': Serial, 'R': r, 'G':g,'B':b,'40-70比例%':r1,'70-120比例%':r2,'325比例%':r3,'砂粉產地':locate,'樹酯品牌':brand,'樹酯比例%':r4[0],
                '色粉1':add,'色粉1比例%(樹酯)':rate,'色粉2':add2,'色粉2比例%(樹酯)':rate2,'色粉3':add3,'色粉3比例%(樹酯)':rate3,'偶聯劑%(樹酯)':r6,'促進劑%(樹酯)':r7,
                '固化劑%(樹酯)':r8,'color':color_list}
        df = pd.DataFrame(dict)
        if len(refPt)==8:
                print(df)
                #df.to_csv("D:\桌面\JA Material\JA-material\data base\\%s" %(result18),index=False, mode='a', header=False,encoding="utf_8_sig")
                df.to_csv(".data base\\%s" %(result18),index=False, mode='a', header=False,encoding="utf_8_sig")
                root2=Tk()
                root2.withdraw()
                messagebox.showinfo("純色板建立資料庫", "成功")
                                    
def color_def(rr,gg,bb):
        global color
        if abs(bb-gg)<=1 and abs(bb-rr)<=1:
            color="White"
            return(color)

        elif bb>=gg and bb>=rr:
               if bb-gg>5 and bb-rr>=5:
                   color="Blue"
                   return(color)
                
               elif bb-gg<5:
                   color="Cyan"
                   return(color)
  
               else:
                   color="Purple"
                   return(color)

        elif gg>=rr and gg>=bb:
               if gg-rr>5 or gg-bb>5:
                   color="Green"
                   return(color)

               elif gg-rr<5:
                   color="Yellow"
                   return(color)

               else:
                   color="Cyan"
                   return(color)

        elif rr>=gg and rr>=bb:
               if rr-gg>=5 and rr-bb>=5:
                   color="Red"
                   return(color)

               elif rr-gg<5:
                   color="Yellow"
                   return(color)
                
               else:
                   color="Purple"
                   return(color)

        else:
               color="White"
               return(color)

              
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
        if input == ord("c") or input == ord ("C"):
            cv2.imwrite(".test/%d.jpeg" % (index),
                        cv2.resize(frame, (800, 800), interpolation=cv2.INTER_AREA))
            print("%s: %d 張圖片" % (class_name, index))
            # bind the callback function to window
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
