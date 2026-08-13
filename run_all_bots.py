import os
import sys
import time
import subprocess
import logging
from sync_posts import update_bot_json

VENV_PYTHON = "/home/wil/Documents/Jobs/personal projects/waifu-bot-env/bin/python"

# Set up logging so you can track batch progress in terminal or a log file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("bot_runner.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

# Configuration for sequential execution
BOT_PIPELINES = [
    {
        "name": "Alien Romance Bot",
        "slug": "alien-romance",
        "script": "/home/wil/Documents/Jobs/personal projects/alienromancebot/ThisAlienRomanceBot/alien_romance_bot.py" # Update with your actual script paths
    },
    {
        "name": "Waifu Bot",
        "slug": "waifu",
        "script": "/home/wil/Documents/Jobs/personal projects/waifubot/waifu_bot_envtoken.py"
    },
    {
        "name": "Cat Bot",
        "slug": "cat",
        "script": "/home/wil/Documents/Jobs/personal projects/catbot/Cat_DNE_Bot/cat_bot_envtoken.py"
    }
]

# Pause between runs to allow GPU cool-down and OS memory cleanup
COOL_DOWN_SECONDS = 10 

def run_all_sequentially():
    logging.info("Starting batch execution of all bot pipelines...")

    for bot in BOT_PIPELINES:
        bot_name = bot["name"]
        script_path = bot["script"]
        bot_slug = bot["slug"]

        if not os.path.exists(script_path):
            logging.error(f"Script file for '{bot_name}' not found at: {script_path}. Skipping.")
            continue

        logging.info(f"==========================================")
        logging.info(f" Launching: {bot_name}")
        logging.info(f"==========================================")

        try:
            # Run the bot in its own isolated process
            result = subprocess.run(
                [VENV_PYTHON, script_path],
                check=True,
                text=True
            )
            logging.info(f"Successfully completed generation/posting for '{bot_name}'.")

            # Instantly update public/posts.json for this specific bot
            logging.info(f"Syncing Facebook posts for '{bot_slug}'...")
            update_bot_json(target_slug=bot_slug)

        except subprocess.CalledProcessError as e:
            logging.error(f"'{bot_name}' failed with exit code {e.returncode}. Moving to next task.")
        except Exception as e:
            logging.error(f"Unexpected error running '{bot_name}': {e}")

        logging.info(f"Waiting {COOL_DOWN_SECONDS} seconds for resources to settle...")
        time.sleep(COOL_DOWN_SECONDS)

if __name__ == "__main__":
    run_all_sequentially()