from datetime import datetime
import googlemaps
from twilio.rest import Client


# gmaps documentation https://pypi.org/project/googlemaps/

# this can be scheduled using a cronjob (crontab -e) for example 12 am every day would be 0 12 * * * /path/to/script.py

now = datetime.now()

def get_commute_duration():
  home_addy = "your address"
  beach_addy = "26th avenue beach santa cruz ca"

  gmaps_api_key = "Key"

  gmaps = googlemaps.Client(key = gmaps_api_key)
  directions = gmaps.directions(home_addy, beach_addy, departure_time = now)


  first_leg = directions[0]['legs'][0] # accesses the first portion of the journy


  duration = first_leg['duration']['text'] # Extract the duration text of the first leg

  return duration

def send_text(message):
  twilio_sid = "sid"
  twilio_token = "token"
  twilio_num = "num"
  receiving_num = "num"

  client = Client(twilio_sid, twilio_token)

  client.message.create(
      to = receiving_num,
      from_ = twilio_num,
      body = message
  )

def main():
  commute_duration = get_commute_duration()

  now = datetime.now()

  arrival_time = now + duration

  message = (
      f"heyo, the commute to surf today will be"{commute_duration}
  )

  send_text(message)


if __name__ == "__main__":
  main()