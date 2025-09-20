import cv2

if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Could not open video.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("ERROR: Could not get this frame.")
            break

        cv2.imshow('test_getShape', frame)

        shape = frame.shape
        print(f"shape is {shape}")
        print("-------")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()




