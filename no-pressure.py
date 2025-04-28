from furhat_remote_api import FurhatRemoteAPI
import time

furhat = FurhatRemoteAPI("localhost")

def run_friendly_session():
    # Start the session with instructions
    furhat.gesture(name="BigSmile")
    furhat.say(text="Hi everyone! It's great to see you all here.", blocking=True)
    furhat.say(text="Today, we're going to have a group discussion, where you will discuss the topic: XX.", blocking=True)
    furhat.say(text="Each of you will have time to speak and share your thoughts. Feel free to build on each other's ideas or share what comes to mind.", blocking=True)
    furhat.say(text="Just remember to stay on topic and enjoy the conversation! Good luck!", blocking=True)
    furhat.gesture(name="Smile")

    # List of motivational messages
    encouragements = [
        "You're doing awesome, keep building on each other's thoughts!",
        "Great work so far, let's keep the discussion going!",
        "Wonderful collaboration happening here!",
        "Let's keep the conversation flowing!",
        "You're all doing a fantastic job, stay focused!",
    ]

    # Announcement: 6 minutes left 
    print("6 minutes left")
    time.sleep(60)  # Wait first minute 

    # Countdown loop from 5 minutes to 1 minute
    for minute_left in range(5, 0, -1):
        print(f"{minute_left} minutes left")
        furhat.say(text=encouragements[5 - minute_left], blocking=True)
        time.sleep(60)

    # After countdown is finished
    print("Time's up!")
    furhat.say(text="That brings us to the end of our discussion. Thank you all for sharing your thoughts today. It's been a pleasure listening to all of you.", blocking=True)
    furhat.say(text="Now, you'll fill out a post-discussion form, which will be handed to you by the experiment coordinator.", blocking=True)
    time.sleep(10)
    furhat.say(text="Please rate your experience during the first discussion by circling a number from 1 to 10 for each question", blocking=True)

# Run the session
run_friendly_session()
