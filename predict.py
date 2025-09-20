from ultralytics import YOLO
import cv2
import os
import random

model = YOLO(r"runs\\detect\\train4\\weights\\best.pt")
modelNames = ['tudou','xilanhua','jidan','xianggu','doufu','zhurou','xihongshi','niurou','qingjiao','qincai','qingcai','doujiao']

cnt = 3
images_dir_path = r"D:\\A_YOLO\\temp_trainImage"
all_files = os.listdir(images_dir_path)
jpg_files_list = [f for f in all_files if f.endswith('.jpg')]
select_files = random.sample(jpg_files_list, cnt)

for select_file in select_files:
    image_path = os.path.join(images_dir_path, select_file)
    print(image_path)
    image = cv2.imread(image_path)

    results = model(image)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
            label = f'{modelNames[cls]}: {conf:.2f}'
            cv2.putText(image, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)


    cv2.imshow('test', image)
    cv2.waitKey(0)