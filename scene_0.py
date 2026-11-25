"""
scene_0.py – Title Card (target duration: ~5 seconds)

Scene 0 is a simple title card:
  • Project title fades in at the centre.
  • Subtitle ("Eigenvalues & Eigenvectors") fades in below.
  • Author placeholders fade in last.
  • Hold for a moment, then everything fades out cleanly.

No motion other than fades.  Background matches the global BACKGROUND colour.
"""

from manim import *
from helpers import BACKGROUND, MAIN_TEXT, AXES_COL, EIG_AMBER, EIG_TEAL


class TitleCard(Scene):
    # ── Background colour ──────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BACKGROUND

        # ── Title ──────────────────────────────────────────────────────────
        title = Text(
            "Eigenvalues & Eigenvectors",
            font_size=56,
            color=MAIN_TEXT,
            weight=BOLD,
        ).move_to(UP * 0.8)

        # Coloured "of a 2×2 Matrix" subtitle
        subtitle = Text(
            "of a 2×2 Matrix",
            font_size=40,
            color=AXES_COL,
        ).next_to(title, DOWN, buff=0.3)

        # Decorative coloured rule (amber | teal)
        rule_left = Line(
            LEFT * 3.5, LEFT * 0.2,
            color=EIG_AMBER, stroke_width=2,
        ).move_to(DOWN * 0.5 + LEFT * 1.85)
        rule_right = Line(
            RIGHT * 0.2, RIGHT * 3.5,
            color=EIG_TEAL, stroke_width=2,
        ).move_to(DOWN * 0.5 + RIGHT * 1.85)

        # Course / author placeholders
        course_line = Text(
            "Linear Algebra – University Course",
            font_size=28,
            color=AXES_COL,
        ).move_to(DOWN * 1.1)

        author_line = Text(
            "Vanshika Soni  ·  E25B070667",
            font_size=26,
            color=AXES_COL,
        ).next_to(course_line, DOWN, buff=0.25)

        # ── Animation sequence ─────────────────────────────────────────────
        # 1. Fade in title + subtitle together (0.8 s)
        self.play(
            FadeIn(title, shift=UP * 0.3, run_time=0.8),
        )
        self.play(
            FadeIn(subtitle, shift=UP * 0.2, run_time=0.6),
        )

        # 2. Draw the coloured rules (0.5 s)
        self.play(
            GrowFromCenter(rule_left),
            GrowFromCenter(rule_right),
            run_time=0.5,
        )

        # 3. Fade in author block (0.5 s)
        self.play(
            FadeIn(course_line, shift=UP * 0.2, run_time=0.5),
            FadeIn(author_line, shift=UP * 0.2, run_time=0.5),
        )

        # 4. Hold so the total scene is ~5 s
        self.wait(1.8)

        # 5. Fade everything out (1 s)
        self.play(
            FadeOut(
                VGroup(title, subtitle, rule_left, rule_right,
                       course_line, author_line),
            ),
            run_time=1.0,
        )
