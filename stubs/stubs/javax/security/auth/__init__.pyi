from typing import Any

from java.lang import Object

class Subject(Object):
    def __init__(self, *args: Any) -> None: ...
    @staticmethod
    def callAs(subject: Subject, action: Any) -> Any: ...
    @staticmethod
    def current() -> Subject: ...
