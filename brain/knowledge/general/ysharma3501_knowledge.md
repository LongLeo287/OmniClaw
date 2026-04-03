---
id: ysharma3501-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.657262
---

# KNOWLEDGE EXTRACT: ysharma3501
> **Extracted on:** 2026-03-30 18:01:25
> **Source:** ysharma3501

---

## File: `LinaCodec.md`
```markdown
# 📦 ysharma3501/LinaCodec [🔖 PENDING/APPROVE]
🔗 https://github.com/ysharma3501/LinaCodec


## Meta
- **Stars:** ⭐ 261 | **Forks:** 🍴 25
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-19
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A highly compressive and high-quality neural audio codec for speech models.

## README (trích đầu)
```
## Linacodec: Highly compressive audio tokenizer for speech models.
<p align="center">
  <a href="https://huggingface.co/YatharthS/LinaCodec">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-FFD21E" alt="Hugging Face Model">
  </a>
</p>

Linacodec is an audio tokenizer that compresses audio into just 12.5 tokens per second (171 bps) and decodes to 48khz audio.

https://github.com/user-attachments/assets/77094afd-2d5d-490e-b283-9100e74a69a4

### Key benefits
* Compression: 12.5 tokens/sec (60x more compressed than DAC).
* Audio Quality: 48khz output (much clearer then 16khz/24khz which is the standard).
* Encoder Speed: 200x realtime.
* Decoder Speed: 400x realtime(even faster with batching)
* Many Tasks: Indirectly even supports voice conversion, audio super-resolution, and audio denoising!

### Why is this even useful?
Audio tokenizers directly contribute to speed, quality, and capability of TTS/ASR models. LinaCodec massively improves upon previous codecs in these areas.
* Inference Speed: Enables TTS models to run 800x realtime, 8x faster than [MiraTTS](https://github.com/ysharma3501)!
* Fast training: High-quality TTS models can be trained in less then 1 day.
* Versatile: Works for both Text-to-Speech and Speech-to-Text unlike most other codecs.

### Comparisons
| Model | Total Tokens/Sec | Sample Rate |
| :--- | :--- | :--- |
| Linacodec | 12.5 | 48khz |
| DAC | 774 | 44.1khz |
| EnCodec | 300 | 24khz |
| Xcodec2 | 50 | 16khz |
| Mimi | 200 | 24khz |

Lower tokens/sec means faster models and higher sample rate means more clarity.

### Usage

Simple 1 line installation:
```
pip install git+https://github.com/ysharma3501/LinaCodec.git
```

Reconstruction
```python
from IPython.display import Audio
from linacodec.codec import LinaCodec

## load model
lina_tokenizer = LinaCodec() ## will download YatharthS/LinaCodec from huggingface

## get speech tokens and global embedding
speech_tokens, global_embedding = lina_tokenizer.encode("your_audio_path.wav")

## decode them into 48khz audio
audio = lina_tokenizer.decode(speech_tokens, global_embedding)

## display audio
display(Audio(audio.cpu(), rate=48000))
```

Voice conversion
```python
## Assuming you have loaded model
source_wav = "source_wav.wav" ## the content you want
reference_wav = "reference_wav.wav" ## the timbre(style) you want

## convert voice
audio = lina_tokenizer.convert_voice(source_wav, reference_wav)

## display audio
display(Audio(audio.cpu(), rate=48000))
```

Audio super resolution
```python
## get speech tokens and global embedding from 24khz wav
speech_tokens, global_embedding = lina_tokenizer.encode("your_audio_path.wav")

## decode them into 48khz audio(upsamples from 24khz-->48khz)
audio = lina_tokenizer.decode(speech_tokens, global_embedding)

## display audio
display(Audio(audio.cpu(), rate=48000))
```


### Notes
This is heavily based of [kanade-tokenizer](https://github.com/frothywater/kanade-tokenizer) so massive thanks to them! 

The k
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `LuxTTS.md`
```markdown
# 📦 ysharma3501/LuxTTS [🔖 PENDING/APPROVE]
🔗 https://github.com/ysharma3501/LuxTTS


## Meta
- **Stars:** ⭐ 3386 | **Forks:** 🍴 417
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A high-quality rapid TTS voice cloning model that reaches speeds of 150x realtime.

## README (trích đầu)
```
# LuxTTS
<p align="center">
  <a href="https://huggingface.co/YatharthS/LuxTTS">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-FFD21E" alt="Hugging Face Model">
  </a>
  &nbsp;
  <a href="https://huggingface.co/spaces/YatharthS/LuxTTS">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue" alt="Hugging Face Space">
  </a>
  &nbsp;
  <a href="https://colab.research.google.com/drive/1cDaxtbSDLRmu6tRV_781Of_GSjHSo1Cu?usp=sharing">
    <img src="https://img.shields.io/badge/Colab-Notebook-F9AB00?logo=googlecolab&logoColor=white" alt="Colab Notebook">
  </a>
</p>

LuxTTS is an lightweight zipvoice based text-to-speech model designed for high quality voice cloning and realistic generation at speeds exceeding 150x realtime.

https://github.com/user-attachments/assets/a3b57152-8d97-43ce-bd99-26dc9a145c29


### The main features are
- Voice cloning: SOTA voice cloning on par with models 10x larger.
- Clarity: Clear 48khz speech generation unlike most TTS models which are limited to 24khz.
- Speed: Reaches speeds of 150x realtime on a single GPU and faster then realtime on CPU's as well.
- Efficiency: Fits within 1gb vram meaning it can fit in any local gpu.

## Usage
You can try it locally, colab, or spaces.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1cDaxtbSDLRmu6tRV_781Of_GSjHSo1Cu?usp=sharing)
[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/YatharthS/LuxTTS)

#### Simple installation:
```
git clone https://github.com/ysharma3501/LuxTTS.git
cd LuxTTS
pip install -r requirements.txt
```

#### Load model:
```python
from zipvoice.luxvoice import LuxTTS

# load model on GPU
lux_tts = LuxTTS('YatharthS/LuxTTS', device='cuda')

# load model on CPU
# lux_tts = LuxTTS('YatharthS/LuxTTS', device='cpu', threads=2)

# load model on MPS for macs
# lux_tts = LuxTTS('YatharthS/LuxTTS', device='mps')
```

#### Simple inference
```python
import soundfile as sf
from IPython.display import Audio

text = "Hey, what's up? I'm feeling really great if you ask me honestly!"

## change this to your reference file path, can be wav/mp3
prompt_audio = 'audio_file.wav'

## encode audio(takes 10s to init because of librosa first time)
encoded_prompt = lux_tts.encode_prompt(prompt_audio, rms=0.01)

## generate speech
final_wav = lux_tts.generate_speech(text, encoded_prompt, num_steps=4)

## save audio
final_wav = final_wav.numpy().squeeze()
sf.write('output.wav', final_wav, 48000)

## display speech
if display is not None:
  display(Audio(final_wav, rate=48000))
```

#### Inference with sampling params:
```python
import soundfile as sf
from IPython.display import Audio

text = "Hey, what's up? I'm feeling really great if you ask me honestly!"

## change this to your reference file path, can be wav/mp3
prompt_audio = 'audio_file.wav'

rms = 0.01 ## higher m
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

