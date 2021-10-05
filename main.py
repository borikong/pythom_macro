import pyautogui as pa
import keyboard
import time
import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,qApp,QApplication
from PyQt5.QtWidgets import QMessageBox, QStatusBar,QPushButton,QLineEdit,QGroupBox,QTextEdit,QLabel,QHBoxLayout,QVBoxLayout,QGridLayout

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

        print(self.objectName())
        self.statusBar=QStatusBar()

        self.pdf_root = ""
        self.save_root = ""

        self.pos = [[], [], [], [], [], [], [], []]
        self.n = 0

        start_macro_btn = QPushButton('매크로 시작')
        pos1_btn = QPushButton('pos1')
        pos2_btn = QPushButton('pos2')
        pos3_btn = QPushButton('pos3')

        pos1_btn.clicked.connect(self.get_pos1)
        pos2_btn.clicked.connect(self.get_pos2)
        pos3_btn.clicked.connect(self.get_pos3)
        start_macro_btn.clicked.connect(self.start_macro)

        self.pos1_qle = QLineEdit()
        self.pos2_qle = QLineEdit()
        self.pos3_qle=QLineEdit()

        self.pos1_qle.setDisabled(True)
        self.pos2_qle.setDisabled(True)
        self.pos3_qle.setDisabled(True)

        groupbox1=QGroupBox("pos1 선택")
        groupbox2 = QGroupBox("pos2 선택")
        groupbox3 = QGroupBox("pos3 선택")

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        hbox1.addWidget(self.pos1_qle)
        hbox1.addWidget(pos1_btn)
        hbox2.addWidget(self.pos2_qle)
        hbox2.addWidget(pos2_btn)
        hbox3.addWidget(self.pos3_qle)
        hbox3.addWidget(pos3_btn)

        groupbox1.setLayout(hbox1)
        groupbox2.setLayout(hbox2)
        groupbox3.setLayout(hbox3)

        self.vbox=QVBoxLayout()
        self.vbox.addWidget(groupbox1)
        self.vbox.addWidget(groupbox2)
        self.vbox.addWidget(groupbox3)
        self.vbox.addWidget(start_macro_btn)

        self.setLayout(self.vbox)
        self.setWindowTitle('영수증 첨부지 별 PDF 쪼개기 시스템')
        self.resize(500, 200)
        self.center()
        self.show()

    def get_pos1(self):
        local_n=0
        while True:
            if keyboard.is_pressed('f2'):
                x,y=pa.position()
                print(pa.position())
                self.pos[local_n].append(x)
                self.pos[local_n].append(y)
                print(self.pos)
                time.sleep(1)
                break
        self.pos1_qle.setText("("+str(self.pos[local_n][0])+","+str(self.pos[local_n][1])+")")

    def get_pos2(self):
        local_n=1
        while True:
            if keyboard.is_pressed('f2'):
                x,y=pa.position()
                print(pa.position())
                self.pos[local_n].append(x)
                self.pos[local_n].append(y)
                print(self.pos)
                time.sleep(1)
                break
        self.pos2_qle.setText("("+str(self.pos[local_n][0])+","+str(self.pos[local_n][1])+")")

    def get_pos3(self):
        local_n=2
        while True:
            if keyboard.is_pressed('f2'):
                x,y=pa.position()
                print(pa.position())
                self.pos[local_n].append(x)
                self.pos[local_n].append(y)
                print(self.pos)
                time.sleep(1)
                break
        self.pos3_qle.setText("("+str(self.pos[local_n][0])+","+str(self.pos[local_n][1])+")")

    def start_macro(self):
        x=0
        y=1
        for i in range(3):
            pa.click(x=self.pos[i][x], y=self.pos[i][y])

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())