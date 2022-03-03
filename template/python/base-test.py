#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Vivian Sedov
#
# File Name: {{_name_}}.py
__author__ = "Vivian Sedov"
__email__ = "viv.sv@hotmail.com"

import logging

import pytest
from rich.logging import RichHandler
from termcolor import colored

root = logging.getLogger()
if root.handlers:
    for h in root.handlers:
        root.removeHandler(h)()

FORMAT = "%(message)s"
logging.basicConfig(level="INFO",
                    format=FORMAT,
                    datefmt="[%X]",
                    handlers=[RichHandler()])


@pytest.fixture()
def resource() -> {{_input_: class_name}}:
    print(colored("Setup Outer Function Call", "magenta", "on_grey"))

    yield {{_cursor_}}()

    print(colored("Teardown Outer Function Call", "magenta", "on_grey"))


@pytest.mark.usefixtures("resource")
class TestArray:

    @classmethod
    def setup_class(cls) -> None:
        print(
            colored(
                f"Setup Class : Start : class -> {cls.__name__} execution,green"
            ))

    @classmethod
    def teardown_class(cls) -> None:
        print(
            colored(
                f"Setup Class : Start : class -> {cls.__name__} execution,green"
            ))

    def test_case_1(self, resource: resource) -> None:
        pass
