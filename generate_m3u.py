#!/usr/bin/env python3
import json
from pathlib import Path

JSON_FILE = Path("channels.json")
M3U_FILE = Path("playlist.m3u")

def main():
    with JSON_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)

    lines = ["#EXTM3U"]

    for category, channels in data.items():
        if not isinstance(channels, list):
            continue

        for ch in channels:
            if not isinstance(ch, dict):
                continue

            name = str(ch.get("name", "")).strip()
            url = str(ch.get("url", "")).strip()
            logo = str(ch.get("logo", "")).strip()

            if not name or not url:
                continue

            lines.append(
                f'#EXTINF:-1 tvg-name="{name}" '
                f'tvg-logo="{logo}" group-title="{category}",{name}'
            )
            lines.append(url)

    M3U_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Created {M3U_FILE} with {sum(1 for x in lines if x.startswith('#EXTINF:'))} channels.")

if __name__ == "__main__":
    main()
