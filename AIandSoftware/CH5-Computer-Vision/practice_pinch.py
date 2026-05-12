import cv2
import mediapipe as mp
import math

# Function to calculate distance and check pinch status
def is_pinch(landmarks, threshold=0.1):
    # Landmark 4: Thumb Tip, Landmark 8: Index Finger Tip
    thumb_tip = landmarks.landmark[4]
    index_tip = landmarks.landmark[8]
    print(f'Thumb tip: {thumb_tip}')
    print(f'Index tip: {index_tip}')
    x1 = thumb_tip.x
    y1 = thumb_tip.y
    x2 = index_tip.x
    y2 = index_tip.y
    if((x1-x2)**2 + (y1-y2)**2)<threshold**2:
        return True
    else:
      return False # TODO: Change Return

# 1. Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# 2. Camera Setup
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    status_text = "Not-Pinch"
    text_color = (0, 0, 255) # Red

    # 3. Process Results
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
            
            # 4. Highlight Tips with Large Pink Circles
            for tip_id in [4, 8]:
                tip = hand_lms.landmark[tip_id]
                cx, cy = int(tip.x * w), int(tip.y * h)
                cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            # 5. Check for pinch gesture
            if is_pinch(hand_lms):
                status_text = "Pinch"
                text_color = (0, 255, 0) # Green

    # 6. Display status text (fontScale increased to 4.5 for 3x larger font)
    # Original was 1.5, now 4.5 for high visibility
    cv2.putText(frame, status_text, (50, 150), 
                cv2.FONT_HERSHEY_SIMPLEX, 4.5, text_color, 10)

    cv2.imshow("Pinch", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()