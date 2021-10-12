import pyautogui as pa
import keyboard
import time
import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,qApp,QApplication
from PyQt5.QtWidgets import QComboBox, QStatusBar,QPushButton,QLineEdit,QGroupBox,QTextEdit,QLabel,QHBoxLayout,QVBoxLayout,QGridLayout

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

        self.pos = []
        self.n = 0

        ##Button
        start_macro_btn = QPushButton('매크로 시작')
        pos1_btn = QPushButton('pos1')
        pos2_btn = QPushButton('pos2')
        pos3_btn = QPushButton('pos3')
        pos4_btn = QPushButton('pos4')
        pos5_btn = QPushButton('pos5')
        pos6_btn = QPushButton('pos6')
        pos7_btn = QPushButton('pos7')
        scroll_btn=QPushButton('스크롤')

        ##Button Connect
        pos1_btn.clicked.connect(self.get_pos1)
        pos2_btn.clicked.connect(self.get_pos2)
        pos3_btn.clicked.connect(self.get_pos3)
        pos4_btn.clicked.connect(self.get_pos4)
        pos5_btn.clicked.connect(self.get_pos5)
        pos6_btn.clicked.connect(self.get_pos6)
        pos7_btn.clicked.connect(self.get_pos7)
        start_macro_btn.clicked.connect(self.start_macro)
        scroll_btn.clicked.connect(self.scr)

        ##QLineEdit
        self.pos1_qle = QLineEdit()
        self.pos2_qle = QLineEdit()
        self.pos3_qle=QLineEdit()
        self.pos4_qle = QLineEdit()
        self.pos5_qle = QLineEdit()
        self.pos6_qle = QLineEdit()
        self.pos7_qle=QLineEdit()

        self.pos1_qle.setDisabled(True)
        self.pos2_qle.setDisabled(True)
        self.pos3_qle.setDisabled(True)
        self.pos4_qle.setDisabled(True)
        self.pos5_qle.setDisabled(True)
        self.pos6_qle.setDisabled(True)
        self.pos7_qle.setDisabled(True)

        ##QCombobox
        self.combo1=QComboBox()

        groupbox1=QGroupBox("pos1 선택")
        groupbox2 = QGroupBox("pos2 선택")
        groupbox3 = QGroupBox("pos3 선택")
        groupbox4 = QGroupBox("pos4 선택")
        groupbox5 = QGroupBox("pos5 선택")
        groupbox6 = QGroupBox("pos6 선택")
        groupbox7 = QGroupBox("pos7 선택")


        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        hbox7 = QHBoxLayout()

        hbox1.addWidget(self.pos1_qle)
        hbox1.addWidget(pos1_btn)
        hbox1.addWidget(scroll_btn)
        hbox2.addWidget(self.pos2_qle)
        hbox2.addWidget(pos2_btn)
        hbox3.addWidget(self.pos3_qle)
        hbox3.addWidget(pos3_btn)
        hbox4.addWidget(self.pos4_qle)
        hbox4.addWidget(pos4_btn)
        hbox5.addWidget(self.pos5_qle)
        hbox5.addWidget(pos5_btn)
        hbox6.addWidget(self.pos6_qle)
        hbox6.addWidget(pos6_btn)
        hbox7.addWidget(self.pos7_qle)
        hbox7.addWidget(pos7_btn)

        groupbox1.setLayout(hbox1)
        groupbox2.setLayout(hbox2)
        groupbox3.setLayout(hbox3)
        groupbox4.setLayout(hbox4)
        groupbox5.setLayout(hbox5)
        groupbox6.setLayout(hbox6)
        groupbox7.setLayout(hbox7)

        self.vbox=QVBoxLayout()
        self.vbox.addWidget(groupbox1)
        self.vbox.addWidget(groupbox2)
        self.vbox.addWidget(groupbox3)
        self.vbox.addWidget(groupbox4)
        self.vbox.addWidget(groupbox5)
        self.vbox.addWidget(groupbox6)
        self.vbox.addWidget(groupbox7)
        self.vbox.addWidget(start_macro_btn)

        self.setLayout(self.vbox)
        self.setWindowTitle('영수증 첨부지 별 PDF 쪼개기 시스템')
        self.resize(500, 200)
        self.center()
        self.show()

    def get_pos(self,local_n):
        while True:
            if keyboard.is_pressed('f2'):
                x, y = pa.position()
                print(pa.position())
                self.pos.append([])
                self.pos[local_n].append(x)
                self.pos[local_n].append(y)
                print(self.pos)
                time.sleep(0.2)
                break


        if local_n==0:
            self.pos1_qle.setText("(" + str(self.pos[local_n][0]) + "," + str(self.pos[local_n][1]) + ")")
        elif local_n==1:
            self.pos2_qle.setText("(" + str(self.pos[local_n][0]) + "," + str(self.pos[local_n][1]) + ")")
        elif local_n==2:
            self.pos3_qle.setText("(" + str(self.pos[local_n][0]) + "," + str(self.pos[local_n][1]) + ")")
        elif local_n==3:
            self.pos4_qle.setText("(" + str(self.pos[local_n][0]) + "," + str(self.pos[local_n][1]) + ")")
        elif local_n==4:
            self.pos5_qle.setText("(" + str(self.pos[local_n][0]) + "," + str(self.pos[local_n][1]) + ")")
        elif local_n==5:
            self.pos6_qle.setText("(" + str(self.pos[local_n][0]) + "," + str(self.pos[local_n][1]) + ")")
        elif local_n==6:
            self.pos7_qle.setText("(" + str(self.pos[local_n][0]) + "," + str(self.pos[local_n][1]) + ")")

    def get_pos1(self):
        self.get_pos(0)

    def get_pos2(self):
        self.get_pos(1)

    def get_pos3(self):
        self.get_pos(2)

    def get_pos4(self):
        self.get_pos(3)

    def get_pos5(self):
        self.get_pos(4)

    def get_pos6(self):
        self.get_pos(5)

    def get_pos7(self):
        self.get_pos(6)

    def start_macro(self):
        x=0
        y=1
        for i in range(len(self.pos)):
            pa.click(x=self.pos[i][x], y=self.pos[i][y])
            pa.scroll(20)

    def scr(self):
        pa.scroll(20)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())