import cv2 as cv
import time

def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv.imshow('window', frame)
        if cv.waitKey(1) == ord("q"):
            break
        elif cv.waitKey(1) == ord("s"):
            cv.imwrite(f'Capture screenshot at {time.time()}.jpg', frame)

    cap.release()
    cv.destroyAllWindows()

main()
