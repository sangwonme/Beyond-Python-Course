# pose_image.py
import cv2
import mediapipe as mp

# 1. Initialize MediaPipe Pose solution for static images
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

# Use static_image_mode=True for better accuracy on single images
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

# 2. Load an image from file
image_path = 'person.jpg'  # Replace with your image file name
image = cv2.imread(image_path)

if image is not None:
    # 3. Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 4. Process the image and find pose landmarks
    results = pose.process(image_rgb)
    
    # 5. Draw the pose landmarks on the image
    if results.pose_landmarks:
        print("Pose detected successfully!")
        mp_draw.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        print(results.pose_landmarks.landmark[25])
        print(results.pose_landmarks.landmark[25].x)
        # 6. Display the output image
        cv2.imshow("Pose Estimation on Image", image)
        cv2.waitKey(0) # Wait until a key is pressed
    else:
        print("No pose detected in the image.")
else:
    print("Could not read the image. Check the file path.")

# Release resources
cv2.destroyAllWindows()
pose.close()