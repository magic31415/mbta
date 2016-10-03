trains=python mbta.py

curl -X POST 'https://api.twilio.com/2010-04-01/Accounts/API_KEY/Messages.json' \
--data-urlencode 'To=YOUR_PHONE'  \
--data-urlencode 'From=TWILIO_PHONE'  \
--data-urlencode "Body=Trains: $trains"  \
-u API_KEY:API_KEY_PASSWORD
