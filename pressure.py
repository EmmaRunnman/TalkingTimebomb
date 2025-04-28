import time
import json
import datetime
from furhat_remote_api import FurhatRemoteAPI

furhat = FurhatRemoteAPI("localhost")

logs = []  # List to hold logs

# Function to log events
def log_event(event_type, message):
    logs.append({
        "timestamp": str(datetime.datetime.now()),
        "type": event_type,
        "message": message
    })

def run_pressure_session():
    # Start the session with instructions
    furhat.say(text="Welcome to the session! I will be monitoring this 10 minutes discussion.", blocking=True)
    furhat.say(text="Each of you will speak, and you will each have two minutes to talk.", blocking=True)
    furhat.say(text="I’ll call out the time each minute to remind you how much time is left.", blocking=True)
    furhat.say(text="Let's begin the discussion!", blocking=True)

    # Log the start of the session
    log_event("session_start", "pressure_session")

    session_start = time.time()

    for minute in range(6, 0, -1):  # Loop from 10 minutes down to 1 minute
        furhat.say(text=f"{minute} minutes left.", blocking=True)
        log_event("time_update", f"{minute} minutes remaining")

        # Track time and announce each minute
        time.sleep(60)  

    # End of session
    furhat.say(text="Time's up! The discussion has ended.", blocking=True)
    furhat.say(text="Thank you all for participating.", blocking=True)
    log_event("session_end", "pressure_session")

    # Save logs to a file
    with open("discussion_log.json", "w") as f:
        json.dump(logs, f, indent=4)
    print("✅ Logs saved.")

# Run the session
run_pressure_session()
