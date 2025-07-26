"""
travel_tools.py ✈️🏨
--------------------
Travel Tools Module by Kashan Malik

This module provides handy tools for fetching flight and hotel information.
Perfect for building travel planning agents and applications!

Author: Kashan Malik
"""

from agents import function_tool

@function_tool
def get_flight_info(
    origin: str,
    destination: str,
    departure_date: str,
    return_date: str = None
) -> str:
    """
    ✈️ Get Flight Information

    Fetches available flight details between two locations for specified dates.

    Args:
        origin (str): 🏙️ The city or airport you're flying from.
        destination (str): 🌆 The city or airport you're flying to.
        departure_date (str): 📅 Departure date (YYYY-MM-DD).
        return_date (str, optional): 📅 Return date (YYYY-MM-DD), if it's a round trip.

    Returns:
        str: 📝 A friendly summary of available flights.

    Example:
        get_flight_info("New York", "London", "2024-07-01", "2024-07-10")
    """
    # 🚧 TODO: Integrate with real flight APIs for live data!
    summary = f"✈️ Flight info from {origin} to {destination} on {departure_date}"
    if return_date:
        summary += f" and returning on {return_date}"
    summary += ".\n\nSafe travels! 🌍"
    return summary

@function_tool
def get_hotel_info(
    location: str,
    check_in_date: str,
    check_out_date: str
) -> str:
    """
    🏨 Get Hotel Information

    Finds hotel options for your stay in a given location and dates.

    Args:
        location (str): 📍 The city or area for your hotel.
        check_in_date (str): 🛎️ Check-in date (YYYY-MM-DD).
        check_out_date (str): 🛏️ Check-out date (YYYY-MM-DD).

    Returns:
        str: 📝 A friendly summary of available hotels.

    Example:
        get_hotel_info("Paris", "2024-08-01", "2024-08-05")
    """
    # 🚧 TODO: Connect to hotel booking APIs for real-time availability!
    summary = (
        f"🏨 Hotel info for {location} from {check_in_date} to {check_out_date}."
        "\n\nEnjoy your stay! 🌟"
    )
    return summary

# Made with ❤️ by Kashan Malik