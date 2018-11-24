#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Copyright (C) 2015-2018 Shenzhen Auto-link world Information Technology Co., Ltd.
  All Rights Reserved

  Name: Parse.py
  Purpose:

  Created By:    Clive Lau <liuxusheng@auto-link.com.cn>
  Created Date:  2018-02-23

  Changelog:
  Date         Desc
  2018-02-23   Created by Clive Lau
"""

# Builtin libraries

# Third-party libraries

# Customized libraries
from Protobuf import tbox_pb2
from ParseDump import ParseDump


class Parse(object):
    def __init__(self):
        pass
        # LogTag
        # self._tag = self.__class__.__name__ + ' '
        # print(self._tag + "__init__ called")

    def __del__(self):
        pass
        # print(self._tag + "__del__ called")

    def on_create(self):
        pass
        # print(self._tag + "on_create called")

    def on_destroy(self):
        pass
        # print(self._tag + "on_destroy called")

    def on_parse(self, msg):
        msgtop = tbox_pb2.MsgTop()
        msgtop.ParseFromString(msg)
        ParseDump.dump(msgtop)


if __name__ == '__main__':
    pass
