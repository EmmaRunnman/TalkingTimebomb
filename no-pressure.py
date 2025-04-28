from furhat_remote_api import FurhatRemoteAPI
import time

furhat = FurhatRemoteAPI("localhost")

def run_friendly_session():
    # Start the session with instructions
    furhat.gesture(name="BigSmile")
    furhat.say(text="Hi everyone! It's great to see you here.", blocking=True)
    furhat.say(text="You're about to have a group discussion.", blocking=True)
    furhat.say(text="Each of you will have time to speak and share your thoughts.", blocking=True)
    furhat.say(text="Feel free to build on each other's ideas or share what comes to mind. ", blocking=True)
    furhat.say(text="Just remember to stay on topic and enjoy the conversation! Good luck!", blocking=True)
    furhat.gesture(name="Smile")

    # Print the total time at the beginning
    print("10 minutes left")

    # Countdown loop from 9 to 1    
    for minute in range(7, 0, -1): 
        time.sleep(60)
        print(f"{minute} minutes left")
    
    # Wait the final minute before ending
    time.sleep(60) 

    # End the session after 10 minutes
    furhat.say(text="Time's up! Thanks so much for being part of this discussion. You all did great!", blocking=True)
    print(f"{minute} minutes left")

# Run the session
run_friendly_session()
