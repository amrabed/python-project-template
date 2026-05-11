from project.app import main


def test_main():
    try:
        main(args=[], standalone_mode=False)
    except SystemExit:
        pass


if __name__ == "__main__":
    import pytest

    pytest.main()
