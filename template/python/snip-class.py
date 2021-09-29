#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: {{_name_}}.py
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"
import pyinspect as pi


class {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}(object):
	def __init__(self{{_cursor_}}):

    def __repr__(self):
        return



def main() -> None:
    pass


if __name__ == "__main__":
    pi.install_traceback()
    main()
