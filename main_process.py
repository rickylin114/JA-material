import keyboard  # using module keyboard
import cv2
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
    from purecam import CircleCallback
    from purecam import purecam_start
    cv2.setMouseCallback("mouse_callback",CircleCallback)
    img=cv2.imread(".%s/%d.jpeg" % (class_name, index),1)
    cv2.namedWindow('mouse_callback',0)
    cv2.imshow("mouse_callback",img)
    
def purepic():
    camera.pack_forget()
    picture.pack_forget()
    manual=tk.Button(root,image=img_manual,relief='flat',command=lambda :pure_manual()) 
    auto=tk.Button(root,image=img_auto,relief='flat',command=lambda :pure_auto()) 
    manual.pack(ipadx=5, ipady=5, expand=True)
    auto.pack(ipadx=5, ipady=5, expand=True)

def multicam():
    root.destroy()
    import multicam
    from multicam import CircleCallback
    from multicam import multicam_start
    cv2.setMouseCallback("mouse_callback",CircleCallback)
    

def multipic():
    root.destroy()
    import JA_multiColors as multi
    multi.main()

def cdpcam():
    root.destroy()
    import cdpcam
    from cdpcam import CircleCallback
    from cdpcam import purecam_start
    cv2.setMouseCallback("mouse_callback",CircleCallback)

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
    Avr=tk.Button(root, image=img_avr,relief='flat',command=lambda :CDPAVR()) 
    BigData=tk.Button(root,image=img_big,relief='flat',command=lambda :CDP()) 
    Avr.pack(ipadx=5, ipady=5, expand=True)
    BigData.pack(ipadx=5, ipady=5, expand=True)


def cdmcam():
    root.destroy()
    import cdmcam
    from cdmcam import CircleCallback
    from cdmcam import multicam_start
    cv2.setMouseCallback("mouse_callback",CircleCallback)

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
    camera=tk.Button(root,image=img_camera,relief='flat',command=lambda :cdmcam()) 
    picture=tk.Button(root,image=img_import,relief='flat',command=lambda :cdmpic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)
    
def func2():
    global camera,picture
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    camera=tk.Button(root, image=img_camera,relief='flat',command=lambda :cdpcam())
    picture=tk.Button(root, image=img_import,relief='flat',command=lambda :cdppic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)

def func3():
    global camera,picture
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    camera=tk.Button(root, image=img_camera,relief='flat',command=lambda :multicam()) 
    picture=tk.Button(root,image=img_import,relief='flat',command=lambda :multipic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)

def func4():
    global camera,picture,img_camera,img_import
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    img_camera=PhotoImage(file="buttons/camera.png")
    camera=tk.Button(root,image=img_camera,relief='flat',command=lambda :purecam())
    img_import=PhotoImage(file="buttons/import.png")
    picture=tk.Button(root,image=img_import,relief='flat',command=lambda :purepic()) 
    camera.pack(ipadx=5, ipady=5, expand=True)
    picture.pack(ipadx=5, ipady=5, expand=True)

    
root = tk.Tk()
root.geometry('400x400')
root.title('玉禮配方配對app')

img_camera=PhotoImage(file="buttons/camera.png")
img_import=PhotoImage(file="buttons/import.png")
img_avr=PhotoImage(file="buttons/average.png")
img_big=PhotoImage(file="buttons/bigdata.png")
img_auto=PhotoImage(file="buttons/auto.png")
img_manual=PhotoImage(file="buttons/manual.png")

img = PhotoImage(file="buttons/QJ.png")
panel = Label(root, image = img)
panel.pack(side = "top",fill = "both")

img1 = PhotoImage(file="buttons/multibutton.png")

button1 =tk.Button(root, image=img1,text=" ",relief='flat',command=lambda :func1())


img2 = PhotoImage(file="buttons/purebutton.png") 
button2 =tk.Button(root, image=img2,text=" ",relief='flat',command=lambda :func2())


img3 = PhotoImage(file="buttons/multicompare.png") 
button3 =tk.Button(root, image=img3,text=" ",relief='flat',command=lambda :func3())


img4 = PhotoImage(file="buttons/purecompare.png") 
button4 =tk.Button(root, image=img4,text=" ",relief='flat',command=lambda :func4())

button1.pack(expand=True)
button2.pack(ipadx=3, ipady=3, expand=True)
button3.pack(ipadx=3, ipady=3, expand=True)
button4.pack(ipadx=3, ipady=3, expand=True)

root.mainloop()


 
