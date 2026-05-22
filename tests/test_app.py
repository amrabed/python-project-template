from click.testing import CliRunner

from project.app import main


def test_main_default():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Hello World! 👋" in result.output


def test_main_custom_name():
    runner = CliRunner()
    result = runner.invoke(main, ["--name", "Palette"])
    assert result.exit_code == 0
    assert "Hello Palette! 👋" in result.output


def test_main_whitespace_name():
    runner = CliRunner()
    result = runner.invoke(main, ["--name", "   "])
    assert result.exit_code == 0
    assert "Hello World! 👋" in result.output


def test_main_long_name():
    runner = CliRunner()
    long_name = "A" * 101
    result = runner.invoke(main, ["--name", long_name])
    assert result.exit_code != 0
    assert "Error: Name cannot exceed 100 characters." in result.output


if __name__ == "__main__":
    import pytest

    pytest.main()
