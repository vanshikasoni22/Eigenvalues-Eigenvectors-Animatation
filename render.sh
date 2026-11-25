#!/usr/bin/env bash
# render.sh – Render all 11 scenes and concatenate into Video.mp4
#
# Usage:
#   chmod +x render.sh
#   ./render.sh ql    # low quality (480p15) – quick preview
#   ./render.sh qh    # high quality (1080p60) – final render
#
# After rendering, Video.mp4 is created in the current directory.

set -e

QUALITY="${1:-ql}"   # default to low quality

echo "==> Rendering with quality flag: -${QUALITY}"
echo ""

SCENES=(
  "scene_0.py TitleCard"
  "scene_1.py Hook"
  "scene_2.py ConceptEquation"
  "scene_3.py VisualIntuition"
  "scene_3b.py PowerIteration"
  "scene_4.py WorkedExample"
  "scene_4b.py SecondExample"
  "scene_4c.py NegativeEigenvalue"
  "scene_5.py Interpretation"
  "scene_5b.py PredictPause"
  "scene_6.py SummaryCredits"
)

for entry in "${SCENES[@]}"; do
  FILE=$(echo "$entry" | awk '{print $1}')
  CLASS=$(echo "$entry" | awk '{print $2}')
  echo "--- Rendering $CLASS from $FILE ---"
  manim -"${QUALITY}" "$FILE" "$CLASS"
done

echo ""
echo "==> All scenes rendered. Concatenating with ffmpeg..."

# Build the ffmpeg file list
LISTFILE="concat_list.txt"
> "$LISTFILE"

for entry in "${SCENES[@]}"; do
  FILE=$(echo "$entry" | awk '{print $1}')
  CLASS=$(echo "$entry" | awk '{print $2}')

  # Manim output directory varies by quality
  if [ "$QUALITY" = "qh" ]; then
    VIDDIR="media/videos/${FILE%.py}/1080p60"
  else
    VIDDIR="media/videos/${FILE%.py}/480p15"
  fi

  VIDFILE="${VIDDIR}/${CLASS}.mp4"
  if [ -f "$VIDFILE" ]; then
    echo "file '$VIDFILE'" >> "$LISTFILE"
  else
    echo "WARNING: Expected output not found: $VIDFILE"
  fi
done

ffmpeg -y -f concat -safe 0 -i "$LISTFILE" -c copy Video.mp4

echo ""
echo "==> Done! Output: Video.mp4"
