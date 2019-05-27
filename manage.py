#encoding=utf-8
"""
@version: 1
@author: Duke
@file:manage.py
@time:2019/4/29 9:35 AM
"""

import sys
import management
import commandtools

if __name__ == "__main__":
    commandtools.execute_commands(management, *sys.argv)