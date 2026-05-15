from click.testing import CliRunner

from project.app import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ["--name", "Jules"])
    assert result.exit_code == 0
    assert "Hello Jules! 👋" in result.output


def test_main_default():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Hello World! 👋" in result.output


def test_version():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output.lower()


if __name__ == "__main__":
    import pytest

    pytest.main()
