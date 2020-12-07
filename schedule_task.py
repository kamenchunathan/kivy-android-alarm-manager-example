"""
schedules an alarm using the android alarm manager

The actual scheduling is done inside the AlarmScheduler java class in the
myapp/ folder which contains java files to be included in the app build

The implementation was done in java instead of python using jnius because of an
error that occurred when using the getClass() method of a reflected java class.
"""
import time
from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
AlarmScheduler = autoclass('org.myapp.AlarmScheduler')


def get_time_5seconds_from_now_in_millis():
    """returns the time 5 seconds from now in milliseconds"""
    return int((time.time() + 5) * 1000)


def schedule_task():
    """
    Schedules a task by calling a method in the alarm scheduler class
    The task itself is in the Notify class in Notify.java which is simply
    to obtain the default ringtone and have it ring

    The current activity is passed when initializing the class because it is a
    requirement when using getSystemService() which is required to get the
    alarm manager.
    """
    this = PythonActivity.mActivity

    alarm_time = get_time_5seconds_from_now_in_millis()
    alarm_scheduler = AlarmScheduler(this)
    alarm_scheduler.setAlarm(alarm_time)
