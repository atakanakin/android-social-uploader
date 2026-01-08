from pathlib import Path

from core.device import open_instagram_share, open_youtube_share
from platforms.instagram import automate_reels_post
from platforms.youtube import automate_youtube_upload


def instagram(caption: str, device_path: Path) -> None:
    """Execute the complete Instagram Reels upload pipeline.

    Args:
        caption: Caption text for the post.
        device_path: Path to the video file on the device.
    """
    print("[+] Opening Instagram share intent via MediaStore URI")
    open_instagram_share(str(device_path))

    print("[+] Starting UI Automation sequence")
    print(f"[+] Using caption: '{caption}'")
    automate_reels_post(caption)

    print("[✓] Automation pipeline completed")


def youtube(caption: str, device_path: Path) -> None:
    """Execute the complete YouTube upload pipeline.

    Args:
        caption: Caption text (unused for YouTube).
        device_path: Path to the video file on the device.
    """
    print("[+] Opening YouTube share intent via MediaStore URI")
    open_youtube_share(str(device_path))

    print("[+] Starting YouTube UI Automation sequence")
    automate_youtube_upload(caption)

    print("[✓] YouTube Automation pipeline completed")
