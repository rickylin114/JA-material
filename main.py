import keyboard  # using module keyboard
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def purecam():
    
    import JA_pureColors as pure
    pure.main()
    
def purepic():
    
    import JA_pureColors as pure
    pure.main()

def multicam():
    
    import JA_multiColors as multi
    multi.main()

def multipic():
    
    import JA_multiColors as multi
    multi.main()

def cdpcam():
    
    import CollectingData_pureColorsed as cdp
    cdp.main()

def cdppic():
    
    import CollectingData_pureColorsed as cdp
    cdp.main()

def cdmcam():
    
    import CollectingData_multiColors as cdm
    cdm.main()

def cdmpic():
    
    import CollectingData_multiColors as cdm
    cdm.main()
    
def func1():
    
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    camera=tk.Button(root, text="以照相機輸入",font=("微軟正黑體", 10),command=lambda :cdmcam()) 
    picture=tk.Button(root, text="以圖片輸入",font=("微軟正黑體", 10),command=lambda :cdmpic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)
    
def func2():
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    camera=tk.Button(root, text="以照相機輸入",font=("微軟正黑體", 10),command=lambda :cdpcam()) 
    picture=tk.Button(root, text="以圖片輸入",font=("微軟正黑體", 10),command=lambda :cdppic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)

def func3():
    
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
    
    #messagebox.showinfo("純色板比對資料庫", "請選取任意八個點")
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    camera=tk.Button(root, text="以照相機輸入",font=("微軟正黑體", 10),command=lambda :purecam()) 
    picture=tk.Button(root, text="以圖片輸入",font=("微軟正黑體", 10),command=lambda :purepic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)

    
root = tk.Tk()

'''
C = Canvas(root, bg="black", height=400, width=400)
bg = PhotoImage("D:/桌面/JA Material/JA-material/background.jpg")
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
'''
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


    
    
'''
self.left_close = QtWidgets.QPushButton("") # 關閉按鈕
self.left_visit = QtWidgets.QPushButton("") # 空白按鈕
self.left_mini = QtWidgets.QPushButton("")  # 最小化按鈕 原文網址：https://itw01.com/QND9KEG.html

self.left_label_1 = QtWidgets.QPushButton("每日推薦")
self.left_label_1.setObjectName('left_label')

def _show_value(v, *pargs):
    m=v.get()
    print(v.get())
    if m=="1":
        print('執行:建立多色資料庫')
        import CollectingData_multiColors as cdm
        cdm.main()

    if m=="2":
        print('執行:建立純色資料庫')
        import CollectingData_pureColors as cdp
        cdp.main()

    if m=="3":
        print('執行:多色板比對資料庫')
        import JA_multiColors as multi
        multi.main()

    if m=="4":
        print('執行:純色板比對資料庫')
        import JA_pureColors as pure
        pure.main()

    else:
        print('錯誤')
        
        
    

root = Tk()
root.geometry('800x800')
labelmode = tk.Label(root,
                    text = "請輸入模式代號:")
labelmode.configure(font=("微軟正黑體", 12))
labelmode.pack()

entry_var1 = StringVar()
e1 = Entry(root,textvariable=entry_var1)
e1.pack()
entry_var1.trace('w', lambda *pargs: _show_value(entry_var1, *pargs))
instruction = tk.Label(root,
                    text = "1:建立資料庫:多色取樣1000點\n\n2:建立資料庫:純色取樣100點\n\n3:多色板比對資料庫\n\n4:純色板比對資料庫")
instruction.configure(font=("微軟正黑體", 10))
instruction.pack()
root.mainloop()

def callbackFunc():
    #resultString.set("{}".format(landString.get()))
    resultString.get()
    print (resultString.get())
    if resultString.get=="1":
        print ("fuck")

def callbackFunc():
    print(resultString)
    print(resultString.set())
    
app = tk.Tk() 
app.geometry('800x800')

labelLand = tk.Label(app,
                    text = "請輸入模式代號:")
labelLand.grid(column=0, row=0, sticky=tk.W)
landString = tk.StringVar()

entryLand = tk.Entry(app, width=20, textvariable=landString)
entryLand.grid(column=1, row=0, padx=10)

resultButton = tk.Button(app, text = '執行',
                         command=callbackFunc)
resultButton.grid(column=0, row=1, pady=10, sticky=tk.W)
resultString=tk.StringVar()
resultLabel = tk.Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=1, padx=10, sticky=tk.W)

app.mainloop()

while True:
    window = tk.Tk()
    window.title('My Window')
    window.geometry('800x800')
    var=tk.StringVar()
    e1=tk.Entry(window,textvariable=var,bd=5,show=None, font=('Arial', 14))
    value=var.get()
    e1.pack()
    window.mainloop()
    try:  
        if value==1: 
            print('執行:建立多色資料庫')
            import CollectingData_multiColors as cdm
            cdm.main()
            break
        
        if keyboard.is_pressed('2'): 
            print('執行:建立純色資料庫')
            import CollectingData_pureColors as cdp
            cdp.main()
            break
        
        if keyboard.is_pressed('3'): 
            print('執行:多色板比對資料庫')
            import JA_multiColors as multi
            multi.main()
            break

        if keyboard.is_pressed('4'): 
            print('執行:純色板比對資料庫')
            import JA_pureColors as pure
            pure.main()
            break
        
        else:
            pass
    except:
        print('輸入錯誤')
        '''
