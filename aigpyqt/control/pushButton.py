#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :  pushButton.py
@Date    :  2021/05/08
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
'''

from PyQt5.QtWidgets import QPushButton
from aigpyqt.style import ColorStyle


class PushButton(QPushButton):
    def __init__(self, text: str, style: ColorStyle = ColorStyle.Default):
        super(PushButton, self).__init__()
        self.setText(text)
        self.setObjectName(style.name + "PushButton")

        


