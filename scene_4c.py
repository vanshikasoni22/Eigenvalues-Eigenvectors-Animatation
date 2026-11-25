"""
scene_4c.py – Negative Eigenvalue: C = [[0,1],[1,0]]
(target ~40 seconds)

VIVA EXPLANATION:
  C = [[0,1],[1,0]] is the reflection matrix across the line y = x.
  It swaps x and y coordinates: (x,y) → (y,x).

  Eigenvalues:
    det(C − λI) = det([[-λ,1],[1,-λ]]) = λ² − 1 = 0  →  λ = 1 and λ = −1.

  Eigenvectors:
    λ = 1 : (C−I)v=0 → [[-1,1],[1,-1]]v=0 → y=x → v=(1,1).
      (1,1) stays put under reflection: makes sense — it lies ON y=x.)
    λ = −1: (C+I)v=0 → [[1,1],[1,1]]v=0 → x+y=0 → v=(1,−1).
      (1,−1) flips to (−1,1) = −1·(1,−1). Same line, opposite direction.

  KEY TEACHING POINT: a negative eigenvalue means the eigenvector is
  reflected through the ORIGIN (flipped 180°) but stays on the same LINE.
  Caption: "Negative eigenvalue: same line, opposite direction."
"""

import numpy as np
from manim import *
from helpers import (
    BACKGROUND, GRID_ORIG, GRID_TRSF, AXES_COL,
    MAIN_TEXT, EIG_AMBER, EIG_TEAL, HIGHLIGHT,
    make_title_text, make_caption,
)

C_MAT = np.array([[0, 1], [1, 0]], dtype=float)


class NegativeEigenvalue(Scene):
    """
    Demonstrates a negative eigenvalue using the reflection matrix C.
    Key animation: v = (1,−1) smoothly flips to (−1,1) under C.
    """

    def construct(self):
        self.camera.background_color = BACKGROUND

        # ── Labels ─────────────────────────────────────────────────────────
        title   = make_title_text("Scene 4c – Negative Eigenvalue")
        mat_mob = MathTex(
            r"C = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}",
            color=MAIN_TEXT, font_size=36,
        ).to_corner(UR, buff=0.3)
        self.add(title, mat_mob)

        caption_a = make_caption(
            "C swaps x and y: a reflection across y = x"
        )
        self.play(FadeIn(caption_a, shift=UP * 0.2, run_time=0.5))
        self.wait(1.5)

        # ── Grid ───────────────────────────────────────────────────────────
        plane = NumberPlane(
            x_range=[-5, 5], y_range=[-3.5, 3.5],
            background_line_style={
                "stroke_color": GRID_ORIG,
                "stroke_width": 1, "stroke_opacity": 0.6,
            },
            axis_config={"stroke_color": AXES_COL, "stroke_width": 1.5},
        )
        self.play(Create(plane, run_time=0.8, rate_func=smooth))

        # ── Guide line y = x ───────────────────────────────────────────────
        guide_yx = DashedLine(
            np.array([-3.5, -3.5, 0]), np.array([3.5, 3.5, 0]),
            color=EIG_AMBER, stroke_width=2, dash_length=0.2, stroke_opacity=0.6,
        )
        lbl_yx = Text("y = x", font_size=20, color=EIG_AMBER)
        lbl_yx.next_to(np.array([2.8, 2.8, 0]), UR, buff=0.1)
        self.play(Create(guide_yx, run_time=0.5), FadeIn(lbl_yx, run_time=0.3))

        # ── Show eigenvalue equations ──────────────────────────────────────
        self.play(FadeOut(caption_a, run_time=0.3))
        caption_b = make_caption(
            "det(C − λI) = λ² − 1 = 0  →  λ = 1 and λ = −1"
        )
        self.play(FadeIn(caption_b, shift=UP * 0.2, run_time=0.4))

        char_eq = MathTex(
            r"\lambda^2 - 1 = 0",
            r"\implies \lambda = 1,\ \lambda = -1",
            font_size=38, color=MAIN_TEXT,
        ).to_corner(DL, buff=0.6).shift(UP * 0.3)
        self.play(FadeIn(char_eq[0], shift=UP * 0.2, run_time=0.5))
        self.wait(1.5)
        self.play(FadeIn(char_eq[1], shift=UP * 0.2, run_time=0.5))
        self.wait(1.5)

        self.play(FadeOut(caption_b, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # EIGENVECTOR 1: λ = 1, v = (1,1) → stays (amber)
        # ══════════════════════════════════════════════════════════════════
        caption_c = make_caption("λ = 1: eigenvector (1,1) lies ON y = x — it stays put")
        self.play(FadeIn(caption_c, shift=UP * 0.2, run_time=0.4))

        arr_amber = Arrow(
            ORIGIN, np.array([2.0, 2.0, 0]),
            buff=0, color=EIG_AMBER, stroke_width=4,
            max_tip_length_to_length_ratio=0.12,
        )
        lbl_amber = MathTex(r"(1,1)",  font_size=26, color=EIG_AMBER)
        lbl_amber.next_to(arr_amber.get_end(), UR, buff=0.1)

        self.play(GrowArrow(arr_amber), FadeIn(lbl_amber, run_time=0.3))
        self.play(Flash(arr_amber, color=EIG_AMBER, flash_radius=0.5, run_time=0.6))
        # Soft pulse: stays in place → there_and_back scale
        self.play(
            arr_amber.animate(rate_func=there_and_back).scale(1.2),
            run_time=0.6,
        )
        self.wait(1.5)
        self.play(FadeOut(caption_c, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # EIGENVECTOR 2: λ = −1, v = (1,−1) → flips to (−1,1)
        # KEY ANIMATION: rotate arrow 180° around the origin.
        # ══════════════════════════════════════════════════════════════════
        caption_d = make_caption(
            "λ = −1: eigenvector (1,−1) flips to (−1,1)  —  same LINE, opposite direction"
        )
        self.play(FadeIn(caption_d, shift=UP * 0.2, run_time=0.4))

        # Guide line through (1,−1) direction
        guide_neg = DashedLine(
            np.array([-3.5, 3.5, 0]), np.array([3.5, -3.5, 0]),
            color=EIG_TEAL, stroke_width=1.5, dash_length=0.2, stroke_opacity=0.5,
        )
        self.play(Create(guide_neg, run_time=0.5))

        # Initial arrow: (1,−1) direction, teal
        arr_teal = Arrow(
            ORIGIN, np.array([2.0, -2.0, 0]),
            buff=0, color=EIG_TEAL, stroke_width=4,
            max_tip_length_to_length_ratio=0.12,
        )
        lbl_teal_before = MathTex(r"(1,-1)", font_size=26, color=EIG_TEAL)
        lbl_teal_before.next_to(arr_teal.get_end(), DR, buff=0.1)

        self.play(GrowArrow(arr_teal), FadeIn(lbl_teal_before, run_time=0.3))
        self.wait(0.8)

        # Apply C: flip the arrow 180° around origin (smooth rotation)
        self.play(FadeOut(lbl_teal_before, run_time=0.2))
        self.play(
            Rotate(arr_teal, angle=PI, about_point=ORIGIN,
                   rate_func=smooth, run_time=2.0),
        )

        # Arrow now points to (−1,1)
        lbl_teal_after = MathTex(r"(-1,1) = -1 \cdot (1,-1)",
                                 font_size=24, color=EIG_TEAL)
        lbl_teal_after.next_to(arr_teal.get_end(), UL, buff=0.1)
        self.play(FadeIn(lbl_teal_after, shift=UP * 0.2, run_time=0.5))
        self.play(Flash(arr_teal, color=EIG_TEAL, flash_radius=0.5, run_time=0.6))
        self.wait(2.0)
        self.play(FadeOut(caption_d, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # VERIFICATION CHECKS
        # ══════════════════════════════════════════════════════════════════
        caption_e = make_caption("Verification")
        self.play(FadeIn(caption_e, shift=UP * 0.2, run_time=0.4))

        # Fade grid to 20 % for readability
        self.play(plane.animate.set_opacity(0.2), run_time=0.4)

        vc1 = MathTex(
            r"C\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}1\\1\end{pmatrix}=1\cdot\begin{pmatrix}1\\1\end{pmatrix}",
            font_size=34, color=EIG_AMBER,
        ).move_to(DOWN * 1.5 + LEFT * 2.0)
        self.play(FadeIn(vc1, shift=UP * 0.2, run_time=0.6))
        self.wait(1.5)
        t1 = Text("✓", font_size=36, color=EIG_AMBER).next_to(vc1, RIGHT, buff=0.2)
        self.play(FadeIn(t1, run_time=0.3))
        self.play(Flash(vc1, color=EIG_AMBER, flash_radius=0.5, run_time=0.5))

        vc2 = MathTex(
            r"C\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}-1\\1\end{pmatrix}=-1\cdot\begin{pmatrix}1\\-1\end{pmatrix}",
            font_size=34, color=EIG_TEAL,
        ).next_to(vc1, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(vc1.animate.set_opacity(0.4), run_time=0.3)
        self.play(FadeIn(vc2, shift=UP * 0.2, run_time=0.6))
        self.wait(1.5)
        t2 = Text("✓", font_size=36, color=EIG_TEAL).next_to(vc2, RIGHT, buff=0.2)
        self.play(FadeIn(t2, run_time=0.3))
        self.play(Flash(vc2, color=EIG_TEAL, flash_radius=0.5, run_time=0.5))

        self.wait(2.0)

        # ── Fade out ───────────────────────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
