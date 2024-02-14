from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(
        self,
        type_of_parrot: ParrotType,
        number_of_coconuts: int,
        voltage: float,
        nailed: bool,
    ) -> None:
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self) -> float | int:
        if self._type == ParrotType.AFRICAN:
            return max(
                0, self._base_speed() - self._load_factor() * self._number_of_coconuts
            )
        if self._type == ParrotType.NORWEGIAN_BLUE:
            if self._nailed:
                return 0
            else:
                return self._compute_base_speed_for_voltage(self._voltage)

        raise ValueError("should be unreachable")

    def cry(self) -> str:
        if self._type == ParrotType.AFRICAN:
            return "Sqaark!"
        if self._type == ParrotType.NORWEGIAN_BLUE:
            if self._voltage > 0:
                return "Bzzzzzz"
            else:
                return "..."

        raise ValueError("should be unreachable")

    def _compute_base_speed_for_voltage(self, voltage: float) -> float:
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self) -> float:
        return 9.0

    def _base_speed(self) -> float:
        return 12.0


class EuropeanParrot(Parrot):

    def __init__(self, number_of_coconuts: int, voltage: float, nailed: bool) -> None:
        super().__init__(ParrotType.EUROPEAN, number_of_coconuts, voltage, nailed)

    def speed(self) -> float | int:
        return self._base_speed()

    def cry(self) -> str:
        return "Sqoork!"


class AfricanParrot(Parrot):

    def __init__(self, number_of_coconuts: int, voltage: float, nailed: bool) -> None:
        super().__init__(ParrotType.AFRICAN, number_of_coconuts, voltage, nailed)

    def speed(self) -> float | int:
        return max(
            0, self._base_speed() - self._load_factor() * self._number_of_coconuts
        )

    def cry(self) -> str:
        return "Sqaark!"
