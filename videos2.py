import cv2 as cv

def main():
    cap = cv.VideoCapture('output.avi')

    if not cap.isOpened():
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv.imshow('window', frame)
        if cv.waitKey(1) == ord("q"):
            break
    
    cap.release()
    cv.destroyAllWindows()

main()