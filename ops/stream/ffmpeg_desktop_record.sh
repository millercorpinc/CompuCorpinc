#!/usr/bin/env bash
# Record the desktop (Linux/X11) to a timestamped MP4 file.
# Usage:
#   bash ops/stream/ffmpeg_desktop_record.sh
#
# Environment variables:
#   OUT_DIR  - output directory (default: ./work/captures)
#   FPS      - frames per second (default: 30)
#   DISPLAY  - X display to capture (default: :0.0)
#
# Press q in this terminal to stop recording.

set -euo pipefail

OUT_DIR="${OUT_DIR:-./work/captures}"
FPS="${FPS:-30}"
DISPLAY_ID="${DISPLAY:-:0.0}"

mkdir -p "$OUT_DIR"

OUTFILE="$OUT_DIR/dos_session_$(date +%Y%m%d_%H%M%S).mp4"

echo "Recording $DISPLAY_ID → $OUTFILE  (press q to stop)"

ffmpeg -y \
  -f x11grab -framerate "$FPS" -i "$DISPLAY_ID" \
  -c:v libx264 -preset veryfast -pix_fmt yuv420p \
  "$OUTFILE"
