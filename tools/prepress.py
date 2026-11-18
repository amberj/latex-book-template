"""Paperback prepress helpers for book-length LaTeX layouts.

Pure functions, standard library only. No network, no file writes, no unseeded
state. Values are planning aids; the printer's current guidelines are
authoritative.
"""

# Approximate paper stock thickness in inches per 1000 pages.
PAPER_THICKNESS_PER_1000 = {
    "black-cream": 0.002252,
    "black-white": 0.002000,
    "color-premium": 0.002347,
}

# Common trade trim sizes in inches (width, height).
TRIM_SIZES = {
    "a4": (8.27, 11.69),
    "letter": (8.5, 11.0),
    "5.5x8.25": (5.5, 8.25),
    "6x9": (6.0, 9.0),
}


def spine_width_inches(page_count, paper="black-cream", cover_thickness_in=0.009):
    """Wraparound cover spine width in inches."""
    if page_count <= 0:
        raise ValueError("page_count must be positive")
    if paper not in PAPER_THICKNESS_PER_1000:
        raise ValueError("unknown paper: %s" % paper)
    if cover_thickness_in < 0:
        raise ValueError("cover thickness must be non-negative")
    return (page_count / 1000.0) * PAPER_THICKNESS_PER_1000[paper] + 2 * cover_thickness_in


def gutter_inches(page_count):
    """Minimum inner margin by page-count class (planning heuristic)."""
    if page_count <= 150:
        return 0.375
    if page_count <= 300:
        return 0.500
    if page_count <= 500:
        return 0.625
    if page_count <= 700:
        return 0.750
    if page_count <= 828:
        return 0.875
    raise ValueError("page_count exceeds common paperback maximum (828)")


def trim_matches(interior_w_in, interior_h_in, trim, tol=0.01):
    """Whether an interior PDF page size matches a named trim size."""
    if trim not in TRIM_SIZES:
        raise ValueError("unknown trim: %s" % trim)
    w, h = TRIM_SIZES[trim]
    return abs(interior_w_in - w) <= tol and abs(interior_h_in - h) <= tol


def inner_margin_mm(page_count, safety_mm=2.0):
    """Practical safe inner margin in mm from the page-count heuristic."""
    return round(gutter_inches(page_count) * 25.4 + safety_mm, 1)
