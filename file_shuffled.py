import os
import random
import shutil

def generate_shuffled_list(dir_path, target_dir, cunt=80):
    """
    从指定目录中随机选取指定数量的 .jpg 文件，复制到目标目录并重命名
    
    参数:
        dir_path (str): 源目录路径
        target_dir (str): 目标目录路径
        cunt (int): 要选取的文件数量
    """
    # 获取源目录下所有 .jpg 文件
    all_files = os.listdir(dir_path)
    file_jpg_list = [f for f in all_files if f.endswith('.jpg')]

    # 检查数量是否超出实际文件数
    if cunt > len(file_jpg_list):
        cunt = len(file_jpg_list)

    # 随机选取指定数量的文件
    selected_files = random.sample(file_jpg_list, cunt)

    # 创建目标目录（若不存在）
    os.makedirs(target_dir, exist_ok=True)

    # 复制并重命名文件
    for i, filename in enumerate(selected_files, start=1):
        src_path = os.path.join(dir_path, filename)
        new_name = f"{i:04d}.jpg"
        dst_path = os.path.join(target_dir, new_name)
        shutil.copy(src_path, dst_path)

if __name__ == "__main__":
    dir_path = r'D://A_YOLO//temp_trainImage'
    target_dir = r'D://A_YOLO//temp_trainImage//tempImage'
    generate_shuffled_list(dir_path, target_dir)