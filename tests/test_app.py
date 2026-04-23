from click.testing import CliRunner

from project.app import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ["--name", "Jules"])
    assert result.exit_code == 0
    assert "Hello Jules!" in result.output
