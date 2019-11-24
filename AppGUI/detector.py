import cv2 as cv

class testCam():
    def test(self)
        cap = cv.VideoCapture(0)
        while True:
            (grab, frame) = cap.read()
            if not grab:
                print("No image")
                break

            cv.imshow("frame", frame)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break