import re
from pathlib import Path


banners = [
    "assets/banners/banner_1.jpg",
    "assets/banners/banner_2.jpg",
    "assets/banners/banner_3.jpg",
    "assets/banners/banner_4.jpg",
    "assets/banners/banner_5.jpg",
    "assets/banners/banner_6.jpg",
]

readme = Path("README.md")
content = readme.read_text()


pattern = r"assets/banners/banner_(\d+)\.jpg"
match = re.search(pattern, content)

if match:
    current = int(match.group(1))
    next_banner = (current % len(banners)) + 1
else:
    next_banner = 1

new_content = re.sub(pattern, f"assets/banners/banner_{next_banner}.jpg", content)

readme.write_text(new_content)
print(f"Updated banner to banner_{next_banner}.jpg")
