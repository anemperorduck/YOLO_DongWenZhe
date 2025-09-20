from ultralytics import YOLO
import cv2

def yolo_predict():
    # Load a pre-trained YOLO model (you can choose n, s, m, l, or x versions)
    model = YOLO(r"yolo11n.pt")

    img = cv2.imread(r'test_images/000000000025.jpg')

    res = model(img)[0]
    print(res)
    print("----------------------------------")
    dic = res.names
    print(dic)
    print("----------------------------------")
    # 遍历检测到的框
    for box in res.boxes:
        print(box.cls, box.conf, box.xyxy)
        print("----------------------------------")

        # 打印类别名称
        cls_index = box.cls.cpu().detach().numpy()[0]  # 取出类别索引
        print(dic[int(cls_index)])  # 转换为整数并打印类别名称
        print("----------------------------------")

        # 获取图像的高度和宽度
        h, w, _ = img.shape

        # 获取框的坐标并转换为整数
        xyxy = box.xyxy.cpu().detach().numpy().astype(int)[0]
        x1, y1, x2, y2 = xyxy[0], xyxy[1], xyxy[2], xyxy[3]

        # 在图像上绘制矩形框
        cv2.rectangle(img, (x1,y1), (x2, y2), (255, 0, 0), 2)  # 设置线宽为2
    print(res.boxes)
    res.show()
    cv2.imshow('text', img)
    cv2.waitKey(0)
    cv2.destroyWindow()


if __name__ == "__main__":
    model = YOLO(r"yolo11n.pt")
    img = cv2.imread(r"test_images/000000000025.jpg")
    results = model(img)
    for res in results:
        box = res.boxes
        xyxy = box.xyxy.cpu().detach().numpy().astype(float)
        print(f"xyxy is {xyxy}")

        xywh = box.xywh.cpu().detach().numpy().astype(float)
        print(f"xywh is {xywh}")

        xyxyn = box.xyxyn.cpu().detach().numpy().astype(float)
        print(f"xyxyn is {xyxyn}")

        xywhn = box.xywhn.cpu().detach().numpy().astype(float)
        print(f"xywhn is {xywhn}")

    res.show()















