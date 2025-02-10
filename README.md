# 🥟 HoloList to JSON & iCalendar

> Dump hololive & HOLOSTARS Birthdays from [HoloList](https://hololist.net) to JSON & iCalendar

## Latest Data

A JSON file containing the *latest* HoloList data is present in the [`latest.json`](https://raw.githubusercontent.com/Fuwn/hololist-to-json/refs/heads/main/latest.json)
file.

An ICS file containing the *latest* HoloList iCalendar is present in the [`latest.ics`](https://raw.githubusercontent.com/Fuwn/hololist-to-json/refs/heads/main/latest.ics) file.

You can generate both of these files locally using the [`generate_latest`](./generate_latest) Bash script.

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
