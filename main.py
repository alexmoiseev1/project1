import sys

import src.misc as misc
import gui.interface as interface
from gui.interface import YResultListItem
from src.search import YSearch
from src.excelsaver import ExcelSaver

from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QFileDialog
from PyQt5.QtGui import QColor
import PyQt5.QtCore as core

from functools import partial

class YWindow(QMainWindow):

    def __init__(self, keywords):
        super().__init__()
        self.ui = interface.Ui_MainWindow()
        self.keywords = keywords
        self.disabled = set()
        self.result = {}
        self.init()

    def init(self):
        self.ui.setupUi(self)
        self.__center()
        self.setWindowTitle(misc.WINDOW_TITLE)

        self.ui.actionExport_to_Excel.triggered.connect(partial(self.export_to_excel, self.ui.actionExport_to_Excel))

        self.ui.listWidget.setStyleSheet("QListWidget::item { padding: 10px 0; }")
        self.ui.listWidget_2.setStyleSheet("QListWidget::item { border-bottom: 1px solid #999; }")
        self.ui.listWidget_2.setHorizontalScrollBarPolicy(core.Qt.ScrollBarAlwaysOff)

        self.ui.addButton.clicked.connect(self.addButtonClick)
        self.ui.searchButton.clicked.connect(self.searchButtonClick)
        self.ui.removeButton.clicked.connect(self.removeButtonClick)
        self.ui.toggleButton.clicked.connect(self.toggleButtonClick)

        self.updateKeywordsList()

        self.show()

    def export_to_excel(self, item):
        filePath = QFileDialog.getSaveFileName(self, 'Save File', '/')
        saver = ExcelSaver()
        print(self.result)
        if self.result != {}:
            saver.export(self.result, filePath[0])

    def __center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def addButtonClick(self):
        text = self.ui.lineEdit.text().strip()

        if text != '':
            self.keywords.add(text)
            self.updateKeywordsList()

        self.ui.lineEdit.clear()

    def searchButtonClick(self):
        if self.ui.listWidget.count() > 0:

            for key in self.keywords:
                if key not in self.disabled:
                    temp = YSearch.run(q=key)
                    temp_dict = YSearch.to_dict(temp)
                    self.result.update(temp_dict)

            for channelId in self.result:
                channel_info = YSearch.channel(channelId)
                self.result[channelId]['stats'] = channel_info['statistics']['subscriberCount']
                self.result[channelId]['mail'] = YSearch.desc_to_mail(channel_info['snippet']['description'])
            self.updateSearchResultList(self.result)


    def toggleButtonClick(self):
        for i in self.ui.listWidget.selectedIndexes():
            item = self.ui.listWidget.item(i.row())
            
            if item.text() not in self.disabled:
                self.disabled.add(item.text())
                item.setBackground(QColor('#bbb'))
                item.setForeground(QColor('#ddd'))
            else:
                self.disabled.remove(item.text())
                item.setBackground(QColor('#fff'))
                item.setForeground(QColor('#000'))

    def removeButtonClick(self):
        for i in self.ui.listWidget.selectedIndexes():
            item = self.ui.listWidget.item(i.row())
            self.keywords.remove(item.text())
        self.updateKeywordsList()

    def updateKeywordsList(self):
        self.ui.listWidget.clear()
        [self.ui.listWidget.addItem(keyword) for keyword in sorted(self.keywords)]


    def updateSearchResultList(self, result):
        self.ui.listWidget_2.clear()


        for item in result:
            list_item_widget = YResultListItem()

            list_item_widget.setTextUp(result[item]['title'])
            list_item_widget.setTextDown('https://www.youtube.com/channel/' + result[item]['channelId'])
            list_item_widget.setTextRight('Subscribers: ' + result[item]['stats'])
            list_item_widget.setTextLeft(result[item]['mail'])

            list_item = QListWidgetItem(self.ui.listWidget_2)
            list_item.setSizeHint(list_item_widget.sizeHint())
            self.ui.listWidget_2.addItem(list_item)
            self.ui.listWidget_2.setItemWidget(list_item, list_item_widget)


def open_keywords():
    with open('etc/keywords', 'r') as f:
        key_words = set([line.strip() for line in f.readlines()])
    return key_words

if __name__ == '__main__':
    app = QApplication(sys.argv)
    initial_keys = open_keywords()
    window = YWindow(initial_keys)
    sys.exit(app.exec_())

