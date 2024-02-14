from src.parrot import Parrot, ParrotType, EuropeanParrot, AfricanParrot


def test_speed_of_european_parrot() -> None:
    parrot = EuropeanParrot(0, 0, False)
    assert parrot.speed() == 12.0


def test_cry_of_european_parrot() -> None:
    parrot = EuropeanParrot(0, 0, False)
    assert parrot.cry() == "Sqoork!"


def test_speed_of_african_parrot_with_one_coconut() -> None:
    parrot = AfricanParrot(1, 0, False)
    assert parrot.speed() == 3.0


def test_cry_of_african_parrot() -> None:
    parrot = AfricanParrot(1, 0, False)
    assert parrot.cry() == "Sqaark!"


def test_speed_of_african_parrot_with_two_coconuts() -> None:
    parrot = AfricanParrot(2, 0, False)
    assert parrot.speed() == 0.0


def test_speed_of_african_parrot_with_no_coconuts() -> None:
    parrot = AfricanParrot(0, 0, False)
    assert parrot.speed() == 12.0


def test_speed_norwegian_blue_parrot_nailed() -> None:
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, True)
    assert parrot.speed() == 0.0


def test_speed_norwegian_blue_parrot_not_nailed() -> None:
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
    assert parrot.speed() == 18.0


def test_speed_norwegian_blue_parrot_not_nailed_high_voltage() -> None:
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
    assert parrot.speed() == 24.0


def test_cry_norwegian_blue_parrot_high_voltage() -> None:
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1, False)
    assert parrot.cry() == "Bzzzzzz"


def test_cry_norwegian_blue_parrot_no_voltage() -> None:
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 0, False)
    assert parrot.cry() == "..."
