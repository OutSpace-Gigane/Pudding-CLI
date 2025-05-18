import time
import start

start.INTRO()

print("Type Something Long")
start = time.time()
WPMTESTER = input(">> ")
end = time.time()

speed = len(WPMTESTER) / (end - start)
print(f"Typing Speed is {speed:.2f} characters per second.")
