import random

def get_location():
    locations = [
        "Barcelona", "Rosario"
    ]

    pickup_position = random.randint(0,len(locations)-1)
    return locations[pickup_position]

