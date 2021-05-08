#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :  label.py
@Date    :  2021/05/08
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
'''
from PyQt5.QtWidgets import QLabel

class Label(QLabel):
    def __init__(self, text: str = ""):
        super(Label, self).__init__()
        self.setText(text)
