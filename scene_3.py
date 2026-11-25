"""
scene_3.py – Visual Intuition (target: ~75 seconds – the longest scene)

Sub-parts:
  a) Show the grid + matrix label; apply A smoothly.
  b) Show (1,0) → (2,1): morphs and turns off its line. Dashed original line,
     coloured magenta for "off-line" emphasis.
  c) Show (1,1) → (3,3): amber, stays on y = x, labelled "λ = 3".
  d) Show (1,−1) → (1,−1): teal, unchanged, labelled "λ = 1".
  e) CURVE VISUAL: unit circle + ValueTracker rotating a unit vector v.
     Av traces an ellipse via TracedPath.  Flash amber/teal at eigenvector angles.

Uses NumberPlane directly (not LinearTransformationScene) so we can control
exactly what is drawn and when.
"""

import numpy as np
from manim import *
from helpers import (
    BACKGROUND, GRID_ORIG, GRID_TRSF, AXES_COL,
    MAIN_TEXT, EIG_AMBER, EIG_TEAL, HIGHLIGHT,
    make_title_text, make_matrix_mob, make_caption,
    A_MAT,
)

# ── Helper: apply 2×2 matrix to a 3-D Manim point ──────────────────────────
def apply_A(point: np.ndarray) -> np.ndarray:
    x, y = point[0], point[1]
    nx = 2 * x + y
    ny = x + 2 * y
    return np.array([nx, ny, 0])


class VisualIntuition(MovingCameraScene):
    """
    Uses MovingCameraScene so we can do a subtle slow zoom in/out.
    """

    def construct(self):
        self.camera.background_color = BACKGROUND
        self.camera.frame.save_state()

        # ── Labels ─────────────────────────────────────────────────────────
        title   = make_title_text("Scene 3 – Visual Intuition")
        mat_mob = make_matrix_mob()
        self.add(title, mat_mob)

        # ══════════════════════════════════════════════════════════════════
        # PART A – Grid + smooth transformation
        # ══════════════════════════════════════════════════════════════════
        plane = NumberPlane(
            x_range=[-6, 6],
            y_range=[-4, 4],
            background_line_style={
                "stroke_color": GRID_ORIG,
                "stroke_width": 1,
                "stroke_opacity": 0.7,
            },
            axis_config={"stroke_color": AXES_COL, "stroke_width": 1.5},
            faded_line_ratio=1,
        )
        self.play(Create(plane, run_time=1.2, rate_func=smooth))

        caption_a = make_caption("Applying A to the entire plane…")
        self.play(FadeIn(caption_a, shift=UP * 0.2, run_time=0.4))
        self.wait(0.4)

        # Apply A to every point in the plane
        self.play(
            plane.animate(rate_func=smooth).apply_matrix(
                [[2, 1], [1, 2]]
            ),
            run_time=3,
        )
        self.wait(1)   # required 1 s pause

        # Recolour grid lines to show "transformed" state
        plane.set_color(GRID_TRSF)

        # ══════════════════════════════════════════════════════════════════
        # PART B – (1,0) → (2,1): turns off its line
        # ══════════════════════════════════════════════════════════════════
        self.play(FadeOut(caption_a, run_time=0.3))
        caption_b = make_caption("(1, 0) rotates away from the x-axis after A")
        self.play(FadeIn(caption_b, shift=UP * 0.2, run_time=0.4))

        # Dashed original direction (x-axis unit)
        dashed_orig = DashedLine(
            LEFT * 2.5, RIGHT * 2.5,
            color=HIGHLIGHT, stroke_width=2, dash_length=0.15,
        ).shift(ORIGIN)

        # Pre-transform vector
        v10 = Arrow(ORIGIN, RIGHT, buff=0, color=MAIN_TEXT,
                    stroke_width=4, max_tip_length_to_length_ratio=0.15)
        label_v10 = MathTex(r"\mathbf{e}_1 = (1,0)", font_size=28,
                             color=MAIN_TEXT).next_to(RIGHT, RIGHT, buff=0.1)

        self.play(GrowArrow(v10), FadeIn(label_v10, run_time=0.3))
        self.play(Create(dashed_orig, run_time=0.5))
        self.wait(0.3)

        # Morph v to Av = (2,1)
        tracker_b = ValueTracker(0)
        v_b_start = np.array([1.0, 0.0, 0.0])
        v_b_end   = np.array([2.0, 1.0, 0.0])

        def _build_b():
            t   = tracker_b.get_value()
            tip = v_b_start * (1 - t) + v_b_end * t
            return Arrow(ORIGIN, tip, buff=0, color=HIGHLIGHT,
                         stroke_width=4, max_tip_length_to_length_ratio=0.15)

        v_b_mob = always_redraw(_build_b)
        self.add(v_b_mob)
        self.remove(v10)

        label_Av10 = MathTex(r"A\mathbf{e}_1 = (2,1)", font_size=28,
                              color=HIGHLIGHT)
        label_Av10.next_to(np.array([2, 1, 0]), RIGHT, buff=0.15)

        self.play(
            tracker_b.animate(rate_func=smooth).set_value(1),
            run_time=1.5,
        )
        self.play(
            FadeIn(label_Av10, run_time=0.4),
            Indicate(v_b_mob, color=HIGHLIGHT, scale_factor=1.2, run_time=0.5),
        )
        self.wait(0.5)
        self.play(
            FadeOut(label_v10), FadeOut(label_Av10),
            v_b_mob.animate.set_opacity(0.3),
            dashed_orig.animate.set_opacity(0.3),
            run_time=0.5,
        )
        self.play(FadeOut(caption_b, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # PART C – (1,1) → (3,3): stays on y = x  [amber, λ = 3]
        # ══════════════════════════════════════════════════════════════════
        caption_c = make_caption("(1,1) stays on y = x — scales by λ = 3")
        self.play(FadeIn(caption_c, shift=UP * 0.2, run_time=0.4))

        # y = x guide line
        guide_c = DashedLine(
            np.array([-3.5, -3.5, 0]), np.array([3.5, 3.5, 0]),
            color=EIG_AMBER, stroke_width=1.5, dash_length=0.15, stroke_opacity=0.5,
        )
        self.play(Create(guide_c, run_time=0.5))

        tracker_c = ValueTracker(0)
        v_c_start = np.array([1.0, 1.0, 0.0])
        v_c_end   = np.array([3.0, 3.0, 0.0])

        def _build_c():
            t   = tracker_c.get_value()
            tip = v_c_start * (1 - t) + v_c_end * t
            return Arrow(ORIGIN, tip, buff=0, color=EIG_AMBER,
                         stroke_width=4, max_tip_length_to_length_ratio=0.12)

        v_c_mob = always_redraw(_build_c)
        self.add(v_c_mob)

        label_c_before = MathTex(r"(1,1)", font_size=26, color=EIG_AMBER)
        label_c_before.next_to(np.array([1, 1, 0]), UR, buff=0.1)
        self.play(FadeIn(label_c_before, run_time=0.3))

        self.play(
            tracker_c.animate(rate_func=smooth).set_value(1),
            run_time=1.5,
        )
        label_c_after = MathTex(r"\lambda=3\ \Rightarrow\ (1,1)\to(3,3)",
                                 font_size=26, color=EIG_AMBER)
        label_c_after.next_to(np.array([3, 3, 0]), RIGHT, buff=0.15)
        self.play(FadeIn(label_c_after, run_time=0.4))
        self.play(
            Flash(v_c_mob, color=EIG_AMBER, flash_radius=0.5, run_time=0.6),
            v_c_mob.animate(rate_func=there_and_back).scale(1.2),
        )
        self.wait(0.5)
        self.play(
            FadeOut(label_c_before), FadeOut(label_c_after),
            v_c_mob.animate.set_opacity(0.5),
            guide_c.animate.set_opacity(0.2),
            run_time=0.5,
        )
        self.play(FadeOut(caption_c, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # PART D – (1,−1) → (1,−1): unchanged  [teal, λ = 1]
        # ══════════════════════════════════════════════════════════════════
        caption_d = make_caption("(1,−1) is unchanged — λ = 1 means no scaling")
        self.play(FadeIn(caption_d, shift=UP * 0.2, run_time=0.4))

        guide_d = DashedLine(
            np.array([-3.5, 3.5, 0]), np.array([3.5, -3.5, 0]),
            color=EIG_TEAL, stroke_width=1.5, dash_length=0.15, stroke_opacity=0.5,
        )
        self.play(Create(guide_d, run_time=0.5))

        tracker_d = ValueTracker(0)
        v_d_start = np.array([1.0, -1.0, 0.0])
        v_d_end   = np.array([1.0, -1.0, 0.0])  # no change!

        def _build_d():
            t   = tracker_d.get_value()
            tip = v_d_start * (1 - t) + v_d_end * t
            return Arrow(ORIGIN, tip, buff=0, color=EIG_TEAL,
                         stroke_width=4, max_tip_length_to_length_ratio=0.15)

        v_d_mob = always_redraw(_build_d)
        self.add(v_d_mob)

        label_d = MathTex(r"\lambda=1\ \Rightarrow\ (1,-1)\to(1,-1)",
                          font_size=26, color=EIG_TEAL)
        label_d.next_to(np.array([1, -1, 0]), DR, buff=0.15)

        self.play(
            tracker_d.animate(rate_func=smooth).set_value(1),
            run_time=0.8,
        )
        self.play(FadeIn(label_d, run_time=0.4))
        self.play(
            Flash(v_d_mob, color=EIG_TEAL, flash_radius=0.5, run_time=0.6),
            v_d_mob.animate(rate_func=there_and_back).scale(1.2),
        )
        self.wait(0.5)
        self.play(
            FadeOut(label_d),
            v_d_mob.animate.set_opacity(0.5),
            guide_d.animate.set_opacity(0.2),
            run_time=0.5,
        )
        self.play(FadeOut(caption_d, run_time=0.3))

        # ══════════════════════════════════════════════════════════════════
        # PART E – Curve visual: unit circle → ellipse via TracedPath
        # ══════════════════════════════════════════════════════════════════
        # Fade out the grid so the circle is clearer
        self.play(
            plane.animate.set_opacity(0.2),
            v_b_mob.animate.set_opacity(0.0),
            v_c_mob.animate.set_opacity(0.0),
            v_d_mob.animate.set_opacity(0.0),
            run_time=0.6,
        )

        caption_e = make_caption("Rotating v around the unit circle — Av traces an ellipse")
        self.play(FadeIn(caption_e, shift=UP * 0.2, run_time=0.4))

        # Slow zoom in for the curve visual
        self.play(
            self.camera.frame.animate(rate_func=smooth)
                .scale(0.85)
                .move_to(ORIGIN),
            run_time=1.2,
        )

        # Draw the unit circle (static guide)
        unit_circle = Circle(radius=1, color=AXES_COL, stroke_width=1.5,
                             stroke_opacity=0.6)
        self.play(Create(unit_circle, run_time=0.6))

        # Angle tracker for the rotating unit vector
        angle_tracker = ValueTracker(0)

        # Unit vector v (rotating on the circle)
        def _unit_v():
            theta = angle_tracker.get_value()
            tip   = np.array([np.cos(theta), np.sin(theta), 0])
            return Arrow(ORIGIN, tip, buff=0, color=MAIN_TEXT,
                         stroke_width=3, max_tip_length_to_length_ratio=0.2)

        v_unit = always_redraw(_unit_v)
        self.add(v_unit)

        # Av dot that traces the ellipse
        def _Av_dot():
            theta = angle_tracker.get_value()
            vx = np.cos(theta)
            vy = np.sin(theta)
            ax = 2 * vx + vy
            ay = vx + 2 * vy
            return Dot(np.array([ax, ay, 0]), radius=0.07, color=GRID_TRSF)

        Av_dot = always_redraw(_Av_dot)
        self.add(Av_dot)

        # TracedPath following Av_dot
        ellipse_trace = TracedPath(
            Av_dot.get_center,
            stroke_color=GRID_TRSF,
            stroke_width=2.5,
            dissipating_time=None,   # keep the whole trace
        )
        self.add(ellipse_trace)

        # Rotate v from 0 → 2π (one full revolution)
        # Flash at eigenvector angles: 45° (π/4) → amber, 135° (3π/4) → teal
        # We split the animation into segments to allow flashes
        def rotate_segment(start_angle, end_angle, rt):
            self.play(
                angle_tracker.animate(rate_func=smooth)
                    .set_value(end_angle),
                run_time=rt,
            )

        # Rotate to 45° (π/4): eigenvector (1,1)
        rotate_segment(0, np.pi / 4, 1.0)
        self.play(
            Flash(Av_dot, color=EIG_AMBER, flash_radius=0.4, run_time=0.5),
        )

        # Rotate to 135° (3π/4): eigenvector (1,−1) (pointing other way)
        rotate_segment(np.pi / 4, 3 * np.pi / 4, 1.0)
        self.play(
            Flash(Av_dot, color=EIG_TEAL, flash_radius=0.4, run_time=0.5),
        )

        # Rotate to 225° (5π/4): anti-eigenvector (−1,−1)
        rotate_segment(3 * np.pi / 4, 5 * np.pi / 4, 1.0)
        self.play(
            Flash(Av_dot, color=EIG_AMBER, flash_radius=0.4, run_time=0.5),
        )

        # Rotate to 315° (7π/4): anti-eigenvector (−1,1)
        rotate_segment(5 * np.pi / 4, 7 * np.pi / 4, 1.0)
        self.play(
            Flash(Av_dot, color=EIG_TEAL, flash_radius=0.4, run_time=0.5),
        )

        # Complete full revolution
        rotate_segment(7 * np.pi / 4, 2 * np.pi, 0.5)

        # Draw the semi-axes of the resulting ellipse
        # Long axis: along (1,1)/√2 * 3  →  tip at (3/√2, 3/√2)
        s2 = np.sqrt(2)
        long_axis = Arrow(
            ORIGIN,
            np.array([3 / s2, 3 / s2, 0]),
            buff=0, color=EIG_AMBER, stroke_width=3,
            max_tip_length_to_length_ratio=0.12,
        )
        short_axis = Arrow(
            ORIGIN,
            np.array([1 / s2, -1 / s2, 0]),
            buff=0, color=EIG_TEAL, stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        label_long  = MathTex(r"\lambda=3", font_size=26, color=EIG_AMBER)
        label_long.next_to(long_axis.get_end(), UR, buff=0.1)
        label_short = MathTex(r"\lambda=1", font_size=26, color=EIG_TEAL)
        label_short.next_to(short_axis.get_end(), DR, buff=0.1)

        self.play(
            GrowArrow(long_axis),
            FadeIn(label_long, run_time=0.4),
        )
        self.play(
            GrowArrow(short_axis),
            FadeIn(label_short, run_time=0.4),
        )

        # Zoom back out
        self.play(
            self.camera.frame.animate(rate_func=smooth)
                .restore(),
            run_time=1.0,
        )

        self.wait(2.5)

        # ── Fade out ───────────────────────────────────────────────────────
        self.play(
            *[FadeOut(m) for m in self.mobjects if m is not self.camera.frame],
            run_time=1.0,
        )
