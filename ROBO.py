from ultralytics import YOLO
import cv2
import torch
import serial

torch.set_num_threads(4)
# print(f"PyTorch threads: {torch.get_num_threads()}")

# SERIAL_PORT = '/dev/ttyS0'
# BAUD_RATE = 115200
# ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

TARGET_OBJ_BALL = "Ball_blue"
TARGET_OBJ_GOAL = "frame_red"
MEDIAN = 100  # 整除、取余
serial_send_info = [0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0]


def get_coord(coord_left, coord_right):
    coord = int(coord_left + (coord_right - coord_left) / 2)
    coord_divide = coord // MEDIAN
    coord_reminder = coord % MEDIAN
    return coord_divide, coord_reminder, coord


if __name__ == "__main__":

    model = YOLO("Best_best.pt")
    model.to("cpu")

    cap = cv2.VideoCapture(0)
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
        # print(serial_send_info)

        for box in res.boxes:
            cls_index = box.cls.cpu().detach().numpy()[0]
            label = dic[int(cls_index)]
            # print(label)
            xyxy = box.xyxy.cpu().detach().numpy().astype(int)[0]
            x1, y1, x2, y2 = xyxy[0], xyxy[1], xyxy[2], xyxy[3]

            # 标签是否是目标地点
            if label == TARGET_OBJ_GOAL:
                serial_send_info[5] = 1
                target_goal_x_divide, target_goal_x_reminder, target_goal_x_coord = get_coord(x1, x2)
                target_goal_y_divide, target_goal_y_reminder, target_goal_y_coord = get_coord(y1, y2)

                serial_send_info[6] = target_goal_x_divide
                serial_send_info[7] = target_goal_x_reminder
                serial_send_info[8] = target_goal_y_divide
                serial_send_info[9] = target_goal_y_reminder

                # print(f"label -> {label}")
                # print(f"target_goal_x_divide -> {target_goal_x_divide} ,"
                #       f"target_goal_x_reminder -> {target_goal_x_reminder} ,"
                #       f"target_goal_x_coord -> {target_goal_x_coord}")
                # print(f"target_goal_y_divide -> {target_goal_y_divide}, "
                #       f"target_goal_y_reminder -> {target_goal_y_reminder}, "
                #       f"target_goal_y_coord -> {target_goal_y_coord}")

            # 标签是否是目标球
            if label == TARGET_OBJ_BALL:
                serial_send_info[0] = 1
                target_ball_x_divide, target_ball_x_reminder, target_ball_x_coord = get_coord(x1, x2)
                target_ball_y_divide, target_ball_y_reminder, target_ball_y_coord = get_coord(y1, y2)

                serial_send_info[1] = target_ball_x_divide
                serial_send_info[2] = target_ball_x_reminder
                serial_send_info[3] = target_ball_y_divide
                serial_send_info[4] = target_ball_x_reminder

                # print(f"label -> {label}")
                # print(f"target_ball_x_divide -> {target_ball_x_divide}, "
                #       f"target_ball_x_reminder -> {target_ball_x_reminder}, "
                #       f"target_ball_x_coord -> {target_ball_x_coord}")
                # print(f"target_ball_y_divide -> {target_ball_y_divide}, "
                #       f"target_ball_y_reminder -> {target_ball_y_reminder}, "
                #       f"target_ball_y_coord -> {target_ball_y_coord}")

            print(f"serial_send_info -> {serial_send_info}")
            # for info in serial_send_info:
            #     ser.write(info)

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv2.imshow('test', img)

        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # if cv2.getWindowProperty('test', cv2.WND_PROP_VISIBLE) < 1:
            # break

    cap.release()
    cv2.destroyAllWindows()

# ser.close()
