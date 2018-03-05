import requests
import time
import json

# Prints JSON with pizzazz
def pretty_print(string):
    parsed = json.loads(string)
    return json.dumps(parsed, indent=4, sort_keys=True)

# URL for REST API
space_url = 'http://api.open-notify.org/iss-pass.json'

# Parameters for the body of the REST API call
params = {'lat' : 25.717396, 'lon':-80.278130}

response = requests.get(space_url, params)

print("Status Code:", response.status_code)

if response.ok:
    # Make that content pretty!
    print("Content:", pretty_print(response.content))

    # Get date of next time we will see the ISS
    parsed = json.loads(response.content)

    if type(parsed) is dict and 'response' in parsed:
        # Since we get back multiple times when the ISS will be overhead,
        # we only want the first one
        next_rise_time = parsed['response'][0]['risetime']
        
        # Converts Unix Time to readable date. Another module!
        date_of_risetime = time.ctime(int(next_rise_time))
        print("Next time we will see the ISS is", date_of_risetime)
else:
    print("ERROR: Bad response code. Exiting")
