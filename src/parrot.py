from abc import ABC, abstractmethod


class Parrot(ABC):

    def __init__(self, number_of_coconuts: int, voltage: float, nailed: bool) -> None:
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    @abstractmethod
    def speed(self) -> float | int:
        raise NotImplementedError()

    @abstractmethod
    def cry(self) -> str:
        raise NotImplementedError()

    def _base_speed(self) -> float:
        return 12.0


class EuropeanParrot(Parrot):

    def __init__(self, number_of_coconuts: int, voltage: float, nailed: bool) -> None:
        super().__init__(number_of_coconuts, voltage, nailed)

    def speed(self) -> float | int:
        return self._base_speed()

    def cry(self) -> str:
        return "Sqoork!"


class AfricanParrot(Parrot):

    def __init__(self, number_of_coconuts: int, voltage: float, nailed: bool) -> None:
        super().__init__(number_of_coconuts, voltage, nailed)

    def speed(self) -> float | int:
        return max(
            0, self._base_speed() - self._load_factor() * self._number_of_coconuts
        )

    def cry(self) -> str:
        return "Sqaark!"

    def _load_factor(self) -> float:
        return 9.0


class NorwegianBlueParrot(Parrot):

    def __init__(self, number_of_coconuts: int, voltage: float, nailed: bool) -> None:
        super().__init__(number_of_coconuts, voltage, nailed)

    def speed(self) -> float | int:
        if self._nailed:
            return 0
        else:
            return min([24.0, self._voltage * self._base_speed()])

    def cry(self) -> str:
        if self._voltage > 0:
            return "Bzzzzzz"
        else:
            return "..."
