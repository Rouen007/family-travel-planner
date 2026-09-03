"""
Universal CLI for Family Travel Planner Artifact Pipeline
"""
import os
import sys
import argparse

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
from build_styled_docx import build_docx
from generate_web import generate_web
from render_poster import render_poster

def main():
    parser = argparse.ArgumentParser(description="Family Travel Planner Multi-Format Artifact CLI")
    parser.add_argument("command", choices=["all", "docx", "web", "poster"], help="Artifact to compile")
    parser.add_argument("--input", "-i", default="", help="Path to travel markdown plan")
    parser.add_argument("--output-dir", "-o", default="dist", help="Output directory for generated files")
    parser.add_argument("--view", "-v", action="store_true", help="Open generated outputs immediately")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    docx_out = os.path.join(args.output_dir, "travel_plan.docx")
    web_out = os.path.join(args.output_dir, "index.html")
    poster_out = os.path.join(args.output_dir, "travel_poster.png")

    if args.command in ["all", "docx"]:
        build_docx(args.input, docx_out)
    if args.command in ["all", "web"]:
        generate_web(args.input, web_out)
    if args.command in ["all", "poster"]:
        render_poster(args.input, poster_out, view=args.view)

    print(f"\n🎉 All requested artifacts generated successfully inside '{args.output_dir}' directory!")

if __name__ == "__main__":
    main()
