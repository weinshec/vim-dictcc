import unittest
import urllib.error
from dictcc import DictQuery
from unittest.mock import patch


class DictCCTests(unittest.TestCase):

    def test_DictQuery_has_target_word_property(self):
        q = DictQuery("foobar")
        self.assertEqual(q.target, "foobar")

    def test_DictQuery_returns_list_of_translations(self):
        q = DictQuery("thought")
        tranlations = q.translations
        self.assertGreaterEqual(len(tranlations), 1)

    def test_DictQuery_translations_list_is_empty_for_not_found_word(self):
        q = DictQuery("aksuldgfhuiaerg")
        self.assertListEqual(q.translations, [])

    @patch("urllib.request.urlopen", side_effect=urllib.error.URLError("dooh"))
    def test_DictQuery_translations_list_is_empty_if_URLError(self, mock):
        q = DictQuery("thought")
        try:
            self.assertListEqual(q.translations, [])
        except Exception:
            self.fail("Uncaught Exception occurred!")

    def test_DictQuery_can_return_as_lines_staring_with_target(self):
        q = DictQuery("aber")
        first_line = q.as_lines()[0]
        self.assertIn("aber", first_line)

    def test_DictQuery_can_return_as_lines(self):
        q = DictQuery("aber")
        lines = q.as_lines()
        self.assertIn("but", lines[1])
        self.assertIn("aber", lines[1])
