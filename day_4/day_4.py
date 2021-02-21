with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# Part 1 - I may have overcomplicated this!
import re
from datetime import datetime


def get_time_and_message(info):
    m = re.match(r"\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\]\s(.+)", info)
    if m is None:
        print(info)
    return datetime.strptime(m.groups()[0], "%Y-%m-%d %H:%M"), m.groups()[1]


def get_guard(info):
    m = re.match(r".+#(\d+)\s", info)
    if m:
        return int(m.groups()[0])
    else:
        return None


data = []

for d in PUZZLE_INPUT.splitlines():
    data.append(get_time_and_message(d))

# Sort the data
data.sort(key=lambda x: x[0])

current_guard = None
sleep_records = {}
guard_records = {}

guards = {}
asleep = False
asleep_since = 0

for d, m in data:
    # First message is guard and indicates a new night
    guard = get_guard(m)
    if guard:
        current_guard = guard
        if current_guard not in guards:
            guards[current_guard] = []
    else:
        # Must be an action
        asleep = not asleep
        t = datetime(d.year, d.month, d.day)

        if not asleep:
            # Woken up
            guards[current_guard].extend([i for i in range(asleep_since, d.minute)])
        else:
            asleep_since = d.minute

        if t not in guard_records:
            guard_records[t] = current_guard

        if t in sleep_records:
            sleep_records[t].append(d.minute)
        else:
            sleep_records[t] = [d.minute]


def print_schedule(sleeps, guards):
    for k, v in sleep_records.items():
        line = "{}-{} #{} ".format(k.month, k.day, guard_records[k])
        asleep = False
        for m in range(60):
            if m in v:
                asleep = not asleep
            if asleep:
                line += "#"
            else:
                line += "."
        print(line)


print_schedule(sleep_records, guard_records)

most_sleeps = 0
most_slept = None

for k, v in guards.items():
    if len(v) > most_sleeps:
        most_sleeps = len(v)
        most_slept = k

# Find most slept minute
unique_minutes = set(guards[most_slept])

most_common = 0
how_many = 0

for m in unique_minutes:
    if guards[most_slept].count(m) > how_many:
        most_common = m
        how_many = guards[most_slept].count(m)

print(
    "Most slept is {} with {}. Most common minute is {}".format(
        most_slept, most_sleeps, most_common
    )
)

# 19830
print(f"Part 1: {most_common * most_slept}")

# Part 2
most_common = 0
how_many = 0
which_guard = 0

for k, v in guards.items():
    unique_minutes = set(v)
    for m in unique_minutes:
        if v.count(m) > how_many:
            most_common = m
            how_many = v.count(m)
            which_guard = k

# 43695
print(
    "Most asleep on the same minute was {} at {} = {}".format(
        which_guard, most_common, which_guard * most_common
    )
)
