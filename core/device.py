import subprocess
from subprocess import CompletedProcess
import re
import time
from core.config import ADB_BINARY


def run_adb(command: list[str], shell: bool = False) -> CompletedProcess:
    """Run an ADB command.

    Args:
        command: List of command arguments.
        shell: Whether to run the command with shell=True.

    Returns:
        CompletedProcess with the command result.
    """
    return subprocess.run(
        [ADB_BINARY] + command, shell=shell, capture_output=True, text=True, check=True
    )


def ensure_device_connected(device_ip: str) -> None:
    """Ensure that the Android device is connected via ADB over network.

    Args:
        device_ip: IP address of the Android device.
    """
    print(f"[+] Connecting to device at {device_ip}...")
    run_adb(["connect", device_ip])
    time.sleep(3)


def push_video(local_path: str, device_path: str) -> None:
    """Push a video file to the Android device.

    Args:
        local_path: Path to the local video file.
        device_path: Path on the device to save the file.
    """
    run_adb(["push", local_path, device_path])


def delete_video(device_path: str) -> None:
    """Delete a video file from the Android device.

    Args:
        device_path: Path to the file on the device.
    """
    run_adb(["shell", "rm", device_path])


def scan_media(device_path: str) -> None:
    """Trigger Android media scanner for a file.

    Args:
        device_path: Path to the file on the device.
    """
    run_adb(
        [
            "shell",
            "am",
            "broadcast",
            "-a",
            "android.intent.action.MEDIA_SCANNER_SCAN_FILE",
            "-d",
            f"file://{device_path}",
        ]
    )


def _get_media_id(device_path: str) -> str:
    """Get the media ID for a file from MediaStore.

    Args:
        device_path: Path to the file on the device.

    Returns:
        The media ID as a string.
    """
    real_path = device_path.replace("/sdcard/", "/storage/emulated/0/")
    cmd = f"adb shell content query --uri content://media/external/video/media --projection _id --where \"_data=\\'{real_path}\\'\""

    for _ in range(10):
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout.strip()

        if "_id=" in output:
            match = re.search(r"_id=(\d+)", output)
            if match:
                return match.group(1)

        time.sleep(1)

    raise RuntimeError(f"Media ID not found for {device_path}")


def open_instagram_share(device_path: str) -> None:
    """Open Instagram share intent for a video file.

    Args:
        device_path: Path to the video file on the device.
    """
    scan_media(device_path)

    try:
        media_id = _get_media_id(device_path)
        content_uri = f"content://media/external/video/media/{media_id}"
    except RuntimeError:
        content_uri = f"file://{device_path}"

    print("[ADB] Warming up Instagram...")
    run_adb(
        [
            "shell",
            "monkey",
            "-p",
            "com.instagram.android",
            "-c",
            "android.intent.category.LAUNCHER",
            "1",
        ]
    )

    time.sleep(4.0)

    print("[ADB] Launching Share Intent...")
    run_adb(
        [
            "shell",
            "am",
            "start",
            "-a",
            "android.intent.action.SEND",
            "-t",
            "video/mp4",
            "--eu",
            "android.intent.extra.STREAM",
            content_uri,
            "-n",
            "com.instagram.android/com.instagram.share.handleractivity.ShareHandlerActivity",
            "-f",
            "0x10000000",
        ]
    )


def open_youtube_share(device_path: str) -> None:
    """Open YouTube share intent for a video file.

    Args:
        device_path: Path to the video file on the device.
    """
    scan_media(device_path)

    try:
        media_id = _get_media_id(device_path)
        content_uri = f"content://media/external/video/media/{media_id}"
    except RuntimeError:
        content_uri = f"file://{device_path}"

    print("[ADB] Launching YouTube Upload Intent...")
    run_adb(
        [
            "shell",
            "am",
            "start",
            "-a",
            "android.intent.action.SEND",
            "-t",
            "video/*",
            "--eu",
            "android.intent.extra.STREAM",
            content_uri,
            "-n",
            "com.google.android.youtube/com.google.android.apps.youtube.app.application.Shell_UploadActivity",
            "-f",
            "0x1",
        ]
    )
