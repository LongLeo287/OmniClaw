import time
import sys
import random

def colored(text, color_code):
    return f"\x1b[{color_code}m{text}\x1b[0m"

# Frames
f_idle_1 = r"""
     , _ ,     
    ( o o )    
   /'  M  `\   
  |___|_|___|  
"""
f_idle_blink = r"""
     , _ ,     
    ( - - )    
   /'  M  `\   
  |___|_|___|  
"""
f_look_r = r"""
     , _ ,     
    ( o > )    
   /'  M  `\   
  |___|_|___|  
"""
f_look_l = r"""
     , _ ,     
    ( < o )    
   /'  M  `\   
  |___|_|___|  
"""
f_sleep_1 = r"""
       Z       
     , _ ,  z  
    ( - - )    
  --|___|___|--
"""
f_sleep_2 = r"""
         Z     
     , _ , Z   
    ( - - )    
  --|___|___|--
"""
f_walk_1 = r"""
               
     , _ ,     
    ( o o )    
  ==/  M  \==  
"""
f_walk_2 = r"""
               
     , _ ,     
    ( - - )    
  --|___|___|--
"""

def draw_frame(frame, padding, color):
    sys.stdout.write('\r')
    for line in frame.strip('\n').split('\n'):
        if not line.strip(): 
            sys.stdout.write("    " + padding + "            \033[K\n")
        else:
            sys.stdout.write("    " + padding + colored(line, color) + "\033[K\n")
    sys.stdout.flush()

def hide_cursor(): sys.stdout.write('\033[?25l')
def show_cursor(): sys.stdout.write('\033[?25h\n')
def move_up(lines): sys.stdout.write(f"\033[{lines}A")

def run_pet():
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except: pass
    
    print("\n" + colored("✦ OMNICLAW VIRTUAL BUDDY (Press Ctrl+C to exit) ✦", "35;1"))
    hide_cursor()
    print("\n" * 5)
    move_up(5)
    
    color = "36" # Cyan
    x_pos = 5
    
    states = ["IDLE", "WALK", "SLEEP"]
    
    try:
        while True:
            # Tâm trạng thay đổi ngẫu nhiên
            state = random.choices(states, weights=[40, 40, 20])[0]
            duration = random.randint(10, 25) # Số khung hình cho mỗi chu kì
            
            if state == "IDLE":
                for _ in range(duration):
                    padding = " " * x_pos
                    r = random.random()
                    if r < 0.15: frame = f_idle_blink
                    elif r < 0.30: frame = f_look_r
                    elif r < 0.45: frame = f_look_l
                    else: frame = f_idle_1
                    
                    draw_frame(frame, padding, color)
                    time.sleep(0.5)
                    move_up(4)
                    
            elif state == "SLEEP":
                padding = " " * x_pos
                for i in range(duration):
                    frame = f_sleep_1 if i % 2 == 0 else f_sleep_2
                    draw_frame(frame, padding, "90") # Chuyển màu tối khi ngủ
                    time.sleep(0.8)
                    move_up(4)
                    
            elif state == "WALK":
                direction = random.choice([-1, 1])
                for i in range(duration):
                    x_pos += direction * 2
                    if x_pos >= 40: 
                        direction = -1
                        frame = f_look_l
                    elif x_pos <= 0: 
                        direction = 1
                        x_pos = 0
                        frame = f_look_r
                    else:
                        frame = f_walk_1 if i % 2 == 0 else f_walk_2
                    
                    padding = " " * x_pos
                    draw_frame(frame, padding, color)
                    time.sleep(0.15)
                    move_up(4)
                    
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[4B")
        sys.stdout.write("\033[K")
        show_cursor()
        print(colored("  >> Cyber-Owl wrapped itself in its wings and went offline.", "90"))

if __name__ == "__main__":
    run_pet()
