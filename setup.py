from setuptools import setup

setup(
    name='my_screenshot_app',
    version='1.0',
    py_modules=['my_screenshot_app'],
    install_requires=[
        'pyautogui',
        'PyYAML',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'my_screenshot_app = my_screenshot_app:main',
        ],
    },
)
