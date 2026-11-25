"""
scene_5b.py – Predict-the-Answer Pause: D = [[3,0],[0,1]]
(target ~30 seconds)

VIVA EXPLANATION:
  This scene turns the viewer into an active learner by posing a question
  before giving the answer. D = [[3,0],[0,1]] is a DIAGONAL matrix — the
  simplest case. The eigenvalues are just the diagonal entries (3 and 1),
  and the eigenvectors are the standard basis vectors (1,0) and (0,1).

  After a 5-second countdown, the answer is revealed:
    λ = 3, eigenvector (1,0): the x-axis stretches by factor 3.
    λ = 1, eigenvector (0,1): the y-axis is unchanged.

  KEY RULE: For ANY diagonal matrix diag(a, b):
    eigenvalues are a and b, eigenvectors are (1,0) and (0,1).

  The grid animation visually confirms: x-axis stretches 3×, y-axis stays.
"""

import numpy as np
from manim import *
from helpers import (
    BACKGROUND, GRID_ORIG, AXES_COL,
    MAIN_TEXT, EIG_AMBER, EIG_TEAL, HIGHLIGHT,
    make_title_text, make_caption,
)

D_MAT = np.array([[3, 0], [0, 1]], dtype=float)


class PredictPause(Scene):
    """
    Interactive pause scene: viewer is asked to predict eigenvalues of D
    before a 5-second countdown reveals the answer.
    """

    def construct(self):
        self.camera.background_color = BACKGROUND

        # ── Labels ─────────────────────────────────────────────────────────
        title   = make_title_text("Scene 5b – Predict the Answer")
        mat_mob = MathTex(
            r"D = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}",
            color=MAIN_TEXT, font_size=36,
        ).to_corner(UR, buff=0.3)
        self.add(title, mat_mob)

        # ── Pose the question ──────────────────────────────────────────────
        question = Text(
            "Pause. What are the eigenvalues of D?",
            font_size=38,
            color=MAIN_TEXT,
            weight=BOLD,
        ).move_to(UP * 1.5)

        hint = Text(
            "(Hint: D is diagonal — look at its entries.)",
            font_size=26,
            color=AXES_COL,
        ).next_to(question, DOWN, buff=0.3)

        self.play(
            FadeIn(question, shift=UP * 0.3, run_time=0.6, rate_func=smooth)
        )
        self.play(
            FadeIn(hint, shift=UP * 0.2, run_time=0.4)
        )
        self.wait(0.5)

        caption_q = make_caption("Think before looking at the answer below…")
        self.play(FadeIn(caption_q, shift=UP * 0.2, run_time=0.4))

        # ── Countdown timer: 5 → 1 ────────────────────────────────────────
        # Each digit shown for ~1 second
        countdown_label = Text("Answer in:", font_size=28, color=AXES_COL)
        countdown_label.move_to(DOWN * 0.5)
        self.play(FadeIn(countdown_label, run_time=0.3))

        count_text = None
        for i in range(5, 0, -1):
            new_num = Text(str(i), font_size=72, color=EIG_AMBER, weight=BOLD)
            new_num.next_to(countdown_label, DOWN, buff=0.3)

            if count_text is None:
                self.play(FadeIn(new_num, run_time=0.2))
            else:
                self.play(
                    FadeOut(count_text, run_time=0.15),
                    FadeIn(new_num, run_time=0.2),
                )
            count_text = new_num
            self.wait(0.65)   # ~1 s per digit including transition

        self.play(FadeOut(count_text, run_time=0.2))

        # ── Reveal answer ──────────────────────────────────────────────────
        self.play(
            FadeOut(question, hint, countdown_label, caption_q, run_time=0.5),
        )

        caption_ans = make_caption(
            "Diagonal matrix: eigenvalues = diagonal entries, "
            "eigenvectors = standard basis"
        )
        self.play(FadeIn(caption_ans, shift=UP * 0.2, run_time=0.4))

        ans_lines = []

        ans1 = MathTex(
            r"\lambda_1 =", r"3",
            r"\quad \mathbf{v}_1 = (1,0)\ \text{(x-axis stretches } \times 3\text{)}",
            font_size=36,
        ).move_to(UP * 1.5)
        ans1[0].set_color(MAIN_TEXT)
        ans1[1].set_color(EIG_AMBER)
        ans1[2].set_color(EIG_AMBER)
        self.play(FadeIn(ans1, shift=UP * 0.2, run_time=0.6))
        ans_lines.append(ans1)
        self.wait(1.5)

        ans2 = MathTex(
            r"\lambda_2 =", r"1",
            r"\quad \mathbf{v}_2 = (0,1)\ \text{(y-axis unchanged)}",
            font_size=36,
        ).next_to(ans1, DOWN, buff=0.4, aligned_edge=LEFT)
        ans2[0].set_color(MAIN_TEXT)
        ans2[1].set_color(EIG_TEAL)
        ans2[2].set_color(EIG_TEAL)
        self.play(ans1.animate.set_opacity(0.4), run_time=0.3)
        self.play(FadeIn(ans2, shift=UP * 0.2, run_time=0.6))
        ans_lines.append(ans2)
        self.wait(1.5)

        rule = MathTex(
            r"\text{Rule: for } \mathrm{diag}(a,b),\ "
            r"\lambda\text{'s} = a,b;\ "
            r"\mathbf{v}\text{'s} = (1,0),(0,1)",
            font_size=30, color=HIGHLIGHT,
        ).next_to(ans2, DOWN, buff=0.45, aligned_edge=LEFT)
        self.play(*[m.animate.set_opacity(0.4) for m in ans_lines], run_time=0.3)
        self.play(FadeIn(rule, shift=UP * 0.2, run_time=0.6))
        self.wait(1.5)

        # ── Grid stretch animation ─────────────────────────────────────────
        self.play(FadeOut(caption_ans, run_time=0.3))
        caption_grid = make_caption("Watch the grid: x-axis stretches 3×, y-axis stays")
        self.play(FadeIn(caption_grid, shift=UP * 0.2, run_time=0.4))

        # Fade text so grid is readable
        self.play(
            *[m.animate.set_opacity(0.25) for m in ans_lines + [rule]],
            run_time=0.4,
        )

        plane = NumberPlane(
            x_range=[-5, 5], y_range=[-3.5, 3.5],
            background_line_style={
                "stroke_color": GRID_ORIG,
                "stroke_width": 1, "stroke_opacity": 0.6,
            },
            axis_config={"stroke_color": AXES_COL, "stroke_width": 1.5},
        )
        self.play(Create(plane, run_time=0.6, rate_func=smooth))

        # Eigenvector arrows before transform
        arr_x = Arrow(ORIGIN, RIGHT * 1.5, buff=0, color=EIG_AMBER,
                      stroke_width=4, max_tip_length_to_length_ratio=0.15)
        arr_y = Arrow(ORIGIN, UP * 1.5,    buff=0, color=EIG_TEAL,
                      stroke_width=4, max_tip_length_to_length_ratio=0.15)
        self.play(GrowArrow(arr_x), GrowArrow(arr_y))

        # Apply D: x stretches by 3, y stays
        self.play(
            plane.animate(rate_func=smooth).apply_matrix(D_MAT),
            # Arrow for x stretches to 4.5 (1.5 * 3), y stays at 1.5
            arr_x.animate(rate_func=smooth).put_start_and_end_on(
                ORIGIN, RIGHT * 4.5
            ),
            run_time=3.0,
        )
        self.wait(2.0)

        # ── Fade out ───────────────────────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
