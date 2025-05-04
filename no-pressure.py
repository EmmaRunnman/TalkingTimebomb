from furhat_remote_api import FurhatRemoteAPI
import time

furhat = FurhatRemoteAPI("localhost")

# List of motivational messages
encouragements = [
    "You're doing awesome, keep building on each other's thoughts!",
    "Great work so far, let's keep the discussion going!",
    "Wonderful collaboration happening here!",
    "Let's keep the conversation flowing!",
    "You're all doing a fantastic job, stay focused!",
]

def run_friendly_session():
    furhat.gesture(name="BigSmile")
    furhat.say(text="Hi everyone! It's great to see you all here.", blocking=True)
    furhat.say(text="Today, we're going to have a group discussion, where you will discuss the topic: Technology in Education.", blocking=True)
    furhat.say(text="Each of you will have time to speak and share your thoughts. Feel free to build on each other's ideas or share what comes to mind.", blocking=True)
    furhat.say(text="Just remember to stay on topic and enjoy the conversation!", blocking=True)
    furhat.gesture(name="Smile")

def run_non_pressure_session():
    # Repeat instructions until participants confirm
    while True:
        run_friendly_session()
        furhat.say(text="Does everyone understand?", blocking=True)
        response = input("👉 Type 'yes' to proceed, 'no' to repeat instructions: ").strip().lower()

        if response == "yes":
            furhat.say(text="Great! Let's begin the discussion.", blocking=True)
            break
        else:
            print("🔁 Repeating instructions...")
            furhat.say(text="Let me repeat the instructions for you.", blocking=True)

    # Initial time announcement
    print("6 minutes left")
    time.sleep(60)

    # Countdown with encouragements
    for minute_left in range(5, 0, -1):
        print(f"{minute_left} minutes left")
        furhat.say(text=encouragements[5 - minute_left], blocking=True)
        time.sleep(60)

    # Discussion ends
    print("Discussion ended.")
    furhat.say(text="That brings us to the end of our discussion. Thank you all for sharing your thoughts today. It's been a pleasure listening to all of you.", blocking=True)

    furhat.say(text="Now, you'll fill out a post-discussion form, which will be handed to you by the experiment coordinator.", blocking=True)

    time.sleep(5)

    furhat.say(text="Please rate your experience during the first discussion by circling a number from 1 to 10 for each question.", blocking=True)

    time.sleep(10)

    furhat.say(text="After you all have completed the form, we will begin our next part of the experiment.", blocking=True)

# Run the session
run_non_pressure_session()
