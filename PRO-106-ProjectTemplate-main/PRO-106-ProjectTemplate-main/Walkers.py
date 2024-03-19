import cv2


# Create our body classifier
classifier = cv2.CascadeClassifier("C:/Users/lenovo/Downloads/PRO-106-ProjectTemplate-main/PRO-106-ProjectTemplate-main/haarcascade_fullbody.xml")

# Initiate video capture for video file
cap = cv2.VideoCapture('C:/Users/lenovo/Downloads/PRO-106-ProjectTemplate-main/PRO-106-ProjectTemplate-main/walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    
    # Pass frame to our body classifier
    body = classifier.detectMultiScale(gray,1.2,3)
    
    # Extract bounding boxes for any bodies identified
    print(len(body))

    for (x,y,w,h) in body:
       
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)  

        
        roi_color = frame[y:y+h, x:x+w] 
        
              
    cv2.imshow('img',frame)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
