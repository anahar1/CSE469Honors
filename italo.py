import requests
import json
from datetime import datetime
import time

# get username input from user
username = input("Enter Instagram username: ")

try:
    # get the user's profile data
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    while response.status_code == 429: # handle rate limiting
        print("Rate limited. Retrying in 30 seconds...")
        time.sleep(30)
        response = requests.get(url)
    data = json.loads(response.text)

    # extract the join date from the profile data
    joined_timestamp = data["graphql"]["user"]["date_joined"]
    joined_date = datetime.fromisoformat(joined_timestamp[:19])

    # print the join date in a formatted string
    print(f"{username} joined Instagram on {joined_date.strftime('%B %d, %Y')}")
except Exception as e:
    print("Error:", e)