# detection_print.py
import cv2
from ultralytics import YOLO

# Load the pre-trained YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        # Run YOLOv8 on the frame
        results = model(frame, verbose=False) # verbose=False reduces terminal noise
        
        # Iterate through the results
        for r in results:
            boxes = r.boxes # Get the bounding boxes
            
            for box in boxes:
                # 1. Get Bounding Box coordinates [x1, y1, x2, y2]
                # .tolist() converts the tensor to a list of numbers
                coords = box.xyxy[0].tolist()
                x1, y1, x2, y2 = coords
                
                # 2. Get Confidence Score
                conf = box.conf[0].item()
                
                # 3. Get Class Name
                cls_id = int(box.cls[0].item())
                cls_name = model.names[cls_id]
                
                # Print the data to terminal
                print(f"Object: {cls_name} | Conf: {conf:.2f} | Box: [{int(x1)}, {int(y1)}, {int(x2)}, {int(y2)}]")
        
        # Visualize the boxes on the screen
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv8 Detection", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()