import requests

# Define API URL
API_URL = 'https://apiip.net/api/check?accessKey={YOUR_API_KEY}'

# Enter the ip for search
IP_FOR_SEARCH = '&ip=67.250.186.196'

# Getting in response JSON
res = requests.get(API_URL+IP_FOR_SEARCH)

# Loading JSON from text to object
json_response = res.json()

# Print the results
print(json_response)
