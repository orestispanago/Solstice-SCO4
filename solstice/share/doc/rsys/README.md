# RSys

C89 library defining several basic components helpful in the development of C
libraries/applications. Among others, it provides macros that describe the host
environment (OS, compiler, etc.) several low level functionalities (thread,
timer, ref counter, etc.), generic containers (dynamic array, hash table, etc.)
and basic mathematics (linear algebra, quaternions, etc.)

## How to build

The RSys library uses [CMake](http://www.cmake.org) and the
[RCMake](https://gitlab.com/vaplv/rcmake/#tag-readme) package to build. First,
install the RCMake package in a given `<RCMAKE_DIR>` directory. Then, generate
the CMake project from the `cmake/CMakeLists.txt` file by appending the
`<RCMAKE_DIR>` directory to the `CMAKE_PREFIX_PATH` variable. The resulting
project can be now edited, built, tested and installed as any CMake project.

## Release notes

### Version 0.7.1

- Add the FALLTHROUGH macro that disables compilation warning on switch
  statement fallthrough.
- Fix a possible wrong return code in the set routine of the hash tables.

### Version 0.7

- Add the `res_to_cstr` function that returns a string describing the submitted
  result code.
- Add the `SIMD_AVX` macro that is defined if the AVX instruction set is
  available on the host machine.
- Fix the aligned allocation of the LIFO allocator: the returned address was
  not necessarily aligned on the expected value.
- Fix the `search_lower_bound` algorithm.
- Fix a compilation error when RSys was linked against a version of the GNU C
  Library less than 2.17.

### Version 0.6.1

- Fix the detection of a 64-bits architecture on the CL compiler.

### Version 0.6

- Remove the `big_buffer` container. Its implementation was awful and it was
  thus useless.
- Add the read/write mutex API and provide an implementation with POSIX
  threads.
- Add the `CHK` macro. It replaces the `[N]CHECK` macros that become
  deprecated.

### Version 0.5

- Add the `big_buffer` container, i.e. out of core dynamic array of POD data.
- Update the `clock_time` API: the `time_<add|current|sub>` functions
  return a pointer toward the result.
- Add the `time_zero` function that cleans-up the submitted time.
- Add a Last In First Out (LIFO) allocator. It uses a pre-allocated memory pool
  to store a stack of allocated memory blocks. A memory block is allocated on
  top of the stack. On "free" invocation, it is marked as freed but it is
  effectively removed from the allocated memory when it lies on top of the
  stack.

### Version 0.4

- Add the `double2`, `double3`, `double4`, `double33`, `double22` and
  `double44` data types that provide the same functionalities of their `float`
  alternative.
- Add the `purge` function to the hash table and the dynamic array data
  structures. This function not only resets the state of the structure, as the
  `clear` function, but also frees its internal memory.
- Implement a new image API that provides and explicit image data structure.
  The old API is still available but is deprecated.

## License

RSys is Copyright (C) 2013-2018 Vincent Forest (vaplv@free.fr). It is a free
software released under LGPL v3+ license. You are welcome to redistribute it
under certain conditions; refer to the COPYING files for details.

