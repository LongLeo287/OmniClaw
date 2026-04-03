---
id: github.com-ysharma3501-linacodec-9c8efa86-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:45.931582
---

# KNOWLEDGE EXTRACT: github.com_ysharma3501_LinaCodec_9c8efa86
> **Extracted on:** 2026-04-01 17:07:18
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525516/github.com_ysharma3501_LinaCodec_9c8efa86

---

## File: `.gitignore`
```
# Created by https://www.toptal.com/developers/gitignore/api/python,macos,visualstudiocode
# Edit at https://www.toptal.com/developers/gitignore?templates=python,macos,visualstudiocode

### macOS ###
# General
.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon


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

### macOS Patch ###
# iCloud generated files
*.icloud

### Python ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
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
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
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
*.py,cover
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
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
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
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

### Python Patch ###
# Poetry local configuration file - https://python-poetry.org/docs/configuration/#local-configuration
poetry.toml

# ruff
.ruff_cache/

# LSP config files
pyrightconfig.json

### VisualStudioCode ###
.vscode/
# !.vscode/settings.json
# !.vscode/tasks.json
# !.vscode/launch.json
# !.vscode/extensions.json
# !.vscode/*.code-snippets

# Local History for Visual Studio Code
.history/

# Built Visual Studio Code Extensions
*.vsix

### VisualStudioCode Patch ###
# Ignore all local history of files
.history
.ionide

# End of https://www.toptal.com/developers/gitignore/api/python,macos,visualstudiocode

/exp/
/test/
/data/
/output/
/weights/
/archive/
/notebook/
uv.lock
```

## File: `README.md`
```markdown
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

The key novel parts I added are:
1. Dual-Path Vocos Decoder: Enables high-quality 48kHz reconstruction from original 24khz vocos using only 30 hours of training data (compared to the typical hundreds of hours).
2. Distilled WavLM Base+: Increased encoder speed while being similar quality.
3. Snake based upsampling: Used custom upsampling block to upscale features based off snake activation from [BigVGAN](https://github.com/NVIDIA/BigVGAN).

## Next steps
- [x] Release code and model
- [ ] Release article on how kanade and Lina work so well at rates of 12.5 t/s compared to others.
- [ ] Possible paper on how these techniques can easily work on any codec.

Stars and Likes would be appreciated if found helpful, thank you.

Model link: https://huggingface.co/YatharthS/LinaCodec
Email: yatharthsharma3501@gmail.com
```

## File: `pyproject.toml`
```
[project]
name = "linacodec"
version = "0.0.11"
description = "Linacodec is a highly compressive and rapid audio tokenizer for audio models."
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
  "huggingface_hub",
  "jsonargparse[signatures]",
  "numpy",
  "safetensors",
  "soundfile",
  "torch",
  "torchaudio",
  "tqdm",
  "vocos",
]

[project.optional-dependencies]
train = [
  "einops",
]

[build-system]
requires = ["uv_build>=0.9.6,<0.10.0"]
build-backend = "uv_build"

[tool.uv.sources]
torch = [{ index = "pytorch-cu126", marker = "sys_platform == 'linux' or sys_platform == 'win32'" }]
torchaudio = [{ index = "pytorch-cu126", marker = "sys_platform == 'linux' or sys_platform == 'win32'" }]

[[tool.uv.index]]
name = "pytorch-cu126"
url = "https://download.pytorch.org/whl/cu126"
explicit = true

[tool.ruff]
line-length = 120
```

## File: `src/linacodec/__init__.py`
```python
from .model import LinaCodecFeatures, LinaCodecModel, LinaCodecConfig
from .util import load_audio, load_vocoder, vocode

__all__ = [
    "LinaCodecModel",
    "LinaCodecConfig",
    "LinaCodecFeatures",
    "load_audio",
    "load_vocoder",
    "vocode",
]
```

## File: `src/linacodec/codec.py`
```python
import torch
from linacodec.vocoder.vocos import Vocos
from huggingface_hub import snapshot_download
from .model import LinaCodecModel
from .util import load_audio, load_vocoder, vocode

class LinaCodec:
    def __init__(self, model_path=None):

        ## download from hf
        if model_path is None:
            model_path = snapshot_download("YatharthS/LinaCodec")

        ## loads linacodec model
        model = LinaCodecModel.from_pretrained(config_path=f"{model_path}/config.yaml", weights_path=f'{model_path}/model.safetensors').eval().cuda()

        ## loads distilled wavlm model, 97m params --> 25m + 18m params
        model.load_distilled_wavlm(f"{model_path}/wavlm_encoder.pth")
        model.wavlm_model.cuda()
        model.distilled_layers = [6, 9]

        ## loads vocoder, based of custom vocos and hifigan model with snake
        vocos = Vocos.from_hparams(f'{model_path}/vocoder/config.yaml').cuda()
        vocos.load_state_dict(torch.load(f'{model_path}/vocoder/pytorch_model.bin'))

        self.model = model
        self.vocos = vocos

    @torch.no_grad()
    def encode(self, audio_path):
        """encodes audio into discrete content tokens at a rate of 12.5 t/s or 25 t/s and 128 dim global embedding, single codebook"""
        ## load audio and extract features
        audio = load_audio(audio_path, sample_rate=self.model.config.sample_rate).cuda()
        features = self.model.encode(audio)
        return features.content_token_indices, features.global_embedding

    @torch.no_grad()
    @torch.autocast(device_type='cuda', dtype=torch.float16)
    def decode(self, content_tokens, global_embedding):
        """decodes tokens and embedding into 48khz waveform"""
        ## decode tokens and embedding to mel spectrogram
        mel_spectrogram = self.model.decode(content_token_indices=content_tokens, global_embedding=global_embedding)

        ## decode mel spectrogram into 48khz audio using custom vocos model
        waveform = vocode(self.vocos, mel_spectrogram.unsqueeze(0))
        return waveform
        
    def convert_voice(self, source_file, reference_file):
        """converts voice timbre, will keep content of source file but timbre of reference file"""

        ## get tokens and embedding
        speech_tokens, global_embedding = self.encode(source_file)
        ref_speech_tokens, ref_global_embedding = self.encode(reference_file)

        ## decode to audio
        audio = self.decode(speech_tokens, ref_global_embedding)
        return audio

```

## File: `src/linacodec/model.py`
```python
import math
from dataclasses import dataclass

import jsonargparse
import torch
import torch.nn as nn
import torch.nn.functional as F

from .module.fsq import FiniteScalarQuantizer
from .module.global_encoder import GlobalEncoder
from .module.postnet import PostNet
from .module.ssl_extractor import SSLFeatureExtractor
from .module.transformer import Transformer
from .module.distill_wavlm import wav2vec2_model
from .util import freeze_modules, get_logger

logger = get_logger()


@dataclass
class LinaCodecConfig:
    # SSL Feature settings
    local_ssl_layers: tuple[int, ...] = (6, 9)  # Indices of SSL layers for local branch
    global_ssl_layers: tuple[int, ...] = (1, 2)  # Indices of SSL layers for global branch
    normalize_ssl_features: bool = True  # Whether to normalize local SSL features before encoding

    # Down/up-sampling settings
    downsample_factor: int = 2  # Temporal downsampling factor for local features
    mel_upsample_factor: int = 4  # Conv1DTranspose upsampling factor for mel features before interpolation
    use_conv_downsample: bool = True  # Whether to use Conv1D for downsampling instead average pooling
    local_interpolation_mode: str = "linear"  # Interpolation mode for local upsampling ("linear", "nearest")
    mel_interpolation_mode: str = "linear"  # Interpolation mode for mel upsampling ("linear", "nearest")

    # Mel spectrogram settings
    sample_rate: int = 24000
    n_fft: int = 1024
    hop_length: int = 256
    n_mels: int = 100
    padding: str = "center"


@dataclass
class LinaCodecFeatures:
    content_embedding: torch.Tensor | None = None  # (seq_len, dim)
    content_token_indices: torch.Tensor | None = None  # (seq_len,)
    global_embedding: torch.Tensor | None = None  # (dim,)


class LinaCodecModel(nn.Module):
    """Model architecture and forward pass logic for Kanade tokenizer."""

    def __init__(
        self,
        config: LinaCodecConfig,
        ssl_feature_extractor: SSLFeatureExtractor,
        local_encoder: Transformer,
        local_quantizer: FiniteScalarQuantizer,
        feature_decoder: Transformer | None,
        global_encoder: GlobalEncoder,
        mel_prenet: Transformer,
        mel_decoder: Transformer,
        mel_postnet: PostNet,
    ):
        super().__init__()
        self.config = config
        self._init_ssl_extractor(config, ssl_feature_extractor)
        self._init_local_branch(config, local_encoder, local_quantizer, feature_decoder)
        self._init_global_branch(global_encoder)
        self._init_mel_decoder(config, mel_prenet, mel_decoder, mel_postnet)
        
    def load_distilled_wavlm(self, path: str):
        """Loads distilled wavlm model, 970m params --> 250m params"""
        ckpt = torch.load(path)
        wavlm_model = wav2vec2_model(**ckpt["config"])
        result = wavlm_model.load_state_dict(ckpt["state_dict"], strict=False)
        self.wavlm_model = wavlm_model.cuda()
        self.distilled_layers = [6, 8] ## can set custom, 6-8 seems best however

    def _init_ssl_extractor(self, config: LinaCodecConfig, ssl_feature_extractor: SSLFeatureExtractor):
        """Initialize and configure SSL feature extractor."""
        self.ssl_feature_extractor = ssl_feature_extractor
        freeze_modules([self.ssl_feature_extractor])
        logger.debug(
            f"SSL feature extractor initialized and frozen, feature dim: {self.ssl_feature_extractor.feature_dim}"
        )

        # Configure local SSL layers
        self.local_ssl_layers = list(config.local_ssl_layers)
        if len(self.local_ssl_layers) > 1:
            logger.debug(
                f"Using average of {len(self.local_ssl_layers)} SSL layers for local branch: {self.local_ssl_layers}"
            )
        else:
            logger.debug(f"Using single SSL layer {self.local_ssl_layers[0]} for local branch")

        if config.normalize_ssl_features:
            logger.debug("Normalizing local SSL features before encoding")

        # Configure global SSL layers
        self.global_ssl_layers = list(config.global_ssl_layers)
        if len(self.global_ssl_layers) > 1:
            logger.debug(
                f"Using average of {len(self.global_ssl_layers)} SSL layers for global branch: {self.global_ssl_layers}"
            )
        else:
            logger.debug(f"Using single SSL layer {self.global_ssl_layers[0]} for global branch")

    def _init_local_branch(
        self,
        config: LinaCodecConfig,
        local_encoder: Transformer,
        local_quantizer: FiniteScalarQuantizer,
        feature_decoder: Transformer | None,
    ):
        """Initialize local branch components (encoder, downsampling, quantizer, decoder)."""
        self.local_encoder = local_encoder
        self.local_quantizer = local_quantizer
        self.feature_decoder = feature_decoder

        # Configure downsampling
        self.downsample_factor = config.downsample_factor
        if self.downsample_factor > 1:
            logger.debug(f"Using temporal downsampling with factor {self.downsample_factor}")
            if config.use_conv_downsample:
                # Create Conv1d layers for downsampling and upsampling local embeddings
                feature_dim = local_encoder.output_dim
                self.conv_downsample = nn.Conv1d(
                    feature_dim, feature_dim, kernel_size=config.downsample_factor, stride=config.downsample_factor
                )
                self.conv_upsample = nn.ConvTranspose1d(
                    feature_dim, feature_dim, kernel_size=config.downsample_factor, stride=config.downsample_factor
                )  # won't be used unless training feature reconstruction
                logger.debug(f"Using Conv1d downsampling/upsampling with kernel size {config.downsample_factor}")
            else:
                self.conv_downsample = None
                self.conv_upsample = None
                logger.debug("Using average pooling and linear interpolation for downsampling/upsampling")
        else:
            self.conv_downsample = None
            self.conv_upsample = None

    def _init_global_branch(self, global_encoder: GlobalEncoder):
        """Initialize global branch components."""
        self.global_encoder = global_encoder

    def _init_mel_decoder(
        self, config: LinaCodecConfig, mel_prenet: Transformer, mel_decoder: Transformer, mel_postnet: PostNet
    ):
        """Initialize mel decoder components (prenet, upsampling, decoder, postnet)."""
        self.mel_prenet = mel_prenet
        self.mel_decoder = mel_decoder
        self.mel_postnet = mel_postnet

        # Configure mel upsampling
        self.mel_conv_upsample = None
        if config.mel_upsample_factor > 1:
            # Create Conv1DTranspose layer for mel upsampling
            input_dim = mel_prenet.output_dim
            self.mel_conv_upsample = nn.ConvTranspose1d(
                input_dim, input_dim, kernel_size=config.mel_upsample_factor, stride=config.mel_upsample_factor
            )
            logger.debug(f"Using Conv1DTranspose for mel upsampling with factor {config.mel_upsample_factor}")

    def _calculate_waveform_padding(self, audio_length: int, ensure_recon_length: bool = False) -> int:
        """Calculate required padding for input waveform to ensure consistent SSL feature lengths."""
        extractor = self.ssl_feature_extractor
        sample_rate = self.config.sample_rate
        # SSL may resample the input to its own sample rate, so calculate the number of samples after resampling
        num_samples_after_resampling = audio_length / sample_rate * extractor.ssl_sample_rate
        # We expect the SSL feature extractor to be consistent with its hop size
        expected_ssl_output_length = math.ceil(num_samples_after_resampling / extractor.hop_size)
        # If ensure_recon_length is True, we want to make sure the output length is exactly divisible by downsample factor
        if ensure_recon_length and (remainder := expected_ssl_output_length % self.downsample_factor) != 0:
            expected_ssl_output_length += self.downsample_factor - remainder
        # But it may require more input samples to produce that output length, so calculate the required input length
        num_samples_required_after_resampling = extractor.get_minimum_input_length(expected_ssl_output_length)
        # That number of samples is at the SSL sample rate, so convert back to our original sample rate
        num_samples_required = num_samples_required_after_resampling / extractor.ssl_sample_rate * sample_rate
        # Calculate padding needed on each side
        padding = math.ceil((num_samples_required - audio_length) / 2)
        return padding

    def _calculate_original_audio_length(self, token_length: int) -> int:
        """Calculate the original audio length based on token length."""
        extractor = self.ssl_feature_extractor
        sample_rate = self.config.sample_rate
        # Calculate the feature length before downsampling
        feature_length = token_length * self.downsample_factor
        num_samples_required_after_resampling = extractor.get_minimum_input_length(feature_length)
        num_samples_required = num_samples_required_after_resampling / extractor.ssl_sample_rate * sample_rate
        return math.ceil(num_samples_required)

    def _calculate_target_mel_length(self, audio_length: int) -> int:
        """Calculate the target mel spectrogram length based on audio length."""
        if self.config.padding == "center":
            return audio_length // self.config.hop_length + 1
        elif self.config.padding == "same":
            return audio_length // self.config.hop_length
        else:
            return (audio_length - self.config.n_fft) // self.config.hop_length + 1

    def _process_ssl_features(self, features: list[torch.Tensor], layers: list[int]) -> torch.Tensor:
        if len(layers) > 1:
            # Get features from multiple layers and average them
            selected_features = [features[i - 1] for i in layers]
            mixed_features = torch.stack(selected_features, dim=0).mean(dim=0)
        else:
            # Just take the single specified layer
            mixed_features = features[layers[0] - 1]
        return mixed_features

    def _normalize_ssl_features(self, features: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
        if not self.config.normalize_ssl_features:
            return features

        # Compute mean and std across time steps for each sample and feature dimension
        mean = torch.mean(features, dim=1, keepdim=True)  # (B, 1, C)
        std = torch.std(features, dim=1, keepdim=True)  # (B, 1, C)
        return (features - mean) / (std + eps)

    def forward_ssl_features(
        self, waveform: torch.Tensor, padding: int | None = None
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """Forward pass to extract SSL features. (B, T, C)
        Args:
            waveform: Input waveform tensor of shape (B, channels, samples)
            padding: Optional padding to apply on both sides of the waveform. This is useful to ensure
                     that the SSL feature extractor produces consistent output lengths.
        Returns:
            local_ssl_features: Local SSL features for local branch. (B, T, C)
            global_ssl_features: Global SSL features for global branch. (B, T, C)
        """
        # Prepare input waveform
        if waveform.dim() == 3:
            waveform = waveform.squeeze(1)

        # 1. Extract SSL features
        if padding > 0:
            waveform = F.pad(waveform, (padding, padding), mode="constant")

        with torch.no_grad():
            acoustic_wavlm_features = self.ssl_feature_extractor(waveform, num_layers=2) ## only needs 2 layers as acoustic info is present in them
            waveform = self.ssl_feature_extractor.resampler(waveform)
            distilled_wavlm_features = self.wavlm_model.extract_features(waveform, num_layers=max(self.distilled_layers))[0] ## semantic and prosody info is present in layer 4-10, 6-8 is best for quality

        local_ssl_features = self._process_ssl_features(distilled_wavlm_features, self.distilled_layers)
        local_ssl_features = self._normalize_ssl_features(local_ssl_features)

        global_ssl_features = self._process_ssl_features(acoustic_wavlm_features, self.global_ssl_layers)

        return local_ssl_features, global_ssl_features

    def forward_content(
        self, local_ssl_features: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor] | None:
        """Forward pass to extract content embeddings from the local branch.
        Args:
            local_ssl_features: Local SSL features tensor of shape (B, T, C)
        Returns:
            local_quantized: Quantized local embeddings. (B, T/factor, C)
            indices: Content token indices. (B, T/factor)
            ssl_recon: Reconstructed SSL features (if feature decoder is present). (B, T, C)
            perplexity: Quantizer perplexity (if feature decoder is present). Scalar tensor.
        """
        local_encoded = self.local_encoder(local_ssl_features)

        # Downsample temporally if needed: (B, T, C) -> (B, T/factor, C)
        if self.downsample_factor > 1:
            if self.config.use_conv_downsample:
                local_encoded = self.conv_downsample(local_encoded.transpose(1, 2)).transpose(1, 2)
            else:
                local_encoded = F.avg_pool1d(
                    local_encoded.transpose(1, 2), kernel_size=self.downsample_factor, stride=self.downsample_factor
                ).transpose(1, 2)

        # If training feature reconstruction, decode local embeddings
        ssl_recon = None
        perplexity = torch.tensor(0.0)
        if self.feature_decoder is not None:
            local_quantized, local_quantize_info = self.local_quantizer(local_encoded)
            indices = local_quantize_info["indices"]
            perplexity = torch.mean(local_quantize_info["perplexity"])

            local_latent_for_ssl = local_quantized
            # Upsample if needed
            if self.downsample_factor > 1:
                if self.config.use_conv_downsample:
                    # Use conv transpose for upsampling: (B, T/factor, C) -> (B, C, T/factor) -> conv -> (B, C, T) -> (B, T, C)
                    local_latent_for_ssl = self.conv_upsample(local_latent_for_ssl.transpose(1, 2)).transpose(1, 2)
                else:
                    # (B, T/factor, C) -> (B, T, C)
                    local_latent_for_ssl = F.interpolate(
                        local_latent_for_ssl.transpose(1, 2),
                        size=local_ssl_features.shape[1],
                        mode=self.config.local_interpolation_mode,
                    ).transpose(1, 2)

            ssl_recon = self.feature_decoder(local_latent_for_ssl)
        else:
            # If not training feature reconstruction, just get quantized local embeddings
            local_quantized, indices = self.local_quantizer.encode(local_encoded)

        return local_quantized, indices, ssl_recon, perplexity

    def forward_global(self, global_ssl_features: torch.Tensor) -> torch.Tensor:
        """Forward pass to extract global embeddings from the global branch.
        Args:
            global_ssl_features: Global SSL features tensor of shape (B, T, C)
        Returns:
            global_encoded: Global embeddings. (B, C)
        """
        global_encoded = self.global_encoder(global_ssl_features)
        return global_encoded

    def forward_mel(
        self, content_embeddings: torch.Tensor, global_embeddings: torch.Tensor, mel_length: int
    ) -> torch.Tensor:
        """Forward pass to generate mel spectrogram from content and global embeddings.
        Args:
            content_embeddings: Content embeddings tensor of shape (B, T, C)
            global_embeddings: Global embeddings tensor of shape (B, C)
            mel_length: Target mel spectrogram length (T_mel)
        Returns:
            mel_recon: Reconstructed mel spectrogram tensor of shape (B, n_mels, T_mel)
        """
        local_latent = self.mel_prenet(content_embeddings)

        # Upsample local latent to match mel spectrogram length
        # First use Conv1DTranspose if configured
        if self.mel_conv_upsample is not None:
            # (B, T/factor, C) -> (B, C, T/factor) -> conv -> (B, C, T*upsample_factor) -> (B, T*upsample_factor, C)
            local_latent = self.mel_conv_upsample(local_latent.transpose(1, 2)).transpose(1, 2)
        local_latent = F.interpolate(
            local_latent.transpose(1, 2), size=mel_length, mode=self.config.mel_interpolation_mode
        ).transpose(1, 2)  # (B, T_current, C) -> (B, T_mel, C)

        # Generate mel spectrogram, conditioned on global embeddings
        mel_recon = self.mel_decoder(local_latent, condition=global_embeddings.unsqueeze(1))
        mel_recon = mel_recon.transpose(1, 2)  # (B, n_mels, T)

        mel_recon = self.mel_postnet(mel_recon)
        return mel_recon

    # ======== Inference methods ========

    def weights_to_save(self, *, include_modules: list[str]) -> dict[str, torch.Tensor]:
        """Get model weights for saving. Excludes certain modules not needed for inference."""
        excluded_modules = [
            m
            for m in ["ssl_feature_extractor", "feature_decoder", "conv_upsample"]
            if m not in include_modules
        ]
        state_dict = {
            name: param
            for name, param in self.named_parameters()
            if not any(name.startswith(excl) for excl in excluded_modules)
        }
        return state_dict

    @classmethod
    def from_hparams(cls, config_path: str) -> "LinaCodecModel":
        """Instantiate KanadeModel from config file.
        Args:
            config_path (str): Path to model configuration file (.yaml).
        Returns:
            KanadeModel: Instantiated KanadeModel.
        """
        parser = jsonargparse.ArgumentParser(exit_on_error=False)
        parser.add_argument("--model", type=LinaCodecModel)
        cfg = parser.parse_path(config_path)
        cfg = parser.instantiate_classes(cfg)
        return cfg.model

    @classmethod
    def from_pretrained(
        cls,
        repo_id: str | None = None,
        revision: str | None = None,
        config_path: str | None = None,
        weights_path: str | None = None,
    ) -> "KanadeModel":
        """Load LinaCodec either from HuggingFace Hub or local config and weights files.
        Args:
            repo_id (str, optional): HuggingFace Hub repository ID. If provided, loads config and weights from the hub.
            revision (str, optional): Revision (branch, tag, commit) for the HuggingFace Hub repo.
            config_path (str, optional): Path to model configuration file (.yaml). Required if repo_id is not provided.
            weights_path (str, optional): Path to model weights file (.safetensors). Required if repo_id is not provided.
        Returns:
            LinaCodec: Loaded LinaCodec instance.
        """
        if repo_id is not None:
            # Load from HuggingFace Hub
            from huggingface_hub import hf_hub_download

            config_path = hf_hub_download(repo_id, "config.yaml", revision=revision)
            weights_path = hf_hub_download(repo_id, "model.safetensors", revision=revision)
        else:
            # Check local paths
            if config_path is None or weights_path is None:
                raise ValueError(
                    "Please provide either HuggingFace Hub repo_id or both config_path and weights_path for model loading."
                )

        # Load model from config
        model = cls.from_hparams(config_path)

        # Load weights
        from safetensors.torch import load_file

        state_dict = load_file(weights_path, device="cpu")
        model.load_state_dict(state_dict, strict=False)
        logger.info(f"Loaded weights from safetensors file: {weights_path}")

        return model

    @torch.inference_mode()
    def encode(self, waveform: torch.Tensor, return_content: bool = True, return_global: bool = True) -> LinaCodecFeatures:
        """Extract content and/or global features from audio using Kanade model.
        Args:
            waveform (torch.Tensor): Input audio waveform tensor (samples,). The sample rate should match model config.
            return_content (bool): Whether to extract content features.
            return_global (bool): Whether to extract global features.
        Returns:
            dict[str, torch.Tensor]: Extracted features.
        """
        audio_length = waveform.size(0)
        padding = self._calculate_waveform_padding(audio_length)
        local_ssl_features, global_ssl_features = self.forward_ssl_features(waveform.unsqueeze(0), padding=padding)

        result = LinaCodecFeatures()
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=True):
            if return_content:
                content_embedding, token_indices, _, _ = self.forward_content(local_ssl_features)
                result.content_embedding = content_embedding.squeeze(0)  # (seq_len, dim)
                result.content_token_indices = token_indices.squeeze(0)  # (seq_len,)

            if return_global:
                global_embedding = self.forward_global(global_ssl_features)
                result.global_embedding = global_embedding.squeeze(0)  # (dim,)

        return result

    def decode_token_indices(self, indices: torch.Tensor) -> torch.Tensor:
        """Get content embeddings from content token indices. (..., seq_len) -> (..., seq_len, dim)"""
        content_embedding = self.local_quantizer.decode(indices)
        return content_embedding

    @torch.inference_mode()
    def decode(
        self,
        global_embedding: torch.Tensor,
        content_token_indices: torch.Tensor | None = None,
        content_embedding: torch.Tensor | None = None,
        target_audio_length: int | None = None,
    ) -> torch.Tensor:
        """Synthesize audio from content and global features using LinaCodec model and Vocos.
        Args:
            global_embedding (torch.Tensor): Global embedding tensor (dim,).
            content_token_indices (torch.Tensor, optional): Optional content token indices tensor (seq_len).
            content_embedding (torch.Tensor, optional): Optional content embedding tensor (seq_len, dim).
                If both content_token_indices and content_embedding are provided, content_embedding takes precedence.
            target_audio_length (int, optional): Target length of the output audio in samples.
                If None, uses the original audio length estimated from the sequence length of content tokens.
        Returns:
            torch.Tensor: Generated mel spectrogram tensor (n_mels, T).
        """
        # Obtain content embedding if not provided
        if content_embedding is None:
            if content_token_indices is None:
                raise ValueError("Either content_token_indices or content_embedding must be provided.")
            content_embedding = self.decode_token_indices(content_token_indices)

        if target_audio_length is None:
            # Estimate original audio length from content token sequence length
            seq_len = content_embedding.size(0)
            target_audio_length = self._calculate_original_audio_length(seq_len)

        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=True):
            mel_length = self._calculate_target_mel_length(target_audio_length)
            content_embedding = content_embedding.unsqueeze(0)  # (1, seq_len, dim)
            global_embedding = global_embedding.unsqueeze(0)  # (1, dim)
            mel_spectrogram = self.forward_mel(content_embedding, global_embedding, mel_length=mel_length)

        return mel_spectrogram.squeeze(0)  # (n_mels, T)

    @torch.inference_mode()
    def voice_conversion(self, source_waveform: torch.Tensor, reference_waveform: torch.Tensor) -> torch.Tensor:
        """Convert voice using LinaCodec model and Vocos, keeping content from source and global characteristics from reference.
        Only supports single audio input. Just a convenient wrapper around encode and decode methods.
        Args:
            source_waveform (torch.Tensor): Source audio waveform tensor (samples,).
            reference_waveform (torch.Tensor): Reference audio waveform tensor (samples_ref,).
        Returns:
            torch.Tensor: Converted mel spectrogram tensor (n_mels, T).
        """
        # Extract source content features and reference global features
        source_features = self.encode(source_waveform, return_content=True, return_global=False)
        reference_features = self.encode(reference_waveform, return_content=False, return_global=True)

        # Synthesize mel spectrogram using source content and reference global features
        mel_spectrogram = self.decode(
            content_embedding=source_features.content_embedding,
            global_embedding=reference_features.global_embedding,
            target_audio_length=source_waveform.size(0),
        )
        return mel_spectrogram
```

## File: `src/linacodec/util.py`
```python
import logging

import torch
import torch.nn as nn

# Configure logger
logger = logging.getLogger("kanade_tokenizer")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s %(name)s: %(message)s"))
logger.addHandler(handler)


def get_logger() -> logging.Logger:
    return logger


def freeze_modules(modules: list[nn.Module] | None):
    for module in modules:
        if module is not None:
            for param in module.parameters():
                param.requires_grad = False


def _load_audio_internal(
    path: str, frame_offset: int | None = None, num_frames: int | None = None
) -> tuple[torch.Tensor, int]:
    # TorchAudio >= 2.9.0 removed decoding and encoding capabilities to TorchCodec.
    # See: https://github.com/pytorch/audio/issues/3902
    # waveform, sample_rate = torchaudio.load(path, frame_offset=frame_offset or 0, num_frames=num_frames or -1)

    import soundfile as sf

    with sf.SoundFile(path) as f:
        if frame_offset is not None:
            f.seek(frame_offset)
        frames = f.read(frames=num_frames or -1, dtype="float32", always_2d=True)
        waveform = torch.from_numpy(frames.T)
        sample_rate = f.samplerate
    return waveform, sample_rate


def load_audio(audio_path: str, sample_rate: int = 24000) -> torch.Tensor:
    import torchaudio

    """Load and preprocess audio file."""
    waveform, sr = _load_audio_internal(audio_path)

    # Convert to mono if stereo
    if waveform.shape[0] > 1:
        waveform = torch.mean(waveform, dim=0, keepdim=True)

    # Resample if necessary
    if sr != sample_rate:
        resampler = torchaudio.transforms.Resample(sr, sample_rate)
        waveform = resampler(waveform)

    # Normalize waveform
    max_val = torch.max(torch.abs(waveform)) + 1e-8
    waveform = waveform / max_val  # Normalize to [-1, 1]

    return waveform.squeeze(0)  # Remove channel dimension


def load_vocoder():
    from vocos import Vocos

    model = Vocos.from_pretrained("charactr/vocos-mel-24khz")
    model = model.eval()
    return model


def vocode(vocoder, mel_spectrogram: torch.Tensor) -> torch.Tensor:
    """Convert mel spectrogram to waveform using Vocos vocoder.
    Args:
        vocoder (Vocos): Pretrained Vocos vocoder.
        mel_spectrogram (torch.Tensor): Input mel spectrogram tensor (..., n_mels, frame).
    Returns:
        torch.Tensor: Generated audio waveform tensor (..., samples).
    """
    mel_spectrogram = mel_spectrogram.to(torch.float32)  # Ensure mel spectrogram is in float32
    generated_waveform = vocoder.decode(mel_spectrogram)
    return generated_waveform
```

## File: `src/linacodec/module/adaln_zero.py`
```python
# Adapted from: https://github.com/facebookresearch/DiT


import torch
from torch import nn


class AdaLNZero(nn.Module):
    """
    Adaptive Layer Normalization Zero (AdaLNZero) module.

    Combines LayerNorm with adaptive conditioning to produce shift, scale, and gate values.
    The gate is used to scale features before residual connection.

    Args:
        dim: Feature dimension
        condition_dim: Conditioning dimension
        eps: LayerNorm epsilon
        return_gate: If True, returns gate value for scaling.
    """

    def __init__(
        self,
        dim: int,
        condition_dim: int,
        eps: float = 1e-5,
        return_gate: bool = True,
    ):
        super().__init__()
        self.dim = dim
        self.condition_dim = condition_dim
        self.return_gate = return_gate

        # LayerNorm without learnable parameters
        self.norm = nn.LayerNorm(dim, eps=eps, elementwise_affine=False)

        # Conditioning network: condition -> shift, scale, gate
        output_dim = 3 * dim if return_gate else 2 * dim
        self.condition_proj = nn.Sequential(
            nn.SiLU(),
            nn.Linear(condition_dim, output_dim),
        )

        # Initialize to zero for stable training
        nn.init.zeros_(self.condition_proj[1].weight)
        nn.init.zeros_(self.condition_proj[1].bias)

    def forward(self, x: torch.Tensor, condition: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor] | None:
        """
        Args:
            x: Input tensor of shape (B, L, dim)
            condition: Conditioning tensor of shape (B, L, condition_dim) or (B, 1, condition_dim)

        Returns:
            modulated_x: Normalized and modulated features
            gate: Gate values for scaling (None if return_gate=False)
        """
        x_norm = self.norm(x)
        condition_params = self.condition_proj(condition)

        if self.return_gate:
            shift, scale, gate = condition_params.chunk(3, dim=-1)
        else:
            shift, scale = condition_params.chunk(2, dim=-1)
            gate = None

        modulated_x = x_norm * (1 + scale) + shift
        return modulated_x, gate
```

## File: `src/linacodec/module/audio_feature.py`
```python
# Adapted from:
# Vocos: https://github.com/gemelo-ai/vocos/blob/main/vocos/feature_extractors.py

import torch
import torchaudio
from torch import nn


def safe_log(x: torch.Tensor, clip_val: float = 1e-7) -> torch.Tensor:
    return torch.log(torch.clip(x, min=clip_val))


class MelSpectrogramFeature(nn.Module):
    def __init__(
        self,
        sample_rate: int = 24000,
        n_fft: int = 1024,
        hop_length: int = 256,
        n_mels: int = 100,
        padding: str = "center",
    ):
        super().__init__()

        # Vocos style: center padding, HTK mel scale, without normalization
        if padding not in ["center", "same"]:
            raise ValueError("Padding must be 'center' or 'same'.")

        self.padding = padding
        self.mel_spec = torchaudio.transforms.MelSpectrogram(
            sample_rate=sample_rate,
            n_fft=n_fft,
            hop_length=hop_length,
            n_mels=n_mels,
            center=padding == "center",
            power=1,
        )

    def forward(self, audio):
        """
        Returns:
            mel_specgram (Tensor): Mel spectrogram of the input audio. (B, C, L)
        """
        if self.padding == "same":
            pad = self.mel_spec.win_length - self.mel_spec.hop_length
            audio = torch.nn.functional.pad(audio, (pad // 2, pad // 2), mode="reflect")

        specgram = self.mel_spec.spectrogram(audio)
        mel_specgram = self.mel_spec.mel_scale(specgram)
        mel_specgram = safe_log(mel_specgram)
        return mel_specgram
```

## File: `src/linacodec/module/components.py`
```python
from collections import defaultdict
from typing import List, Optional, Tuple
import math

import torch
from torch import nn, Tensor
from torch.nn import Module, Parameter

from .hardconcrete import HardConcrete
from .pruning_utils import (
    prune_linear_layer,
    prune_conv1d_layer,
    prune_layer_norm,
)


def _init_transformer_params(module):
    """
    Initialize the weights of Transformer module in Wav2Vec2/HuBERT.

    If the module is ``nn.Linear``, normalize the weight with mean 0 and standard deviation 0.02.
    If ``bias`` is set to ``True`` in the module, set ``bias`` to 0.

    If the module is ``nn.Embedding``, normalize the weight with mean 0 and standard deviation 0.02.
    If ``padding_idx`` is not None, set the weight of padding to 0.

    Note:
        Ths method corresponds to
        `init_bert_params
        <https://github.com/facebookresearch/fairseq/blob/main/fairseq/modules/transformer_sentence_encoder.py#L21>`__
        in the original ``fairseq`` implementation.
    """

    def normal_(data):
        data.copy_(data.cpu().normal_(mean=0.0, std=0.02).to(data.device))

    if isinstance(module, nn.Linear):
        normal_(module.weight.data)
        if module.bias is not None:
            module.bias.data.zero_()
    if isinstance(module, nn.Embedding):
        normal_(module.weight.data)
        if module.padding_idx is not None:
            module.weight.data[module.padding_idx].zero_()


class LayerNorm(nn.LayerNorm):
    """Layer norm with transpose"""

    def forward(self, input: Tensor) -> Tensor:
        x = input.transpose(-2, -1)
        x = nn.functional.layer_norm(x, self.normalized_shape, self.weight, self.bias, self.eps)
        x = x.transpose(-2, -1)
        return x


class ConvLayerBlock(Module):
    """Convolution unit of FeatureExtractor"""

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int,
        stride: int,
        bias: bool,
        layer_norm: Optional[Module],
        prune_conv_channels: bool = False,
    ):
        super().__init__()
        self.kernel_size = kernel_size
        self.stride = stride
        self.layer_norm = layer_norm
        self.conv = nn.Conv1d(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            stride=stride,
            bias=bias,
        )

        if prune_conv_channels:
            self.hard_concrete = HardConcrete(n_in=out_channels, init_mean=0.01)
        else:
            self.hard_concrete = None

    def forward(
        self,
        x: Tensor,
        length: Optional[Tensor],
    ) -> Tuple[Tensor, Optional[Tensor]]:
        """
        Args:
            x (Tensor): Shape: ``[batch, in_channels, in_frame]``.
            length (Tensor or None, optional): Shape ``[batch, ]``.
        Returns:
            Tensor: Shape ``[batch, out_channels, out_frames]``.
            Optional[Tensor]: Shape ``[batch, ]``.
        """
        x = self.conv(x)
        if self.layer_norm is not None:
            x = self.layer_norm(x)
        x = nn.functional.gelu(x)

        if self.hard_concrete is not None:
            channel_mask = self.hard_concrete()  # hard concrete mask, (out_channels,)
            x = x * channel_mask.unsqueeze(-1)

        if length is not None:
            length = torch.div(length - self.kernel_size, self.stride, rounding_mode="floor") + 1
            # When input length is 0, the resulting length can be negative. So fix it here.
            length = torch.max(torch.zeros_like(length), length)
        return x, length
    
    def get_num_params_and_out_channels(self, in_channels):
        if self.hard_concrete is not None:
            out_channels = self.hard_concrete.l0_norm()
        else:
            out_channels = self.conv.out_channels
        
        num_params = in_channels * out_channels * self.kernel_size
        if self.conv.bias is not None:
            num_params += out_channels
        if self.layer_norm is not None:
            num_params += out_channels * 2
        
        return num_params, out_channels


class FeatureExtractor(Module):
    """Extract features from audio

    Args:
        conv_layers (nn.ModuleList):
            convolution layers
    """

    def __init__(
        self,
        conv_layers: nn.ModuleList,
    ):
        super().__init__()
        self.conv_layers = conv_layers

        # NOTE: a dummy weight used to save the soft mask of the last conv layer
        self.dummy_weight = nn.Parameter(
            torch.ones(conv_layers[-1].conv.out_channels, dtype=torch.float32),
            requires_grad=False
        )

    def forward(
        self,
        x: Tensor,
        length: Optional[Tensor],
    ) -> Tuple[Tensor, Optional[Tensor]]:
        """
        Args:
            x (Tensor):
                Input Tensor representing a batch of audio,
                shape: ``[batch, time]``.
            length (Tensor or None, optional):
                Valid length of each input sample. shape: ``[batch, ]``.

        Returns:
            Tensor:
                The resulting feature, shape: ``[batch, frame, feature]``
            Optional[Tensor]:
                Valid length of each output sample. shape: ``[batch, ]``.
        """
        if x.ndim != 2:
            raise ValueError("Expected the input Tensor to be 2D (batch, time), " "but received {list(x.shape)}")

        x = x.unsqueeze(1)  # (batch, channel==1, frame)
        for layer in self.conv_layers:
            x, length = layer(x, length)  # (batch, feature, frame)
        x = x.transpose(1, 2)  # (batch, frame, feature)
        x = x * self.dummy_weight
        return x, length

    def get_num_params_and_final_out_channels(self):
        in_channels = 1
        num_params = 0
        for layer in self.conv_layers:
            layer_params, in_channels = layer.get_num_params_and_out_channels(in_channels)
            num_params += layer_params

        num_params += in_channels   # dummy weight
        
        return num_params, in_channels
    
    def prune(self):
        """"Prune conv layers and dummy weight based on hardconcrete parameters.
        This is an in-place operation.
        """
        new_config = []     # [(output_channel, kernel_size, stride), ...]
        for idx, layer in enumerate(self.conv_layers):
            if layer.hard_concrete is not None:
                assert not layer.hard_concrete.training
                mask = layer.hard_concrete()    # (out_features,)
                index = mask.nonzero().squeeze(-1)    # 2D -> 1D
                assert len(index) > 0, f"Conv channels pruned to zero at index {idx}"
                new_config.append(
                    (len(index), layer.kernel_size, layer.stride)
                )

                # prune the current layer
                prune_conv1d_layer(layer.conv, index, "output")
                if layer.layer_norm is not None:
                    prune_layer_norm(layer.layer_norm, index)

                # prune the next layer
                if idx == len(self.conv_layers) - 1:
                    self.dummy_weight.data *= mask
                    self.dummy_weight = nn.Parameter(
                        self.dummy_weight.index_select(0, index).clone().detach(), requires_grad=False
                    )
                else:
                    self.conv_layers[idx+1].conv.weight.data *= mask.unsqueeze(-1)
                    prune_conv1d_layer(self.conv_layers[idx+1].conv, index, dim="input")

                layer.hard_concrete = None
            else:
                new_config.append(
                    (layer.conv.out_channels, layer.kernel_size, layer.stride)
                )
                index = torch.arange(layer.conv.out_channels, dtype=torch.long)

        return new_config, index


class FeatureProjection(Module):
    """Layer that connects FeatureExtractor and Encoder

    Projects features to encoder dimension.

    Args:
        in_features (int): Input feature dim.
        out_features (int): Output feature dim.
        dropout (float): Dropout probability.
    """

    def __init__(
        self,
        in_features: int,
        out_features: int,
        dropout: float,
    ):
        super().__init__()
        self.layer_norm = nn.LayerNorm(in_features)
        self.projection = nn.Linear(
            in_features,
            out_features,
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        """
        Args:
            x (Tensor):
                Feature Tensor. shape: ``[batch, frame, in_feature]``
        Returns:
            Tensor: Projected features. ``[batch, frame, out_feature]``.
        """
        x = self.layer_norm(x)
        x = self.projection(x)
        x = self.dropout(x)
        return x
    
    def get_num_params(self, in_features):
        return in_features * 2 + (in_features + 1) * self.projection.out_features


class ConvolutionalPositionalEmbedding(Module):
    """Positional embedding which is placed at the beginning of Transformer.

    Args:
        embed_dim (int): Feature dimension of the input Tensor.
        kernel_size (int): The number of frames to be use.
        groups (int): The number of groups in feature dimensions.
    """

    def __init__(
        self,
        embed_dim: int,
        kernel_size: int,
        groups: int,
    ):
        super().__init__()
        self.embed_dim = embed_dim
        self.kernel_size = kernel_size
        self.conv = nn.Conv1d(
            in_channels=embed_dim,
            out_channels=embed_dim,
            kernel_size=kernel_size,
            padding=kernel_size // 2,
            groups=groups,
        )

        self.conv = nn.utils.weight_norm(self.conv, name="weight", dim=2)
        self.num_remove: int = 1 if kernel_size % 2 == 0 else 0

    def __prepare_scriptable__(self):
        for hook in self.conv._forward_pre_hooks.values():
            # The hook we want to remove is an instance of WeightNorm class, so
            # normally we would do `if isinstance(...)` but this class is not accessible
            # because of shadowing, so we check the module name directly.
            # https://github.com/pytorch/pytorch/blob/be0ca00c5ce260eb5bcec3237357f7a30cc08983/torch/nn/utils/__init__.py#L3
            if hook.__module__ == "torch.nn.utils.weight_norm" and hook.__class__.__name__ == "WeightNorm":
                torch.nn.utils.remove_weight_norm(self.conv)
        return self

    def forward(self, x):
        """
        Args:
            x (Tensor): shape ``[batch, frame, feature]``.

        Returns:
            Tensor: The resulting feature. Shape ``[batch, frame, feature]``.
        """
        x = x.transpose(-2, -1)
        x = self.conv(x)
        if self.num_remove > 0:
            x = x[..., : -self.num_remove]
        x = torch.nn.functional.gelu(x)
        x = x.transpose(-2, -1)
        return x


class SelfAttention(Module):
    """Multihead Self Attention module

    Args:
        embed_dim (int): Total dimension of the model.
        num_heads (int): The number of heads.
        dropout (float, optional):
            Dropout probability on attn_output_weights. Default: ``0.0``
    """

    def __init__(
        self,
        embed_dim: int,
        num_heads: int,
        head_dim: int,
        dropout: float = 0.0,
        prune_heads: bool = False,  # whether to prune attention heads
        prune_layer: bool = False,  # whether to prune entire attention layers
    ):
        super().__init__()

        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = head_dim
        self.dropout = torch.nn.Dropout(dropout)

        self.scaling = self.head_dim**-0.5

        self.k_proj = nn.Linear(embed_dim, num_heads * head_dim, bias=True)
        self.v_proj = nn.Linear(embed_dim, num_heads * head_dim, bias=True)
        self.q_proj = nn.Linear(embed_dim, num_heads * head_dim, bias=True)
        self.out_proj = nn.Linear(num_heads * head_dim, embed_dim, bias=True)

        if prune_heads:
            self.hard_concrete_for_heads = HardConcrete(n_in=num_heads, init_mean=0.01)
        else:
            self.hard_concrete_for_heads = None

        if prune_layer:
            self.hard_concrete_for_layer = HardConcrete(n_in=1, init_mean=0.01)
        else:
            self.hard_concrete_for_layer = None

    def forward(
        self,
        x: Tensor,
        attention_mask: Optional[Tensor] = None,
        position_bias: Optional[Tensor] = None,
        key_padding_mask: Optional[Tensor] = None,
    ) -> Tuple[Tensor, Optional[Tensor]]:
        """
        Args:
            x (Tensor): shape: ``[batch_size, sequence_length, embed_dim]``.
            attention_mask (Tensor or ``None``, optional):
                shape: ``[batch_size, 1, sequence_length, sequence_length]``
            position_bias: Not used. Only for the compatibility with :py:class:`WavLMSelfAttention`.
            key_padding_mask (Tensor or ``None``): Not used. Only for the compatibility with
                :py:class:`WavLMSelfAttention`.
        Returns:
            (Tensor, ``None``): The resulting attention output and ``None`` (necessary for compatibility
                with :py:class:`WavLMSelAttention`).
                Attention output shape: ``[batch, sequence_length, embed_dim]``.
        """
        if x.ndim != 3 or x.shape[2] != self.embed_dim:
            raise ValueError(
                f"The expected input shape is (batch, sequence, embed_dim=={self.embed_dim}). " f"Found {x.shape}."
            )
        batch_size, length, embed_dim = x.size()
        
        shape = (batch_size, length, self.num_heads, self.head_dim)
        q = self.q_proj(x).view(*shape).transpose(2, 1)  # B, nH, L, Hd
        k = self.k_proj(x).view(*shape).permute(0, 2, 3, 1)  # B, nH, Hd, L
        v = self.v_proj(x).view(*shape).transpose(2, 1)  # B, nH, L, Hd

        # scale down q to avoid value overflow.
        weights = (self.scaling * q) @ k  # B, nH, L, L
        if attention_mask is not None:
            weights += attention_mask
        # subtracting a constant value from the tensor won't change the output of softmax.
        # apply the subtraction to avoid value overflow in torch.nn.functional.softmax.
        # for more details, please see Equation 7 in https://arxiv.org/abs/2112.08778
        weights = weights - weights.max(dim=-1, keepdim=True)[0]

        weights = torch.nn.functional.softmax(weights, dim=-1)
        weights = self.dropout(weights)

        output = weights @ v  # B, nH, L, Hd

        if self.hard_concrete_for_heads is not None:
            head_mask = self.hard_concrete_for_heads()  # (nH,)
            output = output * head_mask.unsqueeze(-1).unsqueeze(-1)

        output = output.transpose(2, 1).reshape(batch_size, length, self.num_heads * self.head_dim)

        output = self.out_proj(output)

        if self.hard_concrete_for_layer is not None:
            layer_mask = self.hard_concrete_for_layer() # (1,)
            output = output * layer_mask

        return output, None  # Necessary for compatibility with WavLMSelAttention

    def get_num_params(self):
        if self.hard_concrete_for_heads is not None:
            num_heads = self.hard_concrete_for_heads.l0_norm()
        else:
            num_heads = self.num_heads
        num_params = (self.embed_dim + 1) * num_heads * self.head_dim * 3 \
            + (num_heads * self.head_dim + 1) * self.embed_dim

        if self.hard_concrete_for_layer is not None:
            num_params *= self.hard_concrete_for_layer.l0_norm()
        
        return num_params

    def prune(self):
        new_config = {
            "use_attention": True,
            "num_heads": self.num_heads,
        }
        if self.hard_concrete_for_layer is not None:
            assert not self.hard_concrete_for_layer.training
            layer_mask = self.hard_concrete_for_layer() # (1,)
            self.out_proj.weight.data *= layer_mask
            self.out_proj.bias.data *= layer_mask
            if layer_mask == 0:
                new_config["use_attention"] = False
            self.hard_concrete_for_layer = None

        if self.hard_concrete_for_heads is not None:
            assert not self.hard_concrete_for_heads.training
            head_mask = self.hard_concrete_for_heads()  # (num_heads,)
            new_config["num_heads"] = len(head_mask.nonzero())
            if new_config["num_heads"] == 0:
                new_config["use_attention"] = False
            else:
                full_mask = head_mask.repeat_interleave(self.head_dim)
                full_index = full_mask.nonzero().squeeze(-1)  # 1D

                prune_linear_layer(self.k_proj, full_index, "output")
                prune_linear_layer(self.v_proj, full_index, "output")
                prune_linear_layer(self.q_proj, full_index, "output")

                self.out_proj.weight.data *= full_mask
                prune_linear_layer(self.out_proj, full_index, "input")
            self.hard_concrete_for_heads = None

        return new_config


class WavLMSelfAttention(SelfAttention):
    """Multi-headed self-attention for WavLM model :cite:`chen2022wavlm`.

    Args:
        embed_dim (int): Total dimension of the model.
        num_heads (int): The number of heads.
        dropout (float, optional): Dropout probability on attn_output_weights. (Default: to ``0.0``)
        bias (bool, optional): If ``True``, add bias to input / output projection layers. (Default: ``True``)
        has_relative_attention_bias (bool, optional): If ``True``, apply relative position embedding.
            Necessary in the first encoder layer, but not in the subsequent ones. (Default: ``False``)
        num_buckets (int, optional): Number of buckets for relative position embedding. (Default: ``32``)
        max_distance (int, optional): Naximum distance for relative position embedding. (Default: ``128``)
        gru_rel_pos (bool, optional): If ``True``, apply gated relative position embedding. (Default: ``False``)
    """

    def __init__(
        self,
        embed_dim: int,
        total_num_heads: int,
        remaining_heads: Optional[List[int]] = None,
        dropout: float = 0.0,
        bias: bool = True,
        has_relative_attention_bias: bool = False,
        num_buckets: int = 32,
        max_distance: int = 128,
        gru_rel_pos: bool = True,
        prune_heads: bool = False,
        prune_layer: bool = False,
    ):
        self.total_num_heads = total_num_heads
        if remaining_heads is None:
            self.remaining_heads = list(range(total_num_heads))
        else:
            self.remaining_heads = remaining_heads  # list of indices
        
        self.head_dim = embed_dim // total_num_heads

        super().__init__(embed_dim, len(self.remaining_heads), self.head_dim, dropout, prune_heads, prune_layer)

        self.has_relative_attention_bias = has_relative_attention_bias
        self.num_buckets = num_buckets
        self.max_distance = max_distance

        if has_relative_attention_bias:
            self.rel_attn_embed = nn.Embedding(num_buckets, total_num_heads)
        else:
            self.rel_attn_embed = None

        # override linear layers to customize bias
        self.k_proj = nn.Linear(embed_dim, len(self.remaining_heads) * self.head_dim, bias=bias)
        self.v_proj = nn.Linear(embed_dim, len(self.remaining_heads) * self.head_dim, bias=bias)
        self.q_proj = nn.Linear(embed_dim, len(self.remaining_heads) * self.head_dim, bias=bias)
        self.out_proj = nn.Linear(len(self.remaining_heads) * self.head_dim, embed_dim, bias=bias)

        self.gru_rel_pos = gru_rel_pos
        if self.gru_rel_pos:
            self.gru_rel_pos_linear = nn.Linear(self.head_dim, 8)
            self.gru_rel_pos_const = nn.Parameter(torch.ones(1, total_num_heads, 1, 1))
        self.has_position_bias = True

    def compute_bias(self, query_length: int, key_length: int) -> Tensor:
        """Compute relative position embeddings for WavLM model.
        Args:
            query_length (int): Query position can take values between 0 and ``query_length - 1``.
            key_length (int): Key position can take values between 0 and ``key_length - 1``.
        Returns:
            Tensor of shape `(num_heads, query_length, key_length)`, relative positions embeddings
        """
        context_position = torch.arange(query_length, dtype=torch.long)[:, None]
        memory_position = torch.arange(key_length, dtype=torch.long)[None, :]
        relative_position = memory_position - context_position  # Shape (query_length, key_length)
        relative_position_bucket = self._relative_positions_bucket(relative_position, bidirectional=True)
        relative_position_bucket = relative_position_bucket.to(self.rel_attn_embed.weight.device)
        values = self.rel_attn_embed(relative_position_bucket)  # Shape (query_length, key_length, num_heads)
        values = values.permute([2, 0, 1])
        return values

    def _relative_positions_bucket(self, relative_positions: Tensor, bidirectional: bool = True):
        """Compute relative position buckets for WavLM model. Computation similar to formula (5) in WavLM
           paper :cite:`chen2022wavlm`.
        Args:
            relative_positions (Tensor): Relative offsets between query and key positions,
                of shape ``(query_length, key_length)``.
            bidirectional (bool): If ``True``, values will be filled both above and below the diagonal in the resulting
                matrix. If ``False``, the elements above the diagonal (i.e. with negative relative offsets) will be set
                to zero. (Default ``True``)
        Returns:
            Tensor of shape ``(query_length, key_length)`` filled bucketed values of with relative positions.
        """
        num_buckets = self.num_buckets
        max_distance = self.max_distance
        # Shape (query_length, key_length)
        relative_buckets = torch.zeros_like(relative_positions, dtype=torch.long)

        if bidirectional:
            num_buckets = num_buckets // 2
            relative_buckets += (relative_positions > 0).to(torch.long) * num_buckets
            relative_positions = torch.abs(relative_positions)
        else:
            relative_positions = -torch.min(relative_positions, torch.zeros_like(relative_positions))

        max_exact = num_buckets // 2
        is_small = relative_positions < max_exact

        relative_postion_if_large = max_exact + (
            torch.log(relative_positions.float() / max_exact)
            / math.log(max_distance / max_exact)
            * (num_buckets - max_exact)
        ).to(torch.long)
        relative_postion_if_large = torch.min(
            relative_postion_if_large, torch.full_like(relative_postion_if_large, num_buckets - 1)
        )

        relative_buckets += torch.where(is_small, relative_positions, relative_postion_if_large)
        return relative_buckets

    def forward(
        self,
        query: Tensor,
        attention_mask: Optional[Tensor] = None,
        position_bias: Optional[Tensor] = None,
        key_padding_mask: Optional[Tensor] = None,
    ) -> Tuple[Tensor, Optional[Tensor]]:
        """
        Args:
            query (Tensor): Input of shape ``(batch_size, src_len, embed_dim)``.
            key_padding_mask (Tensor or None, optional): Mask to exclude keys that are pads, of shape
                `(batch, src_len)`, where padding elements are indicated by 1s. (Default: ``None``)
            attn_mask: Needs to be ``None``. The argument exists for compatibility with
                ``EncoderLayer``. (Default: ``None``)
            position_bias (Tensor or None, optional): Position bias of shape
                ``(batch_size * num_heads, src_len, src_len)``. When used inside WavLM model encoder, will be
                generated in the first layer and then passed from each encoder layer to the next one.
                (Default: ``None``)
        Returns:
            attn_output (Tensor): Attention output of shape ``(batch_size, src_len, embed_dim)``.
            position_bias (Tensor or None): Position bias of shape ``(batch_size * num_heads, src_len, src_len)``.
        """
        bsz, seq_len, embed_dim = query.size()
        assert embed_dim == self.embed_dim
        assert key_padding_mask is None

        # only for the first layer
        if self.rel_attn_embed is not None and position_bias is None:
            position_bias = self.compute_bias(seq_len, seq_len)
            position_bias = position_bias.unsqueeze(0).repeat(bsz, 1, 1, 1).view(bsz * self.total_num_heads, seq_len, seq_len)

        attn_mask_rel_pos: Optional[Tensor] = None
        if position_bias is not None:
            attn_mask_rel_pos = position_bias
            if self.gru_rel_pos:  # Apply gating on relative position bias
                query_layer = query.view(bsz, seq_len, self.total_num_heads, -1)
                query_layer = query_layer.permute(0, 2, 1, 3)

                gate_a, gate_b = torch.sigmoid(
                    self.gru_rel_pos_linear(query_layer).view(bsz, self.total_num_heads, seq_len, 2, 4).sum(-1, keepdim=False)
                ).chunk(2, dim=-1)
                gate_a_1 = gate_a * (gate_b * self.gru_rel_pos_const - 1.0) + 2.0
                attn_mask_rel_pos = gate_a_1.view(bsz * self.total_num_heads, -1, 1) * position_bias

            attn_mask_rel_pos = attn_mask_rel_pos.view((-1, seq_len, seq_len))
            attn_mask_rel_pos = attn_mask_rel_pos.reshape(bsz, self.total_num_heads, seq_len, seq_len)[:, self.remaining_heads, :, :]

        attn_mask = attn_mask_rel_pos
        if attention_mask is not None:
            attn_mask = attn_mask + attention_mask
        if key_padding_mask is not None:
            attn_mask = attn_mask.masked_fill(
                key_padding_mask.reshape(bsz, 1, 1, seq_len),
                float("-inf")
            )
        attn_output, _ = super().forward(query, attention_mask=attn_mask)

        return attn_output, position_bias

    def prune(self):
        new_config = {
            "use_attention": True,
            "remaining_heads": self.remaining_heads,
        }
        if self.hard_concrete_for_layer is not None:
            assert not self.hard_concrete_for_layer.training
            layer_mask = self.hard_concrete_for_layer() # (1,)
            self.out_proj.weight.data *= layer_mask
            self.out_proj.bias.data *= layer_mask
            if layer_mask == 0:
                new_config["use_attention"] = False
            self.hard_concrete_for_layer = None

        if self.hard_concrete_for_heads is not None:
            assert not self.hard_concrete_for_heads.training
            head_mask = self.hard_concrete_for_heads()  # (num_heads,)
            new_config["remaining_heads"] = head_mask.nonzero().squeeze(-1).tolist()
            if len(new_config["remaining_heads"]) == 0:
                new_config["use_attention"] = False
            else:
                full_mask = head_mask.repeat_interleave(self.head_dim)
                full_index = full_mask.nonzero().squeeze(-1)  # 1D

                prune_linear_layer(self.k_proj, full_index, "output")
                prune_linear_layer(self.v_proj, full_index, "output")
                prune_linear_layer(self.q_proj, full_index, "output")

                self.out_proj.weight.data *= full_mask
                prune_linear_layer(self.out_proj, full_index, "input")
            self.hard_concrete_for_heads = None

        return new_config


class FeedForward(Module):
    """Layer that follows attention layer in encoder layer."""

    def __init__(
        self,
        io_features: int,
        intermediate_features: int,
        intermediate_dropout: float,
        output_dropout: float,
        prune_intermediate: bool = False,
        prune_layer: bool = False,
    ):
        super().__init__()
        self.intermediate_dense = nn.Linear(io_features, intermediate_features)
        self.intermediate_dropout = nn.Dropout(intermediate_dropout)
        self.output_dense = nn.Linear(intermediate_features, io_features)
        self.output_dropout = nn.Dropout(output_dropout)

        if prune_intermediate:
            self.hard_concrete_for_intermediate = HardConcrete(
                n_in=intermediate_features, init_mean=0.5
            )
        else:
            self.hard_concrete_for_intermediate = None
        
        if prune_layer:
            self.hard_concrete_for_layer = HardConcrete(n_in=1, init_mean=0.01)
        else:
            self.hard_concrete_for_layer = None

    def forward(self, x):
        """
        Args:
            x (Tensor): shape: `(batch, sequence_length, io_features)`
        Returns:
            x (Tensor): shape: `(batch, sequence_length, io_features)`
        """
        x = self.intermediate_dense(x)
        x = torch.nn.functional.gelu(x)
        x = self.intermediate_dropout(x)

        if self.hard_concrete_for_intermediate is not None:
            intermediate_mask = self.hard_concrete_for_intermediate()   # (intermediate_features,)
            x = x * intermediate_mask

        x = self.output_dense(x)
        x = self.output_dropout(x)

        if self.hard_concrete_for_layer is not None:
            layer_mask = self.hard_concrete_for_layer()     # (1,)
            x = x * layer_mask

        return x
    
    def get_num_params(self):
        io_features = self.intermediate_dense.in_features
        if self.hard_concrete_for_intermediate is not None:
            intermediate_features = self.hard_concrete_for_intermediate.l0_norm()
        else:
            intermediate_features = self.intermediate_dense.out_features
        num_params = (io_features + 1) * intermediate_features + (intermediate_features + 1) * io_features

        if self.hard_concrete_for_layer is not None:
            num_params *= self.hard_concrete_for_layer.l0_norm()
        
        return num_params
    
    def prune(self):
        new_config = {
            "use_feed_forward": True,
            "ff_interm_features": self.intermediate_dense.out_features
        }
        if self.hard_concrete_for_layer is not None:
            assert not self.hard_concrete_for_layer.training
            layer_mask = self.hard_concrete_for_layer()
            self.output_dense.weight.data *= layer_mask
            self.output_dense.bias.data *= layer_mask
            if layer_mask == 0:
                new_config["use_feed_forward"] = False
            self.hard_concrete_for_layer = None

        if self.hard_concrete_for_intermediate is not None:
            assert not self.hard_concrete_for_intermediate.training
            interm_mask = self.hard_concrete_for_intermediate()
            interm_index = interm_mask.nonzero().squeeze(-1)    # NOTE: must specify dim=-1
            new_config["ff_interm_features"] = len(interm_index)
            if new_config["ff_interm_features"] == 0:
                new_config["use_feed_forward"] = False
            else:
                prune_linear_layer(self.intermediate_dense, interm_index, "output")

                self.output_dense.weight.data *= interm_mask
                prune_linear_layer(self.output_dense, interm_index, "input")
            self.hard_concrete_for_intermediate = None

        return new_config


class EncoderLayer(Module):
    """A layer unit in encoder. Combines multihead self attention and feed forward."""

    def __init__(
        self,
        attention: Optional[Module],    # can be None if the entire layer is pruned
        dropout: float,
        layer_norm_first: bool,
        feed_forward: Optional[Module], # can be None if the entire layer is pruned
        embed_dim: int,
    ):
        super().__init__()
        self.attention = attention
        self.dropout = nn.Dropout(dropout)
        self.layer_norm = nn.LayerNorm(embed_dim)
        self.layer_norm_first = layer_norm_first
        self.feed_forward = feed_forward
        self.final_layer_norm = nn.LayerNorm(embed_dim)
        self.embed_dim = embed_dim

    def forward(
        self,
        x: Tensor,
        attention_mask: Optional[Tensor] = None,
        position_bias: Optional[Tensor] = None,
        key_padding_mask: Optional[Tensor] = None,
    ) -> Tuple[Tensor, Optional[Tensor]]:
        """
        Args:
            x (Tensor): Input of shape ``(batch, sequence_length, embed_dim)``.
            attention_mask (Tensor or ``None``, optional): attention mask
                of shape ``(batch, 1, sequence_length, sequence_length)``. (Default: ``None``)
            position_bias (Tensor or ``None``, optional): position bias of shape
                ``(batch_size * num_heads, src_len, src_len)``.
                Only necessary for WavLM model, ``None`` otherwise. (Default: ``None``)
            key_padding_mask (Tensor or ``None``, optional): key padding mask of shape ``(batch_size, src_len)``.
                Only used for WavLM model, ignored otherwise. (Default: ``None``)
        Returns:
            (x, position_bias): Shapes are the same as in the input. Position bias is only relevant for WaLM model,
                ``None`` otherwise.
        """
        if self.attention is not None:
            residual = x

            if self.layer_norm_first:
                x = self.layer_norm(x)

            x, position_bias = self.attention(
                x, attention_mask=attention_mask, position_bias=position_bias, key_padding_mask=key_padding_mask
            )

            x = self.dropout(x)
            x = residual + x

        if self.layer_norm_first:
            if self.feed_forward is not None:
                x = x + self.feed_forward(self.final_layer_norm(x))
        else:
            # NOTE: for post norm, the layer norms should always be applied even if the layers are pruned.
            x = self.layer_norm(x)
            if self.feed_forward is not None:
                x = x + self.feed_forward(x)
            x = self.final_layer_norm(x)
        return x, position_bias

    def get_num_params(self):
        num_params = self.embed_dim * 2 * 2     # two layer norms
        if self.attention is not None:
            num_params += self.attention.get_num_params()
        if self.feed_forward is not None:
            num_params += self.feed_forward.get_num_params()
        return num_params


class Transformer(Module):
    def __init__(
        self,
        pos_conv_embed: Module,
        dropout: float,
        layers: Module,
        layer_norm_first: bool,
        layer_drop: float,
    ):
        super().__init__()
        self.pos_conv_embed = pos_conv_embed
        self.layer_norm = nn.LayerNorm(pos_conv_embed.embed_dim)
        self.layer_norm_first = layer_norm_first
        self.layer_drop = layer_drop
        self.dropout = nn.Dropout(dropout)
        self.layers = layers

    def _preprocess(self, x: Tensor):
        x = x + self.pos_conv_embed(x)

        if self.layer_norm_first:
            x = self.layer_norm(x)

        x = self.dropout(x)
        return x

    def forward(
        self,
        x: Tensor,
        attention_mask: Optional[Tensor] = None,
        position_bias: Optional[Tensor] = None,
    ) -> Tensor:
        x = self._preprocess(x)
        for layer in self.layers:
            if not (self.training and torch.rand(1).item() <= self.layer_drop):
                x, position_bias = layer(x, attention_mask, position_bias=position_bias)

        if not self.layer_norm_first:
            x = self.layer_norm(x)
        return x

    def get_intermediate_outputs(
        self,
        x: Tensor,
        attention_mask: Optional[Tensor] = None,
        num_layers: Optional[int] = None,
        position_bias: Optional[Tensor] = None,
    ) -> List[Tensor]:
        if num_layers is not None:
            if not 0 < num_layers <= len(self.layers):
                raise ValueError(f"`num_layers` must be between [1, {len(self.layers)}]")

        ret: List[Tensor] = []
        x = self._preprocess(x)
        for layer in self.layers:
            x, position_bias = layer(x, attention_mask, position_bias=position_bias)
            ret.append(x)
            if num_layers is not None and len(ret) >= num_layers:
                return ret
        return ret
    
    def get_num_params(self):
        # pos_conv_embed and layer_norm
        num_params = sum(p.numel() for p in self.pos_conv_embed.parameters()) + self.pos_conv_embed.embed_dim * 2
        for layer in self.layers:
            num_params += layer.get_num_params()
        return num_params
    
    def prune(self):
        new_config = defaultdict(list)
        for layer in self.layers:
            attention_config = layer.attention.prune()
            new_config["use_attention"].append(attention_config["use_attention"])
            if "remaining_heads" in attention_config:
                new_config["remaining_heads"].append(attention_config["remaining_heads"])
            else:
                new_config["num_heads"].append(attention_config["num_heads"])

            if not attention_config["use_attention"]:
                layer.attention = None
            
            ff_config = layer.feed_forward.prune()
            new_config["use_feed_forward"].append(ff_config["use_feed_forward"])
            new_config["ff_interm_features"].append(ff_config["ff_interm_features"])
            if not ff_config["use_feed_forward"]:
                layer.feed_forward = None
        
        return new_config


class Encoder(Module):
    def __init__(
        self,
        feature_projection: Module,
        transformer: Module,
    ):
        super().__init__()
        self.feature_projection = feature_projection
        self.transformer = transformer

    def _preprocess(
        self,
        features: Tensor,
        lengths: Optional[Tensor] = None,
    ) -> Tuple[Tensor, Optional[Tensor]]:
        x = self.feature_projection(features)

        mask: Optional[Tensor] = None
        if lengths is not None:
            batch_size, max_len, _ = x.shape
            # create mask for padded elements and zero-out them
            mask = torch.arange(max_len, device=lengths.device).expand(batch_size, max_len) >= lengths[:, None]
            x[mask] = 0.0
            # extend the mask to attention shape and set weight
            mask = -10000.0 * mask[:, None, None, :].to(dtype=features.dtype)
            mask = mask.expand(batch_size, 1, max_len, max_len)
        return x, mask

    def forward(
        self,
        features: Tensor,
        lengths: Optional[Tensor] = None,
    ) -> Tensor:
        x, mask = self._preprocess(features, lengths)
        x = self.transformer(x, attention_mask=mask)
        return x

    def extract_features(
        self,
        features: Tensor,
        lengths: Optional[Tensor] = None,
        num_layers: Optional[int] = None,
    ) -> List[Tensor]:
        x, masks = self._preprocess(features, lengths)
        interm = self.transformer.get_intermediate_outputs(x, attention_mask=masks, num_layers=num_layers)
        return [x] + interm
    
    def get_num_params(self, in_features):
        """Calculate the current model size."""
        feature_projection_size = self.feature_projection.get_num_params(in_features)
        transformer_size = self.transformer.get_num_params()
        return feature_projection_size + transformer_size
    
    def prune(self, conv_out_index):
        """In-place pruning of submodules."""
        prune_layer_norm(self.feature_projection.layer_norm, conv_out_index)
        prune_linear_layer(self.feature_projection.projection, conv_out_index, "input")
        transformer_config = self.transformer.prune()
        return transformer_config


################################################################################
def _get_feature_extractor(
    norm_mode: str,
    shapes: List[Tuple[int, int, int]],
    bias: bool,
    prune_conv_channels: bool = False,
) -> FeatureExtractor:
    """
    Args:
        norm_mode (str):
            Either "group_norm" or "layer_norm".
            If "group_norm", then a single normalization is applied
            in the first convolution block. Otherwise, all the convolution
            blocks will have layer normalization.
            This option corresponds to "extractor_mode" from fairseq.
            Expected values are "group_norm" for Base arch, and
            "layer_norm" for Large arch.
        shapes (list of tuple of int):
            Configuration of convolution layers. List of convolution configuration,
            i.e. ``[(output_channel, kernel_size, stride), ...]``
            This option corresponds to "conv_feature_layers" from fairseq.
            Expected values are
            ``[(512, 10, 5)] + [(512, 3, 2)] * 4 + [(512, 2, 2)] * 2``
            for all the architectures.
        bias (bool):
            Whether to include bias term to each convolution operation.
            This option corresponds to "conv_bias" from fairseq.
            Expected values are False for Base arch, and True for Large arch.

    See Also:
        * Original implementation
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L666-L733
        * "extractor_mode"
          - Def and base:
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L38-L45
          - Large:
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/pretraining/wav2vec2_large_librivox.yaml#L52
        * "conv_feature_layers"
          - Def, base and large:
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L94-L100
        * "conv_bias"
          - Def and base:
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L101-L103
          - Large:
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/pretraining/wav2vec2_large_librivox.yaml#L61
    """
    if norm_mode not in ["group_norm", "layer_norm"]:
        raise ValueError("Invalid norm mode")
    blocks = []
    in_channels = 1
    for i, (out_channels, kernel_size, stride) in enumerate(shapes):
        normalization = None
        if norm_mode == "group_norm" and i == 0:
            normalization = nn.GroupNorm(
                num_groups=out_channels,
                num_channels=out_channels,
                affine=True,
            )
        elif norm_mode == "layer_norm":
            normalization = LayerNorm(
                normalized_shape=out_channels,
                elementwise_affine=True,
            )
        blocks.append(
            ConvLayerBlock(
                in_channels=in_channels,
                out_channels=out_channels,
                kernel_size=kernel_size,
                stride=stride,
                bias=bias,
                layer_norm=normalization,
                prune_conv_channels=prune_conv_channels,
            )
        )
        in_channels = out_channels
    return FeatureExtractor(nn.ModuleList(blocks))


def _get_encoder(
    in_features: int,
    embed_dim: int,
    dropout_input: float,
    pos_conv_kernel: int,
    pos_conv_groups: int,
    num_layers: int,
    use_attention: List[bool],
    use_feed_forward: List[bool],
    num_heads: List[int],
    head_dim: int,
    attention_dropout: float,
    ff_interm_features: List[int],
    ff_interm_dropout: float,
    dropout: float,
    layer_norm_first: bool,
    layer_drop: float,
    prune_attention_heads: bool = False,
    prune_attention_layer: bool = False,
    prune_feed_forward_intermediate: bool = False,
    prune_feed_forward_layer: bool = False,
) -> Encoder:
    """
    Args:
        in_features (int): The number of input features.
        embed_dim (int):
            The dimension of embedding.
            This option corresponds to "encoder_embed_dim" from fairseq.
            Expected values are 768 for Base arch, and 1024 for Large arch.
        dropout_input (float):
            The dropout probability applied after the input feature is projected
            to ``embed_dim``.
            This option corresponds to "dropout_input" from fairseq.
            Expected values are 0.1 for both Base and Large arch.
        pos_conv_kernel (int):
            The kernel size of convolutional positional embeddings.
            This option corresponds to "conv_pos" from fairseq.
            Expected values are 128 for both Base and Large arch.
        pos_conv_groups (int):
            The number of groups of convolutional positional embeddings.
            This option corresponds to "conv_pos_groups" from fairseq.
            Expected values are 16 for both Base and Large arch.
        num_layers (int):
            The number of self attention layers in transformer block.
            This option corresponds to "encoder_layers" from fairseq.
            Expected values are 12 for Base and 24 for Large arch.
        num_heads (int):
            The number of heads in self attention layers.
            This option corresponds to "encoder_attention_heads" from fairseq.
            Expected values are 12 for Base and 16 for Large arch.
        attention_dropout (float):
            The dropout probability applied after softmax in self-attention layer.
            This option corresponds to "attention_dropout" from fairseq.
            Expected values are 0.1 for Base and 0.0 for Large arch.
        ff_interm_features (int):
            The dimension of hidden features in feed forward layer.
            This option corresponds to "encoder_ffn_embed_dim" from fairseq.
            Expected values are 3072 for Base and 4096 for Large arch.
        ff_interm_dropout (float):
            The dropout probability applied in feedforward layer.
            This option correspinds to "activation_dropout" from fairseq.
            Expected values are 0.1 for both Base and Large arch.
        dropout (float):
            The dropout probability applied at the end of feed forward layer.
            This option corresponds to "dropout" from fairseq.
            Expected values are 0.1 for Base and 0.0 for Large arch.
        layer_norm_first (bool):
            Control the order of layer norm in transformer layer and each encoder layer.
            If True, in transformer layer, layer norm is applied before features are fed
            to encoder layers. In encoder layer, two layer norms are applied before and after
            self attention.
            If False, in transformer layer, layer norm is applied after features are fed
            to encoder layers. In encoder layer, two layer norms are applied after self
            attention, before and after feed forward.
            This option corresponds to "layer_norm_first" from fairseq.
            Expected values are False for Base and True for Large arch.
        layer_drop (float):
            Probability to drop each encoder layer during training.
            This option corresponds to "layerdrop" from fairseq.
            Expected values are 0.1 for both Base and Large arch.

    See Also:
        * "encoder_embed_dim"
          - Def and base
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L49-L51
          - Large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/pretraining/wav2vec2_large_librivox.yaml#L64
        * "dropout_input"
          - Def, base and large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L75-L78
        * "conv_pos"
          - Def, base and large
            NOTE: The description is wrong.
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L204-L207
          - Usage
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L756
        * "conv_pos_groups"
          - Def, base and large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L208-L211
        * "encoder_layers"
          - Def and base
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L46-L48
          - Large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/pretraining/wav2vec2_large_librivox.yaml#L63
        * "encoder_attention_heads"
          - Def and base
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L55-L57
          - Large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/pretraining/wav2vec2_large_librivox.yaml#L66
        * "attention_dropout"
          - Def and base
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L66-L68
          - Large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/pretraining/wav2vec2_large_librivox.yaml#L60
        * "encoder_ffn_embed_dim"
          - Def and base
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L52-L54
          - Large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/pretraining/wav2vec2_large_librivox.yaml#L65
        * "activation_dropout"
          - Def
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L69-L71
          - Base
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/finetuning/base_960h.yaml#L55
          - Large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/finetuning/vox_960h.yaml#L55
        * "dropout"
          - Def and base
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L63-L65
          - Large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/pretraining/wav2vec2_large_librivox.yaml#L59
        * "layer_norm_first"
          - Def and base
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L91-L93
          - Large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/pretraining/wav2vec2_large_librivox.yaml#L53
        * "layerdrop"
          - Def
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L72-L74
          - Base
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/finetuning/base_960h.yaml#L54
          - Large
            https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/examples/wav2vec/config/finetuning/vox_960h.yaml#L54
    """
    feature_projection = FeatureProjection(in_features, embed_dim, dropout_input)
    pos_conv = ConvolutionalPositionalEmbedding(embed_dim, pos_conv_kernel, pos_conv_groups)

    # Original impl
    # https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L768-L782
    encoder_layers = nn.ModuleList()
    for idx in range(num_layers):
        if use_attention[idx]:
            attention = SelfAttention(
                embed_dim=embed_dim,
                num_heads=num_heads[idx],
                head_dim=head_dim,
                dropout=attention_dropout,
                prune_heads=prune_attention_heads,
                prune_layer=prune_attention_layer,
            )
        else:
            attention = None
        if use_feed_forward[idx]:
            feed_forward = FeedForward(
                io_features=embed_dim,
                intermediate_features=ff_interm_features[idx],
                intermediate_dropout=ff_interm_dropout,
                output_dropout=dropout,
                prune_intermediate=prune_feed_forward_intermediate,
                prune_layer=prune_feed_forward_layer,
            )
        else:
            feed_forward = None
        encoder_layers.append(
            EncoderLayer(
                attention=attention,
                dropout=dropout,
                layer_norm_first=layer_norm_first,
                feed_forward=feed_forward,
                embed_dim=embed_dim,
            )
        )
    transformer = Transformer(
        pos_conv_embed=pos_conv,
        dropout=dropout,
        layers=encoder_layers,
        layer_norm_first=not layer_norm_first,
        layer_drop=layer_drop,
    )
    return Encoder(feature_projection, transformer)


def _get_wavlm_encoder(
    in_features: int,
    embed_dim: int,
    dropout_input: float,
    pos_conv_kernel: int,
    pos_conv_groups: int,
    num_layers: int,
    use_attention: List[bool],
    use_feed_forward: List[bool],
    total_num_heads: List[int],
    remaining_heads: List[List[int]],
    num_buckets: int,
    max_distance: int,
    attention_dropout: float,
    ff_interm_features: List[int],
    ff_interm_dropout: float,
    dropout: float,
    layer_norm_first: bool,
    layer_drop: float,
    prune_attention_heads: bool = False,
    prune_attention_layer: bool = False,
    prune_feed_forward_intermediate: bool = False,
    prune_feed_forward_layer: bool = False,
) -> Encoder:
    """
    Construct encoder for WavLM model :cite:`chen2022wavlm`. The structure of the encoder and most of the argments are
    the same as in :py:func:`_get_encoder` so refer there for documentation. The only difference from Wav2Vec2 encoder
    is usage of `WavLMSelfAttention` instead of `SelfAttention` and two additional parameters: `num_buckets` and
    `max_distance`.
    Args:
        in_features (int): See :py:func:`_get_encoder`.
        embed_dim (int): See :py:func:`_get_encoder`.
        dropout_input (float): See :py:func:`_get_encoder`.
        pos_conv_kernel (int): See :py:func:`_get_encoder`.
        pos_conv_groups (int): See :py:func:`_get_encoder`.
        num_layers (int): See :py:func:`_get_encoder`.
        num_heads (int): See :py:func:`_get_encoder`.
        num_buckets (int): Number of buckets for relative position embedding.
        max_distance (int): Maximum distance for relative position embedding.
        attention_dropout (float): See :py:func:`_get_encoder`.
        ff_interm_features (int): See :py:func:`_get_encoder`.
        ff_interm_dropout (float): See :py:func:`_get_encoder`.
        dropout (float): See :py:func:`_get_encoder`.
        layer_norm_first (bool): See :py:func:`_get_encoder`.
        layer_drop (float): See :py:func:`_get_encoder`.

    """
    feature_projection = FeatureProjection(in_features, embed_dim, dropout_input)
    pos_conv = ConvolutionalPositionalEmbedding(embed_dim, pos_conv_kernel, pos_conv_groups)

    # Original impl
    # https://github.com/pytorch/fairseq/blob/425c36eafff535fe7337f8bdd5ace22ebacc78cb/fairseq/models/wav2vec/wav2vec2.py#L768-L782
    encoder_layers = nn.ModuleList()
    for i in range(num_layers):
        if use_attention[i]:
            attention = WavLMSelfAttention(
                embed_dim=embed_dim,
                total_num_heads=total_num_heads[i],
                remaining_heads=remaining_heads[i],
                dropout=attention_dropout,
                has_relative_attention_bias=(i == 0),  # Position embedding is only necessary in the first layer.
                num_buckets=num_buckets,
                max_distance=max_distance,
                prune_heads=prune_attention_heads,
                prune_layer=prune_attention_layer,
            )
        else:
            attention = None
        if use_feed_forward[i]:
            feed_forward = FeedForward(
                io_features=embed_dim,
                intermediate_features=ff_interm_features[i],
                intermediate_dropout=ff_interm_dropout,
                output_dropout=dropout,
                prune_intermediate=prune_feed_forward_intermediate,
                prune_layer=prune_feed_forward_layer,
            )
        else:
            feed_forward = None
        encoder_layers.append(
            EncoderLayer(
                attention=attention,
                dropout=dropout,
                layer_norm_first=layer_norm_first,
                feed_forward=feed_forward,
                embed_dim=embed_dim,
            )
        )
    transformer = Transformer(
        pos_conv_embed=pos_conv,
        dropout=dropout,
        layers=encoder_layers,
        layer_norm_first=not layer_norm_first,
        layer_drop=layer_drop,
    )
    return Encoder(feature_projection, transformer)


def _get_padding_mask(input: Tensor, lengths: Tensor) -> Tensor:
    """Generate the padding mask given the padded input and the lengths Tensors.
    Args:
        input (Tensor): The padded Tensor of dimension `[batch, max_len, frequency]`.
        lengths (Tensor): The lengths Tensor of dimension `[batch,]`.

    Returns:
        (Tensor): The padding mask.
    """
    batch_size, max_len, _ = input.shape
    mask = torch.arange(max_len, device=lengths.device).expand(batch_size, max_len) >= lengths[:, None]
    return mask


class GradMultiply(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, scale):
        ctx.scale = scale
        res = x.new(x)
        return res

    @staticmethod
    def backward(ctx, grad):
        return grad * ctx.scale, None
```

## File: `src/linacodec/module/convnext.py`
```python
# Adapted from: https://github.com/gemelo-ai/vocos/blob/main/vocos/models.py


import torch
from torch import nn


class ConvNeXtBlock(nn.Module):
    """ConvNeXt Block adapted from https://github.com/facebookresearch/ConvNeXt to 1D audio signal.

    Args:
        dim (int): Number of input channels.
        intermediate_dim (int): Dimensionality of the intermediate layer.
        layer_scale_init_value (float, optional): Initial value for the layer scale. None means no scaling.
            Defaults to None.
    """

    def __init__(
        self,
        dim: int,
        intermediate_dim: int,
        layer_scale_init_value: float,
    ):
        super().__init__()
        self.dwconv = nn.Conv1d(dim, dim, kernel_size=7, padding=3, groups=dim)  # depthwise conv
        self.norm = nn.LayerNorm(dim, eps=1e-6)
        self.pwconv1 = nn.Linear(dim, intermediate_dim)  # pointwise/1x1 convs, implemented with linear layers
        self.act = nn.GELU()
        self.pwconv2 = nn.Linear(intermediate_dim, dim)
        self.gamma = (
            nn.Parameter(layer_scale_init_value * torch.ones(dim), requires_grad=True)
            if layer_scale_init_value > 0
            else None
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        residual = x
        x = self.dwconv(x)
        x = x.transpose(1, 2)  # (B, C, T) -> (B, T, C)
        x = self.norm(x)
        x = self.pwconv1(x)
        x = self.act(x)
        x = self.pwconv2(x)
        if self.gamma is not None:
            x = self.gamma * x
        x = x.transpose(1, 2)  # (B, T, C) -> (B, C, T)

        x = residual + x
        return x


class ConvNextBackbone(nn.Module):
    """
    Backbone module built with ConvNeXt blocks.

    Args:
        input_channels (int): Number of input features channels.
        dim (int): Hidden dimension of the model.
        intermediate_dim (int): Intermediate dimension used in ConvNeXtBlock.
        num_layers (int): Number of ConvNeXtBlock layers.
        layer_scale_init_value (float, optional): Initial value for layer scaling. Defaults to `1 / num_layers`.
    """

    def __init__(
        self,
        input_channels: int,
        dim: int,
        intermediate_dim: int,
        num_layers: int,
        output_channels: int | None = None,
        layer_scale_init_value: float | None = None,
        skip_embed: bool = False,
    ):
        super().__init__()
        self.input_channels = input_channels
        self.output_channels = output_channels
        self.dim = dim
        self.embed = nn.Conv1d(input_channels, dim, kernel_size=7, padding=3) if not skip_embed else nn.Identity()
        self.norm = nn.LayerNorm(dim, eps=1e-6)
        layer_scale_init_value = layer_scale_init_value or 1 / num_layers
        self.convnext = nn.ModuleList(
            [
                ConvNeXtBlock(
                    dim=dim,
                    intermediate_dim=intermediate_dim,
                    layer_scale_init_value=layer_scale_init_value,
                )
                for _ in range(num_layers)
            ]
        )
        self.proj_out = nn.Linear(dim, output_channels) if output_channels else nn.Identity()
        self.final_layer_norm = nn.LayerNorm(dim, eps=1e-6)
        self.apply(self._init_weights)

    @property
    def input_dim(self) -> int:
        return self.input_channels

    @property
    def output_dim(self) -> int:
        return self.output_channels if self.output_channels else self.dim

    def _init_weights(self, m):
        if isinstance(m, (nn.Conv1d, nn.Linear)):
            nn.init.trunc_normal_(m.weight, std=0.02)
            nn.init.constant_(m.bias, 0)

    def forward(self, x: torch.Tensor, **kwargs) -> torch.Tensor:
        """
        Args:
            x (Tensor): Input tensor of shape (B, L, C), where B is the batch size,
                        C denotes output features, and L is the sequence length.
        Returns:
            Tensor: Output of shape (B, L, H), where B is the batch size, L is the sequence length,
                    and H denotes the model dimension.
        """
        x = x.transpose(1, 2)  # (B, L, C) -> (B, C, L)
        x = self.embed(x)
        x = self.norm(x.transpose(1, 2))
        x = x.transpose(1, 2)
        for conv_block in self.convnext:
            x = conv_block(x)
        x = self.final_layer_norm(x.transpose(1, 2))
        x = self.proj_out(x)
        return x
```

## File: `src/linacodec/module/discriminator.py`
```python
# Adapted from:
# https://github.com/gemelo-ai/vocos/blob/main/vocos/discriminators.py
# https://github.com/gemelo-ai/vocos/blob/main/vocos/loss.py

import torch
from einops import rearrange
from torch import nn
from torch.nn.utils.parametrizations import weight_norm


def get_2d_padding(kernel_size: tuple[int, int], dilation: tuple[int, int] = (1, 1)):
    return (((kernel_size[0] - 1) * dilation[0]) // 2, ((kernel_size[1] - 1) * dilation[1]) // 2)


class SpectrogramDiscriminator(nn.Module):
    def __init__(
        self,
        frequency_bins: int,
        channels: int = 32,
        kernel_size: tuple[int, int] = (3, 3),
        dilation: list[int] = [1, 2, 4],
        bands: tuple[tuple[float, float], ...] = ((0.0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1.0)),
        use_downsample: bool = True,
    ):
        super().__init__()
        self.bands = [(int(b[0] * frequency_bins), int(b[1] * frequency_bins)) for b in bands]

        self.stacks = nn.ModuleList()
        for _ in self.bands:
            stack = nn.ModuleList(
                [weight_norm(nn.Conv2d(1, channels, kernel_size, padding=get_2d_padding(kernel_size)))]
            )

            for d in dilation:
                # dilation on time axis
                pad = get_2d_padding(kernel_size, (d, 1))
                stack.append(weight_norm(nn.Conv2d(channels, channels, kernel_size, dilation=(d, 1), padding=pad)))

            stack.append(weight_norm(nn.Conv2d(channels, channels, kernel_size, padding=get_2d_padding(kernel_size))))

            self.stacks.append(stack)

        self.conv_post = weight_norm(nn.Conv2d(channels, 1, kernel_size, padding=get_2d_padding(kernel_size)))
        if use_downsample:
            self.downsample = nn.AvgPool2d(4, stride=2, padding=1, count_include_pad=False)
        else:
            self.downsample = nn.Identity()

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, list[torch.Tensor]]:
        """
        Args:
            x (Tensor): Input spectrogram (B, C, F, T).
        Returns:
            output (Tensor): Discriminator output.
            intermediates (list[Tensor]): List of intermediate feature maps.
        """
        if x.dim() == 3:
            x = x.unsqueeze(1)
        assert x.dim() == 4, f"Expected 4D input, got {x.dim()}D"

        # Split into bands
        x = rearrange(x, "b c f t -> b c t f")
        x_bands = [x[..., b[0] : b[1]] for b in self.bands]

        x = []
        intermediates = []
        for x_band, stack in zip(x_bands, self.stacks):
            for layer in stack:
                x_band = layer(x_band)
                x_band = torch.nn.functional.leaky_relu(x_band, 0.1)
                intermediates.append(x_band)
            x.append(x_band)

        # Concatenate the outputs from all bands
        x = torch.cat(x, dim=-1)
        x = self.conv_post(x)
        x = self.downsample(x)
        return x, intermediates
```

## File: `src/linacodec/module/distill_wavlm.py`
```python
"""Speech SSL models supporting pruning.

Originally from:
https://github.com/pytorch/audio/blob/main/torchaudio/models/wav2vec2/model.py

"""

import math
from typing import List, Optional, Tuple

import torch
import torch.nn.functional as F
from torch import Tensor
from torch.nn import Module

from . import components


class Wav2Vec2Model(Module):
    """Acoustic model used in *wav2vec 2.0* :cite:`baevski2020wav2vec`.

    Note:
        To build the model, please use one of the factory functions.
        :py:func:`wav2vec2_model`, :py:func:`wav2vec2_base`, :py:func:`wav2vec2_large`,
        :py:func:`wav2vec2_large_lv60k`, :py:func:`hubert_base`, :py:func:`hubert_large`,
        and :py:func:`hubert_xlarge`.

    See Also:
        * :class:`torchaudio.pipelines.Wav2Vec2Bundle`: Pretrained models (without fine-tuning)
        * :class:`torchaudio.pipelines.Wav2Vec2ASRBundle`: ASR pipelines with pretrained models.

    Args:
        feature_extractor (torch.nn.Module):
            Feature extractor that extracts feature vectors from raw audio Tensor.

        encoder (torch.nn.Module):
            Encoder that converts the audio features into the sequence of probability
            distribution (in negative log-likelihood) over labels.

        aux (torch.nn.Module or None, optional):
            Auxiliary module. If provided, the output from encoder is passed to this module.
    """  # noqa: E501

    def __init__(
        self,
        normalize_waveform: bool,
        feature_extractor: Module,
        encoder: Module,
        aux: Optional[Module] = None,
    ):
        super().__init__()
        self.normalize_waveform = normalize_waveform
        self.feature_extractor = feature_extractor
        self.encoder = encoder
        self.aux = aux

    @torch.jit.export
    def extract_features(
        self,
        waveforms: Tensor,
        lengths: Optional[Tensor] = None,
        num_layers: Optional[int] = None,
    ) -> Tuple[List[Tensor], Optional[Tensor]]:
        """Extract feature vectors from raw waveforms

        This returns the list of outputs from the intermediate layers of
        transformer block in encoder.

        Args:
            waveforms (Tensor): Audio tensor of shape `(batch, frames)`.
            lengths (Tensor or None, optional):
                Indicates the valid length of each audio in the batch.
                Shape: `(batch, )`.
                When the ``waveforms`` contains audios with different durations,
                by providing ``lengths`` argument, the model will compute
                the corresponding valid output lengths and apply proper mask in
                transformer attention layer.
                If ``None``, it is assumed that the entire audio waveform
                length is valid.
            num_layers (int or None, optional):
                If given, limit the number of intermediate layers to go through.
                Providing `1` will stop the computation after going through one
                intermediate layers. If not given, the outputs from all the
                intermediate layers are returned.

        Returns:
            (List[Tensor], Optional[Tensor]):
            List of Tensors
                Features from requested layers.
                Each Tensor is of shape: `(batch, time frame, feature dimension)`
            Tensor or None
                If ``lengths`` argument was provided, a Tensor of shape `(batch, )`
                is returned.
                It indicates the valid length in time axis of each feature Tensor.
        """
        if self.normalize_waveform:
            if lengths is not None:
                waveforms = [
                    F.layer_norm(wave[:length], (length,)) for wave, length in zip(waveforms, lengths)
                ]
                waveforms = torch.nn.utils.rnn.pad_sequence(waveforms, batch_first=True)
            else:
                waveforms = F.layer_norm(waveforms, waveforms.shape[-1:])

        x, lengths = self.feature_extractor(waveforms, lengths)
        x = self.encoder.extract_features(x, lengths, num_layers)   # (num_layers+1,), including the input
        return x, lengths
    
    def get_num_params(self):
        """Calculate the current size."""
        feature_extractor_size, encoder_in_features = self.feature_extractor.get_num_params_and_final_out_channels()
        encoder_size = self.encoder.get_num_params(encoder_in_features)
        return feature_extractor_size + encoder_size
    
    def prune(self):
        self.eval()     # must be in eval mode
        conv_config, conv_out_index = self.feature_extractor.prune()    # [(output_channel, kernel_size, stride), ...]
        transformer_config = self.encoder.prune(conv_out_index)     # NOTE: this is a defaultdict(list)
        use_attention = transformer_config["use_attention"]
        use_feed_forward = transformer_config["use_feed_forward"]
        num_heads = transformer_config["num_heads"]     # can be []
        remaining_heads = transformer_config["remaining_heads"]     # can be []
        ff_interm_features = transformer_config["ff_interm_features"]

        return conv_config, use_attention, use_feed_forward, num_heads, remaining_heads, ff_interm_features

    def forward(
        self,
        waveforms: Tensor,
        lengths: Optional[Tensor] = None,
    ) -> Tuple[Tensor, Optional[Tensor]]:
        """Compute the sequence of probability distribution over labels.

        Args:
            waveforms (Tensor): Audio tensor of shape `(batch, frames)`.
            lengths (Tensor or None, optional):
                Indicates the valid length of each audio in the batch.
                Shape: `(batch, )`.
                When the ``waveforms`` contains audios with different durations,
                by providing ``lengths`` argument, the model will compute
                the corresponding valid output lengths and apply proper mask in
                transformer attention layer.
                If ``None``, it is assumed that all the audio in ``waveforms``
                have valid length. Default: ``None``.

        Returns:
            (Tensor, Optional[Tensor]):
            Tensor
                The sequences of probability distribution (in logit) over labels.
                Shape: `(batch, frames, num labels)`.
            Tensor or None
                If ``lengths`` argument was provided, a Tensor of shape `(batch, )`
                is returned.
                It indicates the valid length in time axis of the output Tensor.
        """
        if self.normalize_waveform:
            if lengths is not None:
                waveforms = [
                    F.layer_norm(wave[:length], (length,)) for wave, length in zip(waveforms, lengths)
                ]
                waveforms = torch.nn.utils.rnn.pad_sequence(waveforms, batch_first=True)
            else:
                waveforms = F.layer_norm(waveforms, waveforms.shape[-1:])

        x, lengths = self.feature_extractor(waveforms, lengths)
        x = self.encoder(x, lengths)
        if self.aux is not None:
            x = self.aux(x)
        return x, lengths


def wav2vec2_model(**configs) -> Wav2Vec2Model:
    """Wraps the original wav2vec2_model and wavlm_model."""

    if "encoder_remaining_heads" in configs:
        return wavlm_model(**configs)
    
    return wav2vec2_model_original(**configs)


def wav2vec2_model_original(
    extractor_mode: str,
    extractor_conv_layer_config: Optional[List[Tuple[int, int, int]]],
    extractor_conv_bias: bool,
    encoder_embed_dim: int,
    encoder_projection_dropout: float,
    encoder_pos_conv_kernel: int,
    encoder_pos_conv_groups: int,
    encoder_num_layers: int,
    encoder_use_attention: List[bool],
    encoder_use_feed_forward: List[bool],
    encoder_num_heads: List[int],
    encoder_head_dim: int,
    encoder_attention_dropout: float,
    encoder_ff_interm_features: List[int],
    encoder_ff_interm_dropout: float,
    encoder_dropout: float,
    encoder_layer_norm_first: bool,
    encoder_layer_drop: float,
    aux_num_out: Optional[int],
    normalize_waveform: bool,
    extractor_prune_conv_channels: bool = False,
    encoder_prune_attention_heads: bool = False,
    encoder_prune_attention_layer: bool = False,
    encoder_prune_feed_forward_intermediate: bool = False,
    encoder_prune_feed_forward_layer: bool = False,
) -> Wav2Vec2Model:
    """Builds custom :class:`~torchaudio.models.Wav2Vec2Model`.

    Note:
        The "feature extractor" below corresponds to
        `ConvFeatureExtractionModel <https://github.com/pytorch/fairseq/blob/dd3bd3c0497ae9a7ae7364404a6b0a4c501780b3/fairseq/models/wav2vec/wav2vec2.py#L736>`__
        in the original ``fairseq`` implementation.
        This is referred as "(convolutional) feature encoder" in the *wav2vec 2.0*
        :cite:`baevski2020wav2vec` paper.

        The "encoder" below corresponds to `TransformerEncoder <https://github.com/pytorch/fairseq/blob/dd3bd3c0497ae9a7ae7364404a6b0a4c501780b3/fairseq/models/wav2vec/wav2vec2.py#L817>`__,
        and this is referred as "Transformer" in the paper.

    Args:
        extractor_mode (str): Operation mode of feature extractor.
            Valid values are ``"group_norm"`` or ``"layer_norm"``.
            If ``"group_norm"``, then a single normalization is applied
            in the first convolution block. Otherwise, all the convolution
            blocks will have layer normalization.

            This option corresponds to ``extractor_mode`` from ``fairseq``.
        extractor_conv_layer_config (list of integer tuples or None):
            Configuration of convolution layers in feature extractor.
            List of convolution configuration,
            i.e. ``[(output_channel, kernel_size, stride), ...]``

            If ``None`` is provided, then the following default value is used.

            .. code-block:: python

               [
                 (512, 10, 5),
                 (512, 3, 2),
                 (512, 3, 2),
                 (512, 3, 2),
                 (512, 3, 2),
                 (512, 2, 2),
                 (512, 2, 2),
               ]

            This option corresponds to ``conv_feature_layers`` from ``fairseq``.

        extractor_conv_bias (bool):
            Whether to include bias term to each convolution operation.

            This option corresponds to ``conv_bias`` from ``fairseq``.

        encoder_embed_dim (int):
            The dimension of embedding in encoder.

            This option corresponds to ``encoder_embed_dim`` from ``fairseq``.

        encoder_projection_dropout (float):
            The dropout probability applied after the input feature is projected
            to ``encoder_embed_dim``.

            This option corresponds to ``dropout_input`` from ``fairseq``.

        encoder_pos_conv_kernel (int):
            The kernel size of convolutional positional embeddings.

            This option corresponds to ``conv_pos`` from ``fairseq``.

        encoder_pos_conv_groups (int):
            The number of groups of convolutional positional embeddings.

            This option corresponds to ``conv_pos_groups`` from ``fairseq``.

        encoder_num_layers (int):
            The number of self attention layers in transformer block.

            This option corresponds to ``encoder_layers`` from ``fairseq``.

        encoder_num_heads (int):
            The number of heads in self attention layers.

            This option corresponds to ``encoder_attention_heads`` from ``fairseq``.

        encoder_attention_dropout (float):
            The dropout probability applied after softmax in self-attention layer.

            This option corresponds to ``attention_dropout`` from ``fairseq``.

        encoder_ff_interm_features (int):
            The dimension of hidden features in feed forward layer.

            This option corresponds to ``encoder_ffn_embed_dim`` from ``fairseq``.

        encoder_ff_interm_dropout (float):
            The dropout probability applied in feedforward layer.

            This option correspinds to ``activation_dropout`` from ``fairseq``.

        encoder_dropout (float):
            The dropout probability applied at the end of feed forward layer.

            This option corresponds to ``dropout`` from ``fairseq``.

        encoder_layer_norm_first (bool):
            Control the order of layer norm in transformer layer and each encoder layer.
            If True, in transformer layer, layer norm is applied before features are fed
            to encoder layers. In encoder layer, two layer norms are applied before and after
            self attention.
            If False, in transformer layer, layer norm is applied after features are fed
            to encoder layers. In encoder layer, two layer norms are applied after self
            attention, before and after feed forward.

            This option corresponds to ``layer_norm_first`` from ``fairseq``.

        encoder_layer_drop (float):
            Probability to drop each encoder layer during training.

            This option corresponds to ``layerdrop`` from ``fairseq``.

        aux_num_out (int or None):
            When provided, attach an extra linear layer on top of encoder, which can be
            used for fine-tuning.

    Returns:
        Wav2Vec2Model:
            The resulting model.
    """  # noqa: E501
    if extractor_conv_layer_config is None:
        extractor_conv_layer_config = [(512, 10, 5)] + [(512, 3, 2)] * 4 + [(512, 2, 2)] * 2

    feature_extractor = components._get_feature_extractor(
        extractor_mode, extractor_conv_layer_config, extractor_conv_bias, 
        prune_conv_channels=extractor_prune_conv_channels,
    )
    encoder = components._get_encoder(
        in_features=extractor_conv_layer_config[-1][0],
        embed_dim=encoder_embed_dim,
        dropout_input=encoder_projection_dropout,
        pos_conv_kernel=encoder_pos_conv_kernel,
        pos_conv_groups=encoder_pos_conv_groups,
        num_layers=encoder_num_layers,
        use_attention=encoder_use_attention,
        use_feed_forward=encoder_use_feed_forward,
        num_heads=encoder_num_heads,
        head_dim=encoder_head_dim,
        attention_dropout=encoder_attention_dropout,
        ff_interm_features=encoder_ff_interm_features,
        ff_interm_dropout=encoder_ff_interm_dropout,
        dropout=encoder_dropout,
        layer_norm_first=encoder_layer_norm_first,
        layer_drop=encoder_layer_drop,
        prune_attention_heads=encoder_prune_attention_heads,
        prune_attention_layer=encoder_prune_attention_layer,
        prune_feed_forward_intermediate=encoder_prune_feed_forward_intermediate,
        prune_feed_forward_layer=encoder_prune_feed_forward_layer,
    )
    aux = None
    if aux_num_out is not None:
        aux = torch.nn.Linear(in_features=encoder_embed_dim, out_features=aux_num_out)
    return Wav2Vec2Model(normalize_waveform, feature_extractor, encoder, aux)

def wavlm_model(
    extractor_mode: str,
    extractor_conv_layer_config: Optional[List[Tuple[int, int, int]]],
    extractor_conv_bias: bool,
    encoder_embed_dim: int,
    encoder_projection_dropout: float,
    encoder_pos_conv_kernel: int,
    encoder_pos_conv_groups: int,
    encoder_num_layers: int,
    encoder_use_attention: List[bool],
    encoder_use_feed_forward: List[bool],
    encoder_total_num_heads: List[int],
    encoder_remaining_heads: List[List[int]],
    encoder_num_buckets: int,
    encoder_max_distance: int,
    encoder_attention_dropout: float,
    encoder_ff_interm_features: List[int],
    encoder_ff_interm_dropout: float,
    encoder_dropout: float,
    encoder_layer_norm_first: bool,
    encoder_layer_drop: float,
    aux_num_out: Optional[int],
    normalize_waveform: bool,
    extractor_prune_conv_channels: bool = False,
    encoder_prune_attention_heads: bool = False,
    encoder_prune_attention_layer: bool = False,
    encoder_prune_feed_forward_intermediate: bool = False,
    encoder_prune_feed_forward_layer: bool = False,
) -> Wav2Vec2Model:
    """Builds custom WaveLM model :cite:`chen2022wavlm`. The architecture is compatible
    with Wav2Vec2 model :cite:`baevski2020wav2vec`, and so the output object is
    :class:`~torchaudio.models.Wav2Vec2Model`. Most of the arguments have the same meaning
    as in :py:func:`wav2vec2_model` so please refer there for documentation.

    Args:
        extractor_mode (str): Operation mode of feature extractor.
            See :py:func:`wav2vec2_model`.

        extractor_conv_layer_config (list of integer tuples or None):
            See :py:func:`wav2vec2_model`.

        extractor_conv_bias (bool):
            See :py:func:`wav2vec2_model`.

        encoder_embed_dim (int):
            See :py:func:`wav2vec2_model`.

        encoder_projection_dropout (float):
            See :py:func:`wav2vec2_model`.

        encoder_pos_conv_kernel (int):
            See :py:func:`wav2vec2_model`.

        encoder_pos_conv_groups (int):
            See :py:func:`wav2vec2_model`.

        encoder_num_layers (int):
            See :py:func:`wav2vec2_model`.

        encoder_num_heads (int):
            See :py:func:`wav2vec2_model`.

        encoder_num_buckets (int):
            Number of buckets for relative position embedding.
        encoder_max_distance (int):
            Maximum distance for relative position embedding.

        encoder_attention_dropout (float):
            See :py:func:`wav2vec2_model`.

        encoder_ff_interm_features (int):
            See :py:func:`wav2vec2_model`.

        encoder_ff_interm_dropout (float):
            See :py:func:`wav2vec2_model`.

        encoder_dropout (float):
            See :py:func:`wav2vec2_model`.

        encoder_layer_norm_first (bool):
            See :py:func:`wav2vec2_model`.

        encoder_layer_drop (float):
            See :py:func:`wav2vec2_model`.

        aux_num_out (int or None):
            See :py:func:`wav2vec2_model`.

    Returns:
        Wav2Vec2Model:
            The resulting model.
    """
    if extractor_conv_layer_config is None:
        extractor_conv_layer_config = [(512, 10, 5)] + [(512, 3, 2)] * 4 + [(512, 2, 2)] * 2

    feature_extractor = components._get_feature_extractor(
        extractor_mode, extractor_conv_layer_config, extractor_conv_bias,
        prune_conv_channels=extractor_prune_conv_channels,
    )
    encoder = components._get_wavlm_encoder(
        in_features=extractor_conv_layer_config[-1][0],
        embed_dim=encoder_embed_dim,
        dropout_input=encoder_projection_dropout,
        pos_conv_kernel=encoder_pos_conv_kernel,
        pos_conv_groups=encoder_pos_conv_groups,
        num_layers=encoder_num_layers,
        use_attention=encoder_use_attention,
        use_feed_forward=encoder_use_feed_forward,
        total_num_heads=encoder_total_num_heads,
        remaining_heads=encoder_remaining_heads,
        num_buckets=encoder_num_buckets,
        max_distance=encoder_max_distance,
        attention_dropout=encoder_attention_dropout,
        ff_interm_features=encoder_ff_interm_features,
        ff_interm_dropout=encoder_ff_interm_dropout,
        dropout=encoder_dropout,
        layer_norm_first=encoder_layer_norm_first,
        layer_drop=encoder_layer_drop,
        prune_attention_heads=encoder_prune_attention_heads,
        prune_attention_layer=encoder_prune_attention_layer,
        prune_feed_forward_intermediate=encoder_prune_feed_forward_intermediate,
        prune_feed_forward_layer=encoder_prune_feed_forward_layer,
    )
    aux = None
    if aux_num_out is not None:
        aux = torch.nn.Linear(in_features=encoder_embed_dim, out_features=aux_num_out)
    return Wav2Vec2Model(normalize_waveform, feature_extractor, encoder, aux)


def wavlm_base(
    encoder_projection_dropout: float = 0.1,
    encoder_attention_dropout: float = 0.1,
    encoder_ff_interm_dropout: float = 0.1,
    encoder_dropout: float = 0.1,
    encoder_layer_drop: float = 0.1,
    aux_num_out: Optional[int] = None,
) -> Wav2Vec2Model:
    """Builds "base" WaveLM model :cite:`chen2022wavlm`. The architecture is compatible
    with Wav2Vec2 model :cite:`baevski2020wav2vec`, and so the output class is
    :class:`~torchaudio.models.Wav2Vec2Model`.

    Args:
        encoder_projection_dropout (float):
            See :py:func:`wav2vec2_model`.
        encoder_attention_dropout (float):
            See :py:func:`wav2vec2_model`.
        encoder_ff_interm_dropout (float):
            See :py:func:`wav2vec2_model`.
        encoder_dropout (float):
            See :py:func:`wav2vec2_model`.
        encoder_layer_drop (float):
            See :py:func:`wav2vec2_model`.
        aux_num_out (int, optional):
            See :py:func:`wav2vec2_model`.

    Returns:
        Wav2Vec2Model:
            The resulting model.
    """
    return wavlm_model(
        extractor_mode="group_norm",
        extractor_conv_layer_config=None,
        extractor_conv_bias=False,
        encoder_embed_dim=768,
        encoder_projection_dropout=encoder_projection_dropout,
        encoder_pos_conv_kernel=128,
        encoder_pos_conv_groups=16,
        encoder_num_layers=12,
        encoder_num_heads=12,
        encoder_num_buckets=320,
        encoder_max_distance=800,
        encoder_attention_dropout=encoder_attention_dropout,
        encoder_ff_interm_features=3072,
        encoder_ff_interm_dropout=encoder_ff_interm_dropout,
        encoder_dropout=encoder_dropout,
        encoder_layer_norm_first=False,
        encoder_layer_drop=encoder_layer_drop,
        aux_num_out=aux_num_out,
    )
```

## File: `src/linacodec/module/fsq.py`
```python
# Finite Scalar Quantization: https://arxiv.org/abs/2309.15505

import torch
from torch import nn

from ..util import get_logger

logger = get_logger()


def round_ste(z: torch.Tensor) -> torch.Tensor:
    """Round with straight through gradients."""
    zhat = z.round()
    return z + (zhat - z).detach()


def get_entropy(prob: torch.Tensor, eps: float = 1e-10) -> torch.Tensor:
    return -torch.sum(prob * torch.log(prob + eps), dim=-1)


class FSQ(nn.Module):
    def __init__(self, levels: list[int]):
        super().__init__()
        self.levels = levels
        self.dim = len(levels)

        _levels = torch.tensor(levels, dtype=torch.long)
        self.register_buffer("_levels", _levels, persistent=False)
        _basis = torch.cumprod(torch.tensor([1] + levels[:-1]), dim=0, dtype=torch.long)
        self.register_buffer("_basis", _basis, persistent=False)

    def bound(self, z: torch.Tensor, eps: float = 1e-3) -> torch.Tensor:
        """Bound `z`, an array of shape (..., d)."""
        half_l = (self._levels - 1) * (1 - eps) / 2
        offset = torch.where(self._levels % 2 == 0, 0.5, 0.0)
        shift = (offset / half_l).tan()
        return (z + shift).tanh() * half_l - offset

    def quantize(self, z: torch.Tensor) -> torch.Tensor:
        """Quantizes z, returns quantized zhat, same shape as z."""
        quantized = round_ste(self.bound(z))
        half_width = self._levels // 2  # Renormalize to [-1, 1].
        return quantized / half_width

    def _scale_and_shift(self, zhat_normalized: torch.Tensor) -> torch.Tensor:
        half_width = self._levels // 2
        return (zhat_normalized * half_width) + half_width

    def _scale_and_shift_inverse(self, zhat: torch.Tensor) -> torch.Tensor:
        half_width = self._levels // 2
        return (zhat - half_width) / half_width

    def codes_to_indices(self, zhat: torch.Tensor) -> torch.Tensor:
        """Converts a `code` to an index in the codebook."""
        # (B, T, C) -> (B, T)
        assert zhat.shape[-1] == len(self.levels)
        zhat = self._scale_and_shift(zhat)
        return (zhat * self._basis.to(torch.float64)).to(torch.long).sum(dim=-1)

    def indices_to_codes(self, indices: torch.Tensor) -> torch.Tensor:
        """Inverse of `codes_to_indices`."""
        # (B, T) -> (B, T, C)
        indices = indices.unsqueeze(-1)
        codes_non_centered = (indices // self._basis) % self._levels
        return self._scale_and_shift_inverse(codes_non_centered)

    def encode(self, z: torch.Tensor) -> torch.Tensor:
        z_q = self.quantize(z)
        indices = self.codes_to_indices(z_q)  # (B, T)
        return z_q, indices

    def decode(self, indices: torch.Tensor) -> torch.Tensor:
        z_q = self.indices_to_codes(indices)  # (B, T, C)
        return z_q

    def forward(self, z: torch.Tensor):
        z_q = self.quantize(z)
        indices = self.codes_to_indices(z_q)  # (B, T)
        return z_q, indices


class FiniteScalarQuantizer(nn.Module):
    def __init__(self, input_dim: int, output_dim: int, levels: list[int]) -> None:
        super().__init__()
        self.input_dim_ = input_dim
        self.output_dim_ = output_dim

        self.fsq = FSQ(levels)
        logger.debug(
            f"Finite Scalar Quantizer with levels: {levels}, input_dim: {input_dim}, output_dim: {output_dim}, codebook_size: {self.all_codebook_size}"
        )

        self.proj_in = nn.Linear(input_dim, len(levels)) if len(levels) != input_dim else nn.Identity()
        self.proj_out = nn.Linear(len(levels), output_dim) if len(levels) != output_dim else nn.Identity()

    def build_codebook(self) -> None:
        pass

    @property
    def output_dim(self) -> int:
        return self.output_dim_

    @property
    def all_codebook_size(self) -> int:
        size = 1
        for level in self.fsq.levels:
            size *= level
        return size

    def forward(self, z: torch.Tensor) -> tuple[torch.Tensor, dict]:
        latent = self.proj_in(z)  # Latent projected by proj_in
        quantized_latent, indices = self.fsq(latent)  # Quantized latent before proj_out
        z_q = self.proj_out(quantized_latent)

        # Compute perplexity from used indices distribution
        flat_indices = indices.view(-1)
        unique_indices, counts = torch.unique(flat_indices, return_counts=True)
        used_indices_probs = counts.float() / flat_indices.numel()
        entropy = get_entropy(used_indices_probs)
        perplexity = torch.exp(entropy)

        info_dict = {
            "latent": latent,
            "quantized_latent": quantized_latent,
            "indices": indices,
            "perplexity": perplexity,
        }
        return z_q, info_dict

    def encode(self, z: torch.Tensor, skip_proj: bool = False) -> tuple[torch.Tensor, torch.Tensor]:
        z = self.proj_in(z)
        z_q, indices = self.fsq.encode(z)
        if not skip_proj:
            z_q = self.proj_out(z_q)
        return z_q, indices

    def decode(self, indices: torch.Tensor) -> torch.Tensor:
        z_q = self.fsq.decode(indices)
        z_q = self.proj_out(z_q)
        return z_q
```

## File: `src/linacodec/module/global_encoder.py`
```python
# Adapted from: https://github.com/microsoft/UniSpeech/blob/main/downstreams/speaker_verification/models/ecapa_tdnn.py

import torch
import torch.nn as nn

from .convnext import ConvNextBackbone


class AttentiveStatsPool(nn.Module):
    def __init__(self, input_channels: int, output_channels: int, attention_channels: int = 128):
        super().__init__()

        self.attn = nn.Sequential(
            nn.Conv1d(input_channels, attention_channels, kernel_size=1),
            nn.Tanh(),
            nn.Conv1d(attention_channels, input_channels, kernel_size=1),
            nn.Softmax(dim=2),
        )
        self.proj = nn.Linear(input_channels * 2, output_channels)
        self.norm = nn.LayerNorm(output_channels)

    def forward(self, x):
        alpha = self.attn(x)

        mean = torch.sum(alpha * x, dim=2)
        residuals = torch.sum(alpha * (x**2), dim=2) - mean**2
        std = torch.sqrt(residuals.clamp(min=1e-4, max=1e4))

        x = torch.cat([mean, std], dim=1)
        return self.norm(self.proj(x))


class GlobalEncoder(nn.Module):
    def __init__(
        self,
        input_channels: int,
        output_channels: int,
        dim: int,
        intermediate_dim: int,
        num_layers: int,
        skip_embed: bool = False,
        attention_channels: int = 128,
        use_attn_pool: bool = True,
    ):
        super().__init__()

        self.backbone = ConvNextBackbone(
            input_channels=input_channels,
            dim=dim,
            intermediate_dim=intermediate_dim,
            num_layers=num_layers,
            skip_embed=skip_embed,
        )
        if use_attn_pool:
            self.pooling = AttentiveStatsPool(
                input_channels=dim, output_channels=output_channels, attention_channels=attention_channels
            )
        else:
            self.pooling = nn.Sequential(
                nn.AdaptiveAvgPool1d(1),
                nn.Flatten(1),
                nn.Linear(dim, output_channels),
                nn.LayerNorm(output_channels),
            )
        self.output_channels = output_channels

    @property
    def output_dim(self):
        return self.output_channels

    def forward(self, x):
        features = self.backbone(x)
        # (B, T, C) -> (B, C, T)
        features = features.transpose(1, 2)
        return self.pooling(features)  # (B, C_out)
```

## File: `src/linacodec/module/hardconcrete.py`
```python
import math

import torch
import torch.nn as nn


class HardConcrete(nn.Module):
    """A HarcConcrete module.
    Use this module to create a mask of size N, which you can
    then use to perform L0 regularization.

    To obtain a mask, simply run a forward pass through the module
    with no input data. The mask is sampled in training mode, and
    fixed during evaluation mode, e.g.:

    >>> module = HardConcrete(n_in=100)
    >>> mask = module()
    >>> norm = module.l0_norm()
    """

    def __init__(
        self,
        n_in: int,
        init_mean: float = 0.5,
        init_std: float = 0.01,
        temperature: float = 2/3,     # from CoFi
        stretch: float = 0.1,
        eps: float = 1e-6
    ) -> None:
        """Initialize the HardConcrete module.
        Parameters
        ----------
        n_in : int
            The number of hard concrete variables in this mask.
        init_mean : float, optional
            Initial drop rate for hard concrete parameter,
            by default 0.5.,
        init_std: float, optional
            Used to initialize the hard concrete parameters,
            by default 0.01.
        temperature : float, optional
            Temperature used to control the sharpness of the
            distribution, by default 1.0
        stretch : float, optional
            Stretch the sampled value from [0, 1] to the interval
            [-stretch, 1 + stretch], by default 0.1.
        """
        super().__init__()

        self.n_in = n_in
        self.limit_l = -stretch
        self.limit_r = 1.0 + stretch
        self.log_alpha = nn.Parameter(torch.zeros(n_in))
        self.beta = temperature
        self.init_mean = init_mean
        self.init_std = init_std
        self.bias = -self.beta * math.log(-self.limit_l / self.limit_r)

        self.eps = eps
        self.compiled_mask = None
        self.reset_parameters()

    def reset_parameters(self):
        """Reset the parameters of this module."""
        self.compiled_mask = None
        mean = math.log(1 - self.init_mean) - math.log(self.init_mean)
        self.log_alpha.data.normal_(mean, self.init_std)

    def l0_norm(self) -> torch.Tensor:
        """Compute the expected L0 norm of this mask.
        Returns
        -------
        torch.Tensor
            The expected L0 norm.
        """
        return (self.log_alpha + self.bias).sigmoid().sum()

    def forward(self) -> torch.Tensor:
        """Sample a hard concrete mask.
        Returns
        -------
        torch.Tensor
            The sampled binary mask
        """
        if self.training:
            # Reset the compiled mask
            self.compiled_mask = None
            # Sample mask dynamically
            u = self.log_alpha.new(self.n_in).uniform_(self.eps, 1 - self.eps)
            s = torch.sigmoid((torch.log(u / (1 - u)) + self.log_alpha) / self.beta)
            s = s * (self.limit_r - self.limit_l) + self.limit_l
            mask = s.clamp(min=0., max=1.)

        else:
            # Compile new mask if not cached
            if self.compiled_mask is None:
                # Get expected sparsity
                expected_num_zeros = self.n_in - self.l0_norm().item()
                num_zeros = round(expected_num_zeros)
                # Approximate expected value of each mask variable z;
                # We use an empirically validated magic number 0.8
                soft_mask = torch.sigmoid(self.log_alpha / self.beta * 0.8)
                # Prune small values to set to 0
                _, indices = torch.topk(soft_mask, k=num_zeros, largest=False)
                soft_mask[indices] = 0.
                self.compiled_mask = soft_mask
            mask = self.compiled_mask

        return mask

    def extra_repr(self) -> str:
        return str(self.n_in)

    def __repr__(self) -> str:
        return "{}({})".format(self.__class__.__name__, self.extra_repr())
```

## File: `src/linacodec/module/postnet.py`
```python
# Adapted from: https://github.com/ming024/FastSpeech2

import torch
import torch.nn as nn


def get_padding(kernel_size: int, dilation: int = 1):
    return ((kernel_size - 1) * dilation) // 2


class Norm(nn.Module):
    def __init__(self, channels: int):
        super().__init__()
        self.norm = nn.LayerNorm(channels)

    def forward(self, x):
        # (batch_size, channels, sequence_length)
        x = x.transpose(1, 2)
        x = self.norm(x)
        return x.transpose(1, 2)


class PostNet(nn.Module):
    def __init__(
        self,
        input_channels: int = 100,
        channels: int = 512,
        kernel_size: int = 5,
        num_layers: int = 5,
        dropout: float = 0.5,
        use_layer_norm: bool = False,
    ):
        super().__init__()

        padding = get_padding(kernel_size)
        self.convolutions = nn.ModuleList()

        self.convolutions.append(
            nn.Sequential(
                nn.Conv1d(input_channels, channels, kernel_size=kernel_size, padding=padding),
                Norm(channels) if use_layer_norm else nn.BatchNorm1d(channels),
            )
        )
        for i in range(1, num_layers - 1):
            self.convolutions.append(
                nn.Sequential(
                    nn.Conv1d(channels, channels, kernel_size=kernel_size, padding=padding),
                    Norm(channels) if use_layer_norm else nn.BatchNorm1d(channels),
                )
            )
        self.convolutions.append(
            nn.Sequential(
                nn.Conv1d(channels, input_channels, kernel_size=kernel_size, padding=padding),
                Norm(input_channels) if use_layer_norm else nn.BatchNorm1d(input_channels),
            )
        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        residual = x

        for i in range(len(self.convolutions) - 1):
            x = self.convolutions[i](x)
            x = torch.tanh(x)
            x = self.dropout(x)

        x = self.convolutions[-1](x)
        x = self.dropout(x)

        return x + residual
```

## File: `src/linacodec/module/pruning_utils.py`
```python
"""Utility functions for pruning."""

from typing import Union

import torch
import torch.nn as nn


def prune_linear_layer(layer: nn.Linear, index: torch.LongTensor, dim: str):
    "Prune linear layer in place."
    # NOTE: weight: (out_features, in_features), bias: (out_features,)
    if dim == "input":
        dim = 1
        layer.in_features = len(index)
    elif dim == "output":
        dim = 0
        layer.out_features = len(index)
    else:
        raise ValueError

    layer.weight = nn.Parameter(layer.weight.index_select(dim, index).clone().detach())
    if layer.bias is not None and dim == 0:
        layer.bias = nn.Parameter(layer.bias.index_select(0, index).clone().detach())


def prune_conv1d_layer(layer: nn.Conv1d, index: torch.LongTensor, dim: str):
    """Prune conv1d in place."""
    # NOTE: weight: (out_channels, in_channels, kernel_size), bias: (out_channels,)
    if dim == "input":
        dim = 1
        layer.in_channels = len(index)
    elif dim == "output":
        dim = 0
        layer.out_channels = len(index)
    else:
        raise ValueError
    
    layer.weight = nn.Parameter(layer.weight.index_select(dim, index).clone().detach())
    if layer.bias is not None and dim == 0:
        layer.bias = nn.Parameter(layer.bias.index_select(0, index).clone().detach())


def prune_layer_norm(layernorm: Union[nn.LayerNorm, nn.GroupNorm], index: torch.LongTensor):
    """Prune layer norm or group norm in place."""
    layernorm.weight = nn.Parameter(layernorm.weight.index_select(0, index).clone().detach())
    layernorm.bias = nn.Parameter(layernorm.bias.index_select(0, index).clone().detach())
    if isinstance(layernorm, nn.LayerNorm):
        layernorm.normalized_shape = (len(index),)
    elif isinstance(layernorm, nn.GroupNorm):
        layernorm.num_groups = len(index)
        layernorm.num_channels = len(index)
```

## File: `src/linacodec/module/ssl_extractor.py`
```python
import torch
import torch.nn as nn
import torchaudio
import torchaudio.pipelines as pipelines
from torchaudio.models.wav2vec2 import Wav2Vec2Model
from torchaudio.models.wav2vec2.components import ConvLayerBlock

from ..util import get_logger

logger = get_logger()


# Map of friendly names to torchaudio pipeline bundles
MODEL_REGISTRY = {
    "wav2vec2_base": pipelines.WAV2VEC2_BASE,
    "wav2vec2_large": pipelines.WAV2VEC2_LARGE,
    "wav2vec2_large_lv60k": pipelines.WAV2VEC2_LARGE_LV60K,
    "hubert_base": pipelines.HUBERT_BASE,
    "hubert_large": pipelines.HUBERT_LARGE,
    "hubert_xlarge": pipelines.HUBERT_XLARGE,
    "wavlm_base": pipelines.WAVLM_BASE,
    "wavlm_base_plus": pipelines.WAVLM_BASE_PLUS,
    "wavlm_large": pipelines.WAVLM_LARGE,
}


class SSLFeatureExtractor(nn.Module):
    def __init__(self, model_name: str = "wavlm_base_plus", output_layer: int | None = None, sample_rate: int = 16000):
        """
        Args:
            model_name: Name of the SSL model to use
            output_layer: Which layer's features to extract (None for last layer), 1-based indexing
            sample_rate: Sample rate of input audio
        """
        super().__init__()
        self.output_layer = output_layer if output_layer is not None else -1

        if model_name not in MODEL_REGISTRY:
            raise ValueError(f"Unknown model: {model_name}. Available models: {list(MODEL_REGISTRY.keys())}")
        bundle = MODEL_REGISTRY[model_name]
        self.model: Wav2Vec2Model = bundle.get_model()
        self.model.eval()
        self.feature_dim: int = bundle._params["encoder_embed_dim"]

        self.ssl_sample_rate = bundle.sample_rate
        # Create resampler if needed
        if sample_rate != self.ssl_sample_rate:
            logger.debug(f"Resampling from {sample_rate} to {self.ssl_sample_rate} required by {model_name}.")
            self.resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=self.ssl_sample_rate)
        else:
            self.resampler = None

    @property
    def hop_size(self) -> int:
        """Get the hop size of the model's convolutional layers."""
        hop_size = 1
        for _, stride in self.conv_config:
            hop_size *= stride
        return hop_size

    @property
    def conv_config(self) -> list[tuple[int, int]]:
        """Get the configuration of the convolutional layers in the model."""
        conv_layers = []
        for layer in self.model.feature_extractor.conv_layers:
            layer: ConvLayerBlock
            conv_layers.append((layer.kernel_size, layer.stride))
        return conv_layers

    def get_minimum_input_length(self, desired_output_length: int) -> int:
        """Calculate the minimum input length required to produce a given output length."""
        length = desired_output_length
        for kernel_size, stride in reversed(self.conv_config):
            length = (length - 1) * stride + kernel_size
        return length

    @torch.no_grad()
    def forward(
        self,
        waveform: torch.Tensor,
        lengths: torch.Tensor | None = None,
        num_layers: int | None = None,
        return_lengths: bool = False,
    ) -> list[torch.Tensor]:
        """
        Args:
            waveform: (batch_size, num_samples)
            lengths: Optional tensor of sequence lengths for each batch item (used for attention masking)

        Returns:
            features: List of feature tensors for each layer (batch_size, frame, dim)
            lengths: Sequence lengths for each batch item
        """
        if waveform.dim() == 1:
            waveform = waveform.unsqueeze(0)
        # Resample if needed
        if self.resampler is not None:
            waveform = self.resampler(waveform)

        features, feature_lengths = self.model.extract_features(
            waveform, lengths, num_layers=num_layers or self.output_layer
        )

        if return_lengths:
            return features, feature_lengths
        return features
```

## File: `src/linacodec/module/transformer.py`
```python
# Adapted from https://github.com/meta-llama/llama3/blob/main/llama/model.py
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.


import torch
import torch.nn.functional as F
from torch import nn

from ..util import get_logger
from .adaln_zero import AdaLNZero


logger = get_logger()


try:
    from flash_attn import flash_attn_func, flash_attn_with_kvcache

    FLASH_ATTN_AVAILABLE = True
except ImportError:
    FLASH_ATTN_AVAILABLE = False


def precompute_freqs_cis(dim: int, end: int, theta: float = 10000.0):
    freqs = 1.0 / (theta ** (torch.arange(0, dim, 2)[: (dim // 2)].float() / dim))
    t = torch.arange(end, device=freqs.device, dtype=torch.float32)
    freqs = torch.outer(t, freqs)
    freqs_cis = torch.polar(torch.ones_like(freqs), freqs)  # complex64
    return freqs_cis


def reshape_for_broadcast(freqs_cis: torch.Tensor, x: torch.Tensor):
    ndim = x.ndim
    assert 0 <= 1 < ndim
    assert freqs_cis.shape == (x.shape[1], x.shape[-1])
    shape = [d if i == 1 or i == ndim - 1 else 1 for i, d in enumerate(x.shape)]
    return freqs_cis.view(*shape)


def apply_rotary_emb(x: torch.Tensor, freqs_cis: torch.Tensor) -> torch.Tensor:
    x_ = torch.view_as_complex(x.float().reshape(*x.shape[:-1], -1, 2))
    freqs_cis = reshape_for_broadcast(freqs_cis, x_)
    x_out = torch.view_as_real(x_ * freqs_cis).flatten(3)
    return x_out.type_as(x)


class Attention(nn.Module):
    def __init__(
        self,
        dim: int,
        n_heads: int,
        dropout: float,
        window_size: int | None,
        qkv_bias: bool = False,
        proj_bias: bool = False,
        use_flash_attention: bool = False,
        causal: bool = False,
    ):
        super().__init__()
        self.n_heads = n_heads
        self.head_dim = dim // n_heads

        self.wq = nn.Linear(dim, n_heads * self.head_dim, bias=qkv_bias)
        self.wk = nn.Linear(dim, n_heads * self.head_dim, bias=qkv_bias)
        self.wv = nn.Linear(dim, n_heads * self.head_dim, bias=qkv_bias)
        self.wo = nn.Linear(n_heads * self.head_dim, dim, bias=proj_bias)

        self.scale = self.head_dim**-0.5
        self.dropout = dropout

        # Enable local attention if window_size is specified
        self.use_local_attention = window_size is not None
        if self.use_local_attention:
            assert window_size % 2 == 1, "Window size must be odd for local attention."
            self.window_per_side = window_size // 2

        self.use_flash_attention = use_flash_attention

        self.causal = causal

    def create_mask(
        self, bsz: int, seqlen: int, mask: torch.Tensor | None, device: torch.device
    ) -> torch.Tensor | None:
        """Create attention mask combining provided mask and local attention constraints"""
        if not self.use_local_attention and mask is None:
            return None

        # Start with all positions allowed
        attn_mask = torch.ones((seqlen, seqlen), dtype=torch.bool, device=device)

        if self.causal:
            # Causal mask: no future positions allowed
            attn_mask = torch.tril(attn_mask)

        # Apply local attention constraints
        if self.use_local_attention:
            attn_mask = torch.triu(attn_mask, diagonal=-self.window_per_side)
            attn_mask = torch.tril(attn_mask, diagonal=self.window_per_side)

        # Expand mask to batch size
        attn_mask = attn_mask.unsqueeze(0).expand(bsz, -1, -1)

        # Apply global mask if provided
        if mask is not None:
            assert mask.shape[-1] == seqlen and mask.shape[-2] == seqlen, (
                "Mask must be square and match sequence length."
            )
            # Ensure mask has correct batch dimensions
            if mask.dim() == 2:
                mask = mask.unsqueeze(0).expand(bsz, -1, -1)
            attn_mask = attn_mask & mask

        # Expand to head dimension
        attn_mask = attn_mask.unsqueeze(1).expand(-1, self.n_heads, -1, -1)
        return attn_mask

    def forward(
        self,
        x: torch.Tensor,
        freqs_cis: torch.Tensor | None,
        mask: torch.Tensor | None,
        return_kv: bool = False,
    ) -> torch.Tensor | tuple[torch.Tensor, tuple[torch.Tensor, torch.Tensor]]:
        """Forward pass for multi-head attention.
        Args:
            x (torch.Tensor): Input tensor of shape (bsz, seqlen, dim).
            freqs_cis (torch.Tensor, optional): Precomputed rotary frequencies.
            mask (torch.Tensor, optional): Attention mask.
            return_kv (bool): Whether to return KV pairs for caching.
        Returns:
            output (torch.Tensor): Output tensor of shape (bsz, seqlen, dim).
            new_kv (tuple, optional): KV pairs if return_kv is True.
        """
        bsz, seqlen, _ = x.shape
        xq, xk, xv = self.wq(x), self.wk(x), self.wv(x)

        xq = xq.view(bsz, seqlen, self.n_heads, self.head_dim)
        xk = xk.view(bsz, seqlen, self.n_heads, self.head_dim)
        xv = xv.view(bsz, seqlen, self.n_heads, self.head_dim)

        # Apply rotary embeddings if provided
        if freqs_cis is not None:
            xq = apply_rotary_emb(xq, freqs_cis=freqs_cis[:seqlen])
            xk = apply_rotary_emb(xk, freqs_cis=freqs_cis[:seqlen])

        if self.use_flash_attention and FLASH_ATTN_AVAILABLE:
            assert mask is None, "Flash attention does not support arbitrary masking."

            # Flash Attention
            window_size = (self.window_per_side, self.window_per_side) if self.use_local_attention else (-1, -1)
            output = flash_attn_func(
                xq,  # (bsz, seqlen, n_heads, head_dim)
                xk,  # (bsz, seqlen, n_heads, head_dim)
                xv,  # (bsz, seqlen, n_heads, head_dim)
                dropout_p=(self.dropout if self.training else 0.0),
                softmax_scale=self.scale,
                window_size=window_size,
                causal=self.causal,
            )  # (bsz, seqlen, n_heads, head_dim)

        else:
            attn_mask = self.create_mask(bsz, seqlen, mask, x.device)

            # SDPA Attention
            output = F.scaled_dot_product_attention(
                xq.transpose(1, 2),  # (bsz, n_heads, seqlen, head_dim)
                xk.transpose(1, 2),  # (bsz, n_heads, seqlen, head_dim)
                xv.transpose(1, 2),  # (bsz, n_heads, seqlen, head_dim)
                attn_mask=attn_mask,  # (bsz, n_heads, seqlen, seqlen) boolean mask
                dropout_p=self.dropout,
                scale=self.scale,
            ).transpose(1, 2)  # (bsz, seqlen, n_heads, head_dim)

        output = output.contiguous().view(bsz, seqlen, -1)
        output = self.wo(output)

        if return_kv:
            return output, (xk, xv)
        return output

    def forward_with_cache(
        self,
        x: torch.Tensor,
        kv_cache: tuple[torch.Tensor, torch.Tensor],
        freqs_cis: torch.Tensor,
        start_pos: int,
    ) -> tuple[torch.Tensor, tuple[torch.Tensor, torch.Tensor]]:
        """
        Forward pass with KV cache for efficient inference. Only used for inference.

        Args:
            x (torch.Tensor): Input tensor for the current step. Shape: (bsz, 1, dim)
            kv_cache: A tuple of (key_cache, value_cache) from previous steps.
            start_pos (int): The starting position of the new token in the sequence.
            freqs_cis (torch.Tensor): Precomputed rotary frequencies.

        Returns:
            output (torch.Tensor): Output tensor after attention. Shape: (bsz, 1, dim)
            new_kv (tuple): Updated KV cache including the new key and value.
        """
        bsz, seqlen, _ = x.shape
        assert seqlen == 1, "KV cache method is designed for single-token generation."

        xq, xk, xv = self.wq(x), self.wk(x), self.wv(x)

        xq = xq.view(bsz, seqlen, self.n_heads, self.head_dim)
        xk = xk.view(bsz, seqlen, self.n_heads, self.head_dim)
        xv = xv.view(bsz, seqlen, self.n_heads, self.head_dim)

        # Apply rotary embeddings using the correct positional slice
        xq = apply_rotary_emb(xq, freqs_cis=freqs_cis[start_pos : start_pos + seqlen])
        xk = apply_rotary_emb(xk, freqs_cis=freqs_cis[start_pos : start_pos + seqlen])

        # Update the KV cache
        k_cache, v_cache = kv_cache
        new_kv = (xk, xv)
        xk = torch.cat([k_cache, xk], dim=1)
        xv = torch.cat([v_cache, xv], dim=1)

        # For single token generation, causal mask is implicitly handled.
        # We attend to all keys (prefix + previous tokens).
        if self.use_flash_attention and FLASH_ATTN_AVAILABLE:
            # Flash Attention
            output = flash_attn_with_kvcache(
                xq,  # (bsz, 1, n_heads, head_dim)
                xk,  # (bsz, 1+kv_len, n_heads, head_dim)
                xv,  # (bsz, 1+kv_len, n_heads, head_dim)
                softmax_scale=self.scale,
            )  # (bsz, 1, n_heads, head_dim)
        else:
            # SDPA Attention
            output = F.scaled_dot_product_attention(
                xq.transpose(1, 2),  # (bsz, n_heads, 1, head_dim)
                xk.transpose(1, 2),  # (bsz, n_heads, 1+kv_len, head_dim)
                xv.transpose(1, 2),  # (bsz, n_heads, 1+kv_len, head_dim)
                scale=self.scale,
            ).transpose(1, 2)  # (bsz, 1, n_heads, head_dim)

        output = output.contiguous().view(bsz, seqlen, -1)
        return self.wo(output), new_kv


class FeedForward(nn.Module):
    def __init__(
        self,
        dim: int,
        hidden_dim: int,
        multiple_of: int,
        ffn_dim_multiplier: float | None,
    ):
        super().__init__()
        hidden_dim = int(2 * hidden_dim / 3)
        # custom dim factor multiplier
        if ffn_dim_multiplier is not None:
            hidden_dim = int(ffn_dim_multiplier * hidden_dim)
        hidden_dim = multiple_of * ((hidden_dim + multiple_of - 1) // multiple_of)

        self.w1 = nn.Linear(dim, hidden_dim, bias=False)
        self.w2 = nn.Linear(hidden_dim, dim, bias=False)
        self.w3 = nn.Linear(dim, hidden_dim, bias=False)

    def forward(self, x):
        return self.w2(F.silu(self.w1(x)) * self.w3(x))


class TransformerBlock(nn.Module):
    def __init__(
        self,
        dim: int,
        n_heads: int,
        qkv_bias: bool,
        proj_bias: bool,
        window_size: int | None,
        multiple_of: int,
        ffn_dim_multiplier: float | None,
        dropout: float,
        norm_eps: float,
        adanorm_condition_dim: int | None = None,
        use_flash_attention: bool = False,
        use_adaln_zero: bool = False,
        causal: bool = False,
    ):
        super().__init__()
        self.attention = Attention(
            dim=dim,
            n_heads=n_heads,
            dropout=dropout,
            window_size=window_size,
            use_flash_attention=use_flash_attention,
            qkv_bias=qkv_bias,
            proj_bias=proj_bias,
            causal=causal,
        )

        self.feed_forward = FeedForward(
            dim=dim,
            hidden_dim=4 * dim,
            multiple_of=multiple_of,
            ffn_dim_multiplier=ffn_dim_multiplier,
        )

        # Choose between AdaLNZero and regular LayerNorm
        self.use_adaln_zero = use_adaln_zero
        if self.use_adaln_zero:
            assert adanorm_condition_dim is not None, "condition_dim must be provided when using AdaLNZero"
            self.attention_norm = AdaLNZero(dim, adanorm_condition_dim, eps=norm_eps, return_gate=True)
            self.ffn_norm = AdaLNZero(dim, adanorm_condition_dim, eps=norm_eps, return_gate=True)
        else:
            self.attention_norm = nn.LayerNorm(dim, eps=norm_eps)
            self.ffn_norm = nn.LayerNorm(dim, eps=norm_eps)

    def forward(
        self,
        x: torch.Tensor,
        freqs_cis: torch.Tensor | None,
        mask: torch.Tensor | None,
        condition: torch.Tensor | None = None,
        return_kv: bool = False,
        kv_cache: tuple[torch.Tensor, torch.Tensor] | None = None,
        start_pos: int | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, tuple[torch.Tensor, torch.Tensor]]:
        """
        Forward pass for a single Transformer block.
        Args:
            x (torch.Tensor): Input tensor of shape (bsz, seqlen, dim).
            freqs_cis (torch.Tensor, optional): Precomputed rotary frequencies.
            mask (torch.Tensor, optional): Attention mask.
            condition (torch.Tensor, optional): Conditioning tensor for AdaLNZero.
            return_kv (bool): Whether to return KV pairs for caching.
            kv_cache (tuple, optional): KV cache for efficient inference.
            start_pos (int, optional): Starting position for KV cache.
        Returns:
            out (torch.Tensor): Output tensor of shape (bsz, seqlen, dim).
            new_kv (tuple, optional): New KV pairs if return_kv is True or kv_cache is provided.
        """
        # Apply normalization
        if self.use_adaln_zero:
            assert condition is not None, "condition must be provided when using AdaLNZero"
            attn_normed, attn_gate = self.attention_norm(x, condition=condition)
        else:
            attn_normed = self.attention_norm(x)

        # Forward attention with KV cache if provided
        new_kv = None
        if kv_cache is not None and start_pos is not None:
            # Use KV cache for efficient inference
            attn_out, new_kv = self.attention.forward_with_cache(attn_normed, kv_cache, freqs_cis, start_pos)
        elif return_kv:
            # Return KV pairs for caching
            attn_out, new_kv = self.attention(attn_normed, freqs_cis, mask, return_kv=True)
        else:
            attn_out = self.attention(attn_normed, freqs_cis, mask)

        # Apply gating for attention if using AdaLNZero
        if self.use_adaln_zero:
            h = x + attn_gate * attn_out  # residual + gate * x
        else:
            h = x + attn_out

        # Apply normalization for feedforward
        if self.use_adaln_zero:
            ffn_normed, ffn_gate = self.ffn_norm(h, condition=condition)
        else:
            ffn_normed = self.ffn_norm(h)

        ffn_out = self.feed_forward(ffn_normed)

        # Apply gating for feedforward if using AdaLNZero
        if self.use_adaln_zero:
            out = h + ffn_gate * ffn_out  # residual + gate * x
        else:
            out = h + ffn_out

        # If using KV cache, return the new KV pairs
        if new_kv is not None:
            return out, new_kv
        return out


class Transformer(nn.Module):
    def __init__(
        self,
        dim: int = 4096,
        n_layers: int = 32,
        n_heads: int = 32,
        qkv_bias: bool = False,
        proj_bias: bool = False,
        window_size: int | None = None,
        multiple_of: int = 256,
        ffn_dim_multiplier: float | None = None,
        dropout: float = 0.1,
        norm_eps: float = 1e-5,
        use_rope: bool = True,
        rope_theta: float = 500000.0,
        max_seq_len: int = 2048,
        input_dim: int | None = None,
        output_dim: int | None = None,
        adanorm_condition_dim: int | None = None,
        use_flash_attention: bool = False,
        use_adaln_zero: bool = False,
        use_xavier_init: bool = True,
        causal: bool = False,
    ):
        super().__init__()
        self.dim = dim
        self.n_heads = n_heads
        self.rope_theta = rope_theta
        self.use_adaln_zero = use_adaln_zero

        self.layers = nn.ModuleList()
        for layer_id in range(n_layers):
            self.layers.append(
                TransformerBlock(
                    dim=dim,
                    n_heads=n_heads,
                    window_size=window_size,
                    multiple_of=multiple_of,
                    ffn_dim_multiplier=ffn_dim_multiplier,
                    dropout=dropout,
                    qkv_bias=qkv_bias,
                    proj_bias=proj_bias,
                    norm_eps=norm_eps,
                    adanorm_condition_dim=adanorm_condition_dim,
                    use_flash_attention=use_flash_attention,
                    use_adaln_zero=use_adaln_zero,
                    causal=causal,
                )
            )

        # Choose between AdaLNZero (without gate) and regular LayerNorm for final norm
        if self.use_adaln_zero:
            assert adanorm_condition_dim is not None, "condition_dim must be provided when using AdaLNZero"
            self.norm = AdaLNZero(dim, adanorm_condition_dim, eps=norm_eps, return_gate=False)
        else:
            self.norm = nn.LayerNorm(dim, eps=norm_eps)
        self.input_proj = nn.Linear(input_dim, dim) if input_dim is not None else nn.Identity()
        self.output_proj = nn.Linear(dim, output_dim) if output_dim is not None else nn.Identity()
        self.output_dim_ = output_dim if output_dim is not None else dim

        if use_rope:
            self.freqs_cis = precompute_freqs_cis(dim // n_heads, max_seq_len * 2, rope_theta)
            logger.debug(
                f"Using RoPE with theta={rope_theta}, max_seq_len={max_seq_len}, "
                f"dim={dim}, n_heads={n_heads}, freqs_cis shape={self.freqs_cis.shape}"
            )
        else:
            self.freqs_cis = None

        if window_size is not None:
            logger.debug(f"Using local attention with window size {window_size}")

        if self.use_adaln_zero:
            logger.debug(f"Using AdaLNZero conditioning with condition_dim={adanorm_condition_dim}")

        if use_flash_attention:
            logger.debug("Using Flash Attention for memory-efficient attention computation")

        if use_xavier_init:
            logger.debug("Using Xavier initialization for linear layers")
            self.apply(self._init_weights)
            self.apply(self._init_adaln_zero)

    @property
    def output_dim(self) -> int:
        return self.output_dim_

    def _init_weights(self, module: nn.Module):
        if isinstance(module, nn.Linear):
            nn.init.xavier_normal_(module.weight)
            if module.bias is not None:
                nn.init.zeros_(module.bias)

    def _init_adaln_zero(self, module: nn.Module):
        if isinstance(module, AdaLNZero):
            # Initialize condition projection weights to zero
            nn.init.zeros_(module.condition_proj[1].weight)
            nn.init.zeros_(module.condition_proj[1].bias)

    def forward(
        self,
        x: torch.Tensor,
        mask: torch.Tensor | None = None,
        condition: torch.Tensor | None = None,
        return_kv: bool = False,
        kv_cache: list[tuple[torch.Tensor, torch.Tensor]] | None = None,
        start_pos: int | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, list[tuple[torch.Tensor, torch.Tensor]]]:
        """
        Forward pass for the Transformer model.
        Args:
            x (torch.Tensor): Input tensor of shape (bsz, seqlen, input_dim).
            mask (torch.Tensor, optional): Attention mask.
            condition (torch.Tensor, optional): Conditioning tensor for AdaLNZero.
            return_kv (bool): Whether to return KV pairs for caching.
            kv_cache (list, optional): List of KV caches for each layer for efficient inference.
            start_pos (int, optional): Starting position for KV cache.
        Returns:
            output (torch.Tensor): Output tensor of shape (bsz, seqlen, output_dim).
            new_kv_list (list, optional): List of new KV pairs for each layer if return_kv is True or kv_cache is provided.
        """
        bsz, seqlen, _dim = x.shape

        if self.use_adaln_zero:
            assert condition is not None, "condition must be provided when using AdaLNZero"

        # Rotary embeddings
        if self.freqs_cis is not None:
            # Recompute freqs_cis if the sequence length or starting position exceeds the precomputed length
            expected_len = (start_pos + 1) if start_pos is not None else seqlen
            if expected_len > self.freqs_cis.shape[0]:
                logger.warning(
                    f"Input sequence length {expected_len} exceeds precomputed RoPE length {self.freqs_cis.shape[0]}. Recomputing freqs_cis."
                )
                self.freqs_cis = precompute_freqs_cis(self.dim // self.n_heads, expected_len * 4, self.rope_theta)

            self.freqs_cis = self.freqs_cis.to(x.device)
            freqs_cis = self.freqs_cis
        else:
            freqs_cis = None

        x = self.input_proj(x)
        new_kv_list = []
        for i, layer in enumerate(self.layers):
            # Collect KV cache if provided
            if kv_cache is not None and start_pos is not None:
                x, new_kv = layer(x, freqs_cis, mask, condition, kv_cache=kv_cache[i], start_pos=start_pos)
                new_kv_list.append(new_kv)
            elif return_kv:
                x, new_kv = layer(x, freqs_cis, mask, condition, return_kv=True)
                new_kv_list.append(new_kv)
            else:
                x = layer(x, freqs_cis, mask, condition)

        # Apply final normalization
        if self.use_adaln_zero:
            x, _ = self.norm(x, condition=condition)  # Final norm doesn't use gate
        else:
            x = self.norm(x)

        output = self.output_proj(x)

        # If using KV cache, return the new KV pairs
        if new_kv_list:
            return output, new_kv_list
        return output
```

## File: `src/linacodec/vocoder/linkwitz.py`
```python
import torch

## linkwitz_riley FFT Crossover. Original 48khz audio has slight phase issues with limited training data, this fixes the issue with 99% speed.
def crossover_merge_linkwitz_riley(path1_48k, path2_48k, sample_rate=48000, cutoff=4000, transition_bins=8):
    # 1. Frequency Domain
    spec1 = torch.fft.rfft(path1_48k)
    spec2 = torch.fft.rfft(path2_48k)

    n_bins = spec1.size(-1)
    cutoff_bin = int((cutoff / (sample_rate / 2)) * n_bins)

    # 2. Linkwitz-Riley / Butterworth Taper
    # This creates a "Flatter" response than Hann or Sigmoid
    mask = torch.ones(n_bins, device=spec1.device)
    
    half = transition_bins // 2
    start = max(0, cutoff_bin - half)
    end = min(n_bins, cutoff_bin + half)
    actual_width = end - start

    # Create a 4th-order-like steepness (very transparent)
    # We use a normalized frequency vector from -1 to 1 across the transition
    x = torch.linspace(-1, 1, steps=actual_width, device=spec1.device)
    
    # This polynomial approximates a Linkwitz-Riley transition:
    # It stays flatter longer than a Sigmoid but is smoother than Linear.
    fade = 0.5 * (x * (3 - x**2) * 0.5 + 0.5) 
    # Or for extreme transparency, use a Cubic Hermite:
    fade = 3 * torch.pow((x + 1) / 2, 2) - 2 * torch.pow((x + 1) / 2, 3)

    mask[:start] = 0
    mask[start:end] = fade
    mask[end:] = 1

    # 3. Direct Complex Merge
    merged_spec = (spec1 * mask) + (spec2 * (1.0 - mask))

    return torch.fft.irfft(merged_spec, n=path1_48k.size(-1))
```

## File: `src/linacodec/vocoder/upsampler_block.py`
```python
## Upsampler block is custom hifigan based upsampling block used to upscale vocos backbone features. Modified it to use snake function for faster training.

import warnings
from typing import Any, List, Optional, Tuple

import torch
from torch import Tensor, nn
from torch import Tensor, nn
from typing import Any, List, Optional, Tuple
from torch.nn.utils.parametrizations import weight_norm

@torch.jit.script
def snake(x, alpha):
    shape = x.shape
    x = x.reshape(shape[0], shape[1], -1)
    x = x + (alpha + 1e-9).reciprocal() * torch.sin(alpha * x).pow(2)
    x = x.reshape(shape)
    return x


class Snake1d(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.alpha = nn.Parameter(torch.ones(1, channels, 1))

    def forward(self, x):
        return snake(x, self.alpha)

def nonlinearity(x):
    return x * torch.sigmoid(x)


def Normalize(in_channels, num_groups=32):
    return torch.nn.GroupNorm(num_groups=num_groups, num_channels=in_channels, eps=1e-6, affine=True)

class ResnetBlock(nn.Module):
    def __init__(self, *, in_channels, out_channels=None, conv_shortcut=False,
                 dropout, temb_channels=512):
        super().__init__()
        self.in_channels = in_channels
        out_channels = in_channels if out_channels is None else out_channels
        self.out_channels = out_channels
        self.use_conv_shortcut = conv_shortcut
        self.snake1 = Snake1d(in_channels)
        self.norm1 = Normalize(in_channels)
        self.conv1 = torch.nn.Conv1d(in_channels,
                                     out_channels,
                                     kernel_size=3,
                                     stride=1,
                                     padding=1)
        if temb_channels > 0:
            self.temb_proj = torch.nn.Linear(temb_channels,
                                             out_channels)
        self.norm2 = Normalize(out_channels)
        self.dropout = torch.nn.Dropout(dropout)
        self.conv2 = torch.nn.Conv1d(out_channels,
                                     out_channels,
                                     kernel_size=3,
                                     stride=1,
                                     padding=1)
        self.snake2 = Snake1d(out_channels)
        if self.in_channels != self.out_channels:
            if self.use_conv_shortcut:
                self.conv_shortcut = torch.nn.Conv1d(in_channels,
                                                     out_channels,
                                                     kernel_size=3,
                                                     stride=1,
                                                     padding=1)
            else:
                self.nin_shortcut = torch.nn.Conv1d(in_channels,
                                                    out_channels,
                                                    kernel_size=1,
                                                    stride=1,
                                                    padding=0)

    def forward(self, x, temb=None):
        h = x
        h = self.norm1(h)
        h = self.snake1(h)
        h = self.conv1(h)

        if temb is not None:
            h = h + self.temb_proj(nonlinearity(temb))[:, :, None]

        h = self.norm2(h)
        h = self.snake2(h)
        h = self.dropout(h)
        h = self.conv2(h)

        if self.in_channels != self.out_channels:
            if self.use_conv_shortcut:
                x = self.conv_shortcut(x)
            else:
                x = self.nin_shortcut(x)

        return x + h
class UpSamplerBlock(nn.Module):
    """Transpose Conv plus Resnet Blocks to upsample feature embedding."""
    def __init__(self, in_channels: int, upsample_factors: List[int], kernel_sizes: Optional[List[int]] = None):
        super().__init__()
        self.in_channels = in_channels
        self.upsample_factors = list(upsample_factors or [])
        self.kernel_sizes = list(kernel_sizes or [8] * len(self.upsample_factors))

        assert len(self.kernel_sizes) == len(self.upsample_factors), "kernel_sizes and upsample_factors must have the same length"

        self.upsample_layers = nn.ModuleList()
        self.resnet_blocks  = nn.ModuleList()
        self.out_proj = nn.Linear(self.in_channels // (2 ** len(self.upsample_factors)), self.in_channels, bias=True)

        for i, (k, u) in enumerate(zip(self.kernel_sizes, self.upsample_factors)):
            c_in  = self.in_channels // (2 ** i)
            c_out = self.in_channels // (2 ** (i + 1))
            self.upsample_layers.append(
                weight_norm(nn.ConvTranspose1d(c_in, c_out, kernel_size=k, stride=u, padding=(k - u) // 2))
            )
            self.resnet_blocks.append(
                ResnetBlock(in_channels=c_out, out_channels=c_out, dropout=0.0, temb_channels=0)
            )
        self.final_snake = Snake1d(self.in_channels)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: [B, C, L] -> ... -> [B, C', L']
        for up, rsblk in zip(self.upsample_layers, self.resnet_blocks):
            x = rsblk(up(x))
        x = self.out_proj(x.transpose(1, 2))

        # 2. Transpose back for Snake: [B, L, C_high] -> [B, C_high, L]
        x = x.transpose(1, 2)
        return self.final_snake(x)
      
def init_weights(m):
    if isinstance(m, nn.Conv1d) or isinstance(m, nn.ConvTranspose1d):
        # Xavier initialization helps keep signal variance steady
        nn.init.xavier_uniform_(m.weight)
        if m.bias is not None:
            nn.init.constant_(m.bias, 0)
    elif isinstance(m, nn.Linear):
        nn.init.trunc_normal_(m.weight, std=0.02)
        if m.bias is not None:
            nn.init.constant_(m.bias, 0)
    elif isinstance(m, Snake1d):
        # Crucial: Start alpha at 1.0.
        # Too high = noisy; too low = linear.
        nn.init.constant_(m.alpha, 1.0)
```

## File: `src/linacodec/vocoder/vocos.py`
```python
from __future__ import annotations

from typing import Any, Dict, Tuple, Union, Optional

import torch
import yaml
from huggingface_hub import hf_hub_download
from torch import nn
from vocos.feature_extractors import FeatureExtractor, EncodecFeatures
from vocos.heads import FourierHead
from vocos.models import Backbone
from vocos.heads import ISTFTHead
from torch.cuda.amp import autocast
import torchaudio.functional as AF

from .linkwitz import crossover_merge_linkwitz_riley
from .upsampler_block import UpSamplerBlock

def instantiate_class(args: Union[Any, Tuple[Any, ...]], init: Dict[str, Any]) -> Any:
    """Instantiates a class with the given args and init.

    Args:
        args: Positional arguments required for instantiation.
        init: Dict of the form {"class_path":...,"init_args":...}.

    Returns:
        The instantiated class object.
    """
    kwargs = init.get("init_args", {})
    if not isinstance(args, tuple):
        args = (args,)
    class_module, class_name = init["class_path"].rsplit(".", 1)
    module = __import__(class_module, fromlist=[class_name])
    args_class = getattr(module, class_name)
    return args_class(*args, **kwargs)


class Vocos(nn.Module):
    """
    The Vocos class represents a Fourier-based neural vocoder for audio synthesis.
    This class is primarily designed for inference, with support for loading from pretrained
    model checkpoints. It consists of three main components: a feature extractor,
    a backbone, and a head.
    """

    def __init__(
        self, feature_extractor: FeatureExtractor, backbone: Backbone, head: FourierHead, upsampler: UpSamplerBlock, head_48k: ISTFTHead,
    ):
        super().__init__()
        self.feature_extractor = feature_extractor
        self.backbone = backbone
        self.head = head
        self.upsampler = upsampler
        self.head_48k = head_48k
        self.freq_range = 4000
        self.return_48k = True

    @classmethod
    def from_hparams(cls, config_path: str) -> Vocos:
        """
        Class method to create a new Vocos model instance from hyperparameters stored in a yaml configuration file.
        """
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        feature_extractor = instantiate_class(args=(), init=config["feature_extractor"])
        backbone = instantiate_class(args=(), init=config["backbone"])
        head = instantiate_class(args=(), init=config["head"])
        upsampler = instantiate_class(args=(), init=config["upsampler"])
        head_48k = instantiate_class(args=(), init=config["head_48k"])
        model = cls(feature_extractor=feature_extractor, backbone=backbone, head=head, upsampler=upsampler, head_48k=head_48k)
        return model

    @classmethod
    def from_pretrained(cls, repo_id: str, revision: Optional[str] = None) -> Vocos:
        """
        Class method to create a new Vocos model instance from a pre-trained model stored in the Hugging Face model hub.
        """
        config_path = hf_hub_download(repo_id=repo_id, filename="config.yaml", revision=revision)
        model_path = hf_hub_download(repo_id=repo_id, filename="pytorch_model.bin", revision=revision)
        model = cls.from_hparams(config_path)
        state_dict = torch.load(model_path, map_location="cpu")
        if isinstance(model.feature_extractor, EncodecFeatures):
            encodec_parameters = {
                "feature_extractor.encodec." + key: value
                for key, value in model.feature_extractor.encodec.state_dict().items()
            }
            state_dict.update(encodec_parameters)
        model.load_state_dict(state_dict)
        model.eval()
        return model

    @torch.inference_mode()
    def forward(self, audio_input: torch.Tensor, **kwargs: Any) -> torch.Tensor:
        """
        Method to run a copy-synthesis from audio waveform. The feature extractor first processes the audio input,
        which is then passed through the backbone and the head to reconstruct the audio output.

        Args:
            audio_input (Tensor): The input tensor representing the audio waveform of shape (B, T),
                                        where B is the batch size and L is the waveform length.


        Returns:
            Tensor: The output tensor representing the reconstructed audio waveform of shape (B, T).
        """
        features = self.feature_extractor(audio_input, **kwargs)
        audio_output = self.decode(features, **kwargs)
        return audio_output

    @torch.inference_mode()
    def decode(self, features_input: torch.Tensor, **kwargs: Any) -> torch.Tensor:
        """
        Method to decode audio waveform from already calculated features. The features input is passed through
        the backbone and the head to reconstruct the audio output.

        Args:
            features_input (Tensor): The input tensor of features of shape (B, C, L), where B is the batch size,
                                     C denotes the feature dimension, and L is the sequence length.

        Returns:
            Tensor: The output tensor representing the reconstructed audio waveform of shape (B, T).
        """

        ## uses a dual path technique(one head predicts 24khz, other predicts 48khz) and then merged using sigmoid crossover for best quality in just 20 hours data!
        features = self.backbone(features_input, **kwargs).transpose(1, 2)
        upsampled_features = self.upsampler(features).transpose(1, 2)
        pred_audio = self.head_48k(upsampled_features)

        pred_audio2 = self.head(features.transpose(1, 2))
        pred_audio2 = AF.resample(pred_audio2, 24000, 48000)
        pred_audio = pred_audio[:, :pred_audio2.shape[1]]
        with autocast(enabled=False):
            merged_audio = crossover_merge_linkwitz_riley(pred_audio.float(), pred_audio2.float(), cutoff=self.freq_range)
        if self.return_48k == True:
            return merged_audio
        else:
            return pred_audio2
```

