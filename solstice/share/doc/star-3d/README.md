# Star 3D

## Overview

Star-3D is a C/C++ library whose purpose is to manage a virtual environment
composed of triangular meshes. The resulting virtual world can then be
ray-traced and sampled, providing an efficient way to deal with geometric data
of arbitrary 3D contents. In addition of purely geometric data, user defined
per vertex data can be setup, allowing the definition of attributes that
spatially vary over the geometry surface. To ensure high ray-tracing
efficiency, the Star-3D ray-tracing back-end relies on the [Intel(R) Rendering
Framework](https://software.intel.com/en-us/rendering-framework):
[Embree](https://embree.github.io) that provides several ray-tracing kernels
optimized for a wide range of data workloads. The target users of Star-3D are
thus programmers that have to efficiently deal with complex 3D environment as
numerical simulation engineers, researchers in complex systems or graphics
programmers.

The main concept exposed by the Star-3D C API are *shapes*. A *shape*
represents a 3D object whose data is defined by the user and can be updated at
any time. A 3D environment is built by attaching one or several *shapes* to a
*scene*. To access the *scene* data through sampling, ray-tracing or indexing,
one have to create a *scene view* that commits the current *scene* geometry
as the geometry of the *view*. A *scene* can also be instantiated into one or
several *shapes*, each with its own attributes (e.g. position, orientation,
etc.). Since the *scene* geometry is stored once even though it is
instantiated several times, this feature can be used to create extremely
complex environment with a low memory footprint.

Star-3D is currently used in several softwares dealing with complex arbitrary
3D contents, ranging from graphics applications and thermal simulations to
electromagnetism. Please refer to these projects for informations on their
purpose.

  * [High-Tune: RenDeRer](https://gitlab.com/meso-star/htrdr.git)
  * [Solstice-Solver](https://gitlab.com/meso-star/solstice-solver.git)
  * [Star-4V/S](https://gitlab.com/meso-star/star-4v_s.git)
  * [Star-Display](https://gitlab.com/meso-star/star-display.git)
  * [Star-GebhartFactor](https://gitlab.com/meso-star/star-gf.git)
  * [Star-Schiff](https://gitlab.com/meso-star/star-schiff.git)

## Install

### Pre-requisites

Star-3D is compatible GNU/Linux as well as Microsoft Windows 7 and later, both
in 64-bits. It was successfully built with the [GNU Compiler
Collection](https://gcc.gnu.org) (versions 4.7 and later) as well as with
Microsoft Visual Studio 2015. It relies on [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/) package to build. It also depends on
the [RSys](https://gitlab.com/vaplv/rsys/) and
[Embree](https://embree.github.io/) libraries.

### How to build

First ensure that CMake and a C/C++ compiler is installed on your system. Then
install the [RCMake](https://gitlab.com/vaplv/rcmake.git) package as well as
the [RSys](https://gitlab.com/vaplv/rsys.git) and
[Embree](https://embree.github.io) libraries. Finally generate the project from
the `cmake/CMakeLists.txt` file by appending to the `CMAKE_PREFIX_PATH`
variable the `<RCMAKE_DIR>`, `<RSYS_DIR>` and `<EMBREE_DIR>`
directories, where `<RCMAKE_DIR>`, `<RSYS_DIR>` and `<EMBREE_DIR`> are the
install directories of the RCMake package, the RSys and the Embree libraries,
respectively. The resulting project can be edited, built, tested and installed
as any CMake project (Refer to the [CMake
documentation](https://cmake.org/documentation) for further informations on
CMake).

Example on a GNU/Linux system:

    ~ $ git clone https://gitlab.com/meso-star/star-3d.git
    ~ $ mkdir star-3d/build && cd star-3d/build
    ~/star-3d/build $ cmake -G "Unix Makefiles" \
    > -DCMAKE_PREFIX_PATH="<RCMAKE_DIR>;<RSYS_DIR>;<EMBREE_DIR>" \
    > -DCMAKE_INSTALL_PREFIX=<STAR3D_INSTALL_DIR> \
    > ../cmake
    ~/star-3d/build $ make && make test
    ~/star-3d/build $ make install

with `<STAR3D_INSTALL_DIR>` the directory in which Star-3D is going to be
installed.

## Quick Start

Once installed, the Star-3D library and its associated headers are deployed,
providing the whole environment required to develop C/C++ applications with
Star-3D. The `<STAR3D_INSTALL_DIR>/include/star/s3d.h` header defines the
Star-3D Application Programming Interface (API). Refer to this
[file](https://gitlab.com/meso-star/star-3d/blob/master/src/s3d.h) for the API
reference documentation.

A Star-3D [CMake
package](https://cmake.org/cmake/help/v3.5/manual/cmake-packages.7.html) is
also installed to facilitate the use of Star-3D in projects relying on the
CMake build system. For instance, the following `CMakeLists.txt` file uses the
Star-3D package to build an executable relying on the Star-3D library.

    project(my_project C)

    # Use the Star-3D CMake package
    find_package(Star3D REQUIRED)

    # Define the program to build
    add_executable(my_program main.c)

    # Link the program against Star-3D
    target_link_libraries(my_program Star3D)

This `CMakeLists.txt` is then used to generate the target project as, for
instance, on a GNU/Linux system:

    cmake -G "Unix Makefiles" -DCMAKE_PREFIX_PATH="<STAR3D_INSTALL_DIR>" <MY_PROJECT_DIR>

with `<STAR3D_INSTALL_DIR>` the install directory of Star-3D and
`<MY_PROJECT_DIR>` the location of the `CMakeLists.txt` file.

## Release notes

### Version 0.6

- Migrate the ray-tracing back-end from Embree2 to Embree3.

### Version 0.5.1

- Fix a compilation issue on VC2017.

### Version 0.5

- Add the support of spherical shapes. A sphere is composed of one primitive
  that can be sampled and/or ray-traced as any other primitives of the scene.
  Hit filtering is also fully supported.

### Version 0.4.2

- Update the version of the RSys dependency to 0.6: replace the deprecated
  `[N]CHECK` macros by the new macro `CHK`.

### Version 0.4.1

- Fix the `s3d_scene_view` consistency when it is created from a scene
  containing instances: the geometries might be not correctly synchronised and
  thus could be outdated.

### Version 0.4

- Implement the `s3d_scene_view` API; it replaces the
  `s3d_scene_<begin|end>_session` functions that were removed. A view registers
  the state of the scene from which it is created. It is used to retrieve the
  scene data through ray-tracing, sampling or indexing. Several views can be
  created on the same scene.
- Add the possibility to attach a same shape to several scenes.
- Fix a memory overconsumption with instantiated shapes: the instantiated
  back-end data were copied rather than shared.
- Add the `s3d_scene_shapes_count` function that returns the overall number of
  shapes in the scene.
- Add the `s3d_instance_set_transform` and `s3d_instance_transform` functions
  that sets or gets the transformation matrix of the instance, respectively.
- Add the `s3d_primitive_get_transform` function that gets the transformation
  matrix of a primitive.
- Add the `s3d_primitive_has_attrib` function that returns if a primitive has a
  specific attribute or not.
- Add the `s3d_triangle_get_vertex_attrib` function that retrieves the
  vertex attributes of a triangular primitive.

## License

Star-3D is free software copyright (C) 2015-2019 |Meso|Star>
(<contact@meso-star.com>). It is released under the CeCILLv2.1 license. You are
welcome to redistribute it under certain conditions; refer to the COPYING files
for details.

