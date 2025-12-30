import argparse
from pathlib import Path

from pipelines.workflows import instagram, youtube
from utils.helpers import read_caption


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Android Social Media Upload Automation")
    parser.add_argument("--video", required=True, type=Path, help="Path to the local video file")
    parser.add_argument("--platform", choices=["instagram", "youtube", "all"], default="all", help="Platform to upload to (default: all)")

    args = parser.parse_args()

    caption = read_caption(args.video)

    if args.platform == "instagram":
        instagram(args.video, caption)
    elif args.platform == "youtube":
        youtube(args.video, caption)
    elif args.platform == "all":
        instagram(args.video, caption)
        youtube(args.video, caption)