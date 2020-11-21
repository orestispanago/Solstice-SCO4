# Polygon

This small C89 library triangulates simple polygons, i.e. polygons whose their
non consecutive edges does not intersect. It relies on the ear-clipping variant
of Xianshu Kong et al. presented in "The Graham Scan Triangulates Simple
Polygons".

## How to build

The library uses [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/#tab-readme) package to build. It also
depends on the [RSys](https://gitlab.com/vaplv/rsys/#tab-readme) library.
First, install the RCMake package and the RSys library. Then, generate the
project from the cmake/CMakeLists.txt file by appending the RCMake and RSys
install directories to the `CMAKE_PREFIX_PATH` variable. The resulting project
can be edited, built, tested and installed as any CMake project.

## Release notes

### Version 0.1.2

- Update the version of the RSys dependency to 0.6: replace the deprecated
  `[N]CHECK` macros by the new macro `CHK`.

## License

Polygon is Copyright (C) 2014-2017 Vincent Forest (vaplv@free.fr). It is a free
software released under the [OSI](https://opensource.org)-approved GPL v3+
license. You are welcome to redistribute it under certain conditions; refer to
the COPYING file for details.

