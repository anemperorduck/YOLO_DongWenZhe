import cv2
from ultralytics import YOLO

if __name__ == '__main__':
    # Load the YOLO model
    model = YOLO("yolo11n.pt")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Could not open video.")
        exit()

    while True:
        success, frame = cap.read()
        if success:
            # Run YOLO inference on the frame
            results = model(frame)
            # Visualize the results on the frame
            annotated_frame = results[0].plot()
            cv2.imshow("Inference", annotated_frame)

            cv2.waitKey(1)
            if cv2.getWindowProperty('test', cv2.WND_PROP_VISIBLE) < 1:
                break
        else:
            print("ERROR: Could not get this frame")
            break

    cap.release()
    cv2.destroyAllWindows()
