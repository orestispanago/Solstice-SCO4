# Solstice Solver

The purpose of this library is to integrate the solar flux in complex solar
facilities. It has been developed in the scope of the Solstice project, in
collaboration with the
[Laboratory of Excellence Solstice](http://www.labex-solstice.fr) and the
[PROMES](http://www.promes.cnrs.fr/index.php?page=home-en) laboratory of the
National Center for Scientific Research ([CNRS](http://www.cnrs.fr/index.php)).

## How to build

The Solstice-Solver library relies on the [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/) package to build.
It also depends on the
[RSys](https://gitlab.com/vaplv/rsys/),
[Star-3D](https://gitlab.com/meso-star/star-3d/),
[Star-3DUT](https://gitlab.com/meso-star/star-3dut),
[Star-CPR](https://gitlab.com/meso-star/star-cpr),
[Star-SF](https://gitlab.com/meso-star/star-sf) and
[Star-SP](https://gitlab.com/meso-star/star-sp/) libraries as well as on the
[OpenMP](http://www.openmp.org) 1.2 specification to parallelize its
computations.

First ensure that CMake and a compiler that implements the OpenMP 1.2
specification are installed on your system. Then install the RCMake package as
well as all the aforementioned prerequisites. Finally generate the project from
the `cmake/CMakeLists.txt` file by appending to the `CMAKE_PREFIX_PATH`
variable the install directories of its dependencies.

## Release notes

### Version 0.8

- Register into the estimator the final state of the RNG used during the
  simulation. Add the `ssol_estimator_get_rng_state` function that returns this
  state.

### Version 0.7.3

- Update the version of the RSys and StarSP dependencies. 
- Fix a compilation warning with GCC7 and above.

### Version 0.7.2

- Fix the gaussian sunshape.

### Version 0.7.1

- Fix the creation of a glossy BSDF that uses a pillbox microfacet
  distribution.

### Version 0.7

- Add the Gaussian sun shape.
- Add the microfacet distribution parameter to the mirror material: one can
  choose either the Beckmann or the pillbox distribution.

### Version 0.6.1

- Rename the `ssol_sun_pillbox_set_theta_max` function in
  `ssol_sun_pillbox_set_half_angle`.

### Version 0.6

- Fix the integration for non parallel sun: the angle between the principal sun
  direction and the sampled direction was not correctly taken into account
  leading to a wrong initial weight for the optical paths.
- Fix the integration with shapes having perturbed normals: perturbed normals
  must be taken into account in the bounces of the optical paths only, not in
  the energy computations.
- Fix the distribution of the pillbox sun: the pdf was wrong.
- Fix the `ssol_sun_pillbox_aperture` function and rename it in
  `ssol_sun_pillbox_set_theta_max`. The submitted parameter, i.e. `theta_max`,
  is the angular radius but was treated as the angular diameter.
- Update the `ssol_solve` API: add a parameter that controls the number of
  realisations than can fail before an error occurs.

### Version 0.5

- Improve the performances up to 50% by optimising the allocation of the BSDF
  during the optical paths. Performance gains are mainly observed in situations
  where the optical paths are deep, i.e. when they bounce on many surfaces.

### Version 0.4.2

- Energy conservation property might not be ensured when the optical paths were
  fully absorbed.
- Handle infinite optical paths, i.e. paths that bounces infinitely due to the
  material properties and/or numerical inaccuracies. Use a Russian roulette to
  stop the optical random walk without bias.

### Version 0.4.1

- Fix a wrong "path inconsistency" check. The paths going from a dielectric to
  infinity were wrongly detected as inconsistent.

### Version 0.4

- Add the `SSOL_PATH_ERROR` type used for the paths that travel unforeseen
  mediums.
- Fix the cosine factor estimation that did not take into account the
  shadowed realisations.
- Ensure the energy conservation property for dielectric materials. Previously,
  some energy was lost even for dielectric materials with no absorption.

### Version 0.3

- Full rewrite of the estimated values. The global results report the cosine
  factor, and the overall flux that is: absorbed by the receivers, atmosphere
  or others entities; occluded before it reaches a primary entity; missed
  because it does not reaches any surface. The per receiver results include the
  incoming/absorbed flux in 3 situations: all phenomenons are taken into
  account; the atmosphere is disabled; the material propagate the whole
  incoming flux, i.e. they absorbed nothing.
- Update the `ssol_solve` API. Streamed binary outputs are removed.

### Version 0.2.2

- Fix the estimation of the cosine factor for the  sampled instances: it was
  not correctly reported and was thus always equal to 0.

### Version 0.2

- Add normal maps to describe spatially varying normals in the tangent space of
  the surface.
- Add support of spectral data to the atmosphere and the materials.
- Fix the per primitive irradiance estimate by dividing the result by the area
  of the primitive in order to have watts per square meter.

## Licenses

Solstice-Solver is developed by [|Meso|Star>](http://www.meso-star.com) for the
[National Center for Scientific Research](http://www.cnrs.fr/index.php) (CNRS).
Copyright (C) 2016-2018 CNRS, 2018-2019
[|Meso|Star>](http://www.meso-star.com). It is free software released under the
GPL v3+ license: GNU GPL version 3 or later. You are welcome to redistribute it
under certain conditions; refer to the COPYING file for details.

