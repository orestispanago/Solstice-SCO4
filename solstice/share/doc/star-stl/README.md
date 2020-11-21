# Star STereo Lithography

This library loads stl file formats. Currently, only the stl ASCII format is
supported.

## How to build

The library uses [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/#tab-readme) package to build. It also
depends on the [RSys](https://gitlab.com/vaplv/rsys/#tab-readme) library.
First, install the RCMake package and the RSys library. Then, generate the
project from the cmake/CMakeLists.txt file by appending the RCMake and the RSys
install directories to the `CMAKE_PREFIX_PATH` variable. The resulting project
can be edited, built, tested and installed as any CMake project.

## Release notes

### Version 0.3.2

- Update the version of the RSys dependency to 0.6: replace the deprecated
  `[N]CHECK` macros by the new macro `CHK`.

## License

Star-STL is Copyright (C) |Meso|Star> 2015-2016 (<contact@meso-star.com>). It
is a free software released under the [OSI](http://opensource.org)-approved
CeCILL license. You are welcome to redistribute it under certain conditions;
refer to the COPYING files for details.

