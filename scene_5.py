"""
scene_5.py – Interpretation: det, trace, and geometric meaning (target: ~40 s)

What happens:
  1. Draw a unit square (corners (0,0),(1,0),(1,1),(0,1)).
  2. Morph it smoothly into the parallelogram formed by the columns of A
     (columns: (2,1) and (1,2)).  Fill with 30 % opacity blue.
  3. Show "Area = det(A) = 3" text revealed one line at a time.
  4. Show det = λ₁ × λ₂ = 3 × 1 = 3  and  trace = λ₁ + λ₂ = 3 + 1 = 4.
  5. Show eigenvector arrows (amber, teal) grow by their respective eigenvalues.
"""

import numpy as np
from manim import *
from helpers import (
    BACKGROUND, GRID_ORIG, GRID_TRSF, AXES_COL,
    MAIN_TEXT, EIG_AMBER, EIG_TEAL, HIGHLIGHT,
    make_title_text, make_matrix_mob, make_caption,
)


class Interpretation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        # ── Labels ─────────────────────────────────────────────────────────
        title   = make_title_text("Scene 5 – Geometric Interpretation")
        mat_mob = make_matrix_mob()
        self.add(title, mat_mob)

        caption_a = make_caption("The unit square transforms into a parallelogram")
        self.play(FadeIn(caption_a, shift=UP * 0.2, run_time=0.4))

        # ── Background plane ───────────────────────────────────────────────
        plane = NumberPlane(
            x_range=[-5, 5],
            y_range=[-3.5, 3.5],
            background_line_style={
                "stroke_color": GRID_ORIG,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
            axis_config={"stroke_color": AXES_COL, "stroke_width": 1.5},
        )
        self.play(Create(plane, run_time=0.8))

        # ── Unit square ────────────────────────────────────────────────────
        # Vertices: (0,0), (1,0), (1,1), (0,1) in scene coords (1 unit = 1 scene unit)
        square = Polygon(
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
            color=MAIN_TEXT,
            stroke_width=2,
            fill_color="#4D96FF",
            fill_opacity=0.3,
        )
        self.play(Create(square, run_time=0.6))
        self.wait(0.3)

        # ── Morph to parallelogram (columns of A: (2,1) and (1,2)) ─────────
        # Parallelogram vertices: (0,0), col1=(2,1), col1+col2=(3,3), col2=(1,2)
        parallelogram = Polygon(
            [0, 0, 0], [2, 1, 0], [3, 3, 0], [1, 2, 0],
            color=GRID_TRSF,
            stroke_width=2.5,
            fill_color="#4D96FF",
            fill_opacity=0.3,
        )
        self.play(
            Transform(square, parallelogram, run_time=2.5, rate_func=smooth),
        )
        self.wait(0.5)
        self.play(FadeOut(caption_a, run_time=0.3))

        # ── Area label ────────────────────────────────────────────────────
        area_label = MathTex(
            r"\text{Area} = |\det(A)| = 3",
            font_size=38, color=MAIN_TEXT,
        ).to_corner(DL, buff=0.5).shift(UP * 0.3)

        caption_b = make_caption("det(A) = area scaling factor")
        self.play(FadeIn(caption_b, shift=UP * 0.2, run_time=0.4))
        self.play(FadeIn(area_label, shift=UP * 0.2, run_time=0.6))
        self.wait(0.4)

        # ── det and trace relations ────────────────────────────────────────
        all_shown = [area_label]

        det_line = MathTex(
            r"\det(A) = \lambda_1 \cdot \lambda_2 = ",
            r"3",
            r"\times",
            r"1",
            r"= 3",
            font_size=36,
        )
        det_line[0].set_color(MAIN_TEXT)
        det_line[1].set_color(EIG_AMBER)
        det_line[2].set_color(MAIN_TEXT)
        det_line[3].set_color(EIG_TEAL)
        det_line[4].set_color(MAIN_TEXT)
        det_line.next_to(area_label, DOWN, buff=0.35, aligned_edge=LEFT)

        # Dim previous
        self.play(area_label.animate.set_opacity(0.4), run_time=0.3)
        self.play(FadeIn(det_line, shift=UP * 0.2, run_time=0.6))
        all_shown.append(det_line)
        self.wait(0.4)
        self.play(FadeOut(caption_b, run_time=0.3))

        caption_c = make_caption("trace(A) = sum of eigenvalues")
        self.play(FadeIn(caption_c, shift=UP * 0.2, run_time=0.4))

        trace_line = MathTex(
            r"\mathrm{tr}(A) = \lambda_1 + \lambda_2 = ",
            r"3",
            r"+",
            r"1",
            r"= 4",
            font_size=36,
        )
        trace_line[0].set_color(MAIN_TEXT)
        trace_line[1].set_color(EIG_AMBER)
        trace_line[2].set_color(MAIN_TEXT)
        trace_line[3].set_color(EIG_TEAL)
        trace_line[4].set_color(MAIN_TEXT)
        trace_line.next_to(det_line, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(*[m.animate.set_opacity(0.4) for m in all_shown], run_time=0.3)
        self.play(FadeIn(trace_line, shift=UP * 0.2, run_time=0.6))
        all_shown.append(trace_line)
        self.wait(0.5)
        self.play(FadeOut(caption_c, run_time=0.3))

        # ── Eigenvector arrows growing ─────────────────────────────────────
        caption_d = make_caption("Eigenvectors show the stretch directions")
        self.play(FadeIn(caption_d, shift=UP * 0.2, run_time=0.4))

        # Amber eigenvector: starts at (0,0), grows to (3,3)/√2 (scaled by 3)
        s2 = np.sqrt(2)
        arr_amber_start = Arrow(
            ORIGIN, np.array([1 / s2, 1 / s2, 0]),
            buff=0, color=EIG_AMBER, stroke_width=3,
            max_tip_length_to_length_ratio=0.12,
        )
        arr_amber_end = Arrow(
            ORIGIN, np.array([3 / s2, 3 / s2, 0]),
            buff=0, color=EIG_AMBER, stroke_width=3,
            max_tip_length_to_length_ratio=0.12,
        )
        lbl_amber = MathTex(r"\times 3", font_size=26, color=EIG_AMBER)
        lbl_amber.next_to(arr_amber_end.get_end(), UR, buff=0.1)

        # Teal eigenvector: stays (1/√2, −1/√2) (λ=1, no scaling)
        arr_teal = Arrow(
            ORIGIN, np.array([1 / s2, -1 / s2, 0]),
            buff=0, color=EIG_TEAL, stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        lbl_teal = MathTex(r"\times 1", font_size=26, color=EIG_TEAL)
        lbl_teal.next_to(arr_teal.get_end(), DR, buff=0.1)

        self.play(GrowArrow(arr_amber_start), GrowArrow(arr_teal))
        self.play(
            Transform(arr_amber_start, arr_amber_end, rate_func=smooth, run_time=1.2),
        )
        self.play(
            FadeIn(lbl_amber, run_time=0.3),
            FadeIn(lbl_teal, run_time=0.3),
        )

        self.wait(2.5)   # hold to reach ~40 s

        # ── Fade out ───────────────────────────────────────────────────────
        self.play(
            *[FadeOut(m) for m in self.mobjects],
            run_time=1.0,
        )
