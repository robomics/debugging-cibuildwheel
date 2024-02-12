// Copyright (C) 2024 Roberto Rossini <roberros@uio.no>
//
// SPDX-License-Identifier: MIT

#include <pybind11/pybind11.h>

std::string call_me() { return "Wassup!"; }

PYBIND11_MODULE(mymodule, m) { m.def("call_me", &call_me); }
