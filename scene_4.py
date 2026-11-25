"""
scene_4.py – Worked Example (target: ~90 seconds)

Walks through the full algebraic derivation step by step.
Each new MathTex line appears bright; previous lines dim to 40 % opacity.

Steps shown:
  1. Characteristic equation  (A − λI)v = 0
  2. det(A − λI) = 0
  3. Expand determinant: (2−λ)² − 1 = 0
  4. Simplify: λ² − 4λ + 3 = 0
  5. Factor: (λ−3)(λ−1) = 0
  6. Solutions: λ = 3 (amber)  and  λ = 1 (teal)

  7. Solve (A−3I)v = 0  →  y = x  →  v = (1,1)  [amber] + arrow on plane
  8. Solve (A−I)v = 0   →  y = −x →  v = (1,−1) [teal]  + arrow on plane

  9. Verification: A(1,1) = (3,3) = 3(1,1) — amber flash
 10. Verification: A(1,−1) = (1,−1) = 1(1,−1) — teal flash
"""

import numpy as np
from manim import *
from helpers import (
    BACKGROUND, AXES_COL, MAIN_TEXT, EIG_AMBER, EIG_TEAL, HIGHLIGHT,
    make_title_text, make_matrix_mob, make_caption,
)


# ── Utility: sequential-reveal list of MathTex equations ───────────────────
def _reveal(scene: Scene, mob_new: VMobject, prev_mobs: list,
            run_time: float = 0.7, wait: float = 0.5):
    """
    Dim all previous mobs to 40 % opacity, then FadeIn the new one.
    Returns updated list including the new mob.
    """
    dim_anims = [m.animate.set_opacity(0.4) for m in prev_mobs]
    if dim_anims:
        scene.play(*dim_anims, run_time=0.3)
    scene.play(FadeIn(mob_new, shift=UP * 0.25, run_time=run_time,
                      rate_func=smooth))
    scene.wait(wait)
    return prev_mobs + [mob_new]


class WorkedExample(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        # ── Labels ─────────────────────────────────────────────────────────
        title   = make_title_text("Scene 4 – Worked Example")
        mat_mob = make_matrix_mob()
        self.add(title, mat_mob)

        # ══════════════════════════════════════════════════════════════════
        # SECTION A – Characteristic equation derivation
        # Place equations on the LEFT half of the screen in a vertical stack
        # ══════════════════════════════════════════════════════════════════
        caption_a = make_caption("Step 1: form the characteristic equation")
        self.play(FadeIn(caption_a, shift=UP * 0.2, run_time=0.4))

        eq_lines = []   # tracks all displayed equation mobs

        # ── Line 1: (A − λI)v = 0 ─────────────────────────────────────────
        line1 = MathTex(
            r"(A - \lambda I)\mathbf{v} = \mathbf{0}",
            font_size=46, color=MAIN_TEXT,
        ).move_to(UP * 2.5 + LEFT * 2)
        eq_lines = _reveal(self, line1, eq_lines, run_time=0.8, wait=0.5)

        # ── Line 2: det(A − λI) = 0 ───────────────────────────────────────
        self.play(FadeOut(caption_a, run_time=0.3))
        caption_b = make_caption("For non-trivial solutions the determinant must be zero")
        self.play(FadeIn(caption_b, shift=UP * 0.2, run_time=0.4))

        line2 = MathTex(
            r"\det(A - \lambda I) = 0",
            font_size=46, color=MAIN_TEXT,
        ).next_to(line1, DOWN, buff=0.45, aligned_edge=LEFT)
        eq_lines = _reveal(self, line2, eq_lines, run_time=0.7, wait=0.5)

        # ── Line 3: expand the 2×2 determinant ────────────────────────────
        self.play(FadeOut(caption_b, run_time=0.3))
        caption_c = make_caption("Expand the 2 × 2 determinant")
        self.play(FadeIn(caption_c, shift=UP * 0.2, run_time=0.4))

        line3 = MathTex(
            r"(2-\lambda)^2 - 1^2 = 0",
            font_size=46, color=MAIN_TEXT,
        ).next_to(line2, DOWN, buff=0.45, aligned_edge=LEFT)
        eq_lines = _reveal(self, line3, eq_lines, run_time=0.7, wait=0.5)

        # ── Line 4: simplify ───────────────────────────────────────────────
        line4 = MathTex(
            r"\lambda^2 - 4\lambda + 3 = 0",
            font_size=46, color=MAIN_TEXT,
        ).next_to(line3, DOWN, buff=0.45, aligned_edge=LEFT)
        eq_lines = _reveal(self, line4, eq_lines, run_time=0.7, wait=0.5)
        self.play(FadeOut(caption_c, run_time=0.3))

        # ── Line 5: factor ─────────────────────────────────────────────────
        caption_d = make_caption("Factor the characteristic polynomial")
        self.play(FadeIn(caption_d, shift=UP * 0.2, run_time=0.4))

        line5 = MathTex(
            r"(\lambda - 3)(\lambda - 1) = 0",
            font_size=46, color=MAIN_TEXT,
        ).next_to(line4, DOWN, buff=0.45, aligned_edge=LEFT)
        eq_lines = _reveal(self, line5, eq_lines, run_time=0.7, wait=0.5)

        # ── Line 6: eigenvalues (colour-coded) ────────────────────────────
        self.play(FadeOut(caption_d, run_time=0.3))
        caption_e = make_caption("Two eigenvalues found!")
        self.play(FadeIn(caption_e, shift=UP * 0.2, run_time=0.4))

        line6 = MathTex(
            r"\lambda_1 = ", r"3", r"\quad \lambda_2 = ", r"1",
            font_size=50,
        )
        line6[0].set_color(MAIN_TEXT)
        line6[1].set_color(EIG_AMBER)   # 3 → amber
        line6[2].set_color(MAIN_TEXT)
        line6[3].set_color(EIG_TEAL)    # 1 → teal
        line6.next_to(line5, DOWN, buff=0.5, aligned_edge=LEFT)
        eq_lines = _reveal(self, line6, eq_lines, run_time=0.7, wait=0.3)

        # Surround eigenvalue line with matching rectangles
        rect6 = SurroundingRectangle(
            line6, color=EIG_AMBER, buff=0.2, corner_radius=0.1, stroke_width=2,
        )
        self.play(Create(rect6, run_time=0.5))
        self.play(rect6.animate(rate_func=there_and_back).set_stroke(width=4),
                  run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(caption_e, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # SECTION B – Solve eigenvectors
        # Clear the screen for a fresh vertical stack on the right side
        # ══════════════════════════════════════════════════════════════════
        self.play(
            FadeOut(VGroup(*eq_lines, rect6), run_time=0.8),
        )

        # ── Mini plane on the right for arrow display ──────────────────────
        mini_plane = NumberPlane(
            x_range=[-3.5, 3.5],
            y_range=[-3, 3],
            x_length=4,
            y_length=4,
            background_line_style={
                "stroke_color": "#2A3458",
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
            axis_config={"stroke_color": AXES_COL, "stroke_width": 1},
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)
        self.play(Create(mini_plane, run_time=0.6))

        # ── Eigenvector 1: λ = 3, v = (1,1) ────────────────────────────────
        caption_f = make_caption("Solving (A − 3I)v = 0 gives y = x")
        self.play(FadeIn(caption_f, shift=UP * 0.2, run_time=0.4))

        ev3_lines = []

        s_ev3_1 = MathTex(
            r"A - 3I = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}",
            font_size=38, color=MAIN_TEXT,
        ).move_to(UP * 2.3 + LEFT * 2.2)
        ev3_lines = _reveal(self, s_ev3_1, ev3_lines, run_time=0.7, wait=0.4)

        s_ev3_2 = MathTex(
            r"\Rightarrow -x + y = 0 \Rightarrow y = x",
            font_size=38, color=MAIN_TEXT,
        ).next_to(s_ev3_1, DOWN, buff=0.4, aligned_edge=LEFT)
        ev3_lines = _reveal(self, s_ev3_2, ev3_lines, run_time=0.6, wait=0.4)

        s_ev3_3 = MathTex(
            r"\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}",
            font_size=46, color=EIG_AMBER,
        ).next_to(s_ev3_2, DOWN, buff=0.4, aligned_edge=LEFT)
        ev3_lines = _reveal(self, s_ev3_3, ev3_lines, run_time=0.6, wait=0.3)

        # Arrow appear on mini plane
        # The mini_plane is shifted right so we compute in its local coords
        plane_origin = mini_plane.c2p(0, 0)
        tip_v1       = mini_plane.c2p(1, 1)
        arr_v1 = Arrow(
            start=plane_origin, end=tip_v1,
            buff=0, color=EIG_AMBER, stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )
        lbl_v1 = MathTex(r"(1,1)", font_size=22, color=EIG_AMBER)
        lbl_v1.next_to(tip_v1, UR, buff=0.08)
        self.play(GrowArrow(arr_v1), FadeIn(lbl_v1, run_time=0.3))
        self.play(
            Flash(arr_v1, color=EIG_AMBER, flash_radius=0.4, run_time=0.5),
        )
        self.play(FadeOut(caption_f, run_time=0.3))

        # ── Eigenvector 2: λ = 1, v = (1,−1) ──────────────────────────────
        caption_g = make_caption("Solving (A − I)v = 0 gives y = −x")
        self.play(FadeIn(caption_g, shift=UP * 0.2, run_time=0.4))

        s_ev1_1 = MathTex(
            r"A - I = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}",
            font_size=38, color=MAIN_TEXT,
        ).next_to(s_ev3_3, DOWN, buff=0.5, aligned_edge=LEFT)
        ev3_lines = _reveal(self, s_ev1_1, ev3_lines, run_time=0.6, wait=0.4)

        s_ev1_2 = MathTex(
            r"\Rightarrow x + y = 0 \Rightarrow y = -x",
            font_size=38, color=MAIN_TEXT,
        ).next_to(s_ev1_1, DOWN, buff=0.4, aligned_edge=LEFT)
        ev3_lines = _reveal(self, s_ev1_2, ev3_lines, run_time=0.6, wait=0.4)

        s_ev1_3 = MathTex(
            r"\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}",
            font_size=46, color=EIG_TEAL,
        ).next_to(s_ev1_2, DOWN, buff=0.4, aligned_edge=LEFT)
        ev3_lines = _reveal(self, s_ev1_3, ev3_lines, run_time=0.6, wait=0.3)

        tip_v2 = mini_plane.c2p(1, -1)
        arr_v2 = Arrow(
            start=plane_origin, end=tip_v2,
            buff=0, color=EIG_TEAL, stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )
        lbl_v2 = MathTex(r"(1,-1)", font_size=22, color=EIG_TEAL)
        lbl_v2.next_to(tip_v2, DR, buff=0.08)
        self.play(GrowArrow(arr_v2), FadeIn(lbl_v2, run_time=0.3))
        self.play(
            Flash(arr_v2, color=EIG_TEAL, flash_radius=0.4, run_time=0.5),
        )
        self.play(FadeOut(caption_g, run_time=0.3))

        self.wait(0.5)

        # ══════════════════════════════════════════════════════════════════
        # SECTION C – Verification checks
        # ══════════════════════════════════════════════════════════════════
        self.play(
            FadeOut(VGroup(*ev3_lines), run_time=0.6),
        )

        caption_h = make_caption("Verification: substitute back and check")
        self.play(FadeIn(caption_h, shift=UP * 0.2, run_time=0.4))

        verify_lines = []

        v_eq1 = MathTex(
            r"A\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}3\\3\end{pmatrix}=3\begin{pmatrix}1\\1\end{pmatrix}",
            font_size=38, color=EIG_AMBER,
        ).move_to(UP * 1.3 + LEFT * 2)
        verify_lines = _reveal(self, v_eq1, verify_lines, run_time=0.7, wait=0.4)
        self.play(Flash(v_eq1, color=EIG_AMBER, flash_radius=0.6, run_time=0.6))

        tick1 = Text("✓", font_size=42, color=EIG_AMBER)
        tick1.next_to(v_eq1, RIGHT, buff=0.3)
        self.play(FadeIn(tick1, run_time=0.3))

        v_eq2 = MathTex(
            r"A\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}1\\-1\end{pmatrix}=1\cdot\begin{pmatrix}1\\-1\end{pmatrix}",
            font_size=38, color=EIG_TEAL,
        ).next_to(v_eq1, DOWN, buff=0.5, aligned_edge=LEFT)
        verify_lines = _reveal(self, v_eq2, verify_lines, run_time=0.7, wait=0.4)
        self.play(Flash(v_eq2, color=EIG_TEAL, flash_radius=0.6, run_time=0.6))

        tick2 = Text("✓", font_size=42, color=EIG_TEAL)
        tick2.next_to(v_eq2, RIGHT, buff=0.3)
        self.play(FadeIn(tick2, run_time=0.3))

        self.play(FadeOut(caption_h, run_time=0.3))
        self.wait(3.0)   # hold to reach ~90 s total

        # ── Fade out ───────────────────────────────────────────────────────
        all_mobs = [m for m in self.mobjects]
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
