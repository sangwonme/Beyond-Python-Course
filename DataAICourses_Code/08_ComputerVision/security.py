import cv2
import os
import time
from ultralytics import YOLO

# 1. Initialize YOLOv8 model and create storage directory
model = YOLO('yolov8n.pt')
save_dir = "security_captures"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    print(f"📁 Created directory: {save_dir}")

# 2. Setup Webcam and timing variables
cap = cv2.VideoCapture(0)
last_saved_time = 0
cooldown_seconds = 3  # Time to wait between saves to avoid duplicate spam

print("🚀 Security System Active. Press 'q' to stop.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("❌ Failed to grab frame.")
        break

    # Run YOLOv8 detection (stream=True is more memory efficient)
    results = model(frame, verbose=False)
    
    current_time = time.time()

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Get class ID and confidence
            cls_id = int(box.cls[0].item())
            cls_name = model.names[cls_id]
            conf = box.conf[0].item()

            # Target only 'person' with confidence > 50%
            if cls_name == 'person' and conf > 0.5:
                
                # Check if the cooldown period has passed
                if current_time - last_saved_time > cooldown_seconds:
                    
                    # 3. Get Bounding Box Coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

                    # 4. Crop the person from the frame (Array Slicing)
                    # Use max/min to ensure coordinates are within image boundaries
                    h, w, _ = frame.shape
                    crop_img = frame[max(0, y1):min(h, y2), max(0, x1):min(w, x2)]

                    if crop_img.size > 0:
                        timestamp = time.strftime("%Y%m%d-%H%M%S")
                        filename = f"{save_dir}/intruder_{timestamp}.jpg"
                        
                        # Save the cropped image
                        cv2.imwrite(filename, crop_img)
                        print(f"📸 Alert! Person detected. Cropped image saved: {filename}")
                        
                        last_saved_time = current_time

    # 5. Display the real-time feed with annotations
    annotated_frame = results[0].plot()
    cv2.imshow("AI Security Monitor", annotated_frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("🛑 System Shutdown.")