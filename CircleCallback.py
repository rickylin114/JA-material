import cv2
def CircleCallback(event,x,y,flags,param):
    n=8
    global refPt,PtBGR
    if event == cv2.EVENT_LBUTTONDOWN:
            refPt.append((x, y))
            b, g, r = img[x,y]
            PtBGR.append((b,g,r)) 
            print(refPt[0:n])
            print(PtBGR[0:n])
            b=[x[0] for x in PtBGR]
            g=[x[1] for x in PtBGR]
            r=[x[2] for x in PtBGR]
            #print(r[0:n])
            cv2.circle(img,(x,y),5,(76,201,255),2)
            
img=cv2.imread('red.jpg',1)
print(img.dtype)
cv2.namedWindow('mouse_callback')
# bind the callback function to window
cv2.setMouseCallback('mouse_callback',CircleCallback)
 
