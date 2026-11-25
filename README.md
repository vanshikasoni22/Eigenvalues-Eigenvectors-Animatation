# 🎬 Eigenvalues and Eigenvectors of a 2×2 Matrix
### A Mathematical Animation Project built with [Manim Community Edition](https://www.manim.community/)

> **Author:** Vanshika Soni  
> **Student ID:** E25B070667  
> **Topic:** Linear Algebra – Eigenvalues and Eigenvectors of $2 \times 2$ Matrices  
> **Target Video Length:** ~5 minutes (16:9, 1080p60)  

---

## 📌 Project Overview

This project is a silent, pedagogical animation illustrating the geometric intuition and algebraic derivation of **eigenvalues** and **eigenvectors** for undergraduate linear algebra students.

The primary matrix investigated is:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$
with analytic eigenvalues $\lambda_1 = 3$, $\lambda_2 = 1$ and corresponding eigenvectors $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

The project also explores:
- **Power Iteration / Dominant Eigenvalues** ($A^n \mathbf{v}$)
- **Non-symmetric Matrix:** $B = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ ($\lambda = 5, 2$)
- **Reflection & Negative Eigenvalues:** $C = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ ($\lambda = 1, -1$)
- **Diagonal Matrix & Active Learning:** $D = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$ ($\lambda = 3, 1$)

---

## 🎨 Consistent Colour Palette

To maintain clear visual hierarchy, each colour represents a distinct mathematical concept across all scenes:

| Role | Colour | Hex | Description |
|---|---|---|---|
| **Background** | Deep Navy | `#0B1020` | Dark minimalist canvas |
| **Original Grid** | Slate Blue | `#2A3458` | Pre-transformation coordinate grid |
| **Transformed Grid** | Royal Azure | `#4D96FF` | Post-transformation grid & traces |
| **Axes & Secondary Text** | Muted Slate | `#8892B0` | Axis lines, guides, subtitles, captions |
| **Main Text & Generic Vectors** | Crisp White | `#F1F5F9` | Default vectors, standard formulas |
| **Eigenvector ($\lambda = 3$ / $\lambda = 5$)** | Amber Gold | `#FF9F1C` | Dominant / primary eigenvector direction |
| **Eigenvector ($\lambda = 1$ / $\lambda = 2$)** | Bright Teal | `#2EC4B6` | Secondary eigenvector direction |
| **Turned-off Alert / Highlights** | Neon Magenta | `#F72585` | Vectors rotating off-line, highlights |

---

## 📽️ Scene Breakdown (11 Scenes)

| Scene | File | Class | Target Duration | Description |
|:---:|---|---|:---:|---|
| **0** | `scene_0.py` | `TitleCard` | ~5 s | Title card with student name, ID, and animated branding. |
| **1** | `scene_1.py` | `Hook` | ~35 s | 8 arrows on grid; 6 rotate off (flash magenta), 2 stay on line (amber & teal). *"Which directions don't turn?"* |
| **2** | `scene_2.py` | `ConceptEquation` | ~40 s | Core definition $A\mathbf{v} = \lambda\mathbf{v}$ written and explained line-by-line with dynamic dimming. |
| **3** | `scene_3.py` | `VisualIntuition` | ~75 s | Morphing vectors: $(1,0) \to (2,1)$, $(1,1) \to (3,3)$, $(1,-1) \to (1,-1)$; unit circle morphing into an ellipse via `TracedPath`. |
| **3b** | `scene_3b.py` | `PowerIteration` | ~50 s | Repeated application $A^n(1,0) \to$ line $y=x$; demonstrates why dominant eigenvalue $3^n \gg 1^n$ wins. |
| **4** | `scene_4.py` | `WorkedExample` | ~90 s | Step-by-step derivation: $\det(A - \lambda I) = 0 \to \lambda = 3, 1$; solving eigenspaces with mini-plane plot and tick verification. |
| **4b** | `scene_4b.py` | `SecondExample` | ~60 s | Non-symmetric matrix $B = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} \to \lambda = 5, 2$; eigenvectors $\begin{pmatrix}1\\1\end{pmatrix}$ and $\begin{pmatrix}1\\-2\end{pmatrix}$, $\det$ and trace relations. |
| **4c** | `scene_4c.py` | `NegativeEigenvalue` | ~40 s | Reflection matrix $C$; eigenvector $(1,-1)$ smoothly rotates $180^\circ$ through the origin ($\lambda = -1$). |
| **5** | `scene_5.py` | `Interpretation` | ~40 s | Unit square transforms to parallelogram ($\text{Area} = \|\det(A)\| = 3$); trace and stretch relations. |
| **5b** | `scene_5b.py` | `PredictPause` | ~30 s | Active learning: 5-second countdown to guess eigenvalues of diagonal matrix $D = \text{diag}(3,1)$. |
| **6** | `scene_6.py` | `SummaryCredits` | ~35 s | 3 key conceptual takeaways, references, AI tool attributions, and closing frame. |

---

## ⚙️ Installation & Setup

### Prerequisites

- **macOS / Linux / Windows**
- **Python 3.12** *(Recommended; Python 3.14 is currently incompatible with Manim dependencies)*
- **Homebrew** (on macOS)

```bash
# 1. Install system dependencies (macOS)
brew install python@3.12 cairo pkg-config ffmpeg
brew install --cask basictex

# 2. Update LaTeX package manager and install required math packages
sudo tlmgr update --self
sudo tlmgr install dvisvgm collection-latexextra
```

### Virtual Environment Setup

```bash
# Clone the repository
git clone https://github.com/vanshikasoni22/Eigenvalues-Eigenvectors-Animatation.git
cd Eigenvalues-Eigenvectors-Animatation

# Create virtual environment with Python 3.12
/opt/homebrew/bin/python3.12 -m venv venv
source venv/bin/activate

# Install Manim and dependencies
pip install manim numpy
```

---

## 🚀 How to Run & Render

Always ensure your virtual environment is active:
```bash
source venv/bin/activate
```

### 1. Render All Scenes & Automatically Concatenate

```bash
# Fast Preview (480p, 15fps):
python3 render_all.py ql
# or: ./render.sh ql

# Final HD Quality (1080p, 60fps):
python3 render_all.py qh
# or: ./render.sh qh
```
This generates **`Video.mp4`** in the root directory.

### 2. Render and Preview Individual Scenes

Use the `-p` flag to preview immediately upon completion:
```bash
manim -ql -p scene_0.py TitleCard
manim -ql -p scene_1.py Hook
manim -ql -p scene_2.py ConceptEquation
manim -ql -p scene_3.py VisualIntuition
manim -ql -p scene_3b.py PowerIteration
manim -ql -p scene_4.py WorkedExample
manim -ql -p scene_4b.py SecondExample
manim -ql -p scene_4c.py NegativeEigenvalue
manim -ql -p scene_5.py Interpretation
manim -ql -p scene_5b.py PredictPause
manim -ql -p scene_6.py SummaryCredits
```

### 3. Check Exact Scene Durations

Run the duration checker script to inspect the exact runtime of each rendered clip:
```bash
./check_durations.sh ql   # or qh
```

---

## 🎙️ Adding Voice-over

Manim generates silent video files. To attach your voice-over:

### Method A: In iMovie or CapCut (Recommended)
1. Open iMovie and create a new project.
2. Drag `Video.mp4` onto the timeline.
3. Click the **Microphone icon** to record audio live as the video plays, or drag in your pre-recorded `.mp3` / `.m4a` file.
4. Export as MP4.

### Method B: Single-command via FFmpeg
```bash
ffmpeg -i Video.mp4 -i voiceover.mp3 -c:v copy -c:a aac -shortest Video_with_Voiceover.mp4
```

---

## 🛠️ Design Principles & Motion Rules

- **Smooth Easing:** All animations use `rate_func=smooth` or `rate_func=there_and_back` for natural pulses; linear motion is strictly avoided.
- **Dynamic Opacity / Dimming:** When presenting multi-line derivations, previous lines dim to 40% opacity (`set_opacity(0.4)`) to direct student attention to the active line.
- **Parametric Interpolation:** Vectors morph continuously from $\mathbf{v}$ to $A\mathbf{v}$ using `ValueTracker` and `always_redraw`, allowing viewers to see direction and magnitude change simultaneously.
- **Compile-Time Assertions:** `helpers.py` verifies all matrix eigenvalues and eigenvectors with NumPy at import time to prevent mathematical discrepancies.

---

## 📚 References & Acknowledgments

- **Gilbert Strang**, *Introduction to Linear Algebra* (5th Edition).
- **Grant Sanderson (3Blue1Brown)**, *Essence of Linear Algebra* series.
- **Manim Community**, [manim.community documentation](https://docs.manim.community/).
- **AI Tooling:** Antigravity / Gemini for code orchestration & debugging; Claude for educational script drafting.
