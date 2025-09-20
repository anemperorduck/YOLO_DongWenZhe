from ultralytics import YOLO
import cv2
import serial

# SERIAL_PORT = '/dev/ttyS0'
# BAUD_RATE = 115200
# ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

TARGET_OBJ = "fork"


# 获取中心位置坐标
def get_coord(coord_left, coord_right) -> int:
    coord = int(coord_left + (coord_right - coord_left) / 2)
    return coord


if __name__ == '__main__':
    model = YOLO("yolo11n.pt")

    img1 = cv2.imread(r"test_images/000000000009.jpg")
    img2 = cv2.imread(r"test_images/000000000025.jpg")

    res1 = model(img1)[0]
    res2 = model(img2)[0]

    dic1 = res1.names
    dic2 = res2.names
    # print(f"dic1 is {dic1}")
    # print(f"dic2 is {dic2}")

    for box in res1.boxes:
        cls_index = box.cls.cpu().detach().numpy()[0]
        label = dic1[int(cls_index)]
        print(label)

        if label == TARGET_OBJ:
            xyxy = box.xyxy.cpu().detach().numpy().astype(int)[0]
            print(f"xyxy of {TARGET_OBJ} is {xyxy}")
            x1, y1, x2, y2 = xyxy[0], xyxy[1], xyxy[2], xyxy[3]

            # 整数形式
            goal_coord_x = get_coord(x1, x2)
            goal_coord_y = get_coord(y1, y2)
            print(f"the central coord of target object {TARGET_OBJ} is [ {goal_coord_x} , {goal_coord_y} ]")

            break

    print("end of program")
