import time
import sys
import random
import os

def colored(text, color_code):
    return f"\x1b[{color_code}m{text}\x1b[0m"

# Core ASCII Frames (Cyber-Owl)
FRAMES = {
    "idle_1": r"""
     , _ ,     
    ( o o )    
   /'  M  `\   
  |___|_|___|  
""",
    "idle_blink": r"""
     , _ ,     
    ( - - )    
   /'  M  `\   
  |___|_|___|  
""",
    "look_r": r"""
     , _ ,     
    ( o > )    
   /'  M  `\   
  |___|_|___|  
""",
    "look_l": r"""
     , _ ,     
    ( < o )    
   /'  M  `\   
  |___|_|___|  
""",
    "sleep_1": r"""
       Z       
     , _ ,  z  
    ( - - )    
  --|___|___|--
""",
    "sleep_2": r"""
         Z     
     , _ , Z   
    ( - - )    
  --|___|___|--
""",
    "walk_1": r"""
               
     , _ ,     
    ( o o )    
  ==/  M  \==  
""",
    "walk_2": r"""
               
     , _ ,     
    ( - - )    
  --|___|___|--
""",
    "jump": r"""
     , _ ,     
    ( ^_^ )    
   /'  M  `\   
     | |       
""",
    "land": r"""
               
     , _ ,     
    ( ^_^ )    
  --|___|___|--
"""
}

class OmniPetEngine:
    def __init__(self, color="36"):
        self.color = color
        self.x_pos = 5
        self.init_console()

    def init_console(self):
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except: pass

    def hide_cursor(self): sys.stdout.write('\033[?25l')
    def show_cursor(self): sys.stdout.write('\033[?25h')
    def move_up(self, lines): sys.stdout.write(f"\033[{lines}A")

    def draw_frame(self, frame_key, padding, custom_color=None):
        frame = FRAMES[frame_key]
        c = custom_color if custom_color else self.color
        sys.stdout.write('\r')
        for line in frame.strip('\n').split('\n'):
            if not line.strip(): 
                sys.stdout.write("    " + padding + "            \033[K\n")
            else:
                sys.stdout.write("    " + padding + colored(line, c) + "\033[K\n")
        sys.stdout.flush()

    def cleanup(self):
        sys.stdout.write("\033[4B\033[K")
        sys.stdout.write('\r\033[K')
        self.show_cursor()

    # ANIMATION PRESETS
    
    def celebrate(self):
        """Short jumping animation for pipeline successes"""
        self.init_console()
        self.hide_cursor()
        print("\n" * 5)
        self.move_up(5)
        try:
            for _ in range(2): # Jump Twice
                self.draw_frame("jump", " "*self.x_pos, "32;1") # Green
                time.sleep(0.3)
                self.move_up(4)
                self.draw_frame("land", " "*self.x_pos, "32")
                time.sleep(0.15)
                self.move_up(4)
                
            self.draw_frame("idle_1", " "*self.x_pos)
            time.sleep(0.2)
        finally:
            self.cleanup()

    def infinite_loop(self):
        """Runs the infinite state machine"""
        print("\n" + colored("✦ OMNICLAW VIRTUAL BUDDY (Nhấn Ctrl+C để thoát) ✦", "35;1"))
        self.hide_cursor()
        print("\n" * 5)
        self.move_up(5)
        
        states = ["IDLE", "WALK", "SLEEP"]
        direction = 1
        
        try:
            while True:
                state = random.choices(states, weights=[40, 40, 20])[0]
                duration = random.randint(10, 25)
                
                if state == "IDLE":
                    for _ in range(duration):
                        r = random.random()
                        if r < 0.15: f = "idle_blink"
                        elif r < 0.30: f = "look_r"
                        elif r < 0.45: f = "look_l"
                        else: f = "idle_1"
                        
                        self.draw_frame(f, " "*self.x_pos)
                        time.sleep(0.4)
                        self.move_up(4)
                        
                elif state == "SLEEP":
                    for i in range(duration):
                        f = "sleep_1" if i % 2 == 0 else "sleep_2"
                        self.draw_frame(f, " "*self.x_pos, "90")
                        time.sleep(0.8)
                        self.move_up(4)
                        
                elif state == "WALK":
                    direction = random.choice([-1, 1])
                    for i in range(duration):
                        self.x_pos += direction * 2
                        if self.x_pos >= 40: 
                            direction = -1; f = "look_l"
                        elif self.x_pos <= 0: 
                            direction = 1; self.x_pos = 0; f = "look_r"
                        else:
                            f = "walk_1" if i % 2 == 0 else "walk_2"
                        
                        self.draw_frame(f, " "*self.x_pos)
                        time.sleep(0.15)
                        self.move_up(4)
                        
        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup()
            print(colored("  >> Buddy went offline.\n", "90"))

if __name__ == "__main__":
    engine = OmniPetEngine()
    engine.infinite_loop()
