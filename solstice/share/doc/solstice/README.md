# Solstice

The purpose of this program is to compute the total power collected by a
concentrated solar plant, and to evaluate various efficiencies for each primary
reflector: it computes losses due to cosine effect, to shadowing and
masking, to orientation and surface irregularities, to reflectivity and to
atmospheric transmission. The efficiency for each one of these effects is
subsequently computed for each reflector, which provides insightful information
when looking for the optimal design of a concentrated solar plant. Note that
Solstice relies on Monte-Carlo method, which means that every result is
provided with its numerical accuracy.

In addition of the aforementioned computations, Solstice can render an image of
the solar plant, either with a simple ray-caster or with a path-tracing
algorithm that correctly handles the materials of the scene.

Solstice is designed to handle complex solar plants: any number of reflectors
can be specified (planes, conics, cylindro-parabolic, etc.) and positioned in
3D space, with a possibility for 1-axis and 2-axis auto-orientation with
respect to the sun direction. CAO geometries can be added to the solar plant
thanks to the support of the STereo Lithography file format. Multiple materials
can be used, as long as the relevant physical properties are provided (matte,
mirror, dielectric, etc.). Spectral effects are also taken into account: it is
possible to define the spectral distribution of any physical property,
including the input solar spectrum and the absorption of the atmosphere, at any
spectral resolution.

Solstice has been developed in the scope of the Solstice project, in
collaboration with the
[Laboratory of Excellence Solstice](http://www.labex-solstice.fr) and the
[PROMES](http://www.promes.cnrs.fr/index.php?page=home-en) laboratory of the
National Center for Scientific Research ([CNRS](http://www.cnrs.fr/index.php)).
Refer to the Solstice man pages for more informations on the provided
functionalities.

## How to build

This program relies on the [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/) packages to build.
It also depends on the
[LibYAML](http://pyyaml.org/wiki/LibYAML),
[RSys](https://gitlab.com/vaplv/rsys/),
[Solstice-Anim](https://gitlab.com/meso-star/solstice-anim/),
[Solstice-Solver](https://gitlab.com/meso-star/solstice-solver/),
[Star-3DUT](https://gitlab.com/meso-star/star-3dut/),
[Star-SP](https://gitlab.com/meso-star/star-sp/) and
[Star-STL](https://gitlab.com/meso-star/star-stm/) libraries.
The documentation is written in
[AsciiDoc](http://www.methods.co.nz/asciidoc/) text format and relies on its
tool suite to generate HTML and/or ROFF man pages. If the AsciiDoc tools cannot
be found, the documentation will not be built.

First ensure that CMake is installed on your system. Then install the RCMake
package as well as the aforementioned prerequisites. Finally generate the
project from the `cmake/CMakeLists.txt` file by appending to the
`CMAKE_PREFIX_PATH` variable the install directories of its dependencies. The
resulting project can be edited, built, tested and installed as any CMake
project. Refer to the [CMake](https://cmake.org/documentation) for further
informations on CMake.

## Release notes

### Version 0.9

- Add the `-G` option that saves and restores the state of the random number
  generator. This option can be used to ensure the statistical independence
  between successive runs.

### Version 0.8.2

- Fix man pages: the -D option of the solstice CLI was wrongly documented. The
  zenith and elevation angles were sometimes inverted.
- Bump version of the StarSP dependency to 0.8.

### Version 0.8.1

- Fix the VTK of the receiver map: the receiver map was written as `double`
  while the type notified in the VTK file was `float`. This might produce
  errors on loading of the resulting VTK file. The VTK data type is now set to
  `double` to make it consistent with the type of the written values.

### Version 0.8

Add the support of per-triangle absorbed flux density. The `per_primitive`
attribute of the receiver file format controls which flux densities to output
for each triangle of a receiver. Its value can be:

- `NONE`: no per-triangle flux density is computed, i.e. no receiver map is
  output for the receiver. It was the comportment of the previous version of
  Solstice when the `per_primitive` flag was undefined or was set to 0.
- `INCOMING`: output the estimate of the per-triangle incoming flux density.
  It was the comportment of the previous version of Solstice when the
  `per_primitive` flag was set to 1.
- `ABSORBED`: output the estimate of the per-triangle absorbed flux density.
- `INCOMING_AND_ABSORBED`: output both the estimates of incoming and absorbed
  flux density for each triangle of the receiver.

### Version 0.7.1

- Replace the `roughness` parameter of the mirror material by the
  `slope_error` parameter.
- Improve the documentation of the sun direction.
- Ensure that the per-receiver results are sorted according to the order of the
  receivers as listed in the submitted receiver file.

### Version 0.7

- Add the `gaussian` sun shape.
- Add the `microfacet` attribute to the mirror material. It controls the normal
  distribution of the microfacets when the mirror roughness is not null. The
  supported distributions are `BECKMANN` and `PILLBOX`.

### Version 0.6.1

- Fix the solstice-input man page. The `extinction` parameter of the medium and
  the atmosphere was named `absorption`.
- Rename the pillbox `theta_max` parameter in `half_angle`.

### Version 0.6

- Rename the `absorption` parameter of the medium and the atmosphere in
  `extinction`.
- Add several global and per-receiver estimations. The outputs now fully
  describe the incoming and absorbed fluxes: overall flux, flux without
  material loss, flux without atmospheric loss, material losses and atmospheric
  losses.
- Rename the pillbox `aperture` parameter in `theta_max`.
- Fix the distribution of the pillbox sun: the pdf was wrong and its angular
  parameter was internally used as an angular diameter while it is a angular
  radius.
- Fix the solver for non parallel sun: the angle between the principal sun
  direction and the sampled direction was not correctly taken into account
  leading to a wrong initial weight for the optical paths.
- Fix the solver with shapes having perturbed normals: perturbed normals
  must be taken into account in the bounces of the optical paths only, not in
  the energy computations.

### Version 0.5

- Improve the performances of the solver up to 50% in situations where the
  radiative random walks bounce on many surfaces.

### Version 0.4.1

- Update the name of the output data in the solstice-output man page.
- Fix an issue in "dump geometry" mode, i.e. option `-g`. Solstice might fail
  to export the solar plant geometry due to a wrong constraint on the pivots.

### Version 0.4

- Update the color of the paths output with the `-p` option. A path is blue,
  turquoise or yellow if it reaches a receiver, misses the receivers or is
  occluded before it reaches a primary reflector, respectively.
- Add a new type of paths tracked with the `-p` option: a path is red if it
  travels unforeseen mediums.
- Correctly handle the `stacks` parameter of the cylinder.

### Version 0.3

- Fix several issues in the output results. Refer to the Solsice-Solver 0.3
  release notes for more informations.
- Add the `--version` option.
- Update the man pages to fix some issues and improve the output documentation.

### Version 0.2.3

- Update the solstice-input file format. The anchor and entity name cannot
  contain spaces or tabulations anymore.
- Fix the reported sun directions in the solstice-output. For each submitted
  sun direction, solstice correctly output its Cartesian coordinates but always
  wrote the azimuthal and elevation angles of the first direction.
- Update the solstice-output map page: add the missing `<efficiency>` grammar
  rule and fix the definition of the `<map-side-data>` grammar rule.

### Version 0.2.2

- Fix how the AsciiDoc tool suite is looking for on Windows; it was never found
  and consequently the documentation was not generated.

### Version 0.2.1

- Fix the install target on Windows: copy the solstice runtime libraries in the
  solstice installation path.

### Version 0.2

- Add the support of an optional normal map to the materials. It defines
  spatially varying normals in the tangent space of the surface. Currently,
  only the quadric surfaces are parameterizable: using a normal mapped material
  on the other shapes will produce unforeseen behaviors.
- Add the support of spectral data to the materials: a material attribute can be
  either a scalar or follow a spectral distribution.
- Add an optional atmospheric absorption after the first reflection of the light
  path; the sun description includes the atmospheric effect before the first
  reflector.
- Write the man pages of the Solstice command line and its associated file
  formats.
- Add the verbose option `-v`.
- Update the output format of the simulation.

## License

Solstice is developed by [|Meso|Star>](http://www.meso-star.com) for the
[National Center for Scientific Research](http://www.cnrs.fr/index.php) (CNRS).
Copyright (C) 2016-2018 CNRS, 2018-2019
[|Meso|Star>](http://www.meso-star.com). It is free software released under the
GPL v3+ license: GNU GPL version 3 or later. You are welcome to redistribute it
under certain conditions; refer to the COPYING file for details.

