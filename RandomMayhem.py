#  zzzzzzzzzzzzzzzzzzzzzzzzzzzz MAYHAM RUMBLE zzzzzzzzzzzzzzzzzzzzzzzzzzzz
# Developed by ZachShack
# 04-14-22

import random

hunter = {
    "Solar": ["Golden Gun - Deadshot", "Golden Gun - Marksman", "Blade Barrage"],
    "Void": ["Shadowshot - Deadfall", "Shadowshot - Mobius Quiver", "Spectral Blades"],
    "Arc": ["Arc Staff", "Gathering Storm", "Storms Edge"],
    "Stasis": ["Revenant"],
    "Strand": ["Silkstrike"]
}

titan = {
    "Solar": ["Hammer of Sol", "Burning Maul"],
    "Void": ["Sentinel Shield", "Ward of Dawn", "Twilight Arsenal"],
    "Arc": ["Fists of Havoc", "ThunderCrash"],
    "Stasis": ["Glacial Quake"],
    "Strand": ["Blade Fury"]
}

warlock = {
    "Solar": ["Dawnblade", "Well of Radiance", "Song of Flame"],
    "Void": ["Nova bomb - Cataclysm", "Nova bomb - Vortex", "Nova Warp"],
    "Arc": ["Stormtrance", "ChaosReach"],
    "Stasis": ["Winter's Wrath"],
    "Strand": ["Needlestorm"]
}

# Randomize Functions to return subclass and super for the player
def randomHunter():
    subclass = random.choice(list(hunter.keys()))
    return subclass, random.choice(hunter[subclass])

def randomTitan():
    subclass = random.choice(list(titan.keys()))
    return subclass, random.choice(titan[subclass])

def randomWarlock():
    subclass = random.choice(list(warlock.keys()))
    return subclass, random.choice(warlock[subclass])

# Try block to import colorama from console (also imports os)
try:
    from colorama import Fore, Style
except ImportError:
    import os
    os.system("pip install colorama")
    from colorama import Fore, Style

color_map = {
    "Solar": Fore.RED,
    "Void": Fore.MAGENTA,
    "Arc": Fore.CYAN,
    "Stasis": Fore.BLUE,
    "Strand": Fore.GREEN
}

while True:
    guardian = input('Are you a  Hunter, Titan, Warlock :').strip().lower()

    if guardian == "hunter":
        subclass, super = randomHunter()
    elif guardian == "titan": 
        subclass, super = randomTitan()
    elif guardian == "warlock":   
        subclass, super = randomWarlock()
    elif guardian == "x":
        break # Exits loop when user types "x"
    else:
        print("Uninstalling Windows 32... ")
        continue # Restart loop for a valid input

    print(f"{color_map[subclass]}Super: {subclass} | {super}{Style.RESET_ALL}")


