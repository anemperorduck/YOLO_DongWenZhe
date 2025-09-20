import os.path
import cv2

set_path = './datasets/set_test/images'

if __name__ == "__main__":
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("ERROR: couldn't open video!")
        exit()

    cnt_frame = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("ERROR: couldn't read frame!")
            break

        cv2.imshow('Video', frame)

        if cnt_frame % 30 == 0:
            img_path = os.path.join(set_path, f'frame{cnt_frame // 10}.jpg')
            cv2.imwrite(img_path, frame)
            print(f'{img_path}: saves successfully')

        cnt_frame += 1

        cv2.waitKey(1)
        if cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()
