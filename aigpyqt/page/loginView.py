#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :  loginView.py
@Date    :  2021/04/30
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
'''
import cgitb
import sys
import aigpy

from aigpyqt.style import ColorStyle
from aigpyqt.control import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class LoginView(FramelessWidget):
    viewWidth = 650
    viewHeight = 400
    logoWidth = 300

    def __init__(self):
        super(LoginView, self).__init__()
        self.setFixedSize(self.viewWidth, self.viewHeight)
        self.__initView__()

    def __creatHLayout__(self, widgets):
        layout = QHBoxLayout()
        for item in widgets:
            layout.addWidget(item)
        return layout

    def __initAccountTab__(self):
        self.userEdit = LineEdit()
        self.pwdEdit = LineEdit()
        self.rememberMeBox = CheckBox("RememberMe", True)
        self.automaticLoginBox = CheckBox("AutomaticLogin", True)
        self.confimBtn = PushButton("OK", ColorStyle.Primary)

        grid = QGridLayout()
        grid.setSpacing(15)
        grid.setRowStretch(0, 1)
        grid.addLayout(self.__creatHLayout__([Label("username:"), self.userEdit]), 1, 0, 1, 2)
        grid.addLayout(self.__creatHLayout__([Label("password:"), self.pwdEdit]), 2, 0, 1, 2)
        grid.setRowStretch(3, 1)
        grid.addLayout(self.__creatHLayout__([self.rememberMeBox, self.automaticLoginBox]), 4, 0, 1, 2)
        grid.addWidget(self.confimBtn, 5, 0, 1, 2)
        grid.setRowStretch(6, 1)

        widget = QWidget()
        widget.setLayout(grid)
        return widget

    def __initProxyTab__(self):
        self.enableProxyCheck = CheckBox('')
        self.proxyHostEdit = LineEdit()
        self.proxyPortEdit = LineEdit()
        self.proxyUserEdit = LineEdit()
        self.proxyPwdEdit = LineEdit()

        grid = QGridLayout()
        grid.setSpacing(8)
        grid.setRowStretch(0, 1)
        grid.addWidget(Label("HttpProxy"), 1, 0)
        grid.addWidget(self.enableProxyCheck, 1, 1)
        grid.addWidget(Label("Host"), 2, 0)
        grid.addWidget(self.proxyHostEdit, 2, 1)
        grid.addWidget(Label("Port"), 3, 0)
        grid.addWidget(self.proxyPortEdit, 3, 1)
        grid.addWidget(Label("UserName"), 4, 0)
        grid.addWidget(self.proxyUserEdit, 4, 1)
        grid.addWidget(Label("Password"), 5, 0)
        grid.addWidget(self.proxyPwdEdit, 5, 1)
        grid.setRowStretch(6, 1)

        widget = QWidget()
        widget.setLayout(grid)
        return widget

    def __initView__(self):
        icon = Label()
        icon.setFixedSize(self.logoWidth, self.viewHeight)
        icon.setStyleSheet("QLabel{background-color:rgb(0,0,0);}")
        icon.setPixmap(QPixmap("./aigpyqt/resource/svg/Down.svg"))
        icon.setAlignment(Qt.AlignCenter)

        tab = QTabWidget(self)
        tab.addTab(self.__initAccountTab__(), "LOGIN")
        tab.addTab(self.__initProxyTab__(), "PROXY")
        tab.setFixedWidth(self.viewWidth - self.logoWidth - 60)

        self.hideMaxWindowButton()
        self.hideMinWindowButton()
        self.setValidMoveWidget(icon)

        grid = self.getGrid()
        grid.setSpacing(15)
        grid.setContentsMargins(0,0,0,0) 
        grid.addWidget(icon)
        grid.addWidget(tab, 0, 1, Qt.AlignCenter)

    def enableHttpProxy(self) -> bool:
        return self.enableProxyCheck.isChecked()
    
    def isRememberMe(self) -> bool:
        return self.rememberMeBox.isChecked()

    def isAutoLogin(self) -> bool:
        return self.automaticLoginBox.isChecked()

    def getProxyInfo(self) -> dict:
        infos = {}
        infos['host'] = self.proxyHostEdit.text()
        infos['port'] = self.proxyPortEdit.text()
        infos['username'] = self.proxyUserEdit.text()
        infos['password'] = self.proxyPwdEdit.text()
        return infos

    def getAccountInfo(self) -> dict:
        infos = {}
        infos['username'] = self.userEdit.text()
        infos['password'] = self.pwdEdit.text()
        return infos

    def setButtonClickFunction(self, func): 
        self.confimBtn.clicked.connect(func)

    def showErrMessage(self, text: str):
        qmb = QMessageBox(self)
        qmb.setWindowTitle('Error')
        qmb.setIcon(QMessageBox.Warning)
        qmb.setText(text)
        qmb.addButton(QPushButton('OK', qmb), QMessageBox.YesRole)
        qmb.open()
