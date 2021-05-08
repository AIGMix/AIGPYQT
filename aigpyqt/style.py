#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :  enum.py
@Date    :  2021/05/08
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :  
'''

from enum import Enum

class ColorStyle(Enum):
    Default = 0,
    Primary = 1,
    Success = 2,
    Danger = 3,
    Warning = 4,
    Info = 5,
    CloseWindow = 6,
    MaxWindow = 7,
    MinWindow = 8,

class ThemeStyle(Enum):
    Default = 0,
    Dark = 1,
