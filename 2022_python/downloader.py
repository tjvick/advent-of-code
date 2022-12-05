import os
from datetime import datetime
from pathlib import Path
from time import sleep

import requests
from dotenv import load_dotenv

load_dotenv()
cookie = os.getenv('COOKIE')

YEAR = 2022
DAY_TO_DOWNLOAD = 5


def wait_until_time(day: int):
    target_time = datetime(
        year=YEAR,
        month=12,
        day=day,
        hour=0,
        minute=0
    )

    while datetime.now() < target_time:
        time_remaining = target_time - datetime.now()
        print("Time remaining: ", time_remaining)
        sleep(1)

    return


def request_input_file(day):
    return requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input",
        headers={
            "Cookie": cookie
        }
    )


def wait_and_get_input(day: int) -> str:
    wait_until_time(day)

    response = request_input_file(day)

    if "Please don't repeatedly request this endpoint" not in response.text:
        return response.text

    print("Woops! Reprimanded!")
    sleep(1)
    return wait_and_get_input(day)


def write_input_file(day: int, file_text: str):
    folder = f"solutions/day{day:02d}"
    file = Path(folder) / "input"
    file.write_text(file_text)


input_file_text = wait_and_get_input(day=DAY_TO_DOWNLOAD)
write_input_file(day=DAY_TO_DOWNLOAD, file_text=input_file_text)

