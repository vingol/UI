#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from UI_main_win import *
from UI_show_plot import *
from UI_show_cloud_image import *
from PyQt5.QtWidgets import QApplication, QMainWindow


os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["DEBUSSY"] = "1"

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

class MyWindow_show_plot(QMainWindow, Ui_MainWindow_show_plot):
    def __init__(self, parent=None):
        super(MyWindow_show_plot, self).__init__(parent)
        self.setupUi(self)

class MyWindow_cloud_image(QMainWindow, Ui_MainWindow_show_cloudimage):
    def __init__(self, parent=None):
        super(MyWindow_cloud_image, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # 字体随分辨率自适应
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()

    # 跳转 show plot
    Window_show_plot = MyWindow_show_plot()

    btn_show_plot = myWin.pushButton_3
    btn_show_plot.clicked.connect(Window_show_plot.show)

    # 跳转 show image
    Window_cloud_image = MyWindow_cloud_image()

    btn_cloud_image = myWin.pushButton_4
    btn_cloud_image.clicked.connect(Window_cloud_image.show)

    sys.exit(app.exec_())