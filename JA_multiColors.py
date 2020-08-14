import cv2
import numpy as np
import pandas as pd
import random

df= pd.read_csv("D:/桌面/JA Material/JA-material/data base/MQdata.csv")
refPt = []
PtBGR=[]
#n= int(input("輸入取樣點數:"))


def CircleCallback(event,x,y,flags,param):
    c=0
    global refPt,PtBGR,w,h,Serial
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
                #print(refPt[0:c])
                df_test = pd.DataFrame(list(zip(r,g,b)),columns=['R','G','B'])
                loan=pd.merge(df_test,df)
                #print (loan)
                dups_loan = loan.pivot_table(index=['Serial no'],aggfunc='size')
                Newdf=dups_loan.sort_values(ascending=False)
                BAvr=(round(sum(b[0:c])/c))
                GAvr=(round(sum(g[0:c])/c))
                RAvr=(round(sum(r[0:c])/c))
                #print((RAvr,GAvr,BAvr))
                Avr=round((BAvr+GAvr+RAvr)/3)
                if len(Newdf):
                    print (Newdf.head(3))
                else:
                    print("找不到匹配型號，或拍攝環境不佳，曝光、白平衡錯誤")

#cv2.namedWindow('image')
#cv2.setMouseCallback('image', average_bgr)
            
img=cv2.imread('MQ217.jpg',1)
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
