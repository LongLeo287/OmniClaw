import sys
import os
import time

# Inject local path to load omniclawdex
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import omniclawdex

def colored(text, color_code):
    return f"\x1b[{color_code}m{text}\x1b[0m"

def print_stat_card(pid, pet_data, ivs):
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except: pass

    # Calculate final stats
    f_int = omniclawdex.GachaSystem.calculate_final_stat(pet_data['base_stats']['int'], ivs['int_iv'])
    f_spd = omniclawdex.GachaSystem.calculate_final_stat(pet_data['base_stats']['spd'], ivs['spd_iv'])
    f_def = omniclawdex.GachaSystem.calculate_final_stat(pet_data['base_stats']['def'], ivs['def_iv'])

    color = pet_data['color']
    
    print("\n" + colored("[SYS] Accessing OmniClawDex Database...", "90"))
    time.sleep(0.5)
    print(colored(f"✦ WILD COMPANION APPEARED! ✦\n", "35;1"))
    
    art = pet_data['frames']['idle_1']
    for line in art.strip('\n').split('\n'):
        print("    " + colored(line, color))
        time.sleep(0.1)

    print("\n" + colored("╔" + "═"*40 + "╗", "90"))
    print(colored("║ ", "90") + colored(f"ID: {pid} | {pet_data['name']}", color).ljust(48) + colored("║", "90"))
    print(colored("╠" + "═"*40 + "╣", "90"))
    print(colored("║ ", "90") + colored(f"Rarity : [{pet_data['rarity_tier']}]", color).ljust(48) + colored("║", "90"))
    print(colored("║ ", "90") + colored(f"Affinit: {pet_data['agent_affinity']}", "37").ljust(48) + colored("║", "90"))
    print(colored("║ ", "90") + colored(f"Domain : {pet_data['specialty']}", "32").ljust(48) + colored("║", "90"))
    print(colored("╠" + "═"*40 + "╣", "90"))
    print(colored("║ ", "90") + colored(f"INT (Logic) : {f_int} (IV:{ivs['int_iv']})", "36").ljust(48) + colored("║", "90"))
    print(colored("║ ", "90") + colored(f"SPD (Code)  : {f_spd} (IV:{ivs['spd_iv']})", "33").ljust(48) + colored("║", "90"))
    print(colored("║ ", "90") + colored(f"DEF (Armor) : {f_def} (IV:{ivs['def_iv']})", "31").ljust(48) + colored("║", "90"))
    print(colored("╚" + "═"*40 + "╝", "90"))
    
    print(colored(f"\n  >> {pet_data['description']}", "3m"))
    
    return pid, pet_data, ivs

def summon(affinity=None):
    pid, pet_data = omniclawdex.GachaSystem.draw_gacha(affinity)
    ivs = omniclawdex.GachaSystem.roll_ivs()
    return print_stat_card(pid, pet_data, ivs)

if __name__ == "__main__":
    summon()
