import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
pkg_dir = os.path.dirname(current_dir)
scripts_dir = os.path.join(pkg_dir, "scripts")
sys.path.insert(0, scripts_dir)

from parser import parse_travel_markdown
from build_styled_docx import build_docx
from generate_web import generate_web
from render_poster import render_poster

class TestFamilyTravelPlanner(unittest.TestCase):
    def setUp(self):
        self.sample_md = os.path.join(pkg_dir, "examples", "shanghai_sample.md")
        self.output_dir = os.path.join(pkg_dir, "dist_test")
        os.makedirs(self.output_dir, exist_ok=True)

    def test_parser(self):
        data = parse_travel_markdown(self.sample_md)
        self.assertIn("title", data)
        self.assertEqual(len(data["outfits"]), 4)
        self.assertEqual(len(data["days"]), 3)

    def test_docx_generation(self):
        out_docx = os.path.join(self.output_dir, "test.docx")
        build_docx(self.sample_md, out_docx)
        self.assertTrue(os.path.exists(out_docx))
        self.assertGreater(os.path.getsize(out_docx), 1000)

    def test_web_generation(self):
        out_web = os.path.join(self.output_dir, "test.html")
        generate_web(self.sample_md, out_web)
        self.assertTrue(os.path.exists(out_web))
        self.assertGreater(os.path.getsize(out_web), 500)

if __name__ == "__main__":
    unittest.main()
