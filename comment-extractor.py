import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout, QPushButton,QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QTimer
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from certifi.__main__ import args


data = {'company1': ['Apple', 'Facebook', 'Google', 'Amazon' 'Walmart'],
        'company2': ['Dropbox', 'Starbucks', 'eBay', 'Canon' , 'wix'],
        'company3': ['c', '', '', '' ''],
        'company4': ['', '', '', '' '']}


class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.resize(310, 189)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 1000)
        mainLayout = QVBoxLayout()
        companies = ('Apple', 'Facebook', 'Google', 'Amazon', 'Walmart', 'Dropbox', 'Starbucks', 'eBay', 'Canon', 'Wix')
        model = QStandardItemModel(len(companies), 1)
        model.setHorizontalHeaderLabels(['Company'])

        for row, company in enumerate(companies):
            item = QStandardItem(company)
            model.setItem(row, 0, item)


        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(0)

        search_field = QLineEdit()
        search_field.setStyleSheet('font-size: 35px; height: 60px;')
        search_field.textChanged.connect(filter_proxy_model.setFilterRegExp)
        mainLayout.addWidget(search_field)

        table = QTableView()
        table.setStyleSheet('font-size: 35px;')
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(filter_proxy_model)
        mainLayout.addWidget(table)

        self.setLayout(mainLayout)





app = QApplication(sys.argv)
demo = AppDemo()
demo.show()

sys.exit(app.exec_())

