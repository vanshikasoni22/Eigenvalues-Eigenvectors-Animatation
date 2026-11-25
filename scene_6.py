"""
scene_6.py – Summary + Credits (target: ~35 seconds)

Three takeaways revealed one by one with LaggedStart, then:
  • A credits frame with references, music placeholder, and AI tools credit.
  • A closing frame.
"""

from manim import *
from helpers import (
    BACKGROUND, MAIN_TEXT, AXES_COL, EIG_AMBER, EIG_TEAL, HIGHLIGHT,
    make_title_text, make_caption,
)


TAKEAWAYS = [
    (EIG_AMBER,
     r"Eigenvectors are the ONLY directions A leaves unchanged",
     "The direction of v does not rotate under A"),
    (EIG_TEAL,
     r"Eigenvalues tell you HOW MUCH A scales those directions",
     r"$\lambda=3$ stretches; $\lambda=1$ preserves length"),
    (MAIN_TEXT,
     r"det(A) = $\lambda_1 \lambda_2$ and tr(A) = $\lambda_1 + \lambda_2$",
     "Global properties encoded in the eigenvalue pair"),
]


class SummaryCredits(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        # ── Title ──────────────────────────────────────────────────────────
        title = make_title_text("Scene 6 – Summary")
        self.add(title)

        heading = Text(
            "Key Takeaways",
            font_size=48,
            color=MAIN_TEXT,
            weight=BOLD,
        ).move_to(UP * 2.8)
        self.play(FadeIn(heading, shift=UP * 0.2, run_time=0.5))

        # ── Three takeaway blocks with LaggedStart ─────────────────────────
        takeaway_mobs = []
        for i, (color, main_text, sub_text) in enumerate(TAKEAWAYS):
            # Number bullet
            num = Text(f"{i+1}.", font_size=36, color=color, weight=BOLD)

            # Main line
            main = Text(main_text, font_size=30, color=color)

            # Sub-line
            sub = Text(sub_text, font_size=22, color=AXES_COL)

            block = VGroup(num, main, sub).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            # Actually place the number to the left of the text block
            text_part = VGroup(main, sub).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            row = VGroup(num, text_part).arrange(RIGHT, buff=0.25, aligned_edge=UP)

            if i == 0:
                row.next_to(heading, DOWN, buff=0.5).align_to(heading, LEFT).shift(RIGHT * 0.5)
            else:
                row.next_to(takeaway_mobs[-1], DOWN, buff=0.4).align_to(takeaway_mobs[-1], LEFT)

            takeaway_mobs.append(row)

        # Reveal with LaggedStart: each takeaway dims the previous ones
        for i, mob in enumerate(takeaway_mobs):
            dim_anims = [m.animate.set_opacity(0.4) for m in takeaway_mobs[:i]]
            if dim_anims:
                self.play(*dim_anims, run_time=0.3)
            self.play(
                FadeIn(mob, shift=UP * 0.25, run_time=0.6, rate_func=smooth)
            )
            self.wait(0.5)

        # Restore opacity on all three briefly
        self.play(*[m.animate.set_opacity(1.0) for m in takeaway_mobs], run_time=0.4)
        self.wait(1.0)

        # ── Fade to credits ────────────────────────────────────────────────
        self.play(
            FadeOut(VGroup(heading, *takeaway_mobs, title)),
            run_time=0.8,
        )

        # ── Credits frame ─────────────────────────────────────────────────
        cred_title = Text("References & Credits", font_size=38,
                          color=MAIN_TEXT, weight=BOLD).move_to(UP * 2.5)

        refs = [
            "Gilbert Strang, Introduction to Linear Algebra, 5th ed.",
            "3Blue1Brown, Essence of Linear Algebra (YouTube, 2016).",
            "Manim Community Edition – manim.community",
        ]
        ref_mobs = VGroup(*[
            Text(r, font_size=22, color=AXES_COL) for r in refs
        ]).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        ref_mobs.next_to(cred_title, DOWN, buff=0.5).align_to(cred_title, LEFT)

        music_line = Text(
            "Music: [Placeholder – add royalty-free music credit here]",
            font_size=22, color=AXES_COL,
        ).next_to(ref_mobs, DOWN, buff=0.4).align_to(ref_mobs, LEFT)

        ai_line = Text(
            "AI tools: Antigravity / Gemini for code  ·  Claude for script drafting",
            font_size=22, color=AXES_COL,
        ).next_to(music_line, DOWN, buff=0.2).align_to(music_line, LEFT)

        self.play(
            FadeIn(cred_title, shift=UP * 0.2, run_time=0.5),
            LaggedStart(
                *[FadeIn(r, shift=UP * 0.15, run_time=0.4) for r in ref_mobs],
                lag_ratio=0.3,
            ),
        )
        self.play(
            FadeIn(music_line, shift=UP * 0.15, run_time=0.4),
            FadeIn(ai_line,    shift=UP * 0.15, run_time=0.4),
        )
        self.wait(1.5)

        # ── Closing frame ──────────────────────────────────────────────────
        self.play(
            FadeOut(VGroup(cred_title, ref_mobs, music_line, ai_line)),
            run_time=0.6,
        )

        close_text = Text(
            "Thank you",
            font_size=64,
            color=MAIN_TEXT,
            weight=BOLD,
        ).move_to(ORIGIN)

        # Colour "Thank" amber and "you" teal
        close_text_amber = Text("Thank", font_size=64, color=EIG_AMBER, weight=BOLD)
        close_text_teal  = Text(" you",  font_size=64, color=EIG_TEAL,  weight=BOLD)
        close_group = VGroup(close_text_amber, close_text_teal).arrange(RIGHT, buff=0.0)
        close_group.move_to(ORIGIN)

        self.play(FadeIn(close_group, shift=UP * 0.3, run_time=0.6))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
