import cv2 as cv
import time

def main():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'DIVX')
    outfile = cv.VideoWriter('output.avi', fourcc, 10.0, (640, 480))

    if not cap.isOpened():
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if cv.waitKey(1) == ord('s'):
            while True:
                if cv.waitKey(1) == ord('s'):
                    break

                ret, frame = cap.read()
                outfile.write(frame)
                cv.imshow('window', frame)

        cv.imshow('window', frame)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    outfile.release()
    cv.destroyAllWindows()

main()
