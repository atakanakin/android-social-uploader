import argparse
from pathlib import Path

from core.device import delete_video, push_video
from pipelines.workflows import instagram, youtube
from utils.helpers import read_caption


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Android Social Media Upload Automation"
    )
    parser.add_argument(
        "--video", required=True, type=Path, help="Path to the local video file"
    )
    parser.add_argument(
        "--platform",
        choices=["instagram", "youtube", "all"],
        default="all",
        help="Platform to upload to (default: all)",
    )

    args = parser.parse_args()

    caption = read_caption(args.video)
    device_path = Path("/sdcard/Download/") / f"{args.video.stem}.mp4"

    print(f"[+] Pushing video: {args.video} -> {device_path}")
    push_video(str(args.video), str(device_path))

    if args.platform == "instagram":
        instagram(caption, device_path)
    elif args.platform == "youtube":
        youtube(caption, device_path)
    elif args.platform == "all":
        instagram(caption, device_path)
        youtube(caption, device_path)

    print(f"[+] Deleting video from device: {device_path}")
    delete_video(str(device_path))
    print("[✓] Upload automation completed.")
