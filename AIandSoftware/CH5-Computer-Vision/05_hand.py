# hand_image.py
import cv2
import mediapipe as mp

# 1. Initialize MediaPipe Hands for static images
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Use static_image_mode=True for processing single images
hands = mp_hands.Hands(
    static_image_mode=True, 
    max_num_hands=2, 
    min_detection_confidence=0.5
)

# 2. Load an image from file
image_path = 'hand.jpg'  # Replace with your image file path
image = cv2.imread(image_path)

if image is not None:
    # 3. Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 4. Process the image
    results = hands.process(image_rgb)
    
    # 5. Check if hands are detected and visualize
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw all landmarks and connections
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Print the coordinate of the thumb tip (Landmark 4)
            h, w, c = image.shape
            thumb_tip = hand_landmarks.landmark[4]
            cx, cy = int(thumb_tip.x * w), int(thumb_tip.y * h)
            print(f"Thumb Tip Position: ({cx}, {cy})")

        # 6. Show the result
        cv2.imshow("Hand Pose on Image", image)
        cv2.waitKey(0)
    else:
        print("No hands detected.")
else:
    print("Image not found.")

# Release resources
hands.close()
cv2.destroyAllWindows()