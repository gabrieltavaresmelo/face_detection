import cv2

print(cv2.__version__)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

img = cv2.imread('sample.jpg')
result = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

for (x,y,w,h) in faces: 
    cv2.rectangle(result,(x,y),(x+w,y+h),(255,255,0),2)  

cv2.imshow('original', img) 
cv2.imshow('result', result) 
cv2.imwrite('sample-result.jpg', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
