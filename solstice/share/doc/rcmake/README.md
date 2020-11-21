# CMake helper scripts

This code base provides [CMake](http://www.cmake.org) scripts and templates to
help in the developement of C or C++ libraries/applications with CMake.
Currently, GCC, MinGW and the Microsoft CL compilers are supported.

The main code base entry point is the `rcmake.cmake` file that defines the
compiler flags and several helper functions. The `toolchain_<COMPILER>.cmake`
scripts are CMake toolchain files used to
[cross-compile](http://www.cmake.org/Wiki/CMake_Cross_Compiling) a C program on
a given `COMPILER`. The files with the `*.in` suffix are CMake or C templates
internally used by RCMake to generate project specific files.

## Install

The code base relies on the CMake toolchain. To install it, generate the
project from the `CMakeLists.txt` file with the `CMAKE_INSTALL_PREFIX` set to
the expected install directory and then invoke the `install` target on the
resulting project (Refer to the CMake
[documentation](http://www.cmake.org/documentation) for further informations).

## Quick start

To use the RCMake package, add the following lines to your `CMakeLists.txt`

    find_package(RCMake REQUIRED)
    set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH} ${RCMAKE_SOURCE_DIR}")
    include(rcmake)

and generate your project by appending the `<INSTALL_DIR>` directory
to the `CMAKE_PREFIX_PATH` variable where `INSTALL_DIR` is the directory in
which RCMake is installed.

## Release notes

### Version 0.4

- Update the CMake config template: clean up the code and setup the
  `INTERFACE_INCLUDE_DIRECTORIES` CMake properties to the imported target. It
  is thus no more necessary to append the include directories of the imported
  target for the projects that links against this target.

## License

RCMake is Copyright (C) 2013-2017 Vincent Forest (vaplv@free.fr). It is a free
software released under the [OSI](https://opensource.org)-approved GPL v3+
license. You are welcome to redistribute it under certain conditions; refer to
the COPYING file for details.

