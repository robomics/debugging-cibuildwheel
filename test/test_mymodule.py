# Copyright (C) 2023 Roberto Rossini <roberros@uio.no>
#
# SPDX-License-Identifier: MIT

import pytest

import mymodule

class TestClass:
    def test_mymodule(self):
        assert mymodule.call_me() == "Wassup!"
