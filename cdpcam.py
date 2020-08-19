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
color_name=[]
locate=[]
brand=[]


#n= int(input("輸入取樣點數:"))

root = tk.Tk()
root.geometry("600x800")
def quitScreen():
    messagebox.showinfo("建立純色資料庫", "點擊視窗開始建立")
    root.destroy()
    root2=Tk()
    root2.destroy()

def getTextInput():
    global result2,result3,result4,result5,result6
    global result7,result8,result9,result10,result11,result12
    global result13,result14,result15,result16,result17
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
    
'''
labelmode = tk.Label(root,text = "請輸入圖片完整名稱\n ex:104432 7.jpg")
labelmode.configure(font=("微軟正黑體", 10))
labelmode.grid(row=0)
text=tk.Text(root, width=20,height=1)
text.grid(row=0,column=1)
'''
labelmode2 = tk.Label(root,text = "請輸入編號\n ex:391532 河源7%白")
labelmode2.configure(font=("微軟正黑體", 10))
labelmode2.grid(row=1)
text2=tk.Text(root, width=20,height=1)
text2.grid(row=1,column=1)

labelmode3 = tk.Label(root,text = "色粉種類1 ex:鈦白粉")
labelmode3.configure(font=("微軟正黑體", 10))
labelmode3.grid(row=2)
text3=tk.Text(root, width=20,height=1)
text3.grid(row=2,column=1)

labelmode4 = tk.Label(root,text = "佔樹酯比例%\n ex:0")
labelmode4.configure(font=("微軟正黑體", 10))
labelmode4.grid(row=2,column=2)
text4=tk.Text(root,width=20, height=1)
text4.grid(row=2,column=3)

labelmode5 = tk.Label(root,text = "色粉種類2\n ex:鐵黑粉")
labelmode5.configure(font=("微軟正黑體", 10))
labelmode5.grid(row=3)
text5=tk.Text(root, width=20,height=1)
text5.grid(row=3,column=1)

labelmode6 = tk.Label(root,text = "佔樹酯比例%\n ex:1")
labelmode6.configure(font=("微軟正黑體", 10))
labelmode6.grid(row=3,column=2)
text6=tk.Text(root, width=20,height=1)
text6.grid(row=3,column=3)

labelmode7 = tk.Label(root,text = "色粉種類3\n ex:炭黑粉")
labelmode7.configure(font=("微軟正黑體", 10))
labelmode7.grid(row=4)
text7=tk.Text(root, width=20,height=1)
text7.grid(row=4,column=1)

labelmode8 = tk.Label(root,text = "佔樹酯比例%\n ex:2")
labelmode8.configure(font=("微軟正黑體", 10))
labelmode8.grid(row=4,column=2)
text8=tk.Text(root, width=20,height=1)
text8.grid(row=4,column=3)

labelmode9 = tk.Label(root,text = "砂粉40-70比例\n%")
labelmode9.configure(font=("微軟正黑體", 10))
labelmode9.grid(row=5)
text9=tk.Text(root, width=20,height=1)
text9.grid(row=5,column=1)

labelmode10 = tk.Label(root,text = "砂粉70-120比例%\n")
labelmode10.configure(font=("微軟正黑體", 10))
labelmode10.grid(row=5,column=2)
text10=tk.Text(root, width=20,height=1)
text10.grid(row=5,column=3)

labelmode11 = tk.Label(root,text = "砂粉325比例%\n")
labelmode11.configure(font=("微軟正黑體", 10))
labelmode11.grid(row=6)
text11=tk.Text(root, width=20,height=1)
text11.grid(row=6,column=1)

labelmode12 = tk.Label(root,text = "砂粉產地\n ex:河源")
labelmode12.configure(font=("微軟正黑體", 10))
labelmode12.grid(row=6,column=2)
text12=tk.Text(root, width=20,height=1)
text12.grid(row=6,column=3)

labelmode13 = tk.Label(root,text = "樹酯品牌\n")
labelmode13.configure(font=("微軟正黑體", 10))
labelmode13.grid(row=7)
text13=tk.Text(root, width=20,height=1)
text13.grid(row=7,column=1)

labelmode14 = tk.Label(root,text = "樹酯比例\n")
labelmode14.configure(font=("微軟正黑體", 10))
labelmode14.grid(row=7,column=2)
text14=tk.Text(root, width=20,height=1)
text14.grid(row=7,column=3)

labelmode15 = tk.Label(root,text = "偶聯劑%(樹酯)\n")
labelmode15.configure(font=("微軟正黑體", 10))
labelmode15.grid(row=8)
text15=tk.Text(root, width=20,height=1)
text15.grid(row=8,column=1)

labelmode16 = tk.Label(root,text = "促進劑%(樹酯)\n")
labelmode16.configure(font=("微軟正黑體", 10))
labelmode16.grid(row=8,column=2)
text16=tk.Text(root, width=20,height=1)
text16.grid(row=8,column=3)

labelmode17 = tk.Label(root,text = "固化劑%(樹酯)\n")
labelmode17.configure(font=("微軟正黑體", 10))
labelmode17.grid(row=9)
text17=tk.Text(root, width=20,height=1)
text17.grid(row=9,column=1)



btnRead=tk.Button(root, height=1, width=10, text="確定", 
                    command=getTextInput)

btnRead.grid(row=12,column=2)

btnRead=tk.Button(root, height=1, width=10, text="開始", 
                    command=quitScreen)

btnRead.grid(row=12,column=3)

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
    global refPt,PtBGR,w,h,Serial,r1,r2,r3,r4,rate,rate2,rate3,r6,r7,r8,r9,add,add2,add3,color,b,g,r
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
        dict = {'Serial no': Serial, 'R': r, 'G':g,'B':b,'40-70比例%':r1,'70-120比例%':r2,'325比例%':r3,'砂粉產地':locate,'樹酯品牌':brand,'樹酯比例%':r4[0],
                '色粉1':add,'色粉1比例%(樹酯)':rate,'色粉2':add2,'色粉2比例%(樹酯)':rate2,'色粉3':add3,'色粉3比例%(樹酯)':rate3,'偶聯劑%(樹酯)':r6,'促進劑%(樹酯)':r7,
                '固化劑%(樹酯)':r8}
        df = pd.DataFrame(dict)
        if len(refPt)==8:
                print(df)
                df.to_csv('D:/桌面/JA Material/JA-material/data base/PureColorcam.csv',index=False,header=False,encoding="utf_8_sig")
                #df.to_csv('D:/桌面/JA Material/JA-material/data base/PureColorBig.csv',index=False, mode='a', header=False,encoding="utf_8_sig")  
                root2=Tk()
                root2.withdraw()
                messagebox.showinfo("純色板建立資料庫", "成功")
                                    
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
