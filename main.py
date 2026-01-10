import argparse
from pathlib import Path

from core.device import delete_video, push_video, ensure_device_connected
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
        "--move-path",
        type=Path,
        help="Optional new path to move the video after upload",
    )
    parser.add_argument(
        "--platform",
        choices=["instagram", "youtube", "all"],
        default="all",
        help="Platform to upload to (default: all)",
    )
    parser.add_argument(
        "--device-ip",
        type=str,
        help="IP address of the Android device (if using ADB over network)",
    )

    args = parser.parse_args()

    caption = read_caption(args.video)
    device_path = Path("/sdcard/Download/") / f"{args.video.stem}.mp4"

    print(f"[+] Pushing video: {args.video} -> {device_path}")
    if args.device_ip:
        ensure_device_connected(args.device_ip)
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

    if args.move_path:
        args.move_path.mkdir(parents=True, exist_ok=True)
        new_path = args.move_path / args.video.name
        caption_file = args.video.with_suffix(".txt")
        args.video.replace(new_path)
        caption_file.replace(args.move_path / caption_file.name)
        print(f"[+] Moved video and caption to: {args.move_path}")

    print("[✓] Upload automation completed.")
