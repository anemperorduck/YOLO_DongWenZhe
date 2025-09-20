import os
import random
import shutil

def decrease_sample_list(dir_path, target_dir, flag):
    """
    从指定目录中选取的 .jpg 文件，
    每flag个文件，复制一个文件到目标目录并重命名
    
    参数:
        dir_path (str): 源目录路径
        target_dir (str): 目标目录路径
        flag (int): 步长
    """

    # 获取源目录下所有 .jpg 文件
    all_files = os.listdir(dir_path)
    file_jpg_list = [f for f in all_files if f.endswith('.jpg')]
    
    # 按文件名排序确保顺序一致性
    file_jpg_list.sort()
    
    # 创建目标目录（如果不存在）
    os.makedirs(target_dir, exist_ok=True)
    
    # 初始化计数器
    count = 0
    
    # 遍历排序后的文件列表
    for i, filename in enumerate(file_jpg_list):
        # 每flag个文件处理一个
        if i % flag == 0:
            # 源文件完整路径
            src_path = os.path.join(dir_path, filename)
            # 目标文件新名称（顺序编号）
            dst_path = os.path.join(target_dir, f"{count}.jpg")
            
            # 复制文件到目标目录
            shutil.copy2(src_path, dst_path)
            count += 1


if __name__=="__main__":
    dir_path = r"D:\\A_YOLO\\datasets\\JPEGImages"
    target_dir = r"D:\A_YOLO\datasets\JPEGImages_decrease"
    flag = 4
    decrease_sample_list(dir_path, target_dir, flag)