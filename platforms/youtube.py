import uiautomator2 as u2
from utils.helpers import human_sleep


def automate_youtube_upload(title: str) -> None:
    """Automate the YouTube video upload flow.

    Args:
        title: The title for the video.
    """
    d = u2.connect()
    try:
        d.dump_hierarchy()
    except:
        pass

    print("[UI-YT] Connected to device")
    human_sleep()

    if d(text="Next").exists(timeout=5):
        print("[UI-YT] Clicking Next")
        d(text="Next").click()
        human_sleep()

    if d(text="Next").exists(timeout=5):
        print("[UI-YT] Clicking Next")
        d(text="Next").click()
        human_sleep()

    title_field = d(textContains="Caption your")
    if not title_field.exists():
        title_field = d(className="android.widget.EditText", instance=0)

    if title_field.exists(timeout=10):
        print(f"[UI-YT] Writing title: {title}")
        title_field.click()
        human_sleep()
        d.send_keys(title)

        d.press("back")
        human_sleep()
    else:
        print("[UI-YT] Title field NOT found! Continuing hoping it's pre-filled...")

    if d(text="Next").exists(timeout=5):
        print("[UI-YT] Clicking Next")
        d(text="Next").click()
        human_sleep()
    elif d(description="Next").exists(timeout=5):
        d(description="Next").click()
        human_sleep()

    not_for_kids = d(textContains="not made for kids")

    if not_for_kids.exists(timeout=5):
        print("[UI-YT] Selecting 'Not made for kids'")
        not_for_kids.click()
        human_sleep()
    else:
        print("[UI-YT] WARNING: 'Made for kids' selection not found. Upload might fail.")

    upload_btn = d(textContains="Upload Short")

    if upload_btn.exists(timeout=5):
        print("[UI-YT] Clicking Upload")
        upload_btn.click()
        print("[UI-YT] Upload started!")
    else:
        print("[UI-YT] Upload button NOT found.")

    human_sleep()