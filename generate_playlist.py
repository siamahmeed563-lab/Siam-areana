import json

with open("channels.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lines = ["#EXTM3U"]

for group, channels in data.items():
    if isinstance(channels, list):
        for ch in channels:
            name = ch.get("name", "")
            url = ch.get("url", "")
            logo = ch.get("logo", "")

            if url:
                lines.append(
                    f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}'
                )
                lines.append(url)

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("playlist.m3u generated successfully!")
