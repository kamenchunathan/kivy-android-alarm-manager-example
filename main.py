from datetime import datetime, date, timedelta, time

from kivy import platform
from kivy.logger import Logger
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker


class RootAppLayout(FloatLayout):
    pass


class TodoApp(MDApp):
    title = 'Todo'
    selected_task_time: datetime = ObjectProperty()

    def build(self):
        self.root_widget = RootAppLayout()
        return self.root_widget

    def currently_set_time_or_default(self):
        default_text = 'Set time'
        time_format_string = '%a %d/%m/%Y %I:%M %p'

        if self.selected_task_time:
            return datetime.strftime(self.selected_task_time, time_format_string)
        return default_text

    def schedule_todo_item(self, title, message):
        Logger.debug('App: scheduling todo item')
        if platform == 'android':
            Logger.info('App: scheduling task')
            import schedule_task

            schedule_task.schedule_task(self.selected_task_time, title, message)

    def show_date_picker(self):
        min_date = date.today()
        max_date = date.today() + timedelta(days=365)  # No use in scheduling items a year from now

        date_dialog = MDDatePicker(
            callback=self.set_date,
            min_date=min_date,
            max_date=max_date
        )
        date_dialog.open()

    def show_time_picker(self):
        today = datetime.today()

        time_dialog = MDTimePicker()
        time_dialog.set_time(time(hour=today.hour, minute=today.minute))
        time_dialog.bind(time=self.set_time)
        time_dialog.open()

    def set_date(self, set_date: date):
        self.selected_task_time = datetime(day=set_date.day, month=set_date.month, year=set_date.year)
        self.show_time_picker()

    def set_time(self, _, set_time: time):
        self.selected_task_time = datetime(
            day=self.selected_task_time.day,
            month=self.selected_task_time.month,
            year=self.selected_task_time.year,
            hour=set_time.hour,
            minute=set_time.minute
        )

    def on_selected_task_time(self, instance, selected_task_time):
        self.root_widget.ids.set_time_btn.text = self.currently_set_time_or_default()


if __name__ == '__main__':
    TodoApp().run()
