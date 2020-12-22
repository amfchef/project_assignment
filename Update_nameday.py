import requests


class Update_nameday:
    def update_nameday(self):
        URL = 'https://sholiday.faboul.se/dagar/v2.1/'
        from datetime import datetime
        now = datetime.now()
        r = requests.get(URL)
        text = r.text
        json_text_from_URL = r.json()

        days_dict = json_text_from_URL['dagar']
        day = days_dict[0]
        todays_date = "Today's date is: " + str(day['datum'])
        nameday = "Today's nameday is: " + str(day['namnsdag'])
        date_and_nameday = todays_date + "\n" + nameday
        return date_and_nameday

