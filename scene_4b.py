"""
scene_4b.py – Second Worked Example: B = [[4,1],[2,3]]
(target ~60 seconds)

VIVA EXPLANATION:
  This scene reinforces the eigenvalue calculation method on a different matrix.
  B = [[4,1],[2,3]] is NOT symmetric (unlike A = [[2,1],[1,2]]), which makes
  it a richer example. We follow exactly the same steps as scene_4:
    1. Write (B − λI)v = 0.
    2. Set det(B − λI) = 0 and expand.
    3. Factor to find λ = 5 and λ = 2.
    4. Solve each system for the eigenvector.
    5. Verify by substitution.
    6. Show det = λ₁λ₂ and trace = λ₁+λ₂.
  Colour convention: λ=5 → amber, λ=2 → teal (matches A's λ=3 and λ=1).

Derivation facts:
  det(B − λI) = (4−λ)(3−λ) − 1·2 = 12 − 7λ + λ² − 2 = λ² − 7λ + 10
              = (λ−5)(λ−2) = 0.
  λ=5: (B−5I)v=0 → [[-1,1],[2,-2]]v=0 → −x+y=0 → y=x → v=(1,1).
  λ=2: (B−2I)v=0 → [[2,1],[2,1]]v=0 → 2x+y=0 → y=−2x → v=(1,−2).
  B(1,1) = (5,5) = 5(1,1) ✓   B(1,−2) = (2,−4) = 2(1,−2) ✓
  trace(B) = 7 = 5+2 ✓   det(B) = 10 = 5×2 ✓
"""

import numpy as np
from manim import *
from helpers import (
    BACKGROUND, GRID_ORIG, GRID_TRSF, AXES_COL,
    MAIN_TEXT, EIG_AMBER, EIG_TEAL,
    make_title_text, make_caption,
)

B_MAT = np.array([[4, 1], [2, 3]], dtype=float)


def _reveal_eq(scene: Scene, mob_new: VMobject, prev: list,
               run_time: float = 0.65, wait: float = 1.5):
    """Dim previous equations to 40 %, then FadeIn the new one."""
    if prev:
        scene.play(*[m.animate.set_opacity(0.4) for m in prev], run_time=0.3)
    scene.play(FadeIn(mob_new, shift=UP * 0.25, run_time=run_time, rate_func=smooth))
    scene.wait(wait)
    return prev + [mob_new]


class SecondExample(MovingCameraScene):
    """
    Full eigen-calculation for B = [[4,1],[2,3]] shown step-by-step.
    Uses MovingCameraScene for a slight zoom-in during the algebra section.
    """

    def construct(self):
        self.camera.background_color = BACKGROUND
        self.camera.frame.save_state()

        # ── Top-right matrix label (B, not A) ─────────────────────────────
        title   = make_title_text("Scene 4b – Second Example")
        mat_mob = MathTex(
            r"B = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}",
            color=MAIN_TEXT, font_size=36,
        ).to_corner(UR, buff=0.3)
        self.add(title, mat_mob)

        caption_intro = make_caption(
            "Let us try a second matrix B = [[4,1],[2,3]]"
        )
        self.play(FadeIn(caption_intro, shift=UP * 0.2, run_time=0.5))
        self.wait(1.5)

        # ══════════════════════════════════════════════════════════════════
        # SECTION A – Characteristic polynomial (left half of screen)
        # ══════════════════════════════════════════════════════════════════
        self.play(FadeOut(caption_intro, run_time=0.3))
        caption_a = make_caption("Step 1 – characteristic polynomial of B")
        self.play(FadeIn(caption_a, shift=UP * 0.2, run_time=0.4))

        # Zoom in slightly for algebra
        self.play(
            self.camera.frame.animate(rate_func=smooth).scale(0.88),
            run_time=0.8,
        )

        eq_lines = []
        anchor   = UP * 2.4 + LEFT * 3.0

        L1 = MathTex(r"\det(B-\lambda I)=0",
                     font_size=42, color=MAIN_TEXT).move_to(anchor).align_to(anchor, LEFT)
        eq_lines = _reveal_eq(self, L1, eq_lines)

        L2 = MathTex(r"(4-\lambda)(3-\lambda) - 2 = 0",
                     font_size=42, color=MAIN_TEXT).next_to(L1, DOWN, buff=0.4, aligned_edge=LEFT)
        eq_lines = _reveal_eq(self, L2, eq_lines)

        L3 = MathTex(r"\lambda^2 - 7\lambda + 10 = 0",
                     font_size=42, color=MAIN_TEXT).next_to(L2, DOWN, buff=0.4, aligned_edge=LEFT)
        eq_lines = _reveal_eq(self, L3, eq_lines)

        L4 = MathTex(r"(\lambda-5)(\lambda-2) = 0",
                     font_size=42, color=MAIN_TEXT).next_to(L3, DOWN, buff=0.4, aligned_edge=LEFT)
        eq_lines = _reveal_eq(self, L4, eq_lines)

        self.play(FadeOut(caption_a, run_time=0.3))
        caption_b = make_caption("Two eigenvalues: λ = 5 (amber) and λ = 2 (teal)")
        self.play(FadeIn(caption_b, shift=UP * 0.2, run_time=0.4))

        L5 = MathTex(r"\lambda_1 =", r"5", r"\quad \lambda_2 =", r"2",
                     font_size=48)
        L5[0].set_color(MAIN_TEXT)
        L5[1].set_color(EIG_AMBER)
        L5[2].set_color(MAIN_TEXT)
        L5[3].set_color(EIG_TEAL)
        L5.next_to(L4, DOWN, buff=0.45, aligned_edge=LEFT)
        eq_lines = _reveal_eq(self, L5, eq_lines, wait=0.5)

        rect5 = SurroundingRectangle(L5, color=EIG_AMBER, buff=0.2,
                                     corner_radius=0.1, stroke_width=2)
        self.play(Create(rect5, run_time=0.5))
        self.play(rect5.animate(rate_func=there_and_back).set_stroke(width=4),
                  run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(caption_b, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # SECTION B – Eigenvectors + mini plane
        # ══════════════════════════════════════════════════════════════════
        self.play(FadeOut(VGroup(*eq_lines, rect5), run_time=0.6))
        self.play(self.camera.frame.animate.restore(), run_time=0.5)

        # Mini plane on the right
        mini_plane = NumberPlane(
            x_range=[-3, 3], y_range=[-3, 3],
            x_length=4.2, y_length=4.2,
            background_line_style={
                "stroke_color": GRID_ORIG,
                "stroke_width": 1, "stroke_opacity": 0.5,
            },
            axis_config={"stroke_color": AXES_COL, "stroke_width": 1},
        ).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.1)
        self.play(Create(mini_plane, run_time=0.6))

        # ── Eigenvector for λ = 5: v = (1,1) ──────────────────────────────
        caption_c = make_caption("Solving (B − 5I)v = 0  →  y = x  →  v = (1,1)")
        self.play(FadeIn(caption_c, shift=UP * 0.2, run_time=0.4))

        ev5_lines = []
        s1 = MathTex(r"B - 5I = \begin{pmatrix}-1&1\\2&-2\end{pmatrix}",
                     font_size=36, color=MAIN_TEXT).move_to(UP * 2.2 + LEFT * 2.2)
        ev5_lines = _reveal_eq(self, s1, ev5_lines, wait=1.0)

        s2 = MathTex(r"\Rightarrow -x + y = 0 \Rightarrow y = x",
                     font_size=36, color=MAIN_TEXT).next_to(s1, DOWN, buff=0.38, aligned_edge=LEFT)
        ev5_lines = _reveal_eq(self, s2, ev5_lines, wait=1.0)

        s3 = MathTex(r"\mathbf{v}_1 = \begin{pmatrix}1\\1\end{pmatrix}",
                     font_size=44, color=EIG_AMBER).next_to(s2, DOWN, buff=0.38, aligned_edge=LEFT)
        ev5_lines = _reveal_eq(self, s3, ev5_lines, wait=0.5)

        # Arrow on mini plane for (1,1)
        o = mini_plane.c2p(0, 0)
        t1 = mini_plane.c2p(1, 1)
        arr1 = Arrow(o, t1, buff=0, color=EIG_AMBER, stroke_width=4,
                     max_tip_length_to_length_ratio=0.15)
        lbl1 = MathTex(r"(1,1)", font_size=20, color=EIG_AMBER).next_to(t1, UR, buff=0.08)
        self.play(GrowArrow(arr1), FadeIn(lbl1, run_time=0.3))
        self.play(Flash(arr1, color=EIG_AMBER, flash_radius=0.4, run_time=0.5))
        self.wait(1.0)
        self.play(FadeOut(caption_c, run_time=0.3))

        # ── Eigenvector for λ = 2: v = (1,−2) ─────────────────────────────
        caption_d = make_caption("Solving (B − 2I)v = 0  →  y = −2x  →  v = (1,−2)")
        self.play(FadeIn(caption_d, shift=UP * 0.2, run_time=0.4))

        s4 = MathTex(r"B - 2I = \begin{pmatrix}2&1\\2&1\end{pmatrix}",
                     font_size=36, color=MAIN_TEXT).next_to(s3, DOWN, buff=0.5, aligned_edge=LEFT)
        ev5_lines = _reveal_eq(self, s4, ev5_lines, wait=1.0)

        s5 = MathTex(r"\Rightarrow 2x + y = 0 \Rightarrow y = -2x",
                     font_size=36, color=MAIN_TEXT).next_to(s4, DOWN, buff=0.38, aligned_edge=LEFT)
        ev5_lines = _reveal_eq(self, s5, ev5_lines, wait=1.0)

        s6 = MathTex(r"\mathbf{v}_2 = \begin{pmatrix}1\\-2\end{pmatrix}",
                     font_size=44, color=EIG_TEAL).next_to(s5, DOWN, buff=0.38, aligned_edge=LEFT)
        ev5_lines = _reveal_eq(self, s6, ev5_lines, wait=0.5)

        t2 = mini_plane.c2p(1, -2)
        arr2 = Arrow(o, t2, buff=0, color=EIG_TEAL, stroke_width=4,
                     max_tip_length_to_length_ratio=0.15)
        lbl2 = MathTex(r"(1,-2)", font_size=20, color=EIG_TEAL).next_to(t2, DR, buff=0.08)
        self.play(GrowArrow(arr2), FadeIn(lbl2, run_time=0.3))
        self.play(Flash(arr2, color=EIG_TEAL, flash_radius=0.4, run_time=0.5))
        self.wait(1.0)
        self.play(FadeOut(caption_d, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # SECTION C – Verification + trace/det
        # ══════════════════════════════════════════════════════════════════
        self.play(FadeOut(VGroup(*ev5_lines), run_time=0.5))

        caption_e = make_caption("Verification: substitution check")
        self.play(FadeIn(caption_e, shift=UP * 0.2, run_time=0.4))

        verify_lines = []
        v1 = MathTex(
            r"B\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}5\\5\end{pmatrix}=5\begin{pmatrix}1\\1\end{pmatrix}",
            font_size=36, color=EIG_AMBER,
        ).move_to(UP * 1.8 + LEFT * 1.8)
        verify_lines = _reveal_eq(self, v1, verify_lines, wait=0.5)
        tick1 = Text("✓", font_size=38, color=EIG_AMBER).next_to(v1, RIGHT, buff=0.25)
        self.play(FadeIn(tick1, run_time=0.3))
        self.play(Flash(v1, color=EIG_AMBER, flash_radius=0.6, run_time=0.5))

        v2 = MathTex(
            r"B\begin{pmatrix}1\\-2\end{pmatrix}=\begin{pmatrix}2\\-4\end{pmatrix}=2\begin{pmatrix}1\\-2\end{pmatrix}",
            font_size=36, color=EIG_TEAL,
        ).next_to(v1, DOWN, buff=0.45, aligned_edge=LEFT)
        verify_lines = _reveal_eq(self, v2, verify_lines, wait=0.5)
        tick2 = Text("✓", font_size=38, color=EIG_TEAL).next_to(v2, RIGHT, buff=0.25)
        self.play(FadeIn(tick2, run_time=0.3))
        self.play(Flash(v2, color=EIG_TEAL, flash_radius=0.6, run_time=0.5))

        self.play(FadeOut(caption_e, run_time=0.3))
        caption_f = make_caption("det and trace connect to eigenvalues")
        self.play(FadeIn(caption_f, shift=UP * 0.2, run_time=0.4))

        td1 = MathTex(
            r"\mathrm{tr}(B) = 4+3 = 7 = ", r"5", r"+", r"2",
            font_size=36,
        ).next_to(v2, DOWN, buff=0.5, aligned_edge=LEFT)
        td1[0].set_color(MAIN_TEXT); td1[1].set_color(EIG_AMBER)
        td1[2].set_color(MAIN_TEXT); td1[3].set_color(EIG_TEAL)
        verify_lines = _reveal_eq(self, td1, verify_lines, wait=0.8)

        td2 = MathTex(
            r"\det(B) = 12-2 = 10 = ", r"5", r"\times", r"2",
            font_size=36,
        ).next_to(td1, DOWN, buff=0.38, aligned_edge=LEFT)
        td2[0].set_color(MAIN_TEXT); td2[1].set_color(EIG_AMBER)
        td2[2].set_color(MAIN_TEXT); td2[3].set_color(EIG_TEAL)
        verify_lines = _reveal_eq(self, td2, verify_lines, wait=1.5)

        self.wait(1.5)

        # ── Fade out ───────────────────────────────────────────────────────
        self.play(
            *[FadeOut(m) for m in self.mobjects
              if m is not self.camera.frame],
            run_time=1.0,
        )
