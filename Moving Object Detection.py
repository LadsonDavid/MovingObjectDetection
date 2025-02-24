import cv2
import imutils
cam=cv2.VideoCapture(0)
firstframe=None
area=400
while True:
    text="Normal"
    _,img=cam.read()
    img=imutils.resize(img,height=300,width=300)
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(grey,(21,21),0)
    if firstframe is None:
        firstframe=blur
        continue
    diff=cv2.absdiff(firstframe,blur)
    thresh=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)[1]
    thresh=cv2.dilate(thresh,None,iterations=2)
    cont=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cont=imutils.grab_contours(cont)
    for c in cont:
        if cv2.contourArea(c)<area:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(77,187,250),2)
        text="Moving object detected"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(77,187,250),2)
    cv2.imshow("Video",img)
    key=cv2.waitKey(1)
    if key==113:
        break
cam.release()
cv2.destroyAllWindows()
