# OBS Notes – Capturing the DOSBox-X Window

## Scene setup

1. Open OBS and create a new **Scene** called `DOS Workstation`.
2. Add a **Window Capture** source:
   - **Window**: select the DOSBox-X window (`DOSBox-X – AI DOS Workstation`).
   - If Window Capture is not available (Linux/Wayland), use **Screen Capture**
     and crop to the DOSBox-X window area.
3. In **Output** → **Video**, set the base (canvas) resolution to:
   - `1280×720` for a compact recording, or
   - `1920×1080` for full HD.
4. Optional: add a **Crop/Pad** filter to remove the DOSBox-X title bar and
   show only the DOS text area.

## Streaming

- Add a **Stream** output pointing to your RTMP endpoint (Twitch, YouTube, etc.)
  or a local SRT destination.
- Enable **Replay Buffer** if you want to capture highlights on demand.

## Local recording

- Go to **Output** → **Recording** → set path to `work/captures/`.
- Format: `mp4` with `libx264` codec, CRF 20–23 for good quality/size balance.

## Tips

- Use the **Colour Correction** filter to boost contrast on the DOS text for
  better legibility on stream.
- Add a **Text (GDI+)** source with the current task/message subject as an
  overlay so viewers know what the AI is working on.
- Keep audio muted unless you add a TTS narration layer.
