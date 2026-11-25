"""
scene_3b.py – Power Iteration: "What happens if we apply A again and again?"
(target ~50 seconds)

VIVA EXPLANATION:
  This scene demonstrates the concept of power iteration — repeatedly applying
  matrix A to a vector. The key insight is that the dominant eigenvector
  (the one with the larger eigenvalue) wins: its component grows as 3^n while
  the other component stays at 1^n = 1. So any starting vector eventually
  aligns with the (1,1) direction (amber eigenvector).

Sub-parts:
  a) Show v = (1,0) on the grid.
  b) Apply A once: A^1 v = (2,1). Arrow appears with trail.
  c) Apply A again: A^2 v = (5,4). Arrow appears with trail.
  d) Apply A again: A^3 v = (14,13). Arrow appears with trail.
  e) Show angle to y=x shrinking after each step (angle arcs + degree labels).
  f) Eigendecomposition:
       (1,0) = ½(1,1) + ½(1,-1)
       A^n(1,0) = (3^n/2)(1,1) + (1^n/2)(1,-1)
     → as n grows, 3^n term dominates → vector swings to (1,1) direction.
  g) Caption: "The bigger eigenvalue wins: 3^n grows, 1^n stays at 1."
"""

import numpy as np
from manim import *
from helpers import (
    BACKGROUND, GRID_ORIG, AXES_COL,
    MAIN_TEXT, EIG_AMBER, EIG_TEAL, HIGHLIGHT,
    make_title_text, make_matrix_mob, make_caption,
    A_MAT,
)


def _unit_arrow(v2d: np.ndarray, color: str, length: float = 2.2) -> Arrow:
    """
    Create an Arrow in the direction of v2d but with a fixed display length.
    We normalise so that even A^3 v = (14,13) fits on screen.
    """
    norm = np.linalg.norm(v2d)
    if norm < 1e-9:
        return Arrow(ORIGIN, RIGHT * length, buff=0, color=color,
                     stroke_width=4, max_tip_length_to_length_ratio=0.12)
    tip = (v2d / norm) * length
    return Arrow(ORIGIN, np.array([tip[0], tip[1], 0]),
                 buff=0, color=color, stroke_width=4,
                 max_tip_length_to_length_ratio=0.12)


def _angle_to_yx(v2d: np.ndarray) -> float:
    """Return the angle (radians) between v2d and the y=x line."""
    theta = np.arctan2(v2d[1], v2d[0])      # angle of v
    target = np.pi / 4                       # y=x is at 45°
    return abs(target - theta)


class PowerIteration(MovingCameraScene):
    """
    Demonstrates power iteration on A = [[2,1],[1,2]].
    Uses MovingCameraScene for a subtle zoom during the equation reveal.
    """

    def construct(self):
        self.camera.background_color = BACKGROUND
        self.camera.frame.save_state()

        # ── Labels ─────────────────────────────────────────────────────────
        title   = make_title_text("Scene 3b – Power Iteration")
        mat_mob = make_matrix_mob()          # shows A in top-right corner
        self.add(title, mat_mob)

        caption_intro = make_caption("What happens if we apply A again and again?")
        self.play(FadeIn(caption_intro, shift=UP * 0.2, run_time=0.5))

        # ── Grid ───────────────────────────────────────────────────────────
        plane = NumberPlane(
            x_range=[-5, 5], y_range=[-3.5, 3.5],
            background_line_style={
                "stroke_color": GRID_ORIG,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
            axis_config={"stroke_color": AXES_COL, "stroke_width": 1.5},
        )
        self.play(Create(plane, run_time=0.8, rate_func=smooth))

        # ── Guide line y = x (amber dashed) ───────────────────────────────
        guide_yx = DashedLine(
            np.array([-3.5, -3.5, 0]), np.array([3.5, 3.5, 0]),
            color=EIG_AMBER, stroke_width=1.5,
            dash_length=0.2, stroke_opacity=0.5,
        )
        self.play(Create(guide_yx, run_time=0.5))
        guide_lbl = Text("y = x", font_size=20, color=EIG_AMBER)
        guide_lbl.next_to(np.array([2.8, 2.8, 0]), UR, buff=0.1)
        self.play(FadeIn(guide_lbl, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # VECTORS: v, Av, A²v, A³v
        # Actual values:  v=(1,0)  Av=(2,1)  A²v=(5,4)  A³v=(14,13)
        # We show them normalised to length 2.2 so all fit on screen,
        # and label each with its actual coordinate tuple.
        # ══════════════════════════════════════════════════════════════════
        powers = [
            (np.array([1.0,  0.0]), MAIN_TEXT,  "(1, 0)",    r"v"),
            (np.array([2.0,  1.0]), MAIN_TEXT,  "(2, 1)",    r"Av"),
            (np.array([5.0,  4.0]), MAIN_TEXT,  "(5, 4)",    r"A^2 v"),
            (np.array([14.0,13.0]), MAIN_TEXT,  "(14, 13)",  r"A^3 v"),
        ]

        arrows    = []   # displayed arrow mobs
        arc_mobs  = []   # angle arc mobs
        shown_mobs = []  # everything to fade at end

        self.play(FadeOut(caption_intro, run_time=0.3))
        caption_pw = make_caption("Each application of A rotates the vector closer to y = x")
        self.play(FadeIn(caption_pw, shift=UP * 0.2, run_time=0.4))

        for i, (v2d, color, coord_str, tex_str) in enumerate(powers):
            arr = _unit_arrow(v2d, color)
            arrows.append(arr)

            # Coordinate label next to arrow tip
            tip_norm = arr.get_end()
            lbl = MathTex(tex_str + r"= \mathbf{" + coord_str + r"}",
                          font_size=22, color=color)
            lbl.next_to(tip_norm, RIGHT if tip_norm[0] >= 0 else LEFT, buff=0.12)

            # Angle arc: gap between this vector and y=x
            angle_v  = np.arctan2(v2d[1], v2d[0])
            gap      = max(np.pi / 4 - angle_v, 0)   # angle to y=x line
            gap_deg  = np.degrees(gap)
            arc_r    = 0.55 + 0.12 * i
            arc      = Arc(
                radius=arc_r,
                start_angle=angle_v,
                angle=gap,
                color=HIGHLIGHT,
                stroke_width=1.5,
            )
            angle_lbl = Text(f"{gap_deg:.1f}°", font_size=16, color=HIGHLIGHT)
            # Place label halfway around the arc
            mid_angle = angle_v + gap / 2
            angle_lbl.move_to(np.array([
                (arc_r + 0.25) * np.cos(mid_angle),
                (arc_r + 0.25) * np.sin(mid_angle), 0
            ]))

            if i == 0:
                self.play(GrowArrow(arr), FadeIn(lbl, run_time=0.3),
                          run_time=0.6)
                self.play(Create(arc), FadeIn(angle_lbl, run_time=0.3))
            else:
                # Dim previous arrows to 30 %
                self.play(
                    *[a.animate.set_opacity(0.3) for a in arrows[:-1]],
                    run_time=0.3,
                )
                self.play(GrowArrow(arr), FadeIn(lbl, run_time=0.3),
                          run_time=0.7, rate_func=smooth)
                self.play(Create(arc), FadeIn(angle_lbl, run_time=0.3))
                # Indicate: vector aligns more with amber guide
                if i == 3:
                    self.play(
                        Flash(arr, color=EIG_AMBER, flash_radius=0.4,
                              run_time=0.5),
                    )

            arc_mobs.extend([arc, angle_lbl])
            shown_mobs.extend([arr, lbl])
            self.wait(1.5)   # pause so viewer can read

        # ── Zoom in slightly for the equation block ────────────────────────
        self.play(
            self.camera.frame.animate(rate_func=smooth)
                .scale(0.90).shift(RIGHT * 0.5),
            run_time=1.0,
        )

        self.play(FadeOut(caption_pw, run_time=0.3))
        caption_eq = make_caption(
            "Eigendecomposition explains the convergence"
        )
        self.play(FadeIn(caption_eq, shift=UP * 0.2, run_time=0.4))

        # ══════════════════════════════════════════════════════════════════
        # EIGENDECOMPOSITION EQUATIONS (revealed one line at a time)
        # Placed in lower-left so they don't overlap the arrows.
        # ══════════════════════════════════════════════════════════════════
        eq_anchor = LEFT * 3.8 + DOWN * 1.0   # anchor for the block

        eq1 = MathTex(
            r"(1,0) = \tfrac{1}{2}(1,1) + \tfrac{1}{2}(1,-1)",
            font_size=32, color=MAIN_TEXT,
        ).move_to(eq_anchor).align_to(eq_anchor, LEFT)

        eq2 = MathTex(
            r"A^n(1,0) = \frac{3^n}{2}(1,1) + \frac{1^n}{2}(1,-1)",
            font_size=32, color=MAIN_TEXT,
        ).next_to(eq1, DOWN, buff=0.35, aligned_edge=LEFT)

        eq3 = MathTex(
            r"\text{As } n \to \infty,\ 3^n \gg 1^n"
            r"\implies \text{direction} \to (1,1)",
            font_size=28, color=EIG_AMBER,
        ).next_to(eq2, DOWN, buff=0.35, aligned_edge=LEFT)

        eq_mobs = []
        for eq in [eq1, eq2, eq3]:
            if eq_mobs:
                self.play(
                    *[e.animate.set_opacity(0.4) for e in eq_mobs],
                    run_time=0.3,
                )
            self.play(FadeIn(eq, shift=UP * 0.25, run_time=0.7, rate_func=smooth))
            eq_mobs.append(eq)
            self.wait(2.0)   # reader pause after each equation

        # Surround equation block with amber rectangle
        rect = SurroundingRectangle(
            VGroup(eq1, eq2, eq3), color=EIG_AMBER,
            buff=0.2, corner_radius=0.1, stroke_width=2,
        )
        self.play(Create(rect, run_time=0.6, rate_func=smooth))

        # ── Final caption ──────────────────────────────────────────────────
        self.play(FadeOut(caption_eq, run_time=0.3))
        caption_final = make_caption(
            "The bigger eigenvalue wins: 3ⁿ grows, 1ⁿ stays at 1"
        )
        self.play(FadeIn(caption_final, shift=UP * 0.2, run_time=0.5))

        # Zoom back out
        self.play(
            self.camera.frame.animate(rate_func=smooth).restore(),
            run_time=0.8,
        )

        self.wait(2.5)

        # ── Fade everything out ────────────────────────────────────────────
        self.play(
            *[FadeOut(m) for m in self.mobjects
              if m is not self.camera.frame],
            run_time=1.0,
        )
