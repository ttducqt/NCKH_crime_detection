# This Python file uses the following encoding: utf-8
import cv2 as cv
import sys
import numpy as np
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QWidget
from Ui_main import Ui_Form
     
class RECORD_VIDEO(QtCore.QObject):
    image_data = QtCore.Signal(np.ndarray)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.camera_port = 0
        self.camera = cv.VideoCapture(self.camera_port)
        self.timer = QtCore.QBasicTimer()

    def start_recording(self):
        self.timer.start(0, self)

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return

        grab, image = self.camera.read()
        image = cv.flip(image, 1)
        if grab:
            self.image_data.emit(image)

class DETECTION_WIDGET(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 3
        self._min_size = (30, 30)
        # self.setFixedSize(QtCore.QSize(800, 300))
        self.setGeometry(QtCore.QRect(200,200,50,50))

    def image_data_slot(self, image_data):  
        self.image = self.get_qimage(image_data)
        # if self.image.size() != self.size():
        #     self.setFixedSize(self.image.size())

        self.update()

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        QImage = QtGui.QImage

        image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)

        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()


class action:
    def testCam(self):
        cap = cv.VideoCapture(0)
        while True:
            (grab, frame) = cap.read()
            if not grab:
                print("No image")
                break

            cv.imshow("frame", frame)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break
        
        cap.release()
        cv.destroyAllWindows()
    
class mainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)  
        # self.ui.pushButton.clicked.connect(action.testCam)
        # self.ui.alertButton.clicked.connect(self.safe)
        self.ui.warnButton.clicked.connect(self.warn)
        # self.ui.alertButton.clicked.connect(self.alert)

        self.ui.face_detection_widget = DETECTION_WIDGET()
        # self.record_video = RECORD_VIDEO()
        # image_data_slot = self.ui.face_detection_widget.image_data_slot
        # self.record_video.image_data.connect(image_data_slot)
        # self.record_video.start_recording()

        self.ui.layout = QtWidgets.QVBoxLayout(self)
        self.ui.layout.addWidget(self.ui.face_detection_widget)
        # self.setLayout(self.ui.layout)
        
        # self.ui.info_camLabel.setText("Camera " + str(self.record_video.camera_port))
    
    def warn(self):
        self.ui.warningStatus.hide()

if __name__ == "__main__":
    app = QApplication([])
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())


    
        

    
