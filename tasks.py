import os
import json

from kivy.app import App
from kivy.logger import Logger
from plyer import notification


if __name__ == '__main__':
    received_argument = os.getenv("PYTHON_SERVICE_ARGUMENT")
    Logger.info('Tasks: argument passed to python: {0}'.format(received_argument))

    # Convert the argument from string to json
    task: dict = json.loads(received_argument)

    notification.notify(
        title=task.get('title', ''),
        message=task.get('message', ''),
        app_name=App.title,
        timeout=3
    )
