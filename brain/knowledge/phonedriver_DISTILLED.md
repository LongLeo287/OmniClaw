---
id: phonedriver
type: knowledge
owner: OA_Triage
---
# phonedriver
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Phone Driver

A Python-based mobile automation agent that uses Qwen3-VL vision-language models to understand and interact with Android devices through visual analysis and ADB commands.

<p align="center">
  <img src="Images/PhoneDriver.png" width="600" alt="Phone Driver Demo">
</p>

## Features

- 🤖 **Vision-powered automation**: Uses Qwen3-VL to visually understand phone screens
- 📱 **ADB integration**: Controls Android devices via ADB commands
- 🎯 **Natural language tasks**: Describe what you want in plain English
- 🖥️ **Web UI**: Built-in Gradio interface for easy control
- 📊 **Real-time feedback**: Live screenshots and execution logs

## Requirements

- Python 3.10+
- Android device with USB debugging & Developer Mode enabled
- ADB (Android Debug Bridge) installed
- GPU with sufficient VRAM (Tested on 24gb GPU with Qwen3-VL-8B Model)
- The Repo is set to use the Dense Qwen3-VL 4B/8B Model which performs very well. To swap to an MoE model, see the configuration section below 

## Installation

### 1. Install ADB

**Linux/Ubuntu:**
```bash
sudo apt update
sudo apt install adb
```
### 2. Clone Repo & Install Python Dependencies

```bash
git clone https://github.com/OminousIndustries/PhoneDriver.git
cd PhoneDriver
```
Create a Virtual Enviornment

```bash
python -m venv phonedriver
source phonedriver/bin/activate
```
Install Python Deps

```bash
pip install git+https://github.com/huggingface/transformers
# pip install transformers==4.57.0 # currently, V4.57.0 is not released

# Install other requirements
pip install pillow gradio qwen_vl_utils requests
```

### 3. Connect Your Device

1. Enable USB debugging on your Android device (Settings → Developer Options)
2. Connect via USB
3. Verify connection:
```bash
adb devices
```
You should see your device listed.

## Configuration

### Model Selection

Edit `qwen_vl_agent.py` to choose your model:

```python
# For 4B model
model_name: str = "Qwen/Qwen3-VL-4B-Instruct"

# For 8B model 
#model_name: str = "Qwen/Qwen3-VL-8B-Instruct"
```

### If you want to try a Qwen3 MoE model, you need to change the import in `qwen_vl_agent.py` to the following:

```python
#from transformers import Qwen3VLForConditionalGeneration, AutoProcessor  - Comment this import out, it is for the Dense models
# Uncomment the import below for the MoE Variants!!!
from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor
```

You will also need to change line 61: 

```python
        self.model = Qwen3VLForConditionalGeneration.from_pretrained(
```
Change it to:

```python
        self.model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
```

### Screen Resolution

The agent can auto-detect your device resolution from the Web UI settings tab, but you can manually configure it in `config.json`.

```json
{
  "screen_width": 1080,
  "screen_height": 2340,
  ...
}
```

To get your device resolution, with the device connected to your computer type the following in the terminal: 
```bash
adb shell wm size
```

## Usage

### Web UI (Recommended)

Launch the Gradio interface:

```bash
python ui.py
```

Navigate to `http://localhost:7860` and enter tasks like:
- "Open Chrome"
- "Search for weather in New York"
- "Open Settings and enable WiFi"

### Command Line

```bash
python phone_agent.py "your task here"
```

Example:
```bash
python phone_agent.py "Open the camera app"
```

## How It Works

1. **Screenshot Capture**: Takes a screenshot of the phone via ADB
2. **Visual Analysis**: Qwen3-VL analyzes the screen to understand UI elements
3. **Action Planning**: Determines the best action to take (tap, swipe, type, etc.)
4. **Execution**: Sends ADB commands to perform the action
5. **Repeat**: Continues until task is complete or max cycles reached

## Configuration Options

Key settings in `config.json`:

- `temperature`: Model creativity (0.0-1.0, default: 0.1)
- `max_tokens`: Max response length (default: 512)
- `step_delay`: Wait time between actions in seconds (default: 1.5)
- `max_retries`: Maximum retry attempts (default: 3)
- `use_flash_attention`: Enable Flash Attention 2 for faster inference

## Troubleshooting

**Device not detected:**
- Ensure USB debugging is enabled
- Run `adb devices` to verify connection
- Try `adb kill-server && adb start-server`

**Wrong tap locations:**
- Auto-detect resolution in Settings tab of UI
- Or manually verify with `adb shell wm size`

**Model loading errors:**
- Ensure you have sufficient VRAM
- Try the 8B model for lower memory requirements
- Check that transformers is installed from source

**Out of memory:**
- Use the 8B model instead of 30B
- Reduce `max_tokens` in config
- Close other applications using GPU memory

## License

Apache License 2.0 - see LICENSE file for details

## Acknowledgments

- Built with [Qwen3-VL](https://github.com/QwenLM/Qwen-VL) by Alibaba Cloud
- Uses [Gradio](https://gradio.app/) for the web interface

```

### File: config.json
```json
{
  "device_id": null,
  "screen_width": 1080,
  "screen_height": 2340,
  "screenshot_dir": "./screenshots",
  "max_retries": 3,
  "use_flash_attention": true,
  "temperature": 0.1,
  "max_tokens": 512,
  "step_delay": 1.5,
  "enable_visual_debug": true
}

```

### File: phone_agent.py
```py
import os
import json
import time
import logging
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

from qwen_vl_agent import QwenVLAgent


class PhoneAgent:
    """
    Phone automation agent using Qwen3-VL for visual understanding and ADB for control.
    
    This agent:
    - Captures screenshots from Android devices via ADB
    - Uses Qwen3-VL to analyze screens and determine actions
    - Executes actions through ADB commands
    - Tracks context and action history
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the phone agent.
        
        Args:
            config: Configuration dictionary
        """
        # Default configuration
        default_config = {
            'device_id': None,  # Auto-detect first device if None
            'screen_width': 1080,  # Must match your device
            'screen_height': 2340,  # Must match your device
            'screenshot_dir': './screenshots',
            'max_retries': 3,
            'model_name': 'Qwen/Qwen3-VL-30B-A3B-Instruct',
            'use_flash_attention': False,
            'temperature': 0.1,
            'max_tokens': 512,
            'step_delay': 1.5,  # Seconds to wait after each action
            'enable_visual_debug': False,  # Save annotated screenshots
        }
        
        self.config = default_config
        if config:
            self.config.update(config)
        
        # Session context
        self.context = {
            'previous_actions': [],
            'current_app': "Home",
            'task_request': "",
            'session_id': datetime.now().strftime("%Y%m%d_%H%M%S"),
            'screenshots': []
        }
        
        # Setup logging
        self._setup_logging()
        
        # Initialize directories
        self._setup_directories()
        
        # Check ADB connection
        self._check_adb_connection()
        
        # Initialize Qwen3-VL agent
        logging.info("Initializing Qwen3-VL agent...")
        self.vl_agent = QwenVLAgent(
            use_flash_attention=self.config.get('use_flash_attention', False),
            temperature=self.config['temperature'],
            max_tokens=self.config['max_tokens'],
        )
        logging.info("Phone agent ready")
    
    def _setup_logging(self):
        """Configure logging for this session."""
        log_file = f"phone_agent_{self.context['session_id']}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        logging.info(f"Session started: {self.context['session_id']}")
    
    def _setup_directories(self):
        """Create necessary directories."""
        Path(self.config['screenshot_dir']).mkdir(parents=True, exist_ok=True)
        logging.info(f"Screenshots directory: {self.config['screenshot_dir']}")
    
    def _check_adb_connection(self):
        """Verify ADB connection and get device info."""
        try:
            # List devices
            result = subprocess.run(
                ["adb", "devices"],
                check=True,
                capture_output=True,
                text=True
            )
            
            # Auto-detect device if not specified
            if self.config['device_id'] is None:
                lines = result.stdout.strip().split('\n')
                if len(lines) > 1:
                    device_info = lines[1].split('\t')
                    if len(device_info) > 0 and device_info[1].strip() == 'device':
                        self.config['device_id'] = device_info[0].strip()
                        logging.info(f"Auto-detected device: {self.config['device_id']}")
                    else:
                        raise Exception("No authorized device found")
                else:
                    raise Exception("No devices connected")
            
            # Test connection
            self._run_adb_command("shell echo 'Connected'")
            logging.info("✓ ADB connection verified")
            
            # Get actual screen resolution
            self._verify_screen_resolution()
            
        except subprocess.CalledProcessError as e:
            logging.error(f"ADB error: {e}")
            raise Exception(
                "Failed to connect via ADB. Ensure USB debugging is enabled and device is authorized."
            )
    
    def _verify_screen_resolution(self):
        """Verify the configured screen resolution matches the device."""
        try:
            result = self._run_adb_command("shell wm size")
            # Output format: "Physical size: 1080x2340"
            if "Physical size:" in result:
                size_str = result.split("Physical size:")[1].strip()
                width, height = map(int, size_str.split('x'))
                
                if width != self.config['screen_width'] or height != self.config['screen_height']:
                    logging.warning("=" * 60)
                    logging.warning("RESOLUTION MISMATCH DETECTED!")
                    logging.warning(f"Device actual:    {width} x {height}")
                    logging.warning(f"Config setting:   {self.config['screen_width']} x {self.config['screen_height']}")
                    logging.warning("Please update config.json with correct resolution!")
                    logging.warning("=" * 60)
                    
                    # Update config automatically
                    self.config['screen_width'] = width
                    self.config['screen_height'] = height
                    logging.info(f"Auto-corrected to: {width} x {height}")
                else:
                    logging.info(f"✓ Screen resolution confirmed: {width} x {height}")
        except Exception as e:
            logging.warning(f"Could not verify screen resolution: {e}")
    
    def _run_adb_command(self, command: str) -> str:
        """Execute an ADB command and return output."""
        device_prefix = f"-s {self.config['device_id']}" if self.config['device_id'] else ""
        full_command = f"adb {device_prefix} {command}"
        
        try:
            result = subprocess.run(
                full_command,
                shell=True,
                check=True,
                capture_output=True,
                text=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"ADB command failed: {command}")
            logging.error(f"Error: {e.stderr}")
            raise
    
    def capture_screenshot(self) -> str:
        """
        Capture a screenshot from the device.
        
        Returns:
            Path to the saved screenshot
        """
        timestamp = int(time.time())
        screenshot_path = os.path.join(
            self.config['screenshot_dir'],
            f"screen_{self.context['session_id']}_{timestamp}.png"
        )
        
        try:
            # Capture and transfer screenshot
            self._run_adb_command("shell screencap -p /sdcard/screenshot.png")
            self._run_adb_command(f"pull /sdcard/screenshot.png {screenshot_path}")
            self._run_adb_command("shell rm /sdcard/screenshot.png")
            
            logging.info(f"Screenshot captured: {screenshot_path}")
            self.context['screenshots'].append(screenshot_path)
            return screenshot_path
            
        except Exception as e:
            logging.error(f"Screenshot capture failed: {e}")
            raise
    
    def execute_action(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute an action on the device.
        
        Args:
            action: Action dictionary from Qwen3-VL
            
        Returns:
            Result dictionary with success status
        """
        try:
            action_type = action['action']
            logging.info(f"Executing: {action_type}")
            
            # Handle task completion
            if action_type == 'terminate':
                status = action.get('status', 'success')
                message = action.get('message', 'Task complete')
                logging.info(f"✓ Task {status}: {message}")
                return {
                    'success': True,
                    'action': action,
                    'task_complete': True
                }
            
            # Handle each action type
            if action_type == 'tap':
                self._execute_tap(action)
            
            elif action_type == 'swipe':
                self._execute_swipe(action)
            
            elif action_type == 'type':
                self._execute_type(action)
            
            elif action_type == 'wait':
                self._execute_wait(action)
            
            else:
                raise ValueError(f"Unknown action type: {action_type}")
            
            # Record action in history
            self.context['previous_actions'].append({
                'action': action_type,
                'timestamp': time.time(),
                'elementName': action.get('observation', '')[:50]  # Brief description
            })
            
            # Standard delay after action
            time.sleep(self.config['step_delay'])
            
            return {
                'success': True,
                'action': action,
                'task_complete': False
            }
            
        except Exception as e:
            logging.error(f"Action execution failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'action': action,
                'task_complete': False
            }
    
    def _execute_tap(self, action: Dict[str, Any]):
        """Execute a tap action."""
        if 'coordinates' not in action:
            raise ValueError("Tap action missing coordinates")
        
        # Get normalized coordinates
        norm_x, norm_y = action['coordinates']
        
        # Convert to pixel coordinates
        x = int(norm_x * self.config['screen_width'])
        y = int(norm_y * self.config['screen_height'])
        
        # Clamp to screen bounds
        x = max(0, min(x, self.config['screen_width'] - 1))
        y = max(0, min(y, self.config['screen_height'] - 1))
        
        logging.info(f"Tapping at ({x}, {y}) [normalized: ({norm_x:.3f}, {norm_y:.3f})]")
        self._run_adb_command(f"shell input tap {x} {y}")
    
    def _execute_swipe(self, action: Dict[str, Any]):
        """Execute a swipe action."""
        direction = action.get('direction', 'up')
        
        # Calculate swipe coordinates
        center_x = self.config['screen_width'] // 2
        center_y = self.config['screen_height'] // 2
        
        start_x, start_y = center_x, center_y
        
        # Define swipe distances (70% of screen dimension)
        swipe_distance = 0.7
        
        if direction == 'up':
            end_x = center_x
            end_y = int(center_y * (1 - swipe_distance))
        elif direction == 'down':
            end_x = center_x
            end_y = int(center_y * (1 + swipe_distance))
        elif direction == 'left':
            end_x = int(center_x * (1 - swipe_distance))
            end_y = center_y
        elif direction == 'right':
            end_x = int(center_x * (1 + swipe_distance))
            end_y = center_y
        else:
            raise ValueError(f"Invalid swipe direction: {direction}")
        
        logging.info(f"Swiping {direction}: ({start_x}, {start_y}) -> ({end_x}, {end_y})")
        self._run_adb_command(f"shell input swipe {start_x} {start_y} {end_x} {end_y} 300")
    
    def _execute_type(self, action: Dict[str, Any]):
        """Execute a type action."""
        if 'text' not in action:
            raise ValueError("Type action missing text")
        
        text = action['text']
        
        # Check if we tapped a text field recently
        recent_actions = self.context['previous_actions'][-3:]
        tapped_text_field = any(
            a.get('action') == 'tap' for a in recent_actions
        )
        
        if not tapped_text_field:
            logging.warning("Type action without recent tap - may fail")
        
        # Escape and format text for ADB
        escaped_text = text.replace("'", "\\'").replace('"', '\\"')
        escaped_text = escaped_text.replace(" ", "%s")  # ADB requires %s for spaces
        
        logging.info(f"Typing: {text}")
        self._run_adb_command(f'shell input text "{escaped_text}"')
    
    def _execute_wait(self, action: Dict[str, Any]):
        """Execute a wait action."""
        wait_time = action.get('waitTime', 1000) / 1000.0  # Convert ms to seconds
        logging.info(f"Waiting {wait_time:.1f}s...")
        time.sleep(wait_time)
    
    def execute_cycle(self, user_request: str) -> Dict[str, Any]:
        """
        Execute a single interaction cycle.
        
        Args:
            user_request: The user's task request
            
        Returns:
            Result dictionary
        """
        try:
            # Capture screenshot
            screenshot_path = self.capture_screenshot()
            
            # Analyze with Qwen3-VL
            action = self.vl_agent.analyze_screenshot(
                screenshot_path,
                user_request,
                self.context
            )
            
            if not action:
                raise Exception("Failed to get action from model")
            
            # Log model's observation and reasoning
            if 'observation' in action:
                logging.info(f"Model observation: {action['observation']}")
            if 'reasoning' in action:
                logging.info(f"Model reasoning: {action['reasoning']}")
            
            # Execute the action
            result = self.execute_action(action)
            
            return result
            
        except Exception as e:
            logging.error(f"Cycle execution failed: {e}")
            raise
    
    def execute_task(self, user_request: str, max_cycles: int = 15) -> Dict[str, Any]:
        """
        Execute a complete task through multiple cycles.
        
        Args:
            user_request: The user's task description
            max_cycles: Maximum number of action cycles
            
        Returns:
            Task result dictionary
        """
        self.context['task_request'] = user_request
        logging.info("=" * 60)
        logging.info(f"STARTING TASK: {user_request}")
        logging.info("=" * 60)
        
        cycles = 0
        task_complete = False
        last_error = None
        
        while cycles < max_cycles and not task_complete:
            cycles += 1
 
... [TRUNCATED]
```

### File: qwen_vl_agent.py
```py
# qwen_vl_agent.py
import json
import logging
import re
from typing import Any, Dict, List, Optional

import torch
from PIL import Image
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor  # NOT MoeFor
#from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor - This is only for the MoE Variants!!!
from qwen_vl_utils import process_vision_info
import warnings

# To supress these warnings you can uncomment the following two lines
# warnings.filterwarnings('ignore', message='.*Flash Efficient attention.*')
# warnings.filterwarnings('ignore', message='.*Mem Efficient attention.*')


class QwenVLAgent:
    """
    Vision-Language agent using Qwen3-VL-30B-A3B-Instruct for mobile GUI automation.
    Uses the official mobile_use function calling format.
    """

    def __init__(
        self,
        model_name: str = "Qwen/Qwen3-VL-8B-Instruct",
        device_map: str = "auto",
        dtype: Optional[torch.dtype] = None,
        use_flash_attention: bool = False,
        temperature: float = 0.1,
        max_tokens: int = 512,
    ) -> None:
        """Initialize the Qwen3-VL agent."""
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

        logging.info(f"Loading Qwen3-VL model: {model_name}")

        if dtype is None:
            dtype = torch.bfloat16

        # Build model kwargs once; load once
        model_kwargs: Dict[str, Any] = dict(
            torch_dtype=dtype,
            device_map=device_map,
            low_cpu_mem_usage=True,
            # Only for Strix Halo with 96gb set in bios
            #max_memory={0: "90GiB"},
        )

        if use_flash_attention:
            try:
                import flash_attn  # noqa: F401
                model_kwargs["attn_implementation"] = "flash_attention_2"
                logging.info("Flash Attention 2 enabled")
            except Exception:
                logging.warning("flash_attn not installed; using default attention")

        self.model = Qwen3VLForConditionalGeneration.from_pretrained(
            model_name, **model_kwargs
        )
        self.processor = AutoProcessor.from_pretrained(model_name)
        # For MoE Models You need to change to self.model=Qwen3VLMoeForConditionalGeneration.from_pretrained
        # System prompt matching official format
        self.system_prompt = """# Tools

You may call one or more functions to assist with the user query.

You are provided with function signatures within <tools></tools> XML tags:
<tools>
{"type": "function", "function": {"name": "mobile_use", "description": "Use a touchscreen to interact with a mobile device, and take screenshots.\n* This is an interface to a mobile device with touchscreen. You can perform actions like clicking, typing, swiping, etc.\n* Some applications may take time to start or process actions, so you may need to wait and take successive screenshots to see the results of your actions.\n* The screen's resolution is 999x999.\n* Make sure to click any buttons, links, icons, etc with the cursor tip in the center of the element. Don't click boxes on their edges unless asked.", "parameters": {"properties": {"action": {"description": "The action to perform. The available actions are:\n* `click`: Click the point on the screen with coordinate (x, y).\n* `swipe`: Swipe from the starting point with coordinate (x, y) to the end point with coordinates2 (x2, y2).\n* `type`: Input the specified text into the activated input box.\n* `wait`: Wait specified seconds for the change to happen.\n* `terminate`: Terminate the current task and report its completion status.", "enum": ["click", "swipe", "type", "wait", "terminate"], "type": "string"}, "coordinate": {"description": "(x, y): The x (pixels from the left edge) and y (pixels from the top edge) coordinates to click. Required only by `action=click` and `action=swipe`. Range: 0-999.", "type": "array"}, "coordinate2": {"description": "(x, y): The end coordinates for swipe. Required only by `action=swipe`. Range: 0-999.", "type": "array"}, "text": {"description": "Required only by `action=type`.", "type": "string"}, "time": {"description": "The seconds to wait. Required only by `action=wait`.", "type": "number"}, "status": {"description": "The status of the task. Required only by `action=terminate`.", "type": "string", "enum": ["success", "failure"]}}, "required": ["action"], "type": "object"}}}
</tools>

For each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:
<tool_call>
{"name": <function-name>, "arguments": <args-json-object>}
</tool_call>

Rules:
- Output exactly in the order: Thought, Action, <tool_call>.
- Be brief: one sentence for Thought, one for Action.
- Do not output anything else outside those three parts.
- If finishing, use action=terminate in the tool call.
- For each function call, there must be an "action" key in the "arguments" which denote the type of the action.
- Coordinates are in 999x999 space where (0,0) is top-left and (999,999) is bottom-right."""
        logging.info("Qwen3-VL agent initialized successfully")

    def analyze_screenshot(
        self,
        screenshot_path: str,
        user_request: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:
        """Analyze a phone screenshot and determine the next action."""
        try:
            # Load and resize image to prevent OOM
            image = Image.open(screenshot_path)

            # Resize if too large - keep aspect ratio, max dimension 1280
            max_size = 1280
            if max(image.size) > max_size:
                ratio = max_size / max(image.size)
                new_size = tuple(int(dim * ratio) for dim in image.size)
                image = image.resize(new_size, Image.Resampling.LANCZOS)
                logging.info(f"Resized image from {Image.open(screenshot_path).size} to {image.size}")

            # Build action history
            history = []
            if context:
                previous_actions = context.get('previous_actions', [])
                for i, act in enumerate(previous_actions[-5:], 1):  # Last 5 actions
                    action_type = act.get('action', 'unknown')
                    element = act.get('elementName', '')
                    history.append(f"Step {i}: {action_type} {element}".strip())

            history_str = "; ".join(history) if history else "No previous actions"

            # Build user query in official format
            user_query = f"""The user query: {user_request}.
Task progress (You have done the following operation on the current device): {history_str}."""

            # Messages in official format
            messages = [
                {
                    "role": "system",
                    "content": [{"type": "text", "text": self.system_prompt}],
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_query},
                        {"type": "image", "image": image},
                    ],
                },
            ]

            # Generate response
            action = self._generate_action(messages)

            if action:
                logging.info(f"Generated action: {action.get('action', 'unknown')}")
                logging.debug(f"Full action: {json.dumps(action, indent=2)}")

            return action

        except Exception as e:
            logging.error(f"Error analyzing screenshot: {e}", exc_info=True)
            return None

    def _generate_action(self, messages: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Generate an action from the model given messages."""
        try:
            # Use processor's chat template
            text = self.processor.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )

            # Collect image/video inputs
            image_inputs, video_inputs = process_vision_info(messages)

            # >>>>>>>>>> IMPORTANT FIX: avoid empty lists (use None) <<<<<<<<<<
            if not image_inputs:
                image_inputs = None
            if not video_inputs:
                video_inputs = None

            inputs = self.processor(
                text=[text],
                images=image_inputs,
                videos=video_inputs,   # None when no videos -> skips video path
                padding=True,
                return_tensors="pt",
            )

            # Move to device
            inputs = inputs.to(self.model.device)

            logging.debug("Generating model response...")

            # Optional: clear cache around generation (works with HIP too)
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

            with torch.no_grad():
                generated_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=self.max_tokens,
                    temperature=self.temperature,
                    do_sample=self.temperature > 0,
                    pad_token_id=self.processor.tokenizer.pad_token_id,
                )

            if torch.cuda.is_available():
                torch.cuda.empty_cache()

            # Trim input tokens from output
            generated_ids_trimmed = [
                out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
            ]

            # Decode
            output_text = self.processor.batch_decode(
                generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
            )[0]

            logging.debug(f"Model output: {output_text}")

            # Parse action
            action = self._parse_action(output_text)
            return action

        except Exception as e:
            logging.error(f"Error generating action: {e}", exc_info=True)
            return None

    def _parse_action(self, text: str) -> Optional[Dict[str, Any]]:
        """Parse action from model output in official format."""
        try:
            # Extract tool_call XML content
            match = re.search(r'<tool_call>\s*(\{.*?\})\s*</tool_call>', text, re.DOTALL)
            if not match:
                logging.error("No <tool_call> tags found in output")
                logging.debug(f"Output text: {text}")
                return None

            tool_call_json = match.group(1)
            tool_call = json.loads(tool_call_json)

            # Extract arguments
            if 'arguments' not in tool_call:
                logging.error("No 'arguments' in tool_call")
                return None

            args = tool_call['arguments']
            action_type = args.get('action')
            if not action_type:
                logging.error("No 'action' in arguments")
                return None

            # Convert to our internal format
            action: Dict[str, Any] = {'action': action_type}

            # Handle coordinates (convert from 999x999 space to normalized 0-1)
            if 'coordinate' in args:
                coord = args['coordinate']
                action['coordinates'] = [coord[0] / 999.0, coord[1] / 999.0]

            if 'coordinate2' in args:
                coord2 = args['coordinate2']
                action['coordinate2'] = [coord2[0] / 999.0, coord2[1] / 999.0]

            # Handle swipe - convert to direction for compatibility
            if action_type == 'swipe' and 'coordinates' in action and 'coordinate2' in action:
                start = action['coordinates']
                end = action['coordinate2']
                dx = end[0] - start[0]
                dy = end[1] - start[1]
                if abs(dy) > abs(dx):
                    action['direction'] = 'down' if dy > 0 else 'up'
                else:
                    action['direction'] = 'right' if dx > 0 else 'left'

            # Map action names
            if action_type == 'click':
                action['action'] = 'tap'  # our internal name

            # Copy other fields
            if 'text' in args:
                action['text'] = args['text']
            if 'time' in args:
                action['waitTime'] = int(float(args['time']) * 1000)  # ms
            if 'status' in args:
                action['status'] = args['status']
                action['message'] = f"Task {args['status']}"

            # Extract thought/action description
            thought_match = re.search(r'Thought:\s*(.+?)(?:\n|$)', text)
            action_match = re.search(r'Action:\s*(.+?)(?:\n|$)', text)
            if thought_match:
                action['reasoning'] = thought_match.group(1).strip().strip('"')
            if action_match:
                action['observation'] = action_match.group(1).strip().strip('"')

            # Validate essentials
            if action['action'] == 'tap' and 'coordinates' not in action:
                logging.error("Tap action missing coordinates")
                return None
            if action['action'] == 'type' and 'text' not in action:
                logging.error("Type action missing text")
                return None

            return action

        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON from tool_call: {e}")
            logging.debug(f"Text: {text}")
            return None
        except Exception as e:
            logging.error(f"Error parsing action: {e}")
            logging.debug(f"Text: {text}")
            return None

    def check_task_completion(
        self,
        screenshot_path: str,
        user_request: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Ask the model if the task has been completed."""
        try:
            # Load and resize image
            image = Image.open(screenshot_path)
            max_size = 1280
            if max(image.size) > max_size:
                ratio = max_size / max(image.size)
                new_size = tuple(int(dim * ratio) for dim in image.size)
                image = image.resize(new_size, Image.Resampling.LANCZOS)

            completion_query = f"""The user query: {user_request}.

You have completed {len(context.get('previous_actions', []))} actions.

Look at the current screen and determine: Has the task been completed successfully?

If complete, use action=terminate with status="success".
If not complete, explain what still needs to be done and use action=terminate with status="failure"."""  # noqa: E501

            messages = [
                {
                    "role": "system",
                    "content": [{"type": "text", "text": self.system_prompt}],
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": completion_query},
                        {"type": "image", "image": image},
                 
... [TRUNCATED]
```

### File: qwen_vl_utils.py
```py
# qwen_vl_utils.py
from typing import Any, Dict, List, Tuple
from PIL import Image


def _as_image(x):
    """
    Accepts PIL.Image, local path, or http(s)/data URL.
    Returns a PIL.Image (RGB) or passes URLs through (processor can fetch).
    """
    if isinstance(x, Image.Image):
        return x.convert("RGB")
    if isinstance(x, str):
        if x.lower().startswith(("http://", "https://", "data:")):
            return x
        return Image.open(x).convert("RGB")
    # Let the processor handle anything else it supports
    return x


def process_vision_info(messages: List[Dict[str, Any]]) -> Tuple[List[Any], List[Any]]:
    """
    Minimal shim matching the signature that qwen_vl_agent expects.
    Collects image/video inputs from the chat-format messages.
    """
    images, videos = [], []
    for m in messages:
        for c in m.get("content", []):
            t = c.get("type")
            if t == "image":
                images.append(_as_image(c.get("image")))
            elif t == "video":
                videos.append(c.get("video"))
    return images, videos

```

### File: ui.py
```py
import os
import json
import logging
import subprocess
from pathlib import Path
from threading import Thread
import gradio as gr

from phone_agent import PhoneAgent


class UILogHandler(logging.Handler):
    """Custom logging handler that stores logs for UI display."""
    
    def __init__(self):
        super().__init__()
        self.logs = []
    
    def emit(self, record):
        log_entry = self.format(record)
        self.logs.append(log_entry)
        if len(self.logs) > 200:
            self.logs = self.logs[-200:]


# Global state
current_screenshot = None
log_handler = None
is_running = False
agent = None
current_config = None


def load_config(config_path="config.json"):
    """Load configuration from file."""
    if not os.path.exists(config_path):
        return get_default_config()
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        default = get_default_config()
        for key, value in default.items():
            if key not in config:
                config[key] = value
        return config
    except json.JSONDecodeError:
        return get_default_config()


def get_default_config():
    """Get default configuration."""
    return {
        "device_id": None,
        "screen_width": 1080,
        "screen_height": 2340,
        "screenshot_dir": "./screenshots",
        "max_retries": 3,
        "model_name": "Qwen/Qwen3-VL-30B-A3B-Instruct",
        "use_flash_attention": False,
        "temperature": 0.1,
        "max_tokens": 512,
        "step_delay": 1.5,
        "enable_visual_debug": False
    }


def save_config(config, config_path="config.json"):
    """Save configuration to file."""
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        logging.error(f"Failed to save config: {e}")
        return False


def setup_logging():
    """Configure logging for the UI."""
    global log_handler
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    log_handler = UILogHandler()
    log_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(formatter)
    root_logger.addHandler(log_handler)
    
    file_handler = logging.FileHandler("phone_agent_ui.log")
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)


def detect_device_resolution():
    """Try to detect connected device resolution via ADB."""
    try:
        result = subprocess.run(
            ["adb", "shell", "wm", "size"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0 and "Physical size:" in result.stdout:
            size_str = result.stdout.split("Physical size:")[1].strip()
            width, height = map(int, size_str.split('x'))
            return width, height, f"✓ Detected: {width} x {height}"
        else:
            return None, None, "⚠️ No device detected"
            
    except Exception as e:
        return None, None, f"✗ Error: {str(e)}"


def execute_task_thread(task, max_cycles, config):
    """Run task in background thread."""
    global current_screenshot, is_running, agent
    
    if log_handler:
        log_handler.logs.clear()
    
    is_running = True
    
    try:
        logging.info(f"Starting task: '{task}'")
        
        # Only create agent if it doesn't exist
        if agent is None:
            logging.info("Initializing Phone Agent (first time)...")
            agent = PhoneAgent(config)
        else:
            logging.info("Reusing existing agent...")
            # Reset context for new task
            from datetime import datetime
            agent.context['previous_actions'] = []
            agent.context['task_request'] = task
            agent.context['session_id'] = datetime.now().strftime("%Y%m%d_%H%M%S")
            agent.context['screenshots'] = []
        
        # Monkey-patch to capture screenshots
        original_capture = agent.capture_screenshot
        def capture_with_tracking():
            path = original_capture()
            global current_screenshot
            current_screenshot = path
            return path
        
        agent.capture_screenshot = capture_with_tracking
        
        # Execute task
        result = agent.execute_task(task, max_cycles=max_cycles)
        
        if result['success']:
            logging.info(f"✓ Task completed in {result['cycles']} cycles")
        else:
            logging.info(f"⚠️ Task incomplete after {result['cycles']} cycles")
            
    except KeyboardInterrupt:
        logging.info("Task interrupted by user")
    except Exception as e:
        logging.error(f"Task execution error: {e}", exc_info=True)
    finally:
        is_running = False


def start_task(task, max_cycles, config_json):
    """Start a task execution."""
    global is_running, current_config
    
    if is_running:
        return (
            "⚠️ A task is already running",
            None,
            gr.update(active=False)
        )
    
    if not task.strip():
        return (
            "✗ Please enter a task",
            None,
            gr.update(active=False)
        )
    
    try:
        config = json.loads(config_json)
        current_config = config
    except json.JSONDecodeError as e:
        return (
            f"✗ Invalid config JSON: {e}",
            None,
            gr.update(active=False)
        )
    
    try:
        max_cycles = int(max_cycles)
        if max_cycles < 1:
            max_cycles = 15
    except ValueError:
        max_cycles = 15
    
    thread = Thread(target=execute_task_thread, args=(task, max_cycles, config))
    thread.daemon = True
    thread.start()
    
    return (
        "✓ Task started...",
        None,
        gr.update(active=True)
    )


def update_ui():
    """Update UI with latest screenshot and logs."""
    global current_screenshot, log_handler, is_running
    
    screenshot = None
    if current_screenshot and os.path.exists(current_screenshot):
        screenshot = current_screenshot
    
    logs = "\n".join(log_handler.logs) if log_handler else ""
    
    timer_state = gr.update(active=is_running)
    
    return (screenshot, logs, timer_state)


def stop_task():
    """Stop the currently running task."""
    global is_running
    if is_running:
        logging.warning("Task stop requested by user")
        is_running = False
        return "⚠️ Stopping task..."
    return "No task running"


def apply_settings(screen_width, screen_height, temp, max_tok, step_delay, use_fa2, visual_debug):
    """Apply settings changes to config."""
    global current_config
    
    try:
        config = current_config or load_config()
        
        config['screen_width'] = int(screen_width)
        config['screen_height'] = int(screen_height)
        config['temperature'] = float(temp)
        config['max_tokens'] = int(max_tok)
        config['step_delay'] = float(step_delay)
        config['use_flash_attention'] = use_fa2
        config['enable_visual_debug'] = visual_debug
        
        if save_config(config):
            current_config = config
            return "✓ Settings saved", json.dumps(config, indent=2)
        else:
            return "✗ Failed to save settings", json.dumps(config, indent=2)
            
    except ValueError as e:
        return f"✗ Invalid value: {e}", json.dumps(current_config or {}, indent=2)


def auto_detect_resolution():
    """Auto-detect device resolution."""
    width, height, message = detect_device_resolution()
    
    if width and height:
        return width, height, message
    else:
        return 1080, 2340, message


def clear_logs_fn():
    """Clear the log display."""
    if log_handler:
        log_handler.logs.clear()
    return ""


def create_ui():
    """Create the Gradio interface."""
    global current_config
    current_config = load_config()
    
    Path(current_config['screenshot_dir']).mkdir(parents=True, exist_ok=True)
    
    with gr.Blocks(title="Phone Agent Control Panel", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 📱 Phone Agent Control Panel")
        gr.Markdown("*Powered by Qwen3-VL-30B for mobile GUI automation*")
        
        with gr.Tabs():
            with gr.Tab("🎯 Task Control"):
                with gr.Row():
                    with gr.Column(scale=2):
                        task_input = gr.Textbox(
                            label="Task Description",
                            placeholder="e.g., 'Open Chrome and search for weather in New York'",
                            lines=3
                        )
                        
                        with gr.Row():
                            max_cycles = gr.Number(
                                label="Max Cycles",
                                value=15,
                                minimum=1,
                                maximum=50
                            )
                            start_btn = gr.Button("▶️ Start Task", variant="primary", scale=2)
                            stop_btn = gr.Button("⏹️ Stop", variant="stop", scale=1)
                        
                        status_text = gr.Textbox(label="Status", lines=2, interactive=False)
                    
                    with gr.Column(scale=3):
                        image_output = gr.Image(
                            label="Current Screen",
                            type="filepath",
                            height=600
                        )
                
                log_output = gr.Textbox(
                    label="📋 Execution Log",
                    lines=15,
                    max_lines=20,
                    interactive=False,
                    show_copy_button=True
                )
                
                with gr.Row():
                    refresh_btn = gr.Button("🔄 Refresh Display")
                    clear_logs_btn = gr.Button("🗑️ Clear Logs")
            
            with gr.Tab("⚙️ Settings"):
                gr.Markdown("### Device Configuration")
                
                with gr.Row():
                    with gr.Column():
                        detect_btn = gr.Button("🔍 Auto-Detect Device Resolution")
                        detect_status = gr.Textbox(label="Detection Status", interactive=False)
                    
                    with gr.Column():
                        screen_width = gr.Number(
                            label="Screen Width (pixels)",
                            value=current_config['screen_width']
                        )
                        screen_height = gr.Number(
                            label="Screen Height (pixels)",
                            value=current_config['screen_height']
                        )
                
                gr.Markdown("### Model Parameters")
                
                with gr.Row():
                    temperature = gr.Slider(
                        label="Temperature",
                        minimum=0.0,
                        maximum=1.0,
                        value=current_config['temperature'],
                        step=0.05
                    )
                    max_tokens = gr.Number(
                        label="Max Tokens",
                        value=current_config['max_tokens'],
                        minimum=128,
                        maximum=2048
                    )
                
                with gr.Row():
                    step_delay = gr.Slider(
                        label="Step Delay (seconds)",
                        minimum=0.5,
                        maximum=5.0,
                        value=current_config['step_delay'],
                        step=0.1
                    )
                
                gr.Markdown("### Advanced Options")
                
                with gr.Row():
                    use_flash_attn = gr.Checkbox(
                        label="Use Flash Attention 2",
                        value=current_config.get('use_flash_attention', False)
                    )
                    visual_debug = gr.Checkbox(
                        label="Enable Visual Debug",
                        value=current_config.get('enable_visual_debug', False)
                    )
                
                apply_btn = gr.Button("💾 Save Settings", variant="primary")
                settings_status = gr.Textbox(label="Settings Status", interactive=False)
                
                gr.Markdown("### Configuration JSON")
                config_editor = gr.Code(
                    label="Current Configuration",
                    language="json",
                    value=json.dumps(current_config, indent=2),
                    lines=15
                )
            
            with gr.Tab("❓ Help"):
                gr.Markdown("""
## Quick Start

1. **Connect Device**: USB debugging enabled, device connected
2. **Configure Resolution**: Use auto-detect in Settings tab
3. **Run Task**: Enter task description and click Start

## Task Examples
- "Open Chrome"
- "Search for weather on Google"
- "Open Settings and enable WiFi"

## Troubleshooting
- **Wrong taps**: Check screen resolution in Settings
- **No device**: Run `adb devices` in terminal
- **Errors**: Check the Execution Log tab
                """)
        
        timer = gr.Timer(value=3, active=False)
        
        # Event handlers
        start_btn.click(
            fn=start_task,
            inputs=[task_input, max_cycles, config_editor],
            outputs=[status_text, image_output, timer]
        )
        
        stop_btn.click(
            fn=stop_task,
            outputs=status_text
        )
        
        timer.tick(
            fn=update_ui,
            outputs=[image_output, log_output, timer]
        )
        
        refresh_btn.click(
            fn=update_ui,
            outputs=[image_output, log_output, timer]
        )
        
        clear_logs_btn.click(
            fn=clear_logs_fn,
            outputs=log_output
        )
        
        detect_btn.click(
            fn=auto_detect_resolution,
            outputs=[screen_width, screen_height, detect_status]
        )
        
        apply_btn.click(
            fn=apply_settings,
            inputs=[
                screen_width,
                screen_height,
                temperature,
                max_tokens,
                step_delay,
                use_flash_attn,
                visual_debug
            ],
            outputs=[settings_status, config_editor]
        )
    
    return demo


def main():
    """Main entry point for the UI."""
    print("Phone Agent UI Starting...")
    print("Setting up logging...")
    setup_logg
... [TRUNCATED]
```

