import random
import time
import sys

def colored(text, color_code):
    return f"\x1b[{color_code}m{text}\x1b[0m"

RARITIES = [
    ("COMMON", "37"),     # White
    ("RARE", "36"),       # Cyan
    ("EPIC", "35"),       # Purple
    ("LEGENDARY", "33;1") # Bold Gold
]

ASCII_PETS = {
    "Omni-Cat": (r"""
   /\___/\
  ( o   o )
  (  =^=  )
  (        )
  (         )
  (          )))))))))))
""", "Curious & Resourceful"),
    
    "Cyber-Owl": (r"""
   , _ ,
  ( o o )
 /'  M  `\
|___|_|___|
""", "Observant & Silent"),

    "Gacha-Dragon": (r"""
    \||/
    |  @___oo
  /\  /\   / (__,,,,|
 ) /^\) ^\/ _/
 )   _ /  / _/
 \___\(__/
""", "Aggressive Code Eater")
}

def roll_gacha():
    roll = random.random()
    if roll < 0.05: return RARITIES[3]
    elif roll < 0.20: return RARITIES[2]
    elif roll < 0.50: return RARITIES[1]
    return RARITIES[0]

def summon_buddy():
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except: pass
    
    print("\n" + colored("[SYS] Initializing /buddy sequence...", "90"))
    
    species_name, (art, trait) = random.choice(list(ASCII_PETS.items()))
    rarity_name, color = roll_gacha()
    
    print(colored("✦ SPAWNING OMNICLAW COMPANION ✦\n", "36;1"))
    
    # Draw pet
    for line in art.strip('\n').split('\n'):
        print("    " + colored(line, color))
        time.sleep(0.1)
        
    print("\n" + colored("═"*35, "90"))
    print(colored("  Name    : ", "90") + colored(f"Unregistered {species_name}", color))
    print(colored("  Rarity  : ", "90") + colored(f"[{rarity_name}]", color))
    print(colored("  Nature  : ", "90") + colored(trait, "32"))
    print(colored("═"*35, "90"))
    
    energy = random.randint(30, 100)
    mood = "Happy" if energy > 60 else "Hungry for Repos"
    
    stats = f"""
  [🔋] Shell Energy : {colored(f"{energy}%", "32" if energy > 60 else "31")}
  [🧠] AI Cooldown  : {random.randint(2, 12)} ms
  [❤️] Pet Mood     : {mood}
"""
    print(stats)
    print(colored(f"  >> {species_name} is watching you compile code...", "3m"))
    print("\n")

if __name__ == "__main__":
    summon_buddy()
