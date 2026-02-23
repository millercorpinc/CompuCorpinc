# Troubleshooting

## DOSBox-X

### DOSBox-X does not find the config file

```bash
dosbox-x -conf ops/dosbox/dosbox-x.conf
```

Run the command from the repository root, or use an absolute path.

### `C:\WORK` mount fails

The autoexec in `dosbox-x.conf` uses a path relative to the config file
location (`ops/dosbox/`):

```dos
mount c ..\..\work\C_WORK
```

If you launch DOSBox-X from a different directory, adjust the mount path or
use an absolute path.

### `MAIL LIST` shows nothing

1. Confirm there are `.MSG` files in `work/C_WORK/MAIL/INBOX/` on the host.
2. Confirm the mount succeeded: type `dir C:\WORK\MAIL\INBOX\` in DOS.
3. Check that filenames end in `.MSG` (uppercase or lowercase – `dir /b` shows
   them as uppercase on FreeDOS).

### `MAIL ARCHIVE` fails with "File not found"

The filename passed to `MAIL ARCHIVE` must match exactly (including
extension). Use `MAIL LIST` to get the exact name.

## ffmpeg recording

### No output / black screen

- Confirm your display is on `:0.0` (Linux/X11). Adjust `-i :0.0` if needed.
- On Wayland, use `-f pipewire` or a screen-capture portal instead of
  `x11grab`.
- On macOS, use `-f avfoundation -i "1"` (replace `1` with your screen index).

### Output file not created

Check that `work/captures/` exists or that `$OUT_DIR` is set to a writable
directory.

## CI failures

### ShellCheck errors

Run locally:

```bash
shellcheck ops/stream/ffmpeg_desktop_record.sh
```

Fix any reported issues before pushing.

### markdownlint errors

Run locally:

```bash
npx markdownlint-cli "**/*.md" --ignore node_modules
```

Common fixes:

- Add a blank line before and after fenced code blocks.
- Use ATX-style headings (`#`, `##`, …) consistently.
- Ensure files end with a newline.
