# mediapipe_pose.py
import cv2
import mediapipe as mp
import time

# 1. Initialize MediaPipe Pose solution
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)

# 2. Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    starttime = time.time()
    success, frame = cap.read()
    
    if success:
        # MediaPipe requires RGB images, but OpenCV uses BGR
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # 3. Run Pose Estimation
        results = pose.process(img_rgb)
        
        # 4. Visualize the results
        if results.pose_landmarks:
            # Draw landmarks and connections (skeleton) on the frame
            mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        # 5. Display the resulting frame
        cv2.imshow("MediaPipe Pose Estimation", frame)
        
        # Exit the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        print("Failed to grab frame")
        break
    print(time.time()-starttime)
# Release resources
cap.release()
cv2.destroyAllWindows()