#!/usr/bin/env python
#
# title           :onoff_touchpad.py
# author          :jm4rcos
# date            :21/Abr/2016
# version         :0.1
# python_version  :2.7.11

'''
GNU - GENERAL PUBLIC LICENSE v3

onoff_touchpad.py

Copyright (C) <2016> JOSE (J) MARCOS <jm4rcos@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the  Free Software Foundation,  either  version 3 of the License, or
(at your option) any later version.

This  program  is distributed  in  the hope that it  will be useful,
but  WITHOUT  ANY  WARRANTY;  without even  the implied warranty  of
MERCHANTABILITY  or  FITNESS  FOR  A  PARTICULAR  PURPOSE.  See  the
GNU General Public License for more details.

You should  have  received  a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import os

# read TouchpadOff and save value
r = os.popen('synclient |grep TouchpadOff').read().strip('\n').split('=')
ri = int(r[1])

# enable touchpad if off
if ri == 0 :
    os.popen('synclient TouchpadOff=1')
# disable it if on
elif ri == 1:
    os.popen('synclient TouchpadOff=0')
