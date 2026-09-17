import sys

from nebula.cli import main


def test_cli_without_command_returns_zero(monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["nebula"])
    assert main() == 0
