# Copyright (C) 2023 Roberto Rossini <roberros@uio.no>
#
# SPDX-License-Identifier: MIT

cmake_minimum_required(VERSION 3.25)
cmake_policy(VERSION 3.25...3.27)
set(CMAKE_POLICY_DEFAULT_CMP0069 NEW)
set(CMAKE_POLICY_DEFAULT_CMP0077 NEW)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_STANDARD 11)

set(CMAKE_CXX_EXTENSIONS OFF)

project(test LANGUAGES CXX)
add_subdirectory(src)
