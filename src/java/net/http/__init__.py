__all__ = ["HttpClient", "HttpRequest", "HttpResponse"]

from typing import TYPE_CHECKING, Optional

from java.lang import Object

if TYPE_CHECKING:
    from java.time import Duration


class HttpResponse(object):
    def connectionLabel(self):
        # type: () -> Optional[str]
        pass


class HttpClient(Object):
    def awaitTermination(self, duration):
        # type: (Duration) -> bool
        pass

    def close(self):
        # type: () -> None
        pass

    def isTerminated(self):
        # type: () -> bool
        pass

    def shutdown(self):
        # type: () -> None
        pass

    def shutdownNow(self):
        # type: () -> None
        pass


class HttpRequest(Object):
    pass
