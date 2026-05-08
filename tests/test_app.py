from pytest import main
from project.app import main as app_main
from io import StringIO
from contextlib import redirect_stdout


def test_main(monkeypatch):
    with redirect_stdout(StringIO()) as out:
        app_main(["-n", "Bolt"])
        assert out.getvalue().strip() == "Hello Bolt!"

    with redirect_stdout(StringIO()) as out:
        app_main([])
        assert out.getvalue().strip() == "Hello World!"


if __name__ == "__main__":
    main()
