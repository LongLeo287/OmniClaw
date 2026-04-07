---
id: voxcpm
type: knowledge
owner: OA_Triage
---
# voxcpm
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
## 🎙️ VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning


[![Project Page](https://img.shields.io/badge/Project%20Page-GitHub-blue)](https://github.com/OpenBMB/VoxCPM/) [![Technical Report](https://img.shields.io/badge/Technical%20Report-Arxiv-red)](https://arxiv.org/abs/2509.24650)[![Live Playground](https://img.shields.io/badge/Live%20PlayGround-Demo-orange)](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo) [![Samples](https://img.shields.io/badge/Audio%20Samples-Page-green)](https://openbmb.github.io/VoxCPM-demopage)

#### VoxCPM1.5 Model Weights

 [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-OpenBMB-yellow)](https://huggingface.co/openbmb/VoxCPM1.5) [![ModelScope](https://img.shields.io/badge/ModelScope-OpenBMB-purple)](https://modelscope.cn/models/OpenBMB/VoxCPM1.5)  



<div align="center">
  <img src="assets/voxcpm_logo.png" alt="VoxCPM Logo" width="40%">
  
  <a href="https://trendshift.io/repositories/17704" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17704" alt="OpenBMB%2FVoxCPM | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>



<div align="center">

👋 Contact us on [WeChat](assets/wechat.png)

</div>

## News 

* [2026.03.30] **VoxCPM2 is comming soon** 🤗
* [2025.12.05] 🎉 🎉 🎉  We Open Source the VoxCPM1.5 [weights](https://huggingface.co/openbmb/VoxCPM1.5)! The model now supports both full-parameter fine-tuning and efficient LoRA fine-tuning, empowering you to create your own tailored version. See [Release Notes](docs/release_note.md) for details.
* [2025.09.30] 🔥 🔥 🔥  We Release VoxCPM [Technical Report](https://arxiv.org/abs/2509.24650)!
* [2025.09.16] 🔥 🔥 🔥  We Open Source the VoxCPM-0.5B [weights](https://huggingface.co/openbmb/VoxCPM-0.5B)!
* [2025.09.16] 🎉 🎉 🎉  We Provide the [Gradio PlayGround](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo) for VoxCPM-0.5B, try it now! 

## Overview

VoxCPM is a novel tokenizer-free Text-to-Speech (TTS) system that redefines realism in speech synthesis. By modeling speech in a continuous space, it overcomes the limitations of discrete tokenization and enables two flagship capabilities: context-aware speech generation and true-to-life zero-shot voice cloning.

Unlike mainstream approaches that convert speech to discrete tokens, VoxCPM uses an end-to-end diffusion autoregressive architecture that directly generates continuous speech representations from text. Built on [MiniCPM-4](https://huggingface.co/openbmb/MiniCPM4-0.5B) backbone, it achieves implicit semantic-acoustic decoupling through hierachical language modeling and FSQ constraints, greatly enhancing both expressiveness and generation stability.

<div align="center">
  <img src="assets/voxcpm_model.png" alt="VoxCPM Model Architecture" width="90%">
</div>


###  🚀 Key Features
- **Context-Aware, Expressive Speech Generation** - VoxCPM comprehends text to infer and generate appropriate prosody, delivering speech with remarkable expressiveness and natural flow. It spontaneously adapts speaking style based on content, producing highly fitting vocal expression trained on a massive 1.8 million-hour bilingual corpus.
- **True-to-Life Voice Cloning** - With only a short reference audio clip, VoxCPM performs accurate zero-shot voice cloning, capturing not only the speaker's timbre but also fine-grained characteristics such as accent, emotional tone, rhythm, and pacing to create a faithful and natural replica.
- **High-Efficiency Synthesis** - VoxCPM supports streaming synthesis with a Real-Time Factor (RTF) as low as 0.17 on a consumer-grade NVIDIA RTX 4090 GPU, making it possible for real-time applications.

### 📦 Model Versions
See [Release Notes](docs/release_note.md) for details
- **VoxCPM1.5** (Latest): 
  - Model Params: 800M
  - Sampling rate of AudioVAE: 44100
  - Token rate in LM Backbone: 6.25Hz (patch-size=4)
  - RTF in a single NVIDIA-RTX 4090 GPU: ~0.15

- **VoxCPM-0.5B** (Original):
  - Model Params: 640M
  - Sampling rate of AudioVAE: 16000
  - Token rate in LM Backbone: 12.5Hz (patch-size=2)
  - RTF in a single NVIDIA-RTX 4090 GPU: 0.17



##  Quick Start

### 🔧 Install from PyPI
``` sh
pip install voxcpm
```
### 1.  Model Download (Optional)
By default, when you first run the script, the model will be downloaded automatically, but you can also download the model in advance.
- Download VoxCPM1.5
    ```
    from huggingface_hub import snapshot_download
    snapshot_download("openbmb/VoxCPM1.5")
    ```

- Or Download VoxCPM-0.5B
    ```
    from huggingface_hub import snapshot_download
    snapshot_download("openbmb/VoxCPM-0.5B")
    ```
- Download ZipEnhancer and SenseVoice-Small. We use ZipEnhancer to enhance speech prompts and SenseVoice-Small for speech prompt ASR in the web demo. 
    ```
    from modelscope import snapshot_download
    snapshot_download('iic/speech_zipenhancer_ans_multiloss_16k_base')
    snapshot_download('iic/SenseVoiceSmall')
    ```

### 2. Basic Usage
```python
import soundfile as sf
import numpy as np
from voxcpm import VoxCPM

model = VoxCPM.from_pretrained("openbmb/VoxCPM1.5")

# Non-streaming
wav = model.generate(
    text="VoxCPM is an innovative end-to-end TTS model from ModelBest, designed to generate highly expressive speech.",
    prompt_wav_path=None,      # optional: path to a prompt speech for voice cloning
    prompt_text=None,          # optional: reference text
    cfg_value=2.0,             # LM guidance on LocDiT, higher for better adherence to the prompt, but maybe worse
    inference_timesteps=10,   # LocDiT inference timesteps, higher for better result, lower for fast speed
    normalize=False,           # enable external TN tool, but will disable native raw text support
    denoise=False,             # enable external Denoise tool, but it may cause some distortion and restrict the sampling rate to 16kHz
    retry_badcase=True,        # enable retrying mode for some bad cases (unstoppable)
    retry_badcase_max_times=3,  # maximum retrying times
    retry_badcase_ratio_threshold=6.0, # maximum length restriction for bad case detection (simple but effective), it could be adjusted for slow pace speech
)

sf.write("output.wav", wav, model.tts_model.sample_rate)
print("saved: output.wav")

# Streaming
chunks = []
for chunk in model.generate_streaming(
    text = "Streaming text to speech is easy with VoxCPM!",
    # supports same args as above
):
    chunks.append(chunk)
wav = np.concatenate(chunks)

sf.write("output_streaming.wav", wav, model.tts_model.sample_rate)
print("saved: output_streaming.wav")
```

### 3. CLI Usage

After installation, the entry point is `voxcpm` (or use `python -m voxcpm.cli`).

```bash
# 1) Direct synthesis (single text)
voxcpm --text "VoxCPM is an innovative end-to-end TTS model from ModelBest, designed to generate highly expressive speech." --output out.wav

# 2) Voice cloning (reference audio + transcript)
voxcpm --text "VoxCPM is an innovative end-to-end TTS model from ModelBest, designed to generate highly expressive speech." \
  --prompt-audio path/to/voice.wav \
  --prompt-text "reference transcript" \
  --output out.wav \
  # --denoise

# (Optinal) Voice cloning (reference audio + transcript file)
voxcpm --text "VoxCPM is an innovative end-to-end TTS model from ModelBest, designed to generate highly expressive speech." \
  --prompt-audio path/to/voice.wav \
  --prompt-file "/path/to/text-file" \
  --output out.wav \
  # --denoise

# 3) Batch processing (one text per line)
voxcpm --input examples/input.txt --output-dir outs
# (optional) Batch + cloning
voxcpm --input examples/input.txt --output-dir outs \
  --prompt-audio path/to/voice.wav \
  --prompt-text "reference transcript" \
  # --denoise

# 4) Inference parameters (quality/speed)
voxcpm --text "..." --output out.wav \
  --cfg-value 2.0 --inference-timesteps 10 --normalize

# 5) Model loading
# Prefer local path
voxcpm --text "..." --output out.wav --model-path /path/to/VoxCPM_model_dir
# Or from Hugging Face (auto download/cache)
voxcpm --text "..." --output out.wav \
  --hf-model-id openbmb/VoxCPM1.5 --cache-dir ~/.cache/huggingface --local-files-only

# 6) Denoiser control
voxcpm --text "..." --output out.wav \
  --no-denoiser --zipenhancer-path iic/speech_zipenhancer_ans_multiloss_16k_base

# 7) Help
voxcpm --help
python -m voxcpm.cli --help
```

### 4. Start web demo

You can start the UI interface by running `python app.py`, which allows you to perform Voice Cloning and Voice Creation.

### 5. Fine-tuning

VoxCPM1.5 supports both full fine-tuning (SFT) and LoRA fine-tuning, allowing you to train personalized voice models on your own data. See the [Fine-tuning Guide](docs/finetune.md) for detailed instructions.

**Quick Start:**
```bash
# Full fine-tuning
python scripts/train_voxcpm_finetune.py \
    --config_path conf/voxcpm_v1.5/voxcpm_finetune_all.yaml

# LoRA fine-tuning
python scripts/train_voxcpm_finetune.py \
    --config_path conf/voxcpm_v1.5/voxcpm_finetune_lora.yaml
```

## 📚 Documentation

- **[Usage Guide](docs/usage_guide.md)** - Detailed guide on how to use VoxCPM effectively, including text input modes, voice cloning tips, and parameter tuning
- **[Fine-tuning Guide](docs/finetune.md)** - Complete guide for fine-tuning VoxCPM models with SFT and LoRA
- **[Release Notes](docs/release_note.md)** - Version history and updates
- **[Performance Benchmarks](docs/performance.md)** - Detailed performance comparisons on public benchmarks

---

## 📚 More Information

###  🌟 Community Projects
We're excited to see the VoxCPM community growing! Here are some amazing projects and features built by our community:
- **[ComfyUI-VoxCPM](https://github.com/wildminder/ComfyUI-VoxCPM)** A VoxCPM extension for ComfyUI.
- **[ComfyUI-VoxCPMTTS](https://github.com/1038lab/ComfyUI-VoxCPMTTS)** A VoxCPM extension for ComfyUI.
- **[WebUI-VoxCPM](https://github.com/rsxdalv/tts_webui_extension.vox_cpm)** A template extension for TTS WebUI.
- **[PR: Streaming API Support (by AbrahamSanders)](https://github.com/OpenBMB/VoxCPM/pull/26)** 
- **[VoxCPM-NanoVLLM](https://github.com/a710128/nanovllm-voxcpm)** NanoVLLM integration for VoxCPM for faster, high-throughput inference on GPU.
- **[VoxCPM-ONNX](https://github.com/bluryar/VoxCPM-ONNX)** ONNX export for VoxCPM supports faster CPU inference.
- **[VoxCPMANE](https://github.com/0seba/VoxCPMANE)** VoxCPM TTS with Apple Neural Engine backend server.
- **[PR: LoRA finetune web UI (by Ayin1412)](https://github.com/OpenBMB/VoxCPM/pull/100)**
- **[voxcpm_rs](https://github.com/madushan1000/voxcpm_rs)** A re-implementation of VoxCPM-0.5B in Rust.

*Note: The projects are not officially maintained by OpenBMB.*



*Have you built something cool with VoxCPM? We'd love to feature it here! Please open an issue or pull request to add your project.*

### 📊 Performance Highlights

VoxCPM achieves competitive results on public zero-shot TTS benchmarks. See [Performance Benchmarks](docs/performance.md) for detailed comparison tables.



## ⚠️ Risks and limitations
- General Model Behavior: While VoxCPM has been trained on a large-scale dataset, it may still produce outputs that are unexpected, biased, or contain artifacts.
- Potential for Misuse of Voice Cloning: VoxCPM's powerful zero-shot voice cloning capability can generate highly realistic synthetic speech. This technology could be misused for creating convincing deepfakes for purposes of impersonation, fraud, or spreading disinformation. Users of this model must not use it to create content that infringes upon the rights of individuals. It is strictly forbidden to use VoxCPM for any illegal or unethical purposes. We strongly recommend that any publicly shared content generated with this model be clearly marked as AI-generated.
- Current Technical Limitations: Although generally stable, the model may occasionally exhibit instability, especially with very long or expressive inputs. Furthermore, the current version offers limited direct control over specific speech attributes like emotion or speaking style.
- Bilingual Model: VoxCPM is trained primarily on Chinese and English data. Performance on other languages is not guaranteed and may result in unpredictable or low-quality audio.
- This model is released for research and development purposes only. We do not recommend its use in production or commercial applications without rigorous testing and safety evaluations. Please use VoxCPM responsibly.

---

## 📝 TO-DO List
Please stay tuned for updates!
- [x] Release the VoxCPM technical report.
- [x] Support higher sampling rate (44.1kHz in VoxCPM-1.5).
- [x] Support SFT and LoRA fine-tuning.
- [ ] Multilingual Support (besides ZH/EN).
- [ ] Controllable Speech Generation by Human Instruction.



## 📄 License
The VoxCPM model weights and code are open-sourced under the [Apache-2.0](LICENSE) license.

## 🙏 Acknowledgments

We extend our sincere gratitude to the following works and resources for their inspiration and contributions:

- [DiTAR](https://arxiv.org/abs/2502.03930) for the diffusion autoregressive backbone used in speech generation
- [MiniCPM-4](https://github.com/OpenBMB/MiniCPM) for serving as the language model foundation
- [CosyVoice](https://github.com/FunAudioLLM/CosyVoice) for the implementation of Flow Matching-based LocDiT
- [DAC](https://github.com/descriptinc/descript-audio-codec) for providing the Audio VAE backbone

## Institutions

This project is developed by the following institutions:
- <img src="assets/modelbest_logo.png" width="28px"> [ModelBest](https://modelbest.cn/)

- <img src="assets/thuhcsi_logo.png" width="28px"> [THUHCSI](https://github.com/thuhcsi)


## ⭐ Star History
 [![Star History Chart](https://api.star-history.com/svg?repos=OpenBMB/VoxCPM&type=Date)](https://star-history.com/#OpenBMB/VoxCPM&Date)


## 📚 Citation

If you find our model helpful, please consider citing our projects 📝 and staring us ⭐️！

```bib
@article{voxcpm2025,
  title        = {VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning},
  author       = {Zhou, Yixuan and Zeng, Guoyang and Liu, Xin and Li, Xiang and Yu, Renjie and Wang, Ziyang and Ye, Runchuan and Sun, Weiyue and Gui, Jiancheng and Li, Kehan and Wu, Zhiyong  and Liu, Zhiyuan},
  journal      = {arXiv preprint arXiv:2509.24650},
  year         = {2025},
}
```

```

### File: app.py
```py
import os
import sys
import numpy as np
import torch
import gradio as gr  
import spaces
from typing import Optional, Tuple
from funasr import AutoModel
from pathlib import Path
os.environ["TOKENIZERS_PARALLELISM"] = "false"
if os.environ.get("HF_REPO_ID", "").strip() == "":
    os.environ["HF_REPO_ID"] = "openbmb/VoxCPM1.5"

import voxcpm


class VoxCPMDemo:
    def __init__(self) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"🚀 Running on device: {self.device}", file=sys.stderr)

        # ASR model for prompt text recognition
        self.asr_model_id = "iic/SenseVoiceSmall"
        self.asr_model: Optional[AutoModel] = AutoModel(
            model=self.asr_model_id,
            disable_update=True,
            log_level='DEBUG',
            device="cuda:0" if self.device == "cuda" else "cpu",
        )

        # TTS model (lazy init)
        self.voxcpm_model: Optional[voxcpm.VoxCPM] = None
        self.default_local_model_dir = "./models/VoxCPM1.5"

    # ---------- Model helpers ----------
    def _resolve_model_dir(self) -> str:
        """
        Resolve model directory:
        1) Use local checkpoint directory if exists
        2) If HF_REPO_ID env is set, download into models/{repo}
        3) Fallback to 'models'
        """
        if os.path.isdir(self.default_local_model_dir):
            return self.default_local_model_dir

        repo_id = os.environ.get("HF_REPO_ID", "").strip()
        if len(repo_id) > 0:
            target_dir = os.path.join("models", repo_id.replace("/", "__"))
            if not os.path.isdir(target_dir):
                try:
                    from huggingface_hub import snapshot_download  # type: ignore
                    os.makedirs(target_dir, exist_ok=True)
                    print(f"Downloading model from HF repo '{repo_id}' to '{target_dir}' ...", file=sys.stderr)
                    snapshot_download(repo_id=repo_id, local_dir=target_dir, local_dir_use_symlinks=False)
                except Exception as e:
                    print(f"Warning: HF download failed: {e}. Falling back to 'data'.", file=sys.stderr)
                    return "models"
            return target_dir
        return "models"

    def get_or_load_voxcpm(self) -> voxcpm.VoxCPM:
        if self.voxcpm_model is not None:
            return self.voxcpm_model
        print("Model not loaded, initializing...", file=sys.stderr)
        model_dir = self._resolve_model_dir()
        print(f"Using model dir: {model_dir}", file=sys.stderr)
        self.voxcpm_model = voxcpm.VoxCPM(voxcpm_model_path=model_dir)
        print("Model loaded successfully.", file=sys.stderr)
        return self.voxcpm_model

    # ---------- Functional endpoints ----------
    def prompt_wav_recognition(self, prompt_wav: Optional[str]) -> str:
        if prompt_wav is None:
            return ""
        res = self.asr_model.generate(input=prompt_wav, language="auto", use_itn=True)
        text = res[0]["text"].split('|>')[-1]
        return text

    def generate_tts_audio(
        self,
        text_input: str,
        prompt_wav_path_input: Optional[str] = None,
        prompt_text_input: Optional[str] = None,
        cfg_value_input: float = 2.0,
        inference_timesteps_input: int = 10,
        do_normalize: bool = True,
        denoise: bool = True,
    ) -> Tuple[int, np.ndarray]:
        """
        Generate speech from text using VoxCPM; optional reference audio for voice style guidance.
        Returns (sample_rate, waveform_numpy)
        """
        current_model = self.get_or_load_voxcpm()

        text = (text_input or "").strip()
        if len(text) == 0:
            raise ValueError("Please input text to synthesize.")

        prompt_wav_path = prompt_wav_path_input if prompt_wav_path_input else None
        prompt_text = prompt_text_input if prompt_text_input else None

        print(f"Generating audio for text: '{text[:60]}...'", file=sys.stderr)
        wav = current_model.generate(
            text=text,
            prompt_text=prompt_text,
            prompt_wav_path=prompt_wav_path,
            cfg_value=float(cfg_value_input),
            inference_timesteps=int(inference_timesteps_input),
            normalize=do_normalize,
            denoise=denoise,
        )
        return (current_model.tts_model.sample_rate, wav)


# ---------- UI Builders ----------

def create_demo_interface(demo: VoxCPMDemo):
    """Build the Gradio UI for VoxCPM demo."""
    # static assets (logo path)
    gr.set_static_paths(paths=[Path.cwd().absolute()/"assets"])

    with gr.Blocks(
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="gray",
            neutral_hue="slate",
            font=[gr.themes.GoogleFont("Inter"), "Arial", "sans-serif"]
        ),
        css="""
        .logo-container {
            text-align: center;
            margin: 0.5rem 0 1rem 0;
        }
        .logo-container img {
            height: 80px;
            width: auto;
            max-width: 200px;
            display: inline-block;
        }
        /* Bold accordion labels */
        #acc_quick details > summary,
        #acc_tips details > summary {
            font-weight: 600 !important;
            font-size: 1.1em !important;
        }
        /* Bold labels for specific checkboxes */
        #chk_denoise label,
        #chk_denoise span,
        #chk_normalize label,
        #chk_normalize span {
            font-weight: 600;
        }
        """
    ) as interface:
        # Header logo
        gr.HTML('<div class="logo-container"><img src="/gradio_api/file=assets/voxcpm_logo.png" alt="VoxCPM Logo"></div>')

        # Quick Start
        with gr.Accordion("📋 Quick Start Guide ｜快速入门", open=False, elem_id="acc_quick"):
            gr.Markdown("""
            ### How to Use ｜使用说明
            1. **(Optional) Provide a Voice Prompt** - Upload or record an audio clip to provide the desired voice characteristics for synthesis.  
               **（可选）提供参考声音** - 上传或录制一段音频，为声音合成提供音色、语调和情感等个性化特征
            2. **(Optional) Enter prompt text** - If you provided a voice prompt, enter the corresponding transcript here (auto-recognition available).  
               **（可选项）输入参考文本** - 如果提供了参考语音，请输入其对应的文本内容（支持自动识别）。
            3. **Enter target text** - Type the text you want the model to speak.  
               **输入目标文本** - 输入您希望模型朗读的文字内容。
            4. **Generate Speech** - Click the "Generate" button to create your audio.  
               **生成语音** - 点击"生成"按钮，即可为您创造出音频。
            """)

        # Pro Tips
        with gr.Accordion("💡 Pro Tips ｜使用建议", open=False, elem_id="acc_tips"):
            gr.Markdown("""
            ### Prompt Speech Enhancement｜参考语音降噪
            - **Enable** to remove background noise for a clean voice, with an external ZipEnhancer component. However, this will limit the audio sampling rate to 16kHz, restricting the cloning quality ceiling.  
              **启用**：通过 ZipEnhancer 组件消除背景噪音，但会将音频采样率限制在16kHz，限制克隆上限。
            - **Disable** to preserve the original audio's all information, including background atmosphere, and support audio cloning up to 44.1kHz sampling rate.  
              **禁用**：保留原始音频的全部信息，包括背景环境声，最高支持44.1kHz的音频复刻。

            ### Text Normalization｜文本正则化
            - **Enable** to process general text with an external WeTextProcessing component.  
              **启用**：使用 WeTextProcessing 组件，可支持常见文本的正则化处理。
            - **Disable** to use VoxCPM's native text understanding ability. For example, it supports phonemes input (For Chinese, phonemes are converted using pinyin, {ni3}{hao3}; For English, phonemes are converted using CMUDict, {HH AH0 L OW1}), try it!  
              **禁用**：将使用 VoxCPM 内置的文本理解能力。如，支持音素输入（如中文转拼音：{ni3}{hao3}；英文转CMUDict：{HH AH0 L OW1}）和公式符号合成，尝试一下！

            ### CFG Value｜CFG 值
            - **Lower CFG** if the voice prompt sounds strained or expressive, or instability occurs with long text input.  
              **调低**：如果提示语音听起来不自然或过于夸张，或者长文本输入出现稳定性问题。
            - **Higher CFG** for better adherence to the prompt speech style or input text, or instability occurs with too short text input.
              **调高**：为更好地贴合提示音频的风格或输入文本， 或者极短文本输入出现稳定性问题。

            ### Inference Timesteps｜推理时间步
            - **Lower** for faster synthesis speed.  
              **调低**：合成速度更快。
            - **Higher** for better synthesis quality.  
              **调高**：合成质量更佳。
            """)

        # Main controls
        with gr.Row():
            with gr.Column():
                prompt_wav = gr.Audio(
                    sources=["upload", 'microphone'],
                    type="filepath",
                    label="Prompt Speech (Optional, or let VoxCPM improvise)",
                    value="./examples/example.wav",
                )
                DoDenoisePromptAudio = gr.Checkbox(
                    value=False,
                    label="Prompt Speech Enhancement",
                    elem_id="chk_denoise",
                    info="We use ZipEnhancer model to denoise the prompt audio."
                )
                with gr.Row():
                    prompt_text = gr.Textbox(
                        value="Just by listening a few minutes a day, you'll be able to eliminate negative thoughts by conditioning your mind to be more positive.",
                        label="Prompt Text",
                        placeholder="Please enter the prompt text. Automatic recognition is supported, and you can correct the results yourself..."
                    )
                run_btn = gr.Button("Generate Speech", variant="primary")

            with gr.Column():
                cfg_value = gr.Slider(
                    minimum=1.0,
                    maximum=3.0,
                    value=2.0,
                    step=0.1,
                    label="CFG Value (Guidance Scale)",
                    info="Higher values increase adherence to prompt, lower values allow more creativity"
                )
                inference_timesteps = gr.Slider(
                    minimum=4,
                    maximum=30,
                    value=10,
                    step=1,
                    label="Inference Timesteps",
                    info="Number of inference timesteps for generation (higher values may improve quality but slower)"
                )
                with gr.Row():
                    text = gr.Textbox(
                        value="VoxCPM is an innovative end-to-end TTS model from ModelBest, designed to generate highly realistic speech.",
                        label="Target Text",
                    )
                with gr.Row():
                    DoNormalizeText = gr.Checkbox(
                        value=False,
                        label="Text Normalization",
                        elem_id="chk_normalize",
                        info="We use wetext library to normalize the input text."
                    )
                audio_output = gr.Audio(label="Output Audio")

        # Wiring
        run_btn.click(
            fn=demo.generate_tts_audio,
            inputs=[text, prompt_wav, prompt_text, cfg_value, inference_timesteps, DoNormalizeText, DoDenoisePromptAudio],
            outputs=[audio_output],
            show_progress=True,
            api_name="generate",
        )
        prompt_wav.change(fn=demo.prompt_wav_recognition, inputs=[prompt_wav], outputs=[prompt_text])

    return interface


def run_demo(server_name: str = "localhost", server_port: int = 7860, show_error: bool = True):
    demo = VoxCPMDemo()
    interface = create_demo_interface(demo)
    # Recommended to enable queue on Spaces for better throughput
    interface.queue(max_size=10, default_concurrency_limit=1).launch(server_name=server_name, server_port=server_port, show_error=show_error)


if __name__ == "__main__":
    run_demo()
```

### File: lora_ft_webui.py
```py
import os
import sys
import time
import glob
import json
import yaml
import shutil
import datetime
import subprocess
import threading
import gradio as gr
import torch
import soundfile as sf
from pathlib import Path
from typing import Optional, List

# Add src to sys.path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))

# Default pretrained model path relative to this repo
default_pretrained_path = str(project_root / "models" / "openbmb__VoxCPM1.5")

from voxcpm.core import VoxCPM
from voxcpm.model.voxcpm import LoRAConfig
import numpy as np
from funasr import AutoModel

# --- Localization ---
LANG_DICT = {
    "en": {
        "title": "VoxCPM LoRA WebUI",
        "tab_train": "Training",
        "tab_infer": "Inference",
        "pretrained_path": "Pretrained Model Path",
        "train_manifest": "Train Manifest (jsonl)",
        "val_manifest": "Validation Manifest (Optional)",
        "lr": "Learning Rate",
        "max_iters": "Max Iterations",
        "batch_size": "Batch Size",
        "lora_rank": "LoRA Rank",
        "lora_alpha": "LoRA Alpha",
        "save_interval": "Save Interval",
        "start_train": "Start Training",
        "stop_train": "Stop Training",
        "train_logs": "Training Logs",
        "text_to_synth": "Text to Synthesize",
        "voice_cloning": "### Voice Cloning (Optional)",
        "ref_audio": "Reference Audio",
        "ref_text": "Reference Text (Optional)",
        "select_lora": "Select LoRA Checkpoint",
        "cfg_scale": "CFG Scale",
        "infer_steps": "Inference Steps",
        "seed": "Seed",
        "gen_audio": "Generate Audio",
        "gen_output": "Generated Audio",
        "status": "Status",
        "lang_select": "Language / 语言",
        "refresh": "Refresh",
        "output_name": "Output Name (Optional, resume if exists)",
    },
    "zh": {
        "title": "VoxCPM LoRA WebUI",
        "tab_train": "训练 (Training)",
        "tab_infer": "推理 (Inference)",
        "pretrained_path": "预训练模型路径",
        "train_manifest": "训练数据清单 (jsonl)",
        "val_manifest": "验证数据清单 (可选)",
        "lr": "学习率 (Learning Rate)",
        "max_iters": "最大迭代次数",
        "batch_size": "批次大小 (Batch Size)",
        "lora_rank": "LoRA Rank",
        "lora_alpha": "LoRA Alpha",
        "save_interval": "保存间隔 (Steps)",
        "start_train": "开始训练",
        "stop_train": "停止训练",
        "train_logs": "训练日志",
        "text_to_synth": "合成文本",
        "voice_cloning": "### 声音克隆 (可选)",
        "ref_audio": "参考音频",
        "ref_text": "参考文本 (可选)",
        "select_lora": "选择 LoRA 模型",
        "cfg_scale": "CFG Scale (引导系数)",
        "infer_steps": "推理步数",
        "seed": "随机种子 (Seed)",
        "gen_audio": "生成音频",
        "gen_output": "生成结果",
        "status": "状态",
        "lang_select": "Language / 语言",
        "refresh": "刷新",
        "output_name": "输出目录名称 (可选，若存在则继续训练)",
    }
}

# Global variables
current_model: Optional[VoxCPM] = None
asr_model: Optional[AutoModel] = None
training_process: Optional[subprocess.Popen] = None
training_log = ""

def get_timestamp_str():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def get_or_load_asr_model():
    global asr_model
    if asr_model is None:
        print("Loading ASR model (SenseVoiceSmall)...", file=sys.stderr)
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        asr_model = AutoModel(
            model="iic/SenseVoiceSmall",
            disable_update=True,
            log_level='ERROR',
            device=device,
        )
    return asr_model

def recognize_audio(audio_path):
    if not audio_path:
        return ""
    try:
        model = get_or_load_asr_model()
        res = model.generate(input=audio_path, language="auto", use_itn=True)
        text = res[0]["text"].split('|>')[-1]
        return text
    except Exception as e:
        print(f"ASR Error: {e}", file=sys.stderr)
        return ""

def scan_lora_checkpoints(root_dir="lora", with_info=False):
    """
    Scans for LoRA checkpoints in the lora directory.
    
    Args:
        root_dir: Directory to scan for LoRA checkpoints
        with_info: If True, returns list of (path, base_model) tuples
    
    Returns:
        List of checkpoint paths, or list of (path, base_model) tuples if with_info=True
    """
    checkpoints = []
    if not os.path.exists(root_dir):
        os.makedirs(root_dir, exist_ok=True)
    
    # Look for lora_weights.safetensors recursively
    for root, dirs, files in os.walk(root_dir):
        if "lora_weights.safetensors" in files:
            # Use the relative path from root_dir as the ID
            rel_path = os.path.relpath(root, root_dir)
            
            if with_info:
                # Try to read base_model from lora_config.json
                base_model = None
                lora_config_file = os.path.join(root, "lora_config.json")
                if os.path.exists(lora_config_file):
                    try:
                        with open(lora_config_file, "r", encoding="utf-8") as f:
                            lora_info = json.load(f)
                        base_model = lora_info.get("base_model", "Unknown")
                    except (json.JSONDecodeError, OSError):
                        pass
                checkpoints.append((rel_path, base_model))
            else:
                checkpoints.append(rel_path)
            
    # Also check for checkpoints in the default location if they exist
    default_ckpt = "checkpoints/finetune_lora"
    if os.path.exists(os.path.join(root_dir, default_ckpt)):
         # This might be covered by the walk, but good to be sure
         pass

    return sorted(checkpoints, reverse=True)

def load_lora_config_from_checkpoint(lora_path):
    """Load LoRA config from lora_config.json if available."""
    lora_config_file = os.path.join(lora_path, "lora_config.json")
    if os.path.exists(lora_config_file):
        try:
            with open(lora_config_file, "r", encoding="utf-8") as f:
                lora_info = json.load(f)
            lora_cfg_dict = lora_info.get("lora_config", {})
            if lora_cfg_dict:
                return LoRAConfig(**lora_cfg_dict), lora_info.get("base_model")
        except Exception as e:
            print(f"Warning: Failed to load lora_config.json: {e}", file=sys.stderr)
    return None, None

def get_default_lora_config():
    """Return default LoRA config for hot-swapping support."""
    return LoRAConfig(
        enable_lm=True,
        enable_dit=True,
        r=32,
        alpha=16,
        target_modules_lm=["q_proj", "v_proj", "k_proj", "o_proj"],
        target_modules_dit=["q_proj", "v_proj", "k_proj", "o_proj"]
    )

def load_model(pretrained_path, lora_path=None):
    global current_model
    print(f"Loading model from {pretrained_path}...", file=sys.stderr)
    
    lora_config = None
    lora_weights_path = None
    
    if lora_path:
        full_lora_path = os.path.join("lora", lora_path)
        if os.path.exists(full_lora_path):
            lora_weights_path = full_lora_path
            # Try to load LoRA config from lora_config.json
            lora_config, _ = load_lora_config_from_checkpoint(full_lora_path)
            if lora_config:
                print(f"Loaded LoRA config from {full_lora_path}/lora_config.json", file=sys.stderr)
            else:
                # Fallback to default config for old checkpoints
                lora_config = get_default_lora_config()
                print("Using default LoRA config (lora_config.json not found)", file=sys.stderr)
    
    # Always init with a default LoRA config to allow hot-swapping later
    if lora_config is None:
        lora_config = get_default_lora_config()

    current_model = VoxCPM.from_pretrained(
        hf_model_id=pretrained_path,
        load_denoiser=False,
        optimize=False,
        lora_config=lora_config,
        lora_weights_path=lora_weights_path,
    )
    return "Model loaded successfully!"

def run_inference(text, prompt_wav, prompt_text, lora_selection, cfg_scale, steps, seed, pretrained_path=None):
    global current_model
    
    # 如果选择了 LoRA 模型且当前模型未加载，尝试从 LoRA config 读取 base_model
    if current_model is None:
        # 优先使用用户指定的预训练模型路径
        base_model_path = pretrained_path if pretrained_path and pretrained_path.strip() else default_pretrained_path
        
        # 如果选择了 LoRA，尝试从其 config 读取 base_model
        if lora_selection and lora_selection != "None":
            full_lora_path = os.path.join("lora", lora_selection)
            lora_config_file = os.path.join(full_lora_path, "lora_config.json")
            
            if os.path.exists(lora_config_file):
                try:
                    with open(lora_config_file, "r", encoding="utf-8") as f:
                        lora_info = json.load(f)
                    saved_base_model = lora_info.get("base_model")
                    
                    if saved_base_model:
                        # 优先使用保存的 base_model 路径
                        if os.path.exists(saved_base_model):
                            base_model_path = saved_base_model
                            print(f"Using base model from LoRA config: {base_model_path}", file=sys.stderr)
                        else:
                            print(f"Warning: Saved base_model path not found: {saved_base_model}", file=sys.stderr)
                            print(f"Falling back to default: {base_model_path}", file=sys.stderr)
                except Exception as e:
                    print(f"Warning: Failed to read base_model from LoRA config: {e}", file=sys.stderr)
        
        # 加载模型
        try:
            print(f"Loading base model: {base_model_path}", file=sys.stderr)
            status_msg = load_model(base_model_path)
            if lora_selection and lora_selection != "None":
                print(f"Model loaded for LoRA: {lora_selection}", file=sys.stderr)
        except Exception as e:
            error_msg = f"Failed to load model from {base_model_path}: {str(e)}"
            print(error_msg, file=sys.stderr)
            return None, error_msg

    # Handle LoRA hot-swapping
    if lora_selection and lora_selection != "None":
        full_lora_path = os.path.join("lora", lora_selection)
        print(f"Hot-loading LoRA: {full_lora_path}", file=sys.stderr)
        try:
            current_model.load_lora(full_lora_path)
            current_model.set_lora_enabled(True)
        except Exception as e:
            print(f"Error loading LoRA: {e}", file=sys.stderr)
            return None, f"Error loading LoRA: {e}"
    else:
        print("Disabling LoRA", file=sys.stderr)
        current_model.set_lora_enabled(False)

    if seed != -1:
        torch.manual_seed(seed)
        np.random.seed(seed)

    # 处理 prompt 参数：必须同时为 None 或同时有值
    final_prompt_wav = None
    final_prompt_text = None
    
    if prompt_wav and prompt_wav.strip():
        # 有参考音频
        final_prompt_wav = prompt_wav
        
        # 如果没有提供参考文本，尝试自动识别
        if not prompt_text or not prompt_text.strip():
            print("参考音频已提供但缺少文本，自动识别中...", file=sys.stderr)
            try:
                final_prompt_text = recognize_audio(prompt_wav)
                if final_prompt_text:
                    print(f"自动识别文本: {final_prompt_text}", file=sys.stderr)
                else:
                    return None, "错误：无法识别参考音频内容，请手动填写参考文本"
            except Exception as e:
                return None, f"错误：自动识别参考音频失败 - {str(e)}"
        else:
            final_prompt_text = prompt_text.strip()
    # 如果没有参考音频，两个都设为 None（用于零样本 TTS）

    try:
        audio_np = current_model.generate(
            text=text,
            prompt_wav_path=final_prompt_wav,
            prompt_text=final_prompt_text,
            cfg_value=cfg_scale,
            inference_timesteps=steps,
            denoise=False 
        )
        return (current_model.tts_model.sample_rate, audio_np), "Generation Success"
    except Exception as e:
        import traceback
        traceback.print_exc()
        return None, f"Error: {str(e)}"

def start_training(
    pretrained_path,
    train_manifest,
    val_manifest,
    learning_rate,
    num_iters,
    batch_size,
    lora_rank,
    lora_alpha,
    save_interval,
    output_name="",
    # Advanced options
    grad_accum_steps=1,
    num_workers=2,
    log_interval=10,
    valid_interval=1000,
    weight_decay=0.01,
    warmup_steps=100,
    max_steps=None,
    sample_rate=44100,
    # LoRA advanced
    enable_lm=True,
    enable_dit=True,
    enable_proj=False,
    dropout=0.0,
    tensorboard_path="",
    # Distribution options
    hf_model_id="",
    distribute=False,
):
    global training_process, training_log
    
    if training_process is not None and training_process.poll() is None:
        return "Training is already running!"

    if output_name and output_name.strip():
        timestamp = output_name.strip()
    else:
        timestamp = get_timestamp_str()

    save_dir = os.path.join("lora", timestamp)
    checkpoints_dir = os.path.join(save_dir, "checkpoints")
    logs_dir = os.path.join(save_dir, "logs")
    
    os.makedirs(checkpoints_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)

    # Create config dictionary
    # Resolve max_steps default
    resolved_max_steps = int(max_steps) if max_steps not in (None, "", 0) else int(num_iters)

    config = {
        "pretrained_path": pretrained_path,
        "train_manifest": train_manifest,
        "val_manifest": val_manifest,
        "sample_rate": int(sample_rate),
        "batch_size": int(batch_size),
        "grad_accum_steps": int(grad_accum_steps),
        "num_workers": int(num_workers),
        "num_iters": int(num_iters),
        "log_interval": int(log_interval),
        "valid_interval": int(valid_interval),
        "save_interval": int(save_interval),
        "learning_rate": float(learning_rate),
        "weight_decay": float(weight_decay),
        "warmup_steps": int(warmup_steps),
        "max_steps": resolved_max_steps,
        "save_path": checkpoints_dir,
        "tensorboard": tensorboard_path if tensorboard_path else logs_dir,
        "lambdas": {
            "loss/diff": 1.0,
            "loss/stop": 1.0
        },
        "lora": {
            "enable_lm": bool(enable_lm),
            "enable_dit": bool(enable_dit),
            "enable_proj": bool(enable_proj),
            "r": int(lora_rank),
            "alpha": int(lora_alpha),
            "dropout": float(dropout),
            "target_modules_lm": ["q_proj", "v_proj", "k_proj", "o_proj"],
            "target_modules_dit": ["q_proj", "v_proj", "k_proj", "o_proj"]
        },
    }
    
    # Add distribution options if provided
    if hf_model_id and hf_model_id.strip():
        config["hf_model_id"] = hf_model_id.strip()
    if distribute:
        config["distribute"] = True

    config_path = os.path.join(save_dir, "train_config.yaml")
    with open(config_path, "w") as f:
        yaml.
... [TRUNCATED]
```

### File: docs\finetune.md
```md
# VoxCPM Fine-tuning Guide

This guide covers how to fine-tune VoxCPM models with two approaches: full fine-tuning and LoRA fine-tuning.

### 🎓 SFT (Supervised Fine-Tuning)

Full fine-tuning updates all model parameters. Suitable for:
- 📊 Large, specialized datasets
- 🔄 Cases where significant behavior changes are needed

### ⚡ LoRA Fine-tuning

LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that:
- 🎯 Trains only a small number of additional parameters
- 💾 Significantly reduces memory requirements and training time
- 🔀 Supports multiple LoRA adapters with hot-swapping



## Table of Contents

- [Quick Start: WebUI](#quick-start-webui)
- [Data Preparation](#data-preparation)
- [Full Fine-tuning](#full-fine-tuning)
- [LoRA Fine-tuning](#lora-fine-tuning)
- [Inference](#inference)
- [LoRA Hot-swapping](#lora-hot-swapping)
- [FAQ](#faq)

---

## Quick Start: WebUI

For users who prefer a graphical interface, we provide `lora_ft_webui.py` - a comprehensive WebUI for training and inference:

### Launch WebUI

```bash
python lora_ft_webui.py
```

Then open `http://localhost:7860` in your browser.

### Features

- **🚀 Training Tab**: Configure and start LoRA training with an intuitive interface
  - Set training parameters (learning rate, batch size, LoRA rank, etc.)
  - Monitor training progress in real-time
  - Resume training from existing checkpoints

- **🎵 Inference Tab**: Generate audio with trained models
  - Automatic base model loading from LoRA checkpoint config
  - Voice cloning with automatic ASR (reference text recognition)
  - Hot-swap between multiple LoRA models
  - Zero-shot TTS without reference audio

## Data Preparation

Training data should be prepared as a JSONL manifest file, with one sample per line:

```jsonl
{"audio": "path/to/audio1.wav", "text": "Transcript of audio 1."}
{"audio": "path/to/audio2.wav", "text": "Transcript of audio 2."}
{"audio": "path/to/audio3.wav", "text": "Optional duration field.", "duration": 3.5}
{"audio": "path/to/audio4.wav", "text": "Optional dataset_id for multi-dataset.", "dataset_id": 1}
```

### Required Fields

| Field | Description |
|-------|-------------|
| `audio` | Path to audio file (absolute or relative) |
| `text` | Corresponding transcript |

### Optional Fields

| Field | Description |
|-------|-------------|
| `duration` | Audio duration in seconds (speeds up sample filtering) |
| `dataset_id` | Dataset ID for multi-dataset training (default: 0) |

### Requirements

- Audio format: WAV
- Sample rate: 16kHz for VoxCPM-0.5B, 44.1kHz for VoxCPM1.5
- Text: Transcript matching the audio content

See `examples/train_data_example.jsonl` for a complete example.

---

## Full Fine-tuning

Full fine-tuning updates all model parameters. Suitable for large datasets or when significant behavior changes are needed.

### Configuration

Create `conf/voxcpm_v1.5/voxcpm_finetune_all.yaml`:

```yaml
pretrained_path: /path/to/VoxCPM1.5/
train_manifest: /path/to/train.jsonl
val_manifest: ""

sample_rate: 44100
batch_size: 16
grad_accum_steps: 1
num_workers: 2
num_iters: 2000
log_interval: 10
valid_interval: 1000
save_interval: 1000

learning_rate: 0.00001   # Use smaller LR for full fine-tuning
weight_decay: 0.01
warmup_steps: 100
max_steps: 2000
max_batch_tokens: 8192

save_path: /path/to/checkpoints/finetune_all
tensorboard: /path/to/logs/finetune_all

lambdas:
  loss/diff: 1.0
  loss/stop: 1.0
```

### Training

```bash
# Single GPU
python scripts/train_voxcpm_finetune.py --config_path conf/voxcpm_v1.5/voxcpm_finetune_all.yaml

# Multi-GPU
CUDA_VISIBLE_DEVICES=0,1,2,3 torchrun --nproc_per_node=4 \
    scripts/train_voxcpm_finetune.py --config_path conf/voxcpm_v1.5/voxcpm_finetune_all.yaml
```

### Checkpoint Structure

Full fine-tuning saves a complete model directory that can be loaded directly:

```
checkpoints/finetune_all/
└── step_0002000/
    ├── model.safetensors     # Model weights (excluding audio_vae)
    ├── config.json            # Model config
    ├── audiovae.pth           # Audio VAE weights
    ├── tokenizer.json         # Tokenizer
    ├── tokenizer_config.json
    ├── special_tokens_map.json
    ├── optimizer.pth
    └── scheduler.pth
```

---

## LoRA Fine-tuning

LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that trains only a small number of additional parameters, significantly reducing memory requirements.

### Configuration

Create `conf/voxcpm_v1.5/voxcpm_finetune_lora.yaml`:

```yaml
pretrained_path: /path/to/VoxCPM1.5/
train_manifest: /path/to/train.jsonl
val_manifest: ""

sample_rate: 44100
batch_size: 16
grad_accum_steps: 1
num_workers: 2
num_iters: 2000
log_interval: 10
valid_interval: 1000
save_interval: 1000

learning_rate: 0.0001    # LoRA can use larger LR
weight_decay: 0.01
warmup_steps: 100
max_steps: 2000
max_batch_tokens: 8192

save_path: /path/to/checkpoints/finetune_lora
tensorboard: /path/to/logs/finetune_lora

lambdas:
  loss/diff: 1.0
  loss/stop: 1.0

# LoRA configuration
lora:
  enable_lm: true        # Apply LoRA to Language Model
  enable_dit: true       # Apply LoRA to Diffusion Transformer
  enable_proj: false     # Apply LoRA to projection layers (optional)
  
  r: 32                  # LoRA rank (higher = more capacity)
  alpha: 16              # LoRA alpha, scaling = alpha / r
  dropout: 0.0
  
  # Target modules
  target_modules_lm: ["q_proj", "v_proj", "k_proj", "o_proj"]
  target_modules_dit: ["q_proj", "v_proj", "k_proj", "o_proj"]

# Distribution options (optional)
# hf_model_id: "openbmb/VoxCPM1.5"  # HuggingFace ID
# distribute: true                   # If true, save hf_model_id in lora_config.json
```

### LoRA Parameters

| Parameter | Description | Recommended |
|-----------|-------------|-------------|
| `enable_lm` | Apply LoRA to LM (language model) | `true` |
| `enable_dit` | Apply LoRA to DiT (diffusion model) | `true` (required for voice cloning) |
| `r` | LoRA rank (higher = more capacity) | 16-64 |
| `alpha` | Scaling factor, `scaling = alpha / r` | Usually `r/2` or `r` |
| `target_modules_*` | Layer names to add LoRA | attention layers |

### Distribution Options (Optional)

| Parameter | Description | Default |
|-----------|-------------|---------|
| `hf_model_id` | HuggingFace model ID (e.g., `openbmb/VoxCPM1.5`) | `""` |
| `distribute` | If `true`, save `hf_model_id` as `base_model` in checkpoint; otherwise save local `pretrained_path` | `false` |

> **Note**: If `distribute: true`, `hf_model_id` is required.

### Training

```bash
# Single GPU
python scripts/train_voxcpm_finetune.py --config_path conf/voxcpm_v1.5/voxcpm_finetune_lora.yaml

# Multi-GPU
CUDA_VISIBLE_DEVICES=0,1,2,3 torchrun --nproc_per_node=4 \
    scripts/train_voxcpm_finetune.py --config_path conf/voxcpm_v1.5/voxcpm_finetune_lora.yaml
```

### Checkpoint Structure

LoRA training saves LoRA parameters and configuration:

```
checkpoints/finetune_lora/
└── step_0002000/
    ├── lora_weights.safetensors    # Only lora_A, lora_B parameters
    ├── lora_config.json            # LoRA config + base model path
    ├── optimizer.pth
    └── scheduler.pth
```

The `lora_config.json` contains:
```json
{
  "base_model": "/path/to/VoxCPM1.5/",
  "lora_config": {
    "enable_lm": true,
    "enable_dit": true,
    "r": 32,
    "alpha": 16,
    ...
  }
}
```

The `base_model` field contains:
- Local path (default): when `distribute: false` or not set
- HuggingFace ID: when `distribute: true` (e.g., `"openbmb/VoxCPM1.5"`)

This allows loading LoRA checkpoints without the original training config file.

---

## Inference

### Full Fine-tuning Inference

The checkpoint directory is a complete model, load it directly:

```bash
python scripts/test_voxcpm_ft_infer.py \
    --ckpt_dir /path/to/checkpoints/finetune_all/step_0002000 \
    --text "Hello, this is the fine-tuned model." \
    --output output.wav
```

With voice cloning:

```bash
python scripts/test_voxcpm_ft_infer.py \
    --ckpt_dir /path/to/checkpoints/finetune_all/step_0002000 \
    --text "This is voice cloning result." \
    --prompt_audio /path/to/reference.wav \
    --prompt_text "Reference audio transcript" \
    --output cloned_output.wav
```

### LoRA Inference

LoRA inference only requires the checkpoint directory (base model path and LoRA config are read from `lora_config.json`):

```bash
python scripts/test_voxcpm_lora_infer.py \
    --lora_ckpt /path/to/checkpoints/finetune_lora/step_0002000 \
    --text "Hello, this is LoRA fine-tuned result." \
    --output lora_output.wav
```

With voice cloning:

```bash
python scripts/test_voxcpm_lora_infer.py \
    --lora_ckpt /path/to/checkpoints/finetune_lora/step_0002000 \
    --text "This is voice cloning with LoRA." \
    --prompt_audio /path/to/reference.wav \
    --prompt_text "Reference audio transcript" \
    --output cloned_output.wav
```

Override base model path (optional):

```bash
python scripts/test_voxcpm_lora_infer.py \
    --lora_ckpt /path/to/checkpoints/finetune_lora/step_0002000 \
    --base_model /path/to/another/VoxCPM1.5 \
    --text "Use different base model." \
    --output output.wav
```

---

## LoRA Hot-swapping

LoRA supports dynamic loading, unloading, and switching at inference time without reloading the entire model.

### API Reference

```python
from voxcpm.core import VoxCPM
from voxcpm.model.voxcpm import LoRAConfig

# 1. Load model with LoRA structure and weights
lora_cfg = LoRAConfig(
    enable_lm=True, 
    enable_dit=True, 
    r=32, 
    alpha=16,
    target_modules_lm=["q_proj", "v_proj", "k_proj", "o_proj"],
    target_modules_dit=["q_proj", "v_proj", "k_proj", "o_proj"],
)
model = VoxCPM.from_pretrained(
    hf_model_id="openbmb/VoxCPM1.5",  # or local path
    load_denoiser=False,              # Optional: disable denoiser for faster loading
    optimize=True,                    # Enable torch.compile acceleration
    lora_config=lora_cfg,
    lora_weights_path="/path/to/lora_checkpoint",
)

# 2. Generate audio
audio = model.generate(
    text="Hello, this is LoRA fine-tuned result.",
    prompt_wav_path="/path/to/reference.wav",  # Optional: for voice cloning
    prompt_text="Reference audio transcript",   # Optional: for voice cloning
)

# 3. Disable LoRA (use base model only)
model.set_lora_enabled(False)

# 4. Re-enable LoRA
model.set_lora_enabled(True)

# 5. Unload LoRA (reset weights to zero)
model.unload_lora()

# 6. Hot-swap to another LoRA
loaded, skipped = model.load_lora("/path/to/another_lora_checkpoint")
print(f"Loaded {len(loaded)} params, skipped {len(skipped)}")

# 7. Get current LoRA weights
lora_state = model.get_lora_state_dict()
```

### Simplified Usage (Load from lora_config.json)

If your checkpoint contains `lora_config.json` (saved by the training script), you can load everything automatically:

```python
import json
from voxcpm.core import VoxCPM
from voxcpm.model.voxcpm import LoRAConfig

# Load config from checkpoint
lora_ckpt_dir = "/path/to/checkpoints/finetune_lora/step_0002000"
with open(f"{lora_ckpt_dir}/lora_config.json") as f:
    lora_info = json.load(f)

base_model = lora_info["base_model"]
lora_cfg = LoRAConfig(**lora_info["lora_config"])

# Load model with LoRA
model = VoxCPM.from_pretrained(
    hf_model_id=base_model,
    lora_config=lora_cfg,
    lora_weights_path=lora_ckpt_dir,
)
```

Or use the test script directly:

```bash
python scripts/test_voxcpm_lora_infer.py \
    --lora_ckpt /path/to/checkpoints/finetune_lora/step_0002000 \
    --text "Hello world"
```

### Method Reference

| Method | Description | torch.compile Compatible |
|--------|-------------|--------------------------|
| `load_lora(path)` | Load LoRA weights from file | ✅ |
| `set_lora_enabled(bool)` | Enable/disable LoRA | ✅ |
| `unload_lora()` | Reset LoRA weights to initial values | ✅ |
| `get_lora_state_dict()` | Get current LoRA weights | ✅ |
| `lora_enabled` | Property: check if LoRA is configured | ✅ |

---

## FAQ

### 1. How Much Data is Needed for LoRA Fine-tuning to Converge to a Single Voice?

We have tested with 5 minutes and 10 minutes of data (all audio clips are 3-6s in length). In our experiments, both datasets converged to a single voice after 2000 training steps with default configurations. You can adjust the data amount and training configurations based on your available data and computational resources.

### 2. Out of Memory (OOM)

- Increase `grad_accum_steps` (gradient accumulation)
- Decrease `batch_size`
- Use LoRA fine-tuning instead of full fine-tuning
- Decrease `max_batch_tokens` to filter long samples

### 3. Poor LoRA Performance

- Increase `r` (LoRA rank)
- Adjust `alpha` (try `alpha = r/2` or `alpha = r`)
- Increase training steps
- Add more target modules

### 4. Training Not Converging

- Decrease `learning_rate`
- Increase `warmup_steps`
- Check data quality

### 5. LoRA Not Taking Effect at Inference

- Check that `lora_config.json` exists in the checkpoint directory
- Check `load_lora()` return value - `skipped_keys` should be empty
- Verify `set_lora_enabled(True)` is called

### 6. Checkpoint Loading Errors

- Full fine-tuning: checkpoint directory should contain `model.safetensors` (or `pytorch_model.bin`), `config.json`, `audiovae.pth`
- LoRA: checkpoint directory should contain:
  - `lora_weights.safetensors` (or `lora_weights.ckpt`) - LoRA weights
  - `lora_config.json` - LoRA config and base model path

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
