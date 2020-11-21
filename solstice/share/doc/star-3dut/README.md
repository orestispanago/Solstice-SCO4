# Star-3DUtilityToolkit

This library provides functionalities to create 3D shapes.

## How to build

The library uses [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/#tab-readme) package to build. It also
depends on the [RSys](https://gitlab.com/vaplv/rsys/#tab-readme) library.

First ensure that CMake is installed on your system. Then install the RCMake
package as well as all the RSys library. Then generate the project from the
`cmake/CMakeLists.txt` file by appending to the `CMAKE_PREFIX_PATH` variable
the install directories of its dependencies.

## Release notes

### Version 0.3.1

- Update the version of the RSys dependency to 0.6: replace the deprecated
  `[N]CHECK` macros by the new macro `CHK`.

### Version 0.3

- Add the `s3dut_create_thin_cylinder` function that creates a triangulated
  cylinder. Both ends can be closed or left open.
- Add the `s3dut_create_thick_cylinder` function that creates a thick
  triangulated cylinder. Both ends can be closed or left open.
- Add the `s3dut_create_truncated_sphere` function that creates a triangulated
  UV sphere (possibly) truncated along the Z axis. Truncated ends can be closed
  or left open.
- Add the `s3dut_create_thick_truncated_sphere` function that creates a thick
  triangulated UV sphere (possibly) truncated along the Z axis. Truncated ends
  can be closed or left open.
- Add the `s3dut_create_super_shape` function that creates a triangulated super
  shape.
- Add the `s3dut_create_thick_truncated_super_shape` function that creates a
  thick triangulated super shape (possibly) truncated along the Z axis.
  Truncated ends can be closed or left open.
- Increase min number of slices for `s3dut_create_hemisphere` from 2 to 3.
 
### Version 0.2

- Add the `s3dut_create_hemisphere` function that creates a triangulated UV
  hemisphere oriented along the positive Z axis.

## License

Star-3DUtilityToolkit is Copyright (C) |Meso|Star> 2016-2017
(<contact@meso-star.com>). It is a free software released under the
[OSI](http://opensource.org)-approved GPL v3+ license. You are welcome to
redistribute it under certain conditions; refer to the COPYING file for
details.

