"""
helpers.py – Shared constants, colour palette, and utility functions
for the "Eigenvalues and Eigenvectors of a 2×2 Matrix" Manim project.

COLOUR MEANING (use the same colour for the same idea in every scene):
  BACKGROUND   – scene background
  GRID_ORIG    – original (pre-transform) grid lines
  GRID_TRSF    – transformed (post-transform) grid lines
  AXES_COL     – axis lines and secondary / caption text
  MAIN_TEXT    – main text, generic vectors
  EIG_AMBER    – eigenvector for λ = 3  (stays amber everywhere)
  EIG_TEAL     – eigenvector for λ = 1  (stays teal everywhere)
  HIGHLIGHT    – "turned-off-line" / attention flash (magenta)
"""

import numpy as np
from manim import *

# ── Colour palette ─────────────────────────────────────────────────────────
BACKGROUND  = "#0B1020"
GRID_ORIG   = "#2A3458"
GRID_TRSF   = "#4D96FF"
AXES_COL    = "#8892B0"
MAIN_TEXT   = "#F1F5F9"
EIG_AMBER   = "#FF9F1C"
EIG_TEAL    = "#2EC4B6"
HIGHLIGHT   = "#F72585"

# ── Matrix and eigendata ───────────────────────────────────────────────────
A_MAT = np.array([[2, 1],
                  [1, 2]], dtype=float)

EIGENVALUES  = np.array([3.0, 1.0])
EIGENVECTORS = np.array([[1, 1],
                          [1, -1]], dtype=float)   # columns: v1=(1,1), v2=(1,-1)

# ── Extended scene matrices ────────────────────────────────────────────────
# Scene 4b: B = [[4,1],[2,3]], eigenvalues 5 and 2
B_MAT = np.array([[4, 1],
                  [2, 3]], dtype=float)

# Scene 4c: C = [[0,1],[1,0]] (reflection across y=x), eigenvalues 1 and -1
C_MAT = np.array([[0, 1],
                  [1, 0]], dtype=float)

# Scene 5b: D = [[3,0],[0,1]] (diagonal), eigenvalues 3 and 1
D_MAT = np.array([[3, 0],
                  [0, 1]], dtype=float)


# ── Compile-time assertions ────────────────────────────────────────────────

def _verify_eigendata():
    """Assert analytic eigenvalues/eigenvectors of A match numpy."""
    vals, vecs = np.linalg.eig(A_MAT)
    idx  = np.argsort(vals)[::-1]
    vals = vals[idx]
    vecs = vecs[:, idx]

    assert np.allclose(np.sort(vals)[::-1], np.sort(EIGENVALUES)[::-1]), \
        f"Eigenvalue mismatch: numpy={vals}, expected={EIGENVALUES}"

    for i in range(2):
        v  = EIGENVECTORS[:, i] / np.linalg.norm(EIGENVECTORS[:, i])
        nv = vecs[:, i] / np.linalg.norm(vecs[:, i])
        assert np.allclose(v, nv, atol=1e-6) or np.allclose(v, -nv, atol=1e-6), \
            f"Eigenvector {i} mismatch: numpy={nv}, expected={v}"

    # Quick substitution checks: A @ v == λ * v
    v1 = np.array([1.0, 1.0])
    v2 = np.array([1.0, -1.0])
    assert np.allclose(A_MAT @ v1, 3 * v1), "A(1,1) ≠ 3(1,1)"
    assert np.allclose(A_MAT @ v2, 1 * v2), "A(1,-1) ≠ 1(1,-1)"


def _verify_B():
    """Assert eigenvalues of B = [[4,1],[2,3]] are 5 and 2."""
    vals, vecs = np.linalg.eig(B_MAT)
    expected_vals = np.array([5.0, 2.0])
    assert np.allclose(np.sort(vals)[::-1], np.sort(expected_vals)[::-1]), \
        f"B eigenvalue mismatch: numpy={np.sort(vals)[::-1]}, expected={expected_vals}"

    # Substitution checks
    v1 = np.array([1.0, 1.0])
    v2 = np.array([1.0, -2.0])
    assert np.allclose(B_MAT @ v1, 5 * v1),  "B(1,1) ≠ 5(1,1)"
    assert np.allclose(B_MAT @ v2, 2 * v2),  "B(1,-2) ≠ 2(1,-2)"
    assert np.isclose(np.trace(B_MAT), 7.0), "trace(B) ≠ 7"
    assert np.isclose(np.linalg.det(B_MAT), 10.0), "det(B) ≠ 10"


def _verify_C():
    """Assert eigenvalues of C = [[0,1],[1,0]] are 1 and -1."""
    vals, _ = np.linalg.eig(C_MAT)
    assert np.allclose(np.sort(vals), np.array([-1.0, 1.0])), \
        f"C eigenvalue mismatch: numpy={np.sort(vals)}, expected=[-1,1]"

    # Substitution checks
    v1 = np.array([1.0, 1.0])
    v2 = np.array([1.0, -1.0])
    assert np.allclose(C_MAT @ v1,  1 * v1),  "C(1,1) ≠ 1*(1,1)"
    assert np.allclose(C_MAT @ v2, -1 * v2),  "C(1,-1) ≠ -1*(1,-1)"


def _verify_D():
    """Assert eigenvalues of D = diag(3,1) are 3 and 1."""
    vals, _ = np.linalg.eig(D_MAT)
    expected = np.array([3.0, 1.0])
    assert np.allclose(np.sort(vals)[::-1], expected), \
        f"D eigenvalue mismatch: numpy={np.sort(vals)[::-1]}, expected={expected}"

    v1 = np.array([1.0, 0.0])
    v2 = np.array([0.0, 1.0])
    assert np.allclose(D_MAT @ v1, 3 * v1), "D(1,0) ≠ 3(1,0)"
    assert np.allclose(D_MAT @ v2, 1 * v2), "D(0,1) ≠ 1(0,1)"


# Run all assertions at import time
_verify_eigendata()
_verify_B()
_verify_C()
_verify_D()


# ── Shared layout helpers ──────────────────────────────────────────────────

def make_title_text(title: str, scale: float = 0.65) -> Text:
    """Top-left title label used in every scene."""
    return (
        Text(title, color=MAIN_TEXT, font_size=32)
        .scale(scale)
        .to_corner(UL, buff=0.3)
    )


def make_matrix_mob() -> MathTex:
    """Top-right matrix A display used in every scene."""
    m = MathTex(
        r"A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}",
        color=MAIN_TEXT,
        font_size=36,
    )
    m.to_corner(UR, buff=0.3)
    return m


def make_caption(text: str) -> Text:
    """One-line caption at the bottom of the screen."""
    return (
        Text(text, color=AXES_COL, font_size=24)
        .to_edge(DOWN, buff=0.25)
    )


def dim_mobject(mob: Mobject, opacity: float = 0.4) -> ApplyMethod:
    """Return an animation that dims `mob` to `opacity`."""
    return mob.animate.set_opacity(opacity)


def scene_fade_out(scene: Scene, *mobs, run_time: float = 1.0):
    """Fade all given mobjects (or everything on screen) out over `run_time`."""
    targets = list(mobs) if mobs else scene.mobjects
    if targets:
        scene.play(
            *[FadeOut(m) for m in targets],
            run_time=run_time,
        )


# ── Arrow helper: 2-D numpy vector → Manim Arrow in scene coords ──────────

def vec_arrow(tail: np.ndarray, tip: np.ndarray,
              color: str = MAIN_TEXT, buff: float = 0) -> Arrow:
    """Create a Manim Arrow from 2-D numpy arrays (scene units)."""
    return Arrow(
        start=np.array([tail[0], tail[1], 0]),
        end=np.array([tip[0],  tip[1],  0]),
        color=color,
        buff=buff,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.15,
    )


# ── ValueTracker-based morphing vector (always_redraw pattern) ─────────────

def morphing_vector(tracker: ValueTracker,
                    v_start: np.ndarray,
                    v_end:   np.ndarray,
                    color:   str = MAIN_TEXT) -> VMobject:
    """
    Returns a DecimalNumber-free Arrow that smoothly interpolates from
    v_start to v_end as `tracker` goes from 0 → 1.
    Plug into scene with `always_redraw`.
    """
    def _build():
        t = tracker.get_value()
        tip = v_start * (1 - t) + v_end * t
        return Arrow(
            start=ORIGIN,
            end=np.array([tip[0], tip[1], 0]),
            color=color,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )
    return always_redraw(_build)
