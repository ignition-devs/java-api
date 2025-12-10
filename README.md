# java-api

<!--- Badges --->
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/java-api)](https://pypi.org/project/java-api/)
[![PyPI - Version](https://img.shields.io/pypi/v/java-api)](https://pypi.org/project/java-api/)
[![PyPI - Downloads](https://static.pepy.tech/badge/java-api)](https://pepy.tech/projects/java-api)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ignition-devs/java-api-17/main.svg)](https://results.pre-commit.ci/latest/github/ignition-devs/java-api-17/main)
[![ci](https://github.com/ignition-devs/java-api-17/actions/workflows/ci.yml/badge.svg)](https://github.com/ignition-devs/java-api-17/actions/workflows/ci.yml)
[![Join us on GitHub discussions](https://img.shields.io/badge/github-discussions-informational)](https://github.com/orgs/ignition-devs/discussions)

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

To use java-api, you may install it using the following method.

### Installing with `pip`

> [!NOTE]
> For stub files for this package, look for [`java-api-stubs`].

The preferred method is to install it by running `pip`. It requires Python
2.7.18.

```bash
python2 -m pip install java-api
```

This will install it as package to your Python installation, which will allow
you to call Ignition Scripting functions from Python's REPL, and get code
completion using an IDE such as PyCharm and Visual Studio Code.

```bash
$ python2
Python 2.7.18 (default, Sep 23 2024, 13:23:35)
[GCC Apple LLVM 16.0.0 (clang-1600.0.26.3)] on darwin
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
[`java-api-stubs`]: https://pypi.org/project/java-api-stubs/
[LICENSE]: https://github.com/ignition-devs/java-api-17/blob/main/LICENSE
[Microsoft Open Source Code of Conduct]: https://opensource.microsoft.com/codeofconduct/
[Python 2.7.18]: https://www.python.org/downloads/release/python-2718/
