# Copyright (C) 2024 Roberto Rossini <roberros@uio.no>
#
# SPDX-License-Identifier: MIT

find_package(
  Python 3.8
  COMPONENTS Interpreter Development.Module
  REQUIRED)

find_package(pybind11 REQUIRED HINTS "${Python3_SITELIB}/pybind11/")

pybind11_add_module(
  mymodule
  MODULE
  mymodule.cpp)
