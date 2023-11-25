import requests

# Cat as a service (https://cataas.com/)
# normal:
# req = requests.get("https://cataas.com/cat")

# Square:
req = requests.get("https://cataas.com/cat?type=square")

# Save image
with open("cats/cat.jpg", "wb") as handler:
    print("Downloading your new cat image!")
    handler.write(req.content)
