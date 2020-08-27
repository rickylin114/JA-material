import keyboard  # using module keyboard
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def pure_manual():
    root.destroy()
    import JA_pureColors as pure
    pure.main()

def pure_auto():
    root.destroy()
    import JA_pureColors_Auto as auto
    auto.main()

def purecam():
    root.destroy()
    import purecam
    
def purepic():
    camera.pack_forget()
    picture.pack_forget()
    manual=tk.Button(root, text="手動選取點",font=("微軟正黑體", 10),command=lambda :pure_manual()) 
    auto=tk.Button(root, text="自動選取點",font=("微軟正黑體", 10),command=lambda :pure_auto()) 
    manual.pack(ipadx=5, ipady=5, expand=True)
    auto.pack(ipadx=5, ipady=5, expand=True)

def multicam():
    root.destroy()
    import multicam

def multipic():
    root.destroy()
    import JA_multiColors as multi
    multi.main()

def cdpcam():
    root.destroy()
    import cdpcam

def CDP():
    root.destroy()
    import CollectingData_pureColorsed as cdp
    cdp.main()
    
def CDPAVR():
    root.destroy()
    import cdp_avr
    cdp_avr.main()
    
def cdppic():
    camera.pack_forget()
    picture.pack_forget()
    Avr=tk.Button(root, text="平均小數據",font=("微軟正黑體", 10),command=lambda :CDPAVR()) 
    BigData=tk.Button(root, text="一般大數據",font=("微軟正黑體", 10),command=lambda :CDP()) 
    Avr.pack(ipadx=5, ipady=5, expand=True)
    BigData.pack(ipadx=5, ipady=5, expand=True)


def cdmcam():
    root.destroy()
    import cdmcam

def cdmpic():
    root.destroy()
    import CollectingData_multiColors as cdm
    cdm.main()
    
def func1():
    global camera,picture
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    camera=tk.Button(root, text="以照相機輸入",font=("微軟正黑體", 10),command=lambda :cdmcam()) 
    picture=tk.Button(root, text="以圖片輸入",font=("微軟正黑體", 10),command=lambda :cdmpic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)
    
def func2():
    global camera,picture
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    camera=tk.Button(root, text="以照相機輸入",font=("微軟正黑體", 10),command=lambda :cdpcam()) 
    picture=tk.Button(root, text="以圖片輸入",font=("微軟正黑體", 10),command=lambda :cdppic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)

def func3():
    global camera,picture
    #messagebox.showinfo("多色板比對資料庫", "點擊視窗開始比對")
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    camera=tk.Button(root, text="以照相機輸入",font=("微軟正黑體", 10),command=lambda :multicam()) 
    picture=tk.Button(root, text="以圖片輸入",font=("微軟正黑體", 10),command=lambda :multipic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)

def func4():
    global camera,picture
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    camera=tk.Button(root, text="以照相機輸入",font=("微軟正黑體", 10),command=lambda :purecam()) 
    picture=tk.Button(root, text="以圖片輸入",font=("微軟正黑體", 10),command=lambda :purepic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)

    
root = tk.Tk()
root.geometry('400x400')
root.title('玉禮配方配對app')
button1=tk.Button(root, text="建立多色資料庫",font=("微軟正黑體", 10),command=lambda :func1()) 
button2=tk.Button(root, text="建立純色資料庫",font=("微軟正黑體", 10),command=lambda :func2()) 
button3=tk.Button(root, text="多色板比對資料庫",font=("微軟正黑體", 10),command=lambda :func3())
button4=tk.Button(root, text="純色板比對資料庫",font=("微軟正黑體", 10),command=lambda :func4()) 
button1.pack(ipadx=5, ipady=5, expand=True)
button2.pack(ipadx=5, ipady=5, expand=True)
button3.pack(ipadx=5, ipady=5, expand=True)
button4.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()


 
