from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import subprocess


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(429, 255)
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'icons/stopwatch.svg')))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.clock_label = QtWidgets.QLabel(self.centralwidget)
        self.clock_label.setAlignment(QtCore.Qt.AlignCenter)
        self.clock_label.setObjectName("clock_label")
        self.gridLayout.addWidget(self.clock_label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.hours_label = QtWidgets.QLabel(self.centralwidget)
        self.hours_label.setObjectName("hours_label")
        self.horizontalLayout.addWidget(self.hours_label)
        self.hours_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hours_line.sizePolicy().hasHeightForWidth())
        self.hours_line.setSizePolicy(sizePolicy)
        self.hours_line.setMaximumSize(QtCore.QSize(90, 16777215))
        self.hours_line.setAlignment(QtCore.Qt.AlignCenter)
        self.hours_line.setObjectName("hours_line")
        self.horizontalLayout.addWidget(self.hours_line)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.minutes_label = QtWidgets.QLabel(self.centralwidget)
        self.minutes_label.setObjectName("minutes_label")
        self.horizontalLayout.addWidget(self.minutes_label)
        self.minutes_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.minutes_line.sizePolicy().hasHeightForWidth())
        self.minutes_line.setSizePolicy(sizePolicy)
        self.minutes_line.setMinimumSize(QtCore.QSize(0, 0))
        self.minutes_line.setMaximumSize(QtCore.QSize(90, 16777215))
        self.minutes_line.setBaseSize(QtCore.QSize(40, 0))
        self.minutes_line.setAlignment(QtCore.Qt.AlignCenter)
        self.minutes_line.setObjectName("minutes_line")
        self.horizontalLayout.addWidget(self.minutes_line)
        spacerItem4 = QtWidgets.QSpacerItem(40, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.seconds_label = QtWidgets.QLabel(self.centralwidget)
        self.seconds_label.setObjectName("seconds_label")
        self.horizontalLayout.addWidget(self.seconds_label)
        self.seconds_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seconds_line.sizePolicy().hasHeightForWidth())
        self.seconds_line.setSizePolicy(sizePolicy)
        self.seconds_line.setMaximumSize(QtCore.QSize(90, 16777215))
        self.seconds_line.setAlignment(QtCore.Qt.AlignCenter)
        self.seconds_line.setObjectName("seconds_line")
        self.horizontalLayout.addWidget(self.seconds_line)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_2.addWidget(self.stop_button)
        spacerItem7 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_2.addWidget(self.start_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.center_on_screen()
        self.retranslateUi()

        self.time = None
        self.timer = QtCore.QTimer()

        self.os = os.name

        QtCore.QMetaObject.connectSlotsByName(self)
        self.start_button.clicked.connect(self.set_shutdown)
        self.stop_button.clicked.connect(self.stop)
        self.timer.timeout.connect(self.start_timer)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", " "))
        self.clock_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">ShutdownTimer</span></p></body></html>"))
        self.hours_label.setText(_translate("MainWindow", "H:"))
        self.minutes_label.setText(_translate("MainWindow", "M:"))
        self.seconds_label.setText(_translate("MainWindow", "S:"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.start_button.setText(_translate("MainWindow", "Start"))

    def center_on_screen(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move(int((resolution.width() / 2) - (self.frameSize().width() / 2)), int((resolution.height() / 2) - (self.frameSize().height() / 2)))

    def convert_time(self):
        hours, minutes, seconds = 0, 0, 0
        if self.hours_line.text():
            hours = abs(int(self.hours_line.text()))
        if self.minutes_line.text():
            minutes = abs(int(self.minutes_line.text()))
        if self.seconds_line.text():
            seconds = abs(int(self.seconds_line.text()))

        self.time = (hours*60*60) + (minutes*60) + seconds

    def start_timer(self):
        self.time -= 1
        self.clock_label.setText("Shutdown in: " + str(self.time) + 's')
        if self.time == 0:
            self.timer.stop()
        self.repaint()

    def set_shutdown(self):
        self.convert_time()
        print(self.os)
        print(self.time)

        if self.time > 0:
            if self.os == 'posix':
                minutes = self.time / 60
                if minutes < 1:     # anything less than one results in immediate shutdown linux likes minutes windows likes seconds
                    minutes = 1
                subprocess.run(['shutdown', '+' + str(int(minutes))])
                self.timer.start(1000)
                self.start_timer()

            if self.os == 'nt':
                subprocess.run(['shutdown', '/s', '/t', str(self.time)])
                self.start_timer()

    def stop(self):
        if self.os == 'posix':
            subprocess.run(['shutdown', '-c'])
        if self.os == 'nt':
            subprocess.run(['shutdown', '/a'])
        self.timer.stop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
