# java-api

java-api is a Python package that allows developers to get code completion
for Java 17 API Specification functions and classes in their IDE of choice.

## Table of contents

- [Prerequisites](#prerequisites)
- [Installation and usage](#installation-and-usage)
  - [Installing with pip](#installing-with-pip)
- [Project structure](#project-structure)
  - [Packages](#packages)
- [Contributing](#contributing)
- [Discussions](#discussions)
- [Contributors](#contributors)
- [License](#license)
- [Code of conduct](#code-of-conduct)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Python 2.7.18]

## Installation and usage

To use java-api, you may install it by doing any of the following.

### Installing with `pip`

The preferred method is to install it by running `pip`. It requires Python
2.7.18.

```bash
python2 -m pip install git+https://github.com/ignition-devs/java-api-17.git#subdirectory=java-api
```

This will install it as package to your Python installation, which will allow
you to call Ignition Scripting functions from Python's REPL, and get code
completion using an IDE such as PyCharm and Visual Studio Code.

```bash
$ python2
Python 2.7.18 (default, Nov  9 2020, 16:23:15)
[GCC Apple LLVM 12.0.0 (clang-1200.0.32.21)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from __future__ import print_function
>>> import java.lang
>>> print(java.lang.__doc__)
Provides classes that are fundamental to the design of the Java
programming language.

>>> quit()
```

And to uninstall:

```bash
python2 -m pip uninstall java-api
```

## Project structure

### Packages

This project consists of the following packages:

- [java](#javajavax)
- [javax](#javajavax)

#### java/javax

These packages include supporting Java classes and interfaces. For more
information, see documentation here:
<https://docs.oracle.com/en/java/javase/17/docs/api/index.html>.

## Contributing

See [CONTRIBUTING.md].

## Discussions

Feel free to post your questions and/or ideas at [Discussions].

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of contributors can be found here: [CONTRIBUTORS].

## License

See the [LICENSE].

## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct].

<!-- Links -->
[CONTRIBUTING.md]: https://github.com/ignition-devs/java-api-17/blob/main/CONTRIBUTING.md#contributing-to-java-api
[CONTRIBUTORS]: https://github.com/ignition-devs/java-api-17/graphs/contributors
[Discussions]: https://github.com/orgs/ignition-devs/discussions
[LICENSE]: https://github.com/ignition-devs/java-api-17/blob/main/LICENSE
[Microsoft Open Source Code of Conduct]: https://opensource.microsoft.com/codeofconduct/
[Python 2.7.18]: https://www.python.org/downloads/release/python-2718/
