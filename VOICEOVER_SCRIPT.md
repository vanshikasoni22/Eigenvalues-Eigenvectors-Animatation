# 🎙️ Voice-Over Script: Eigenvalues & Eigenvectors of a 2×2 Matrix

**Presenter:** Vanshika Soni (E25B070667)  
**Total Video Length:** 4 minutes 33 seconds  
**Tone:** Confident, engaging, clear academic delivery with natural pauses.

---

## ⏱️ Scene-by-Scene Timed Script

### Scene 0: Title Card
- **Time:** `0:00` – `0:05` (Duration: 5.3s)
- **Visual:** Title "Eigenvalues & Eigenvectors of a 2×2 Matrix" with name and ID.
- **Spoken Lines:**
  > *"Hello everyone! My name is Vanshika Soni, and welcome to this visual exploration of eigenvalues and eigenvectors of a two-by-two matrix."*

---

### Scene 1: The Hook — "Which directions don't turn?"
- **Time:** `0:05` – `0:17` (Duration: 11.7s)
- **Visual:** 8 white arrows on the grid. Matrix $A = \begin{pmatrix}2&1\\1&2\end{pmatrix}$ applies. Most arrows rotate off-line (magenta flash). Two arrows stay on line (amber & teal).
- **Spoken Lines:**
  > *"When a matrix transforms the plane, almost every vector rotates away from its original line. But notice these two special directions in amber and teal — they don't turn at all. They only stretch. Which directions are they, and why do they stay in place?"*

---

### Scene 2: The Core Concept — $A\mathbf{v} = \lambda\mathbf{v}$
- **Time:** `0:17` – `0:30` (Duration: 13.3s)
- **Visual:** Equation $A\mathbf{v} = \lambda\mathbf{v}$ appears. Three definitions reveal one by one with previous lines dimming.
- **Spoken Lines:**
  > *"This introduces the fundamental equation: $A\mathbf{v} = \lambda\mathbf{v}$. Here, $\mathbf{v}$ is a non-zero vector called an eigenvector, and $\lambda$ is a scalar called the eigenvalue. The matrix transforms $\mathbf{v}$ by simply scaling it, without changing its direction."*

---

### Scene 3: Visual Intuition
- **Time:** `0:30` – `1:08` (Duration: 37.9s)
- **Visual:**
  - $(1,0) \to (2,1)$ turns off-axis (magenta).
  - $(1,1) \to (3,3)$ stretches $3\times$ on $y=x$ ($\lambda=3$, amber).
  - $(1,-1) \to (1,-1)$ stays unchanged ($\lambda=1$, teal).
  - Unit circle morphs into an ellipse; flashes at $45^\circ$ and $135^\circ$.
- **Spoken Lines:**
  > *"Let's see this geometrically. The standard basis vector $(1,0)$ rotates off its line to $(2,1)$. But along $y$ equals $x$, the vector $(1,1)$ stretches by a factor of 3 — so its eigenvalue is 3. Along $y$ equals minus $x$, the vector $(1,-1)$ is completely unchanged — an eigenvalue of 1.*  
  > *If we rotate a unit vector around a circle, its image traces an ellipse. The long axis aligns with our amber eigenvector with radius 3, while the short axis aligns with our teal eigenvector with radius 1."*

---

### Scene 3b: Power Iteration — Dominant Eigenvalues
- **Time:** `1:08` – `1:42` (Duration: 33.5s)
- **Visual:** $A^1(2,1)$, $A^2(5,4)$, $A^3(14,13)$ swing closer to $y=x$. Eigendecomposition $(1,0) = \frac{1}{2}(1,1) + \frac{1}{2}(1,-1)$ reveals.
- **Spoken Lines:**
  > *"What happens if we apply $A$ again and again? Starting at $(1,0)$, repeated multiplications produce $(2,1)$, $(5,4)$, and $(14,13)$. Notice the vector swings closer and closer to the line $y$ equals $x$.*  
  > *Why? Because $(1,0)$ is a combination of both eigenvectors. As $n$ grows, $3^n$ grows much faster than $1^n$. The dominant eigenvalue wins!"*

---

### Scene 4: Worked Example — Matrix $A$
- **Time:** `1:42` – `2:19` (Duration: 37.7s)
- **Visual:** $\det(A - \lambda I) = 0 \to \lambda^2 - 4\lambda + 3 = 0 \to \lambda = 3, 1$. Solving eigenspaces with mini plane and checkmarks.
- **Spoken Lines:**
  > *"Now, let's solve for them algebraically. We set $\det(A - \lambda I) = 0$, giving the characteristic polynomial $\lambda^2 - 4\lambda + 3 = 0$. Factoring gives $\lambda_1 = 3$ and $\lambda_2 = 1$.*  
  > *Substituting $\lambda = 3$ into $(A - 3I)\mathbf{v} = 0$ yields $y = x$, giving eigenvector $(1,1)$. Substituting $\lambda = 1$ gives $y = -x$, giving eigenvector $(1,-1)$. Both check out perfectly."*

---

### Scene 4b: Second Example — Non-Symmetric Matrix $B$
- **Time:** `2:19` – `3:08` (Duration: 48.7s)
- **Visual:** $B = \begin{pmatrix}4&1\\2&3\end{pmatrix}$, $\det(B - \lambda I) = \lambda^2 - 7\lambda + 10 = 0 \to \lambda = 5, 2$. Vectors $(1,1)$ and $(1,-2)$ appear on the plane.
- **Spoken Lines:**
  > *"Does this hold for non-symmetric matrices? Consider matrix $B = \begin{pmatrix}4&1\\2&3\end{pmatrix}$.*  
  > *Its characteristic equation is $(4-\lambda)(3-\lambda) - 2 = 0$, simplifying to $\lambda^2 - 7\lambda + 10 = 0$. The roots are $\lambda = 5$ and $\lambda = 2$.*  
  > *For $\lambda = 5$, solving $(B - 5I)\mathbf{v} = 0$ gives eigenvector $(1,1)$ in amber. For $\lambda = 2$, solving $(B - 2I)\mathbf{v} = 0$ yields $2x + y = 0$, so $(1,-2)$ in teal.*  
  > *Notice that the trace, 7, equals $5 + 2$, and the determinant, 10, equals $5 \times 2$."*

---

### Scene 4c: Negative Eigenvalues — Reflection Matrix $C$
- **Time:** `3:08` – `3:39` (Duration: 31.2s)
- **Visual:** Matrix $C = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ swaps $x$ and $y$. Vector $(1,-1)$ flips $180^\circ$ through the origin to $(-1,1)$.
- **Spoken Lines:**
  > *"What about negative eigenvalues? Look at matrix $C$, which swaps $x$ and $y$ — a reflection across the line $y$ equals $x$.*  
  > *Its eigenvalues are 1 and minus 1. The vector $(1,1)$ lies directly on the mirror line, so it stays fixed with $\lambda = 1$. But the perpendicular vector $(1,-1)$ flips $180^\circ$ through the origin to $(-1,1)$ — a negative eigenvalue means the vector stays on the same line, but flips to the opposite direction!"*

---

### Scene 5: Geometric Interpretation — Determinant & Trace
- **Time:** `3:39` – `3:56` (Duration: 17.0s)
- **Visual:** Unit square transforms into parallelogram of area 3. Formulas $\det(A) = 3 \times 1 = 3$ and $\text{tr}(A) = 3 + 1 = 4$ appear.
- **Spoken Lines:**
  > *"Geometrically, the determinant measures area scaling: the unit square transforms into a parallelogram of area 3, which equals the product of the eigenvalues, $3 \times 1$. Meanwhile, the trace equals their sum, $3 + 1 = 4$."*

---

### Scene 5b: Active Learning — Predict the Answer
- **Time:** `3:56` – `4:19` (Duration: 22.9s)
- **Visual:** Matrix $D = \begin{pmatrix}3&0\\0&1\end{pmatrix}$. "Pause. What are the eigenvalues of D?" Countdown: 5, 4, 3, 2, 1. Grid stretches along $x$-axis.
- **Spoken Lines:**
  > *"Pause and test yourself. What are the eigenvalues of diagonal matrix $D$? Five... four... three... two... one...*  
  > *For any diagonal matrix, the eigenvalues are simply the diagonal entries: 3 and 1! The eigenvectors are the standard axes: the $x$-axis stretches threefold, while the $y$-axis remains unchanged."*

---

### Scene 6: Summary & Credits
- **Time:** `4:19` – `4:33` (Duration: 13.8s)
- **Visual:** 3 Takeaways reveal: 1. Invariant directions, 2. Scaling factor, 3. Global properties. Credits & Thank You frame.
- **Spoken Lines:**
  > *"To summarize: eigenvectors are the invariant directions that never rotate under a transformation; eigenvalues tell us how much they stretch or flip; and together, they completely describe the geometry of linear transformations. Thank you for watching!"*

---

## 💡 Practical Recording Tips

1. **Pacing:** Speak at an average of ~130–140 words per minute. Don't rush; let the animations breathe during transitions.
2. **Breathing Pauses:** Where you see pauses or equation reveals, take a breath and let the visual lead for half a second before speaking.
3. **Pronunciation:**
   - $\lambda$: *"lambda"*
   - $\det$: *"determinant"*
   - $\text{tr}$: *"trace"*
   - $\mathbf{v}$: *"vector v"*
   - $\gg$: *"much greater than"*
