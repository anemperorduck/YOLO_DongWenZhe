import os
import shutil
import random


def split_data(labels_dir, images_dir, train_labels_dir, train_images_dir, val_labels_dir, val_images_dir,
               split_ratio=0.8):
    # 确保输出目录存在
    os.makedirs(train_labels_dir, exist_ok=True)
    os.makedirs(train_images_dir, exist_ok=True)
    os.makedirs(val_labels_dir, exist_ok=True)
    os.makedirs(val_images_dir, exist_ok=True)

    # 获取所有label文件
    label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

    # 随机打乱文件顺序
    random.shuffle(label_files)

    # 计算分割点
    split_index = int(len(label_files) * split_ratio)

    # 遍历文件，分配到train和val
    for i, label_file in enumerate(label_files):
        # 假设label文件和image文件的名字（除了扩展名）是相同的
        image_file = os.path.splitext(label_file)[0] + '.jpg'
        # 构造完整的文件路径
        label_path = os.path.join(labels_dir, label_file)
        image_path = os.path.join(images_dir, image_file)

        # 检查文件是否存在
        if os.path.exists(label_path) and os.path.exists(image_path):
            # 根据索引决定放入train还是val
            if i < split_index:
                shutil.copy2(label_path, train_labels_dir)
                shutil.copy2(image_path, train_images_dir)
            else:
                shutil.copy2(label_path, val_labels_dir)
                shutil.copy2(image_path, val_images_dir)
        else:
            print(f"Warning: {label_path} or {image_path} does not exist.")

        # 示例使用方式


labels_dir = r'G:\YOLO_KESH\my_data_set\txt'
images_dir = r'G:\YOLO_KESH\my_data_set\images'
train_labels_dir = r'G:\YOLO_KESH\datasets\coco8\niao\labels\train'
train_images_dir = r'G:\YOLO_KESH\datasets\coco8\niao\images\train'
val_labels_dir = r'G:\YOLO_KESH\datasets\coco8\niao\labels\val'
val_images_dir = r'G:\YOLO_KESH\datasets\coco8\niao\images\val'

split_data(labels_dir, images_dir, train_labels_dir, train_images_dir, val_labels_dir, val_images_dir)