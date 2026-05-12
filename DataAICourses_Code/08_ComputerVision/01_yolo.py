# main.py
from ultralytics import YOLO
import cv2

# 1. Load a pre-trained YOLO model (n: nano - fastest and lightest)
model = YOLO('yolov8n.pt')

# 2. Run inference on an image
# 'source' can be a file path, URL, or even a numpy array
results = model('bus.jpg')

# 3. Process results
for r in results:
    # Plot the detection results on the image
    annotated_frame = r.plot()
    
    # Display the result
    cv2.imshow("YOLOv8 Detection", annotated_frame)
    cv2.waitKey(0)

cv2.destroyAllWindows()