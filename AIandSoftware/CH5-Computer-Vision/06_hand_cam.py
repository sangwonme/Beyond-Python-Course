# hand_pose.py
import cv2
import mediapipe as mp

# 1. Initialize MediaPipe Hands solution
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# max_num_hands: Maximum number of hands to detect
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

# 2. Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 3. Flip the image horizontally for a selfie-view display
    frame = cv2.flip(frame, 1)
    
    # 4. Convert BGR to RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 5. Process the frame and find hand landmarks
    results = hands.process(img_rgb)

    # 6. Visualize the results
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks and their connections
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # 7. Access specific landmark (Example: Tip of the Index Finger)
            index_finger_tip = hand_landmarks.landmark[8]
            h, w, c = frame.shape
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            
            # Draw a circle on the index finger tip
            cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    # 8. Display the output
    cv2.imshow("Hand Tracking", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()