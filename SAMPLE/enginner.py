import os

# if you new to Python CLI stuff, it would be a cool script
# It's just a helper for Post-Pudding-Project Setup
# you can think it's a Cargo.toml (Rust) made for Python.
# but MUCH Different.


def MKFILE(x):
    if os.name == "nt":
        os.system("type nul > " + x)
    else:
        os.system("touch " + x)


print("Welcome to the Settings for the Engine.")
print("If you want any Helpful thing that you miss, this is the place that you wanted!")

print("[1] - Get a Cheatsheet")
print("[2] - Get a Template")
print("")
print("Which Setting do you want?")

i = input("  ")
while True:
    if i == "1":
        print("Importing 'Cheatsheet'")
        with (
            open("../SAMPLE/cheatsheet.txt", "r") as f1,
            open("cheatsheet.txt", "a") as f2,
        ):
            for line in f1:
                f2.write(line)
        print("Done!")
        break
    elif i == "2":
        print("[1] - Progress bars for Loading.")
        print("[2] - Typing Speed Test")
        print("which template do you choose?")
        i1 = input("  ")
        if i1 == "1":
            print("Importing 'Progress Bars for Loading'")
            with open("../SAMPLE/prgbars.py", "r") as f1, open("prgbars.py", "a") as f2:
                for line in f1:
                    f2.write(line)
            print("Done!")
            break
        elif i1 == "2":
            print("Importing 'WPM-Test'")
            with (
                open("../SAMPLE/wpm-test.py", "r") as f1,
                open("wpm-test.py", "a") as f2,
            ):
                for line in f1:
                    f2.write(line)
            print("Done!")
            break
    else:
        print("Invaild Command, Try Again")
