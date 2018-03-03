import re
import datetime
import pytz
import csv
import writefuncs
from task import Task

# stores tasks.csv in data variable

with open('tasks.csv') as csvfile:
    data = csvfile.read()

# stores the multiline pattern in tasks variable.

tasks = re.compile(r'''
    ^(?P<Date>\d+/\d+/\d+), # dates
    (?P<Job>[\w*\s?]*), # task Name
    (?P<Notes>[\w*\s?\w*]*), # task notes
    (?P<Time>\d+:*\d*.?:?\d*)$  # task time
''', re.X|re.M)

def main_menue():

    """
    Displays the program options, and takes the users directions to run the program.
    """

    start = True
    print("""Welcome. What would you like to do?\n(A) Add new entry.\n(B) Search by date.\n(C) Exact search.\n(D) Pattern search.\n(E) Task Time.\n(F) Quit.""")



    while start:

        choose = input("Choose your option. ")

        if choose.lower() == 'a':
            a = Task()
            writefuncs.task_file([a.t_date,a.title,a.notes,a.time_spent])
            print('Great the following entry has been created:')
            print(a)
            start = False
        elif choose.lower() == 'b':
            writefuncs.dlookUp()
            start = False
        elif choose.lower() == 'c':
            writefuncs.exactsearch()
            start = False
        elif choose.lower() == 'd':
            writefuncs.relookup()
            start = False
        elif choose.lower() == 'e':
            writefuncs.bytasktime()
            start = False
        elif choose.lower() == 'f':
            start = False
        elif choose != 'a' or 'b' or 'c' or 'd' or 'e' or 'f':
            print("Please choose a valid choice. ")
            continue

if __name__ == '__main__':
    main_menue()
