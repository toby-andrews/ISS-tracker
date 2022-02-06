import time

import requests
from datetime import datetime
import smtplib

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
# print(data)


MY_LAT = 29.375858
MY_LONG = 47.977406


def iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    # print(data)

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)

    # print(iss_position)

    if MY_LONG - 5 <= longitude <= MY_LONG + 5 and MY_LAT - 5 <= latitude <= MY_LAT + 5:
        return True


def nighttime():
    if sunrise >= hour or hour >= sunset:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])
# print(sunrise)
# print(sunset)

now = datetime.now()
time_now = datetime.now()
hour = time_now.hour


def write_email():
    my_email = "testtesttest@gmail.com"
    password = "testestes"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Look up!\n\nThe station is in the sky!!")


close = iss_nearby()
dark = nighttime()
if close is True and dark is True:
    while True:
        time.sleep(60)
        write_email()
