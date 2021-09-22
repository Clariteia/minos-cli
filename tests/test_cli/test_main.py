import unittest
from pathlib import (
    Path,
)
from tempfile import (
    TemporaryDirectory,
)
from unittest.mock import (
    patch,
)

from typer.testing import (
    CliRunner,
)

from minos.cli import (
    __main__,
    app,
    main,
)


class TestMain(unittest.TestCase):
    def test_microservice_init(self) -> None:
        with TemporaryDirectory() as tmp_dir_name:
            path = Path(tmp_dir_name) / "product"
            with patch("pathlib.Path.cwd", return_value=path):
                with patch("minos.cli.MicroserviceGenerator.build") as mock:
                    result = CliRunner().invoke(app, ["microservice", "init"])

                    self.assertEqual(0, result.exit_code)

                    self.assertEqual(1, mock.call_count)

    def test_microservice_new(self) -> None:
        with TemporaryDirectory() as tmp_dir_name:
            path = Path(tmp_dir_name) / "product"
            with patch("minos.cli.MicroserviceGenerator.build") as mock:
                result = CliRunner().invoke(app, ["microservice", "new", str(path)])

                self.assertEqual(0, result.exit_code)

                self.assertEqual(1, mock.call_count)

    def test_main(self):
        self.assertEqual(__main__.main, main)


if __name__ == "__main__":
    unittest.main()
