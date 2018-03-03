import re
import datetime
import pytz



class Task:
    fmt = '%d/%m/%Y'
    '''
    Will create a Task object with the title, date,notes, and time attributes.
    '''

    def __init__(self,title=None,time_spent=None,notes=None,t_date=None):
        self.title = input("Title os Task: ")
        while True:
            try:
                task_time = int(input("Duration in minutes? "))
                self.time_spent = datetime.timedelta(minutes=task_time).total_seconds()/60
                # self.time_spent = datetime.timedelta(minutes=task_time).total_seconds()/60/60
                break
            except ValueError:
                print("Please enter a valid value for time. ")
        self.notes = input("Task Notes: ")
        while True:
            try:
                t_date = input("Enter date in 'DD/MM/YYYY' format: ")
                realdate = datetime.datetime.strptime(t_date, Task.fmt)
                self.t_date = realdate.strftime(Task.fmt)
                break
            except ValueError:
                print("Make sure you are using 'DD/MM/YYYY' format. ")


    def __repr__(self):
        return('Task date: ' + self.t_date + '\n' +
                'Task title: ' + self.title + '\n' +
                'Task time: ' + str(self.time_spent) + ' minutes \n' +
                'Task notes: ' + self.notes)
