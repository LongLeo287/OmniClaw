---
id: kittentts-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:01.246000
---

# KNOWLEDGE EXTRACT: KittenTTS
> **Extracted on:** 2026-03-31 01:42:16
> **Source:** KittenTTS

---

## File: `.gitignore`
```
# General
.DS_Store
__MACOSX/
.AppleDouble
.LSOverride
Icon[
]

# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

.claude/
.venv*

*.wav

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#   Usually these files are written by a python script from a template
#   before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py.cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
# Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
# uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
# poetry.lock
# poetry.toml

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
# pdm.lock
# pdm.toml
.pdm-python
.pdm-build/

# pixi
#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
# pixi.lock
#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# Redis
*.rdb
*.aof
*.pid

# RabbitMQ
mnesia/
rabbitmq/
rabbitmq-data/

# ActiveMQ
activemq-data/

# SageMath parsed files
*.sage.py

# Environments
.env
.envrc
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#   JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#   be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#   and can be added to the global gitignore or merged into this file.  For a more nuclear
#   option (not recommended) you can uncomment the following to ignore the entire idea folder.
# .idea/

# Abstra
#   Abstra is an AI-powered process automation framework.
#   Ignore directories containing user credentials, local state, and settings.
#   Learn more at https://abstra.io/docs
.abstra/

# Visual Studio Code
#   Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore 
#   that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
#   and can be added to the global gitignore or merged into this file. However, if you prefer, 
#   you could uncomment the following to ignore the entire vscode folder
# .vscode/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/

# Streamlit
.streamlit/secrets.toml
```

## File: `example.py`
```python
from kittentts import KittenTTS

# it will run blazing fast on any GPU. But this example will run on CPU.

# Step 1: Load the model
m = KittenTTS("KittenML/kitten-tts-mini-0.8") # 80M version (highest quality)
# m = KittenTTS("KittenML/kitten-tts-micro-0.8") # 40M version (balances speed and quality )
# m = KittenTTS("KittenML/kitten-tts-nano-0.8") # 15M version (tiny and faster )


# Step 2: Generate the audio 

# this is a sample from the TinyStories dataset. 
text ="""One day, a little girl named Lily found a needle in her room. She knew it was difficult to play with it because it was sharp. """


# available_voices : ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']
voice = 'Bruno'



audio = m.generate(text=text, voice=voice )

# Save the audio
import soundfile as sf
sf.write('output.wav', audio, 24000)
print(f"Audio saved to output.wav")
```

## File: `example_cuda.py`
```python
from kittentts import KittenTTS

# This example will runs on GPU.

# Step 1: Load the model
m = KittenTTS("KittenML/kitten-tts-mini-0.8", backend="cuda") # 80M version (highest quality)
# m = KittenTTS("KittenML/kitten-tts-micro-0.8") # 40M version (balances speed and quality )
# m = KittenTTS("KittenML/kitten-tts-nano-0.8") # 15M version (tiny and faster )


# Step 2: Generate the audio 

# this is a sample from the TinyStories dataset. 
text ="""One day, a little girl named Lily found a needle in her room. She knew it was difficult to play with it because it was sharp. """


# available_voices : ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']
voice = 'Bruno'



audio = m.generate(text=text, voice=voice )

# Save the audio
import soundfile as sf
sf.write('output.wav', audio, 24000)
print(f"Audio saved to output.wav")
```

## File: `example_streaming.py`
```python
import numpy as np
import soundfile as sf
from kittentts import KittenTTS

SAMPLE_RATE = 24000

# Step 1: Load the model
m = KittenTTS("KittenML/kitten-tts-mini-0.8")  # 80M version (highest quality)
# m = KittenTTS("KittenML/kitten-tts-mini-0.8", backend="cuda")  # GPU version
# m = KittenTTS("KittenML/kitten-tts-micro-0.8")  # 40M version
# m = KittenTTS("KittenML/kitten-tts-nano-0.8")  # 15M version (tiny and faster)

# Step 2: Define text and voice
text = """One day, a little girl named Lily found a needle in her room. She knew it was difficult to play with it because it was sharp. Lily wanted to use the needle to sew a button on her shirt. She asked her mom for help."""

voice = "Bruno"

# Optional: try to import sounddevice for real-time playback
try:
    import sounddevice as sd
    has_audio = True
except (ImportError, OSError):
    has_audio = False

# Step 3: Stream audio chunk by chunk
print("Streaming audio...")
chunks = []
for i, chunk in enumerate(m.generate_stream(text=text, voice=voice)):
    audio = chunk.squeeze()
    chunks.append(audio)
    print(f"  Chunk {i + 1}: {len(audio)} samples ({len(audio) / SAMPLE_RATE:.2f}s)")
    if has_audio:
        sd.play(audio, samplerate=SAMPLE_RATE)
        sd.wait()

# Save the full audio
full_audio = np.concatenate(chunks)
sf.write("output_streaming.wav", full_audio, SAMPLE_RATE)
print(f"Audio saved to output_streaming.wav ({len(full_audio) / SAMPLE_RATE:.2f}s total)")
```

## File: `LICENSE`
```
                             Apache License
                       Version 2.0, January 2004
                    http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

    Definitions.

    "License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

    "Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

    "Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

    "You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.

    "Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

    "Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

    "Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

    "Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

    "Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."

    "Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

    Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

    Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

    Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

    (a) You must give any other recipients of the Work or Derivative Works a copy of this License; and (b) You must cause any modified files to carry prominent notices stating that You changed the files; and (c) You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and (d) If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License. You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

    Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

    Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

    Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

    Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

    Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS

APPENDIX: How to apply the Apache License to your work.

  To apply the Apache License to your work, attach the following
  boilerplate notice, with the fields enclosed by brackets "[]"
  replaced with your own identifying information. (Don't include
  the brackets!)  The text should be enclosed in the appropriate
  comment syntax for the file format. We also recommend that a
  file or class name and description of purpose be included on the
  same "printed page" as the copyright notice for easier
  identification within third-party archives.

Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
```

## File: `MANIFEST.in`
```
include README.md
include LICENSE
include requirements.txt
recursive-include kittentts *.py
recursive-include kittentts *.json
recursive-include kittentts *.txt
recursive-include kittentts *.onnx
global-exclude __pycache__
global-exclude *.py[co]
```

## File: `pyproject.toml`
```
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "kittentts"
version = "0.8.1"
description = "Ultra-lightweight text-to-speech model with just 15 million parameters"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "Apache 2.0"}
authors = [
    {name = "KittenML"}
]
keywords = ["text-to-speech", "tts", "speech-synthesis", "neural-networks", "onnx"]
classifiers = [
    "Topic :: Multimedia :: Sound/Audio :: Speech",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]
dependencies = [
    "espeakng_loader",
    "phonemizer",
    "onnxruntime",
    "soundfile",
    "numpy",
    "huggingface_hub",
]

[project.urls]
Homepage = "https://github.com/kittenml/kittentts"
Repository = "https://github.com/kittenml/kittentts"
Issues = "https://github.com/kittenml/kittentts/issues"

[tool.setuptools.packages.find]
where = ["."]
include = ["kittentts*"]

[tool.setuptools.package-data]
kittentts = ["*.json", "*.txt", "*.onnx"]
```

## File: `README.md`
```markdown
# Kitten TTS

<p align="center">
  <img width="607" height="255" alt="Kitten TTS" src="https://github.com/user-attachments/assets/f4646722-ba78-4b25-8a65-81bacee0d4f6" />
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/KittenML/KittenTTS-Demo"><img src="https://img.shields.io/badge/Demo-Hugging%20Face%20Spaces-orange" alt="Hugging Face Demo"></a>
  <a href="https://discord.com/invite/VJ86W4SURW"><img src="https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://kittenml.com"><img src="https://img.shields.io/badge/Website-kittenml.com-blue" alt="Website"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-green.svg" alt="License"></a>
</p>

> **New:** Kitten TTS v0.8 is out -- 15M, 40M, and 80M parameter models now available.

Kitten TTS is an open-source, lightweight text-to-speech library built on ONNX. With models ranging from 15M to 80M parameters (25-80 MB on disk), it delivers high-quality voice synthesis on CPU without requiring a GPU.

> **Status:** Developer preview -- APIs may change between releases.

**Commercial support is available.** For integration assistance, custom voices, or enterprise licensing, [contact us](https://docs.google.com/forms/d/e/1FAIpQLSc49erSr7jmh3H2yeqH4oZyRRuXm0ROuQdOgWguTzx6SMdUnQ/viewform?usp=preview).

## Table of Contents

- [Features](#features)
- [Available Models](#available-models)
- [Demo](#demo)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
- [System Requirements](#system-requirements)
- [Roadmap](#roadmap)
- [Commercial Support](#commercial-support)
- [Community and Support](#community-and-support)
- [License](#license)

## Features

- **Ultra-lightweight** -- Model sizes from 25 MB (int8) to 80 MB, suitable for edge deployment
- **CPU-optimized** -- ONNX-based inference runs efficiently without a GPU
- **8 built-in voices** -- Bella, Jasper, Luna, Bruno, Rosie, Hugo, Kiki, and Leo
- **Adjustable speech speed** -- Control playback rate via the `speed` parameter
- **Text preprocessing** -- Built-in pipeline handles numbers, currencies, units, and more
- **24 kHz output** -- High-quality audio at a standard sample rate

## Available Models

| Model | Parameters | Size | Download |
|---|---|---|---|
| kitten-tts-mini | 80M | 80 MB | [KittenML/kitten-tts-mini-0.8](https://huggingface.co/KittenML/kitten-tts-mini-0.8) |
| kitten-tts-micro | 40M | 41 MB | [KittenML/kitten-tts-micro-0.8](https://huggingface.co/KittenML/kitten-tts-micro-0.8) |
| kitten-tts-nano | 15M | 56 MB | [KittenML/kitten-tts-nano-0.8](https://huggingface.co/KittenML/kitten-tts-nano-0.8-fp32) |
| kitten-tts-nano (int8) | 15M | 25 MB | [KittenML/kitten-tts-nano-0.8-int8](https://huggingface.co/KittenML/kitten-tts-nano-0.8-int8) |

> **Note:** Some users have reported issues with the `kitten-tts-nano-0.8-int8` model. If you encounter problems, please [open an issue](https://github.com/KittenML/KittenTTS/issues).

## Demo

https://github.com/user-attachments/assets/d80120f2-c751-407e-a166-068dd1dd9e8d

### Try it online

Try Kitten TTS directly in your browser on [Hugging Face Spaces](https://huggingface.co/spaces/KittenML/KittenTTS-Demo).

## Quick Start

### Prerequisites

- Python 3.8 or later
- pip

### Installation

```bash
pip install https://github.com/KittenML/KittenTTS/releases/download/0.8.1/kittentts-0.8.1-py3-none-any.whl
```

### Basic Usage

```python
from kittentts import KittenTTS

model = KittenTTS("KittenML/kitten-tts-mini-0.8")
audio = model.generate("This high-quality TTS model runs without a GPU.", voice="Jasper")

import soundfile as sf
sf.write("output.wav", audio, 24000)
```

### Advanced Usage

```python
# Adjust speech speed (default: 1.0)
audio = model.generate("Hello, world.", voice="Luna", speed=1.2)

# Save directly to a file
model.generate_to_file("Hello, world.", "output.wav", voice="Bruno", speed=0.9)

# List available voices
print(model.available_voices)
# ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']
```

### Using with GPU

```
pip install -r requirements_gpu.txt
```

```python
m = KittenTTS("KittenML/kitten-tts-mini-0.8", backend="cuda")
```

Check out `example_cuda.py` 

## API Reference

### `KittenTTS(model_name, cache_dir=None)`

Load a model from Hugging Face Hub.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `model_name` | `str` | `"KittenML/kitten-tts-nano-0.8"` | Hugging Face repository ID |
| `cache_dir` | `str` | `None` | Local directory for caching downloaded model files |

### `model.generate(text, voice, speed, clean_text)`

Synthesize speech from text, returning a NumPy array of audio samples at 24 kHz.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `text` | `str` | -- | Input text to synthesize |
| `voice` | `str` | `"expr-voice-5-m"` | Voice name (see available voices) |
| `speed` | `float` | `1.0` | Speech speed multiplier |
| `clean_text` | `bool` | `False` | Preprocess text (expand numbers, currencies, etc.) |

### `model.generate_to_file(text, output_path, voice, speed, sample_rate, clean_text)`

Synthesize speech and write directly to an audio file.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `text` | `str` | -- | Input text to synthesize |
| `output_path` | `str` | -- | Path to save the audio file |
| `voice` | `str` | `"expr-voice-5-m"` | Voice name |
| `speed` | `float` | `1.0` | Speech speed multiplier |
| `sample_rate` | `int` | `24000` | Audio sample rate in Hz |
| `clean_text` | `bool` | `True` | Preprocess text (expand numbers, currencies, etc.) |

### `model.available_voices`

Returns a list of available voice names: `['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']`

## System Requirements

- **Operating system:** Linux, macOS, or Windows
- **Python:** 3.8 or later
- **Hardware:** Runs on CPU; no GPU required
- **Disk space:** 25-80 MB depending on model variant

A virtual environment (conda, venv, or similar) is recommended to avoid dependency conflicts.

## Roadmap

- [ ] Release optimized inference engine
- [ ] Release mobile SDK
- [ ] Release higher quality TTS models
- [ ] Release multilingual TTS
- [ ] Release KittenASR
- [ ] Need anything else? [Let us know](https://github.com/KittenML/KittenTTS/issues)

## Commercial Support

We offer commercial support for teams integrating Kitten TTS into their products. This includes integration assistance, custom voice development, and enterprise licensing.

[Contact us](https://docs.google.com/forms/d/e/1FAIpQLSc49erSr7jmh3H2yeqH4oZyRRuXm0ROuQdOgWguTzx6SMdUnQ/viewform?usp=preview) or email info@stellonlabs.com to discuss your requirements.

## Community and Support

- **Discord:** [Join the community](https://discord.com/invite/VJ86W4SURW)
- **Website:** [kittenml.com](https://kittenml.com)
- **Custom support:** [Request form](https://docs.google.com/forms/d/e/1FAIpQLSc49erSr7jmh3H2yeqH4oZyRRuXm0ROuQdOgWguTzx6SMdUnQ/viewform?usp=preview)
- **Email:** info@stellonlabs.com
- **Issues:** [GitHub Issues](https://github.com/KittenML/KittenTTS/issues)

## License

This project is licensed under the [Apache License 2.0](LICENSE).
```

## File: `requirements.txt`
```
espeakng_loader
phonemizer
onnxruntime
soundfile
numpy
huggingface_hub
```

## File: `requirements_gpu.txt`
```
espeakng_loader
phonemizer
onnxruntime-gpu
soundfile
numpy
huggingface_hub
nvidia-cublas-cu12                                             
nvidia-cudnn-cu12                                                                                                                                                                    
nvidia-cuda-runtime-cu12                                       
nvidia-curand-cu12                                                                                                                                                                   
nvidia-cufft-cu12 
nvidia-cusolver-cu12                                                                                                                                                                 
nvidia-cusparse-cu12                                           
nvidia-nvjitlink-cu12
```

## File: `setup.py`
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kittentts",
    version="0.8.1",
    author="KittenML",
    author_email="",
    description="Ultra-lightweight text-to-speech model with just 15 million parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kittenml/kittentts",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "espeakng_loader",
        "phonemizer",
        "onnxruntime",
        "soundfile",
        "numpy",
        "huggingface_hub",
    ],
    keywords="text-to-speech, tts, speech-synthesis, neural-networks, onnx",
    project_urls={
        "Bug Reports": "https://github.com/kittenml/kittentts/issues",
        "Source": "https://github.com/kittenml/kittentts",
    },
)
```

## File: `kittentts/get_model.py`
```python
import json
import os
from huggingface_hub import hf_hub_download
from .onnx_model import KittenTTS_1_Onnx


class KittenTTS:
    """Main KittenTTS class for text-to-speech synthesis."""
    
    def __init__(self, model_name="KittenML/kitten-tts-nano-0.8", cache_dir=None, backend=None):
        """Initialize KittenTTS with a model from Hugging Face.
        
        Args:
            model_name: Hugging Face repository ID or model name
            cache_dir: Directory to cache downloaded files
        """
        # Handle different model name formats
        if "/" not in model_name:
            # If just model name provided, assume it's from KittenML
            repo_id = f"KittenML/{model_name}"
        else:
            repo_id = model_name
            
        self.model = download_from_huggingface(repo_id=repo_id, cache_dir=cache_dir, backend=backend)
    
    def generate(self, text, voice="expr-voice-5-m", speed=1.0, clean_text=False):
        """Generate audio from text.
        
        Args:
            text: Input text to synthesize
            voice: Voice to use for synthesis
            speed: Speech speed (1.0 = normal)
            
        Returns:
            Audio data as numpy array
        """
        print(f"Generating audio for text: {text}")
        return self.model.generate(text, voice=voice, speed=speed, clean_text=clean_text)

    def generate_stream(self, text, voice="expr-voice-5-m", speed=1.0, clean_text=False):
        """Generate audio as a stream of chunks.

        Yields:
            numpy.ndarray: Audio data for each text chunk.
        """
        yield from self.model.generate_stream(text, voice=voice, speed=speed, clean_text=clean_text)

    def generate_to_file(self, text, output_path, voice="expr-voice-5-m", speed=1.0, sample_rate=24000):
        """Generate audio from text and save to file.
        
        Args:
            text: Input text to synthesize
            output_path: Path to save the audio file
            voice: Voice to use for synthesis
            speed: Speech speed (1.0 = normal)
            sample_rate: Audio sample rate
        """
        return self.model.generate_to_file(text, output_path, voice=voice, speed=speed, sample_rate=sample_rate)
    
    @property
    def available_voices(self):
        """Get list of available voices."""
        return self.model.all_voice_names


def download_from_huggingface(repo_id="KittenML/kitten-tts-nano-0.1", cache_dir=None, backend=None):
    """Download model files from Hugging Face repository.
    
    Args:
        repo_id: Hugging Face repository ID
        cache_dir: Directory to cache downloaded files
        
    Returns:
        KittenTTS_1_Onnx: Instantiated model ready for use
    """
    # Download config file first
    config_path = hf_hub_download(
        repo_id=repo_id,
        filename="config.json",
        cache_dir=cache_dir
    )
    
    # Load config
    with open(config_path, 'r') as f:
        config = json.load(f)

    if config.get("type") not in ["ONNX1", "ONNX2"]:
        raise ValueError("Unsupported model type.")

    # Download model and voices files based on config
    model_path = hf_hub_download(
        repo_id=repo_id,
        filename=config["model_file"],
        cache_dir=cache_dir
    )
    
    voices_path = hf_hub_download(
        repo_id=repo_id,
        filename=config["voices"],
        cache_dir=cache_dir
    )
    
    # Instantiate and return model
    model = KittenTTS_1_Onnx(model_path=model_path, voices_path=voices_path, speed_priors=config.get("speed_priors", {}) , voice_aliases=config.get("voice_aliases", {}), backend=backend)
    
    return model


def get_model(repo_id="KittenML/kitten-tts-nano-0.1", cache_dir=None, backend=None):
    """Get a KittenTTS model (legacy function for backward compatibility)."""
    return KittenTTS(repo_id, cache_dir, backend=backend)
```

## File: `kittentts/onnx_model.py`
```python
import os
import espeakng_loader
from phonemizer.backend.espeak.wrapper import EspeakWrapper
EspeakWrapper.set_library(espeakng_loader.get_library_path())
os.environ['ESPEAK_DATA_PATH'] = espeakng_loader.get_data_path()
import numpy as np
import phonemizer
import soundfile as sf
import onnxruntime as ort
from .preprocess import TextPreprocessor

def basic_english_tokenize(text):
    """Basic English tokenizer that splits on whitespace and punctuation."""
    import re
    tokens = re.findall(r"\w+|[^\w\s]", text)
    return tokens

def ensure_punctuation(text):
    """Ensure text ends with punctuation. If not, add a comma."""
    text = text.strip()
    if not text:
        return text
    if text[-1] not in '.!?,;:':
        text = text + ','
    return text


def chunk_text(text, max_len=400):
    """Split text into chunks for processing long texts."""
    import re
    
    sentences = re.split(r'[.!?]+', text)
    chunks = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        
        if len(sentence) <= max_len:
            chunks.append(ensure_punctuation(sentence))
        else:
            # Split long sentences by words
            words = sentence.split()
            temp_chunk = ""
            for word in words:
                if len(temp_chunk) + len(word) + 1 <= max_len:
                    temp_chunk += " " + word if temp_chunk else word
                else:
                    if temp_chunk:
                        chunks.append(ensure_punctuation(temp_chunk.strip()))
                    temp_chunk = word
            if temp_chunk:
                chunks.append(ensure_punctuation(temp_chunk.strip()))
    
    return chunks


class TextCleaner:
    def __init__(self, dummy=None):
        _pad = "$"
        _punctuation = ';:,.!?¡¿—…"«»"" '
        _letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        _letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"

        symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)
        
        dicts = {}
        for i in range(len(symbols)):
            dicts[symbols[i]] = i

        self.word_index_dictionary = dicts

    def __call__(self, text):
        indexes = []
        for char in text:
            try:
                indexes.append(self.word_index_dictionary[char])
            except KeyError:
                pass
        return indexes


class KittenTTS_1_Onnx:
    def __init__(self, model_path="kitten_tts_nano_preview.onnx", voices_path="voices.npz", speed_priors={}, voice_aliases={}, backend=None):
        """Initialize KittenTTS with model and voice data.
        
        Args:
            model_path: Path to the ONNX model file
            voices_path: Path to the voices NPZ file
        """
        self.model_path = model_path
        self.voices = np.load(voices_path) 
        providers = []
        if backend == "cuda":
            providers = ["CUDAExecutionProvider"]
        elif backend == "amd_gpu":
            providers = ["ROCMExecutionProvider"]
        elif backend == "cpu":
            providers = ["CPUExecutionProvider"]
        elif backend is None:
            providers = []
        else:
            raise ValueError("Unsupported backend")
        
        self.session = ort.InferenceSession(model_path, providers=providers)
        
        self.phonemizer = phonemizer.backend.EspeakBackend(
            language="en-us", preserve_punctuation=True, with_stress=True
        )
        self.text_cleaner = TextCleaner()
        self.speed_priors = speed_priors
        
        # Available voices
        self.available_voices = [
            'expr-voice-2-m', 'expr-voice-2-f', 'expr-voice-3-m', 'expr-voice-3-f', 
            'expr-voice-4-m', 'expr-voice-4-f', 'expr-voice-5-m', 'expr-voice-5-f'
        ]
        self.all_voice_names = ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']
        self.voice_aliases = voice_aliases

        self.preprocessor = TextPreprocessor(remove_punctuation=False)
    
    def _prepare_inputs(self, text: str, voice: str, speed: float = 1.0) -> dict:
        """Prepare ONNX model inputs from text and voice parameters."""
        if voice in self.voice_aliases:
            voice = self.voice_aliases[voice]

        if voice not in self.available_voices:
            raise ValueError(f"Voice '{voice}' not available. Choose from: {self.available_voices}")
        
        if voice in self.speed_priors:
            speed = speed * self.speed_priors[voice]
        
        # Phonemize the input text
        phonemes_list = self.phonemizer.phonemize([text])
        
        # Process phonemes to get token IDs
        phonemes = basic_english_tokenize(phonemes_list[0])
        phonemes = ' '.join(phonemes)
        tokens = self.text_cleaner(phonemes)
        
        # Add start and end tokens
        tokens.insert(0, 0)
        tokens.append(10)
        tokens.append(0)
        
        input_ids = np.array([tokens], dtype=np.int64)
        ref_id =  min(len(text), self.voices[voice].shape[0] - 1)
        ref_s = self.voices[voice][ref_id:ref_id+1]
        
        return {
            "input_ids": input_ids,
            "style": ref_s,
            "speed": np.array([speed], dtype=np.float32),
        }
    
    def generate(self, text: str, voice: str = "expr-voice-5-m", speed: float = 1.0, clean_text: bool=True) -> np.ndarray:
        out_chunks = []
        if clean_text:
            text = self.preprocessor(text)
        for text_chunk in chunk_text(text):
            out_chunks.append(self.generate_single_chunk(text_chunk, voice, speed))
        return np.concatenate(out_chunks, axis=-1)

    def generate_stream(self, text: str, voice: str = "expr-voice-5-m", speed: float = 1.0, clean_text: bool = True):
        """Generate audio chunk-by-chunk as a generator.

        Yields:
            numpy.ndarray: Audio data for each text chunk.
        """
        if clean_text:
            text = self.preprocessor(text)
        for text_chunk in chunk_text(text):
            yield self.generate_single_chunk(text_chunk, voice, speed)

    def generate_single_chunk(self, text: str, voice: str = "expr-voice-5-m", speed: float = 1.0) -> np.ndarray:
        """Synthesize speech from text.
        
        Args:
            text: Input text to synthesize
            voice: Voice to use for synthesis
            speed: Speech speed (1.0 = normal)
            
        Returns:
            Audio data as numpy array
        """
        onnx_inputs = self._prepare_inputs(text, voice, speed)
        
        outputs = self.session.run(None, onnx_inputs)
        
        # Trim audio
        audio = outputs[0][..., :-5000]

        return audio
    
    def generate_to_file(self, text: str, output_path: str, voice: str = "expr-voice-5-m", 
                          speed: float = 1.0, sample_rate: int = 24000, clean_text: bool=True) -> None:
        """Synthesize speech and save to file.
        
        Args:
            text: Input text to synthesize
            output_path: Path to save the audio file
            voice: Voice to use for synthesis
            speed: Speech speed (1.0 = normal)
            sample_rate: Audio sample rate
            clean_text: If true, it will cleanup the text. Eg. replace numbers with words.
        """
        audio = self.generate(text, voice, speed, clean_text=clean_text)
        sf.write(output_path, audio, sample_rate)
        print(f"Audio saved to {output_path}")

```

## File: `kittentts/preprocess.py`
```python
"""
text_preprocessing.py
A comprehensive text preprocessing library for NLP pipelines.
"""

import re
import unicodedata
from typing import Optional


# ─────────────────────────────────────────────
# Number → Words conversion
# ─────────────────────────────────────────────

_ONES = [
    "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen",
]
_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
_SCALE = ["", "thousand", "million", "billion", "trillion"]

_ORDINAL_EXCEPTIONS = {
    "one": "first", "two": "second", "three": "third", "four": "fourth",
    "five": "fifth", "six": "sixth", "seven": "seventh", "eight": "eighth",
    "nine": "ninth", "twelve": "twelfth",
}

_CURRENCY_SYMBOLS = {
    "$": "dollar", "€": "euro", "£": "pound", "¥": "yen",
    "₹": "rupee", "₩": "won", "₿": "bitcoin",
}

_ROMAN = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
    (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I"),
]
_RE_ROMAN = re.compile(
    r"\b(M{0,4})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b"
)


def _three_digits_to_words(n: int) -> str:
    """Convert a number 0–999 to English words."""
    if n == 0:
        return ""
    parts = []
    hundreds = n // 100
    remainder = n % 100
    if hundreds:
        parts.append(f"{_ONES[hundreds]} hundred")
    if remainder < 20:
        if remainder:
            parts.append(_ONES[remainder])
    else:
        tens_word = _TENS[remainder // 10]
        ones_word = _ONES[remainder % 10]
        parts.append(f"{tens_word}-{ones_word}" if ones_word else tens_word)
    return " ".join(parts)


def number_to_words(n: int) -> str:
    """
    Convert an integer to its English word representation.

    Examples:
        1200      → "twelve hundred"
        1000      → "one thousand"
        1_000_000 → "one million"
        -42       → "negative forty-two"
        0         → "zero"
    """
    if not isinstance(n, int):
        n = int(n)
    if n == 0:
        return "zero"
    if n < 0:
        return f"negative {number_to_words(-n)}"

    # X00–X999 read as "X hundred" (e.g. 1200 → "twelve hundred")
    # Exclude exact multiples of 1000 (1000 → "one thousand", not "ten hundred")
    if 100 <= n <= 9999 and n % 100 == 0 and n % 1000 != 0:
        hundreds = n // 100
        if hundreds < 20:
            return f"{_ONES[hundreds]} hundred"

    parts = []
    for i, scale in enumerate(_SCALE):
        chunk = n % 1000
        if chunk:
            chunk_words = _three_digits_to_words(chunk)
            parts.append(f"{chunk_words} {scale}".strip() if scale else chunk_words)
        n //= 1000
        if n == 0:
            break

    return " ".join(reversed(parts))


def float_to_words(value, decimal_sep: str = "point") -> str:
    """
    Convert a float (or numeric string) to words, reading decimal digits individually.
    Accepts a string to preserve trailing zeros (e.g. "1.50" → "one point five zero").

    Examples:
        3.14   → "three point one four"
        -0.5   → "negative zero point five"
        "3.10" → "three point one zero"
        1.007  → "one point zero zero seven"
    """
    text = value if isinstance(value, str) else f"{value}"
    negative = text.startswith("-")
    if negative:
        text = text[1:]

    if "." in text:
        int_part, dec_part = text.split(".", 1)
        int_words = number_to_words(int(int_part)) if int_part else "zero"
        # Read each decimal digit individually; "0" → "zero"
        digit_map = ["zero"] + _ONES[1:]  # index 0 → "zero"
        dec_words = " ".join(digit_map[int(d)] for d in dec_part)
        result = f"{int_words} {decimal_sep} {dec_words}"
    else:
        result = number_to_words(int(text))

    return f"negative {result}" if negative else result


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string to an integer."""
    val = {"I": 1, "V": 5, "X": 10, "L": 50,
           "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = 0
    for ch in reversed(s.upper()):
        curr = val[ch]
        result += curr if curr >= prev else -curr
        prev = curr
    return result


# ─────────────────────────────────────────────
# Regex patterns
# ─────────────────────────────────────────────

_RE_URL      = re.compile(r"https?://\S+|www\.\S+")
_RE_EMAIL    = re.compile(r"\b[\w.+-]+@[\w-]+\.[a-z]{2,}\b", re.IGNORECASE)
_RE_HASHTAG  = re.compile(r"#\w+")
_RE_MENTION  = re.compile(r"@\w+")
_RE_HTML     = re.compile(r"<[^>]+>")
_RE_PUNCT    = re.compile(r"[^\w\s.,?!;:\-\u2014\u2013\u2026]")
_RE_SPACES   = re.compile(r"\s+")

# Number: do NOT match a leading minus if it is immediately preceded by a letter
# (handles "gpt-3", "gpl-3", "v-2" etc.)
_RE_NUMBER   = re.compile(r"(?<![a-zA-Z])-?[\d,]+(?:\.\d+)?")

# Ordinals: 1st, 2nd, 3rd, 4th … 21st, 101st …
_RE_ORDINAL  = re.compile(r"\b(\d+)(st|nd|rd|th)\b", re.IGNORECASE)

# Percentages: 50%, 3.5%
_RE_PERCENT  = re.compile(r"(-?[\d,]+(?:\.\d+)?)\s*%")

# Currency: $100, €1,200.50, £50, $85K, $2.5M (optional scale suffix)
_RE_CURRENCY = re.compile(r"([$€£¥₹₩₿])\s*([\d,]+(?:\.\d+)?)\s*([KMBT])?(?![a-zA-Z\d])")

# Time: 3:30pm, 14:00, 3:30 AM — requires 2-digit minutes so "3:0" (score) doesn't match
_RE_TIME     = re.compile(r"\b(\d{1,2}):(\d{2})(?::(\d{2}))?\s*(am|pm)?\b", re.IGNORECASE)

# Ranges: 10-20, 100-200 (both sides numeric, hyphen between them)
_RE_RANGE    = re.compile(r"(?<!\w)(\d+)-(\d+)(?!\w)")

# Version/model names: gpt-3, gpt-3.5, v2.0, Python-3.10, GPL-3
# Letter(s) + hyphen + digit(s) [+ more version parts]
_RE_MODEL_VER = re.compile(r"\b([a-zA-Z][a-zA-Z0-9]*)-(\d[\d.]*)(?=[^\d.]|$)")

# Measurement units glued to numbers: 100km, 50kg, 25°C, 5GB
_RE_UNIT     = re.compile(r"(\d+(?:\.\d+)?)\s*(km|kg|mg|ml|gb|mb|kb|tb|hz|khz|mhz|ghz|mph|kph|°[cCfF]|[cCfF]°|ms|ns|µs)\b",
                          re.IGNORECASE)

# Scale suffixes (uppercase only to avoid ambiguity): 7B, 340M, 1.5K, 2T
# Must NOT be preceded by a letter (so 'MB' is handled by unit regex first)
_RE_SCALE    = re.compile(r"(?<![a-zA-Z])(\d+(?:\.\d+)?)\s*([KMBT])(?![a-zA-Z\d])")

# Scientific notation: 1e-4, 2.5e10, 6.022E23
_RE_SCI      = re.compile(r"(?<![a-zA-Z\d])(-?\d+(?:\.\d+)?)[eE]([+-]?\d+)(?![a-zA-Z\d])")

# Fractions: 1/2, 3/4, 2/3
_RE_FRACTION = re.compile(r"\b(\d+)\s*/\s*(\d+)\b")

# Decades: 80s, 90s, 1980s, 2020s (number ending in 0 followed by 's')
_RE_DECADE   = re.compile(r"\b(\d{1,3})0s\b")

# Leading decimal (no digit before the dot): .5, .75
_RE_LEAD_DEC = re.compile(r"(?<!\d)\.([\d])")


# ─────────────────────────────────────────────
# Expansion helpers
# ─────────────────────────────────────────────

def _ordinal_suffix(n: int) -> str:
    """Return the ordinal word for n (e.g. 1 → 'first', 5 → 'fifth', 21 → 'twenty-first')."""
    word = number_to_words(n)
    # For hyphenated compounds like "twenty-one", convert only the last part
    if "-" in word:
        prefix, last = word.rsplit("-", 1)
        joiner = "-"
    else:
        parts = word.rsplit(" ", 1)
        prefix, last, joiner = (parts[0], parts[1], " ") if len(parts) == 2 else ("", parts[0], "")

    # Check exception table
    for base, ordinal in _ORDINAL_EXCEPTIONS.items():
        if last == base:
            last_ord = ordinal
            break
    else:
        # General rule
        if last.endswith("t"):
            last_ord = last + "h"
        elif last.endswith("e"):
            last_ord = last[:-1] + "th"
        else:
            last_ord = last + "th"

    return f"{prefix}{joiner}{last_ord}" if prefix else last_ord


def expand_ordinals(text: str) -> str:
    """
    Convert ordinal numbers to words.

    Examples:
        "1st place"  → "first place"
        "2nd floor"  → "second floor"
        "3rd base"   → "third base"
        "21st century" → "twenty-first century"
        "100th day"  → "one hundredth day"
    """
    def _replace(m: re.Match) -> str:
        return _ordinal_suffix(int(m.group(1)))
    return _RE_ORDINAL.sub(_replace, text)


def expand_percentages(text: str) -> str:
    """
    Expand percentage expressions.

    Examples:
        "50% off"    → "fifty percent off"
        "3.5% rate"  → "three point five percent rate"
        "-2% change" → "negative two percent change"
    """
    def _replace(m: re.Match) -> str:
        raw = m.group(1).replace(",", "")
        if "." in raw:
            return float_to_words(float(raw)) + " percent"
        return number_to_words(int(raw)) + " percent"
    return _RE_PERCENT.sub(_replace, text)


def expand_currency(text: str) -> str:
    """
    Expand currency amounts, including optional scale suffixes.

    Examples:
        "$100"      → "one hundred dollars"
        "€1,200.50" → "twelve hundred euros and fifty cents"
        "£9.99"     → "nine pounds and ninety-nine cents"
        "$85K"      → "eighty five thousand dollars"
        "$2.5M"     → "two point five million dollars"
    """
    _scale_map = {"K": "thousand", "M": "million", "B": "billion", "T": "trillion"}

    def _replace(m: re.Match) -> str:
        symbol = m.group(1)
        raw = m.group(2).replace(",", "")
        scale_suffix = m.group(3)          # e.g. "K", "M", or None
        unit = _CURRENCY_SYMBOLS.get(symbol, "")

        if scale_suffix:
            # e.g. $85K → "eighty five thousand dollars"
            scale_word = _scale_map[scale_suffix]
            num = float_to_words(raw) if "." in raw else number_to_words(int(raw))
            return f"{num} {scale_word} {unit}{'s' if unit else ''}".strip()

        if "." in raw:
            int_part, dec_part = raw.split(".", 1)
            dec_val = int(dec_part[:2].ljust(2, "0"))
            int_words = number_to_words(int(int_part))
            result = f"{int_words} {unit}s" if unit else int_words
            if dec_val:
                cents = number_to_words(dec_val)
                result += f" and {cents} cent{'s' if dec_val != 1 else ''}"
        else:
            val = int(raw)
            words = number_to_words(val)
            result = f"{words} {unit}{'s' if val != 1 and unit else ''}" if unit else words
        return result

    return _RE_CURRENCY.sub(_replace, text)


def expand_time(text: str) -> str:
    """
    Expand time expressions.

    Examples:
        "3:30pm"  → "three thirty pm"
        "14:00"   → "fourteen hundred"
        "9:05 AM" → "nine oh five am"
        "12:00pm" → "twelve pm"
    """
    def _replace(m: re.Match) -> str:
        h = int(m.group(1))
        mins = int(m.group(2))
        suffix = (" " + m.group(4).lower()) if m.group(4) else ""
        h_words = number_to_words(h)
        if mins == 0:
            return f"{h_words} hundred{suffix}" if not m.group(4) else f"{h_words}{suffix}"
        elif mins < 10:
            return f"{h_words} oh {number_to_words(mins)}{suffix}"
        else:
            return f"{h_words} {number_to_words(mins)}{suffix}"
    return _RE_TIME.sub(_replace, text)


def expand_ranges(text: str) -> str:
    """
    Expand numeric ranges.

    Examples:
        "10-20 items"   → "ten to twenty items"
        "pages 100-200" → "pages one hundred to two hundred"
        "2020-2024"     → "twenty twenty to twenty twenty-four"
    """
    def _replace(m: re.Match) -> str:
        lo = number_to_words(int(m.group(1)))
        hi = number_to_words(int(m.group(2)))
        return f"{lo} to {hi}"
    return _RE_RANGE.sub(_replace, text)


def expand_model_names(text: str) -> str:
    """
    Normalise version/model names that use letter-hyphen-number patterns,
    so the number is not misread as negative.

    Examples:
        "GPT-3"      → "GPT 3"
        "gpt-3.5"    → "gpt 3.5"
        "GPL-3"      → "GPL 3"
        "Python-3.10"→ "Python 3.10"
        "v2.0"       stays as "v2.0" (no hyphen — handled by number replacement)
        "IPv6"       stays as "IPv6"
    """
    return _RE_MODEL_VER.sub(lambda m: f"{m.group(1)} {m.group(2)}", text)


def expand_units(text: str) -> str:
    """
    Expand common measurement units glued to numbers.

    Examples:
        "100km"  → "one hundred kilometers"
        "50kg"   → "fifty kilograms"
        "25°C"   → "twenty-five degrees Celsius"
        "5GB"    → "five gigabytes"
    """
    _unit_map = {
        "km": "kilometers", "kg": "kilograms", "mg": "milligrams",
        "ml": "milliliters", "gb": "gigabytes", "mb": "megabytes",
        "kb": "kilobytes", "tb": "terabytes",
        "hz": "hertz", "khz": "kilohertz", "mhz": "megahertz", "ghz": "gigahertz",
        "mph": "miles per hour", "kph": "kilometers per hour",
        "ms": "milliseconds", "ns": "nanoseconds", "µs": "microseconds",
        "°c": "degrees Celsius", "c°": "degrees Celsius",
        "°f": "degrees Fahrenheit", "f°": "degrees Fahrenheit",
    }
    def _replace(m: re.Match) -> str:
        raw = m.group(1)
        unit = m.group(2).lower()
        expanded = _unit_map.get(unit, m.group(2))
        num = float_to_words(float(raw)) if "." in raw else number_to_words(int(raw))
        return f"{num} {expanded}"
    return _RE_UNIT.sub(_replace, text)


def expand_roman_numerals(text: str, context_words: bool = True) -> str:
    """
    Expand Roman numerals that appear as standalone tokens (optionally
    only when preceded by a title-like word to avoid false positives).

    Examples:
        "World War II"     → "World War two"
        "Chapter IV"       → "Chapter four"
        "Louis XIV"        → "Louis fourteen"
        "mix I with V"     → left unchanged (ambiguous single letters)
    """
    _TITLE_WORDS = re.compile(
        r"\b(war|chapter|part|volume|act|scene|book|section|article|"
        r"king|queen|pope|louis|henry|edward|george|william|james|"
        r"phase|round|level|stage|class|type|version|episode|season)\b",
        re.IGNORECASE,
    )

    def _replace(m: re.Match) -> str:
        roman = m.group(0)
        if not roman.strip():
            return roman
        # Skip single ambiguous letters (I, V, X) unless context present
        if len(roman) == 1 and roman in "IVX":
            # Only expand if preceded by a title word
            start = m.start()
            preceding = text[max(0, start - 30): start]
            if not _TITLE_WORDS.search(preceding):
                return roman
        try:
            val = roman_to_int(roman)
            if val == 0:
                return roman
            return number_to_words(val)
        except Exception:
            return roman

    return _RE_ROMAN.sub(_replace, text)


def normalize_leading_decimals(text: str) -> str:
    """
    Normalise bare leading-decimal floats so the number pipeline handles them.

    Examples:
        ".5 teaspoons" → "0.5 teaspoons"
        "-.25 adjustment" → "-0.25 adjustment"
    """
    # Handle -.5 → -0.5 and .5 → 0.5
    text = re.sub(r"(?<!\d)(-)\.([\d])", r"\g<1>0.\2", text)
    return _RE_LEAD_DEC.sub(r"0.\1", text)


def expand_scientific_notation(text: str) -> str:
    """
    Expand scientific-notation numbers to spoken form.

    Examples:
        "1e-4"    → "one times ten to the negative four"
        "2.5e10"  → "two point five times ten to the ten"
        "6.022E23"→ "six point zero two two times ten to the twenty three"
    """
    def _replace(m: re.Match) -> str:
        coeff_raw = m.group(1)
        exp = int(m.group(2))
        coeff_words = float_to_words(coeff_raw) if "." in coeff_raw else number_to_words(int(coeff_raw))
        exp_words = number_to_words(abs(exp))
        sign = "negative " if exp < 0 else ""
        return f"{coeff_words} times ten to the {sign}{exp_words}"
    return _RE_SCI.sub(_replace, text)


def expand_scale_suffixes(text: str) -> str:
    """
    Expand standalone uppercase scale suffixes attached to numbers.

    Examples:
        "7B parameters" → "seven billion parameters"
        "340M model"    → "three hundred forty million model"
        "1.5K salary"   → "one point five thousand salary"
        "$100K budget"  → "$100K budget"  (currency handled upstream)
    """
    _map = {"K": "thousand", "M": "million", "B": "billion", "T": "trillion"}

    def _replace(m: re.Match) -> str:
        raw = m.group(1)
        suffix = m.group(2)
        scale_word = _map.get(suffix, suffix)
        num = float_to_words(raw) if "." in raw else number_to_words(int(raw))
        return f"{num} {scale_word}"

    return _RE_SCALE.sub(_replace, text)


def expand_fractions(text: str) -> str:
    """
    Expand simple numeric fractions.

    Examples:
        "1/2 cup"  → "one half cup"
        "3/4 mile" → "three quarters mile"
        "2/3 done" → "two thirds done"
        "5/8 inch" → "five eighths inch"
    """
    def _replace(m: re.Match) -> str:
        num = int(m.group(1))
        den = int(m.group(2))
        if den == 0:
            return m.group()
        num_words = number_to_words(num)
        if den == 2:
            denom_word = "half" if num == 1 else "halves"
        elif den == 4:
            denom_word = "quarter" if num == 1 else "quarters"
        else:
            denom_word = _ordinal_suffix(den)
            if num != 1:
                denom_word += "s"
        return f"{num_words} {denom_word}"

    return _RE_FRACTION.sub(_replace, text)


def expand_decades(text: str) -> str:
    """
    Expand decade expressions to words.

    Examples:
        "the 80s"    → "the eighties"
        "the 1980s"  → "the nineteen eighties"
        "the 2020s"  → "the twenty twenties"
        "'90s music" → "nineties music"
    """
    _decade_map = {
        0: "hundreds", 1: "tens", 2: "twenties", 3: "thirties", 4: "forties",
        5: "fifties", 6: "sixties", 7: "seventies", 8: "eighties", 9: "nineties",
    }

    def _replace(m: re.Match) -> str:
        base = int(m.group(1))          # e.g. 8 for "80s", 198 for "1980s"
        decade_digit = base % 10
        decade_word = _decade_map.get(decade_digit, "")
        if base < 10:
            return decade_word
        century_part = base // 10       # e.g. 19 for 198
        return f"{number_to_words(century_part)} {decade_word}"

    return _RE_DECADE.sub(_replace, text)


def expand_ip_addresses(text: str) -> str:
    """
    Expand IPv4 addresses to spoken digits per octet.

    Examples:
        "192.168.1.1"  → "one nine two dot one six eight dot one dot one"
        "10.0.0.1"     → "one zero dot zero dot zero dot one"
    """
    _d = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
          "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

    def _octet(s: str) -> str:
        return " ".join(_d[c] for c in s)

    def _replace(m: re.Match) -> str:
        return " dot ".join(_octet(g) for g in m.groups())

    return re.sub(r"\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b", _replace, text)


def expand_phone_numbers(text: str) -> str:
    """
    Expand US phone numbers to spoken digits before range expansion claims the hyphens.

    Examples:
        "555-1234"       → "five five five one two three four"
        "555-123-4567"   → "five five five one two three four five six seven"
        "1-800-555-0199" → "one eight zero zero five five five zero one nine nine"
    """
    _d = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
          "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

    def _digits(s: str) -> str:
        return " ".join(_d[c] for c in s)

    def _join(*groups) -> str:
        return " ".join(_digits(g) for g in groups)

    # Match longest pattern first to avoid partial matches
    # 11-digit: 1-800-555-0199
    text = re.sub(r"(?<!\d-)(?<!\d)\b(\d{1,2})-(\d{3})-(\d{3})-(\d{4})\b(?!-\d)",
                  lambda m: _join(*m.groups()), text)
    # 10-digit: 555-123-4567
    text = re.sub(r"(?<!\d-)(?<!\d)\b(\d{3})-(\d{3})-(\d{4})\b(?!-\d)",
                  lambda m: _join(*m.groups()), text)
    # 7-digit local: 555-1234 (not preceded or followed by digit-hyphen to avoid sub-matching)
    text = re.sub(r"(?<!\d-)\b(\d{3})-(\d{4})\b(?!-\d)",
                  lambda m: _join(*m.groups()), text)
    return text


# ─────────────────────────────────────────────
# Core preprocessing functions
# ─────────────────────────────────────────────

def replace_numbers(text: str, replace_floats: bool = True) -> str:
    """
    Replace all numeric tokens with their word equivalents.

    Examples:
        "There are 1200 students" → "There are twelve hundred students"
        "Pi is 3.14"              → "Pi is three point one four"
        "gpt-3 rocks"             → "gpt-3 rocks"  (hyphen not treated as minus)
    """
    def _replace(m: re.Match) -> str:
        raw = m.group().replace(",", "")
        try:
            if "." in raw and replace_floats:
                # Pass raw string so trailing zeros are preserved ("1.50" → "one point five zero")
                return float_to_words(raw)
            else:
                return number_to_words(int(float(raw)))
        except (ValueError, OverflowError):
            return m.group()
    return _RE_NUMBER.sub(_replace, text)


def to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


def remove_urls(text: str, replacement: str = "") -> str:
    """Remove URLs from text."""
    return _RE_URL.sub(replacement, text).strip()


def remove_emails(text: str, replacement: str = "") -> str:
    """Remove email addresses from text."""
    return _RE_EMAIL.sub(replacement, text).strip()


def remove_html_tags(text: str) -> str:
    """Strip HTML tags from text."""
    return _RE_HTML.sub(" ", text)


def remove_hashtags(text: str, replacement: str = "") -> str:
    """Remove hashtags (e.g. #NLP) from text."""
    return _RE_HASHTAG.sub(replacement, text)


def remove_mentions(text: str, replacement: str = "") -> str:
    """Remove @mentions from text."""
    return _RE_MENTION.sub(replacement, text)


def remove_punctuation(text: str) -> str:
    """Remove non-prosodic punctuation, keeping marks that affect speech rhythm and intonation."""
    return _RE_PUNCT.sub(" ", text)


def remove_extra_whitespace(text: str) -> str:
    """Collapse multiple whitespace characters into a single space and strip ends."""
    return _RE_SPACES.sub(" ", text).strip()


def normalize_unicode(text: str, form: str = "NFC") -> str:
    """Normalize unicode characters (NFC, NFD, NFKC, or NFKD)."""
    return unicodedata.normalize(form, text)


def remove_accents(text: str) -> str:
    """Remove diacritical marks (accents) from characters."""
    nfkd = unicodedata.normalize("NFD", text)
    return "".join(c for c in nfkd if unicodedata.category(c) != "Mn")


def expand_contractions(text: str) -> str:
    """
    Expand common English contractions.

    Examples:
        "don't"   → "do not"
        "they're" → "they are"
        "I've"    → "I have"
    """
    contractions = {
        r"\bcan't\b":   "cannot",
        r"\bwon't\b":   "will not",
        r"\bshan't\b":  "shall not",
        r"\bain't\b":   "is not",
        r"\blet's\b":   "let us",
        r"\b(\w+)n't\b": r"\1 not",
        r"\b(\w+)'re\b": r"\1 are",
        r"\b(\w+)'ve\b": r"\1 have",
        r"\b(\w+)'ll\b": r"\1 will",
        r"\b(\w+)'d\b":  r"\1 would",
        r"\b(\w+)'m\b":  r"\1 am",
        r"\bit's\b":    "it is",
    }
    for pattern, replacement in contractions.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def remove_stopwords(text: str, stopwords: Optional[set] = None) -> str:
    """
    Remove stopwords from text.

    Args:
        stopwords: Set of words to remove. Uses a built-in English set if None.
    """
    if stopwords is None:
        stopwords = {
            "a", "an", "the", "and", "or", "but", "in", "on", "at", "to",
            "for", "of", "with", "by", "from", "is", "was", "are", "were",
            "be", "been", "being", "have", "has", "had", "do", "does", "did",
            "will", "would", "could", "should", "may", "might", "this", "that",
            "these", "those", "it", "its", "i", "me", "my", "we", "our",
            "you", "your", "he", "she", "him", "her", "they", "them", "their",
        }
    tokens = text.split()
    return " ".join(t for t in tokens if t.lower() not in stopwords)


# ─────────────────────────────────────────────
# Pipeline helper
# ─────────────────────────────────────────────

class TextPreprocessor:
    """
    Configurable preprocessing pipeline.

    Usage:
        pp = TextPreprocessor(
            lowercase=True,
            replace_numbers=True,
            remove_urls=True,
            remove_html=True,
            remove_punctuation=True,
        )
        clean = pp("GPT-3 costs $0.002 per token — 50% cheaper than before!")
        # → "gpt three costs zero dollars and zero point two cents per token fifty percent cheaper than before"
    """

    def __init__(
        self,
        lowercase: bool = True,
        replace_numbers: bool = True,
        replace_floats: bool = True,
        expand_contractions: bool = True,
        expand_model_names: bool = True,
        expand_ordinals: bool = True,
        expand_percentages: bool = True,
        expand_currency: bool = True,
        expand_time: bool = True,
        expand_ranges: bool = True,
        expand_units: bool = True,
        expand_scale_suffixes: bool = True,
        expand_scientific_notation: bool = True,
        expand_fractions: bool = True,
        expand_decades: bool = True,
        expand_phone_numbers: bool = True,
        expand_ip_addresses: bool = True,
        normalize_leading_decimals: bool = True,
        expand_roman_numerals: bool = False,
        remove_urls: bool = True,
        remove_emails: bool = True,
        remove_html: bool = True,
        remove_hashtags: bool = False,
        remove_mentions: bool = False,
        remove_punctuation: bool = True,
        remove_stopwords: bool = False,
        stopwords: Optional[set] = None,
        normalize_unicode: bool = True,
        remove_accents: bool = False,
        remove_extra_whitespace: bool = True,
    ):
        self.config = {k: v for k, v in locals().items() if k != "self"}
        self._stopwords = stopwords

    def __call__(self, text: str) -> str:
        return self.process(text)

    def process(self, text: str) -> str:
        cfg = self.config

        if cfg["normalize_unicode"]:
            text = normalize_unicode(text)
        if cfg["remove_html"]:
            text = remove_html_tags(text)
        if cfg["remove_urls"]:
            text = remove_urls(text)
        if cfg["remove_emails"]:
            text = remove_emails(text)
        if cfg["remove_hashtags"]:
            text = remove_hashtags(text)
        if cfg["remove_mentions"]:
            text = remove_mentions(text)
        if cfg["expand_contractions"]:
            text = expand_contractions(text)
        # IP addresses before normalize_leading_decimals (IPs contain dots before digits)
        if cfg["expand_ip_addresses"]:
            text = expand_ip_addresses(text)
        # Normalise bare leading decimals early so downstream regexes see "0.5" not ".5"
        if cfg["normalize_leading_decimals"]:
            text = normalize_leading_decimals(text)
        # Expand special forms before generic number replacement
        if cfg["expand_currency"]:
            text = expand_currency(text)
        if cfg["expand_percentages"]:
            text = expand_percentages(text)
        # Scientific notation before model-name expansion (e.g. "1e-4" contains "e-4")
        if cfg["expand_scientific_notation"]:
            text = expand_scientific_notation(text)
        if cfg["expand_time"]:
            text = expand_time(text)
        if cfg["expand_ordinals"]:
            text = expand_ordinals(text)
        if cfg["expand_units"]:
            text = expand_units(text)
        # Scale suffixes after units (units handles "MB"/"GB"; this handles bare "B"/"M")
        if cfg["expand_scale_suffixes"]:
            text = expand_scale_suffixes(text)
        if cfg["expand_fractions"]:
            text = expand_fractions(text)
        if cfg["expand_decades"]:
            text = expand_decades(text)
        # Phone numbers before ranges, otherwise NNN-NNNN is treated as a range
        if cfg["expand_phone_numbers"]:
            text = expand_phone_numbers(text)
        if cfg["expand_ranges"]:
            text = expand_ranges(text)
        if cfg["expand_model_names"]:
            text = expand_model_names(text)
        if cfg["expand_roman_numerals"]:
            text = expand_roman_numerals(text)
        if cfg["replace_numbers"]:
            text = replace_numbers(text, replace_floats=cfg["replace_floats"])
        if cfg["remove_accents"]:
            text = remove_accents(text)
        if cfg["remove_punctuation"]:
            text = remove_punctuation(text)
        if cfg["lowercase"]:
            text = to_lowercase(text)
        if cfg["remove_stopwords"]:
            text = remove_stopwords(text, self._stopwords)
        if cfg["remove_extra_whitespace"]:
            text = remove_extra_whitespace(text)

        return text


# ─────────────────────────────────────────────
# Quick demo
# ─────────────────────────────────────────────

if __name__ == "__main__":
    pp = TextPreprocessor()

    cases = [
        # ── Numbers ────────────────────────────────────────────────────
        ("Plain integer",              "There are 1200 students and 42 teachers."),
        ("Large number",               "The project costs $1,000,000 and took 365 days."),
        ("Negative number",            "Temperature dropped to -5 degrees overnight."),
        ("Float",                      "Pi is approximately 3.14159."),
        ("Float trailing zero",        "The voltage is 1.50 volts."),
        ("Leading decimal",            "Add .5 teaspoons of salt and .25 cup of milk."),
        ("Negative leading decimal",   "A -.05 correction was applied."),
        ("Zero",                       "There were 0 errors and 0.0 warnings."),
        ("Comma thousands",            "The population is 7,900,000,000."),
        # ── Scientific notation ─────────────────────────────────────────
        ("Scientific e-notation",      "Learning rate is 1e-4, weight decay 1e-5."),
        ("Scientific capital E",       "Avogadro's number is 6.022E23."),
        ("Scientific large exp",       "The signal is 2.5e10 Hz."),
        # ── Scale suffixes ─────────────────────────────────────────────
        ("Model params B",             "We trained a 7B parameter model and a 13B variant."),
        ("Model params M",             "The 340M model beat the 7B on MMLU."),
        ("Scale suffix K",             "The salary was $85K per year."),
        # ── Currency ───────────────────────────────────────────────────
        ("Dollar amount",              "A coffee costs $4.99 here."),
        ("Euro amount",                "Rent is €1,200 per month."),
        ("Pound with cents",           "The book is £9.99."),
        # ── Percentages ────────────────────────────────────────────────
        ("Percentage",                 "Inflation rose by 3.5% last quarter."),
        ("Negative percentage",        "Stocks fell -2% today."),
        # ── Ordinals ───────────────────────────────────────────────────
        ("Ordinals 1st/2nd/3rd",       "She finished 1st, he came 2nd, I was 3rd."),
        ("Ordinal 21st",               "It's the 21st century and the 100th anniversary."),
        ("Ordinal 42nd",               "He ran his 42nd marathon."),
        ("Ordinal 33rd",               "On the 33rd floor."),
        # ── Fractions ──────────────────────────────────────────────────
        ("Half",                       "Cut the recipe in 1/2."),
        ("Quarters",                   "Add 3/4 cup of sugar and 1/4 teaspoon of salt."),
        ("Thirds",                     "The team completed 2/3 of the project."),
        ("Eighths",                    "The pipe is 5/8 inch in diameter."),
        # ── Time ───────────────────────────────────────────────────────
        ("12-hour time",               "The meeting starts at 3:30pm."),
        ("24-hour time",               "Departure at 14:00."),
        ("Time with oh",               "Alarm set for 9:05 AM."),
        ("Midnight",                   "The server restarts at 0:00."),
        # ── Decades ────────────────────────────────────────────────────
        ("Bare decade",                "The 80s music scene was iconic."),
        ("Full decade",                "She grew up listening to 1990s grunge."),
        ("2000s",                      "The 2000s brought social media."),
        ("2020s",                      "AI took off in the 2020s."),
        ("Apostrophe decade",          "Born in the '90s, raised on 2000s pop."),
        # ── Ranges ─────────────────────────────────────────────────────
        ("Numeric range",              "Read pages 10-20 for homework."),
        ("Year range",                 "The war lasted from 2020-2024."),
        ("Temperature range",          "Store between 5-10 degrees."),
        # ── Model / version names ───────────────────────────────────────
        ("GPT-3",                      "gpt-3 is pretty sick."),
        ("GPT-3.5",                    "They upgraded to GPT-3.5 last month."),
        ("GPL-3 license",              "This project is licensed under GPL-3."),
        ("Python version",             "Requires Python-3.10 or higher."),
        ("Multiple versions",          "Both CUDA-11 and CUDA-12 are supported."),
        # ── Units ──────────────────────────────────────────────────────
        ("Distance",                   "The trail is 42km long."),
        ("Weight",                     "Each package weighs 500kg."),
        ("Temperature °C",             "Water boils at 100°C."),
        ("Data size GB",               "Download the 2.5GB model file."),
        ("Frequency GHz",              "The CPU runs at 3.6GHz."),
        ("Latency ms",                 "Average latency is 12ms."),
        # ── HTML / URLs / emails ───────────────────────────────────────
        ("HTML tags",                  "<b>Hello</b> World! It's a great day."),
        ("URL and email",              "Visit https://example.com or email hello@example.com."),
        ("Hashtags and mentions",      "#NLP @user great post!"),
        # ── Contractions ───────────────────────────────────────────────
        ("Contractions",               "I don't know, won't you help? They've already left."),
        ("Ain't / let's",              "Ain't no mountain high enough. Let's go!"),
        # ── Edge / tricky cases ─────────────────────────────────────────
        ("Score / ratio",              "The final score was 3:0."),
        ("Aspect ratio",               "The display is 16:9."),
        ("IP address",                 "Connect to server at 192.168.1.1 on port 8080."),
        ("Phone number",               "Call us at 555-1234 or 1-800-555-0199."),
        ("Negative vs. hyphen",        "On a scale of -10 to 10, she rated it 8."),
        ("Ellipsis",                   "He paused... then spoke."),
        ("Em dash number",             "The result — 42 — surprised everyone."),
        # ── Mixed / real-world ──────────────────────────────────────────
        ("Research abstract",          "We trained a 7B parameter model for 100 epochs at 1e-4 learning rate."),
        ("GPT benchmark",              "GPT-4 scored 90% on the benchmark — 15% better than GPT-3.5."),
        ("News headline",              "Fed raises rates by 0.25%, S&P 500 drops 1.2%."),
        ("Startup pitch",              "We raised $2.5M in seed funding and are growing 20% month-over-month."),
        ("Tech spec",                  "The M3 chip runs at 4.05GHz with a 40M transistor GPU and 8GB RAM."),
    ]

    print("=" * 70)
    print("TextPreprocessor Demo")
    print("=" * 70)
    for label, text in cases:
        print(f"\n  [{label}]")
        print(f"  IN : {text}")
        print(f"  OUT: {pp(text)}")

    print("\n" + "=" * 70)
    print("number_to_words")
    print("=" * 70)
    for n in [0, 1, 12, 19, 20, 99, 100, 1000, 1200, 15_000, 1_000_000, -42, 999_999_999]:
        print(f"  {n:>15,} → {number_to_words(n)}")

    print("\n" + "=" * 70)
    print("float_to_words")
    print("=" * 70)
    for f in [3.14, -0.5, 1200.99, 3.10, 1.007, 0.001]:
        print(f"  {f} → {float_to_words(f)}")

    print("\n" + "=" * 70)
    print("expand_roman_numerals  (opt-in)")
    print("=" * 70)
    pp_roman = TextPreprocessor(expand_roman_numerals=True)
    for text in ["World War II ended in 1945.", "Chapter IV begins here.", "Louis XIV was king."]:
        print(f"  IN : {text}")
        print(f"  OUT: {pp_roman(text)}")
```

## File: `kittentts/__index__.py`
```python
from kittentts.get_model import get_model

    
```

## File: `kittentts/__init__.py`
```python
from kittentts.get_model import get_model, KittenTTS

__version__ = "0.1.0"
__author__ = "KittenML"
__description__ = "Ultra-lightweight text-to-speech model with just 15 million parameters"

__all__ = ["get_model", "KittenTTS"]
```

