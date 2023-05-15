# Importing necessary modules
import time
import winsound

# Function for alarm clock
def alarm_clock(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        if current_time == alarm_time:
            print("Wake up buddy!")
            # Play a sound
            winsound.Beep(440, 1000)  # Change frequency and duration as desired
            break
        time.sleep(1)

# Function for stopwatch
def stopwatch():
    start_time = time.time()
    input("Please press Enter to stop the stopwatch.")
    elapsed_time = time.time() - start_time
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))

# Function for timer
def timer(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = end_time - time.time()
        print("The remaining time: {:.2f} seconds".format(remaining_time), end="\r")
        time.sleep(0.1)
    print("Time's up buddy!")

# Examples:
alarm_time = "04:00:00"
alarm_clock(alarm_time)

stopwatch()

duration = 60  # 1 minute
timer(duration)
