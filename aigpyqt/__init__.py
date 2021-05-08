#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :  __init__.py
@Date    :  2021/05/08
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
'''
import sys
import aigpy
import aigpyqt.theme
from PyQt5.Qt import *
from aigpyqt.page.loginView import LoginView

loginView = None

def buttonClicked():
    account = loginView.getAccountInfo()
    username = account['username']
    password = account['password']
    if aigpy.string.isNull(username) or aigpy.string.isNull(password):
        loginView.showErrMessage('请检查并重新输入正确的账号密码')

if __name__ == '__main__':
    qss = aigpyqt.theme.getThemeQssContent()
    app = QApplication(sys.argv)
    app.setStyleSheet(qss)
    loginView = LoginView()
    loginView.setButtonClickFunction(buttonClicked)
    loginView.show()
    sys.exit(app.exec_())



