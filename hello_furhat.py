from furhat_remote_api import FurhatRemoteAPI
import re
import time
import json
import datetime

# Anslut till Furhat som kör lokalt
furhat = FurhatRemoteAPI("localhost")

logs = []

furhat.say(text="Hello! I am Furhat, your social robot.")

# Fråga efter namn
furhat.say(text="What is your name?", blocking=True)
response = furhat.listen()
name = response.message

# Spara logg
logs.append({
    "timestamp": str(datetime.datetime.now()),
    "prompt": "What is your name?",
    "user_input": name
})

# Furhat svarar med namnet
furhat.say(text=f"Nice to meet you, {name}!")

# Spara till JSON
with open("interaction_log.json", "w") as f:
    json.dump(logs, f, indent=4)