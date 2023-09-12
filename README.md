# Rain-alert

Rain alert app 

Uses [Open Weather API](https://api.openweathermap.org) to fetch data, checks the day's weather and sends sms by using [Twilio](https://www.twilio.com/en-us) if umbrella is needed.


Needed info for .env file:
  
  ```WEATHER_API_KEY``` - Open Weather API key
  
  ```LATITUDE``` - latitude info
  
  ```LONGITUDE``` - longitude info
  
  ```TWILIO_ACCOUNT_SID``` - twilio account sid
  
  ```TWILIO_AUTH_TOKEN``` - twilio auth token
  
  ```FROM_NUMBER``` - twilio phone number
  
  ```TO_NUMBER``` - phone number of recipient
