#!/usr/bin/env python3
"""
render_all.py – Render every scene and concatenate into Video.mp4

Updated scene order (11 scenes total):
  0  TitleCard         ~5 s
  1  Hook              ~35 s
  2  ConceptEquation   ~40 s
  3  VisualIntuition   ~75 s
  3b PowerIteration    ~50 s   ← NEW
  4  WorkedExample     ~90 s
  4b SecondExample     ~60 s   ← NEW
  4c NegativeEigenvalue ~40 s  ← NEW
  5  Interpretation    ~40 s
  5b PredictPause      ~30 s   ← NEW
  6  SummaryCredits    ~35 s

Usage:
  python3 render_all.py ql    # 480p15 preview (fast)
  python3 render_all.py qh    # 1080p60 final  (slow)
"""

import sys
import subprocess
import os

QUALITY = sys.argv[1] if len(sys.argv) > 1 else "ql"

SCENES = [
    ("scene_0.py",  "TitleCard"),
    ("scene_1.py",  "Hook"),
    ("scene_2.py",  "ConceptEquation"),
    ("scene_3.py",  "VisualIntuition"),
    ("scene_3b.py", "PowerIteration"),
    ("scene_4.py",  "WorkedExample"),
    ("scene_4b.py", "SecondExample"),
    ("scene_4c.py", "NegativeEigenvalue"),
    ("scene_5.py",  "Interpretation"),
    ("scene_5b.py", "PredictPause"),
    ("scene_6.py",  "SummaryCredits"),
]

print(f"Rendering with -{QUALITY} quality…\n")

for scene_file, scene_class in SCENES:
    print(f"--- {scene_class} ({scene_file}) ---")
    subprocess.run(
        ["manim", f"-{QUALITY}", scene_file, scene_class],
        check=True,
    )

print("\nAll scenes rendered. Building concat list for ffmpeg…")

vid_subdir = "1080p60" if QUALITY == "qh" else "480p15"
list_lines = []

for scene_file, scene_class in SCENES:
    base     = os.path.splitext(scene_file)[0]
    vid_path = os.path.join("media", "videos", base, vid_subdir,
                            f"{scene_class}.mp4")
    if os.path.isfile(vid_path):
        list_lines.append(f"file '{vid_path}'\n")
    else:
        print(f"  WARNING: {vid_path} not found – skipping")

with open("concat_list.txt", "w") as f:
    f.writelines(list_lines)

subprocess.run(
    ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
     "-i", "concat_list.txt", "-c", "copy", "Video.mp4"],
    check=True,
)

print("\nDone!  Output: Video.mp4")
