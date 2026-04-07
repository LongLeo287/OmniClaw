import sys
import time
import os
import random

# Load Pet Engine
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
try:
    import omni_pet_engine
    HAS_PET = True
except ImportError:
    HAS_PET = False

def colored(text, color_code):
    return f"\x1b[{color_code}m{text}\x1b[0m"

def draw_progress_pet(percentage, engine, eating=False):
    engine.hide_cursor()
    sys.stdout.write('\r')
    
    # Calculate position (0 to 40 max)
    target_pos = int((percentage / 100.0) * 40)
    engine.x_pos = target_pos
    
    # Pick frame
    if eating:
        frame = "jump"
        color = "31;1" # Red for eating bugs
    elif percentage >= 100:
        frame = "idle_1"
        color = "36"
    else:
        frame = "walk_1" if (target_pos % 2 == 0) else "walk_2"
        color = "32" # Green for scanning
        
    engine.draw_frame(frame, " " * engine.x_pos, color)
    sys.stdout.write(f"\n      [{percentage}%] Scanning core infrastructure...\033[K")
    sys.stdout.flush()
    engine.move_up(5)

def run_pulse():
    print(colored("\n========== OMNICLAW SYSTEM PULSE ==========", "35;1"))
    if HAS_PET:
        engine = omni_pet_engine.OmniPetEngine()
        engine.init_console()
        print("\n" * 5)
        engine.move_up(5)
        
        for p in range(1, 101):
            eating = False
            # Simulate randomly finding buggy repos
            if p in [15, 45, 78]:
                eating = True
            
            draw_progress_pet(p, engine, eating)
            
            if eating:
                time.sleep(0.5) # Freeze to chew the bug
            else:
                time.sleep(0.05)
                
        engine.draw_frame("idle_1", " " * 40, "36")
        sys.stdout.write("\n      [100%] System Pulse Complete. Ecosystem is healthy.\033[K\n")
        engine.cleanup()
    else:
        print("Scaning... 100% Complete.")
        
    print(colored("===========================================\n", "35;1"))

if __name__ == "__main__":
    run_pulse()
