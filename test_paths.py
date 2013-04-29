import unittest
import paths
import os.path

class TestPaths(unittest.TestCase):

    def test_make_paths(self):
        output = paths.make_paths("test_files")
        for file in output:
            self.assertTrue(os.path.isfile(file))
            self.assertTrue(file.endswith(".py"))

    def test_group_no_trailing_slash(self):
        expected = ["f", "f/e", "", "t"]

        output = list(paths.group("/a/b/c", ["/a/b/c/f", "/a/b/c/f/e", "/a/b/c", "/a/b/c/t"]))
        self.assertEqual(expected, output)

    def test_group_trailing_slash(self):
        expected = ["f", "f/e", "", "t"]

        output = list(paths.group("/a/b/c/", ["/a/b/c/f", "/a/b/c/f/e", "/a/b/c", "/a/b/c/t"]))
        self.assertEqual(expected, output)

if __name__ == "__main__":
    unittest.main()