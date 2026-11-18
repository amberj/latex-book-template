#!/usr/bin/env python3
"""Print a paperback prepress plan from page count and trim choice."""

import argparse

from prepress import (
    TRIM_SIZES,
    gutter_inches,
    inner_margin_mm,
    spine_width_inches,
)


def main():
    ap = argparse.ArgumentParser(description="Book prepress calculator")
    ap.add_argument("pages", type=int, help="total interior page count")
    ap.add_argument("--paper", default="black-cream",
                    choices=["black-cream", "black-white", "color-premium"])
    ap.add_argument("--trim", default="a4", choices=sorted(TRIM_SIZES))
    args = ap.parse_args()
    try:
        w, h = TRIM_SIZES[args.trim]
        print("trim: %s (%.2f x %.2f in)" % (args.trim, w, h))
        print("spine: %.4f in" % spine_width_inches(args.pages, args.paper))
        print("gutter (min): %.3f in" % gutter_inches(args.pages))
        print("inner margin (safe): %.1f mm" % inner_margin_mm(args.pages))
    except ValueError as exc:
        ap.error(str(exc))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
