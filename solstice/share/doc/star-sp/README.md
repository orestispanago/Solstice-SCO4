# Star SamPling

The purpose of this library is to generate [pseudo] random numbers and random
variates. While it is partly based on C++11 random generators, its API remains
pure C.

## How to build

The Star-Sampling library relies on the [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/) packages to build. It also depends
on the [RSys](https://gitlab.com/vaplv/rsys/) library and on random number
generators from C++11 and the
[Random123](https://github.com/DEShawResearch/Random123-Boost/) library.

First ensure that CMake and a C++11 compiler are installed on your system. Then
install the RCMake package as well as the RSys and Random123 libraries. Finally
generate the project from the `cmake/CMakeLists.txt` file by appending to the
`CMAKE_PREFIX_PATH` variable the `<RCMAKE_INSTALL_DIR>`, `<RSYS_INSTALL_DIR>`
and `<RANDOM123_INSTALL_DIR>` directories, where `<RCMAKE_INSTALL_DIR>`,
`<RSYS_INSTALL_DIR>` and `<RANDOM123_INSTALL_DIR>` are the install directories
of the RCMake package and the RSys and Random123 libraries, respectively.

### Microsoft Visual Studio

When building Star-Sampling using Visual Studio, the Star-Sampling library
also depends on the [Boost](http://www.boost.org) random library as a
replacement for the STL libray that is not fully compliant with the C++11
standard on current Microsoft compilers.

For this platform install the Boost random library. Then generate the CMake
project as above, excepted that you need to add the Boost install directory to
the `CMAKE_PREFIX_PATH` variable and to set the `BOOST_INCLUDEDIR` cmake
variable to the directory that contains the `boost` include directory.

## Release notes

### Version 0.8.1

- Fix a possible invalid memory read on proxy allocator clear.

### Version 0.8

- Add the `ssp_ran_sphere_cap_uniform[_local][_float]` random variates that
  uniformly distributes a point onto a unit sphere cap centered in zero.
- Fix the allocation of the `ssp_rng` data structure: the `ssp_rng` structure
  contains a long double attribute that might be not correctly aligned on 16
  bytes.

### Version 0.7

- Add the `ssp_ran_circle_uniform` random variate that uniformly distributes a
  2 dimensional position onto a unit circle.

### Version 0.6

- Add the `ssp_rng_proxy_create2` function that allows to tune the sub sets of
  pseudo random numbers that the proxy generator can use. Pseudo random numbers
  that do not lie in these partitions are skipped by the proxy. Thanks to this
  functionality, on can create several proxies, each generating its own set of
  pseudo random numbers that does not overlap the sequences of the other
  proxies.
- Update the version of the RSys dependency to 0.6: replace the deprecated
  `[N]CHECK` macros by the new macro `CHK`.

### Version 0.5

- Rename the `ssp_ran_uniform_disk` API call into `ssp_ran_uniform_disk_local`.
- Add a more general version of the uniform disk random variate allowing
  users to provide the disk's normal.
- Add a float equivalent for all the already defined double random variates.
- Add some missing pdf API calls.
- Change the API of some random variates that returned the pdf as an additional
  vector component along with the sampled vector (i.e. filling up a vector[4]
  instead of a vector[3]). The pdf is now returned through an optional
  dedicated argument.

### Version 0.4

- Update the API of the random variates to return double precision reals
  rather than single precision values.
- Use the specific prefix `ssp_ranst` to name the state-based random variates.
- Add the piecewise linear and uniform disk random variates.
- Ensure that the single precision version of the canonical uniform
  distribution does not return 1.
- Speed up the canonical uniform distribution.
- Add the `ssp_rng_proxy_write` and `ssp_rng_proxy_read` functions that
  serializes and deserializes the data of the proxy RNG, respectively.

## Licenses

Star-Sampling is Copyright (C) |Meso|Star> 2015-2018
(<contact@meso-star.com>). It is a free software released under the
[OSI](http://opensource.org)-approved CeCILL license. You are welcome to
redistribute it under certain conditions; refer to the COPYING files for
details.

