import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication
from PyQt5.QtWidgets import QStatusBar,QPushButton,QVBoxLayout,QComboBox,QLineEdit,QHBoxLayout,QGroupBox,QGridLayout
import voice as vc
import time, os
import tkinter.filedialog
from tkinter import Tk

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

        ##변수 세팅
        self.download_path=r"C:\Users\admin\Downloads"
        file_list=os.listdir(self.download_path)
        print(file_list)

        self.statusBar=QStatusBar()

        ##Button
        start_voice_btn = QPushButton('음성인식 시작')
        retry_btn = QPushButton('새로고침')
        change_fname_btn=QPushButton('파일명 변경')
        change_dir_btn=QPushButton('파일 이동')
        select_dir_btn=QPushButton('폴더 선택')

        start_voice_btn.clicked.connect(self.voice_start)
        retry_btn.clicked.connect(self.add_combo)
        change_fname_btn.clicked.connect(self.change_file_name)
        change_dir_btn.clicked.connect(self.change_dir)
        select_dir_btn.clicked.connect(self.get_save_root)

        ##콤보박스
        self.combo=QComboBox()

        for i in file_list:
            self.combo.addItem(i)

        ##QLE
        self.edit_fname_qle=QLineEdit()
        self.ch_dir_qle = QLineEdit()

        ##gropubox
        gbox1=QGroupBox()

        ##grid
        grid1=QGridLayout()

        grid1.addWidget(self.edit_fname_qle,0,0)
        grid1.addWidget(change_fname_btn, 0, 1)
        grid1.addWidget(self.ch_dir_qle, 1, 0)
        grid1.addWidget(change_dir_btn, 1, 1)
        grid1.addWidget(select_dir_btn, 2, 0)
        grid1.addWidget(retry_btn, 2, 1)

        gbox1.setLayout(grid1)

        vbox = QVBoxLayout()
        vbox.addWidget(start_voice_btn)
        vbox.addWidget(self.combo)
        vbox.addWidget(gbox1)

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

    def change_file_name(self):
        print(self.combo.currentText())
        print(self.edit_fname_qle.text())
        old_file=self.combo.currentText()
        old_file=old_file.split(".")
        print(old_file)
        os.rename(self.download_path+"/"+self.combo.currentText(),self.download_path+"/"+self.edit_fname_qle.text()+"."+old_file[-1])
        self.add_combo()

    def add_combo(self):
        self.combo.clear()
        file_list = os.listdir(self.download_path)
        for i in file_list:
            self.combo.addItem(i)

    def change_dir(self):
        print(self.combo.currentText())
        print(self.edit_fname_qle.text())
        # new_dir=self.combo.currentText()
        # new_dir=new_dir.split("/")
        os.rename(self.download_path+"/"+self.combo.currentText(),self.ch_dir_qle.text()+"/"+self.combo.currentText())
        self.add_combo()

    def get_save_root(self):
        Tk().withdraw()
        save_folder = tkinter.filedialog.askdirectory(title="저장 폴더 선택");
        print(save_folder)
        self.ch_dir_qle.setText(save_folder)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())