import cv2
import os
from ultralytics import YOLO

# -----------------------------
# Load model
# -----------------------------
model = YOLO("yolov8n.pt")

# -----------------------------
# Load image
# -----------------------------
image_path = "IMG_4532.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found.")
    exit()

# -----------------------------
# Run detection
# -----------------------------
results = model(image)
result = results[0]

print("\n===== DETECTIONS =====")

boxes = result.boxes

if boxes is not None and len(boxes) > 0:
    for i, box in enumerate(boxes):

        # Bounding box coordinates
        x1, y1, x2, y2 = box.xyxy[0].tolist()

        # Confidence
        conf = float(box.conf[0])

        # Class ID and name
        cls_id = int(box.cls[0])
        class_name = result.names[cls_id]

        # Structured dictionary
        detection_data = {
            "id": i,
            "class_id": cls_id,
            "class_name": class_name,
            "confidence": conf,
            "bbox_xyxy": [x1, y1, x2, y2],
            "center": [(x1 + x2) / 2, (y1 + y2) / 2],
            "width": x2 - x1,
            "height": y2 - y1
        }

        print(detection_data)

        # -----------------------------
        # Draw bounding box manually
        # -----------------------------
        cv2.rectangle(
            image,
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            f"{class_name} {conf:.2f}",
            (int(x1), int(y1) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

else:
    print("No objects detected.")

# -----------------------------
# Save annotated image
# -----------------------------
output_folder = "annotated_results"
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(output_folder, "annotated_" + os.path.basename(image_path))
cv2.imwrite(output_path, image)

print(f"\nAnnotated image saved at: {output_path}")

# -----------------------------
# Show image
# -----------------------------
cv2.imshow("YOLO Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
