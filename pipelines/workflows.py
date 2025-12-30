from pathlib import Path

from core.device import (
    push_video,
    open_instagram_share,
    open_youtube_share
)
from platforms.instagram import automate_reels_post
from platforms.youtube import automate_youtube_upload


def instagram(video_path: Path, caption: str) -> None:
    """Execute the complete Instagram Reels upload pipeline.

    Args:
        video_path: Path to the local video file.
        caption: Caption text for the post.
    """
    device_path = Path("/sdcard/Download/") / f"{video_path.stem}.mp4"

    print(f"[+] Pushing video: {video_path} -> {device_path}")
    push_video(str(video_path), str(device_path))

    print("[+] Opening Instagram share intent via MediaStore URI")
    open_instagram_share(str(device_path))

    print("[+] Starting UI Automation sequence")
    print(f"[+] Using caption: '{caption}'")
    automate_reels_post(caption)

    print("[✓] Automation pipeline completed")


def youtube(video_path: Path, caption: str) -> None:
    """Execute the complete YouTube upload pipeline.

    Args:
        video_path: Path to the local video file.
        caption: Caption text (unused for YouTube).
    """
    device_path = Path("/sdcard/Download/") / f"{video_path.stem}.mp4"

    print(f"[+] Pushing video: {video_path} -> {device_path}")
    push_video(str(video_path), str(device_path))

    print("[+] Opening YouTube share intent via MediaStore URI")
    open_youtube_share(str(device_path))

    print("[+] Starting YouTube UI Automation sequence")
    automate_youtube_upload(caption)

    print("[✓] YouTube Automation pipeline completed")