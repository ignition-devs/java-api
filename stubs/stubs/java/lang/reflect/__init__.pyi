from typing import Any, List, Optional, Set, Union

class Type:
    def getTypeName(self) -> Union[str, unicode]: ...

class AccessFlag:
    class Location:
        CLASS: AccessFlag.Location
        FIELD: AccessFlag.Location
        METHOD: AccessFlag.Location
        INNER_CLASS: AccessFlag.Location
        METHOD_PARAMETER: AccessFlag.Location
        MODULE: AccessFlag.Location
        MODULE_REQUIRES: AccessFlag.Location
        MODULE_EXPORTS: AccessFlag.Location
        MODULE_OPENS: AccessFlag.Location
        def flagsMask(
            self, classFileFormatVersion: Optional[ClassFileFormatVersion] = ...
        ) -> int: ...
        def flags(
            self, classFileFormatVersion: Optional[ClassFileFormatVersion] = ...
        ) -> Set[AccessFlag]: ...
        @staticmethod
        def values() -> List[AccessFlag.Location]: ...
        @staticmethod
        def valueOf(name: Union[str, unicode]) -> AccessFlag.Location: ...

    PUBLIC: AccessFlag
    PRIVATE: AccessFlag
    PROTECTED: AccessFlag
    STATIC: AccessFlag
    FINAL: AccessFlag
    SUPER: AccessFlag
    OPEN: AccessFlag
    TRANSITIVE: AccessFlag
    SYNCHRONIZED: AccessFlag
    STATIC_PHASE: AccessFlag
    VOLATILE: AccessFlag
    BRIDGE: AccessFlag
    TRANSIENT: AccessFlag
    VARARGS: AccessFlag
    NATIVE: AccessFlag
    INTERFACE: AccessFlag
    ABSTRACT: AccessFlag
    STRICT: AccessFlag
    SYNTHETIC: AccessFlag
    ANNOTATION: AccessFlag
    ENUM: AccessFlag
    MANDATED: AccessFlag
    MODULE: AccessFlag
    def locations(
        self, classFileFormatVersion: Optional[ClassFileFormatVersion] = ...
    ) -> Set[AccessFlag.Location]: ...
    def mask(self) -> int: ...
    @staticmethod
    def maskToAccessFlags(
        mask: int,
        location: AccessFlag.Location,
        classFileFormatVersion: Optional[ClassFileFormatVersion] = ...,
    ) -> Set[AccessFlag]: ...
    def sourceModifier(self) -> bool: ...
    @staticmethod
    def values() -> List[AccessFlag]: ...
    @staticmethod
    def valueOf(name: Union[str, unicode]) -> AccessFlag: ...

class ClassFileFormatVersion:
    RELEASE_0: ClassFileFormatVersion
    RELEASE_1: ClassFileFormatVersion
    RELEASE_2: ClassFileFormatVersion
    RELEASE_3: ClassFileFormatVersion
    RELEASE_4: ClassFileFormatVersion
    RELEASE_5: ClassFileFormatVersion
    RELEASE_6: ClassFileFormatVersion
    RELEASE_7: ClassFileFormatVersion
    RELEASE_8: ClassFileFormatVersion
    RELEASE_9: ClassFileFormatVersion
    RELEASE_10: ClassFileFormatVersion
    RELEASE_11: ClassFileFormatVersion
    RELEASE_12: ClassFileFormatVersion
    RELEASE_13: ClassFileFormatVersion
    RELEASE_14: ClassFileFormatVersion
    RELEASE_15: ClassFileFormatVersion
    RELEASE_16: ClassFileFormatVersion
    RELEASE_17: ClassFileFormatVersion
    RELEASE_18: ClassFileFormatVersion
    RELEASE_19: ClassFileFormatVersion
    RELEASE_20: ClassFileFormatVersion
    RELEASE_21: ClassFileFormatVersion
    RELEASE_22: ClassFileFormatVersion
    RELEASE_23: ClassFileFormatVersion
    RELEASE_24: ClassFileFormatVersion
    RELEASE_25: ClassFileFormatVersion
    @staticmethod
    def fromMajor(major: int) -> ClassFileFormatVersion: ...
    @staticmethod
    def latest() -> ClassFileFormatVersion: ...
    def major(self) -> int: ...
    def runtimeVersion(self) -> Any: ...
    @staticmethod
    def values() -> List[ClassFileFormatVersion]: ...
    @staticmethod
    def valueOf(arg: Any) -> ClassFileFormatVersion: ...
