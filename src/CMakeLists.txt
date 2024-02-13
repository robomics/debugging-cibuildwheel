# Copyright (C) 2024 Roberto Rossini <roberros@uio.no>
#
# SPDX-License-Identifier: MIT

find_package(
  Python 3.8
  COMPONENTS Interpreter Development.Module
  REQUIRED)

set(PYBIND11_NEWPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(
  _mymodule
  MODULE
  mymodule.cpp)

install(TARGETS _mymodule LIBRARY DESTINATION mymodule)
