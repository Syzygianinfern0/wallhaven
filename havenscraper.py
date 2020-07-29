from wallhaven import Wallhaven

wallhaven = Wallhaven("Uu9ZXRqp59DmD5b2xb74tI2K01lKnYkO")

# Get the user's public collection
data = wallhaven.get_collection_from_username(username="RaidyHD")
print(data)
