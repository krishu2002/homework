import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4
finger = []
while True:
    ret,img = cap.read()
    
    RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = cv2.flip(img,1)
    RGB = cv2.flip(RGB,1)
    h,w,c = img.shape
    results = hands.process(RGB)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            #accessing the landmarks by their position
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

             #Code goes here  
            for tip in finger_tips:
                x,y = int(lm_list[tip].x*w),int(lm_list[tip].y*h)
                cv2.circle(img,(x,y),15,(255,0,0),cv2.FILLED)
                if lm_list[tip].x < lm_list[tip - 3].x:
                    cv2.circle(img,(x,y),15,(0,255,0),cv2.FILLED)
                    finger.append(True)
                else:
                    finger.append(False)
                print(finger) 
                if all(finger):
                    if lm_list[4].y < lm_list[4 - 1].y < lm_list[4 - 2].y:
                        print("like")
                        cv2.putText(img,"Like",(20,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    if lm_list[4].y > lm_list[4 - 1].y > lm_list[4 - 2].y:
                        print("dislike")
                        cv2.putText(img,"Dislike",(20,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)    



            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("hand tracking", img)
    cv2.waitKey(1)