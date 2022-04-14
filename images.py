import cv2 as cv

def main(imgpath: str):
    img = cv.imread(imgpath, cv.IMREAD_UNCHANGED) # Argument can also be path to local image on computer
    cv.imshow('window', img)

    key = cv.waitKey(0)
    if key == ord("q"):
        cv.destroyAllWindows()
    elif key == ord("s"):
        cv.imwrite("test_successful.jpg", img)

main('test.jpg')