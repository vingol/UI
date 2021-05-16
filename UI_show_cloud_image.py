# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_cloud_image.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import base64
import pickle
import datetime
import numpy as np
from images.cloud_image_jpg import img as cloud_image
from images.map_png import img as map_img
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import scipy.io as scio
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PIL import Image

# 需要先设置内存限制，不然仍然会报错内存溢出
Image.MAX_IMAGE_PIXELS = None

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=4, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.subplots_adjust(left=0.12, bottom=0.2, right=0.9, top=0.9, hspace=0, wspace=0)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # self.init_plot()#打开App时可以初始化图片
        # self.plot()

    def plot(self, image_to_plot, points):
        counter = 0
        count = len(image_to_plot)
        def start_timer():
            nonlocal counter
            global inputs
            counter += 1
            inputs = [counter, image_to_plot, points]
            if counter >= count-1:
                timer.stop()
                timer.deleteLater()

        timer = QTimer(self)
        print('timer start')
        timer.timeout.connect(start_timer)
        timer.timeout.connect(lambda: self.update_figure(inputs))
        timer.start(1000)


    def update_figure(self, inputs):
        self.axes.cla()
        counter, image_to_plot, points = inputs[0], inputs[1], inputs[2]

        self.axes.imshow(image_to_plot[counter], cmap='gray')

        for point in points:
            self.axes.scatter(point[1], point[0], s=10)

        print('plot ', counter)
        self.axes.set_xticks(range(0, 4500, 500))
        x_ticks_ = np.arange(0, 2250, 250)
        self.axes.set_xticklabels(x_ticks_, rotation=0, fontsize=8)

        self.axes.set_yticks(range(0, 3500, 500))
        y_ticks_ = np.arange(0, 1750, 250)
        self.axes.set_yticklabels(y_ticks_, rotation=0, fontsize=8)


        self.axes.set_xlabel('km')
        self.axes.set_ylabel('km')
        self.draw()
        # self.axes.imshow(image_to_plot[counter], cmap='gray')


class Ui_MainWindow_show_cloudimage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 310, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(140, 380, 113, 32))
        self.pushButton2.setObjectName("pushButton2")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 879, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 371, 31))
        self.label.setObjectName("label")
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView.setGeometry(QtCore.QRect(370, 120, 401, 331))
        # self.graphicsView.setMinimumSize(QtCore.QSize(401, 331))
        # self.graphicsView.setMaximumSize(QtCore.QSize(401, 331))
        # self.graphicsView.setObjectName("graphicsView")

        self.m = PlotCanvas(self, width=4, height=3.5)  # 实例化一个画布对象
        self.m.move(370, 120)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 220, 327, 56))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.comboBox_starttime = QtWidgets.QComboBox(self.widget)
        self.comboBox_starttime.setObjectName("comboBox_starttime")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.setItemText(0, "")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.comboBox_starttime.addItem("")
        self.gridLayout.addWidget(self.comboBox_starttime, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.comboBox_endtime = QtWidgets.QComboBox(self.widget)
        self.comboBox_endtime.setObjectName("comboBox_endtime")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.setItemText(0, "")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.comboBox_endtime.addItem("")
        self.gridLayout.addWidget(self.comboBox_endtime, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.comboBox_starttime.currentIndexChanged[str].connect(
            self.get_starttime)  # 条目发生改变，发射信号，传递条目内容

        self.comboBox_endtime.currentIndexChanged[str].connect(
            self.get_endtime)  # 条目发生改变，发射信号，传递条目内容

        # 展示一张
        self.pushButton.clicked.connect(self.show_image)

        # 动态波动
        self.pushButton2.clicked.connect(self.load_and_show)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "显示云图"))

        self.pushButton2.setText(_translate("MainWindow", "动态播放"))

        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:24pt;\">卫星云图数据展示</span></p><p><br/></p></body></html>"))
        self.label_15.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">开始时间：</span></p></body></html>"))
        self.comboBox_starttime.setItemText(1, _translate("MainWindow", "2018-10-27 06:30:00"))
        self.comboBox_starttime.setItemText(2, _translate("MainWindow", "2018-10-27 06:34:17"))
        self.comboBox_starttime.setItemText(3, _translate("MainWindow", "2018-10-27 06:38:34"))
        self.comboBox_starttime.setItemText(4, _translate("MainWindow", "2018-10-27 06:45:00"))
        self.comboBox_starttime.setItemText(5, _translate("MainWindow", "2018-10-27 06:49:17"))
        self.comboBox_starttime.setItemText(6, _translate("MainWindow", "2018-10-27 06:53:34"))
        self.comboBox_starttime.setItemText(7, _translate("MainWindow", "2018-10-27 07:15:00"))
        self.comboBox_starttime.setItemText(8, _translate("MainWindow", "2018-10-27 07:19:17"))
        self.comboBox_starttime.setItemText(9, _translate("MainWindow", "2018-10-27 07:23:34"))
        self.comboBox_starttime.setItemText(10, _translate("MainWindow", "2018-10-27 07:30:00"))
        self.comboBox_starttime.setItemText(11, _translate("MainWindow", "2018-10-27 07:34:17"))
        self.comboBox_starttime.setItemText(12, _translate("MainWindow", "2018-10-27 07:38:34"))
        self.comboBox_starttime.setItemText(13, _translate("MainWindow", "2018-10-27 08:30:00"))
        self.comboBox_starttime.setItemText(14, _translate("MainWindow", "2018-10-27 08:34:17"))
        self.comboBox_starttime.setItemText(15, _translate("MainWindow", "2018-10-27 08:38:34"))
        self.comboBox_starttime.setItemText(16, _translate("MainWindow", "2018-10-27 08:45:00"))
        self.comboBox_starttime.setItemText(17, _translate("MainWindow", "2018-10-27 08:49:17"))
        self.comboBox_starttime.setItemText(18, _translate("MainWindow", "2018-10-27 08:53:34"))
        self.comboBox_starttime.setItemText(19, _translate("MainWindow", "2018-10-27 09:15:00"))
        self.comboBox_starttime.setItemText(20, _translate("MainWindow", "2018-10-27 09:19:17"))
        self.comboBox_starttime.setItemText(21, _translate("MainWindow", "2018-10-27 09:23:34"))
        self.comboBox_starttime.setItemText(22, _translate("MainWindow", "2018-10-27 09:30:00"))
        self.comboBox_starttime.setItemText(23, _translate("MainWindow", "2018-10-27 09:34:17"))
        self.comboBox_starttime.setItemText(24, _translate("MainWindow", "2018-10-27 09:38:34"))
        self.comboBox_starttime.setItemText(25, _translate("MainWindow", "2018-10-27 09:45:00"))
        self.comboBox_starttime.setItemText(26, _translate("MainWindow", "2018-10-27 09:49:17"))
        self.comboBox_starttime.setItemText(27, _translate("MainWindow", "2018-10-27 09:53:34"))
        self.comboBox_starttime.setItemText(28, _translate("MainWindow", "2018-10-27 10:15:00"))
        self.comboBox_starttime.setItemText(29, _translate("MainWindow", "2018-10-27 10:19:17"))
        self.comboBox_starttime.setItemText(30, _translate("MainWindow", "2018-10-27 10:23:34"))
        self.comboBox_starttime.setItemText(31, _translate("MainWindow", "2018-10-27 10:30:00"))
        self.comboBox_starttime.setItemText(32, _translate("MainWindow", "2018-10-27 10:34:17"))
        self.comboBox_starttime.setItemText(33, _translate("MainWindow", "2018-10-27 10:38:34"))
        self.comboBox_starttime.setItemText(34, _translate("MainWindow", "2018-10-27 11:30:00"))
        self.comboBox_starttime.setItemText(35, _translate("MainWindow", "2018-10-27 11:34:17"))
        self.comboBox_starttime.setItemText(36, _translate("MainWindow", "2018-10-27 11:38:34"))
        self.comboBox_starttime.setItemText(37, _translate("MainWindow", "2018-10-27 11:45:00"))
        self.comboBox_starttime.setItemText(38, _translate("MainWindow", "2018-10-27 11:49:17"))
        self.comboBox_starttime.setItemText(39, _translate("MainWindow", "2018-10-27 11:53:34"))
        self.comboBox_starttime.setItemText(40, _translate("MainWindow", "2018-10-27 12:15:00"))
        self.comboBox_starttime.setItemText(41, _translate("MainWindow", "2018-10-27 12:19:17"))
        self.comboBox_starttime.setItemText(42, _translate("MainWindow", "2018-10-27 12:23:34"))
        self.comboBox_starttime.setItemText(43, _translate("MainWindow", "2018-10-27 12:30:00"))
        self.comboBox_starttime.setItemText(44, _translate("MainWindow", "2018-10-27 12:34:17"))
        self.comboBox_starttime.setItemText(45, _translate("MainWindow", "2018-10-27 12:38:34"))
        self.comboBox_starttime.setItemText(46, _translate("MainWindow", "2018-10-27 12:45:00"))
        self.comboBox_starttime.setItemText(47, _translate("MainWindow", "2018-10-27 12:49:17"))
        self.comboBox_starttime.setItemText(48, _translate("MainWindow", "2018-10-27 12:53:34"))
        self.comboBox_starttime.setItemText(49, _translate("MainWindow", "2018-10-27 13:15:00"))
        self.comboBox_starttime.setItemText(50, _translate("MainWindow", "2018-10-27 13:19:17"))
        self.comboBox_starttime.setItemText(51, _translate("MainWindow", "2018-10-27 13:23:34"))
        self.comboBox_starttime.setItemText(52, _translate("MainWindow", "2018-10-27 13:30:00"))
        self.comboBox_starttime.setItemText(53, _translate("MainWindow", "2018-10-27 13:34:17"))
        self.comboBox_starttime.setItemText(54, _translate("MainWindow", "2018-10-27 13:38:34"))
        self.comboBox_starttime.setItemText(55, _translate("MainWindow", "2018-10-27 14:30:00"))
        self.comboBox_starttime.setItemText(56, _translate("MainWindow", "2018-10-27 14:34:17"))
        self.comboBox_starttime.setItemText(57, _translate("MainWindow", "2018-10-27 14:38:34"))
        self.comboBox_starttime.setItemText(58, _translate("MainWindow", "2018-10-27 14:45:00"))
        self.comboBox_starttime.setItemText(59, _translate("MainWindow", "2018-10-27 14:49:17"))
        self.comboBox_starttime.setItemText(60, _translate("MainWindow", "2018-10-27 14:53:34"))
        self.comboBox_starttime.setItemText(61, _translate("MainWindow", "2018-10-27 15:15:00"))
        self.comboBox_starttime.setItemText(62, _translate("MainWindow", "2018-10-27 15:19:17"))
        self.comboBox_starttime.setItemText(63, _translate("MainWindow", "2018-10-27 15:23:34"))
        self.comboBox_starttime.setItemText(64, _translate("MainWindow", "2018-10-27 15:30:00"))
        self.comboBox_starttime.setItemText(65, _translate("MainWindow", "2018-10-27 15:34:17"))
        self.comboBox_starttime.setItemText(66, _translate("MainWindow", "2018-10-27 15:38:34"))
        self.comboBox_starttime.setItemText(67, _translate("MainWindow", "2018-10-27 15:45:00"))
        self.comboBox_starttime.setItemText(68, _translate("MainWindow", "2018-10-27 15:49:17"))
        self.comboBox_starttime.setItemText(69, _translate("MainWindow", "2018-10-27 15:53:34"))
        self.comboBox_starttime.setItemText(70, _translate("MainWindow", "2018-10-27 16:15:00"))
        self.comboBox_starttime.setItemText(71, _translate("MainWindow", "2018-10-27 16:19:17"))
        self.comboBox_starttime.setItemText(72, _translate("MainWindow", "2018-10-27 16:23:34"))
        self.comboBox_starttime.setItemText(73, _translate("MainWindow", "2018-10-27 16:30:00"))
        self.comboBox_starttime.setItemText(74, _translate("MainWindow", "2018-10-27 16:34:17"))
        self.comboBox_starttime.setItemText(75, _translate("MainWindow", "2018-10-27 16:38:34"))
        self.comboBox_starttime.setItemText(76, _translate("MainWindow", "2018-10-27 17:30:00"))
        self.comboBox_starttime.setItemText(77, _translate("MainWindow", "2018-10-27 17:34:17"))
        self.comboBox_starttime.setItemText(78, _translate("MainWindow", "2018-10-27 17:38:34"))
        self.comboBox_starttime.setItemText(79, _translate("MainWindow", "2018-10-27 17:45:00"))
        self.comboBox_starttime.setItemText(80, _translate("MainWindow", "2018-10-27 17:49:17"))
        self.comboBox_starttime.setItemText(81, _translate("MainWindow", "2018-10-27 17:53:34"))
        self.comboBox_starttime.setItemText(82, _translate("MainWindow", "2018-10-27 18:15:00"))
        self.comboBox_starttime.setItemText(83, _translate("MainWindow", "2018-10-27 18:19:17"))
        self.comboBox_starttime.setItemText(84, _translate("MainWindow", "2018-10-27 18:23:34"))
        self.comboBox_starttime.setItemText(85, _translate("MainWindow", "2018-10-27 18:30:00"))
        self.comboBox_starttime.setItemText(86, _translate("MainWindow", "2018-10-27 18:34:17"))
        self.comboBox_starttime.setItemText(87, _translate("MainWindow", "2018-10-27 18:38:34"))
        self.comboBox_starttime.setItemText(88, _translate("MainWindow", "2018-10-27 18:38:34"))
        self.comboBox_starttime.setItemText(89, _translate("MainWindow", "2018-10-27 18:49:17"))
        self.comboBox_starttime.setItemText(90, _translate("MainWindow", "2018-10-27 18:53:34"))
        self.comboBox_starttime.setItemText(91, _translate("MainWindow", "2018-10-27 19:15:00"))
        self.comboBox_starttime.setItemText(92, _translate("MainWindow", "2018-10-27 19:19:17"))
        self.comboBox_starttime.setItemText(93, _translate("MainWindow", "2018-10-27 19:23:34"))
        self.comboBox_starttime.setItemText(94, _translate("MainWindow", "2018-10-27 19:30:00"))
        self.comboBox_starttime.setItemText(95, _translate("MainWindow", "2018-10-27 19:34:17"))
        self.comboBox_starttime.setItemText(96, _translate("MainWindow", "2018-10-27 19:38:34"))
        self.label_16.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">截止时间：</span></p></body></html>"))
        self.comboBox_endtime.setItemText(1, _translate("MainWindow", "2018-10-27 06:30:00"))
        self.comboBox_endtime.setItemText(2, _translate("MainWindow", "2018-10-27 06:34:17"))
        self.comboBox_endtime.setItemText(3, _translate("MainWindow", "2018-10-27 06:38:34"))
        self.comboBox_endtime.setItemText(4, _translate("MainWindow", "2018-10-27 06:45:00"))
        self.comboBox_endtime.setItemText(5, _translate("MainWindow", "2018-10-27 06:49:17"))
        self.comboBox_endtime.setItemText(6, _translate("MainWindow", "2018-10-27 06:53:34"))
        self.comboBox_endtime.setItemText(7, _translate("MainWindow", "2018-10-27 07:15:00"))
        self.comboBox_endtime.setItemText(8, _translate("MainWindow", "2018-10-27 07:19:17"))
        self.comboBox_endtime.setItemText(9, _translate("MainWindow", "2018-10-27 07:23:34"))
        self.comboBox_endtime.setItemText(10, _translate("MainWindow", "2018-10-27 07:30:00"))
        self.comboBox_endtime.setItemText(11, _translate("MainWindow", "2018-10-27 07:34:17"))
        self.comboBox_endtime.setItemText(12, _translate("MainWindow", "2018-10-27 07:38:34"))
        self.comboBox_endtime.setItemText(13, _translate("MainWindow", "2018-10-27 08:30:00"))
        self.comboBox_endtime.setItemText(14, _translate("MainWindow", "2018-10-27 08:34:17"))
        self.comboBox_endtime.setItemText(15, _translate("MainWindow", "2018-10-27 08:38:34"))
        self.comboBox_endtime.setItemText(16, _translate("MainWindow", "2018-10-27 08:45:00"))
        self.comboBox_endtime.setItemText(17, _translate("MainWindow", "2018-10-27 08:49:17"))
        self.comboBox_endtime.setItemText(18, _translate("MainWindow", "2018-10-27 08:53:34"))
        self.comboBox_endtime.setItemText(19, _translate("MainWindow", "2018-10-27 09:15:00"))
        self.comboBox_endtime.setItemText(20, _translate("MainWindow", "2018-10-27 09:19:17"))
        self.comboBox_endtime.setItemText(21, _translate("MainWindow", "2018-10-27 09:23:34"))
        self.comboBox_endtime.setItemText(22, _translate("MainWindow", "2018-10-27 09:30:00"))
        self.comboBox_endtime.setItemText(23, _translate("MainWindow", "2018-10-27 09:34:17"))
        self.comboBox_endtime.setItemText(24, _translate("MainWindow", "2018-10-27 09:38:34"))
        self.comboBox_endtime.setItemText(25, _translate("MainWindow", "2018-10-27 09:45:00"))
        self.comboBox_endtime.setItemText(26, _translate("MainWindow", "2018-10-27 09:49:17"))
        self.comboBox_endtime.setItemText(27, _translate("MainWindow", "2018-10-27 09:53:34"))
        self.comboBox_endtime.setItemText(28, _translate("MainWindow", "2018-10-27 10:15:00"))
        self.comboBox_endtime.setItemText(29, _translate("MainWindow", "2018-10-27 10:19:17"))
        self.comboBox_endtime.setItemText(30, _translate("MainWindow", "2018-10-27 10:23:34"))
        self.comboBox_endtime.setItemText(31, _translate("MainWindow", "2018-10-27 10:30:00"))
        self.comboBox_endtime.setItemText(32, _translate("MainWindow", "2018-10-27 10:34:17"))
        self.comboBox_endtime.setItemText(33, _translate("MainWindow", "2018-10-27 10:38:34"))
        self.comboBox_endtime.setItemText(34, _translate("MainWindow", "2018-10-27 11:30:00"))
        self.comboBox_endtime.setItemText(35, _translate("MainWindow", "2018-10-27 11:34:17"))
        self.comboBox_endtime.setItemText(36, _translate("MainWindow", "2018-10-27 11:38:34"))
        self.comboBox_endtime.setItemText(37, _translate("MainWindow", "2018-10-27 11:45:00"))
        self.comboBox_endtime.setItemText(38, _translate("MainWindow", "2018-10-27 11:49:17"))
        self.comboBox_endtime.setItemText(39, _translate("MainWindow", "2018-10-27 11:53:34"))
        self.comboBox_endtime.setItemText(40, _translate("MainWindow", "2018-10-27 12:15:00"))
        self.comboBox_endtime.setItemText(41, _translate("MainWindow", "2018-10-27 12:19:17"))
        self.comboBox_endtime.setItemText(42, _translate("MainWindow", "2018-10-27 12:23:34"))
        self.comboBox_endtime.setItemText(43, _translate("MainWindow", "2018-10-27 12:30:00"))
        self.comboBox_endtime.setItemText(44, _translate("MainWindow", "2018-10-27 12:34:17"))
        self.comboBox_endtime.setItemText(45, _translate("MainWindow", "2018-10-27 12:38:34"))
        self.comboBox_endtime.setItemText(46, _translate("MainWindow", "2018-10-27 12:45:00"))
        self.comboBox_endtime.setItemText(47, _translate("MainWindow", "2018-10-27 12:49:17"))
        self.comboBox_endtime.setItemText(48, _translate("MainWindow", "2018-10-27 12:53:34"))
        self.comboBox_endtime.setItemText(49, _translate("MainWindow", "2018-10-27 13:15:00"))
        self.comboBox_endtime.setItemText(50, _translate("MainWindow", "2018-10-27 13:19:17"))
        self.comboBox_endtime.setItemText(51, _translate("MainWindow", "2018-10-27 13:23:34"))
        self.comboBox_endtime.setItemText(52, _translate("MainWindow", "2018-10-27 13:30:00"))
        self.comboBox_endtime.setItemText(53, _translate("MainWindow", "2018-10-27 13:34:17"))
        self.comboBox_endtime.setItemText(54, _translate("MainWindow", "2018-10-27 13:38:34"))
        self.comboBox_endtime.setItemText(55, _translate("MainWindow", "2018-10-27 14:30:00"))
        self.comboBox_endtime.setItemText(56, _translate("MainWindow", "2018-10-27 14:34:17"))
        self.comboBox_endtime.setItemText(57, _translate("MainWindow", "2018-10-27 14:38:34"))
        self.comboBox_endtime.setItemText(58, _translate("MainWindow", "2018-10-27 14:45:00"))
        self.comboBox_endtime.setItemText(59, _translate("MainWindow", "2018-10-27 14:49:17"))
        self.comboBox_endtime.setItemText(60, _translate("MainWindow", "2018-10-27 14:53:34"))
        self.comboBox_endtime.setItemText(61, _translate("MainWindow", "2018-10-27 15:15:00"))
        self.comboBox_endtime.setItemText(62, _translate("MainWindow", "2018-10-27 15:19:17"))
        self.comboBox_endtime.setItemText(63, _translate("MainWindow", "2018-10-27 15:23:34"))
        self.comboBox_endtime.setItemText(64, _translate("MainWindow", "2018-10-27 15:30:00"))
        self.comboBox_endtime.setItemText(65, _translate("MainWindow", "2018-10-27 15:34:17"))
        self.comboBox_endtime.setItemText(66, _translate("MainWindow", "2018-10-27 15:38:34"))
        self.comboBox_endtime.setItemText(67, _translate("MainWindow", "2018-10-27 15:45:00"))
        self.comboBox_endtime.setItemText(68, _translate("MainWindow", "2018-10-27 15:49:17"))
        self.comboBox_endtime.setItemText(69, _translate("MainWindow", "2018-10-27 15:53:34"))
        self.comboBox_endtime.setItemText(70, _translate("MainWindow", "2018-10-27 16:15:00"))
        self.comboBox_endtime.setItemText(71, _translate("MainWindow", "2018-10-27 16:19:17"))
        self.comboBox_endtime.setItemText(72, _translate("MainWindow", "2018-10-27 16:23:34"))
        self.comboBox_endtime.setItemText(73, _translate("MainWindow", "2018-10-27 16:30:00"))
        self.comboBox_endtime.setItemText(74, _translate("MainWindow", "2018-10-27 16:34:17"))
        self.comboBox_endtime.setItemText(75, _translate("MainWindow", "2018-10-27 16:38:34"))
        self.comboBox_endtime.setItemText(76, _translate("MainWindow", "2018-10-27 17:30:00"))
        self.comboBox_endtime.setItemText(77, _translate("MainWindow", "2018-10-27 17:34:17"))
        self.comboBox_endtime.setItemText(78, _translate("MainWindow", "2018-10-27 17:38:34"))
        self.comboBox_endtime.setItemText(79, _translate("MainWindow", "2018-10-27 17:45:00"))
        self.comboBox_endtime.setItemText(80, _translate("MainWindow", "2018-10-27 17:49:17"))
        self.comboBox_endtime.setItemText(81, _translate("MainWindow", "2018-10-27 17:53:34"))
        self.comboBox_endtime.setItemText(82, _translate("MainWindow", "2018-10-27 18:15:00"))
        self.comboBox_endtime.setItemText(83, _translate("MainWindow", "2018-10-27 18:19:17"))
        self.comboBox_endtime.setItemText(84, _translate("MainWindow", "2018-10-27 18:23:34"))
        self.comboBox_endtime.setItemText(85, _translate("MainWindow", "2018-10-27 18:30:00"))
        self.comboBox_endtime.setItemText(86, _translate("MainWindow", "2018-10-27 18:34:17"))
        self.comboBox_endtime.setItemText(87, _translate("MainWindow", "2018-10-27 18:38:34"))
        self.comboBox_endtime.setItemText(88, _translate("MainWindow", "2018-10-27 18:38:34"))
        self.comboBox_endtime.setItemText(89, _translate("MainWindow", "2018-10-27 18:49:17"))
        self.comboBox_endtime.setItemText(90, _translate("MainWindow", "2018-10-27 18:53:34"))
        self.comboBox_endtime.setItemText(91, _translate("MainWindow", "2018-10-27 19:15:00"))
        self.comboBox_endtime.setItemText(92, _translate("MainWindow", "2018-10-27 19:19:17"))
        self.comboBox_endtime.setItemText(93, _translate("MainWindow", "2018-10-27 19:23:34"))
        self.comboBox_endtime.setItemText(94, _translate("MainWindow", "2018-10-27 19:30:00"))
        self.comboBox_endtime.setItemText(95, _translate("MainWindow", "2018-10-27 19:34:17"))
        self.comboBox_endtime.setItemText(96, _translate("MainWindow", "2018-10-27 19:38:34"))

    def get_starttime(self, i):
        global start_time
        start_time = i

    def get_endtime(self, i):
        global end_time
        end_time = i

    def time_to_str(self, t):

        t1, t2 = t.split(' ')
        year, month, day = t1.split('-')
        hour, minute, second = t2.split(':')

        return str(year) + str(month) + str(day) + str(hour) + str(minute) + str(second) + '.mat'

    def load_and_show(self):

        try:

            with open('extra_data/cloud_iamge_names.pkl', 'rb') as file:
                image_names = pickle.load(file)

            points = np.loadtxt('extra_data/pixel_pos_.txt')

            print(start_time)
            print(end_time)

            start_name = self.time_to_str(str(pd.to_datetime(start_time) - datetime.timedelta(hours=8)))
            end_name = self.time_to_str(str(pd.to_datetime(end_time) - datetime.timedelta(hours=8)))

            start_index = image_names.index(start_name)
            end_index = image_names.index(end_name)

            images_to_plot = []
            for file_name in image_names[start_index:end_index]:
                images_to_plot.append(scio.loadmat('2018_10_26/'+file_name)['name'])

            self.m.plot(images_to_plot, points)

        except NameError:
            pass



    def show_image(self):

        try:


            with open('extra_data/cloud_iamge_names.pkl', 'rb') as file:
                image_names = pickle.load(file)

            points = np.loadtxt('extra_data/pixel_pos_.txt')

            start_name = self.time_to_str(str(pd.to_datetime(start_time) - datetime.timedelta(hours=8)))

            start_index = image_names.index(start_name)

            with open('20180618051500.pkl', 'rb') as file:
                image_to_plot = pickle.load(file)[1:3001, 11000:15000]

            inputs = [0, [image_to_plot], points]

            self.m.update_figure(inputs)

        except NameError:
            pass


