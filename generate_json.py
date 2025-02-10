import requests
import bs4
import json
import sys

profile = sys.argv[1] if len(sys.argv) > 1 else "hololive"
response = requests.get(f"https://hololist.net/{profile}-birthdays/")

response.raise_for_status()

birthdays = []

for month_div in bs4.BeautifulSoup(response.text, "html.parser").find_all(
    "div", {"label": "month"}
):
    month = int(month_div["id"])

    for row in month_div.find_all("div", class_="row"):
        for entry in row.find_all("div", class_="col-12"):
            # Day
            day_tag = entry.find("h3", class_="fs-6")
            day = int(day_tag.text.split()[-1]) if day_tag else None

            # Name and profile URL
            profile_tag = entry.find("a", class_="line-truncate")
            name = profile_tag.text.strip() if profile_tag else None
            profile_url = profile_tag["href"] if profile_tag else None

            # Picture URL
            img_tag = entry.find("img", class_="lazy-image")
            picture_url = (
                img_tag["data-src"] if img_tag and "data-src" in img_tag.attrs else None
            )

            if day and name and profile_url and picture_url:
                birthdays.append(
                    {
                        "month": month,
                        "day": day,
                        "name": name,
                        "pictureURL": picture_url,
                        "profileURL": profile_url,
                    }
                )

with open(f"{profile}_birthdays.json", "w", encoding="utf-8") as json_file:
    json.dump(birthdays, json_file, ensure_ascii=False, indent=4)
