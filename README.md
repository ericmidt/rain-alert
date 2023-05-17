# Personal rain alert project
This script gets weather information from openweathermap's API, checks if it's going
to rain in the next 12 hours at a specific latitude and longitude, 
and then uses Telegram's API to send a message from a bot to a user.
The environment variables are loaded by the dotenv module from a local .env file.
