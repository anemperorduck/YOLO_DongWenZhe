from ultralytics import YOLO
import cv2
import serial

# SERIAL_PORT = '/dev/ttyS0'
# BAUD_RATE = 115200
# ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)


def get_coord(coord_left, coord_right) -> int:
    coord = int(coord_left + (coord_right - coord_left) / 2)
    return coord


if __name__ == "__main__":

    model = YOLO("best.pt")

    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("ERROR: Could not open video.")
        exit()

    while True:
        ret, img = cap.read()
        if not ret:
            print("ERROR: Could not get this frame")
            break

        res = model(img)[0]
        dic = res.names

        for box in res.boxes:
            cls_index = box.cls.cpu().detach().numpy()[0]
            label = dic[int(cls_index)]
            print(label)

            xyxy = box.xyxy.cpu().detach().numpy().astype(int)[0]
            x1, y1, x2, y2 = xyxy[0], xyxy[1], xyxy[2], xyxy[3]

            goal_ball_x_coord = float(get_coord(x1, x2))
            goal_ball_y_coord = float(get_coord(y1, y2))

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv2.imshow('test', img)

        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.getWindowProperty('test', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()


# ser.close()

