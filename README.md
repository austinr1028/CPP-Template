# CPP-Template

## Purpose

The purpose of this repository is to provide a baseline template for new C++ projects. It provides a project based upon industry standard tools, with a focus on ease of use. It supplies everything from source code formatting, a build system with an integrated package manager, unit tests, and more.

The template project is built upon the following technologies:

* CMake
* clang-format (TODO)
* clang-tidy (TODO)
* Conan
* Doxygen (TODO)
* Google Test
* Git
* Ninja
* Python 3
* Travis (TODO)

## Requirements

Before being able to use this template, you need to have the following packages installed on your system:

* Compiler of your choosing
* Git
* Python 3.7+

## Getting Started

Run the provided [configure.py](configure.py) script. This will install all build dependencies in to a python virtual environment at the root of the project dir, named .venv

Generating build directory:

```bash
$ python3 configure.py
...
Installed all project dependencies
$ export PATH=.venv/bin:$PATH #Optional to put cmake in path
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

### Python virtual environment

Build tools are installed installed in to a python virtual environment, located in the `.venv` directory, found in the project root. These tools are specified in the [py_requirements.txt](py_requirements.txt) file. You may choose to just add the `.venv/bin` directory directly to your `PATH` (as seen above), or you can work directly from the virtual environment by activating it, as follows:

```bash
$ . .venv/bin/activate
```

## Adding C/C++ packages

Packages can be brought in through the Conan package manager. They are specified in the [conanfile.txt](conanfile.txt) file ([documentation](https://docs.conan.io/en/latest/reference/conanfile_txt.html)). They can be added as cmake dependencies using the conan.cmake convention "CONAN_PKG::*package_name*" (see gtest usage for an [example](test/CMakeLists.txt)). See the [bincrafters public-conan channel](https://bintray.com/bincrafters/public-conan) for a number of readily available packages.

## License

MIT License for the related source, do as you wish with this project. Hopefully you found it helpful - pull requrests welcome. Any dependencies may have their own respective licenses and you should follow them as appropriate.
