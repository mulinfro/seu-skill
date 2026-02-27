import io
import contextlib
import unittest

from demo_run.src.calc import main


class CalcCliTest(unittest.TestCase):
    def run_cli(self, argv):
        out = io.StringIO()
        err = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(argv)
        return code, out.getvalue().strip(), err.getvalue().strip()

    def test_add(self):
        code, out, err = self.run_cli(["add", "2", "3"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "5")
        self.assertEqual(err, "")

    def test_sub(self):
        code, out, err = self.run_cli(["sub", "5", "2"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "3")
        self.assertEqual(err, "")

    def test_bad_op(self):
        code, out, err = self.run_cli(["mul", "2", "3"])
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("Unsupported op", err)

    def test_non_int(self):
        code, out, err = self.run_cli(["add", "x", "3"])
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("integers", err)

    def test_missing_args(self):
        code, out, err = self.run_cli(["add", "2"])
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("Usage", err)


if __name__ == "__main__":
    unittest.main()
