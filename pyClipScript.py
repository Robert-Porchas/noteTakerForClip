# save as clip_append.py
# pip install pyperclip
import time
import pyperclip
from datetime import datetime
pyperclip.set_clipboard("xclip")

OUT = "hawkes_notes.txt"

last = ""
print("Watching clipboard. Copy text, and it will append to hawkes_notes.txt")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        cur = pyperclip.paste()
        if isinstance(cur, str) and cur.strip() and cur != last:
            last = cur
            stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(OUT, "a", encoding="utf-8") as f:
                f.write(f"\n\n--- CLIP {stamp} ---\n")
                f.write(cur.strip())
            print(f"Appended {len(cur.strip())} characters.")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nDone.")
