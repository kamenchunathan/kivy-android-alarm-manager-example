"""
schedules an alarm using the android alarm manager

The actual scheduling is done inside the TaskScheduler java class in the
java_src/ folder which contains java files to be included in the app build


The implementation was done in java instead of python using jnius because of an
error that occurred when using the getClass() method of a reflected java class.
This error is likely related to the kivy version being used at the time of writing and may not be an issue with
later versions hence should be easily implemented in python alone.
"""
import json
import time

from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
TaskScheduler = autoclass('org.test.myapp.TaskScheduler')


def get_time_5seconds_from_now_in_millis():
    """returns the time 5 seconds from now in milliseconds"""
    return int((time.time() + 5) * 1000)


def schedule_task(title='Task title', message='Scheduled Task Activity'):
    """
    Schedules a task by calling the schedule task method of the TaskScheduler class
    The task itself is to run a service defined in the buildozer.spec file

    The current activity is passed when initializing the class because it is a
    requirement when using getSystemService() which is required to get the
    alarm manager.
    """
    task_details = {'title': title, 'message': message}
    python_activity = PythonActivity.mActivity

    task_time = get_time_5seconds_from_now_in_millis()
    task_scheduler = TaskScheduler(python_activity)
    task_scheduler.scheduleTask(task_time, json.dumps(task_details))
