# Rain_Alert_Script

This Python script checks the weather forecast for the next 12 hours using the OpenWeatherMap API. If rain is expected, it sends an SMS alert using Twilio's messaging service.

## Prerequisites

1. **Python 3.6+**: Ensure Python is installed on your machine.
2. **Requests Library**: Used to make HTTP requests to the OpenWeatherMap API.
   ```bash
   pip install requests
   ```
3. **Twilio Library**: Used to send SMS alerts.
   ```bash
   pip install twilio
   ```
4. **OpenWeatherMap API Key**: Create an account on [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
5. **Twilio Account**: Set up a Twilio account and get your Account SID, Auth Token, and a Twilio phone number to send SMS messages.

## Setup

1. Clone this repository or download the script.
2. Create a file named `main.py` and add the provided script.
3. Replace the following placeholders with your actual values:
   - `api_key`: OpenWeatherMap API key.
   - `account_sid`: Twilio Account SID.
   - `auth_token`: Twilio Auth Token.
   - `from_`: Twilio phone number.
   - `to`: Your personal phone number.

## Configuration

The script checks for rain in the specified location within the next 12 hours. You can update the `MY_LAT` and `MY_LONG` variables with the latitude and longitude of your desired location.

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. If rain is forecasted within the next 12 hours, you'll receive an SMS alert.

## Example

```plaintext
Rain expected in the next 12 hours—grab your umbrella! ☔️ Stay dry!
```
![app](https://github.com/user-attachments/assets/9259552c-10ac-490b-b1b0-29dbac952298)


## Code Overview

- **Requests API call**: Fetches weather data for the next 12 hours.
- **Twilio client**: Sends an SMS alert if rain is expected.

## Notes

- **Weather Forecast Frequency**: The script is set to retrieve the next 4 data points (12-hour forecast in 3-hour increments).
- **SMS Message Status**: The script prints the message status to confirm successful delivery.

---

Feel free to modify and expand this script for more features.
