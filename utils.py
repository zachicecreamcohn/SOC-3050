

from typing import Tuple
import math

# Define a custom type for coordinates
Coordinate = Tuple[float, float]

def haversine(coord1: Coordinate, coord2: Coordinate) -> float:
    """Calculate the great-circle distance between two points on the Earth's surface given in feet."""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371  # Earth radius in kilometers

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_km = R * c  # Distance in kilometers
    distance_feet = distance_km * 3280.84  # Convert kilometers to feet

    return distance_feet

