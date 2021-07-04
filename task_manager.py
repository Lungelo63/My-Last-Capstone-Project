#importing current date
from datetime import datetime
#opening user file
user_file = open("user.txt", "r+")


login = False
#while login is false,
#if user enters correct credentials, login
#changes to True. Giving exccess
while login == False:
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    for lines in user_file:
        valid_user, valid_password = lines.split(", ")
        
        if valid_user == username and valid_password == password:
            login = True
            print("Logging in...")
        if valid_user != username and valid_password != password:
            print("Invalid login details")
    user_file.seek(0)
user_file.close()
    

#choices for the user to choose from
choices = input('''Select option one below:
r - register username
a - add task
va - view all tasks
vm - view my tasks
e - exit
s - stats
gr - general reports
''')


#if user selects admin selects "r" he can
#register a user to user_file

def reg_user():

    if username == "admin":
        new_userLogin = False

        new_usersName = input("Enter username: ")
        regstr = open("user.txt", "r+")
        v_user, v_password = lines.split(", ")
        
        
        while new_userLogin == False:
            if new_usersName != v_user:
                new_userPass = input("Enter password: ")
                validate = input("Confirm password: ")
            elif new_usersName == v_user:
                print("That username is unavailable. Pick another one")
                new_usersName = input("Enter username: ")
                new_userPass = input("Enter password: ")
                validate = input("Confirm password: ")
                

            if new_userPass == validate:
                new_userLogin = True

            if new_userPass != validate:
                print("password did not match. Try again")

            if new_userPass == validate:
                print("password matches. New user created")
                append_me = open("user.txt", "a")
                append_me.write("\n" + str(new_usersName) + ", " + str(validate))
                append_me.close()
    if username != "admin":
        print("Only admin can add a new user.")

if choices == "r":
    register = reg_user()
    print(register)


def add_task():
    
    tasks = open("tasks.txt", "a")
    assignee = input("Enter the usersname of assignee: ")
    title = input("Enter the title of the task: ")
    description = input("Enter task description: ")
    due_date = input("Enter task due date: ")
    date = datetime.now()
    completed = "no"
        
    tasks.write(str(assignee) + ", " + str(title) + ", " + str(description) + ", " + str(due_date)
                        + ", " + str(date) + ", " + str(completed) + "\n")
    tasks.close

if choices == "a":
    adding_task = add_task()
    print(adding_task)



#if user selects "va" he will be given info
#of every file in an easy to read format
def view_all():
    tasks_file = open("tasks.txt", "r+")
    
    for line in tasks_file:
        assignee, title, description, due_date, date, completed = line.split(", ")
        
        
        print(f'''
        Name:          {assignee}
        Title:         {title}
        Description:   {description}
        Due Date:      {due_date}
        Date Assigned: {date}
        Task Complete: {completed}
        ''')
    tasks_file.close()

if choices == "va":
    all_view = view_all()
    print(all_view)

#if user selects "vm" program
#will desplay specific user task
def view_mine():
    view = open("tasks.txt", "r")
    task_numb = 0
    
    for line in view:
        assignee, title, description, due_date, date, completed = line.split(", ")
        if username == assignee:
            task_numb += 1
            
            print(f'''
            task number:   {task_numb}
            Name:          {assignee}
            Title:         {title}
            Description:   {description}
            Due Date:      {due_date}
            Date Assigned: {date}
            Task Complete: {completed}
            ''')
        
    new_task = input("Would you like to edit a task?")
    if new_task != "-1":
        task_num = input("Please enter the task number: ")
        task_file = view.readlines()
        
        
        
        
        
        
        view.close()
if choices == "vm":
    my_view = view_mine()
    print(my_view)


#if the user selects "e" program
#breaks
if choices == "e":
    print("closing program...")
    breakpoint


#if user selects "s". number of tasks and
#number of users are displayed
if choices == "s":
    stats_file = open("tasks.txt", "r+")
    other_stats = open("tasks.txt", "r+")
    if username == "admin":
        
        
        num_title = 0
        num_assignee = 0
        for line in stats_file:
            assignee, title, description, due_date, date, completed = line.split(", ")
            assignee
            num_assignee += 1
        print(f'''
        Total number of users: {num_assignee}
            ''')
        stats_file.close
        
        
    
        for title in other_stats:
            assignee, title, description, due_date, date, completed = title.split(", ")
            title
            num_title += 1
        print(f'''
        Total number of tasks: {num_title}
            ''')
        other_stats.close()

#if the user select "gr"... 
#the progaram writes and prints out the info
if choices == "gr":
    task_overview = open("task_overview.txt", "w+")
    user_overview = open("user_overview.txt", "w+")
    file_overview = open("tasks.txt", "r+")
    
    numOf_tasks = 0
    for tasks in file_overview:
        assignee, title, description, due_date, date, completed = tasks.split(", ")
        description
        numOf_tasks += 1
        
        uncompleted_tasks = 0
        if completed == "no":
            uncompleted_tasks += 1
            
        completed_tasks = 0
        if completed == "yes":
            completed_tasks += 1
        
        
            
