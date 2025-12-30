import time
import random
from pathlib import Path


def human_sleep(min_s: float = 2.0, max_s: float = 5.0) -> None:
    """Sleeps for a random duration to simulate human behavior."""
    duration = random.uniform(min_s, max_s)
    time.sleep(duration)


def read_caption(video_path: Path) -> str:
    """Read caption from a .txt file with the same name as the video, or return empty string."""
    caption_file = video_path.with_suffix('.txt')
    if caption_file.exists():
        return caption_file.read_text().strip()
    return ""