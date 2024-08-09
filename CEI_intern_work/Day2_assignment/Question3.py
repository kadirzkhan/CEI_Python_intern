''' Write a Python program that reads a JSON file containing NASA APOD data and prints the keys: "explanation","Title"
Use this link to copy your json data (do not use request module, just save the Json to a variable then do json operation) 
JSON Data url: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'''

import json

# Example JSON data saved to a variable
nasa_apod_data = {
    "date": "2023-08-06",
    "explanation": "This is an example explanation of the NASA Astronomy Picture of the Day.",
    "media_type": "image",
    "service_version": "v1",
    "title": "Astronomy Picture of the Day",
    "url": "https://example.com/image.jpg"
}

# Convert JSON data to a dictionary (simulating reading from a file)
data = json.loads(json.dumps(nasa_apod_data))

# Print the values for keys "explanation" and "title"
print("Explanation:", data.get("explanation"))
print("Title:", data.get("title"))