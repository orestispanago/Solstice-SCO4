# Star-ScatteringFunctions

This library provides a set of abstractions to describe the way the
light is scattered at a surface with respect to a geometric optics model. It
defines interfaces to describe Bidirectional Reflectance|Transmittance
Distribution Functions (BRDF & BTDF), microfacet distributions and Fresnel
terms. Several built-in implementation of these interfaces are provided as
specular, lambertian and microfacet reflections, Beckmann and Blinn microfacet
distributions, or dielectric/dielectric and dielectric/conductor Fresnel terms.

Finally, complex scattering functions defines as a combination of several BRDFs
and BTDFs are handled through a Bidirectional Scattering Distribution Function.

## How to build

The library uses [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/#tab-readme) package to build. It also
depends on the
[Star-SP](https://gitlab.com/meso-star/star-sp/#tab-readme) and the
[RSys](https://gitlab.com/vaplv/rsys/#tab-readme) libraries.

First ensure that CMake is installed on your system. Then install the RCMake
package as well as all the aforementioned prerequisites. Finally generate the
project from the `cmake/CMakeLists.txt` file by appending to the
`CMAKE_PREFIX_PATH` variable the install directories of its dependencies.

## Release notes

### Version 0.5

- Add the pillbox microfacet distribution.
- Update the version of the RSys dependency to 0.6: replace the deprecated
  `[N]CHECK` macros by the new macro `CHK`.

### Version 0.4

- Fix the Blinn microfacet distribution.
- Change the microfacet distribution API to no longer require the unused
  outgoing direction parameter.
- Use and require Star-SamPling version 0.5.

### Version 0.3

- A BSDF is no more a composition of BxDFs: the caller writes directly the
  comportment of the BSDF without intermediary abstractions. As a result,
  built-in BxDFs become built-in BSDFs and the BxDF data structure and
  functions are removed from the API.

### Version 0.2

- Fix the thin-dielectric material to ensure the energy conservation property.
- Add the `ssf_specular_dielectric_dielectric_interface` BxDF. This scattering
  function could be built by combining the `ssf_specular_reflection` and the
  `ssf_specular_transmission` BxDFs into a BSDF but such combination does not
  ensure the energy conservation property due to weaknesses into the BSDF
  interface.

## License

Star-ScatteringFunctions is Copyright (C) |Meso|Star> 2016-2017
(<contact@meso-star.com>). It is a free software released under the
[OSI](http://opensource.org)-approved GPL v3+ license. You are welcome to
redistribute it under certain conditions; refer to the COPYING file for
details.

