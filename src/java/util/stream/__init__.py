__all__ = ["BaseStream", "Collector", "Gatherer", "Gatherers", "IntStream", "Stream"]

from typing import Any, Iterable, Set

from java.lang import AutoCloseable, Enum, Runnable
from java.util import Iterator, Spliterator
from java.util.function import (
    BiConsumer,
    BiFunction,
    BinaryOperator,
    Consumer,
    Function,
    IntConsumer,
    Supplier,
)


class BaseStream(AutoCloseable):
    def close(self):
        # type: () -> None
        raise NotImplementedError

    def isParallel(self):
        # type: () -> bool
        raise NotImplementedError

    def iterator(self):
        # type: () -> Iterator
        raise NotImplementedError

    def onClose(self, closeHandler):
        # type: (Runnable) -> Any
        raise NotImplementedError

    def parallel(self):
        # type: () -> Any
        raise NotImplementedError

    def sequential(self):
        # type: () -> Any
        raise NotImplementedError

    def spliterator(self):
        # type: () -> Spliterator
        raise NotImplementedError

    def unordered(self):
        # type: () -> Any
        raise NotImplementedError


class Collector(object):

    class Characteristics(Enum):
        @staticmethod
        def values():
            # type: () -> Iterable[Collector.Characteristics]
            pass

    def accumulator(self):
        # type: () -> BiConsumer
        pass

    def characteristic(self):
        # type: () -> Set[Collector.Characteristics]
        pass

    def combiner(self):
        # type: () -> BinaryOperator
        pass

    def finisher(self):
        # type: () -> Function
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> Collector
        pass

    def supplier(self):
        # type: () -> Supplier
        pass


class IntStream(BaseStream):

    class Builder(IntConsumer):
        def accept(self, value):
            # type: (int) -> None
            raise NotImplementedError

        def add(self, t):
            # type: (int) -> IntStream.Builder
            pass

        def build(self):
            # type: () -> IntStream
            raise NotImplementedError

    class IntMapMultiConsumer(object):
        def accept(self, value, ic):
            # type: (int, IntConsumer) -> None
            raise NotImplementedError

    def close(self):
        # type: () -> None
        pass

    def isParallel(self):
        # type: () -> bool
        return True

    def iterator(self):
        # type: () -> Iterator
        pass

    def onClose(self, closeHandler):
        # type: (Runnable) -> Any
        pass

    def parallel(self):
        # type: () -> Any
        pass

    def sequential(self):
        # type: () -> Any
        pass

    def spliterator(self):
        # type: () -> Spliterator
        pass

    def unordered(self):
        # type: () -> Any
        pass


class Stream(BaseStream):

    class Builder(Consumer):
        def accept(self, t):
            # type: (Any) -> None
            raise NotImplementedError

        def add(self, t):
            # type: (Any) -> Stream.Builder
            pass

        def build(self):
            # type: () -> Stream
            raise NotImplementedError

    @staticmethod
    def builder():
        # type: () -> Stream.Builder
        pass

    def close(self):
        # type: () -> None
        pass

    def gather(self, gatherer):
        # type: (Gatherer) -> Stream
        pass

    def isParallel(self):
        # type: () -> bool
        return True

    def iterator(self):
        # type: () -> Iterator
        pass

    def onClose(self, closeHandler):
        # type: (Runnable) -> Any
        pass

    def parallel(self):
        # type: () -> Any
        pass

    def sequential(self):
        # type: () -> Any
        pass

    def spliterator(self):
        # type: () -> Spliterator
        pass

    def unordered(self):
        # type: () -> Any
        pass


class Gatherer(object):
    class Downstream(object):
        def isRejecting(self):
            # type: () -> bool
            raise NotImplementedError

        def push(self, element):
            # type: (Any) -> bool
            raise NotImplementedError

    class Integrator(object):
        def integrate(self, state, element, downstream):
            # type: (Any, Any, Gatherer.Downstream) -> bool
            raise NotImplementedError

        @staticmethod
        def of(integrator):
            # type: (Gatherer.Integrator) -> Gatherer.Integrator
            pass

        @staticmethod
        def ofGreedy(integrator):
            # type: (Gatherer.Integrator) -> Gatherer.Integrator
            pass

    def andThen(self, next):
        # type: (Gatherer) -> Gatherer
        pass

    def combiner(self):
        # type: () -> BinaryOperator
        pass

    @staticmethod
    def defaultCombiner():
        # type: () -> BinaryOperator
        pass

    @staticmethod
    def defaultFinisher():
        # type: () -> BiConsumer
        pass

    @staticmethod
    def defaultInitializer():
        # type: () -> Supplier
        pass

    def finisher(self):
        # type: () -> BiConsumer
        pass

    def initializer(self):
        # type: () -> Supplier
        pass

    def integrator(self):
        # type: () -> Gatherer.Integrator
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> Gatherer
        pass

    @staticmethod
    def ofSequential(*args):
        # type: (*Any) -> Gatherer
        pass


class Gatherers(object):
    @staticmethod
    def fold(supplier, accumulator):
        # type: (Supplier, BiFunction) -> Gatherer
        pass

    @staticmethod
    def mapConcurrent(maxConcurrency, mapper):
        # type: (int, Function) -> Gatherer
        pass

    @staticmethod
    def scan(supplier, accumulator):
        # type: (Supplier, BiFunction) -> Gatherer
        pass

    @staticmethod
    def windowFixed(windowSize):
        # type: (int) -> Gatherer
        pass

    @staticmethod
    def windowSliding(windowSize):
        # type: (int) -> Gatherer
        pass
