# 🥟 HoloList to JSON & iCalendar

> Dump hololive, HOLOSTARS, & NIJISANJI Project Birthdays from [HoloList](https://hololist.net) to JSON & iCalendar

## Install iCalendar

To install the *latest* iCalendar containing all hololive and HOLOSTARS birthdays, download and open [`latest_hololive.ics`](https://raw.githubusercontent.com/Fuwn/hololist-to-json/refs/heads/main/latest_hololive.ics); for NIJISANJI Project birthdays, download and open [`latest_nijisanji.ics`](https://raw.githubusercontent.com/Fuwn/hololist-to-json/refs/heads/main/latest_nijisanji.ics).

## Latest Data

A JSON file containing the *latest* hololive birthday data is present in the [`latest_hololive.json`](https://raw.githubusercontent.com/Fuwn/hololist-to-json/refs/heads/main/latest_hololive.json)
file; [`latest_nijisanji.json`](https://raw.githubusercontent.com/Fuwn/hololist-to-json/refs/heads/main/latest_nijisanji.json)
contains the *latest* NIJISANJI Project data.

An ICS file containing the *latest* hololive birthday iCalendar is present in the [`latest_hololive.ics`](https://raw.githubusercontent.com/Fuwn/hololist-to-json/refs/heads/main/latest_hololive.ics) file; the *latest* NIJISANJI
Project iCalendar is contained in [`latest_nijisanji.ics`](https://raw.githubusercontent.com/Fuwn/hololist-to-json/refs/heads/main/latest_nijisanji.ics).

You can generate all of these files locally using the [`generate_latest`](./generate_latest) Bash script.

## Sample JSON Data

```json
[
  {
    "month": 1,
    "day": 12,
    "name": "Usada Pekora",
    "pictureURL": "https://hololist.net/wp-content/uploads/2022/02/usada-pekora-portrait-66-300x300.jpg",
    "profileURL": "https://hololist.net/usada-pekora/"
  },
  {
    "month": 12,
    "day": 12,
    "name": "Kobo Kanaeru",
    "pictureURL": "https://hololist.net/wp-content/uploads/2022/03/kobo-kanaeru-portrait-66-300x300.jpg",
    "profileURL": "https://hololist.net/kobo-kanaeru/"
  }
]
```

## License

This project is licensed under the terms of the [GNU General Public License v3.0 license](./LICENSE.txt).
