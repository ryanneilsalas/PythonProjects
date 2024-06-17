import requests
from datetime import datetime

MY_LAT = 10.164238
MY_LONG = 124.862243


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    data = iss_response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if 46 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise_data = response.json()
    sunrise = int(sunrise_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunrise_data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    print("THE ISS IS OVERHEARD!")
else:
    print("THE ISS  IS NOT OVERHEARD :(")