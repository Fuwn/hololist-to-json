import json
from datetime import datetime
import icalendar
import sys

profile = sys.argv[1] if len(sys.argv) > 1 else "hololive"

with open(f"./{profile}_birthdays.json", "r", encoding="utf-8") as file:
    birthdays = json.load(file)

calendar = icalendar.Calendar()
title = "hololive & HOLOSTARS" if profile == "hololive" else "NIJISANJI Project"

calendar.add("prodid", f"-//Fuwn//{title} Birthday Calendar//EN")
calendar.add("version", "2.0")
calendar.add("calscale", "GREGORIAN")
calendar.add("method", "PUBLISH")
calendar.add("x-wr-calname", f"{title} Birthdays")
calendar.add("x-wr-timezone", "Asia/Tokyo")
calendar.add("x-wr-caldesc", "https://github.com/Fuwn/hololist-to-json-and-ical")

# Hakos Baelz gets skipped if it's not a leap year.
current_year = 2024

for birthday in birthdays:
    try:
        event_date = datetime(current_year, birthday["month"], birthday["day"])
        event = icalendar.Event()

        event.add("summary", f"{birthday['name']}'s Birthday")
        event.add(
            "description",
            f"HoloList Profile: {birthday['profileURL']}",
        )
        event.add("dtstart", event_date.date())
        event.add("dtend", event_date.date())
        event.add("dtstamp", datetime.now())
        event.add("rrule", {"freq": "yearly"})
        event.add(
            "uid",
            f"{birthday['name'].replace(' ', '_').lower()}_{birthday['month']}{birthday['day']}@{'hololivepro.com' if profile == 'hololive' else 'nijisanji.jp'}",
        )
        calendar.add_component(event)
    except ValueError as e:
        print(e)

with open(f"{profile}_birthdays.ics", "wb") as ics_file:
    ics_file.write(calendar.to_ical())
