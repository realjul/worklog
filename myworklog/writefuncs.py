import re
import csv
import datetime
import pdb
from task import Task


with open('tasks.csv') as csvfile:
    data = csvfile.read()

tasks = re.compile(r'''
    ^(?P<Date>\d+/\d+/\d+), # dates
    (?P<Job>[\w*\s?]*), # task Name
    (?P<Notes>[\w*\s?\w*]*), # task notes
    (?P<Time>\d+:*\d*.?:?\d*)$  # task time
''', re.X|re.M)

fmt = '%d/%m/%Y'


def task_file(mylist):

    '''
    Writes the tasks created with Task class.

    '''
    # with open('tasks.txt','a') as file:
    #     file.write(tsk)
    with open('tasks.csv', 'a') as file:
        wr = csv.writer(file, delimiter=',')
        wr.writerow(mylist)


def dlookUp():
    """
    Looks up data by date. Uses while loop to keep running untill the user quits.
    """
    # pdb.set_trace()
    with open('tasks.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        rows = list(data)

    while True:
        not_inrow = []
        new_rows = []
        try:
            in_date = input('Search Date: \nPlease use DD/MM/YYYY format. ')
            if isinstance(datetime.datetime.strptime(in_date,'%d/%m/%Y'),datetime.date):
                for row in rows:
                    if len(row) == 0:
                        continue
                    elif row[0] == in_date:
                        print(', '.join(row))
                        new_rows.append(in_date)
                        continue
                if len(new_rows) == 0:
                    print('Date: {} not found.'.format(in_date))


        except ValueError:
            print('Please use a valid date format: DD/MM/YYYY .')

        another = input('Search another date? Enter N to quit or press Enter to search another date. ')
        if another.lower()  == 'n':
            break
        else:
            continue


def bytasktime():
    """
    Find task by time.
    """

    yes = True

    while yes:
        not_found = []
        try:
            time = input("Which time duration are you looking for?\nUse minutes ")

            time2 = datetime.timedelta(minutes = int(time))/60

            if isinstance(time2,datetime.timedelta):
                for match in tasks.finditer(data):
                    if match.group('Time') == str(float(time)):
                        print(match.group())
                        not_found.append(match.group())
            if len(not_found) == 0:
                print("Mmm. Looks like you query was not found. ")


        except ValueError:
                print("Try again.")
                continue

        del(not_found)

        query = input("Search another task time. Y/N ")

        if query.lower() == 'n':
            yes = False
        else:
            continue


def exactsearch():
    """
    Uses two loops to get user input for direction to where to search for the
    text or pattern.
    """
    letsgo = True
    where_bool = True
    title = None
    while where_bool:
        where = input('Where would you like to search? [J]ob or [N]otes. ')
        if where.lower() == 'j':
            title = 'Job'
            where_bool = False
        elif where.lower() == 'n':
            title = 'Notes'
            where_bool = False
        elif where.lower() == 'q':
            where_bool = False
            letsgo = False
            print('Thank you.')
        else:
            print('Please choose [J]ob or [N]otes. ')
            continue


    while letsgo:

        emp_list = []
        pattern = input('Type the text you are looking for: ')

        for pat in tasks.finditer(data):
            if (re.findall(r'\b{x}\b'.format(x = pattern),pat.group(title))):
                print("Date: " + pat.group('Date') +" Title: " + pat.group('Job')+', Your string: '+
                pattern)
                emp_list.append(pat)

        #         foundre.append(', '.join(re.findall(r'{}'.format(pattern),pat.group(title))))
            elif (re.findall(r'{}'.format(pattern),pat.group(title))) == False:
                continue
        if not emp_list:
            print("Your search came back empty.")
        another = input("Would you like anothe search? Y/N ")
        if another.lower() == 'n':
            letsgo = False
        elif another.lower() == 'y':
            continue

    del(emp_list)


def relookup():
    """
    Uses two loops to get user input for direction to where to search for the
    text or pattern.
    """
    the_title = True
    x = True
    while the_title:

        title = input("Where would you like to search? [N]otes or [J]ob? ")
        if title.lower() == 'n':
            title2 = 'Notes'
            the_title = False
        elif title.lower() == 'j':
            title2 = 'Job'
            the_title = False
        else:
            cont = input("Please type '[N]otes/[J]ob'. To quit enter 'Q' else press Enter: ")
            if cont.lower() == 'q':
                the_title = False
                x = False
                print('Thank you.')
            else:
                continue
    while x:
        found = []
        pattern = input("Pattern: ")
        for pat in tasks.finditer(data):
            if (re.findall(r'{}'.format(pattern),pat.group(title2))):
                print("Date: " + pat.group('Date') +" Title: " + pat.group('Job')+', Pattern: '+
                (', '.join(re.findall(r'{}'.format(pattern),pat.group(title2)))))
                found.append((re.findall(r'{}'.format(pattern),pat.group(title2))))
            elif (re.findall(r'{}'.format(pattern),pat.group(title2))) == False:
                continue
    #         if len(found) == 0:
    #             print("No pattern found.")

        another = input("Search another pattern? Y/N")
        if another.lower() == "n":
            x = False
        else:
            continue


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
