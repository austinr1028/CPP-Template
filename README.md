# CPP-Template

Template project that sets up a project to leverage the following technologies:

* CMake
* clang-format (TODO)
* Conan
* Doxygen (TODO)
* Google Test
* Git
* Ninja
* Python 3

## Requirements

Before being able to use this template, you need to have the following packages installed on your system:

* Compiler of your choosing
* Git
* Python 3.7+

## Getting Started

Run the provided configure.py script. This will install all build dependencies in to a python virtual environment at the root of the project dir, named .venv

Generating build directory:

```bash
$ python3 configure.py
...
Installed all project dependencies
$ export PATH=:venv/bin:$PATH #Optional to put cmake in path
$ mkdir bin; cd bin
$ cmake .. -G Ninja -DCMAKE_BUILD_TYPE=<Release, Debug, RelWithDebInfo, MinSizeRel>
...
-- Build files have been written to: */bin
```

**Note:**
OS X users may need to export:

```bash
$ export SDKROOT=$(xcodebuild -version -sdk macosx Path)
```

If using the apple clang compiler

## Compiling and running

From project root:

```bash
$ cmake --build bin --target all
$ bin/test/test
Running main() from gmock_main.cc
[==========] Running 1 test from 1 test case.
[----------] Global test environment set-up.
[----------] 1 test from FactorialTest
[ RUN      ] FactorialTest.Negative
[       OK ] FactorialTest.Negative (0 ms)
[----------] 1 test from FactorialTest (0 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test case ran. (0 ms total)
[  PASSED  ] 1 test.
$ bin/main/main
Hello, world!
```
