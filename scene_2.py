"""
scene_2.py – Concept: Av = λv  (target: ~40 seconds)

What happens here:
  1. The core equation Av = λv is written big in the centre.
     • v is white (MAIN_TEXT), λ is amber (EIG_AMBER).
  2. Three short definition lines appear one at a time below the equation.
     When a new line appears the previous one dims to 40 % opacity.
  3. A SurroundingRectangle (amber) frames the equation to close the scene.
  4. Everything fades out over 1 s.

This scene is purely typographic – no grid.
"""

from manim import *
from helpers import (
    BACKGROUND, MAIN_TEXT, AXES_COL, EIG_AMBER,
    make_title_text, make_matrix_mob, make_caption,
)


class ConceptEquation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        # ── Labels ─────────────────────────────────────────────────────────
        title   = make_title_text("Scene 2 – The Core Equation")
        mat_mob = make_matrix_mob()
        caption = make_caption("Av = λv  defines eigenvalues and eigenvectors")
        self.add(title, mat_mob)

        # ── Main equation with colour ──────────────────────────────────────
        # We build it as a MathTex with coloured parts:
        #   A  v  =  λ  v
        eq = MathTex(
            r"A",        # [0]
            r"\mathbf{v}",  # [1]
            r"=",        # [2]
            r"\lambda",  # [3]
            r"\mathbf{v}",  # [4]
            font_size=96,
        )
        eq[0].set_color(MAIN_TEXT)
        eq[1].set_color(MAIN_TEXT)
        eq[2].set_color(MAIN_TEXT)
        eq[3].set_color(EIG_AMBER)   # λ in amber
        eq[4].set_color(MAIN_TEXT)
        eq.move_to(UP * 1.2)

        # Write the equation letter-by-letter
        self.play(Write(eq, run_time=1.4, rate_func=smooth))
        self.wait(0.4)

        # ── Three definition lines ─────────────────────────────────────────
        defs = [
            (r"\mathbf{v}\ \text{is a non-zero vector}",    MAIN_TEXT),
            (r"\lambda\ \text{is the scaling factor (eigenvalue)}",  EIG_AMBER),
            (r"A\ \text{transforms}\ \mathbf{v}\ \text{without changing its direction}",
             MAIN_TEXT),
        ]

        def_mobs = []
        for i, (tex, color) in enumerate(defs):
            mob = MathTex(tex, font_size=38, color=color)
            if i == 0:
                mob.next_to(eq, DOWN, buff=0.7)
            else:
                mob.next_to(def_mobs[-1], DOWN, buff=0.35)
            def_mobs.append(mob)

        for i, mob in enumerate(def_mobs):
            # Dim previous line(s) to 40 %
            dim_anims = [
                prev.animate.set_opacity(0.4) for prev in def_mobs[:i]
            ]
            # Optionally also dim the equation slightly after line 2
            if i == 2:
                dim_anims.append(eq.animate.set_opacity(0.65))

            if dim_anims:
                self.play(*dim_anims, run_time=0.35)

            # Reveal current line
            self.play(
                FadeIn(mob, shift=UP * 0.3, run_time=0.6, rate_func=smooth)
            )
            self.wait(0.5)

        # Restore full opacity on the equation for the rectangle
        self.play(eq.animate.set_opacity(1.0), run_time=0.3)

        # ── SurroundingRectangle around the equation ───────────────────────
        rect = SurroundingRectangle(
            eq,
            color=EIG_AMBER,
            buff=0.25,
            corner_radius=0.12,
            stroke_width=2.5,
        )
        self.play(Create(rect, run_time=0.8, rate_func=smooth))

        # Soft pulse on rectangle
        self.play(
            rect.animate(rate_func=there_and_back).set_stroke(width=5),
            run_time=0.6,
        )

        self.wait(3.5)   # hold to reach ~40 s total

        # ── Show caption then fade out ─────────────────────────────────────
        self.play(FadeIn(caption, shift=UP * 0.2, run_time=0.5))
        self.wait(0.8)

        self.play(
            *[FadeOut(m) for m in self.mobjects],
            run_time=1.0,
        )
