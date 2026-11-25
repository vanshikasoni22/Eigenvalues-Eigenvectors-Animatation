"""
scene_1.py – Hook: "Which directions don't turn?" (target: ~35 seconds)

What happens here:
  1. The plane with a grid is shown.
  2. Eight unit arrows at different angles are drawn in white.
  3. Matrix A is applied to the grid (smooth, 3 s) using apply_matrix()
     which is the correct LinearTransformationScene API.
  4. Six arrows that rotated off their lines are flashed magenta, then dimmed.
  5. The two eigenvector arrows that stayed on their lines are highlighted
     amber (λ=3) and teal (λ=1) with a soft pulse.
  6. Caption: "Which directions don't turn?"

FIX: get_matrix_transformation() returns a function, NOT an Animation.
     The correct call is self.apply_matrix(..., added_anims=[...]).
"""

import numpy as np
from manim import *
from helpers import (
    BACKGROUND, GRID_ORIG, GRID_TRSF, AXES_COL,
    MAIN_TEXT, EIG_AMBER, EIG_TEAL, HIGHLIGHT,
    make_title_text, make_matrix_mob, make_caption,
)

A_MAT = np.array([[2, 1], [1, 2]], dtype=float)

# 8 unit directions (degrees). Index 2 = 45° → eigenvector (1,1), amber.
# Index 6 = 135° → eigenvector (1,−1), teal.
ARROW_ANGLES_DEG = [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5]


class Hook(LinearTransformationScene):
    """
    Uses LinearTransformationScene for automatic grid colouring + apply_matrix().
    apply_matrix() accepts added_anims= for simultaneous arrow morphing.
    """

    def __init__(self, **kwargs):
        super().__init__(
            include_foreground_plane=True,
            include_background_plane=True,
            background_plane_kwargs={
                "x_range": [-7, 7],
                "y_range": [-4, 4],
                "background_line_style": {
                    "stroke_color": GRID_ORIG,
                    "stroke_width": 1,
                    "stroke_opacity": 0.6,
                },
            },
            foreground_plane_kwargs={
                "x_range": [-7, 7],
                "y_range": [-4, 4],
                "background_line_style": {
                    "stroke_color": GRID_TRSF,
                    "stroke_width": 1,
                    "stroke_opacity": 0.5,
                },
                "axis_config": {"stroke_color": AXES_COL},
            },
            show_coordinates=False,
            **kwargs,
        )

    def construct(self):
        self.camera.background_color = BACKGROUND

        # ── Labels ─────────────────────────────────────────────────────────
        title   = make_title_text("Scene 1 – Hook")
        mat_mob = make_matrix_mob()
        caption = make_caption("Which directions don't turn?")
        self.add(title, mat_mob)

        # ── Build 8 unit arrows (pre-transform positions) ──────────────────
        arrows = []
        for deg in ARROW_ANGLES_DEG:
            rad = np.deg2rad(deg)
            tip = np.array([np.cos(rad), np.sin(rad), 0])
            arr = Arrow(
                start=ORIGIN, end=tip,
                color=MAIN_TEXT, buff=0,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.2,
            )
            arrows.append(arr)

        # Fade all arrows in with a stagger
        self.play(
            LaggedStart(
                *[FadeIn(a, run_time=0.15) for a in arrows],
                lag_ratio=0.12,
            )
        )
        self.play(FadeIn(caption, shift=UP * 0.2, run_time=0.4))
        self.wait(0.4)

        # ── Compute post-transform unit tips for each arrow ────────────────
        # We build replacement Arrow objects at the transformed directions.
        arrows_post = []
        for i, deg in enumerate(ARROW_ANGLES_DEG):
            rad = np.deg2rad(deg)
            v   = np.array([np.cos(rad), np.sin(rad)])
            Av  = A_MAT @ v
            tip_unit = Av / np.linalg.norm(Av)   # keep display length = 1

            color = MAIN_TEXT
            if i == 2:   # 45° = eigenvector (1,1) → amber
                color = EIG_AMBER
            elif i == 6: # 135° = eigenvector (1,−1) → teal
                color = EIG_TEAL

            arr_post = Arrow(
                start=ORIGIN,
                end=np.array([tip_unit[0], tip_unit[1], 0]),
                color=color, buff=0,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.2,
            )
            arrows_post.append(arr_post)

        # ── Apply A to the grid + morph arrows simultaneously ──────────────
        # apply_matrix() is the correct LinearTransformationScene API.
        # added_anims runs alongside the grid transform.
        morph_anims = [
            Transform(pre, post, rate_func=smooth)
            for pre, post in zip(arrows, arrows_post)
        ]

        self.apply_matrix(
            A_MAT,
            added_anims=morph_anims,
            run_time=3,
            rate_func=smooth,
        )
        self.wait(1)   # required 1-second pause after transform

        # ── Flash non-eigenvector arrows magenta, then dim them ────────────
        non_eig_idx = [i for i in range(8) if i not in (2, 6)]
        self.play(
            LaggedStart(
                *[
                    Indicate(arrows[i], color=HIGHLIGHT,
                             scale_factor=1.3, run_time=0.4)
                    for i in non_eig_idx
                ],
                lag_ratio=0.08,
            )
        )
        self.play(
            *[arrows[i].animate.set_opacity(0.2) for i in non_eig_idx],
            run_time=0.5,
        )

        # ── Pulse the two eigenvector arrows ──────────────────────────────
        self.play(
            Flash(arrows[2], color=EIG_AMBER, flash_radius=0.6, run_time=0.6),
            Flash(arrows[6], color=EIG_TEAL,  flash_radius=0.6, run_time=0.6),
        )
        self.play(
            arrows[2].animate(rate_func=there_and_back).scale(1.3),
            arrows[6].animate(rate_func=there_and_back).scale(1.3),
            run_time=0.8,
        )

        # ── Eigenvector labels ─────────────────────────────────────────────
        label_amber = Text("λ = 3", font_size=26, color=EIG_AMBER)
        label_amber.next_to(arrows[2].get_end(), RIGHT, buff=0.15)
        label_teal  = Text("λ = 1", font_size=26, color=EIG_TEAL)
        label_teal.next_to(arrows[6].get_end(), LEFT, buff=0.15)

        self.play(
            FadeIn(label_amber, shift=UP * 0.15),
            FadeIn(label_teal,  shift=UP * 0.15),
            run_time=0.5,
        )

        self.wait(2.5)   # hold so scene reaches ~35 s

        # ── Fade everything out ────────────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
