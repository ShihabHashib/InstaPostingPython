# Instagram Auto Posting Python Script

## Overview

This Python script automates the process of posting images and videos to Instagram. It utilizes the `instabot` library for interacting with Instagram and the `dotenv` library for loading Instagram credentials from a `.env` file.

## Features

- Automatic posting of images and videos to Instagram.
- Randomized intervals between posts to simulate human-like behavior.
- Configuration through a JSON file (`post.json`) where you can specify the media files and captions.

## Prerequisites

- Python 3.x
- `instabot` library: Install using `pip install instabot`
- `dotenv` library: Install using `pip install python-dotenv`

## Usage

1. Create a virtual environment (optional but recommended).
2. Install the required dependencies: `pip install instabot python-dotenv`.
3. Create a `.env` file with your Instagram credentials:

   ```env
   USERNAME=your_instagram_username
   PASSWORD=your_instagram_password
   ```

4. Modify the `post.json` file with the details of your media posts:

   ```json
   [
     {
       "type": "image",
       "file_path": "./posts/02.png",
       "caption": "Time files fast! #memes"
     },
     {
       "type": "image",
       "file_path": "./posts/03.png",
       "caption": "I want to sleep! #memes"
     }
   ]
   ```

5. Run the script:

   ```bash
   python InstagramPoster.py
   ```

The script will log in to your Instagram account, upload the specified media files, and post them at random intervals.

## Disclaimer

This script should be used responsibly and in compliance with Instagram's terms of service. Excessive automation may lead to account suspension.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
