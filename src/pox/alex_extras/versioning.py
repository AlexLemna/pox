""" `pox/alex_extras/versioning.py`

A module allowing Pox to report its version number via the 
`PoxVersion` class."""

import importlib.metadata
import json
import re
from dataclasses import dataclass


# TODO: Amend this class's docstrings to explain (or at least link to)
# how setuptools_scm generates a version number and what the more
# complicated version numbers mean.
@dataclass(init=False)
class PoxVersion:
    """A class representing Pox's version number. The most common use of
    this class will be to simply print it as a string via
    `print(PoxVersion())`."""

    version_string: str
    """The version string, which comes either directly or indirectly from
    `setuptools_scm` package. It may be as simple as a three-integer 'SemVer'
    version (like `0.4.1`) a much more complicated, fully localized 
    development version string like `0.4.1.dev0+gf0154ae.d20240229`."""

    is_editable: bool
    """`True` if Pox was installed with `pip install --editable ...`,
    otherwise `False`."""

    is_dirty: bool
    """`True` if the package was installed in editable mode and has 
    uncommitted changes in the working directory. Otherwise, `False`."""

    def __init__(self) -> None:
        """Initializes the PoxVersion instance."""

        # Note that the order is important here:
        #   1. set self.is_editable
        #   2. set self.version_string
        #   3. set self.is_dirty

        self.is_editable = self.__check_if_editable()
        self.version_string = self.__get_version_string()
        self.is_dirty = self.__check_if_dirty()

    def __str__(self) -> str:
        """Implements `str(PoxVersion)`.

        Generates a string in the format `Pox <version> (<optional notes>)`
        where `<optional notes>` indicate if Pox has been installed in
        editable mode and, if so, if Pox's source code includes uncommitted
        changes."""

        if self.is_editable is False:
            s = f"Pox {self.version_string}"
        elif self.is_editable is True and self.is_dirty is False:
            s = f"Pox {self.version_string} (editable)"
        else:
            s = f"Pox {self.version_string} (has uncommitted changes, editable)"
        return s

    def __check_if_editable(self) -> bool:
        """Returns `True` if Pox was installed via Pip's "editable mode"
        (aka development mode). Otherwise, returns `False`.

        [More info on editable mode here.](https://setuptools.pypa.io/en/latest/userguide/development_mode.html)
        """

        # Got inspiration/guidance from https://stackoverflow.com/a/77824551
        metadata = importlib.metadata.Distribution.from_name("pox")
        direct_url_contents: str | None = metadata.read_text("direct_url.json")

        if direct_url_contents:
            e: bool = (
                json.loads(direct_url_contents)
                .get("dir_info", {})
                .get("editable", False)  # Will be True or False
            )
            return e

        else:
            return False

    def __get_version_string(self) -> str:
        """Returns a version string, using whatever method of version
        discovery is most accurate."""

        # Returns something like '0.4.1.dev0+gf0154ae.d20240229'
        if self.is_editable:
            return self.__get_version_string_at_runtime()
        else:
            return self.__get_version_string_from_metadata()

    def __get_version_string_at_runtime(self) -> str:
        """Technically discouraged, but as far as I know there's no other way
        to get the accurate version info in editable mode *except* by doing
        a runtime check, so this is the blessed way to do it.
        - [More info.](https://setuptools-scm.readthedocs.io/en/latest/usage/#at-runtime-strongly-discouraged)
        """

        try:
            import setuptools_scm
        except ImportError as e:
            # if we're having to get the version string at runtime,
            # setuptools_scm *should* be installed. If that's not the case,
            # we're just going to try our best.
            v = "version unknown"
            v += f", approx. {self.__get_version_string_from_metadata()}"
            return v

        v = setuptools_scm.get_version()
        return v

    def __get_version_string_from_metadata(self) -> str:
        """Fetches Pox's version number from its package metadata. This
        will be accurate if Pox was installed "normally", i.e. downloading
        from GitHub and running `pip install .` but it may be inaccurate
        if Pox was installed in editable mode by downloading from GitHub
        and running `pip install --editable`."""

        v = importlib.metadata.version("pox")
        return v

    def __check_if_dirty(self) -> bool:
        """Returns `True` if we're operating in editable mode (development
        mode) and have uncommitted changes in our working directory.
        Otherwise, returns `False`."""

        if self.is_editable is False:
            return False

        # A 'Match' object if the version string ends in
        # +dYYYYMMDD or .dYYYYMMDD, otherwise 'None'
        match = re.search(
            pattern="[\\.\\+]d\\d{8}$",
            string=self.version_string,
        )

        return False if match is None else True
