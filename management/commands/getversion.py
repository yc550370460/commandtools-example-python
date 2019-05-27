#encoding=utf-8
"""
@version: 1
@author: Duke
@file:getversion.py
@time:2019/4/29 9:32 AM
"""

from common.common import VERSION
import sys


def execute(*args):
    sys.stdout.write("project version:%s \n" % VERSION)