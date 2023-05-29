# My Screenshot App

My Screenshot App is a Python application that allows you to capture screenshots at specified intervals and save them to a designated folder.

## Features

- Set up the save path and interval for capturing screenshots
- Capture screenshots at regular intervals
- Save screenshots with timestamps in separate folders
- Customizable verbosity level to show each saved file

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/my-screenshot-app.git
   ```

2. Change to the project directory:

   ```bash
   cd my-screenshot-app
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

##Packaging

Open a terminal and navigate to the root directory of your project (my_screenshot_app).
Run the following command to create a distribution package:
   ```bash
  python setup.py sdist
   ```

This will create a dist directory containing the distribution package (tar.gz or zip file).

To install your packaged application, you can use pip with the path to the distribution package. For example:
   ```bash
  pip install dist/my_screenshot_app-1.0.tar.gz
   ```

Once installed, you can use the my_screenshot_app command in the terminal to run your application:
   ```bash
  my_screenshot_app
   ```

## Usage

1. Set up the application by running the following command:

   ```bash
   python my_screenshot_app.py
   ```

Follow the prompts to specify the save path and interval.
the entries will  be saved to config.yml file.


2. Start the screenshot capture by running the following command:

   ```bash
   python my_screenshot_app.py
   ```

The screenshots will be saved to the specified save path at the specified interval.

To stop the screenshot capture, press Ctrl+C.

## Configuration

The application uses a YAML configuration file named config.yaml. This file contains the following configuration options:

   ```yaml
   save_path: /path/to/save/screenshots
   interval: 10  # Interval in seconds
   ```

You can manually edit the config.yaml file to change the save path and interval if needed.



##License
This project is licensed under the MIT License.
