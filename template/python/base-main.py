#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: {{_name_}}.py
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


def main() -> None:
    {{_cursor_}}


if __name__ == "__main__":
    pi.install_traceback(enable_prompt=True)
    main()
