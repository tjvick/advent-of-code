import time
from datetime import datetime
import math
import requests

# owner_id = "115313"
owner_id = "405974"

with open('session_id', 'r') as f:
    session_id = f.read()

response = requests.get(
    url=f"https://adventofcode.com/2021/leaderboard/private/view/{owner_id}.json",
    headers={
        "Cookie": f"session={session_id}"
    }
)
print(response.status_code)

data = response.json()

star_info = {}
score_info = {}
names = {}
finish_times = {}

for member_id, member_data in data['members'].items():
    if member_data['stars'] > 0:
        names[member_id] = member_data['name']
        star_info[member_id] = member_data['stars']
        score_info[member_id] = member_data['local_score']

        for day, day_data in member_data['completion_day_level'].items():
            if day not in finish_times:
                finish_times[day] = {}
            for part, time_data in day_data.items():
                if part not in finish_times[day]:
                    finish_times[day][part] = {}
                finish_times[day][part][member_id] = time_data['get_star_ts']


# Anonymous Paul
names['673102'] = 'Paul'
names['403635'] = 'Unknown'

longest_name_length = max([len(name) for name in names.values()])
def print_name(member_id):
    return f'{names[member_id]}{" "*(longest_name_length-len(names[member_id]))}'


print("Stars:")
sorted_star_info = dict(sorted(star_info.items(), key=lambda item: item[1], reverse=True))
for member_id, n_stars in sorted_star_info.items():
    print(f'  {print_name(member_id)}: {n_stars}')

print("\n**********\n")
print("Scores:")
sorted_score_info = dict(sorted(score_info.items(), key=lambda item: item[1], reverse=True))
for member_id, score in sorted_score_info.items():
    print(f'  {print_name(member_id)} : {score}')


print("Times:")
finish_times_sorted_by_day = dict(sorted(finish_times.items(), key=lambda item: int(item[0])))
for day, day_data in finish_times_sorted_by_day.items():
    day_data_sorted_by_part = dict(sorted(day_data.items(), key=lambda item: item[0]))
    print(f'  Day {day}:')
    for part, part_data in day_data_sorted_by_part.items():
        part_data_sorted_by_time = dict(sorted(part_data.items(), key=lambda item: item[1]))
        print(f'    Part {part}:')
        previous_finish_time = int(list(part_data_sorted_by_time.items())[0][1])
        for member_id, finish_time in part_data_sorted_by_time.items():
            finish_timestamp = int(finish_time)
            diff = finish_timestamp - previous_finish_time
            previous_finish_time = finish_timestamp

            finish_time_string = str(datetime.fromtimestamp(finish_timestamp))[11:]
            print_record = f'      {print_name(member_id)}: {finish_time_string}'

            if diff > 0:
                diff_string = time.strftime("%H:%M:%S", time.gmtime(diff))
                print_record += f' (+{diff_string})'

            if diff > 60 * 60 * 24:
                print_record += f' +{math.floor(diff / (60 * 60 * 24))}d'

            print(print_record)
