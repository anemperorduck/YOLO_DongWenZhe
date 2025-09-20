from ultralytics import YOLO

if __name__=='__main__':
    model = YOLO("yolo11n.pt")

    results = model.train(data=r"D:\A_YOLO\datasets\ZhinengZhongduan\ZhinengZhongduan.yaml", 
                          cache=False,
                          imgsz=640,
                          epochs=50,
                          batch=8,
                          device='0')