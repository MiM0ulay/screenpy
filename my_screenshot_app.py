import pyautogui
import datetime
import time
import os
import yaml
import click


def setup():
    # Ask the user for the path to save the screenshots
    save_path = input("Enter the path to save the screenshots: ")

    # Ask the user for the interval between screenshots
    interval = input("Enter the interval between screenshots (in seconds): ")

    # Create a dictionary with the save path and interval
    config = {"save_path": save_path, "interval": interval}

    # Save the configuration to a YAML file
    with open("config.yaml", "w") as file:
        yaml.dump(config, file)

    print("Setup completed successfully.")

def take_screenshots(save_path, interval, verbose):
    # Create a folder with a timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = os.path.join(save_path, timestamp)
    os.makedirs(folder_name)
    print("Folder created:", folder_name)

    # Take screenshots at the specified interval
    count = 1
    try:
        while True:
            # Get the current timestamp
            now = datetime.datetime.now()
            screenshot_timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

            # Capture the screenshot
            screenshot = pyautogui.screenshot()

            # Save the screenshot in the folder
            file_name = os.path.join(folder_name, f"screenshot_{screenshot_timestamp}.png")
            screenshot.save(file_name)

            if verbose:
                print(f"Screenshot {count} saved as {file_name}", flush=True)

            count += 1
            time.sleep(interval)

    except KeyboardInterrupt:
        print("Screenshot capturing stopped.")

@click.command()
@click.option('--verbose', is_flag=True, help='Enable verbosity to show each saved file')
def main(verbose):
    # Check if the setup has been completed
    try:
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        config = None
    except yaml.YAMLError as e:
        print("Error loading configuration file:", str(e))
        config = None

    if config is None or "save_path" not in config or "interval" not in config:
        setup()
    else:
        save_path = config["save_path"]
        interval = float(config["interval"])

        if not save_path or interval <= 0:
            print("Invalid configuration. Make sure 'save_path' is specified and 'interval' is a positive number.")
            exit(1)

        click.echo("Starting the screenshot app...")
        click.echo(f"Save path: {save_path}")
        click.echo(f"Interval: {interval} seconds")
        click.echo(f"Verbosity: {'Enabled' if verbose else 'Disabled'}")
        click.echo("Press Ctrl+C to stop.")

        # Call the function to take screenshots
        take_screenshots(save_path, interval, verbose)


if __name__ == "__main__":
    main()


