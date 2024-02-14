from abc import ABC, abstractmethod


class Parrot(ABC):

    BASE_SPEED = 12.0

    @abstractmethod
    def speed(self) -> float | int:
        raise NotImplementedError()

    @abstractmethod
    def cry(self) -> str:
        raise NotImplementedError()


class EuropeanParrot(Parrot):

    def speed(self) -> float | int:
        return self.BASE_SPEED

    def cry(self) -> str:
        return "Sqoork!"


class AfricanParrot(Parrot):
    LOAD_FACTOR = 9.0

    def __init__(self, number_of_coconuts: int) -> None:
        self._number_of_coconuts = number_of_coconuts

    def speed(self) -> float | int:
        return max(0, self.BASE_SPEED - self.LOAD_FACTOR * self._number_of_coconuts)

    def cry(self) -> str:
        return "Sqaark!"


class NorwegianBlueParrot(Parrot):

    def __init__(self, voltage: float, nailed: bool) -> None:
        self._voltage = voltage
        self._nailed = nailed

    def speed(self) -> float | int:
        if self._nailed:
            return 0
        else:
            return min([24.0, self._voltage * self.BASE_SPEED])

    def cry(self) -> str:
        if self._voltage > 0:
            return "Bzzzzzz"
        else:
            return "..."
