#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :  framelessWidget.py
@Date    :  2021/05/08
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
'''
from aigpyqt.style import ColorStyle
from aigpyqt.control import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class FramelessWidget(QWidget):
    def __init__(self):
        super(FramelessWidget, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.contentGrid = QGridLayout()
        self.windowBtnGrid = self.__creatWindowsButonLayout__()
        self.enableMove = True
        self.validMoveWidget = None

        grid = QGridLayout(self)
        grid.setSpacing(0)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.addLayout(self.contentGrid, 0, 0)
        grid.addLayout(self.windowBtnGrid, 0, 0, Qt.AlignTop | Qt.AlignRight)

    def __showMaxWindows__(self):
        if self.windowState() == Qt.WindowMaximized:
            self.showNormal()
        else:
            self.showMaximized()

    def __creatWindowsButonLayout__(self):
        self.closeBtn = PushButton('', ColorStyle.CloseWindow)
        self.maxBtn = PushButton('', ColorStyle.MaxWindow)
        self.minBtn = PushButton('', ColorStyle.MinWindow)

        self.closeBtn.clicked.connect(self.close)
        self.minBtn.clicked.connect(self.showMinimized)
        self.maxBtn.clicked.connect(self.__showMaxWindows__)

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.minBtn)
        layout.addWidget(self.maxBtn)
        layout.addWidget(self.closeBtn)
        return layout

    def __clickInValidMoveWidget__(self, x=-1, y=-1) -> bool:
        if self.validMoveWidget is None:
            return True
        if x == -1 and y == -1:
            x = self.clickPos.x()
            y = self.clickPos.y()

        pos = self.validMoveWidget.pos()
        if x < pos.x() or x > pos.x() + self.validMoveWidget.width():
            return False
        if y < pos.y() or y > pos.y() + self.validMoveWidget.height():
            return False
        return True

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.clickPos = e.pos()

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.clickPos = QPoint(-1, -1)

    def mouseMoveEvent(self, e: QMouseEvent):
        if not self.enableMove:
            return
        if Qt.LeftButton & e.buttons():
            if self.__clickInValidMoveWidget__():
                self.move(e.pos() + self.pos() - self.clickPos)
    
    def mouseDoubleClickEvent(self, e: QMouseEvent):
        if self.maxBtn.isHidden():
            return
        if Qt.LeftButton & e.buttons():
            if self.__clickInValidMoveWidget__(e.x(), e.y()):
                self.__showMaxWindows__()

    def getGrid(self):
        return self.contentGrid

    def hideMaxWindowButton(self):
        self.maxBtn.hide()

    def hideMinWindowButton(self):
        self.minBtn.hide()

    def disableMove(self):
        self.enableMove = False

    def setValidMoveWidget(self, widget):
        self.validMoveWidget = widget
