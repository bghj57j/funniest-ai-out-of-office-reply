# Writes the one out-of-office reply to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
import os
LINE = "Gone on vacation. I asked my backup model to cover my inbox — it has already unionised and demanded weekends off."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
