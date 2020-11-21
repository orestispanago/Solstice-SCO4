# Solstice Animation

The purpose of this library is to compute the positioning of the constituents
of a solar facility. It has been developed in the scope of the Solstice project,
in collaboration with the
[Laboratory of Excellence Solstice](http://www.labex-solstice.fr) and the
[PROMES](http://www.promes.cnrs.fr/index.php?page=home-en) laboratory of the
National Center for Scientific Research ([CNRS](http://www.cnrs.fr/index.php)).

## How to build

The Solstice-Anim library relies on the [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/) package to build.
It also depends on the [RSys](https://gitlab.com/vaplv/rsys/) and on the
[OpenMP](http://www.openmp.org) 1.2 specification to parallelize its
computations.

First ensure that CMake and a compiler that implements the OpenMP 1.2
specification are installed on your system. Then install the RCMake package as
well as all the aforementioned prerequisites. Finally generate the project from
the `cmake/CMakeLists.txt` file by appending to the `CMAKE_PREFIX_PATH`
variable the install directories of its dependencies.

## Release notes

### Version 0.2.2

- Fix a compilation issue that prevented building tests.

### Version 0.2.1

- Update the version of the RSys dependency to 0.6: replace the deprecated
  `[N]CHECK` macros by the new macro `CHK`.

### Version 0.2

- Update the `sanim_node_visit_tree` function: the submitted sun direction may
  be NULL. In this case, the pivot constraints are not resolved during the tree
  traversal.

## Licenses

Solstice-Anim is developed by [|Meso|Star>](http://www.meso-star.com) for the
[National Center for Scientific Research](http://www.cnrs.fr/index.php) (CNRS).
It is a free software copyright (C) CNRS 2016-2017 and it is released under the
[OSI](http://opensource.org)-approved GPL v3+ license. You are welcome to
redistribute it under certain conditions; refer to the COPYING file for
details.

