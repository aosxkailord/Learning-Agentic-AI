# 🎲✨ Game Tools Module by Kashan Malik ✨🎲
# -------------------------------------------------
# Welcome, adventurer! This module is packed with fun, easy-to-use tools
# to spice up your game sessions. Roll dice, trigger random events, and
# let the adventure unfold! 🚀

from agents import function_tool
import random

@function_tool
def roll_dice() -> int:
    """
    🎲 Roll the Dice!
    -----------------
    Simulates rolling a classic six-sided dice. Perfect for games of chance,
    decision-making, or just adding a bit of suspense!

    Returns:
        int: A random number between 1 and 6 (inclusive).
    
    Example:
        >>> roll_dice()
        4
    """
    return random.randint(1, 6)

@function_tool
def generate_event() -> str:
    """
    🌟 Generate a Random Game Event!
    -------------------------------
    Unleash the unexpected! This function picks a surprise event to keep
    your players on their toes. Great for storytelling and improvisation.

    Returns:
        str: A vivid description of a random game event.
    
    Example:
        >>> generate_event()
        'You found a hidden treasure!'
    """
    events = [
        "🪙 You found a hidden treasure!",
        "👾 A wild monster appears!",
        "🕵️‍♂️ You encountered a mysterious stranger.",
        "🏺 You discovered an ancient artifact.",
        "🌩️ A storm is brewing in the distance."
    ]
    return random.choice(events)
