import uiautomator2 as u2
from utils.helpers import human_sleep


def automate_reels_post(caption: str) -> None:
    """Automate the Instagram Reels upload flow.

    Args:
        caption: The caption text to add to the post.
    """
    d = u2.connect()
    d.dump_hierarchy()
    print("[UI] Connected to device via uiautomator2")
    human_sleep()

    if d(text="Instagram").exists(timeout=5):
        print("[UI] Clicking 'Instagram' on Share Sheet")
        d(text="Instagram").click()
        human_sleep()

    if d(textContains="Reel").exists(timeout=10):
        print("[UI] Selecting 'Reel' mode")
        d(textContains="Reel").click()
        human_sleep()

    if d(text="Next").exists(timeout=10):
        print("[UI] Clicking 'Next'")
        d(text="Next").click()
        human_sleep()

    print("[UI] Looking for caption field...")
    caption_box = d(className="android.widget.EditText")

    if not caption_box.exists():
        caption_box = d(textContains="caption")

    if caption_box.exists(timeout=10):
        print("[UI] Caption field found. Writing...")
        caption_box.click()
        human_sleep()
        d.send_keys(caption)
        human_sleep()

        d.press("back")
        human_sleep()

        if d(text="OK").exists(timeout=3):
            print("[UI] Clicking 'OK' button")
            d(text="OK").click()
        elif d(description="Done").exists(timeout=3):
            print("[UI] Clicking 'Done' checkmark")
            d(description="Done").click()

        human_sleep()
    else:
        print("[UI] WARNING: Caption field NOT found!")

    if d(text="Share").exists(timeout=5):
        print("[UI] Clicking 'Share'")
        d(text="Share").click()
        print("[UI] Share button clicked")
    elif d(textContains="Share").exists(timeout=5):
        d(textContains="Share").click()
        print("[UI] Share button clicked (fuzzy)")
    else:
        print("[UI] Share button NOT found.")

    human_sleep()