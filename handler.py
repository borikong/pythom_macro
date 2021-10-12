import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication
from PyQt5.QtWidgets import QStatusBar,QPushButton,QVBoxLayout
import voice as vc
import time

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):

        self.statusBar=QStatusBar()

        ##Button
        start_voice_btn = QPushButton('음성인식 시작')

        start_voice_btn.clicked.connect(self.voice_start)

        vbox = QVBoxLayout()
        vbox.addWidget(start_voice_btn)

        self.setLayout(vbox)
        self.setWindowTitle('음성명령')
        self.resize(500, 200)
        self.center()
        self.show()

    def voice_start(self):
        audio_path = r"C:\python_project\macro\record_file\temp.wav"
        vc.set()
        vc.start()
        time.sleep(3)
        vc.stop()
        vc.command(vc.recognize_text(audio_path))


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())