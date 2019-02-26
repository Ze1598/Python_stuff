'''
Use the OpenWeatherMap website, more specifically, its Current weather
data API.

In this script, we'll only search for the weather of cities using the city name.
'''

import requests

def get_weather(city_name, api_key, units):
	'''
	Get the current weather status for a given city.
	
	Parameters
	----------
	city_name : str
		The city whose weather is going to be searched.
	api_key : str
		The API key for authentication.
	units : str
		The unit system to use for the weather search
	(imperial or metric).

	Returns
	-------
	tuple
		A two-item tuple, where the first item is the weather
	status and the second is the temperature, in the specified
	unit.
	'''

	# Make the request to the API
	req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={api_key}&units={units}")

	# Convert the response into a JSON object
	json_resp = req.json()

	# Return the current weather 
	return (json_resp["weather"][0]["main"], json_resp["main"]["temp"])



if __name__ == "__main__":

	# Prompt the user for a city to search
	search_city = input("Which do city do you want to know the weather of: ").capitalize()

	# Prompt the user for the unit system to use in the search
	search_units = input("Do you want imperial or metric units: ").lower()
	# Default the search units to imperial in case the user didn't input a valid value
	search_units = search_units if ( (search_units == "imperial") or (search_units == "metric") ) else "imperial"

	# Get the API key from a .txt file in the same directory as this scrip
	with open("OpenWeatherMap.txt") as f:
		api_key = f.readlines()[1]

	# Search the weather using the created function
	search_weather = get_weather(search_city, api_key, search_units)

	# Use a simple conditional to adapt the temperature portion to the unit system the\
	# user chose
	if search_units == "imperial":
		print(f"The weather for {search_city} is {search_weather[0].lower()}, with a temperature of {search_weather[1]} degrees Fahrenheit.")
	elif search_units == "metric":
		print(f"The weather for {search_city} is {search_weather[0].lower()}, with a temperature of {search_weather[1]} degrees Celsius.")

# Sample JSON object for the city Porto (using imperial units; default):
'''
{
	'coord': {
		'lon': -8.61, 
		'lat': 41.15
	}, 
	'weather': [{
		'id': 800, 
		'main': 'Clear', 
		'description': 'clear sky', 
		'icon': '01d'
	}], 
	'base': 'stations', 
	'main': {
		'temp': 286.67, 
		'pressure': 1019,
		'humidity': 76,
		'temp_min': 286.15,
		'temp_max': 287.15
	}, 
	'visibility': 10000, 
	'wind': {
		'speed': 3.1, 
		'deg': 220
	}, 
	'clouds': {'all': 0}, 
	'dt': 1547564400, 
	'sys': {
		'type': 1,
		'id': 6900,
		'message': 0.0021,
		'country': 'PT',
		'sunrise': 1547539046,
		'sunset': 1547573451
	}, 
	'id': 2735943, 
	'name': 'Porto', 
	'cod': 200
}
'''


# Sample JSON object for the city Porto (using metric units):
'''
{
	'coord': {'lon': -8.61, 'lat': 41.15}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 13.58, 'pressure': 1019, 'humidity': 71, 'temp_min': 13, 'temp_max': 14}, 'visibility': 10000, 'wind': {'speed': 3.1, 'deg': 220}, 'clouds': {'all': 0}, 'dt': 1547566200, 'sys': {'type': 1, 'id': 6900, 'message': 0.0364, 'country': 'PT', 'sunrise': 1547539046, 'sunset': 1547573452}, 'id': 2735943, 'name': 'Porto', 'cod': 200
}
'''