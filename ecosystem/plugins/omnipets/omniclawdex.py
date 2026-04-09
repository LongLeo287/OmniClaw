import random

# OMNICLAWDEX REGISTRY
# Base stats scale from 10 to 100

OMNICLAWDEX = {
    "OP-001": {
        "name": "Cyber-Owl",
        "specialty": "Bug Hunter",
        "agent_affinity": "SRE-Agent / Auditor",
        "rarity_tier": "COMMON", # 50%
        "color": "36", # Cyan
        "base_stats": {"int": 80, "spd": 40, "def": 90},
        "description": "Stays up all night hunting for logic errors and security vulnerabilities.",
        "frames": {
            "idle_1": r"""
     , _ ,     
    ( o o )    
   /'  M  `\   
  |___|_|___|  
""",
            "walk_1": r"""
               
     , _ ,     
    ( o > )    
  ==/  M  \==  
"""
        }
    },
    "OP-002": {
        "name": "Null-Cat",
        "specialty": "Code Architect",
        "agent_affinity": "Software Engineer",
        "rarity_tier": "UNCOMMON", # 30%
        "color": "35", # Purple
        "base_stats": {"int": 90, "spd": 85, "def": 40},
        "description": "Cold and skilled. Types code faster than you can debug.",
        "frames": {
            "idle_1": r"""
   /\___/\     
  ( o   o )    
  (  =^=  )    
  (        )   
""",
            "walk_1": r"""
               
   /\___/\     
  ( >   < )    
  --^---^---   
"""
        }
    },
    "OP-003": {
        "name": "Byte-Dog",
        "specialty": "Watchdog",
        "agent_affinity": "DevOps / System Monitor",
        "rarity_tier": "RARE", # 15%
        "color": "32", # Green
        "base_stats": {"int": 50, "spd": 90, "def": 80},
        "description": "Barks aggressively upon detecting OOM warnings or network bottlenecks.",
        "frames": {
            "idle_1": r"""
    __         
   /  \____    
  / / ___  \   
  `m`m   `m`m  
""",
            "walk_1": r"""
               
    __         
   / >\____    
   `m`m   `m`m 
"""
        }
    },
    "OP-004": {
        "name": "Gacha-Dragon",
        "specialty": "Data Assimilator",
        "agent_affinity": "OA Academy / OIW",
        "rarity_tier": "LEGENDARY", # 5%
        "color": "33;1", # Bold Gold
        "base_stats": {"int": 99, "spd": 30, "def": 99},
        "description": "Infinite stomach. Swallows entire repositories containing tens of thousands of lines of code.",
        "frames": {
            "idle_1": r"""
    \||/       
    |  @___oo  
  /\  /\   / ( 
 ) /^\) ^\/ _/ 
""",
            "walk_1": r"""
               
    \||/       
    (  @___oo  
  --\  \   / ( 
    /^\) ^\/ _/
"""
        }
    }
}

class GachaSystem:
    @staticmethod
    def roll_ivs():
        """Rolls Individual Values (IVs) from 0 to 31 like in Pokemon"""
        return {
            "int_iv": random.randint(0, 31),
            "spd_iv": random.randint(0, 31),
            "def_iv": random.randint(0, 31)
        }

    @staticmethod
    def calculate_final_stat(base, iv):
        """Simple formula: Base + (IV * 1.5)"""
        return int(base + (iv * 1.5))
        
    @staticmethod
    def draw_gacha(affinity_filter=None):
        """Pulls a random pet. If affinity is passed, forces a specific pet to spawn."""
        if affinity_filter:
            for pid, data in OMNICLAWDEX.items():
                if affinity_filter.lower() in data["agent_affinity"].lower():
                    return pid, data
                    
        roll = random.random()
        if roll < 0.05:
            pid = "OP-004"
        elif roll < 0.20:
            pid = "OP-003"
        elif roll < 0.50:
            pid = "OP-002"
        else:
            pid = "OP-001"
            
        return pid, OMNICLAWDEX[pid]
