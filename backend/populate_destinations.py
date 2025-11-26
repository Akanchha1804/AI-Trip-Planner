import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trip_planner.settings')
django.setup()

from trips.models import Destination

destinations = [
    {
        "name": "Kyoto",
        "country": "Japan",
        "region": "asia",
        "trip_types": "cultural,relaxation,romantic",
        "activities": "historical tours,nature,food",
        "description": "Experience the timeless beauty of ancient temples, traditional tea ceremonies, and stunning cherry blossoms in Japan's cultural capital.",
        "image_url": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "March-May, October-November",
        "average_cost": "$$$"
    },
    {
        "name": "Santorini",
        "country": "Greece",
        "region": "europe",
        "trip_types": "romantic,luxury,relaxation",
        "activities": "beaches,food,nightlife",
        "description": "Famous for its stunning sunsets, white-washed buildings, and crystal-clear waters. The perfect romantic getaway.",
        "image_url": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "May-October",
        "average_cost": "$$$$"
    },
    {
        "name": "Machu Picchu",
        "country": "Peru",
        "region": "south_america",
        "trip_types": "adventure,cultural,historical",
        "activities": "hiking,historical tours,nature",
        "description": "Explore the lost city of the Incas, high in the Andes Mountains. A bucket-list destination for history buffs and hikers.",
        "image_url": "https://images.unsplash.com/photo-1587595431973-160d0d94add1?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "April-October",
        "average_cost": "$$"
    },
    {
        "name": "Bali",
        "country": "Indonesia",
        "region": "asia",
        "trip_types": "relaxation,adventure,budget",
        "activities": "beaches,nature,nightlife",
        "description": "A tropical paradise offering lush jungles, beautiful beaches, and a vibrant spiritual culture. Perfect for digital nomads and surfers.",
        "image_url": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "April-October",
        "average_cost": "$"
    },
    {
        "name": "Reykjavik",
        "country": "Iceland",
        "region": "europe",
        "trip_types": "adventure,nature",
        "activities": "hiking,nature,northern lights",
        "description": "Land of fire and ice. Witness the Northern Lights, relax in geothermal lagoons, and explore dramatic landscapes.",
        "image_url": "https://images.unsplash.com/photo-1476610182048-b716b8518aae?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "September-March (Northern Lights)",
        "average_cost": "$$$$"
    },
    {
        "name": "Cape Town",
        "country": "South Africa",
        "region": "africa",
        "trip_types": "adventure,family,cultural",
        "activities": "hiking,beaches,historical tours",
        "description": "Where the mountains meet the sea. Enjoy world-class vineyards, Table Mountain hikes, and rich history.",
        "image_url": "https://images.unsplash.com/photo-1580060839134-75a5edca2e99?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "November-March",
        "average_cost": "$$"
    },
    {
        "name": "New York City",
        "country": "USA",
        "region": "north_america",
        "trip_types": "cultural,luxury,family",
        "activities": "shopping,food,nightlife,historical tours",
        "description": "The city that never sleeps. Iconic landmarks, Broadway shows, and endless dining options await.",
        "image_url": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "April-June, September-November",
        "average_cost": "$$$$"
    },
    {
        "name": "Cairo",
        "country": "Egypt",
        "region": "africa",
        "trip_types": "cultural,historical,budget",
        "activities": "historical tours,museums",
        "description": "Home to the Great Pyramids of Giza and the Sphinx. Dive into thousands of years of history.",
        "image_url": "https://images.unsplash.com/photo-1572252009286-268acec5ca0a?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "October-April",
        "average_cost": "$"
    },
    {
        "name": "Sydney",
        "country": "Australia",
        "region": "oceania",
        "trip_types": "adventure,family,beaches",
        "activities": "beaches,surfing,nightlife",
        "description": "Famous for its Opera House and Harbour Bridge. Enjoy a laid-back lifestyle with stunning coastal views.",
        "image_url": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "December-February",
        "average_cost": "$$$"
    },
    {
        "name": "Dubai",
        "country": "UAE",
        "region": "middle_east",
        "trip_types": "luxury,shopping,modern",
        "activities": "shopping,nightlife,desert safari",
        "description": "A city of superlatives. The tallest building, the biggest mall, and luxury beyond imagination.",
        "image_url": "https://images.unsplash.com/photo-1512453979798-5ea904ac6605?auto=format&fit=crop&w=800&q=80",
        "best_time_to_visit": "November-March",
        "average_cost": "$$$$"
    }
]

for dest_data in destinations:
    Destination.objects.get_or_create(
        name=dest_data['name'],
        defaults=dest_data
    )
    print(f"Added {dest_data['name']}")

print("✅ Database populated successfully!")
