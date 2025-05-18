# pyright: reportUnboundVariable=false
import os, configparser, os.path

# version
ver = "v0.0"
# running [version] Here
print("Running Pudding..." + ver)

def MKCONF():
    global path
    conf = configparser.ConfigParser()
    print("Reading config file")
    if os.path.exists("puding.ini"):
        conf.read("puding.ini")
        path = conf.get("Main", "workspace")
    else:
        print("Couldnt find config file. Making one.")
        path = input("Enter workspace path (the folder where you will store your projects, it should be full path): ")
        conf["Main"] = {"workspace" : path}
        with open("puding.ini", "wt") as f:
            conf.write(f)
        print("Done")


def PROJECTLIST():
    global projects
    os.chdir(path)
    projects = os.listdir(path)
    if projects == []:
        print("No projects yet")
    else:
        for i in range(0, len(projects)):
            print(str(i + 1) + ". " + projects[i])


# x will be our filename
def MKFILE(x):
    if os.name == "nt":
        os.system("type nul > " + x)
    else:
        os.system("touch " + x)


# Clearing Screen.
def CLEARSCR():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Insert a name for the Project
def PROJECTNAME():
    global PR_NAME
    # loops until the project is not blank
    while True:
        PR_NAME = input("Project Name Here >> ")
        if PR_NAME == "":
            print("the Project name cannot be blank.")
        else:
            break
    print("Project Name - " + PR_NAME)


# Choose a Template if you want to.
def PROJECT_TEMP():
    global PR_TE_CONST
    global PR_TEMP
    print("Do you want to choose a Template?  [Y / N]")
    print("(if you don't want to, Manual Configuration will be next Section)")
    while True:
        PR_TE_CONST = input(">> ")
        if PR_TE_CONST == "Y" or PR_TE_CONST == "y":
            while True:
                # just choose one that's not hard tho.
                print("[1] - Progress Bars for Loading")
                print("[2] - Typing Speed Test")
                PR_TEMP = input(">> ")
                if PR_TEMP == "1":
                    print("Selected 1")
                    break
                if PR_TEMP == "2":
                    print("Selected 2")
                    break
                else:
                    print("invaild command.")
            break
        # if no, then skip this
        if PR_TE_CONST == "N" or PR_TE_CONST == "n":
            print("Skipped Project Template Section.")
            break
        else:
            print("Invaild command, Try Again.")


# Sets the Project
def PROJECT_SETUP():
    # variable setup (ik there's a lot of CONSTs but whatever)
    global RNAME
    global CONSTMODULE
    global MODULE
    global CONSTCS
    global RNAME_CONST
    global RNAME_TRUE_OR_FALSE
    RNAME_TRUE_OR_FALSE = False

    # making a directory and switching to this directory
    print("creating and switching Source Directory")
    os.system("mkdir " + PR_NAME)
    os.chdir(PR_NAME)
    os.system("mkdir src")
    os.chdir("src")

    # project name
    print("Applying Project Name")
    PR_NAME_F = PR_NAME + ".txt"
    os.system("touch " + PR_NAME_F)
    with open(PR_NAME_F, "a") as f:
        f.write("as a Reminder: \n")
        f.write("The Project is called: " + PR_NAME + "\n")

    # making main file
    print("Creating index.py")
    MKFILE("index.py")

    # appling Template 1
    if PR_TE_CONST == "Y":
        if PR_TEMP == 1:
            print("choosed the template called 'Progress Bars'.")
            # tqdm is Progress bar generator basically.
            print("Installing / Updating 'tqdm'")
            os.system("pip install tqdm")
            # writing the source code
            print("appling the code...")
            with open("index.py", "a") as f:
                f.write("import start\n")
                f.write("from tqdm import tqdm\n")
                f.write("\n")
                f.write("start.INTRO()\n")
                f.write("# 'x' is the value\n")
                f.write("x = 10000\n")
                f.write("for i in tqdm(range(x)):\n")
                f.write("   pass\n")
            print("Completed!")
        # appling Template 2
        elif PR_TEMP == 2:
            print("choosed the template called 'Typing Test'.")
            print("applying the code...")
            with open("index.py", "a") as f:
                # WPM testing...
                f.write("import time\n")
                f.write("import start\n")
                f.write("\n")
                f.write("start.INTRO()\n")
                f.write("sample = \"Hello i'm a Person\"\n")
                f.write("print(\"type something LONG\")\n")
                f.write("start = time.time()\n")
                f.write("inputTYPE = input(\">> \")\n")
                f.write("end = time.time()\n")
                f.write("\n")
                f.write("speed = len(sample) / (end - start)\n")
                f.write(
                    "print(\"Your Typing Speed is {:.2f} characters per second\".format(speed))\n"
                )
    else:
        # if template Section Skipped then you may need to do everything by hand or not (whatever)
        print("Template Section Skipped, Dropping to Manual Configuration.")
        print("Do you want to change the file name? [Y / N]")
        while True:
            RNAME_CONST = input(">> ")
            if RNAME_CONST == "Y" or RNAME_CONST == "y":
                print("New File Name")
                RNAME = input(">> ")
                RNAME_TRUE_OR_FALSE = True
                RNAME = RNAME + ".py"
                os.rename("index.py", RNAME)
                break
            elif RNAME_CONST == "N" or RNAME_CONST == "n":
                print("Skipped Section: Changing File Name")
                break
            else:
                print("Command Not Found")
        # rendering some text to index.py or whatever else idc.
        print("Configuring main file.")
        if RNAME_TRUE_OR_FALSE:
            with open(RNAME, "a") as f:
                f.write("import start\n")
                f.write("start.INTRO()\n")
        else:
            with open("index.py", "a") as f:
                f.write("import start\n")
                f.write("start.INTRO()\n")
        # importing modules and cheatsheets.
        print("Do you want any module(s)?")
        while True:
            CONSTMODULE = input(">> ")
            if CONSTMODULE == "Y" or CONSTMODULE == "y":
                print("You Should put COMMA between module names.")
                MODULE = input(">> ")
                # import modules Section
                if RNAME_TRUE_OR_FALSE:
                    print("importing modules")
                    with open(RNAME, "a") as f:
                        f.write("import " + MODULE + "\n")
                    break
                else:
                    print("importing modules")
                    with open("index.py", "a") as f:
                        f.write("import " + MODULE + "\n")
                    break
            elif CONSTMODULE == "N" or CONSTMODULE == "n":
                print("skipped Module Section")
                break
            else:
                print("Invaild Command")

        # import a cheatsheet
        print("Do you want to get a Cheatsheet?")
        while True:
            CONSTCS = input(">> ")
            if CONSTCS == "Y" or CONSTCS == "y":
                print("Making file called cheatsheet.txt")
                MKFILE("cheatsheet.txt")
                print("Printing cheatsheet link to 'cheatsheet.txt'")
                with open("cheatsheet.txt", "a") as f:
                    f.write(
                        "https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797\n"
                    )
                    f.write("\n")
                    break
            elif CONSTCS == "N" or CONSTCS == "n":
                print("Skipped Cheatsheet Section")
                break
            else:
                print("Invaild Command")

    # ignore Watermark term, it just sets a starting file.
    print("Project should be finished. Setting up an Watermark file.")
    MKFILE("start.py")
    with open("start.py", "a") as f:
        f.write("# you can delete this if you want to.\n")
        f.write("print(\"\")\n")
        f.write("def INTRO():\n")
        f.write("   print(\"This Project Made Withe Pudding Engine!\")\n")
        f.write(
            "   print(\"If you don't want to see this, remove the file called start.py\")\n"
        )
    print("Project Creation Progress is Finished, Good Luck!")


# All Combined.
def MAKEPROJECT():
    PROJECTNAME()
    PROJECT_TEMP()
    PROJECT_SETUP()


def COMMAND():
    while True:
        print("[n]ew project, [e]xit, [d]elete project, [l]ist projects")
        command = input(">> ")
        if command == "n":
            MAKEPROJECT()
        elif command == "e":
            print("Goodbye.")
            break
        elif command == "d":
            try:
                PR_INDEX = int(input("Which project: ")) - 1
            except:
                PR_INDEX = None
                print("Invalid project index. Selecting none.")
            if PR_INDEX != None:
                os.chdir(projects[PR_INDEX])
                ls = os.listdir()
                for i in ls:
                    try:
                        ls = os.listdir()
                        os.remove(i)
                    except IsADirectoryError:
                        os.chdir(i)
                        ls = os.listdir()
                        for i in ls:
                            try:
                                ls = os.listdir()
                                os.remove(i)
                            except IsADirectoryError:
                                os.chdir(i)
                                ls = os.listdir()
                                for i in ls:
                                    os.remove(i)
                                os.chdir("..")
                        os.chdir("..")
                os.chdir("..")
                ls = os.listdir()
                for i in ls:
                    try:
                        ls = os.listdir()
                        os.rmdir(i)
                    except OSError:
                        os.chdir(i)
                        ls = os.listdir()
                        for i in ls:
                            os.rmdir(i)
                    os.chdir("..")
            print("Done")
            ls = None
        elif command == "l":
            PROJECTLIST()
            

# Execution of code
MKCONF()
PROJECTLIST()
COMMAND()
# MAKEPROJECT()
