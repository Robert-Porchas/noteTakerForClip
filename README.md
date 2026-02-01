# pyClip

Small clipboard watcher that appends copied text to a notes file with timestamps.

## What it does
- Polls the clipboard every 0.5s.
- When the clipboard changes and contains non-empty text, it appends the text to `hawkes_notes.txt`.
- Adds a header like `--- CLIP 2026-02-01 15:20:00 ---` for each capture.

## Requirements
- Python 3.8+
- `pyperclip` (`pip install pyperclip`)
- A working clipboard backend for your OS. The script currently sets:
  - `pyperclip.set_clipboard("xclip")`
  - If you are not on Linux/X11, you may need to change or remove that line.

## Usage
```powershell
python .\pyClipScript.py
```

You will see:
```
Watching clipboard. Copy text, and it will append to hawkes_notes.txt
Press Ctrl+C to stop.
```

Stop with Ctrl+C.

## Output
- File: `hawkes_notes.txt`
- The file is ignored by git (see `.gitignore`).

## Notes
- The script filters out repeated clipboard values and whitespace-only content.
- The `hawkes_notes.txt` path is configurable via the `OUT` constant.
