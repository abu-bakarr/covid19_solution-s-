import cv2
img = "pic.jpg"
cascade_src= "data\haarcascades\haarcascade_frontalface_default.xml"
   
face_cascade = cv2.CascadeClassifier(cascade_src)
    
img = cv2.imread(img,1)
# img = cv2.resize(img,(16*100,9*100))
    
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
print (len(faces))
print(faces)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255), 2)  
    
resizeImg = (img, (400,200))
cv2.imshow('rectangled', img)
cv2.waitKey(0) 
