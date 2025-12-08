# java-api-stubs

This package contains a collection of [stubs] for [`java-api`]. These
files were generated using `mypy`'s [`stubgen`].

## Installation and usage

To use java-api-stubs, you may install it with `pip`. It requires Python
3.7+ through 3.12.

> [!WARNING]
> Python 3.13 will not be supported.

```sh
python3 -m pip install \
    git+https://github.com/ignition-devs/java-api-17.git#subdirectory=java-api-stubs \
    "mypy[python2]==0.971"
```

To run `mypy` against your code, execute the following command passing the
source directory (typically `src`) or a single file:

```sh
mypy --py2 src
```

Or

```sh
mypy --py2 code.py
```

## Contributing

See [CONTRIBUTING.md].

## Discussions

Feel free to post your questions and/or ideas at [Discussions].

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of [contributors].

## License

See the [LICENSE].

## Code of conduct

See [CODE_OF_CONDUCT.md].

<!-- Links -->
[CODE_OF_CONDUCT.md]: https://github.com/ignition-devs/.github/blob/main/CODE_OF_CONDUCT.md
[CONTRIBUTING.md]: https://github.com/ignition-devs/java-api-17/blob/main/CONTRIBUTING.md
[contributors]: https://github.com/ignition-devs/java-api-17/graphs/contributors
[Discussions]: https://github.com/orgs/ignition-devs/discussions
[`java-api`]: https://github.com/ignition-devs/java-api-17
[LICENSE]: https://github.com/ignition-devs/java-api-17/blob/main/LICENSE
[`stubgen`]: https://coatl-mypy.readthedocs.io/en/v0.971/stubgen.html
[stubs]: https://www.python.org/dev/peps/pep-484/
