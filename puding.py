import os
import logging

# version
ver = "v0.0"
# running [version] Here
print("Running Pudding..." + ver)

# Setup logs folder and logging
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    try:
        os.makedirs(LOG_DIR)
    except Exception as e:
        print(f"Failed to create log directory: {e}")
        raise

LOG_FILE = os.path.join(LOG_DIR, "pudding.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Pudding started, version %s", ver)

# x will be our filename

def MKFILE(x):
    try:
        if os.name == "nt":
            open(x, 'a').close()
        else:
            open(x, 'a').close()
        logging.info("Created file: %s", x)
    except Exception as e:
        logging.error("Failed to create file %s: %s", x, e)
        print(f"Error creating file {x}: {e}")

# Clearing Screen.
def CLEARSCR():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        logging.info("Screen cleared")
    except Exception as e:
        logging.warning("Failed to clear screen: %s", e)

# Insert a name for the Project

def PROJECTNAME():
    global PR_NAME
    while True:
        PR_NAME = input("Project Name Here >> ")
        if PR_NAME == "":
            print("The Project name cannot be blank.")
        else:
            break
    print("Project Name - " + PR_NAME)
    logging.info("Project name set to: %s", PR_NAME)

# Choose a Template if you want to.

def PROJECT_TEMP():
    global PR_TE_CONST
    global PR_TEMP
    print("Do you want to choose a Template?  [Y / N]")
    print("(if you don't want to, Manual Configuration will be next Section)")
    while True:
        PR_TE_CONST = input(">> ")
        if PR_TE_CONST.lower() == "y":
            while True:
                print("[1] - Progress Bars for Loading")
                print("[2] - Typing Speed Test")
                try:
                    PR_TEMP = int(input(">> "))
                except ValueError:
                    print("Please enter a number.")
                    continue
                if PR_TEMP in [1, 2]:
                    print(f"Selected {PR_TEMP}")
                    logging.info("Template selected: %d", PR_TEMP)
                    break
                else:
                    print("Invalid command.")
            break
        elif PR_TE_CONST.lower() == "n":
            print("Skipped Project Template Section.")
            logging.info("Template section skipped")
            break
        else:
            print("Invalid command, Try Again.")

# Sets the Project

def PROJECT_SETUP():
    global RNAME
    global CONSTMODULE
    global MODULE
    global CONSTCS
    global RNAME_CONST
    global RNAME_TRUE_OR_FALSE
    RNAME_TRUE_OR_FALSE = False

    print("Creating and switching to Source Directory")
    try:
        os.makedirs("src", exist_ok=True)
        os.chdir("src")
        logging.info("Created and switched to src directory")
    except Exception as e:
        logging.error("Failed to setup src directory: %s", e)
        raise

    print("Applying Project Name")
    PR_NAME_F = PR_NAME + ".txt"
    MKFILE(PR_NAME_F)
    try:
        with open(PR_NAME_F, "a") as f:
            f.write("as a Reminder: \n")
            f.write("The Project is called: " + PR_NAME + "\n")
        logging.info("Wrote project name into %s", PR_NAME_F)
    except Exception as e:
        logging.error("Failed to write to %s: %s", PR_NAME_F, e)

    print("Creating index.py")
    MKFILE("index.py")

    if PR_TE_CONST.lower() == "y":
        if PR_TEMP == 1:
            print("Chosen template 'Progress Bars'.")
            print("Installing / Updating 'tqdm'")
            os.system("pip install tqdm")
            print("Applying the code...")
            try:
                with open("index.py", "a") as f:
                    f.write("import start\n")
                    f.write("from tqdm import tqdm\n\n")
                    f.write("start.INTRO()\n")
                    f.write("x = 10000\n")
                    f.write("for i in tqdm(range(x)):\n    pass\n")
                logging.info("Applied progress bar template to index.py")
            except Exception as e:
                logging.error("Failed to apply template 1: %s", e)
        elif PR_TEMP == 2:
            print("Chosen template 'Typing Test'.")
            print("Applying the code...")
            try:
                with open("index.py", "a") as f:
                    f.write("import time\n")
                    f.write("import start\n\n")
                    f.write("start.INTRO()\n")
                    f.write("sample = \"Hello i'm a Person\"\n")
                    f.write("print(\"type something LONG\")\n")
                    f.write("start_time = time.time()\n")
                    f.write("inputTYPE = input(\">> \")\n")
                    f.write("end = time.time()\n\n")
                    f.write("speed = len(sample) / (end - start_time)\n")
                    f.write("print(\"Your Typing Speed is {:.2f} characters per second\".format(speed))\n")
                logging.info("Applied typing test template to index.py")
            except Exception as e:
                logging.error("Failed to apply template 2: %s", e)
    else:
        print("Template Section skipped, manual configuration.")
        logging.info("Manual configuration mode")
        # ... (rest unchanged) ...

    print("Setting up watermark file start.py")
    MKFILE("start.py")
    try:
        with open("start.py", "a") as f:
            f.write("# you can delete this if you want to.\n")
            f.write("def INTRO():\n   print(\"This Project Made With Pudding Engine!\")\n")
            f.write("   print(\"If you don't want to see this, remove the file called start.py\")\n")
        logging.info("Created watermark in start.py")
    except Exception as e:
        logging.error("Failed to write start.py: %s", e)

    print("Project Creation Progress is Finished, Good Luck!")
    logging.info("Project setup completed successfully")

# All Combined.

def MAKEPROJECT():
    PROJECTNAME()
    PROJECT_TEMP()
    PROJECT_SETUP()

# Execution of code
if __name__ == "__main__":
    MAKEPROJECT()
