"""
Universal CLI for Family Travel Planner Artifact Pipeline
Builds Word documents (.docx), Responsive Web apps (.html), and 2K long posters (.png).
"""
import os
import sys
import argparse

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from build_styled_docx import build_docx
from generate_web import generate_web
from render_poster import render_poster

__version__ = "1.2.0"

def main():
    parser = argparse.ArgumentParser(
        prog="family-travel-planner",
        description="Universal Multi-Generational Family Travel Planner CLI"
    )
    parser.add_argument("--version", "-V", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "command",
        choices=["all", "docx", "web", "poster"],
        help="Artifact compilation command: 'all', 'docx', 'web', or 'poster'"
    )
    parser.add_argument("--input", "-i", default="", help="Path to travel markdown plan (optional)")
    parser.add_argument("--output-dir", "-o", default="dist", help="Output directory for generated files (default: 'dist')")
    parser.add_argument("--view", "-v", action="store_true", help="Automatically open generated visual poster in default viewer")
    
    args = parser.parse_args()

    try:
        os.makedirs(args.output_dir, exist_ok=True)
        docx_out = os.path.join(args.output_dir, "travel_plan.docx")
        web_out = os.path.join(args.output_dir, "index.html")
        poster_out = os.path.join(args.output_dir, "travel_poster.png")

        if args.command in ["all", "docx"]:
            build_docx(args.input, docx_out)
        if args.command in ["all", "web"]:
            generate_web(args.input, web_out)
        if args.command in ["all", "poster"]:
            success = render_poster(args.input, poster_out, view=args.view)
            if not success and args.command == "poster":
                sys.exit(1)

        print(f"\n🎉 All requested artifacts generated successfully inside '{args.output_dir}' directory!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error during execution: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
