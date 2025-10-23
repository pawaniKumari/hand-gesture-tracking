#Moves the mouse using the index finger (ID = 8).
#Simulates a mouse click when the thumb (ID = 4) is close to the index finger.
#Displays real-time hand tracking using MediaPipe.
#Uses OpenCV to capture video and display landmarks.

import cv2
import mediapipe
import pyautogui
import time

#initialize mediapipe and get screen size
capture_hands = mediapipe.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
drawing_option = mediapipe.solutions.drawing_utils

#get screen size
screen_width, screen_height = pyautogui.size()

#connect the camera
camera = cv2.VideoCapture(0) # 0-primary webcam

# Check if camera is opened successfully
if not camera.isOpened():
    print("Error: Could not open camera. Please check if your camera is connected and not being used by another application.")
    exit()

x1 = y1 = x2 = y2 = 0 #variables for tracking finger positions

#image capture
try:
  while True:
    ret, image = camera.read()
    
    # Check if frame was captured successfully
    if not ret or image is None:
        print("Error: Failed to capture frame from camera")
        break
        
    image_height, image_width, _ = image.shape

    #flip the image horizontal & convert colors
    image = cv2.flip(image,1)
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    #process hand tracking
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks #detect finger positions

    #draw hand landmarks & get co-ordinates
    if all_hands:
      for hand in all_hands:
        drawing_option.draw_landmarks(image,hand)
        one_hand_landmarks = hand.landmark

        #get specific finger positions
        for id, lm in enumerate(one_hand_landmarks):
          x = int(lm.x * image_width) #convert relative coordinates to pixel values
          y = int(lm.y * image_height)
          #print(x,y) 

          #move cursor with index finger
          if id == 8:
            mouse_x = int(screen_width / image_width * x)
            mouse_y = int(screen_height / image_height * y)
            cv2.circle(image,(x,y),10,(0,255,255)) #draw yellow circles on the finger tip
            pyautogui.moveTo(mouse_x,mouse_y)
            x1 = x
            y1 = y

          #detect thumb finger
          if id == 4:
            x2 = x
            y2 = y
            cv2.circle(image,(x,y),10,(0,255,255))
          
      #click when the fingers are close
      dist = y2 - y1
      print(dist)
      if(dist<40):
        pyautogui.click()
        print("clicked")

    #display the video feed
    cv2.imshow('Hand movement video capture', image)
    key = cv2.waitKey(100)
    if key == 27: #to exit key code is 27
      break

except KeyboardInterrupt:
    print("\nProgram interrupted by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    #release camera and close window
    camera.release()
    cv2.destroyAllWindows()
    print("Camera released and windows closed")