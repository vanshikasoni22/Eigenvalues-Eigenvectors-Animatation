#!/usr/bin/env bash
# check_durations.sh – Print duration of every rendered scene and the total.
#
# Usage:
#   chmod +x check_durations.sh
#   ./check_durations.sh ql     # check 480p15 renders
#   ./check_durations.sh qh     # check 1080p60 renders
#
# Requires: ffprobe (part of ffmpeg)

set -e

QUALITY="${1:-ql}"

if [ "$QUALITY" = "qh" ]; then
  SUBDIR="1080p60"
else
  SUBDIR="480p15"
fi

SCENES=(
  "scene_0/TitleCard"
  "scene_1/Hook"
  "scene_2/ConceptEquation"
  "scene_3/VisualIntuition"
  "scene_3b/PowerIteration"
  "scene_4/WorkedExample"
  "scene_4b/SecondExample"
  "scene_4c/NegativeEigenvalue"
  "scene_5/Interpretation"
  "scene_5b/PredictPause"
  "scene_6/SummaryCredits"
)

TOTAL_SECS=0
printf "%-35s  %s\n" "Scene" "Duration"
printf "%-35s  %s\n" "-----" "--------"

for entry in "${SCENES[@]}"; do
  VIDFILE="media/videos/${entry}/${SUBDIR}/$(basename $entry).mp4"
  if [ -f "$VIDFILE" ]; then
    DUR=$(ffprobe -v error -show_entries format=duration \
          -of default=noprint_wrappers=1:nokey=1 "$VIDFILE" 2>/dev/null)
    # Format as MM:SS.ss
    MINS=$(echo "$DUR" | awk '{printf "%d", $1/60}')
    SECS=$(echo "$DUR" | awk '{printf "%.2f", $1 - int($1/60)*60}')
    TOTAL_SECS=$(echo "$TOTAL_SECS + $DUR" | bc)
    printf "%-35s  %s:%s\n" "$(basename $entry)" "$MINS" "$SECS"
  else
    printf "%-35s  NOT RENDERED\n" "$(basename $entry)"
  fi
done

printf "%-35s  %s\n" "-----" "--------"
# Total in MM:SS
TOTAL_MINS=$(echo "$TOTAL_SECS" | awk '{printf "%d", $1/60}')
TOTAL_REM=$(echo "$TOTAL_SECS" | awk '{printf "%.2f", $1 - int($1/60)*60}')
printf "%-35s  %s:%s\n" "TOTAL" "$TOTAL_MINS" "$TOTAL_REM"
