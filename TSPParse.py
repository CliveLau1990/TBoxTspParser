#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Copyright (C) 2015-2018 Shenzhen Auto-link world Information Technology Co., Ltd.
  All Rights Reserved

  Name: TSPMonitor.py
  Purpose:

  Created By:    Clive Lau <liuxusheng@auto-link.com.cn>
  Created Date:  2018-01-26

  Changelog:
  Date         Desc
  2018-01-26   Created by Clive Lau
"""

# Builtin libraries
import sqlite3
import argparse
import binascii

# Third-party libraries

# Customized libraries
from Parse.Parse import Parse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--db', type=str, default='tspcomm.db')
    args = parser.parse_args()

    parse = Parse()
    parse.on_create()

    try:
        while True:
            curr = 0
            total = 0
            index = 0
            msg = None

            conn = sqlite3.connect(args.db)
            cursor = conn.cursor()
            rows = cursor.execute("SELECT MyIndex, MyLevel, MsgTime, Data FROM MsgData")
            for row in rows:
                if total < str(row[0]):
                    total = str(row[0])
            conn.close()

            index = raw_input('\nPlease type the expected index(MaxIdx:' + str(total) + '):')
            if not index.isdigit():
                print('Error: Invalid value(Integer)')
                continue

            index = int(index)

            if total < index:
                print('Error: Out of range value for index')
                continue

            # index = total - index
            # if index > 0:
            #     index += 1

            conn = sqlite3.connect(args.db)
            cursor = conn.cursor()
            rows = cursor.execute("SELECT MyIndex, MyLevel, MsgTime, Data FROM MsgData")
            for row in rows:
                if index == row[0]:
                    msg = str(row[3])
                # curr += 1
                # if (index) == 0 or (curr == index):
                #   msg = str(row[3])
            conn.close()

            parse.on_parse(msg)

    except KeyboardInterrupt:
        parse.on_destroy()

