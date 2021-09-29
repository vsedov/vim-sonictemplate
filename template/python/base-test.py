#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: {{_name_}}.py
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pytest
from termcolor import colored


@pytest.fixture()
def resource() -> {{_input_: class_name}}:
    print(colored("Setup Outer Function Call", "magenta", "on_grey"))

    yield {{_cursor_}}()

    print(colored("Teardown Outer Function Call", "magenta", "on_grey"))


@pytest.mark.usefixtures("resource")
class TestArray:
    @classmethod
    def setup_class(cls) -> None:
        print(colored(f"Setup Class : Start : class -> {cls.__name__} execution,green"))

    @classmethod
    def teardown_class(cls) -> None:
        print(colored(f"Setup Class : Start : class -> {cls.__name__} execution,green"))

    def test_case_1(self, resource: resource) -> None:
        pass
