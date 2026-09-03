"""
Comprehensive Automated Test Suite for Family Travel Planner
Verifies Parser, Renderer, Docx Generator, Web App Generator, and Edge Cases.
"""
import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
pkg_dir = os.path.dirname(current_dir)
scripts_dir = os.path.join(pkg_dir, "scripts")
sys.path.insert(0, scripts_dir)

from parser import parse_travel_markdown
from renderer import render_template, _micro_render
from build_styled_docx import build_docx
from generate_web import generate_web

class TestFamilyTravelPlanner(unittest.TestCase):
    def setUp(self):
        self.sample_shanghai = os.path.join(pkg_dir, "examples", "shanghai_sample.md")
        self.sample_quanzhou = os.path.join(pkg_dir, "examples", "quanzhou_minnan_heritage.md")
        self.output_dir = os.path.join(pkg_dir, "dist_test")
        os.makedirs(self.output_dir, exist_ok=True)

    def test_parser_empty_and_nonexistent(self):
        """Verify zero recursion error on empty or invalid file paths."""
        data_empty = parse_travel_markdown("")
        self.assertIn("title", data_empty)
        self.assertEqual(len(data_empty["days"]), 3)

        data_none = parse_travel_markdown("/non/existent/path.md")
        self.assertIn("title", data_none)

    def test_parser_family_demographics_quanzhou(self):
        """Verify dynamic detection of 5yo girl + parents (no grandma)."""
        data = parse_travel_markdown(self.sample_quanzhou)
        self.assertIn("泉州", data["title"])
        self.assertEqual(len(data["outfits"]), 3)
        self.assertIn("5岁", data["outfits"][0]["name"])
        # Ensure no Grandma card
        names = [o["name"] for o in data["outfits"]]
        self.assertFalse(any("外婆" in n or "奶奶" in n for n in names))

    def test_parser_family_demographics_shanghai(self):
        """Verify detection of 2yo toddler + Grandma + parents (4 people)."""
        data = parse_travel_markdown(self.sample_shanghai)
        self.assertEqual(len(data["outfits"]), 4)
        names = [o["name"] for o in data["outfits"]]
        self.assertTrue(any("外婆" in n or "长辈" in n for n in names))

    def test_micro_renderer_nested_loops(self):
        """Verify standalone micro-renderer handles nested for-loops and filters."""
        tmpl = '<h1>{{ data.title }}</h1>{% for d in data.days %}<div>{{ d.day_tag }}: {% for t_time, t_desc in d.items %}<span>{{ t_time }} - {{ t_desc }}</span>{% endfor %}</div>{% endfor %}'
        ctx = {
            'data': {
                'title': '测试标题',
                'days': [
                    {'day_tag': 'Day 1', 'items': [('10:00', '启程'), ('12:00', '午餐')]}
                ]
            }
        }
        res = _micro_render(tmpl, ctx)
        self.assertIn("测试标题", res)
        self.assertIn("10:00 - 启程", res)
        self.assertIn("12:00 - 午餐", res)

    def test_docx_generation(self):
        """Verify Word docx builds properly with custom dynamic tables."""
        out_docx = os.path.join(self.output_dir, "test.docx")
        build_docx(self.sample_quanzhou, out_docx)
        self.assertTrue(os.path.exists(out_docx))
        self.assertGreater(os.path.getsize(out_docx), 2000)

    def test_web_generation(self):
        """Verify interactive single page web app builds cleanly."""
        out_web = os.path.join(self.output_dir, "test.html")
        generate_web(self.sample_quanzhou, out_web)
        self.assertTrue(os.path.exists(out_web))
        self.assertGreater(os.path.getsize(out_web), 1000)
        with open(out_web, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn("泉州", html)
        self.assertIn("5岁女娃", html)

    def tearDown(self):
        import shutil
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

if __name__ == "__main__":
    unittest.main()
