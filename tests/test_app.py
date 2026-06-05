from click.testing import CliRunner

from project.app import main


def test_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "--name <name>" in result.output
    assert "-V, --version" in result.output
    assert "Example: app --name Alice" in result.output


def test_version():
    runner = CliRunner()
    result = runner.invoke(main, ["-V"])
    assert result.exit_code == 0
    assert "app, version 0.1.0" in result.output


def test_greet():
    runner = CliRunner()
    result = runner.invoke(main, ["--name", "Jules"])
    assert result.exit_code == 0
    assert "Hello Jules! 👋" in result.output
