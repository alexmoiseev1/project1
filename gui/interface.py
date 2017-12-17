# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ysearchdesign.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont

class YResultListItem(QWidget):
    def __init__ (self, parent = None):
        super(YResultListItem, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()
        self.textRightQLabel = QLabel()
        self.textLeftQLabel = QLabel()

        self.textUpQLabel.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textDownQLabel.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textLeftQLabel.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        hfont = QFont()
        hfont.setPointSize(17)

        self.textUpQLabel.setFont(hfont)
        self.textUpQLabel.setWordWrap(True)

        self.textDownQLabel.setWordWrap(True)
        self.textLeftQLabel.setWordWrap(True)

        self.textUpQLabel.hasSelectedText()
        self.textDownQLabel.hasSelectedText()
        self.textRightQLabel.hasSelectedText()
        self.textLeftQLabel.hasSelectedText()

        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.textQVBoxLayout.addWidget(self.textRightQLabel)
        self.textQVBoxLayout.addWidget(self.textLeftQLabel)

        self.allQHBoxLayout  = QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

        self.textUpQLabel.setStyleSheet('''
            color: rgba(0, 0, 0, 0.7);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgba(0, 0, 0, 0.7);
        ''')
        self.textRightQLabel.setStyleSheet('''
            color: rgba(0, 0, 0, 0.7);
        ''')

        self.textLeftQLabel.setStyleSheet('''
            color: rgba(0, 0, 0, 0.5);
            font-size: 12px;
        ''')

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

    def setTextRight(self, text):
        self.textRightQLabel.setText(text)

    def setTextLeft(self, text):
        self.textLeftQLabel.setText(text)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.actionExport_to_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_to_Excel.setObjectName("actionExport_to_Excel")
        self.menuFile.addAction(self.actionExport_to_Excel)
        self.menubar.addAction(self.menuFile.menuAction())

        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toggleButton = QtWidgets.QPushButton(self.frame)
        self.toggleButton.setAutoDefault(False)
        self.toggleButton.setDefault(False)
        self.toggleButton.setFlat(False)
        self.toggleButton.setObjectName("toggleButton")
        self.horizontalLayout_2.addWidget(self.toggleButton)
        self.removeButton = QtWidgets.QPushButton(self.frame)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setDefault(False)
        self.removeButton.setFlat(False)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout_2.addWidget(self.removeButton)
        self.searchButton = QtWidgets.QPushButton(self.frame)
        self.searchButton.setAutoDefault(False)
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.horizontalLayout_3.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter a keyword..."))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.toggleButton.setText(_translate("MainWindow", "Toggle"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExport_to_Excel.setText(_translate("MainWindow", "Export to Excel"))

