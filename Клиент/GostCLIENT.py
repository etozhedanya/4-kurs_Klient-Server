import sys

import traceback
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow, QMenu,  QComboBox
from PyQt5.uic import loadUi
import pymysql
from datetime import datetime
import sys 
import traceback
import sqlite3
import requests

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
login = 'Danya'
password = '1111'

class Login(QDialog):
                    
    def __init__(self):
        super(Login,self).__init__()
        loadUi("Login.ui",self)

        self.pushButton.clicked.connect(self.glmenu)

    def glmenu(self):
        lg = self.lineEdit_2.text()
        psw = self.lineEdit.text()
        
        if lg == login and psw == password:
            mainwindow = Admin()
            widget.addWidget(mainwindow)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            QMessageBox.about(self, "Ошибка", "Неккоректная авторизация")
            

class Admin(QDialog):
    
    def zapros(self):#функция запроса
        zapr = self.lineEdit_2.text()#переменная введённого условия в запрос
        cmbx = self.comboBox.currentText()#переменная выбранного пункта в комбо бокс 1
        cmbx2 = self.comboBox_2.currentText()#переменная выбранного пункта в комбо бокс 2
        strk = str(cmbx)+"-"+str(cmbx2)+"-"+str(zapr)
        cmbx3 = self.comboBox_3.currentText()

        try:
            if cmbx3 == 'Таблица: Клиенты':
                    com = requests.post(
                        'http://127.0.0.1:5000/zaprs1',
                        json={'text': strk}
                        )

                    itog = com.json()['result']

            
                    self.tableWidget.clear()

                    row = 0
                    column = 0

                    self.tableWidget.setRowCount(len(itog))
                    self.tableWidget.setColumnCount(3)

                    for i in itog:
                        for k in i:
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                            if column == 2:
                                row += 1
                                column = 0
                            else:
                                column += 1
          
                    self.tableWidget.setHorizontalHeaderLabels(["ID Клиента","ФИО","Возраст"])
            
            elif cmbx3 == 'Таблица: Сотрудники':
                com = requests.post(
                'http://127.0.0.1:5000/zaprs2',
                json={'text': strk}
                )
                itog = com.json()['result']
                self.tableWidget.clear()
                row = 0
                column = 0

                self.tableWidget.setRowCount(len(itog))
                self.tableWidget.setColumnCount(5)

                for i in itog:
                    for k in i:
                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                        if column == 4:
                            row += 1
                            column = 0
                        else:
                            column += 1
                              
                self.tableWidget.setHorizontalHeaderLabels(["ID Сотрудника","ФИО","Возраст","Должность","Зарплата"])

            elif cmbx3 == 'Таблица: Смены':
                com = requests.post(
                'http://127.0.0.1:5000/zaprs3',
                json={'text': strk}
                )
                itog = com.json()['result']
                self.tableWidget.clear()
                row = 0
                column = 0

                self.tableWidget.setRowCount(len(itog))
                self.tableWidget.setColumnCount(2)

                for i in itog:
                    for k in i:
                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                        if column == 1:
                            row += 1
                            column = 0
                        else:
                            column += 1
                              
                self.tableWidget.setHorizontalHeaderLabels(["ID Смены","ID Сотрудника"])
                
                
            elif cmbx3 == 'Таблица: Номера':
                com = requests.post(
                'http://127.0.0.1:5000/zaprs4',
                json={'text': strk}
                )
                itog = com.json()['result']
                self.tableWidget.clear()
                row = 0
                column = 0

                self.tableWidget.setRowCount(len(itog))
                self.tableWidget.setColumnCount(3)

                for i in itog:
                    for k in i:
                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                        if column == 2:
                            row += 1
                            column = 0
                        else:
                            column += 1
                              
                self.tableWidget.setHorizontalHeaderLabels(["ID Номера","Класс","Стоимость"])
                
            elif cmbx3 == 'Таблица: Журнал':
                com = requests.post(
                'http://127.0.0.1:5000/zaprs5',
                json={'text': strk}
                )
                itog = com.json()['result']
                self.tableWidget.clear()
                row = 0
                column = 0

                self.tableWidget.setRowCount(len(itog))
                self.tableWidget.setColumnCount(6)

                for i in itog:
                    for k in i:
                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                        if column == 5:
                            row += 1
                            column = 0
                        else:
                            column += 1
                              
                self.tableWidget.setHorizontalHeaderLabels(["ID Записи","ID Клиента","ID Номера","ID Смены","Дата заезда","Дата выезда"])
            
        except pymysql.err.ProgrammingError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Пусто!")
        
        except pymysql.err.OperationalError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Некорректный ввод данных!")
        
        except pymysql.err.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                "Сотрудник привязан к другой таблице!")

        
    
    
    def loadbd(self):
        self.comboBox.clear()
        cmbx3 = self.comboBox_3.currentText()
        if cmbx3 == 'Таблица: Клиенты':
            com = requests.post(
                'http://127.0.0.1:5000/myfunction',
                json={'text': 'text'}
                )

            itog = com.json()['result']

            row = 0
            column = 0
            self.tableWidget.setRowCount(len(itog))
            self.tableWidget.setColumnCount(3)

            for i in itog:
                for k in i:
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                    if column == 2:
                        row += 1
                        column = 0
                    else:
                        column += 1
            self.tableWidget.setHorizontalHeaderLabels(["ID Клиента","ФИО","Возраст"])
            self.comboBox.addItems(["ID Клиента","ФИО","Возраст"])
            
        elif cmbx3 == 'Таблица: Сотрудники': 
            com = requests.post(
                'http://127.0.0.1:5000/myfunction2',
                json={'text': 'text'}
                )

            itog = com.json()['result']

            row = 0
            column = 0
            self.tableWidget.setRowCount(len(itog))
            self.tableWidget.setColumnCount(5)

            for i in itog:
                for k in i:
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                    if column == 4:
                        row += 1
                        column = 0
                    else:
                        column += 1
            self.tableWidget.setHorizontalHeaderLabels(["ID Сотрудника","ФИО","Возраст","Должность","Зарплата"])
            self.comboBox.addItems(["ID Сотрудника","ФИО","Возраст","Должность","Зарплата"])

        elif cmbx3 == 'Таблица: Смены': 
            com = requests.post(
                'http://127.0.0.1:5000/myfunction3',
                json={'text': 'text'}
                )

            itog = com.json()['result']

            row = 0
            column = 0
            self.tableWidget.setRowCount(len(itog))
            self.tableWidget.setColumnCount(2)

            for i in itog:
                for k in i:
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                    if column == 1:
                        row += 1
                        column = 0
                    else:
                        column += 1
            self.tableWidget.setHorizontalHeaderLabels(["ID Смены","ID Сотрудника"])
            self.comboBox.addItems(["ID Смены","ID Сотрудника"])
            
        elif cmbx3 == 'Таблица: Номера': 
            com = requests.post(
                    'http://127.0.0.1:5000/myfunction4',
                    json={'text': 'text'}
                )

            itog = com.json()['result']

            row = 0
            column = 0
            self.tableWidget.setRowCount(len(itog))
            self.tableWidget.setColumnCount(3)

            for i in itog:
                for k in i:
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                    if column == 2:
                        row += 1
                        column = 0
                    else:
                        column += 1
            self.tableWidget.setHorizontalHeaderLabels(["ID Номера","Класс","Стоимость"])
            self.comboBox.addItems(["ID Номера","Класс","Стоимость"])
            
        elif cmbx3 == 'Таблица: Журнал': 
            com = requests.post(
                    'http://127.0.0.1:5000/myfunction5',
                    json={'text': 'text'}
                )

            itog = com.json()['result']

            row = 0
            column = 0
            self.tableWidget.setRowCount(len(itog))
            self.tableWidget.setColumnCount(6)

            for i in itog:
                for k in i:
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                    if column == 5:
                        row += 1
                        column = 0
                    else:
                        column += 1
            self.tableWidget.setHorizontalHeaderLabels(["ID Записи","ID Клиента","ID Номера","ID Смены","Дата заезда","Дата выезда"])
            self.comboBox.addItems(["ID Записи","ID Клиента","ID Номера","ID Смены","Дата заезда","Дата выезда"])
            
    
    def __init__(self):
        super(Admin,self).__init__()
        loadUi("glmenu.ui",self)
        widget.setFixedWidth(600)
        widget.setFixedHeight(506)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()
        
        self.pushButton_5.clicked.connect(self.sotr)
        self.pushButton_2.clicked.connect(self.otr)
        self.pushButton_3.clicked.connect(self.sostotr)
        self.pushButton_4.clicked.connect(self.tran)
        self.pushButton.clicked.connect(self.loadbd)
        self.pushButton_6.clicked.connect(self.zapros)
        self.pushButton_7.clicked.connect(self.zhur)
        
        
    def sotr(self):
        sotrr = Sotrudniki()
        widget.addWidget(sotrr)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def otr(self):
        otrr = Otryad()
        widget.addWidget(otrr)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def tran(self):
        tranr = Transport()
        widget.addWidget(tranr)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def sostotr(self):
        sostotrr = Sostotr()
        widget.addWidget(sostotrr)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def zhur(self):
        zhur = Zhur()
        widget.addWidget(zhur)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Sotrudniki(QDialog):
    def loadbd(self):
        com = requests.post(
        'http://127.0.0.1:5000/myfunction5',
        json={'text': 'text'}
        )

        itog = com.json()['result']

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))
        self.tableWidget.setColumnCount(6)

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 5:
                    row += 1
                    column = 0
                else:
                    column += 1
        self.tableWidget.setHorizontalHeaderLabels(["ID Записи","ID Клиента","ID Номера","ID Смены","Дата заезда","Дата выезда"])

    def dobavzp(self):
        ids = self.lineEdit.text()
        fio = self.lineEdit_2.text()
        gen = self.lineEdit_3.text()
        old = self.lineEdit_4.text()
        zv = self.lineEdit_5.text()
        idot = self.lineEdit_6.text()

        strk = str(ids)+"-"+str(fio)+"-"+str(gen)+"-"+str(old)+"-"+str(zv)+"-"+str(idot)

        com = requests.post(
        'http://127.0.0.1:5000/dobavv4',
        json={'text': strk}
        )
            
        self.tableWidget.clear()
        self.loadbd()
    
    def udalzp(self):
        ids = self.lineEdit_7.text()
        
        strk = str(ids)

        com = requests.post(
        'http://127.0.0.1:5000/ubavv4',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()

    def izmzp(self):
        ids = self.lineEdit_8.text()
        cmbx = self.comboBox.currentText()
        upd = self.lineEdit_9.text()
        
        strk = str(ids)+"-"+str(cmbx)+"-"+str(upd)

        com = requests.post(
        'http://127.0.0.1:5000/izmavv4',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()
                    
    def __init__(self):
        super(Sotrudniki,self).__init__()
        loadUi("sotrudniki.ui",self)
        widget.setFixedWidth(601)
        widget.setFixedHeight(432)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()

        self.pushButton_4.clicked.connect(self.glmenu)
        self.pushButton.clicked.connect(self.dobavzp)
        self.pushButton_2.clicked.connect(self.udalzp)
        self.pushButton_3.clicked.connect(self.izmzp)

    def glmenu(self):
        mainwindow = Admin()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Zhur(QDialog):
    def loadbd(self):
        com = requests.post(
        'http://127.0.0.1:5000/myfunction5',
        json={'text': 'text'}
        )

        itog = com.json()['result']

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))
        self.tableWidget.setColumnCount(6)

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 5:
                    row += 1
                    column = 0
                else:
                    column += 1
        self.tableWidget.setHorizontalHeaderLabels(["ID Записи","ID Клиента","ID Номера","ID Смены","Дата заезда","Дата выезда"])

    def dobavzp(self):
        ids = self.lineEdit.text()
        fio = self.lineEdit_2.text()
        gen = self.lineEdit_3.text()
        old = self.lineEdit_4.text()
        zv = self.lineEdit_5.text()

        strk = str(ids)+"-"+str(fio)+"-"+str(gen)+"-"+str(old)+"-"+str(zv)

        com = requests.post(
        'http://127.0.0.1:5000/dobavv5',
        json={'text': strk}
        )
            
        self.tableWidget.clear()
        self.loadbd()
    
    def udalzp(self):
        ids = self.lineEdit_7.text()
        
        strk = str(ids)

        com = requests.post(
        'http://127.0.0.1:5000/ubavv5',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()

    def izmzp(self):
        ids = self.lineEdit_8.text()
        cmbx = self.comboBox.currentText()
        upd = self.lineEdit_9.text()
        
        strk = str(ids)+"-"+str(cmbx)+"-"+str(upd)

        com = requests.post(
        'http://127.0.0.1:5000/izmavv5',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()
                    
    def __init__(self):
        super(Zhur,self).__init__()
        loadUi("sotrudniki2.ui",self)
        widget.setFixedWidth(501)
        widget.setFixedHeight(432)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()

        self.pushButton_4.clicked.connect(self.glmenu)
        self.pushButton.clicked.connect(self.dobavzp)
        self.pushButton_2.clicked.connect(self.udalzp)
        self.pushButton_3.clicked.connect(self.izmzp)

    def glmenu(self):
        mainwindow = Admin()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Transport(QDialog):
    def loadbd(self):
        com = requests.post(
        'http://127.0.0.1:5000/myfunction3',
        json={'text': 'text'}
        )

        itog = com.json()['result']

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))
        self.tableWidget.setColumnCount(2)

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 1:
                    row += 1
                    column = 0
                else:
                    column += 1
        self.tableWidget.setHorizontalHeaderLabels(["ID Смены","ID Сотрудника"])
    
    def dobavzp(self):
        idsm = self.lineEdit.text()
        idsot = self.lineEdit_2.text()

        strk = str(idsm)+"-"+str(idsot)

        com = requests.post(
        'http://127.0.0.1:5000/dobavv3',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()

    def udalzp(self):
        idsm = self.lineEdit_7.text()
        idsot = self.lineEdit_3.text()

        strk = str(idsm)+"-"+str(idsot)

        com = requests.post(
        'http://127.0.0.1:5000/ubavv3',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()
    
    def __init__(self):
        super(Transport,self).__init__()
        loadUi("Transport.ui",self)
        widget.setFixedWidth(201)
        widget.setFixedHeight(403)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()

        self.pushButton_4.clicked.connect(self.glmenu)
        self.pushButton.clicked.connect(self.dobavzp)
        self.pushButton_2.clicked.connect(self.udalzp)

    def glmenu(self):
        mainwindow = Admin()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Sostotr(QDialog):
    def loadbd(self):
        com = requests.post(
        'http://127.0.0.1:5000/myfunction4',
        json={'text': 'text'}
        )

        itog = com.json()['result']

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))
        self.tableWidget.setColumnCount(3)

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 2:
                    row += 1
                    column = 0
                else:
                    column += 1
        self.tableWidget.setHorizontalHeaderLabels(["ID Номера","Класс","Стоимость"])
    
    def dobavzp(self):
        idnom = self.lineEdit.text()
        clas = self.lineEdit_2.text()
        price = self.lineEdit_3.text()

        strk = str(idnom)+"-"+str(clas)+"-"+str(price)

        com = requests.post(
        'http://127.0.0.1:5000/dobavv2',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()

    def udalzp(self):
        idnom = self.lineEdit_7.text()
        
        strk = str(idnom)

        com = requests.post(
        'http://127.0.0.1:5000/ubavv2',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()

    def izmzp(self):
        idnom = self.lineEdit_8.text()
        cmbx = self.comboBox.currentText()
        upd = self.lineEdit_9.text()
        
        strk = str(idnom)+"-"+str(cmbx)+"-"+str(upd)

        com = requests.post(
        'http://127.0.0.1:5000/izmavv2',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()
    
    def __init__(self):
        super(Sostotr,self).__init__()
        loadUi("Sostotr.ui",self)
        widget.setFixedWidth(301)
        widget.setFixedHeight(432)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()

        self.pushButton_4.clicked.connect(self.glmenu)
        self.pushButton.clicked.connect(self.dobavzp)
        self.pushButton_2.clicked.connect(self.udalzp)
        self.pushButton_3.clicked.connect(self.izmzp)

    def glmenu(self):
        mainwindow = Admin()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Otryad(QDialog):
    def loadbd(self):
        com = requests.post(
        'http://127.0.0.1:5000/myfunction',
        json={'text': 'text'}
        )

        itog = com.json()['result']

        row = 0
        column = 0
        self.tableWidget.setRowCount(len(itog))
        self.tableWidget.setColumnCount(3)

        for i in itog:
            for k in i:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(k)))
                if column == 2:
                    row += 1
                    column = 0
                else:
                    column += 1
        self.tableWidget.setHorizontalHeaderLabels(["ID Клиента","ФИО","Возраст"])
    
    def dobavzp(self):
        idcl = self.lineEdit.text()
        fio = self.lineEdit_2.text()
        old = self.lineEdit_3.text()

        strk = str(idcl)+"-"+str(fio)+"-"+str(old)

        com = requests.post(
        'http://127.0.0.1:5000/dobavv1',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()

    def udalzp(self):
        idcl = self.lineEdit_7.text()
        
        strk = str(idcl)

        com = requests.post(
        'http://127.0.0.1:5000/ubavv1',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()

    def izmzp(self):
        idcl = self.lineEdit_8.text()
        cmbx = self.comboBox.currentText()
        upd = self.lineEdit_9.text()
        
        strk = str(idcl)+"-"+str(cmbx)+"-"+str(upd)

        com = requests.post(
        'http://127.0.0.1:5000/izmavv1',
        json={'text': strk}
        )

        itog = com.json()['result']
            
        self.tableWidget.clear()
        self.loadbd()
    
    def __init__(self):
        super(Otryad,self).__init__()
        loadUi("Otryad.ui",self)
        widget.setFixedWidth(301)
        widget.setFixedHeight(432)

        self.loadbd()
        self.tableWidget.verticalHeader().hide()

        self.pushButton_4.clicked.connect(self.glmenu)
        self.pushButton.clicked.connect(self.dobavzp)
        self.pushButton_2.clicked.connect(self.udalzp)
        self.pushButton_3.clicked.connect(self.izmzp)

    def glmenu(self):
        mainwindow = Admin()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

mainwindow = Login()
widget.addWidget(mainwindow)
widget.setFixedWidth(113)
widget.setFixedHeight(63)
widget.show()
widget.setWindowTitle('Шеметов РГ')
app.exec_()
