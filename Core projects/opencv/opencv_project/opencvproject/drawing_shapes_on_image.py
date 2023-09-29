import  cv2
image=cv2.imread('lena.jpg',1)
# cv2.line(image,(0,0),(400,400),(255,0,0),10) #Blue cross line
cv2.rectangle(image,(150,150),(350,350),(100,100,100),-1) #Green renclangle
cv2.rectangle(image,(150,150),(350,350),(200,200,200),80)
cv2.rectangle(image,(150,150),(350,350),(000,200,200),60)
cv2.rectangle(image,(150,150),(350,350),(000,200,000),50)
cv2.rectangle(image,(150,150),(350,350),(000,000,200),45)
cv2.rectangle(image,(150,150),(350,350),(000,100,200),30)
cv2.rectangle(image,(150,150),(350,350),(000,000,000),15)
cv2.circle(image,(100,100),100,(277,85,255),-1)
cv2.circle(image,(400,100),100,(247,240,0),-1)
cv2.circle(image,(100,400),100,(185,188,250),-1)
cv2.circle(image,(400,400),100,(251,144,68),-1)
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(image,"Happy b'dAy",(200,250),font,0.6,(100,255,100))
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()