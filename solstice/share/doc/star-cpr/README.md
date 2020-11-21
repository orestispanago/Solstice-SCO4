# Star-CliPpeR

This library clips triangulated 2D meshes against 2D polygons. Two clipping
operations between the mesh and the clipping region are provided: the
subtraction and the intersection. The former removes the clipping region from
the original mesh while the latter keeps only the mesh part that intersects the
clipping polygon.

## How to build

The library uses [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/#tab-readme) package to build. It also
depends on the
[Clipper](http://www.angusj.com/delphi/clipper.php),
[Polygon](https://gitlab.Com/vaplv/polygon/#tab-readme) and
[RSys](https://gitlab.com/vaplv/rsys/#tab-readme) libraries.

First ensure that CMake is installed on your system. Then install the RCMake
package as well as all the aforementioned prerequisites. Then generate the
project from the `cmake/CMakeLists.txt` file by appending to the
`CMAKE_PREFIX_PATH` variable the install directories of its dependencies.

## Release notes

### Version 0.1.2

- Update CMake module of the Clipper library: on GNU/Linux, make optional the
  debug version of the library.

### Version 0.1.1

- Update the version of the RSys dependency to 0.6: replace the deprecated
  `[N]CHECK` macros by the new macro `CHK`.

## License

Star-Clipper is Copyright (C) |Meso|Star> 2016 (<contact@meso-star.com>). It is
a free software released under the [OSI](http://opensource.org)-approved GPL
v3+ license. You are welcome to redistribute it under certain conditions; refer
to the COPYING file for details.

