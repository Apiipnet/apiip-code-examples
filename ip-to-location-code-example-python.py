import json
import urllib.request

# Define API URL
API_URL = 'https://apiip.net/api/check?accessKey={YOUR_API_KEY}'

# Enter the ip for search
IP_FOR_SEARCH = '&ip=67.250.186.196'

# Creating request object to API
req = urllib.request.Request(API_URL+IP_FOR_SEARCH)

# Getting in response JSON
response = urllib.request.urlopen(req).read()

# Loading JSON from text to object
json_response = json.loads(response.decode('utf-8'))

# Print the results
print(json_response)