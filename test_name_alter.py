import pytest
from name_alter import ist_gerades


def test_ist_gerade():
    assert ist_gerade(42) == True
    assert ist_gerade(7) == False


def test_hallo_message(capsys):
    name = "Jihen"
    alter = 28
    print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")
    captured = capsys.readouterr()
    assert captured.out == "Hallo Jihen, in 10 Jahren wirst du 38 Jahre alt sein!\n"
