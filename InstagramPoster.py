import os
import json
import time
import random
from instabot import Bot
from dotenv import load_dotenv

# Load Instagram credentials from .env file
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Load JSON File here
with open('post.json') as f:
    media_list = json.load(f)


# For choosing image and video post
def post_media(bot, media):
    file_path = media['file_path']
    caption = media['caption']
    media_type = media['type']

    if media_type == 'image':
        bot.upload_photo(file_path, caption=caption)
    elif media_type == 'video':
        bot.upload_video(file_path, caption=caption)

# Interval time between 20 and 30 minutes


def random_sleep():
    return random.randint(20, 30) * 60

# Main Function Here


def main():
    bot = Bot()
    bot.login(username="USERNAME", password="PASSWORD")

    for media in media_list:
        post_media(bot, media)
        print("Success: Post Uploaded successfully!")
        sleep_time = random_sleep()
        print(f"Next post in {sleep_time/60} minutes")
        time.sleep(sleep_time)

    print("Finish!!! All Post from the list have been Uploaded.")


if __name__ == "__main__":
    main()
