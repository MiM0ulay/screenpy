import pyautogui
import datetime


def take_screenshot():
    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot
    file_name = f"screenshot_{timestamp}.png"
    screenshot.save(file_name)
    print(f"Screenshot saved as {file_name}")


if __name__ == "__main__":
    take_screenshot()
