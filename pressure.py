import random
import time
import json
import datetime
import threading
from furhat_remote_api import FurhatRemoteAPI

furhat = FurhatRemoteAPI("localhost")

logs = []  # List to hold logs

participants = ["Anna", "Linnea", "Emma"]

stress_messages = [
    "Tick tock, tick tock...",  
    "(participant), time to say something! Time is ticking!",
    "(participant), have you spoken yet? Time is running out!",
    "Half your time is gone... atime to hurry up.",
    "(participant), do you think you have contributed enough?",
    "If you have something to say... it’s now or never!"
]

session_running = False  # For controlling gaze

def random_gaze():
    while session_running:
        furhat.attend(location="left")
        time.sleep(4)
        furhat.attend(location="right")
        time.sleep(4)
        furhat.attend(location="away")
        time.sleep(4)
        furhat.attend(location="straight")
        time.sleep(4)

def deliver_instructions():
    furhat.say(text="Welcome.", blocking=True)
    furhat.say(text="I will be monitoring this discussion.", blocking=True)
    furhat.say(text="Each of you is expected to speak. You are expected to speak for two minutes. No less.", blocking=True)
    furhat.say(text="You will manage your speaking time as you like.", blocking=True)
#    furhat.say(text="As you speak, you will hear a ticking sound. It will become faster.", blocking=True)
#    furhat.say(text="The sound is there to remind you… that time is running out.", blocking=True)
    furhat.say(text="You may decide yourselves who speaks next.", blocking=True)
    furhat.say(text="The goal is simple: speak. Stay on topic. Do not waste time.", blocking=True)
    furhat.say(text="If time runs out and the task is not completed...", blocking=True)
    furhat.say(text="There will be consequences…", blocking=True)
    furhat.say(text="I’ll be listening.", blocking=True)
    

def log_event(event_type, message):
    logs.append({
        "timestamp": str(datetime.datetime.now()),
        "type": event_type,
        "message": message
    })

def run_pressure_session():
    # Loop until participants confirm understanding
    while True:
        deliver_instructions()

        furhat.say(text="Does everyone understand?", blocking=True)
        response = input("👉 Type 'yes' to proceed, 'no' to repeat instructions: ").strip().lower()

        if response == "yes":
            break
        else:
            print("🔁 Repeating instructions...")
            furhat.say(text="Let me repeat the instructions for you.", blocking=True)

    # SET ANGRY FACE
    furhat.gesture(name="BrowFrown", blocking=False)

    # START RANDOM GAZE MOVEMENT
    global session_running
    session_running = True
    gaze_thread = threading.Thread(target=random_gaze)
    gaze_thread.start()

    log_event("session_start", "pressure_session")

    session_start = time.time()
    random.shuffle(participants)

    furhat.say(text="Begin.", blocking=True)

    for minute_passed in range(7):  # 7 minuter
        target_time = session_start + (minute_passed * 60)

        minutes_left = 7 - minute_passed

        # Always announce minutes left
        if minutes_left > 1:
            furhat.say(text=f"There are {minutes_left} minutes left.", blocking=True)
        elif minutes_left == 1:
            furhat.say(text=f"There is {minutes_left} minute left.", blocking=True)

        log_event("time_update", f"{minutes_left} minutes left")

        # Add extra stress messages
        if minute_passed > 0 and (minute_passed - 1) < len(stress_messages):
            stress_message = stress_messages[minute_passed - 1]
            if "(participant)" in stress_message:
                participant = participants[(minute_passed - 1) % len(participants)]
                stress_message = stress_message.replace("(participant)", participant)
            furhat.say(text=stress_message, blocking=True)
            log_event("stress_message", stress_message)

        # Sleep until next minute
        now = time.time()
        sleep_time = max(0, target_time + 60 - now)
        time.sleep(sleep_time)

    # End of discussion
    furhat.say(text="Time's up! The discussion has ended.", blocking=True)
    log_event("session_end", "pressure_session")

    # STOP RANDOM GAZE
    session_running = False
    gaze_thread.join()

    # Ask manually if the task was completed
    task_completed = input("👉 Was the speaking task completed successfully? (yes/no): ").strip().lower()

    if task_completed == "yes":
        furhat.say(text="You have completed the task. Well done.", blocking=True)
        log_event("task_result", "completed")
    else:
        furhat.say(text="You did not speak enough. You have faild", blocking=True)
        log_event("task_result", "failed")

    # Save logs
    with open("discussion_log.json", "w") as f:
        json.dump(logs, f, indent=4)
    print("✅ Logs saved.")

# Run the session
run_pressure_session()

