import os
import cv2
import json
import numpy as np

def get_code(name) -> int:
    if name == "xiaolian":
        return 0
    if name == "fasixin":
        return 1
    if name == "yonghu":
        return 2
    if name == "sosuo":
        return 3
    if name =="sixin":
        return 4
    if name =="shiping":
        return 5
    if name =="paizhao":
        return 6
    if name =="fanhui":
        return 7
def json2txt(file_path, file_name, out_path, img_path):

    with open(os.path.join(file_path, file_name), "r", encoding='utf-8') as f:
        str = ""
        # 整个JSON文件内容读取到str中
        for i in f.readlines():
            str += i
        # 将这个符合JSON格式的str解析为相应的Python数据结构
        js = json.loads(str)

        # 读取对应的图片以获取其尺寸
        image_file = os.path.join(img_path, file_name.split(".")[0] + ".jpg")  # 假设图片格式为jpg
        if not os.path.exists(image_file):
            print("failed to get the image in jpg formal!!!")
            image_file = os.path.join(img_path, file_name.split(".")[0] + ".png")  # 如果jpg不存在，尝试png
        print("successfully get the image!!!")
        image = cv2.imread(image_file)
        size_y, size_x = image.shape[:2]

        with open(os.path.join(out_path, file_name.split(".")[0] + ".txt"), "w") as f:
            for i in js["labels"]:
                l = get_code(i["name"])
                w = (i["x2"] - i["x1"]) / size_x
                x = (i["x2"] + i["x1"]) / 2 / size_x
                h = (i["y2"] - i["y1"]) / size_y
                y = (i["y2"] + i["y1"]) / 2 / size_y
                print(file_name.split(".")[0])
                print("%d %.08f %.08f %.08f %.08f\n" % (l, x, y, w, h))
                f.write("%d %.06f %.06f %.06f %.06f\n" % (l, x, y, w, h))

if __name__ == "__main__":
    file_path = "json\\"
    out_path = "txt\\"
    img_path = "images\\"  # 图片所在路径
    for i in os.listdir(file_path):
        json2txt(file_path=file_path, file_name=i, out_path=out_path, img_path=img_path)
