# pyright: reportUnboundVariable=false
import os

# version
ver = "v1.001"
# running [version] Here
print("Running Pudding... " + ver)


# x will be our filename
def MKFILE(x):
    # nt means windows which makes the project can run in Windwos too :)
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
                    print("invalid command.")
            break
        # if no, then skip this
        if PR_TE_CONST == "N" or PR_TE_CONST == "n":
            print("Skipped Project Template Section.")
            break
        else:
            print("Invalid command, Try Again.")


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
    os.system("mkdir src")
    os.chdir("src")

    # Applying project name to file
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
        if PR_TE_CONST == "Y" or PR_TE_CONST == "y":
            if PR_TEMP == "1":
                print("choosed the template called 'Progress Bars'.")
                # tqdm is Progress bar generator basically.
                print("Installing / Updating 'tqdm'")
                os.system("pip install tqdm")
                # writing the source code (simplier than previous version.)
                print("appling the code...")
                # Shorter code to export, see SAMPLE Directory of Project for more info
                with (
                    open("../SAMPLE/prgbars.py", "r") as f1,
                    open("index.py", "a") as f2,
                ):
                    for line in f1:
                        f2.write(line)
                print("Completed!")
            # appling Template 2
            elif PR_TEMP == "2":
                print("choosed the template called 'Typing Test'.")
                print("appling the code...")
                with (
                    open("../SAMPLE/wpm-test.py", "r") as f1,
                    open("index.py", "a") as f2,
                ):
                    for line in f1:
                        f2.write(line)
        elif PR_TE_CONST == "N" or PR_TE_CONST == "n":
            # if template Section Skipped then you may need to do everything by hand or not (whatever)
            print("Template Section Skipped, Dropping to Manual Configuration.")
            print("Do you want to change the file name? [Y / N]")
            while True:
                # ask if user wants to change name of file
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
                    print("Invalid Command")

            # import a cheatsheet
            print("Do you want to get a Cheatsheet?")
            while True:
                CONSTCS = input(">> ")
                if CONSTCS == "Y" or CONSTCS == "y":
                    print("Making file called cheatsheet.txt")
                    MKFILE("cheatsheet.txt")
                    print("Printing cheatsheet link to 'cheatsheet.txt'")
                    with (
                        open("../SAMPLE/cheatsheet.txt", "r") as f1,
                        open("cheatsheet.txt", "w") as f2,
                    ):
                        for line in f1:
                            f2.write(line)
                        break
                elif CONSTCS == "N" or CONSTCS == "n":
                    print("Skipped Cheatsheet Section")
                    break
                else:
                    print("Invalid Command")

    print("Setting up an Enginner.")
    MKFILE("enginner.py")
    with open("../SAMPLE/enginner.py", "r") as f1, open("enginner.py", "a") as f2:
        for line in f1:
            f2.write(line)
    # ignore Watermark term, it just sets a starting file.
    print("Project should be finished now setting up an Watermark file.")
    MKFILE("start.py")
    # should replace when it makes troubles
    with open("start.py", "a") as f:
        f.write("# you can delete this if you want to.\n")
        f.write("""print("")\n""")
        f.write("def INTRO():\n")
        f.write("""   print("This Project Made With Puding Engine!")\n""")
        f.write(
            """   print("If you don't want to see this, remove the file called start.py")\n"""
        )
    print("Project Creation Progress is Finished, Good Luck!")


# All Combined.
def MAKEPROJECT():
    PROJECTNAME()
    PROJECT_TEMP()
    PROJECT_SETUP()


# Execution of code
MAKEPROJECT()
