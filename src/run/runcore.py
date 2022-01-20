#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2022 NXP
# All rights reserved.
# 
# SPDX-License-Identifier: BSD-3-Clause

import sys
import os
import rundef
sys.path.append(os.path.abspath(".."))
from ui import uicore
from ui import uidef
from ui import uilang

class memTesterRun(uicore.memTesterUi):

    def __init__(self, parent=None):
        super(memTesterRun, self).__init__(parent)

