#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: {{_name_}}.py
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import logging

import pyinspect as pi
from rich.logging import RichHandler

root = logging.getLogger()
if root.handlers:
    for h in root.handlers:
        root.removeHandler(h)()

FORMAT = "%(message)s"
logging.basicConfig(level="INFO",
                    format=FORMAT,
                    datefmt="[%X]",
                    handlers=[RichHandler()])
class {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}(object):
	def __init__(self{{_cursor_}}):

    def __repr__(self):
        return


def main() -> None:
    {{_cursor_}}


if __name__ == "__main__":
    pi.install_traceback()
    main()
