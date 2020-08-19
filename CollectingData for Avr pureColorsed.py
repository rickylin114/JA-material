import cv2
import numpy as np
import pandas as pd
import random
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

R=[]
G=[]
B=[]
A=[]
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



color='none'
#n= int(input("輸入取樣點數:"))

root = tk.Tk()
root.geometry("600x800")

def getTextInput():
    global result,result2,result3,result4,result5,result6
    global result7,result8,result9,result10,result11,result12
    global result13,result14,result15,result16,result17
    result=text.get(1.0, tk.END+"-1c")
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
    print(result)

labelmode = tk.Label(root,text = "請輸入圖片完整名稱\n ex:104432 7.jpg")
labelmode.configure(font=("微軟正黑體", 10))
labelmode.grid(row=0)
text=tk.Text(root, width=20,height=1)
text.grid(row=0,column=1)

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

btnRead.grid(row=12,column=3)

root.mainloop()


def CircleCallback(event,x,y,flags,param):
    c=0
    

    global refPt,PtBGR,w,h,Serial,r1,r2,r3,r4,rate,rate2,rate3,r6,r7,r8,r9,add,add2,add3,color,A,R,G,B
    
    if event == cv2.EVENT_LBUTTONDOWN:
        n=100
        for c in range(0,n):
            c+=1
            ranx=(random.randint(0,99))
            rany=(random.randint(0,99))
            refPt.append((ranx,rany))
            b, g, r = img[ranx,rany]
            PtBGR.append((b,g,r))
            Avr=round((int(b)+int(g)+int(r))/3)
            color_def(b,g,r,Avr)
            color_name.append(color)
            #print(PtBGR[0:n])
            b=[x[0] for x in PtBGR]
            g=[x[1] for x in PtBGR]
            r=[x[2] for x in PtBGR]
            if len(refPt)==n:
                BAvr=(round(sum(b[0:c])/c))
                GAvr=(round(sum(g[0:c])/c))
                RAvr=(round(sum(r[0:c])/c))
                A.append(Avr)
                R.append(RAvr)
                G.append(GAvr)
                B.append(BAvr)
                N=result2
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
                df = pd.DataFrame(list(zip(Serial,R,G,B,A,r1,r2,r3,locate,brand,r4,add,rate,add2,rate2,add3,rate3,r6,r7,r8,color_name))
                                  ,columns=['Serial no','R','G','B','A','40-70比例%',
                                            '70-120比例%','325比例%','砂粉產地','樹酯品牌','樹酯比例%','色粉1','色粉1比例%(樹酯)',
                                            '色粉2','色粉2比例%(樹酯)','色粉3','色粉3比例%(樹酯)',
                                            '偶聯劑%(樹酯)','促進劑%(樹酯)','固化劑%(樹酯)','顏色'])
                print(df)
                df.to_csv('D:/桌面/JA Material/JA-material/data base/PureColorAvrtest.csv',index=False, encoding="utf_8_sig")
                #df.to_csv('D:/桌面/JA Material/JA-material/data base/PureColorAvr.csv',index=False, mode='a', header=False,encoding="utf_8_sig")
                '''
                match(b,g,r,Avr)
                df = pd.DataFrame(list(zip(Serial,r,g,b)),
                                  columns=['Serial no','R','G','B']
                                  '''
                                  
def color_def(b,g,r,Avr):
        global color
        if abs(int(b)-int(g))<=1 and abs(int(b)-int(r))<=1:
              color='White'
              return color
        
        elif b>=g and b>=r:
               if b-g>5 and b-r>=5:
                      color='Blue'
                      return color
     
               elif b-g<5:
                      color='Cyan'
                      return color
    
               else:
                      color='Purple'
                      return color
   
 
        elif g>=r and g>=b:
               if g-r>5 or g-b>5:
                      color='Green'
                      return color
  
               elif g-r<5:
                      color='Yellow'
                      return color
                      
               else:
                      color='Cyan'
                      return color
  
                      
        elif r>=g and r>=b:
               if r-g>=5 and r-b>=5:
                      color='Red'
                      return color

               elif r-g<5:
                      color='Yellow'
                      return color

               else:
                      color='Purple'
                      return color
 

        else:
              color='White'
              return color


cv2.namedWindow('mouse_callback')

cv2.setMouseCallback('mouse_callback',CircleCallback)
 
def main():
    while (True):
        global img
        
        img=cv2.imread(result,1)
        h, w = img.shape[:2]
        cv2.imshow('mouse_callback',img)

        if cv2.waitKey(20) == 27:
            break
 
    cv2.destroyAllWindows()
 
 
if __name__ == "__main__":
    main()
