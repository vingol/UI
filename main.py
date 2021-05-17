#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import pickle
from UI_main_win import *
from UI_show_plot import *
from UI_show_plot_NeiMeng import *
from UI_show_cloud_image import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject , pyqtSignal


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

class MyWindow_show_plot_NeiMeng(QMainWindow, Ui_MainWindow_show_plot_NeiMeng):
    def __init__(self, parent=None):
        super(MyWindow_show_plot_NeiMeng, self).__init__(parent)
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

    data_source = '吉林'

    def receive(text):
        global data_source
        data_source = text
        print(data_source)

    myWin.signal.connect(receive)

    print(data_source)

    # 跳转 show plot
    Window_show_plot = MyWindow_show_plot()
    MyWindow_show_plot_NeiMeng = MyWindow_show_plot_NeiMeng()

    # with open('main_win_data/data_source.pkl', 'rb') as f:
    #     data_source = pickle.load(f)
    #
    #     print(data_source)

    # btn_show_plot = myWin.pushButton_3
    # #
    # if data_source == '吉林':
    #     print(data_source)
    #     btn_show_plot.clicked.connect(Window_show_plot.show)
    # elif data_source == '内蒙':
    #     print(data_source)
    #     btn_show_plot.clicked.connect(MyWindow_show_plot_NeiMeng.show)

    # 跳转 show image
    Window_cloud_image = MyWindow_cloud_image()

    btn_cloud_image = myWin.pushButton_4
    btn_cloud_image.clicked.connect(Window_cloud_image.show)

    sys.exit(app.exec_())