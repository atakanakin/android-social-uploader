# Android Social Media Upload Automation

Automates video uploads to Instagram Reels and YouTube Shorts on Android devices using ADB and UI automation.

## Features

- Upload videos to Instagram Reels with custom captions
- Upload videos to YouTube Shorts
- Automatic caption loading from `.txt` files
- Command-line interface with flexible options

## Requirements

- Python 3.12+
- Android device with USB debugging enabled
- ADB (Android Debug Bridge) installed
- `uv` package manager

## Setup

1. **Install uv** (if not already installed):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone/sync the project**:

   ```bash
   git clone https://github.com/atakanakin/android-social-uploader.git
   cd android-social-uploader
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

## Usage

### Basic Usage

Upload a video to Instagram:

```bash
uv run main.py --video path/to/video.mp4 --platform instagram
```

Upload a video to YouTube:

```bash
uv run main.py --video path/to/video.mp4 --platform youtube
```

Upload to both platforms:

```bash
uv run main.py --video path/to/video.mp4 --platform all
```

### Caption Support

Create a text file with the same name as your video to automatically load captions:

```
video.mp4
video.txt  # Contains the caption text
```

If no `.txt` file exists, an empty caption will be used.

### Device Setup

1. Enable USB debugging on your Android device
2. Connect device via USB
3. Ensure ADB can detect the device: `adb devices`

## Project Structure

- `core/` - Core utilities and device operations
- `platforms/` - Platform-specific UI automation
- `pipelines/` - High-level workflow orchestration
- `utils/` - Shared helper functions

## Development

To contribute or modify the code:

1. Install dependencies: `uv sync`
2. Make changes to the relevant modules
3. Test with: `uv run main.py --video test.mp4 --platform instagram`
