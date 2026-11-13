__all__ = ["AccessFlag", "ClassFileFormatVersion", "Type"]

from typing import Any, List, Optional, Set, Union


class Type(object):
    def getTypeName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError


class AccessFlag(object):
    """Represents a JVM access flag.

    Access flags were added in Java 20.
    """

    class Location(object):
        CLASS = None  # type: AccessFlag.Location
        FIELD = None  # type: AccessFlag.Location
        METHOD = None  # type: AccessFlag.Location
        INNER_CLASS = None  # type: AccessFlag.Location
        METHOD_PARAMETER = None  # type: AccessFlag.Location
        MODULE = None  # type: AccessFlag.Location
        MODULE_REQUIRES = None  # type: AccessFlag.Location
        MODULE_EXPORTS = None  # type: AccessFlag.Location
        MODULE_OPENS = None  # type: AccessFlag.Location

        def flagsMask(self, classFileFormatVersion=None):
            # type: (Optional[ClassFileFormatVersion]) -> int
            pass

        def flags(self, classFileFormatVersion=None):
            # type: (Optional[ClassFileFormatVersion]) -> Set[AccessFlag]  # noqa: W505
            pass

        @staticmethod
        def values():
            # type: () -> List[AccessFlag.Location]
            pass

        @staticmethod
        def valueOf(name):
            # type: (Union[str, unicode]) -> AccessFlag.Location
            pass

    PUBLIC = None  # type: AccessFlag
    PRIVATE = None  # type: AccessFlag
    PROTECTED = None  # type: AccessFlag
    STATIC = None  # type: AccessFlag
    FINAL = None  # type: AccessFlag
    SUPER = None  # type: AccessFlag
    OPEN = None  # type: AccessFlag
    TRANSITIVE = None  # type: AccessFlag
    SYNCHRONIZED = None  # type: AccessFlag
    STATIC_PHASE = None  # type: AccessFlag
    VOLATILE = None  # type: AccessFlag
    BRIDGE = None  # type: AccessFlag
    TRANSIENT = None  # type: AccessFlag
    VARARGS = None  # type: AccessFlag
    NATIVE = None  # type: AccessFlag
    INTERFACE = None  # type: AccessFlag
    ABSTRACT = None  # type: AccessFlag
    STRICT = None  # type: AccessFlag
    SYNTHETIC = None  # type: AccessFlag
    ANNOTATION = None  # type: AccessFlag
    ENUM = None  # type: AccessFlag
    MANDATED = None  # type: AccessFlag
    MODULE = None  # type: AccessFlag

    def locations(self, classFileFormatVersion=None):
        # type: (Optional[ClassFileFormatVersion]) -> Set[AccessFlag.Location]  # noqa: W505
        pass

    def mask(self):
        # type: () -> int
        pass

    @staticmethod
    def maskToAccessFlags(mask, location, classFileFormatVersion=None):
        # type: (int, AccessFlag.Location, Optional[ClassFileFormatVersion]) -> Set[AccessFlag]  # noqa: W505
        pass

    def sourceModifier(self):
        # type: () -> bool
        pass

    @staticmethod
    def values():
        # type: () -> List[AccessFlag]
        pass

    @staticmethod
    def valueOf(name):
        # type: (Union[str, unicode]) -> AccessFlag
        pass


class ClassFileFormatVersion(object):
    """Represents a class file format version.

    Class file format versions were added in Java 20.
    """

    RELEASE_0 = None  # type: ClassFileFormatVersion
    RELEASE_1 = None  # type: ClassFileFormatVersion
    RELEASE_2 = None  # type: ClassFileFormatVersion
    RELEASE_3 = None  # type: ClassFileFormatVersion
    RELEASE_4 = None  # type: ClassFileFormatVersion
    RELEASE_5 = None  # type: ClassFileFormatVersion
    RELEASE_6 = None  # type: ClassFileFormatVersion
    RELEASE_7 = None  # type: ClassFileFormatVersion
    RELEASE_8 = None  # type: ClassFileFormatVersion
    RELEASE_9 = None  # type: ClassFileFormatVersion
    RELEASE_10 = None  # type: ClassFileFormatVersion
    RELEASE_11 = None  # type: ClassFileFormatVersion
    RELEASE_12 = None  # type: ClassFileFormatVersion
    RELEASE_13 = None  # type: ClassFileFormatVersion
    RELEASE_14 = None  # type: ClassFileFormatVersion
    RELEASE_15 = None  # type: ClassFileFormatVersion
    RELEASE_16 = None  # type: ClassFileFormatVersion
    RELEASE_17 = None  # type: ClassFileFormatVersion
    RELEASE_18 = None  # type: ClassFileFormatVersion
    RELEASE_19 = None  # type: ClassFileFormatVersion
    RELEASE_20 = None  # type: ClassFileFormatVersion
    RELEASE_21 = None  # type: ClassFileFormatVersion
    RELEASE_22 = None  # type: ClassFileFormatVersion
    RELEASE_23 = None  # type: ClassFileFormatVersion
    RELEASE_24 = None  # type: ClassFileFormatVersion
    RELEASE_25 = None  # type: ClassFileFormatVersion

    @staticmethod
    def fromMajor(major):
        # type: (int) -> ClassFileFormatVersion
        pass

    @staticmethod
    def latest():
        # type: () -> ClassFileFormatVersion
        pass

    def major(self):
        # type: () -> int
        pass

    def runtimeVersion(self):
        # type: () -> Any
        pass

    @staticmethod
    def values():
        # type: () -> List[ClassFileFormatVersion]
        pass

    @staticmethod
    def valueOf(arg):
        # type: (Any) -> ClassFileFormatVersion
        pass
