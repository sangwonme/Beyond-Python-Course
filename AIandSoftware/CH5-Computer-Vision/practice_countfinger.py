# finger_counting_final.py
import cv2
import mediapipe as mp

# Function to count extended fingers
def count_fingers(landmarks):
    fingers = []
    
    # 1. Thumb Logic: Compare x-coordinates (Tip vs Joint)
    # Right hand: if 4.x < 3.x, it's open (after flipping)
    if landmarks.landmark[4].x < landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # 2. Other 4 Fingers Logic: Compare y-coordinates (Tip vs PIP joint)
    tip_ids = [8, 12, 16, 20]
    for tip_id in tip_ids:
        if landmarks.landmark[tip_id].y < landmarks.landmark[tip_id - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
            
    return fingers.count(1)

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1) # Flip for mirror view
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    display_count = 0

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
            
            # 3. Call the custom function
            display_count = count_fingers(hand_lms)

    # 4. UI: Display count with large font (3x)
    cv2.putText(frame, f"Count: {display_count}", (50, 150), 
                cv2.FONT_HERSHEY_SIMPLEX, 4.5, (0, 255, 0), 10)

    cv2.imshow("Full Finger Counting", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()