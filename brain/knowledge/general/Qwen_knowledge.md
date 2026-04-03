---
id: qwen-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:06.053248
---

# KNOWLEDGE EXTRACT: Qwen
> **Extracted on:** 2026-03-30 22:28:43
> **Source:** Qwen

---

## File: `.dockerignore`
```
__pycache__
*.so
build
.coverage_*
*.egg-info
*~
.vscode/
.idea/
.git/
.github/
.DS_Store

/private/
/README-docker.md
```

## File: `.gitignore`
```
__pycache__
*.so
build
.coverage_*
*.egg-info
*~
.vscode/
.idea/
.DS_Store

/private/
```

## File: `cli_demo.py`
```python
# Copyright (c) Alibaba Cloud.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

"""A simple command-line interactive chat demo."""

import argparse
import os
import platform
import shutil
from copy import deepcopy

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
from transformers.trainer_utils import set_seed

DEFAULT_CKPT_PATH = 'Qwen/Qwen-7B-Chat'

_WELCOME_MSG = '''\
Welcome to use Qwen-Chat model, type text to start chat, type :h to show command help.
(欢迎使用 Qwen-Chat 模型，输入内容即可进行对话，:h 显示命令帮助。)

Note: This demo is governed by the original license of Qwen.
We strongly advise users not to knowingly generate or allow others to knowingly generate harmful content, including hate speech, violence, pornography, deception, etc.
(注：本演示受Qwen的许可协议限制。我们强烈建议，用户不应传播及不应允许他人传播以下内容，包括但不限于仇恨言论、暴力、色情、欺诈相关的有害信息。)
'''
_HELP_MSG = '''\
Commands:
    :help / :h          Show this help message              显示帮助信息
    :exit / :quit / :q  Exit the demo                       退出Demo
    :clear / :cl        Clear screen                        清屏
    :clear-his / :clh   Clear history                       清除对话历史
    :history / :his     Show history                        显示对话历史
    :seed               Show current random seed            显示当前随机种子
    :seed <N>           Set random seed to <N>              设置随机种子
    :conf               Show current generation config      显示生成配置
    :conf <key>=<value> Change generation config            修改生成配置
    :reset-conf         Reset generation config             重置生成配置
'''


def _load_model_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True, resume_download=True,
    )

    if args.cpu_only:
        device_map = "cpu"
    else:
        device_map = "auto"

    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        device_map=device_map,
        trust_remote_code=True,
        resume_download=True,
    ).eval()

    config = GenerationConfig.from_pretrained(
        args.checkpoint_path, trust_remote_code=True, resume_download=True,
    )

    return model, tokenizer, config


def _gc():
    import gc
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def _clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def _print_history(history):
    terminal_width = shutil.get_terminal_size()[0]
    print(f'History ({len(history)})'.center(terminal_width, '='))
    for index, (query, response) in enumerate(history):
        print(f'User[{index}]: {query}')
        print(f'QWen[{index}]: {response}')
    print('=' * terminal_width)


def _get_input() -> str:
    while True:
        try:
            message = input('User> ').strip()
        except UnicodeDecodeError:
            print('[ERROR] Encoding error in input')
            continue
        except KeyboardInterrupt:
            exit(1)
        if message:
            return message
        print('[ERROR] Query is empty')


def main():
    parser = argparse.ArgumentParser(
        description='QWen-Chat command-line interactive chat demo.')
    parser.add_argument("-c", "--checkpoint-path", type=str, default=DEFAULT_CKPT_PATH,
                        help="Checkpoint name or path, default to %(default)r")
    parser.add_argument("-s", "--seed", type=int, default=1234, help="Random seed")
    parser.add_argument("--cpu-only", action="store_true", help="Run demo with CPU only")
    args = parser.parse_args()

    history, response = [], ''

    model, tokenizer, config = _load_model_tokenizer(args)
    orig_gen_config = deepcopy(model.generation_config)

    _clear_screen()
    print(_WELCOME_MSG)

    seed = args.seed

    while True:
        query = _get_input()

        # Process commands.
        if query.startswith(':'):
            command_words = query[1:].strip().split()
            if not command_words:
                command = ''
            else:
                command = command_words[0]

            if command in ['exit', 'quit', 'q']:
                break
            elif command in ['clear', 'cl']:
                _clear_screen()
                print(_WELCOME_MSG)
                _gc()
                continue
            elif command in ['clear-his', 'clh']:
                print(f'[INFO] All {len(history)} history cleared')
                history.clear()
                _gc()
                continue
            elif command in ['help', 'h']:
                print(_HELP_MSG)
                continue
            elif command in ['history', 'his']:
                _print_history(history)
                continue
            elif command in ['seed']:
                if len(command_words) == 1:
                    print(f'[INFO] Current random seed: {seed}')
                    continue
                else:
                    new_seed_s = command_words[1]
                    try:
                        new_seed = int(new_seed_s)
                    except ValueError:
                        print(f'[WARNING] Fail to change random seed: {new_seed_s!r} is not a valid number')
                    else:
                        print(f'[INFO] Random seed changed to {new_seed}')
                        seed = new_seed
                    continue
            elif command in ['conf']:
                if len(command_words) == 1:
                    print(model.generation_config)
                else:
                    for key_value_pairs_str in command_words[1:]:
                        eq_idx = key_value_pairs_str.find('=')
                        if eq_idx == -1:
                            print('[WARNING] format: <key>=<value>')
                            continue
                        conf_key, conf_value_str = key_value_pairs_str[:eq_idx], key_value_pairs_str[eq_idx + 1:]
                        try:
                            conf_value = eval(conf_value_str)
                        except Exception as e:
                            print(e)
                            continue
                        else:
                            print(f'[INFO] Change config: model.generation_config.{conf_key} = {conf_value}')
                            setattr(model.generation_config, conf_key, conf_value)
                continue
            elif command in ['reset-conf']:
                print('[INFO] Reset generation config')
                model.generation_config = deepcopy(orig_gen_config)
                print(model.generation_config)
                continue
            else:
                # As normal query.
                pass

        # Run chat.
        set_seed(seed)
        try:
            for response in model.chat_stream(tokenizer, query, history=history, generation_config=config):
                _clear_screen()
                print(f"\nUser: {query}")
                print(f"\nQwen-Chat: {response}")
        except KeyboardInterrupt:
            print('[WARNING] Generation interrupted')
            continue

        history.append((query, response))


if __name__ == "__main__":
    main()
```

## File: `FAQ.md`
```markdown
# FAQ

## Installation & Environment

#### Failure in installing flash attention

Flash attention is an option for accelerating training and inference. Only NVIDIA GPUs of Turing, Ampere, Ada, and Hopper architecture, e.g., H100, A100, RTX 3090, T4, RTX 2080, can support flash attention. **You can use our models without installing it.**

#### Which version of transformers should I use?

4.32.0 is preferred.

#### I downloaded the codes and checkpoints but I can't load the model locally. What should I do?

Please check if you have updated the code to the latest, and correctly downloaded all the sharded checkpoint files.

#### `qwen.tiktoken` is not found. What is it?

This is the merge file of the tokenizer. You have to download it. Note that if you just git clone the repo without [git-lfs](https://git-lfs.com), you cannot download this file.

#### transformers_stream_generator/tiktoken/accelerate not found

Run the command `pip install -r requirements.txt`. You can find the file at [https://github.com/QwenLM/Qwen-7B/blob/main/requirements.txt](https://github.com/QwenLM/Qwen/blob/main/requirements.txt).
<br><br>



## Demo & Inference

#### Is there any demo? CLI demo and Web UI demo?

Yes, see `web_demo.py` for web demo and `cli_demo.py` for CLI demo. See README for more information.


#### Can I use CPU only?

Yes, run `python  cli_demo.py --cpu-only` will load the model and inference on CPU only.

#### Can Qwen support streaming?

Yes. See the function `chat_stream` in `modeling_qwen.py`.

#### Gibberish in result when using chat_stream().

This is because tokens represent bytes and a single token may be a meaningless string. We have updated the default setting of our tokenizer to avoid such decoding results. Please update the code to the latest version.

#### It seems that the generation is not related to the instruction...

Please check if you are loading Qwen-Chat instead of Qwen. Qwen is the base model without alignment, which behaves differently from the SFT/Chat model.

#### Is quantization supported?

Yes, the quantization is supported by AutoGPTQ. 


#### Slow when processing long sequences

Updating the code to the latest version can help.

#### Unsatisfactory performance in processing long sequences

Please ensure that NTK is applied. `use_dynamc_ntk` and `use_logn_attn` in `config.json` should be set to `true` (`true` by default).
<br><br>



## Finetuning

#### Can Qwen support SFT or even RLHF?

Yes, we now support SFT, including full-parameter finetuning, LoRA, and Q-LoRA. Also you can check other projects like [FastChat](**[https://github.com/lm-sys/FastChat](https://github.com/lm-sys/FastChat)), [Firefly]([https://github.com/yangjianxin1/Firefly](https://github.com/yangjianxin1/Firefly)), [**LLaMA Efficient Tuning**]([https://github.com/hiyouga/LLaMA-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning)), etc.

However, temporarily we do not support RLHF. We will provide the code in the near future.
<br><br>



## Tokenizer

#### bos_id/eos_id/pad_id not found

In our training, we only use `<|endoftext|>` as the separator and padding token. You can set bos_id, eos_id, and pad_id to tokenizer.eod_id. Learn more about our tokenizer from our documents about the tokenizer.



## Docker

#### Download official docker image is very slow

When downloading our official docker image, you may have a slow download speed due to some network issues. You can refer to [Alibaba Cloud Container Image Service](https://help.aliyun.com/zh/acr/user-guide/accelerate-the-pulls-of-docker-official-images) to accelerate the download of official images.
```

## File: `FAQ_ja.md`
```markdown
# FAQ

## インストールと環境

#### Flash attention 導入の失敗例

Flash attention は、トレーニングと推論を加速するオプションです。H100、A100、RTX 3090、T4、RTX 2080 などの Turing、Ampere、Ada、および Hopper アーキテクチャの NVIDIA GPU だけが、flash attention をサポートできます。それをインストールせずに私たちのモデルを使用することができます。

#### transformers のバージョンは？

4.32.0 が望ましいです。

#### コードとチェックポイントをダウンロードしましたが、モデルをローカルにロードできません。どうすればよいでしょうか？

コードを最新のものに更新し、すべてのシャードされたチェックポイントファイルを正しくダウンロードしたかどうか確認してください。

#### `qwen.tiktoken` が見つかりません。これは何ですか？

これはトークナイザーのマージファイルです。ダウンロードする必要があります。[git-lfs](https://git-lfs.com) を使わずにリポジトリを git clone しただけでは、このファイルをダウンロードできないことに注意してください。

#### transformers_stream_generator/tiktoken/accelerate が見つかりません。

コマンド `pip install -r requirements.txt` を実行してください。このファイルは [https://github.com/QwenLM/Qwen/blob/main/requirements.txt](https://github.com/QwenLM/Qwen/blob/main/requirements.txt) にあります。
<br><br>



## デモと推論

#### デモはありますか？CLI と Web UI のデモはありますか？

はい、Web デモは `web_demo.py` を、CLI デモは `cli_demo.py` を参照してください。詳しくは README を参照してください。



#### CPU のみを使うことはできますか？

はい、`python cli_demo.py --cpu-only` を実行すると、CPU のみでモデルと推論をロードします。

#### Qwen はストリーミングに対応していますか？

`modeling_qwen.py` の `chat_stream` 関数を参照してください。

#### chat_stream() を使用すると、結果に文字化けが発生します。

これは、トークンがバイトを表し、単一のトークンが無意味な文字列である可能性があるためです。このようなデコード結果を避けるため、トークナイザのデフォルト設定を更新しました。コードを最新版に更新してください。

#### インストラクションとは関係ないようですが...

Qwen ではなく Qwen-Chat を読み込んでいないか確認してください。Qwen はアライメントなしのベースモデルで、SFT/Chat モデルとは挙動が異なります。

#### 量子化はサポートされていますか？

はい、量子化は AutoGPTQ でサポートされています。


#### 長いシーケンスの処理に時間がかかる

コードを最新版に更新することで解決します。

#### 長いシーケンスの処理で不満足なパフォーマンス

NTK が適用されていることを確認してください。`config.json` の `use_dynamc_ntk` と `use_logn_attn` を `true` に設定する必要があります（デフォルトでは `true`）。
<br><br>



## ファインチューニング

#### Qwen は SFT、あるいは RLHF に対応できますか？

SFTのコードは提供します。[FastChat](**[https://github.com/lm-sys/FastChat](https://github.com/lm-sys/FastChat))、[Firefly]([https://github.com/yangjianxin1/Firefly](https://github.com/yangjianxin1/Firefly))、[**LLaMA Efficient Tuning**]([https://github.com/hiyouga/LLaMA-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning))など、いくつかのプロジェクトではファインチューニングをサポートしています。近日中に関連コードを更新する予定です。
<br><br>



## トークナイザー

#### bos_id/eos_id/pad_id が見つかりません。

私たちのトレーニングでは、セパレータとパディングトークンとして `<|endoftext|>` のみを使用しています。bos_id、eos_id、pad_id は tokenizer.eod_id に設定できます。私たちのトークナイザーについて詳しくは、トークナイザーについてのドキュメントをご覧ください。

```

## File: `FAQ_zh.md`
```markdown
# FAQ

## 安装&环境

#### flash attention 安装失败

flash attention是一个用于加速模型训练推理的可选项，且仅适用于Turing、Ampere、Ada、Hopper架构的Nvidia GPU显卡（如H100、A100、RTX 3090、T4、RTX 2080），您可以在不安装flash attention的情况下正常使用模型进行推理。

#### 我应该用哪个transformers版本？

建议使用4.32.0。

#### 我把模型和代码下到本地，按照教程无法使用，该怎么办？

答：别着急，先检查你的代码是不是更新到最新版本，然后确认你是否完整地将模型checkpoint下到本地。

#### `qwen.tiktoken`这个文件找不到，怎么办？

这个是我们的tokenizer的merge文件，你必须下载它才能使用我们的tokenizer。注意，如果你使用git clone却没有使用git-lfs，这个文件不会被下载。如果你不了解git-lfs，可点击[官网](https://git-lfs.com/)了解。

#### transformers_stream_generator/tiktoken/accelerate，这几个库提示找不到，怎么办？

运行如下命令：`pip install -r requirements.txt`。相关依赖库在[https://github.com/QwenLM/Qwen-7B/blob/main/requirements.txt](https://github.com/QwenLM/Qwen/blob/main/requirements.txt) 可以找到。
<br><br>


## Demo & 推理

#### 是否提供Demo？CLI Demo及Web UI Demo？

`web_demo.py`和`cli_demo.py`分别提供了Web UI以及CLI的Demo。请查看README相关内容了解更多。

#### 我没有GPU，只用CPU运行CLI demo可以吗？

可以的，运行`python  cli_demo.py --cpu-only`命令即可将模型读取到CPU并使用CPU进行推理。

#### Qwen支持流式推理吗？

Qwen当前支持流式推理。见位于`modeling_qwen.py`的`chat_stream`函数。

#### 使用`chat_stream()`生成混乱的内容及乱码，为什么？

这是由于模型生成过程中输出的部分token需要与后续token一起解码才能输出正常文本，单个token解码结果是无意义字符串，我们已经更新了tokenizer解码时的默认设置，避免这些字符串在生成结果中出现，如果仍有类似问题请更新模型至最新版本。

#### 模型的输出看起来与输入无关/没有遵循指令/看起来呆呆的

请检查是否加载的是Qwen-Chat模型进行推理，Qwen模型是未经align的预训练基模型，不期望具备响应用户指令的能力。我们在模型最新版本已经对`chat`及`chat_stream`接口内进行了检查，避免您误将预训练模型作为SFT/Chat模型使用。

#### 是否有量化版本模型

目前Qwen支持基于AutoGPTQ的4-bit的量化推理。

#### 生成序列较长后速度显著变慢

请更新到最新代码。

#### 处理长序列时效果有问题

请确认是否开启ntk。若要启用这些技巧，请将`config.json`里的`use_dynamc_ntk`和`use_logn_attn`设置为`true`。最新代码默认为`true`。
<br><br>


## 微调

#### 当前是否支持SFT和RLHF？

我们目前提供了SFT的代码，支持全参数微调、LoRA和Q-LoRA。此外，当前有多个外部项目也已实现支持，如[FastChat](**[https://github.com/lm-sys/FastChat](https://github.com/lm-sys/FastChat))、[Firefly]([https://github.com/yangjianxin1/Firefly](https://github.com/yangjianxin1/Firefly))、[**LLaMA Efficient Tuning**]([https://github.com/hiyouga/LLaMA-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning))等。我们会尽快更新这部分代码和说明。

我们还没提供对RLHF训练的支持，敬请期待。
<br><br>


## Tokenizer

#### bos_id/eos_id/pad_id，这些token id不存在，为什么？

在训练过程中，我们仅使用<|endoftext|>这一token作为sample/document之间的分隔符及padding位置占位符，你可以将bos_id, eos_id, pad_id均指向tokenizer.eod_id。请阅读我们关于tokenizer的文档，了解如何设置这些id。


## Docker

#### 下载官方Docker镜像速度很慢

在下载官方镜像时，您可能由于某些网络原因导致下载速度变慢。可以参考[阿里云容器镜像服务](https://help.aliyun.com/zh/acr/user-guide/accelerate-the-pulls-of-docker-official-images)加速官方镜像的下载。
```

## File: `finetune.py`
```python
# This code is based on the revised code from fastchat based on tatsu-lab/stanford_alpaca.


from dataclasses import dataclass, field
import json
import math
import logging
import os
from typing import Dict, Optional, List
import torch
from torch.utils.data import Dataset
from deepspeed import zero
from deepspeed.runtime.zero.partition_parameters import ZeroParamStatus
import transformers
from transformers import Trainer, GPTQConfig, deepspeed
from transformers.trainer_pt_utils import LabelSmoother
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from accelerate.utils import DistributedType


IGNORE_TOKEN_ID = LabelSmoother.ignore_index


@dataclass
class ModelArguments:
    model_name_or_path: Optional[str] = field(default="Qwen/Qwen-7B")


@dataclass
class DataArguments:
    data_path: str = field(
        default=None, metadata={"help": "Path to the training data."}
    )
    eval_data_path: str = field(
        default=None, metadata={"help": "Path to the evaluation data."}
    )
    lazy_preprocess: bool = False


@dataclass
class TrainingArguments(transformers.TrainingArguments):
    cache_dir: Optional[str] = field(default=None)
    optim: str = field(default="adamw_torch")
    model_max_length: int = field(
        default=8192,
        metadata={
            "help": "Maximum sequence length. Sequences will be right padded (and possibly truncated)."
        },
    )
    use_lora: bool = False


@dataclass
class LoraArguments:
    lora_r: int = 64
    lora_alpha: int = 16
    lora_dropout: float = 0.05
    lora_target_modules: List[str] = field(
        default_factory=lambda: ["c_attn", "c_proj", "w1", "w2"]
    )
    lora_weight_path: str = ""
    lora_bias: str = "none"
    q_lora: bool = False


def maybe_zero_3(param):
    if hasattr(param, "ds_id"):
        assert param.ds_status == ZeroParamStatus.NOT_AVAILABLE
        with zero.GatheredParameters([param]):
            param = param.data.detach().cpu().clone()
    else:
        param = param.detach().cpu().clone()
    return param


# Borrowed from peft.utils.get_peft_model_state_dict
def get_peft_state_maybe_zero_3(named_params, bias):
    if bias == "none":
        to_return = {k: t for k, t in named_params if "lora_" in k}
    elif bias == "all":
        to_return = {k: t for k, t in named_params if "lora_" in k or "bias" in k}
    elif bias == "lora_only":
        to_return = {}
        maybe_lora_bias = {}
        lora_bias_names = set()
        for k, t in named_params:
            if "lora_" in k:
                to_return[k] = t
                bias_name = k.split("lora_")[0] + "bias"
                lora_bias_names.add(bias_name)
            elif "bias" in k:
                maybe_lora_bias[k] = t
        for k, t in maybe_lora_bias:
            if bias_name in lora_bias_names:
                to_return[bias_name] = t
    else:
        raise NotImplementedError
    to_return = {k: maybe_zero_3(v) for k, v in to_return.items()}
    return to_return


local_rank = None

def rank0_print(*args):
    if local_rank == 0:
        print(*args)


def safe_save_model_for_hf_trainer(trainer: transformers.Trainer, output_dir: str, bias="none"):
    """Collects the state dict and dump to disk."""
    # check if zero3 mode enabled
    if deepspeed.is_deepspeed_zero3_enabled():
        state_dict = trainer.model_wrapped._zero3_consolidated_16bit_state_dict()
    else:
        if trainer.args.use_lora:
            state_dict = get_peft_state_maybe_zero_3(
                trainer.model.named_parameters(), bias
            )
        else:
            state_dict = trainer.model.state_dict()
    if trainer.args.should_save and trainer.args.local_rank == 0:
        trainer._save(output_dir, state_dict=state_dict)


def preprocess(
    sources,
    tokenizer: transformers.PreTrainedTokenizer,
    max_len: int,
    system_message: str = "You are a helpful assistant."
) -> Dict:
    roles = {"user": "<|im_start|>user", "assistant": "<|im_start|>assistant"}

    im_start = tokenizer.im_start_id
    im_end = tokenizer.im_end_id
    nl_tokens = tokenizer('\n').input_ids
    _system = tokenizer('system').input_ids + nl_tokens
    _user = tokenizer('user').input_ids + nl_tokens
    _assistant = tokenizer('assistant').input_ids + nl_tokens

    # Apply prompt templates
    input_ids, targets = [], []
    for i, source in enumerate(sources):
        if roles[source[0]["from"]] != roles["user"]:
            source = source[1:]

        input_id, target = [], []
        system = [im_start] + _system + tokenizer(system_message).input_ids + [im_end] + nl_tokens
        input_id += system
        target += [im_start] + [IGNORE_TOKEN_ID] * (len(system)-3) + [im_end] + nl_tokens
        assert len(input_id) == len(target)
        for j, sentence in enumerate(source):
            role = roles[sentence["from"]]
            _input_id = tokenizer(role).input_ids + nl_tokens + \
                tokenizer(sentence["value"]).input_ids + [im_end] + nl_tokens
            input_id += _input_id
            if role == '<|im_start|>user':
                _target = [im_start] + [IGNORE_TOKEN_ID] * (len(_input_id)-3) + [im_end] + nl_tokens
            elif role == '<|im_start|>assistant':
                _target = [im_start] + [IGNORE_TOKEN_ID] * len(tokenizer(role).input_ids) + \
                    _input_id[len(tokenizer(role).input_ids)+1:-2] + [im_end] + nl_tokens
            else:
                raise NotImplementedError
            target += _target
        assert len(input_id) == len(target)
        input_id += [tokenizer.pad_token_id] * (max_len - len(input_id))
        target += [IGNORE_TOKEN_ID] * (max_len - len(target))
        input_ids.append(input_id[:max_len])
        targets.append(target[:max_len])
    input_ids = torch.tensor(input_ids, dtype=torch.int)
    targets = torch.tensor(targets, dtype=torch.int)

    return dict(
        input_ids=input_ids,
        labels=targets,
        attention_mask=input_ids.ne(tokenizer.pad_token_id),
    )


class SupervisedDataset(Dataset):
    """Dataset for supervised fine-tuning."""

    def __init__(self, raw_data, tokenizer: transformers.PreTrainedTokenizer, max_len: int):
        super(SupervisedDataset, self).__init__()

        rank0_print("Formatting inputs...")
        sources = [example["conversations"] for example in raw_data]
        data_dict = preprocess(sources, tokenizer, max_len)

        self.input_ids = data_dict["input_ids"]
        self.labels = data_dict["labels"]
        self.attention_mask = data_dict["attention_mask"]

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, i) -> Dict[str, torch.Tensor]:
        return dict(
            input_ids=self.input_ids[i],
            labels=self.labels[i],
            attention_mask=self.attention_mask[i],
        )


class LazySupervisedDataset(Dataset):
    """Dataset for supervised fine-tuning."""

    def __init__(self, raw_data, tokenizer: transformers.PreTrainedTokenizer, max_len: int):
        super(LazySupervisedDataset, self).__init__()
        self.tokenizer = tokenizer
        self.max_len = max_len

        rank0_print("Formatting inputs...Skip in lazy mode")
        self.tokenizer = tokenizer
        self.raw_data = raw_data
        self.cached_data_dict = {}

    def __len__(self):
        return len(self.raw_data)

    def __getitem__(self, i) -> Dict[str, torch.Tensor]:
        if i in self.cached_data_dict:
            return self.cached_data_dict[i]

        ret = preprocess([self.raw_data[i]["conversations"]], self.tokenizer, self.max_len)
        ret = dict(
            input_ids=ret["input_ids"][0],
            labels=ret["labels"][0],
            attention_mask=ret["attention_mask"][0],
        )
        self.cached_data_dict[i] = ret

        return ret


def make_supervised_data_module(
    tokenizer: transformers.PreTrainedTokenizer, data_args, max_len,
) -> Dict:
    """Make dataset and collator for supervised fine-tuning."""
    dataset_cls = (
        LazySupervisedDataset if data_args.lazy_preprocess else SupervisedDataset
    )
    rank0_print("Loading data...")

    train_json = json.load(open(data_args.data_path, "r"))
    train_dataset = dataset_cls(train_json, tokenizer=tokenizer, max_len=max_len)

    if data_args.eval_data_path:
        eval_json = json.load(open(data_args.eval_data_path, "r"))
        eval_dataset = dataset_cls(eval_json, tokenizer=tokenizer, max_len=max_len)
    else:
        eval_dataset = None

    return dict(train_dataset=train_dataset, eval_dataset=eval_dataset)


def train():
    global local_rank

    parser = transformers.HfArgumentParser(
        (ModelArguments, DataArguments, TrainingArguments, LoraArguments)
    )
    (
        model_args,
        data_args,
        training_args,
        lora_args,
    ) = parser.parse_args_into_dataclasses()

    # This serves for single-gpu qlora.
    if getattr(training_args, 'deepspeed', None) and int(os.environ.get("WORLD_SIZE", 1))==1:
        training_args.distributed_state.distributed_type = DistributedType.DEEPSPEED

    local_rank = training_args.local_rank

    device_map = None
    world_size = int(os.environ.get("WORLD_SIZE", 1))
    ddp = world_size != 1
    if lora_args.q_lora:
        device_map = {"": int(os.environ.get("LOCAL_RANK") or 0)} if ddp else "auto"
        if len(training_args.fsdp) > 0 or deepspeed.is_deepspeed_zero3_enabled():
            logging.warning(
                "FSDP or ZeRO3 are incompatible with QLoRA."
            )

    is_chat_model = 'chat' in model_args.model_name_or_path.lower()
    if (
            training_args.use_lora
            and not lora_args.q_lora
            and deepspeed.is_deepspeed_zero3_enabled()
            and not is_chat_model
    ):
        raise RuntimeError("ZeRO3 is incompatible with LoRA when finetuning on base model.")

    model_load_kwargs = {
        'low_cpu_mem_usage': not deepspeed.is_deepspeed_zero3_enabled(),
    }

    # Set RoPE scaling factor
    config = transformers.AutoConfig.from_pretrained(
        model_args.model_name_or_path,
        cache_dir=training_args.cache_dir,
        trust_remote_code=True,
    )
    config.use_cache = False

    # Load model and tokenizer
    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_args.model_name_or_path,
        config=config,
        cache_dir=training_args.cache_dir,
        device_map=device_map,
        trust_remote_code=True,
        quantization_config=GPTQConfig(
            bits=4, disable_exllama=True
        )
        if training_args.use_lora and lora_args.q_lora
        else None,
        **model_load_kwargs,
    )
    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_args.model_name_or_path,
        cache_dir=training_args.cache_dir,
        model_max_length=training_args.model_max_length,
        padding_side="right",
        use_fast=False,
        trust_remote_code=True,
    )
    tokenizer.pad_token_id = tokenizer.eod_id

    if training_args.use_lora:
        if lora_args.q_lora or is_chat_model:
            modules_to_save = None
        else:
            modules_to_save = ["wte", "lm_head"]
        lora_config = LoraConfig(
            r=lora_args.lora_r,
            lora_alpha=lora_args.lora_alpha,
            target_modules=lora_args.lora_target_modules,
            lora_dropout=lora_args.lora_dropout,
            bias=lora_args.lora_bias,
            task_type="CAUSAL_LM",
            modules_to_save=modules_to_save  # This argument serves for adding new tokens.
        )
        if lora_args.q_lora:
            model = prepare_model_for_kbit_training(
                model, use_gradient_checkpointing=training_args.gradient_checkpointing
            )

        model = get_peft_model(model, lora_config)

        # Print peft trainable params
        model.print_trainable_parameters()

        if training_args.gradient_checkpointing:
            model.enable_input_require_grads()

    # Load data
    data_module = make_supervised_data_module(
        tokenizer=tokenizer, data_args=data_args, max_len=training_args.model_max_length
    )

    # Start trainner
    trainer = Trainer(
        model=model, tokenizer=tokenizer, args=training_args, **data_module
    )

    trainer.train()
    trainer.save_state()

    safe_save_model_for_hf_trainer(trainer=trainer, output_dir=training_args.output_dir, bias=lora_args.lora_bias)


if __name__ == "__main__":
    train()
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

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

   Copyright 2023 Alibaba Cloud

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `NOTICE`
```
------------- LICENSE FOR NVIDIA Megatron-LM code  --------------

Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
  * Neither the name of NVIDIA CORPORATION nor the names of its
    contributors may be used to endorse or promote products derived
    from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


------------- LICENSE FOR OpenAI tiktoken code  --------------

MIT License

Copyright (c) 2022 OpenAI, Shantanu Jain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

------------- LICENSE FOR stanford_alpaca code  --------------

                                Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

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

   Copyright 2023 Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
------------- LICENSE FOR PanQiWei AutoGPTQ code  --------------

MIT License

Copyright (c) 2023 潘其威(William)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `openai_api.py`
```python
# Requirement:
#   pip install "openai<1.0"
# Usage:
#   python openai_api.py
# Visit http://localhost:8000/docs for documents.

import base64
import copy
import json
import time
from argparse import ArgumentParser
from contextlib import asynccontextmanager
from pprint import pprint
from typing import Dict, List, Literal, Optional, Union

import torch
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sse_starlette.sse import EventSourceResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig


class BasicAuthMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, username: str, password: str):
        super().__init__(app)
        self.required_credentials = base64.b64encode(
            f'{username}:{password}'.encode()).decode()

    async def dispatch(self, request: Request, call_next):
        authorization: str = request.headers.get('Authorization')
        if authorization:
            try:
                schema, credentials = authorization.split()
                if credentials == self.required_credentials:
                    return await call_next(request)
            except ValueError:
                pass

        headers = {'WWW-Authenticate': 'Basic'}
        return Response(status_code=401, headers=headers)


def _gc(forced: bool = False):
    global args
    if args.disable_gc and not forced:
        return

    import gc

    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


@asynccontextmanager
async def lifespan(app: FastAPI):  # collects GPU memory
    yield
    _gc(forced=True)


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class ModelCard(BaseModel):
    id: str
    object: str = 'model'
    created: int = Field(default_factory=lambda: int(time.time()))
    owned_by: str = 'owner'
    root: Optional[str] = None
    parent: Optional[str] = None
    permission: Optional[list] = None


class ModelList(BaseModel):
    object: str = 'list'
    data: List[ModelCard] = []


class ChatMessage(BaseModel):
    role: Literal['user', 'assistant', 'system', 'function']
    content: Optional[str]
    function_call: Optional[Dict] = None


class DeltaMessage(BaseModel):
    role: Optional[Literal['user', 'assistant', 'system']] = None
    content: Optional[str] = None


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    functions: Optional[List[Dict]] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None
    max_length: Optional[int] = None
    stream: Optional[bool] = False
    stop: Optional[List[str]] = None


class ChatCompletionResponseChoice(BaseModel):
    index: int
    message: Union[ChatMessage]
    finish_reason: Literal['stop', 'length', 'function_call']


class ChatCompletionResponseStreamChoice(BaseModel):
    index: int
    delta: DeltaMessage
    finish_reason: Optional[Literal['stop', 'length']]


class ChatCompletionResponse(BaseModel):
    model: str
    object: Literal['chat.completion', 'chat.completion.chunk']
    choices: List[Union[ChatCompletionResponseChoice,
                        ChatCompletionResponseStreamChoice]]
    created: Optional[int] = Field(default_factory=lambda: int(time.time()))


@app.get('/v1/models', response_model=ModelList)
async def list_models():
    global model_args
    model_card = ModelCard(id='gpt-3.5-turbo')
    return ModelList(data=[model_card])


# To work around that unpleasant leading-\n tokenization issue!
def add_extra_stop_words(stop_words):
    if stop_words:
        _stop_words = []
        _stop_words.extend(stop_words)
        for x in stop_words:
            s = x.lstrip('\n')
            if s and (s not in _stop_words):
                _stop_words.append(s)
        return _stop_words
    return stop_words


def trim_stop_words(response, stop_words):
    if stop_words:
        for stop in stop_words:
            idx = response.find(stop)
            if idx != -1:
                response = response[:idx]
    return response


TOOL_DESC = (
    '{name_for_model}: Call this tool to interact with the {name_for_human} API.'
    ' What is the {name_for_human} API useful for? {description_for_model} Parameters: {parameters}'
)

REACT_INSTRUCTION = """Answer the following questions as best you can. You have access to the following APIs:

{tools_text}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tools_name_text}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!"""

_TEXT_COMPLETION_CMD = object()


def parse_messages(messages, functions):
    if all(m.role != 'user' for m in messages):
        raise HTTPException(
            status_code=400,
            detail='Invalid request: Expecting at least one user message.',
        )

    messages = copy.deepcopy(messages)
    if messages[0].role == 'system':
        system = messages.pop(0).content.lstrip('\n').rstrip()
    else:
        system = 'You are a helpful assistant.'

    if functions:
        tools_text = []
        tools_name_text = []
        for func_info in functions:
            name = func_info.get('name', '')
            name_m = func_info.get('name_for_model', name)
            name_h = func_info.get('name_for_human', name)
            desc = func_info.get('description', '')
            desc_m = func_info.get('description_for_model', desc)
            tool = TOOL_DESC.format(
                name_for_model=name_m,
                name_for_human=name_h,
                # Hint: You can add the following format requirements in description:
                #   "Format the arguments as a JSON object."
                #   "Enclose the code within triple backticks (`) at the beginning and end of the code."
                description_for_model=desc_m,
                parameters=json.dumps(func_info['parameters'],
                                      ensure_ascii=False),
            )
            tools_text.append(tool)
            tools_name_text.append(name_m)
        tools_text = '\n\n'.join(tools_text)
        tools_name_text = ', '.join(tools_name_text)
        instruction = (REACT_INSTRUCTION.format(
            tools_text=tools_text,
            tools_name_text=tools_name_text,
        ).lstrip('\n').rstrip())
    else:
        instruction = ''

    messages_with_fncall = messages
    messages = []
    for m_idx, m in enumerate(messages_with_fncall):
        role, content, func_call = m.role, m.content, m.function_call
        content = content or ''
        content = content.lstrip('\n').rstrip()
        if role == 'function':
            if (len(messages) == 0) or (messages[-1].role != 'assistant'):
                raise HTTPException(
                    status_code=400,
                    detail=
                    'Invalid request: Expecting role assistant before role function.',
                )
            messages[-1].content += f'\nObservation: {content}'
            if m_idx == len(messages_with_fncall) - 1:
                # add a prefix for text completion
                messages[-1].content += '\nThought:'
        elif role == 'assistant':
            if len(messages) == 0:
                raise HTTPException(
                    status_code=400,
                    detail=
                    'Invalid request: Expecting role user before role assistant.',
                )
            if func_call is None:
                if functions:
                    content = f'Thought: I now know the final answer.\nFinal Answer: {content}'
            else:
                f_name, f_args = func_call['name'], func_call['arguments']
                if not content.startswith('Thought:'):
                    content = f'Thought: {content}'
                content = f'{content}\nAction: {f_name}\nAction Input: {f_args}'
            if messages[-1].role == 'user':
                messages.append(
                    ChatMessage(role='assistant',
                                content=content.lstrip('\n').rstrip()))
            else:
                messages[-1].content += '\n' + content
        elif role == 'user':
            messages.append(
                ChatMessage(role='user',
                            content=content.lstrip('\n').rstrip()))
        else:
            raise HTTPException(
                status_code=400,
                detail=f'Invalid request: Incorrect role {role}.')

    query = _TEXT_COMPLETION_CMD
    if messages[-1].role == 'user':
        query = messages[-1].content
        messages = messages[:-1]

    if len(messages) % 2 != 0:
        raise HTTPException(status_code=400, detail='Invalid request')

    history = []  # [(Q1, A1), (Q2, A2), ..., (Q_last_turn, A_last_turn)]
    for i in range(0, len(messages), 2):
        if messages[i].role == 'user' and messages[i + 1].role == 'assistant':
            usr_msg = messages[i].content.lstrip('\n').rstrip()
            bot_msg = messages[i + 1].content.lstrip('\n').rstrip()
            if instruction and (i == len(messages) - 2):
                usr_msg = f'{instruction}\n\nQuestion: {usr_msg}'
                instruction = ''
            history.append([usr_msg, bot_msg])
        else:
            raise HTTPException(
                status_code=400,
                detail=
                'Invalid request: Expecting exactly one user (or function) role before every assistant role.',
            )
    if instruction:
        assert query is not _TEXT_COMPLETION_CMD
        query = f'{instruction}\n\nQuestion: {query}'
    return query, history, system


def parse_response(response):
    func_name, func_args = '', ''
    i = response.find('\nAction:')
    j = response.find('\nAction Input:')
    k = response.find('\nObservation:')
    if 0 <= i < j:  # If the text has `Action` and `Action input`,
        if k < j:  # but does not contain `Observation`,
            # then it is likely that `Observation` is omitted by the LLM,
            # because the output text may have discarded the stop word.
            response = response.rstrip() + '\nObservation:'  # Add it back.
        k = response.find('\nObservation:')
        func_name = response[i + len('\nAction:'):j].strip()
        func_args = response[j + len('\nAction Input:'):k].strip()

    if func_name:
        response = response[:i]
        t = response.find('Thought: ')
        if t >= 0:
            response = response[t + len('Thought: '):]
        response = response.strip()
        choice_data = ChatCompletionResponseChoice(
            index=0,
            message=ChatMessage(
                role='assistant',
                content=response,
                function_call={
                    'name': func_name,
                    'arguments': func_args
                },
            ),
            finish_reason='function_call',
        )
        return choice_data

    z = response.rfind('\nFinal Answer: ')
    if z >= 0:
        response = response[z + len('\nFinal Answer: '):]
    choice_data = ChatCompletionResponseChoice(
        index=0,
        message=ChatMessage(role='assistant', content=response),
        finish_reason='stop',
    )
    return choice_data


# completion mode, not chat mode
def text_complete_last_message(history, stop_words_ids, gen_kwargs, system):
    im_start = '<|im_start|>'
    im_end = '<|im_end|>'
    prompt = f'{im_start}system\n{system}{im_end}'
    for i, (query, response) in enumerate(history):
        query = query.lstrip('\n').rstrip()
        response = response.lstrip('\n').rstrip()
        prompt += f'\n{im_start}user\n{query}{im_end}'
        prompt += f'\n{im_start}assistant\n{response}{im_end}'
    prompt = prompt[:-len(im_end)]

    _stop_words_ids = [tokenizer.encode(im_end)]
    if stop_words_ids:
        for s in stop_words_ids:
            _stop_words_ids.append(s)
    stop_words_ids = _stop_words_ids

    input_ids = torch.tensor([tokenizer.encode(prompt)]).to(model.device)
    output = model.generate(input_ids,
                            stop_words_ids=stop_words_ids,
                            **gen_kwargs).tolist()[0]
    output = tokenizer.decode(output, errors='ignore')
    assert output.startswith(prompt)
    output = output[len(prompt):]
    output = trim_stop_words(output, ['<|endoftext|>', im_end])
    print(f'<completion>\n{prompt}\n<!-- *** -->\n{output}\n</completion>')
    return output


@app.post('/v1/chat/completions', response_model=ChatCompletionResponse)
async def create_chat_completion(request: ChatCompletionRequest):
    global model, tokenizer

    gen_kwargs = {}
    if request.top_k is not None:
        gen_kwargs['top_k'] = request.top_k
    if request.temperature is not None:
        if request.temperature < 0.01:
            gen_kwargs['top_k'] = 1  # greedy decoding
        else:
            # Not recommended. Please tune top_p instead.
            gen_kwargs['temperature'] = request.temperature
    if request.top_p is not None:
        gen_kwargs['top_p'] = request.top_p

    stop_words = add_extra_stop_words(request.stop)
    if request.functions:
        stop_words = stop_words or []
        if 'Observation:' not in stop_words:
            stop_words.append('Observation:')

    query, history, system = parse_messages(request.messages,
                                            request.functions)

    if request.stream:
        if request.functions:
            raise HTTPException(
                status_code=400,
                detail=
                'Invalid request: Function calling is not yet implemented for stream mode.',
            )
        generate = predict(query,
                           history,
                           request.model,
                           stop_words,
                           gen_kwargs,
                           system=system)
        return EventSourceResponse(generate, media_type='text/event-stream')

    stop_words_ids = [tokenizer.encode(s)
                      for s in stop_words] if stop_words else None
    if query is _TEXT_COMPLETION_CMD:
        response = text_complete_last_message(history,
                                              stop_words_ids=stop_words_ids,
                                              gen_kwargs=gen_kwargs,
                                              system=system)
    else:
        response, _ = model.chat(
            tokenizer,
            query,
            history=history,
            system=system,
            stop_words_ids=stop_words_ids,
            **gen_kwargs,
        )
        print('<chat>')
        pprint(history, indent=2)
        print(f'{query}\n<!-- *** -->\n{response}\n</chat>')
    _gc()

    response = trim_stop_words(response, stop_words)
    if request.functions:
        choice_data = parse_response(response)
    else:
        choice_data = ChatCompletionResponseChoice(
            index=0,
            message=ChatMessage(role='assistant', content=response),
            finish_reason='stop',
        )
    return ChatCompletionResponse(model=request.model,
                                  choices=[choice_data],
                                  object='chat.completion')


def _dump_json(data: BaseModel, *args, **kwargs) -> str:
    try:
        return data.model_dump_json(*args, **kwargs)
    except AttributeError:  # pydantic<2.0.0
        return data.json(*args, **kwargs)  # noqa


async def predict(
    query: str,
    history: List[List[str]],
    model_id: str,
    stop_words: List[str],
    gen_kwargs: Dict,
    system: str,
):
    global model, tokenizer
    choice_data = ChatCompletionResponseStreamChoice(
        index=0, delta=DeltaMessage(role='assistant'), finish_reason=None)
    chunk = ChatCompletionResponse(model=model_id,
                                   choices=[choice_data],
                                   object='chat.completion.chunk')
    yield '{}'.format(_dump_json(chunk, exclude_unset=True))

    current_length = 0
    stop_words_ids = [tokenizer.encode(s)
                      for s in stop_words] if stop_words else None

    delay_token_num = max([len(x) for x in stop_words]) if stop_words_ids else 0
    response_generator = model.chat_stream(tokenizer,
                                           query,
                                           history=history,
                                           stop_words_ids=stop_words_ids,
                                           system=system,
                                           **gen_kwargs)
    for _new_response in response_generator:
        if len(_new_response) <= delay_token_num:
            continue
        new_response = _new_response[:-delay_token_num] if delay_token_num else _new_response

        if len(new_response) == current_length:
            continue

        new_text = new_response[current_length:]
        current_length = len(new_response)

        choice_data = ChatCompletionResponseStreamChoice(
            index=0, delta=DeltaMessage(content=new_text), finish_reason=None)
        chunk = ChatCompletionResponse(model=model_id,
                                       choices=[choice_data],
                                       object='chat.completion.chunk')
        yield '{}'.format(_dump_json(chunk, exclude_unset=True))
    
    if current_length != len(_new_response):
        # Determine whether to print the delay tokens
        delayed_text = _new_response[current_length:]
        new_text = trim_stop_words(delayed_text, stop_words)
        if len(new_text) > 0:
            choice_data = ChatCompletionResponseStreamChoice(
                index=0, delta=DeltaMessage(content=new_text), finish_reason=None)
            chunk = ChatCompletionResponse(model=model_id,
                                        choices=[choice_data],
                                        object='chat.completion.chunk')
            yield '{}'.format(_dump_json(chunk, exclude_unset=True))

    choice_data = ChatCompletionResponseStreamChoice(index=0,
                                                     delta=DeltaMessage(),
                                                     finish_reason='stop')
    chunk = ChatCompletionResponse(model=model_id,
                                   choices=[choice_data],
                                   object='chat.completion.chunk')
    yield '{}'.format(_dump_json(chunk, exclude_unset=True))
    yield '[DONE]'

    _gc()


def _get_args():
    parser = ArgumentParser()
    parser.add_argument(
        '-c',
        '--checkpoint-path',
        type=str,
        default='Qwen/Qwen-7B-Chat',
        help='Checkpoint name or path, default to %(default)r',
    )
    parser.add_argument('--api-auth', help='API authentication credentials')
    parser.add_argument('--cpu-only',
                        action='store_true',
                        help='Run demo with CPU only')
    parser.add_argument('--server-port',
                        type=int,
                        default=8000,
                        help='Demo server port.')
    parser.add_argument(
        '--server-name',
        type=str,
        default='127.0.0.1',
        help=
        'Demo server name. Default: 127.0.0.1, which is only visible from the local computer.'
        ' If you want other computers to access your server, use 0.0.0.0 instead.',
    )
    parser.add_argument(
        '--disable-gc',
        action='store_true',
        help='Disable GC after each response generated.',
    )

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = _get_args()

    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path,
        trust_remote_code=True,
        resume_download=True,
    )

    if args.api_auth:
        app.add_middleware(BasicAuthMiddleware,
                           username=args.api_auth.split(':')[0],
                           password=args.api_auth.split(':')[1])

    if args.cpu_only:
        device_map = 'cpu'
    else:
        device_map = 'auto'

    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        device_map=device_map,
        trust_remote_code=True,
        resume_download=True,
    ).eval()

    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path,
        trust_remote_code=True,
        resume_download=True,
    )

    uvicorn.run(app, host=args.server_name, port=args.server_port, workers=1)
```

## File: `README.md`
```markdown
<p align="left">
    <a href="README_CN.md">中文</a>&nbsp ｜ &nbspEnglish&nbsp ｜ &nbsp<a href="README_JA.md">日本語</a> ｜ &nbsp<a href="README_FR.md">Français</a> ｜ &nbsp<a href="README_ES.md">Español</a>
</p>
<br><br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/logo_qwen.jpg" width="400"/>
<p>
<br>

<p align="center">
        🤗 <a href="https://huggingface.co/Qwen">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/qwen">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2309.16609">Paper</a> &nbsp&nbsp ｜ &nbsp&nbsp🖥️ <a href="https://modelscope.cn/studios/qwen/Qwen-72B-Chat-Demo/summary">Demo</a>
<br>
<a href="assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp<a href="https://discord.gg/CV4E9rpNSD">Discord</a>&nbsp&nbsp ｜  &nbsp&nbsp<a href="https://dashscope.aliyun.com">API</a> 
</p>
<br><br>

> [!Important]
> Qwen2 is here! You are welcome to follow [QwenLM/Qwen2](https://github.com/QwenLM/Qwen2) and share your experience there.
>
> This repo ([QwenLM/Qwen](https://github.com/QwenLM/Qwen)) is no longer actively maintained, due to substantial codebase differences.

<br>

|     |                                                              Qwen-Chat                                                               |                                                                Qwen-Chat (Int4)                                                                |                        Qwen-Chat (Int8)                         |                                                            Qwen                                                            |
|-----|:------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 1.8B  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B">🤗</a>  |
| 7B  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B">🤗</a>  |
| 14B | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B">🤗</a> |
| 72B | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B">🤗</a> |



We opensource our **Qwen** series, now including **Qwen**, the base language models, namely **Qwen-1.8B**, **Qwen-7B**, **Qwen-14B**, and **Qwen-72B**, as well as **Qwen-Chat**, the chat models, namely **Qwen-1.8B-Chat**, **Qwen-7B-Chat**, **Qwen-14B-Chat**, and **Qwen-72B-Chat**. Links are on the above table. Click them and check the model cards. Also, we release the **[technical report](https://arxiv.org/abs/2309.16609)**. Please click the paper link and check it out!

In brief, we have strong base language models, which have been stably pretrained for up to 3 trillion tokens of multilingual data with a wide coverage of domains, languages (with a focus on Chinese and English), etc. They are able to achieve competitive performance on benchmark datasets. Additionally, we have chat models that are aligned with human preference based on SFT and RLHF (not released yet), which are able to chat, create content, extract information, summarize, translate, code, solve math problems, and so on, and are able to use tools, play as agents, or even play as code interpreters, etc.

| Model     | Release Date | Max Length | System Prompt Enhancement | # of Pretrained Tokens | Minimum GPU Memory Usage of Finetuning (Q-Lora) | Minimum GPU Usage of Generating 2048 Tokens (Int4) | Tool Usage |
|:----------|:------------:|:----------:|:-------------------------:|:----------------------:|:-----------------------------------------------:|:--------------------------------------------------:|:----------:|
| Qwen-1.8B |   23.11.30   |    32K     |             ✅             |          2.2T          |                      5.8GB                      |                       2.9GB                        |     ✅      |  
| Qwen-7B   |   23.08.03   |    32K     |             ❎             |          2.4T          |                     11.5GB                      |                       8.2GB                        |     ✅      |   
| Qwen-14B  |   23.09.25   |     8K     |             ❎             |          3.0T          |                     18.7GB                      |                       13.0GB                       |     ✅      |
| Qwen-72B  |   23.11.30   |    32K     |             ✅             |          3.0T          |                     61.4GB                      |                       48.9GB                       |     ✅      |   

In this repo, you can figure out:

* Quickstart with Qwen, and enjoy the simple inference.
* Details about the quantization models, including GPTQ and KV cache quantization.
* Statistics of inference performance, including speed and memory.
* Tutorials on finetuning, including full-parameter tuning, LoRA, and Q-LoRA.
* Instructions on deployment, with the example of vLLM and FastChat.
* Instructions on building demos, including WebUI, CLI demo, etc.
* Introduction to DashScope API service, as well as the instructions on building an OpenAI-style API for your model.
* Information about Qwen for tool use, agent, and code interpreter
* Statistics of long-context understanding evaluation
* License agreement
* ...

Also, if you meet problems, turn to [FAQ](FAQ.md) for help first. Still feeling struggled? Feel free to shoot us issues (better in English so that more people can understand you)! If you would like to help us, send us pull requests with no hesitation! We are always excited about PR! 

Would like to chat with us or date us coffee time? Welcome to our Discord or WeChat! 
<br><br>

## News and Updates
* 2023.11.30 🔥 We release **Qwen-72B** and **Qwen-72B-Chat**, which are trained on 3T tokens and support 32k context, along with **Qwen-1.8B**, and **Qwen-1.8B-Chat**, on ModelScope and Hugging Face. We have also strengthened the System Prompt capabilities of the Qwen-72B-Chat and Qwen-1.8B-Chat, see [example documentation](examples/system_prompt.md). Additionally, support the inference on **Ascend 910** and **Hygon DCU**. Check `ascend-support` and `dcu-support` for more details.
* 2023.10.17 We release the Int8 quantized model **Qwen-7B-Chat-Int8** and **Qwen-14B-Chat-Int8**. 
* 2023.9.25 🔥 We release **Qwen-14B** and **Qwen-14B-Chat** on ModelScope and Hugging Face, along with [qwen.cpp](https://github.com/QwenLM/qwen.cpp) and [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent). Codes and checkpoints of **Qwen-7B** and **Qwen-7B-Chat** are also updated. **PLEASE PULL THE LATEST VERSION!**
    - Compared to **Qwen-7B** (original), **Qwen-7B** uses more training tokens, increasing from 2.2T tokens to 2.4T tokens, while the context length extends from 2048 to 8192. The Chinese knowledge and coding ability of **Qwen-7B** have been further improved.
* 2023.9.12 We now support finetuning on the Qwen-7B models, including full-parameter finetuning, LoRA and Q-LoRA.
* 2023.8.21 We release the Int4 quantized model for Qwen-7B-Chat, **Qwen-7B-Chat-Int4**, which requires low memory costs but achieves improved inference speed. Besides, there is no significant performance degradation on the benchmark evaluation.
* 2023.8.3 We release both **Qwen-7B** and **Qwen-7B-Chat** on ModelScope and Hugging Face. We also provide a technical memo for more details about the model, including training details and model performance.
<br>

## Performance
Qwen models outperform the baseline models of similar model sizes on a series of benchmark datasets, e.g., MMLU, C-Eval, GSM8K, MATH, HumanEval, MBPP, BBH, etc., which evaluate the models’ capabilities on natural language understanding, mathematic problem solving, coding, etc. Qwen-72B achieves better performance than LLaMA2-70B on all tasks and outperforms GPT-3.5 on 7 out of 10 tasks. 

<p align="left">
    <img src="assets/radar_72b.jpg" width=600px/>
<p>
      

<br>

| Model             |   MMLU   |  C-Eval  |  GSM8K   |   MATH   | HumanEval |   MBPP   |   BBH    |  CMMLU   |
|:------------------|:--------:|:--------:|:--------:|:--------:|:---------:|:--------:|:--------:|:--------:|
|                   |  5-shot  |  5-shot  |  8-shot  |  4-shot  |  0-shot   |  3-shot  |  3-shot  |  5-shot  |
| LLaMA2-7B         |   46.8   |   32.5   |   16.7   |   3.3    |   12.8    |   20.8   |   38.2   |   31.8   |
| LLaMA2-13B        |   55.0   |   41.4   |   29.6   |   5.0    |   18.9    |   30.3   |   45.6   |   38.4   |
| LLaMA2-34B        |   62.6   |    -     |   42.2   |   6.2    |   22.6    |   33.0   |   44.1   |    -     |
| ChatGLM2-6B       |   47.9   |   51.7   |   32.4   |   6.5    |     -     |    -     |   33.7   |    -     |
| InternLM-7B       |   51.0   |   53.4   |   31.2   |   6.3    |   10.4    |   14.0   |   37.0   |   51.8   |
| InternLM-20B      |   62.1   |   58.8   |   52.6   |   7.9    |   25.6    |   35.6   |   52.5   |   59.0   |
| Baichuan2-7B      |   54.7   |   56.3   |   24.6   |   5.6    |   18.3    |   24.2   |   41.6   |   57.1   |
| Baichuan2-13B     |   59.5   |   59.0   |   52.8   |   10.1   |   17.1    |   30.2   |   49.0   |   62.0   |
| Yi-34B      	  	  |   76.3   |   81.8   |   67.9   |   15.9   |   26.2    |   38.2   |   66.4   |   82.6   |
| XVERSE-65B      	 |   70.8   |   68.6   |   60.3   |    -     |   26.3    |    -     |    -     |    -     |
| **Qwen-1.8B**     |   45.3   |   56.1   |   32.3   |   2.3    |   15.2    |   14.2   |   22.3   |   52.1   |
| **Qwen-7B**       |   58.2   |   63.5   |   51.7   |   11.6   |   29.9    |   31.6   |   45.0   |   62.2   |
| **Qwen-14B**      |   66.3   |   72.1   |   61.3   |   24.8   |   32.3    |   40.8   |   53.4   |   71.0   |
| **Qwen-72B**      | **77.4** | **83.3** | **78.9** | **35.2** | **35.4**  | **52.2** | **67.7** | **83.6** |

For all compared models, we report the best scores between their official reported results and [OpenCompass](https://opencompass.org.cn/leaderboard-llm). 

For more experimental results (detailed model performance on more benchmark datasets) and details, please refer to our technical report by clicking [here](https://qianwen-res.oss-cn-beijing.aliyuncs.com/QWEN_TECHNICAL_REPORT.pdf).
<br><br>

## Requirements

* python 3.8 and above
* pytorch 1.12 and above, 2.0 and above are recommended
* transformers 4.32 and above
* CUDA 11.4 and above are recommended (this is for GPU users, flash-attention users, etc.)
<br>

## Quickstart

Below, we provide simple examples to show how to use Qwen-Chat with 🤖 ModelScope and 🤗 Transformers.

You can use our pre-built docker images to skip most of the environment setup steps, see Section ["Using Pre-built Docker Images"](#-docker) for more details. 

If not using docker, please make sure you have setup the environment and installed the required packages. Make sure you meet the above requirements, and then install the dependent libraries.

```bash
pip install -r requirements.txt
```

If your device supports fp16 or bf16, we recommend installing [flash-attention](https://github.com/Dao-AILab/flash-attention) (**we support flash attention 2 now.**) for higher efficiency and lower memory usage. (**flash-attention is optional and the project can run normally without installing it**)

```bash
git clone https://github.com/Dao-AILab/flash-attention
cd flash-attention && pip install .
# Below are optional. Installing them might be slow.
# pip install csrc/layer_norm
# If the version of flash-attn is higher than 2.1.1, the following is not needed.
# pip install csrc/rotary
```

Now you can start with ModelScope or Transformers.

### 🤗 Transformers

To use Qwen-Chat for the inference, all you need to do is to input a few lines of codes as demonstrated below. Remember to pass in the correct model names or paths, such as "Qwen/Qwen-7B-Chat" and "Qwen/Qwen-14B-Chat". However, **please make sure that you are using the latest code.**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names: "Qwen/Qwen-7B-Chat", "Qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# use bf16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
# use auto mode, automatically select precision based on the device.
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
    device_map="auto",
    trust_remote_code=True
).eval()

# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# 1st dialogue turn
response, history = model.chat(tokenizer, "你好", history=None)
print(response)
# 你好！很高兴为你提供帮助。

# 2nd dialogue turn
response, history = model.chat(tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
# 这是一个关于一个年轻人奋斗创业最终取得成功的故事。
# 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。
# 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。
# 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。
# 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。
# 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。

# 3rd dialogue turn
response, history = model.chat(tokenizer, "给这个故事起一个标题", history=history)
print(response)
# 《奋斗创业：一个年轻人的成功之路》
```

Running Qwen, the base language model, is also simple.

<details>
  <summary>Running Qwen</summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names: "Qwen/Qwen-7B", "Qwen/Qwen-14B" 
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)
# use bf16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="cpu", trust_remote_code=True).eval()
# use auto mode, automatically select precision based on the device.
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B",
    device_map="auto",
    trust_remote_code=True
).eval()

# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)

inputs = tokenizer('蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是', return_tensors='pt')
inputs = inputs.to(model.device)
pred = model.generate(**inputs)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))
# 蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是亚的斯亚贝巴（Addis Ababa）...
```

</details>

<p id="DownloadModel">
In the event of a network issue while attempting to download model checkpoints and codes from HuggingFace, an alternative approach is to initially fetch the checkpoint from ModelScope and then load it from the local directory as outlined below:
</p>

```python
from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Downloading model checkpoint to a local dir model_dir
# model_dir = snapshot_download('qwen/Qwen-7B')
# model_dir = snapshot_download('qwen/Qwen-7B-Chat')
# model_dir = snapshot_download('qwen/Qwen-14B')
model_dir = snapshot_download('qwen/Qwen-14B-Chat')

# Loading local checkpoints
# trust_remote_code is still set as True since we still load codes from local dir instead of transformers
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True
).eval()
```

### 🤖 ModelScope

ModelScope is an open-source platform for Model-as-a-Service (MaaS), which provides flexible and cost-effective model service to AI developers. Similarly, you can run the models with ModelScope as shown below:

```python
from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

# Model names: "qwen/Qwen-7B-Chat", "qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("qwen/Qwen-7B-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

response, history = model.chat(tokenizer, "你好", history=None)
print(response)
response, history = model.chat(tokenizer, "浙江的省会在哪里？", history=history) 
print(response)
response, history = model.chat(tokenizer, "它有什么好玩的景点", history=history)
print(response)
```

### Batch Inference
Qwen supports batch inference. With flash attention enabled, using batch inference can bring a 40% speedup. The example code is shown below:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GenerationConfig
from qwen_generation_utils import make_context, decode_tokens, get_stop_words_ids

# To generate attention masks automatically, it is necessary to assign distinct
# token_ids to pad_token and eos_token, and set pad_token_id in the generation_config.
tokenizer = AutoTokenizer.from_pretrained(
    './',
    pad_token='<|extra_0|>',
    eos_token='<|endoftext|>',
    padding_side='left',
    trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    './',
    pad_token_id=tokenizer.pad_token_id,
    device_map="auto",
    trust_remote_code=True
).eval()
model.generation_config = GenerationConfig.from_pretrained('./', pad_token_id=tokenizer.pad_token_id)

all_raw_text = ["我想听你说爱我。", "今天我想吃点啥，甜甜的，推荐下", "我马上迟到了，怎么做才能不迟到"]
batch_raw_text = []
for q in all_raw_text:
    raw_text, _ = make_context(
        tokenizer,
        q,
        system="You are a helpful assistant.",
        max_window_size=model.generation_config.max_window_size,
        chat_format=model.generation_config.chat_format,
    )
    batch_raw_text.append(raw_text)

batch_input_ids = tokenizer(batch_raw_text, padding='longest')
batch_input_ids = torch.LongTensor(batch_input_ids['input_ids']).to(model.device)
batch_out_ids = model.generate(
    batch_input_ids,
    return_dict_in_generate=False,
    generation_config=model.generation_config
)
padding_lens = [batch_input_ids[i].eq(tokenizer.pad_token_id).sum().item() for i in range(batch_input_ids.size(0))]

batch_response = [
    decode_tokens(
        batch_out_ids[i][padding_lens[i]:],
        tokenizer,
        raw_text_len=len(batch_raw_text[i]),
        context_length=(batch_input_ids[i].size(0)-padding_lens[i]),
        chat_format="chatml",
        verbose=False,
        errors='replace'
    ) for i in range(len(all_raw_text))
]
print(batch_response)

response, _ = model.chat(tokenizer, "我想听你说爱我。", history=None)
print(response)

response, _ = model.chat(tokenizer, "今天我想吃点啥，甜甜的，推荐下", history=None)
print(response)

response, _ = model.chat(tokenizer, "我马上迟到了，怎么做才能不迟到", history=None)
print(response)
```

### CPU

To deploy our models on CPU, we strongly advise you to use [qwen.cpp](https://github.com/QwenLM/qwen.cpp), which is a pure C++ implementation of Qwen and tiktoken. Check the repo for more details!

Also, it is also simple to directly run the model on CPU, which requires your specification of device:

```python
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
```

However, it is likely that you suffer from extremely low inference efficiency.

### Multiple GPUs

If you suffer from lack of GPU memory and you would like to run the model on more than 1 GPU, you can directly use the default loading method, which is now supported by Transformers. The previous method based on `utils.py` is deprecated.

However, though this method is simple, the efficiency of the native pipeline parallelism is low. We advise you to use vLLM with FastChat and please read the section for deployment.

### x86 Platforms
When deploy on Core™/Xeon® Scalable Processors or with Arc™ GPU, [OpenVINO™ Toolkit](https://docs.openvino.ai/2023.3/gen_ai_guide.html) is recommended. You can install and run this [example notebook](https://github.com/openvinotoolkit/openvino_notebooks/tree/main/notebooks/254-llm-chatbot). For related issues, you are welcome to file an issue at [OpenVINO repo](https://github.com/openvinotoolkit/openvino_notebooks/issues). 

### DashScope
The most simple way to use Qwen through APIs is DashScope API service through Alibaba Cloud. We give an introduction to the usage. Additionally, we provide a script for you to deploy an OpenAI-style API on your own servers.

DashScope is the large language model API service provided by Alibaba Cloud, which now supports Qwen. Note that the models behind DashScope are in-house versions temporarily without details provided. The services include `qwen-turbo` and `qwen-plus`, where the former one runs faster and the latter achieves better performance. For more information, visit the documentation [here](https://dashscope.aliyun.com).

Please head to the official website [link](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key?spm=a2c4g.11186623.0.0.6c2774fahtfXdn) to create a DashScope account and obtain the API key (AK). We recommend setting the AK with an environment variable:
```bash
export DASHSCOPE_API_KEY="YOUR_DASHSCOPE_API_KEY"
```
Then please install the packages and click [here](https://help.aliyun.com/zh/dashscope/developer-reference/install-dashscope-sdk) for the documentation. If you use Python, you can install DashScope with pip:
```bash
pip install dashscope
```
If you use JAVA SDK, you can install it in this way:
```xml
<!-- https://mvnrepository.com/artifact/com.alibaba/dashscope-sdk-java -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dashscope-sdk-java</artifactId>
    <version>the-latest-version</version>
</dependency>
```
The simplest way to use DashScope is the usage with messages, which is similar to OpenAI API. The example is demonstrated below:
```python
import random
from http import HTTPStatus
from dashscope import Generation


def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '如何做西红柿鸡蛋？'}]
    gen = Generation()
    response = gen.call(
        Generation.Models.qwen_turbo,
        messages=messages,
        seed=random.randint(1, 10000),  # set the random seed, optional, default to 1234 if not set
        result_format='message',  # set the result to be "message" format.
    )
    return response


if __name__ == '__main__':
    response = call_with_messages()
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
```
For more usages, please visit the official website for more details.
<br><br>

## Quantization

### GPTQ

We provide a solution based on [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ), and release the Int4 and Int8 quantized models, which achieve nearly lossless model effects but improved performance on both memory costs and inference speed.

Here we demonstrate how to use our provided quantized models for inference. Before you start, make sure you meet the requirements of auto-gptq (e.g., torch 2.0 and above, transformers 4.32.0 and above, etc.) and install the required packages:

```bash
pip install auto-gptq optimum
```

If you meet problems installing `auto-gptq`, we advise you to check out the official [repo](https://github.com/PanQiWei/AutoGPTQ) to find a wheel.

> Note: The pre-compiled `auto-gptq` packages strongly depend on the version of `torch` and its CUDA version. Moreover, due to recent update, 
> you may also encounter unsupported version errors from `transformers`, `optimum`, or `peft`.
> We recommend using the latest versions meeting the following requirements:
> - torch==2.1 auto-gptq>=0.5.1 transformers>=4.35.0 optimum>=1.14.0 peft>=0.6.1
> - torch>=2.0,<2.1 auto-gptq<0.5.0 transformers<4.35.0 optimum<1.14.0 peft>=0.5.0,<0.6.0

Then you can load the quantized model easily and run inference as same as usual:

```python
# Model names: "Qwen/Qwen-7B-Chat-Int4", "Qwen/Qwen-14B-Chat-Int4"
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat-Int4",
    device_map="auto",
    trust_remote_code=True
).eval()
response, history = model.chat(tokenizer, "Hi", history=None)
```

We illustrate the model performance of both BF16, Int8 and Int4 models on the benchmark, and we find that the quantized model does not suffer from significant performance degradation. Results are shown below:

| Quantization         | MMLU | CEval (val) | GSM8K | Humaneval |
|----------------------|:----:|:-----------:|:-----:|:---------:|
| Qwen-1.8B-Chat (BF16)| 43.3 |    55.6     | 33.7  |   26.2    |
| Qwen-1.8B-Chat (Int8)| 43.1 |    55.8     | 33.0  |   27.4    |
| Qwen-1.8B-Chat (Int4)| 42.9 |    52.8     | 31.2  |   25.0    |
| Qwen-7B-Chat (BF16)  | 55.8 |    59.7     | 50.3  |   37.2    |
| Qwen-7B-Chat (Int8)  | 55.4 |    59.4     | 48.3  |   34.8    |
| Qwen-7B-Chat (Int4)  | 55.1 |    59.2     | 49.7  |   29.9    |
| Qwen-14B-Chat (BF16) | 64.6 |    69.8     | 60.1  |   43.9    |
| Qwen-14B-Chat (Int8) | 63.6 |    68.6     | 60.0  |   48.2    |
| Qwen-14B-Chat (Int4) | 63.3 |    69.0     | 59.8  |   45.7    |
| Qwen-72B-Chat (BF16) | 74.4 |    80.1     | 76.4  |   64.6    |
| Qwen-72B-Chat (Int8) | 73.5 |    80.1     | 73.5  |   62.2    |
| Qwen-72B-Chat (Int4) | 73.4 |    80.1     | 75.3  |   61.6    |

### Quantization of KV cache

> NOTE: Please be aware that due to the internal mechanism of Hugging Face, the support files for this functionality 
> (i.e., `cache_autogptq_cuda_256.cpp` and `cache_autogptq_cuda_kernel_256.cu`) may be missing. Please manually download
> them from the Hugging Face Hub and place them into the same folder as the other module files.

The attention KV cache can be quantized and compressed for storage, to get a higher sample throughput. The arguments `use_cache_quantization` and `use_cache_kernel` in `config.json` are provided to enable KV cache quantization. The specific use method is as follows:
```python
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
     device_map="auto",
     trust_remote_code=True,
     use_cache_quantization=True,
     use_cache_kernel=True,
     use_flash_attn=False
)
```
Attention: Currently, KV cache quantization and flash attention cannot be used at the same time.
If you enable KV cache quantization and flash attention at the same time (`use_flash_attn=True`, `use_cache_quantization=True`, `use_cache_kernel=True`), `use_flash_attn` is disabled by default (`use_flash_attn=false`).

We have verified that the use of the quantized Int8-KV-Cache model does not suffer from significant performance degradation in downstream evaluation. In the following, we focus on profiling its memory footprint in different conditions. 
The profiling runs on a single A100-SXM4-80G GPU with PyTorch 2.0.1 and CUDA 11.4. 
We use BF16 models to generate 1024 tokens by default, and "OOM" indicates out-of-memory error.

With KV cache quantization, the model can infer with a larger batch size (bs).

| USE KV Cache |  bs=1  |  bs=4  | bs=16  | bs=32  | bs=64  | bs=100 |
|--------------|:------:|:------:|:------:|:------:|:------:|:------:|
| No           | 16.3GB | 24.1GB | 31.7GB | 48.7GB |  OOM   |  OOM   |
| Yes          | 15.5GB | 17.2GB | 22.3GB | 30.2GB | 48.2GB | 72.4GB |

With KV cache quantization the model can save more memory when generating longer sequence (`sl`, sequence length, referring to the number of tokens generated) at the stage of inference.

| USE KV Cache | sl=512 | sl=1024 | sl=2048 | sl=4096 | sl=8192 |
|--------------|:------:|:-------:|:-------:|:-------:|:-------:|
| No           | 15.2GB | 16.3GB  | 17.6GB  | 19.5GB  | 23.2GB  |
| Yes          |  15GB  | 15.5GB  | 15.8GB  | 16.6GB  | 17.6GB  |

The model with KV cache quantization will convert the format of `layer_past` from float to int8, and meanwhile the quantized `layer-past` will also store the quantization parameters.

Specific steps are as follows:

1. Quantize key/value
```
    qv,scale,zero_point=quantize_cache_v(v)
```
2. Store into layer_past

The following is the format of quantized `layer_past`:
```
    layer_past=((q_key,key_scale,key_zero_point),
                (q_value,value_scale,value_zero_point))
```

The original format of `layer_past` is shown below:
```
    layer_past=(key,value)
```

If you want to use the attention KV which is quantized, you can use the dequantization operation to convert the Int8 key/value back to the float format as follows:
```
    v=dequantize_cache_torch(qv,scale,zero_point)
```
<br>


## Inference Performance

This section provides the statistics of speed and memory of models in different precisions. The speed and memory profiling are conducted using [this script](https://qianwen-res.oss-cn-beijing.aliyuncs.com/profile.py). 

We measured the average inference speed (tokens/s) and GPU memory usage of generating 2048 with the models in BF16, Int8, and Int4. 

<table>
    <tr>
        <td>Model Size</td>
        <td>Quantization</td>
        <td>Speed (Tokens/s)</td>
        <td>GPU Memory Usage</td>
    </tr>
    <tr>
        <td rowspan="3">1.8B</td>
        <td>BF16</td>
        <td>54.09</td>
        <td>4.23GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>55.56</td>
        <td>3.48GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>71.07</td>
        <td>2.91GB</td>
    </tr>
    <tr>
        <td rowspan="3">7B</td>
        <td>BF16</td>
        <td>40.93</td>
        <td>16.99GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>37.47</td>
        <td>11.20GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>50.09</td>
        <td>8.21GB</td>
    </tr>
    <tr>
        <td rowspan="3">14B</td>
        <td>BF16</td>
        <td>32.22</td>
        <td>30.15GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>29.28</td>
        <td>18.81GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>38.72</td>
        <td>13.01GB</td>
    </tr>
    <tr>
        <td rowspan="3">72B</td>
        <td>BF16</td>
        <td>8.48</td>
        <td>144.69GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>9.05</td>
        <td>81.27GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>11.32</td>
        <td>48.86GB</td>
    </tr>
    <tr>
        <td>72B + vLLM</td>
        <td>BF16</td>
        <td>17.60</td>
        <td>2xA100</td>
    </tr>
</table>

The profiling runs on a single A100-SXM4-80G GPU (except 2xA100 is mentioned) with PyTorch 2.0.1, CUDA 11.8, and Flash-Attention 2. (72B + vLLM uses PyTorch 2.1.0 and Cuda 11.8.) The inference speed is averaged over the encoded and generated tokens.

Note: The generation speed of the Int4/Int8 models mentioned above is provided by the autogptq library. The current speed of the model loaded using ``AutoModelForCausalLM.from_pretrained`` will be approximately 20% slower. We have reported this issue to the HuggingFace team and will update it promptly if a solution is available.

We also measure the inference speed and GPU memory usage with different settings of context and generation lengths, Flash-Attention version. You can find the results in the according modelcards on Hugging Face or ModelScope.

## Finetuning

### Usage
Now we provide the official training script, `finetune.py`, for users to finetune the pretrained model for downstream applications in a simple fashion. Additionally, we provide shell scripts to launch finetuning with no worries. This script supports the training with [DeepSpeed](https://github.com/microsoft/DeepSpeed) and [FSDP](https://engineering.fb.com/2021/07/15/open-source/fsdp/). The shell scripts that we provide use DeepSpeed (Note: this may have conflicts with the latest version of pydantic and you should use make sure `pydantic<2.0`) and Peft. You can install them by:
```bash
pip install "peft<0.8.0" deepspeed
```

To prepare your training data, you need to put all the samples into a list and save it to a json file. Each sample is a dictionary consisting of an id and a list for conversation. Below is a simple example list with 1 sample:
```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "你好"
      },
      {
        "from": "assistant",
        "value": "我是一个语言模型，我叫通义千问。"
      }
    ]
  }
]
```

After data preparation, you can use the provided shell scripts to run finetuning. Remember to specify the path to the data file, `$DATA`.

The finetuning scripts allow you to perform:
- Full-parameter finetuning
- LoRA
- Q-LoRA

Full-parameter finetuning requires updating all parameters in the whole training process. To launch your training, run the following script:

```bash
# Distributed training. We do not provide single-GPU training script as the insufficient GPU memory will break down the training.
bash finetune/finetune_ds.sh
```

Remember to specify the correct model name or path, the data path, as well as the output directory in the shell scripts. Another thing to notice is that we use DeepSpeed ZeRO 3 in this script. If you want to make changes, just remove the argument `--deepspeed` or make changes in the DeepSpeed configuration json file based on your requirements. Additionally, this script supports mixed-precision training, and thus you can use `--bf16 True` or `--fp16 True`. Remember to use DeepSpeed when you use fp16 due to mixed precision training. Empirically we advise you to use bf16 to make your training consistent with our pretraining and alignment if your machine supports bf16, and thus we use it by default.

Similarly, to run LoRA, use another script to run as shown below. Before you start, make sure that you have installed `peft`. Also, you need to specify your paths to your model, data, and output. We advise you to use absolute path for your pretrained model. This is because LoRA only saves the adapter and the absolute path in the adapter configuration json file is used for finding out the pretrained model to load. Also, this script support both bf16 and fp16.

```bash
# Single GPU training
bash finetune/finetune_lora_single_gpu.sh
# Distributed training
bash finetune/finetune_lora_ds.sh
```

In comparison with full-parameter finetuning, LoRA ([paper](https://arxiv.org/abs/2106.09685)) only updates the parameters of adapter layers but keeps the original large language model layers frozen. This allows much fewer memory costs and thus fewer computation costs. 

Note that if you use LoRA to finetune the base language model, e.g., Qwen-7B, instead of chat models, e.g., Qwen-7B-Chat, the script automatically switches the embedding and output layer as trainable parameters. This is because the base language model has no knowledge of special tokens brought by ChatML format. Thus these layers should be updated for the model to understand and predict the tokens. Or in another word, if your training brings in special tokens in LoRA, you should set the layers to trainable parameters by setting `modules_to_save` inside the code. Also, if we have these parameters trainable, it is not available to use ZeRO 3, and this is why we use ZeRO 2 in the script by default. If you do not have new trainable parameters, you can switch to ZeRO 3 by changing the DeepSpeed configuration file. Additionally, we find that there is a significant gap between the memory footprint of LoRA with and without these trainable parameters. Therefore, if you have trouble with memory, we advise you to LoRA finetune the chat models. Check the profile below for more information. 

If you still suffer from insufficient memory, you can consider Q-LoRA ([paper](https://arxiv.org/abs/2305.14314)), which uses the quantized large language model and other techniques such as paged attention to allow even fewer memory costs. 

Note: to run single-GPU Q-LoRA training, you may need to install `mpi4py` through `pip` or `conda`.

To run Q-LoRA, directly run the following script:

```bash
# Single GPU training
bash finetune/finetune_qlora_single_gpu.sh
# Distributed training
bash finetune/finetune_qlora_ds.sh
```

For Q-LoRA, we advise you to load our provided quantized model, e.g., Qwen-7B-Chat-Int4. You **SHOULD NOT** use the bf16 models. Different from full-parameter finetuning and LoRA, only fp16 is supported for Q-LoRA. For single-GPU training, we have to use DeepSpeed for mixed-precision training due to our observation of errors caused by torch amp. Besides, for Q-LoRA, the troubles with the special tokens in LoRA still exist. However, as we only provide the Int4 models for chat models, which means the language model has learned the special tokens of ChatML format, you have no worry about the layers. Note that the layers of the Int4 model should not be trainable, and thus if you introduce special tokens in your training, Q-LoRA might not work.

> NOTE: Please be aware that due to the internal mechanisms of Hugging Face, certain non-Python files (e.g., `*.cpp` and `*.cu`) 
> may be missing from the saved checkpoint. You may need to manually copy them to the directory containing other files.

Different from full-parameter finetuning, the training of both LoRA and Q-LoRA only saves the adapter parameters. Suppose your training starts from Qwen-7B, you can load the finetuned model for inference as shown below:

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()
```

> NOTE: If `peft>=0.8.0`, it will try to load the tokenizer as well, however, initialized without `trust_remote_code=True`, leading to `ValueError: Tokenizer class QWenTokenizer does not exist or is not currently imported.` Currently, you could downgrade `peft<0.8.0` or move tokenizer files elsewhere to workaround this issue.

If you want to merge the adapters and save the finetuned model as a standalone model (you can only do this with LoRA, and you CANNOT merge the parameters from Q-LoRA), you can run the following codes:

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()

merged_model = model.merge_and_unload()
# max_shard_size and safe serialization are not necessary. 
# They respectively work for sharding checkpoint and save the model to safetensors
merged_model.save_pretrained(new_model_directory, max_shard_size="2048MB", safe_serialization=True)
```

The `new_model_directory` directory will contain the merged model weights and module files. Please note that `*.cu` and `*.cpp` files may be missing in the saved files. If you wish to use the KV cache functionality, please manually copy them. Besides, the tokenizer files are not saved in the new directory in this step. You can copy the tokenizer files or use the following code
```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    path_to_adapter, # path to the output directory
    trust_remote_code=True
)

tokenizer.save_pretrained(new_model_directory)
```


Note: For multi-GPU training, you need to specify the proper hyperparameters for distributed training based on your machine. Besides, we advise you to specify your maximum sequence length with the argument `--model_max_length`, based on your consideration of data, memory footprint, and training speed.

### Quantize Fine-tuned Models

This section applies to full-parameter/LoRA fine-tuned models. (Note: You do not need to quantize the Q-LoRA fine-tuned model because it is already quantized.)
If you use LoRA, please follow the above instructions to merge your model before quantization. 

We recommend using [auto_gptq](https://github.com/PanQiWei/AutoGPTQ) to quantize the finetuned model. 

```bash
pip install auto-gptq optimum
```

Note: Currently AutoGPTQ has a bug referred in [this issue](https://github.com/PanQiWei/AutoGPTQ/issues/370). Here is a [workaround PR](https://github.com/PanQiWei/AutoGPTQ/pull/495), and you can pull this branch and install from the source.

First, prepare the calibration data. You can reuse the fine-tuning data, or use other data following the same format.

Second, run the following script:

```bash
python run_gptq.py \
    --model_name_or_path $YOUR_LORA_MODEL_PATH \
    --data_path $DATA \
    --out_path $OUTPUT_PATH \
    --bits 4 # 4 for int4; 8 for int8
```

This step requires GPUs and may costs a few hours according to your data size and model size.

Then, copy all `*.py`, `*.cu`, `*.cpp` files and `generation_config.json` to the output path. And we recommend you to overwrite `config.json` by copying the file from the coresponding official quantized model
(for example, if you are fine-tuning `Qwen-7B-Chat` and use `--bits 4`, you can find the `config.json` from [Qwen-7B-Chat-Int4](https://huggingface.co/Qwen/Qwen-7B-Chat-Int4/blob/main/config.json)).
You should also rename the ``gptq.safetensors`` into ``model.safetensors``.

Finally, test the model by the same method to load the official quantized model. For example,

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

tokenizer = AutoTokenizer.from_pretrained("/path/to/your/model", trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    "/path/to/your/model",
    device_map="auto",
    trust_remote_code=True
).eval()

response, history = model.chat(tokenizer, "你好", history=None)
print(response)
```

### Multinode Finetuning

Our provided scripts support multinode finetuning. You can refer to the comments in [script](./finetune/finetune_lora_ds.sh) to correctly set corresponding arguments and launch the script on each node. For more information about multinode distributed training, please refer to [torchrun](https://pytorch.org/docs/stable/elastic/run.html).

Note: DeepSpeed ZeRO 3 requires much greater inter-node communication rate than ZeRO 2, which will significantly reduce the training speed in the case of multinode finetuning. Therefore, we do not recommend using DeepSpeed ZeRO 3 configurations in multinode finetuning scripts.

### Profiling of Memory and Speed
We profile the GPU memory and training speed of both LoRA (LoRA (emb) refers to training the embedding and output layer, while LoRA has no trainable embedding and output layer) and Q-LoRA in the setup of single-GPU training. In this test, we experiment on a single A100-SXM4-80G GPU, and we use CUDA 11.8 and Pytorch 2.0. Flash attention 2 is applied. We uniformly use a batch size of 1 and gradient accumulation of 8. We profile the memory (GB) and speed (s/iter) of inputs of different lengths, namely 256, 512, 1024, 2048, 4096, and 8192. We also report the statistics of full-parameter finetuning with Qwen-7B on 2 A100 GPUs. We only report the statistics of 256, 512, and 1024 tokens due to the limitation of GPU memory. 

For Qwen-7B, we also test the performance of multinode finetuning. We experiment using two servers, each containing two A100-SXM4-80G GPUs, and the rest of configurations are the same as other Qwen-7B experiments. The results of multinode finetuning are marked as LoRA (multinode) in the table.

For Qwen-72B, we experiment in two ways: 1) Lora fintuning + DeepSpeed ZeRO 3 on 4 A100-SXM4-80G GPUs and 2) QLora (int4) fine-tuning on a single A100-SXM4-80G GPU. Note that OOM occurs on 4 A100-SXM4-80G GPUs both with LoRA (emb) fine-tuning and LoRA fine-tuning without Deepspeed ZeRO 3 (you can pass `--deepspeed finetune/ds_config_zero3.json` to [`finetune/finetune_lora_ds.sh`](finetune/finetune_lora_ds.sh) to enable DeepSpeed ZeRO 3).

The statistics are listed below:

<table>
    <tr>
      <th rowspan="2">Model Size</th><th rowspan="2">Method</th><th rowspan="2">#Nodes</th><th rowspan="2">#GPUs per node</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">256</th><th align="center">512</th><th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th>
    </tr>
    <tr>
        <th rowspan="4">1.8B</th><td>LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">6.7G / 1.0s/it</td><td align="center">7.4G / 1.0s/it</td><td align="center">8.4G / 1.1s/it</td><td align="center">11.0G / 1.7s/it</td><td align="center">16.2G / 3.3s/it</td><td align="center">21.8G / 6.8s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td>
        <td>1</td><td>1</td>
        <td align="center">13.7G / 1.0s/it</td><td align="center">14.0G / 1.0s/it</td><td align="center">14.0G / 1.1s/it</td><td align="center">15.1G / 1.8s/it</td><td align="center">19.7G / 3.4s/it</td><td align="center">27.7G / 7.0s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">5.8G / 1.4s/it</td><td align="center">6.0G / 1.4s/it</td><td align="center">6.6G / 1.4s/it</td><td align="center">7.8G / 2.0s/it</td><td align="center">10.2G / 3.4s/it</td><td align="center">15.8G / 6.5s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td>
        <td>1</td><td>1</td>
        <td align="center">43.5G / 2.1s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.3s/it</td><td align="center">47.1G / 2.8s/it</td><td align="center">48.3G / 5.6s/it</td>
    </tr>
    <tr>
        <th rowspan="5">7B</th>
        <td>LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">20.1G / 1.2s/it</td><td align="center">20.4G / 1.5s/it</td><td align="center">21.5G / 2.8s/it</td><td align="center">23.8G / 5.2s/it</td><td align="center">29.7G / 10.1s/it</td><td align="center">36.6G / 21.3s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td>
        <td>1</td><td>1</td>
        <td align="center">33.7G / 1.4s/it</td><td align="center">34.1G / 1.6s/it</td><td align="center">35.2G / 2.9s/it</td><td align="center">35.1G / 5.3s/it</td><td align="center">39.2G / 10.3s/it</td><td align="center">48.5G / 21.7s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">11.5G / 3.0s/it</td><td align="center">11.5G / 3.0s/it</td><td align="center">12.3G / 3.5s/it</td><td align="center">13.9G / 7.0s/it</td><td align="center">16.9G / 11.6s/it</td><td align="center">23.5G / 22.3s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td>
<td>1</td><td>2</td>
<td align="center">139.2G / 4.0s/it</td><td align="center">148.0G / 4.0s/it</td><td align="center">162.0G / 4.5s/it</td><td align="center">-</td><td align="center">-</td><td align="center">-</td>
    </tr>
    <tr>
        <td>LoRA (multinode)</td>
        <td>2</td><td>2</td>
        <td align="center">74.7G / 2.09s/it</td><td align="center">77.6G / 3.16s/it</td><td align="center">84.9G / 5.17s/it</td><td align="center">95.1G / 9.25s/it</td><td align="center">121.1G / 18.1s/it</td><td align="center">155.5G / 37.4s/it</td>
    </tr>
    <tr>
        <th rowspan="3">14B</th>
        <td>LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">34.6G / 1.6s/it</td><td align="center">35.1G / 2.4s/it</td><td align="center">35.3G / 4.4s/it</td><td align="center">37.4G / 8.4s/it</td><td align="center">42.5G / 17.0s/it</td><td align="center">55.2G / 36.0s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td>
        <td>1</td><td>1</td>
        <td align="center">51.2 / 1.7s/it</td><td align="center">51.1G / 2.6s/it</td><td align="center">51.5G / 4.6s/it</td><td align="center">54.1G / 8.6s/it</td><td align="center">56.8G / 17.2s/it</td><td align="center">67.7G / 36.3s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">18.7G / 5.3s/it</td><td align="center">18.4G / 6.3s/it</td><td align="center">18.9G / 8.2s/it</td><td align="center">19.9G / 11.8s/it</td><td align="center">23.0G / 20.1s/it</td><td align="center">27.9G / 38.3s/it</td>
    </tr>
    <tr>
        <th rowspan="2">72B</th>
        <td>LoRA + Deepspeed Zero3</td>
        <td>1</td><td>4</td>
        <td align="center">215.4G / 17.6s/it</td><td align="center">217.7G / 20.5s/it</td><td align="center">222.6G / 29.4s/it</td><td align="center">228.8G / 45.7s/it</td><td align="center">249.0G / 83.4s/it</td><td align="center">289.2G / 161.5s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">61.4G / 27.4s/it</td><td align="center">61.4G / 31.5s/it</td><td align="center">62.9G / 41.4s/it</td><td align="center">64.1G / 59.5s/it</td><td align="center">68.0G / 97.7s/it</td><td align="center">75.6G / 179.8s/it</td>
    </tr>
</table>

<br>

## Deployment

### vLLM 

For deployment and fast inference, we suggest using vLLM. 

If you use **CUDA 12.1 and PyTorch 2.1**, you can directly use the following command to install vLLM.

```bash
pip install vllm
```

Otherwise, please refer to the official vLLM [Installation Instructions](https://docs.vllm.ai/en/latest/getting_started/installation.html).

#### vLLM + Transformer-like Wrapper

You can download the [wrapper codes](examples/vllm_wrapper.py) and execute the following commands for multiple rounds of dialogue interaction. (Note: It currently only supports the ``model.chat()`` method.)

```python
from vllm_wrapper import vLLMWrapper

model = vLLMWrapper('Qwen/Qwen-7B-Chat', tensor_parallel_size=1)
# model = vLLMWrapper('Qwen/Qwen-7B-Chat-Int4', tensor_parallel_size=1, dtype="float16")

response, history = model.chat(query="你好", history=None)
print(response)
response, history = model.chat(query="给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
response, history = model.chat(query="给这个故事起一个标题", history=history)
print(response)
```

#### vLLM + Web Demo / OpenAI-like API

You can use FastChat to lauch a web demo or an OpenAI API server. First, install FastChat:

```bash
pip install "fschat[model_worker,webui]"
```

To run Qwen with vLLM and FastChat, you need launch a controller by:
```bash
python -m fastchat.serve.controller
```

Then you can launch the model worker, which means loading your model for inference. For single GPU inference, you can directly run:
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --dtype bfloat16
# python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --dtype float16 # run int4 model
```
However, if you hope to run the model on multiple GPUs for faster inference or larger memory, you can use tensor parallelism supported by vLLM. Suppose you run the model on 4 GPUs, the command is shown below:
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4 --dtype bfloat16
# python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4 --dtype float16 # run int4 model
```

After launching your model worker, you can launch a:

* Web UI Demo
```bash
python -m fastchat.serve.gradio_web_server
```

* OpenAI API
```bash
python -m fastchat.serve.openai_api_server --host localhost --port 8000
```

However, if you find it difficult to use vLLM and FastChat, you can try our provided simplest methods to deploy a web demo, CLI demo, and API.


### Web UI

We provide code for users to build a web UI demo (thanks to @wysaid). Before you start, make sure you install the following packages:

```
pip install -r requirements_web_demo.txt
```

Then run the command below and click on the generated link:

```bash
python web_demo.py
```

<p align="center">
    <br>
    <img src="assets/web_demo.gif" width="600" />
    <br>
<p>

### CLI Demo

We provide a CLI demo example in `cli_demo.py`, which supports streaming output for the generation. Users can interact with Qwen-7B-Chat by inputting prompts, and the model returns model outputs in the streaming mode. Run the command below:

```bash
python cli_demo.py
```

<p align="center">
    <br>
    <img src="assets/cli_demo.gif" width="600" />
    <br>
<p>
<br>

### API

We provide methods to deploy local API based on OpenAI API (thanks to @hanpenggit). Before you start, install the required packages:

```bash
pip install fastapi uvicorn "openai<1.0" pydantic sse_starlette
```

Then run the command to deploy your API:

```bash
python openai_api.py
```

You can change your arguments, e.g., `-c` for checkpoint name or path, `--cpu-only` for CPU deployment, etc. If you meet problems launching your API deployment, updating the packages to the latest version can probably solve them.

Using the API is also simple. See the example below:

```python
import openai
openai.api_base = "http://localhost:8000/v1"
openai.api_key = "none"

# create a request activating streaming response
for chunk in openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=True 
    # Specifying stop words in streaming output format is not yet supported and is under development.
):
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

# create a request not activating streaming response
response = openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=False,
    stop=[] # You can add custom stop words here, e.g., stop=["Observation:"] for ReAct prompting.
)
print(response.choices[0].message.content)
```

<p align="center">
    <br>
    <img src="assets/openai_api.gif" width="600" />
    <br>
<p>

**Function calling** is also supported (but only when `stream=False` for the moment). See the [example usage](examples/function_call_examples.py) here.
<br><br>

## 🐳 Docker

To simplify the deployment process, we provide docker images with pre-built environments: [qwenllm/qwen](https://hub.docker.com/r/qwenllm/qwen). You only need to install the driver and download model files to launch demos, deploy OpenAI API, and finetune the model.

### Preparation

1. Install the correct version of Nvidia driver depending on the image to use:
  - `qwenllm/qwen:cu117` (**recommend**): `>= 515.48.07`
  - `qwenllm/qwen:cu114` (w/o flash-attention): `>= 470.82.01`
  - `qwenllm/qwen:cu121`: `>= 530.30.02`
  - `qwenllm/qwen:latest`: same as `qwenllm/qwen:cu117`

2. Install and configure [docker](https://docs.docker.com/engine/install/) and [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html):

```bash
# configure docker
sudo systemctl start docker
# test if docker is correctly installed
sudo docker run hello-world

# configure nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
# test if nvidia-container-toolkit is correctly installed
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

3. Download model checkpoints and codes to your environment (see [here](#DownloadModel)).

### Deployment

Here we use Qwen-7B-Chat as an example. Before launching a web demo or API, you can setup the configuration as shown below:

```bash
IMAGE_NAME=qwenllm/qwen:cu117
PORT=8901
CHECKPOINT_PATH=/path/to/Qwen-7B-Chat   # Path to downloaded model checkpoints and codes
```
The following scripts can help you build:

* OpenAI API
```bash
bash docker/docker_openai_api.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* Web UI
```bash
bash docker/docker_web_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* CLI Demo
```bash
bash docker/docker_cli_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH}
```

The commands above will automatically download the required image and launch a Web UI demo in background (the service will auto-restart). You can open `http://localhost:${PORT}` on the host to use the demo.

The demo is successfully launched if you see the following output:

```text
Successfully started web demo. Open '...' to try!
Run `docker logs ...` to check demo status.
Run `docker rm -f ...` to stop and remove the demo.
```

If you want to check the status of the demo, you can use `docker logs qwen` to display outputs.

You can use `docker rm -f qwen` to stop the service and remove the container.


### Finetuning

The method of finetuning using the pre-built Docker image is basically the same as [the above chapter](#Finetuning) (we have already installed dependencies in the image):

The following is an example of single-GPU LoRA:
```bash
IMAGE_NAME=qwenllm/qwen:cu117
CHECKPOINT_PATH=/path/to/Qwen-7B                # Path to downloaded model checkpoints and codes
#CHECKPOINT_PATH=/path/to/Qwen-7B-Chat-Int4     # Path to downloaded model checkpoints and codes (Q-LoRA)
DATA_PATH=/path/to/data/root                    # Prepare finetune data at ${DATA_PATH}/example.json
OUTPUT_PATH=/path/to/output/checkpoint          # Path to finetune outputs

# Use all host devices by default
DEVICE=all
# If you need to specify GPUs for training, set device as follow (NOTE: internal quotation marks cannot be omitted)
#DEVICE='"device=0,1,2,3"'

mkdir -p ${OUTPUT_PATH}

# Single-GPU LoRA finetuning
docker run --gpus ${DEVICE} --rm --name qwen \
    --mount type=bind,source=${CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-7B \
    --mount type=bind,source=${DATA_PATH},target=/data/shared/Qwen/data \
    --mount type=bind,source=${OUTPUT_PATH},target=/data/shared/Qwen/output_qwen \
    --shm-size=2gb \
    -it ${IMAGE_NAME} \
    bash finetune/finetune_lora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B/ -d /data/shared/Qwen/data/example.json
```

To make a change to single-GPU Q-LoRA for example, you just need to modify the bash command inside `docker run`:
```bash
bash finetune/finetune_qlora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B-Chat-Int4/ -d /data/shared/Qwen/data/example.json
```
<br>

## 🔥 System Prompt
Qwen-1.8-Chat and Qwen-72B-Chat have been fully trained on diverse system prompts with multiple rounds of complex interactions, so that they can follow a variety of system prompts and realize model customization in context, further improving the scalability of Qwen-chat.

With System Prompt, Qwen-Chat can realize **roly playing**, **language style transfer**, **task setting**, and **behavior setting**.

![](assets/system_prompt_language_style.png)

![](assets/system_prompt_role_play_en.png)

For more information, please refer to the [example documentation](examples/system_prompt.md).

## Tool Usage

Qwen-Chat has been optimized for tool usage and function calling capabilities. Users can develop agents, LangChain applications, and even augment Qwen with a Python Code Interpreter.

We provide documentation on how to implement tool calls based on the principle of ReAct Prompting, please refer to [the ReAct example](examples/react_prompt.md). Based on this principle, we provide support for function calling in [openai_api.py](openai_api.py).

We have tested the model's tool calling capabilities on our open-source Chinese evaluation benchmark and found that Qwen-Chat consistently performs well:

<table>
    <tr>
        <th colspan="4" align="center">Chinese Tool-Use Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th align="center">Model</th><th align="center">Tool Selection (Acc.↑)</th><th align="center">Tool Input (Rouge-L↑)</th><th align="center">False Positive Error↓</th>
    </tr>
    <tr>
        <td>GPT-4</td><td align="center">98.0%</td><td align="center">0.953</td><td align="center">23.9%</td>
    </tr>
    <tr>
        <td>GPT-3.5</td><td align="center">74.5%</td><td align="center">0.807</td><td align="center">80.6%</td>
    </tr>
    <tr>
        <td>Qwen-1_8B-Chat</td><td align="center">85.0%</td><td align="center">0.839</td><td align="center">27.6%</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td><td align="center">95.5%</td><td align="center">0.900</td><td align="center">11.6%</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td><td align="center">96.9%</td><td align="center">0.917</td><td align="center">5.6%</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td><td align="center">98.2%</td><td align="center">0.927</td><td align="center">1.1%</td>
    </tr>
</table>

To assess Qwen's ability to use the Python Code Interpreter for tasks such as mathematical problem solving, data visualization, and other general-purpose tasks such as file handling and web scraping, we have created and open-sourced a benchmark specifically designed for evaluating these capabilities. You can find the benchmark at this [link](https://github.com/QwenLM/Qwen-Agent/tree/main/benchmark).

We have observed that Qwen performs well in terms of code executability and result accuracy when generating code:

<table>
    <tr>
        <th colspan="5" align="center">Code Interpreter Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th rowspan="2" align="center">Model</th>
        <th colspan="3" align="center">Accuracy of Code Execution Results (%)</th>
        <th colspan="1" align="center">Executable Rate of Code (%)</th>
    </tr>
    <tr>
        <th align="center">Math↑</th><th align="center">Visualization-Hard↑</th><th align="center">Visualization-Easy↑</th><th align="center">General↑</th>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td align="center">82.8</td>
        <td align="center">66.7</td>
        <td align="center">60.8</td>
        <td align="center">82.8</td>
    </tr>
    <tr>
        <td>GPT-3.5</td>
        <td align="center">47.3</td>
        <td align="center">33.3</td>
        <td align="center">55.7</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>LLaMA2-13B-Chat</td>
        <td align="center">8.3</td>
        <td align="center">1.2</td>
        <td align="center">15.2</td>
        <td align="center">48.3</td>
    </tr>
    <tr>
        <td>CodeLLaMA-13B-Instruct</td>
        <td align="center">28.2</td>
        <td align="center">15.5</td>
        <td align="center">21.5</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>InternLM-20B-Chat</td>
        <td align="center">34.6</td>
        <td align="center">10.7</td>
        <td align="center">25.1</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>ChatGLM3-6B</td>
        <td align="center">54.2</td>
        <td align="center">4.8</td>
        <td align="center">15.2</td>
        <td align="center">67.1</td>
    </tr>
    <tr>
        <td>Qwen-1.8B-Chat</td>
        <td align="center">25.6</td>
        <td align="center">21.4</td>
        <td align="center">22.8</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td>
        <td align="center">41.9</td>
        <td align="center">23.8</td>
        <td align="center">38.0</td>
        <td align="center">67.2</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td>
        <td align="center">58.4</td>
        <td align="center">31.0</td>
        <td align="center">45.6</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td>
        <td align="center">72.7</td>
        <td align="center">41.7</td>
        <td align="center">43.0</td>
        <td align="center">82.8</td>
    </tr>
</table>

<p align="center">
    <br>
    <img src="assets/code_interpreter_showcase_001.jpg" />
    <br>
<p>

<br>

## Long-Context Understanding

To extend the context length and break the bottleneck of training sequence length, we introduce several techniques, including NTK-aware interpolation, window attention, and LogN attention scaling, to extend the context length of Qwen-14B from 2K to over 8K tokens, and Qwen-1.8B/7B from 8K to 32K tokens. 

For Qwen-72B, we adapt RoPE to longer contexts with a larger rotary base. Qwen-72B supports the max context length of 32K tokens.

We conduct language modeling experiments on the arXiv dataset with the PPL evaluation and find that Qwen can reach outstanding performance in the scenario of long context. Results are demonstrated below:

<table>
    <tr>
        <th rowspan="2">Model</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th><th align="center">16384</th><th align="center">32768</th>
    </tr>
     <tr>
        <td>Qwen-7B (original)</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">39.35</td><td align="center">469.81</td><td align="center">2645.09</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.59</td><td align="center">3.66</td><td align="center">5.71</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.58</td><td align="center">3.56</td><td align="center">4.62</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.58</td><td align="center">3.49</td><td align="center">4.32</td><td align="center">-</td>
    </tr>
    <tr>
    <tr>
        <td>Qwen-1.8B</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.13</b></td><td align="center"><b>3.89</b></td><td align="center">17.42</td><td align="center">433.85</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.14</b></td><td align="center"><b>3.93</b></td><td align="center"><b>3.82</b></td><td align="center"><b>3.83</b></td>
    </tr>
    <tr>
        <td>Qwen-7B</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.31</b></td><td align="center">7.27</td><td align="center">181.49</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.33</b></td><td align="center"><b>3.22</b></td><td align="center"><b>3.17</b></td>
    </tr>
    <tr>
        <td>Qwen-14B</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center">22.79</td><td align="center">334.65</td><td align="center">3168.35</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center"><b>3.29</b></td><td align="center"><b>3.18</b></td><td align="center">3.42</td><td align="center">-</td>
    </tr>
    <tr>
        <td>Qwen-72B</td><td align="center"><b>-</b></td><td align="center"><b>-</b></td><td align="center">-</td><td align="center"><b>2.83</b></td><td align="center"><b>2.73</b></td><td align="center"><b>2.72</b></td>
    </tr>
    </tr>
</table>

Furthermore, to verify the ability of Qwen-72B-Chat on long text understanding, we tested it on [L-Eval](https://arxiv.org/abs/2307.11088) (closed-ended tasks). The results are as follows:

| Model             | Input Length | Average   |  Coursera  |    GSM     |   QuALITY  |    TOEFL   |   CodeU    |  SFcition  |
|:------------------|:------------:|:---------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| ChatGPT-3.5-16k   |     16K      |   60.73   | **63.51**  | **84.00**  |   61.38    |    78.43   | **12.22**  |    64.84   |
| **Qwen-72B-Chat** |     32K      | **62.30** |   58.13    |   76.00    | **77.22**  |  **86.24** |    6.66    |  **69.53** |

We conducted the "needle in a haystack" experiment (the idea came from [@Greg Kamradt](https://twitter.com/GregKamradt/status/1727018183608193393)) to test whether the model can retrieve information at different positions in the inputs of different lengths, the result is as follows:

![](assets/qwen_72b_needle_in_a_haystack.png)

The above results show that Qwen-72B-Chat can accurately retrieve information placed in various positions within an input length of 32k, proving its excellent long text understanding capabilities.

## Tokenizer

Our tokenizer based on tiktoken is different from other tokenizers, e.g., sentencepiece tokenizer. You need to pay attention to special tokens, especially in finetuning. For more detailed information on the tokenizer and related use in fine-tuning, please refer to the [documentation](tokenization_note.md).
<br><br>

## Reproduction

For your reproduction of the model performance on benchmark datasets, we provide scripts for you to reproduce the results. Check [eval/EVALUATION.md](eval/EVALUATION.md) for more information. Note that the reproduction may lead to slight differences from our reported results.
<br><br>

## FAQ

If you meet problems, please refer to [FAQ](FAQ.md) and the issues first to search a solution before you launch a new issue.
<br><br>

## Citation
If you find our work helpful, feel free to give us a cite.

```
@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
}
```
<br>

## License Agreement

The source code provided at <https://github.com/QwenLM/Qwen> is licensed under the [Apache 2.0 License](./LICENSE) that can be found at the root directory.

Researchers and developers are free to use the codes and model weights of both Qwen and Qwen-Chat. For their commercial use, please check the License Agreement accompanying each model.

- Qwen-72B, Qwen-14B, and Qwen-7B are licensed under the [Tongyi Qianwen LICENSE AGREEMENT](./Tongyi%20Qianwen%20LICENSE%20AGREEMENT) that can be found at the corresponding HuggingFace and ModelScope repository. For commercial use, please fill out the form ([72B](https://dashscope.console.aliyun.com/openModelApply/Qwen-72B-Chat), [14B](https://dashscope.console.aliyun.com/openModelApply/Qwen-14B-Chat), and [7B](https://dashscope.console.aliyun.com/openModelApply/qianwen)) to apply.

- Qwen-1.8B is licensed under the [Tongyi Qianwen RESEARCH LICENSE AGREEMENT](./Tongyi%20Qianwen%20RESEARCH%20LICENSE%20AGREEMENT) that can be found at the corresponding HuggingFace and ModelScope repository. For commercial use, please contact us.
<br><br>

## Contact Us

If you are interested to leave a message to either our research team or product team, join our Discord or WeChat groups! Also, feel free to send an email to qianwen_opensource@alibabacloud.com.

```

## File: `README_CN.md`
```markdown
<p align="left">
    中文</a>&nbsp ｜ &nbsp<a href="README.md">English</a>&nbsp ｜ &nbsp<a href="README_JA.md">日本語</a> ｜ &nbsp<a href="README_FR.md">Français</a> ｜ &nbsp<a href="README_ES.md">Español</a>
</p>
<br><br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/logo_qwen.jpg" width="400"/>
<p>
<br>

<p align="center">
        🤗 <a href="https://huggingface.co/Qwen">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/qwen">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2309.16609">Paper</a> &nbsp&nbsp ｜ &nbsp&nbsp🖥️ <a href="https://modelscope.cn/studios/qwen/Qwen-72B-Chat-Demo/summary">Demo</a>
<br>
<a href="assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp<a href="https://discord.gg/z3GAxXZ9Ce">Discord</a>&nbsp&nbsp ｜  &nbsp&nbsp<a href="https://dashscope.aliyun.com">API</a>&nbsp&nbsp | &nbsp&nbsp<a href="https://qianwen.aliyun.com">Web</a>&nbsp&nbsp | &nbsp&nbsp<a href="https://apps.apple.com/cn/app/%E9%80%9A%E4%B9%89%E5%8D%83%E9%97%AE/id6466733523">APP</a>
</p>
<br><br>

> [!Important]
> Qwen2已开，欢迎关注！看这里：[QwenLM/Qwen2](https://github.com/QwenLM/Qwen2)
>
> Qwen2模型代码和用法相比此前版本有较大不同，因此我们使用新的repo进行维护。此repo ([QwenLM/Qwen](https://github.com/QwenLM/Qwen)) 已停止主要更新维护。

> [!Warning]
> 请勿混用[Qwen](https://github.com/QwenLM/Qwen)和[Qwen2](https://github.com/QwenLM/Qwen2)代码，两者并不兼容。
<br>

|     |                                                              Qwen-Chat                                                               |                                                                Qwen-Chat (Int4)                                                                |                        Qwen-Chat (Int8)                         |                                                            Qwen                                                            |
|-----|:------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 1.8B  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B">🤗</a>  |
| 7B  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B">🤗</a>  |
| 14B | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B">🤗</a> |
| 72B | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B">🤗</a> |


  
我们开源了**Qwen**（通义千问）系列工作，当前开源模型的参数规模为18亿（1.8B）、70亿（7B）、140亿（14B）和720亿（72B）。本次开源包括基础模型**Qwen**，即**Qwen-1.8B**、**Qwen-7B**、**Qwen-14B**、**Qwen-72B**，以及对话模型**Qwen-Chat**，即**Qwen-1.8B-Chat**、**Qwen-7B-Chat**、**Qwen-14B-Chat**和**Qwen-72B-Chat**。模型链接在表格中，请点击了解详情。同时，我们公开了我们的<b><a href="https://arxiv.org/abs/2309.16609">技术报告</a></b>，请点击上方论文链接查看。

当前基础模型已经稳定训练了大规模高质量且多样化的数据，覆盖多语言（当前以中文和英文为主），总量高达3万亿token。在相关基准评测中，Qwen系列模型拿出非常有竞争力的表现，显著超出同规模模型并紧追一系列最强的闭源模型。此外，我们利用SFT和RLHF技术实现对齐，从基座模型训练得到对话模型。Qwen-Chat具备聊天、文字创作、摘要、信息抽取、翻译等能力，同时还具备一定的代码生成和简单数学推理的能力。在此基础上，我们针对LLM对接外部系统等方面针对性地做了优化，当前具备较强的工具调用能力，以及最近备受关注的Code Interpreter的能力和扮演Agent的能力。我们将各个大小模型的特点列到了下表。

| 模型        |   开源日期   | 最大上下文长度 | System Prompt强化 | 预训练token数 | 微调（Q-Lora）最小GPU用量 | 生成2048个token的最小显存占用（Int4） | 工具调用 |
|:----------|:--------:|:-------:|:---------------:|:---------:|:-----------------:|:-------------------:|:----:|
| Qwen-1.8B | 23.11.30 |   32K   |        ✅        |   2.2T    |       5.8GB       |        2.9GB        |  ✅   |  
| Qwen-7B   | 23.08.03 |   32K   |        ❎        |   2.4T    |      11.5GB       |        8.2GB        |  ✅   |   
| Qwen-14B  | 23.09.25 |   8K    |        ❎        |   3.0T    |      18.7GB       |       13.0GB        |  ✅   |
| Qwen-72B  | 23.11.30 |   32K   |        ✅        |   3.0T    |      61.4GB       |       48.9GB        |  ✅   |   

  
在这个项目中，你可以了解到以下内容

* 快速上手Qwen-Chat教程，玩转大模型推理
* 量化模型相关细节，包括GPTQ和KV cache量化
* 推理性能数据，包括推理速度和显存占用
* 微调的教程，帮你实现全参数微调、LoRA以及Q-LoRA
* 部署教程，以vLLM和FastChat为例
* 搭建Demo的方法，包括WebUI和CLI Demo
* 搭建API的方法，我们提供的示例为OpenAI风格的API
* 更多关于Qwen在工具调用、Code Interpreter、Agent方面的内容
* 长序列理解能力及评测
* 使用协议
* ...

如果遇到问题，请优先考虑查询[FAQ](FAQ.md)。如仍未解决，随时提出issue（但建议使用英语或提供翻译，有助于帮助更多用户）。如果想帮助我们提升，欢迎提交Pull Requests！

想和我们一起讨论和聊天的话，赶紧加入我们的微信群和Discord server（入口见文档开头部分）！
<br><br>

## 新闻

* 2023.11.30 🔥 我们推出 **Qwen-72B** 和 **Qwen-72B-Chat**，它们在 3T tokens上进行训练，并支持 32k 上下文。同时也发布了 **Qwen-1.8B** 和 **Qwen-1.8B-Chat**。我们还增强了 Qwen-72B-Chat 和 Qwen-1.8B-Chat 的系统指令（System Prompt）功能，请参阅[示例文档](examples/system_prompt.md)。此外，我们还对**昇腾910**以及**海光DCU**实现了推理的支持，详情请查看`ascend-support`及`dcu-support`文件夹。
* 2023年10月17日 我们推出了Int8量化模型**Qwen-7B-Chat-Int8**和**Qwen-14B-Chat-Int8**。
* 2023年9月25日 在魔搭社区（ModelScope）和Hugging Face推出**Qwen-14B**和**Qwen-14B-Chat**模型，并开源 [qwen.cpp](https://github.com/QwenLM/qwen.cpp) 和 [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)。**Qwen-7B**和**Qwen-7B-Chat**的代码和模型也同步得到更新。**请使用最新的代码和模型！**
    - 相比原版Qwen-7B，新版用了更多训练数据（从2.2T增加到2.4T tokens），序列长度从2048扩展至8192。整体中文能力以及代码能力均有所提升。
* 2023年9月12日 支持Qwen-7B和Qwen-7B-Chat的微调，其中包括全参数微调、LoRA以及Q-LoRA。
* 2023年8月21日 发布Qwen-7B-Chat的Int4量化模型，Qwen-7B-Chat-Int4。该模型显存占用低，推理速度相比半精度模型显著提升，在基准评测上效果损失较小。
* 2023年8月3日 在魔搭社区（ModelScope）和Hugging Face同步推出Qwen-7B和Qwen-7B-Chat模型。同时，我们发布了技术备忘录，介绍了相关的训练细节和模型表现。
<br>

## 评测表现

Qwen系列模型相比同规模模型均实现了效果的显著提升。我们评测的数据集包括MMLU、C-Eval、 GSM8K、 MATH、HumanEval、MBPP、BBH等数据集，考察的能力包括自然语言理解、知识、数学计算和推理、代码生成、逻辑推理等。Qwen-72B在所有任务上均超越了LLaMA2-70B的性能，同时在10项任务中的7项任务中超越GPT-3.5.

<p align="left">
    <img src="assets/radar_72b.jpg" width="600"/>
<p>
<br>

| Model              |   MMLU   |  C-Eval  |  GSM8K   |   MATH   | HumanEval |   MBPP   |   BBH    |  CMMLU   |
|:-------------------|:--------:|:--------:|:--------:|:--------:|:---------:|:--------:|:--------:|:--------:|
|                    |  5-shot  |  5-shot  |  8-shot  |  4-shot  |  0-shot   |  3-shot  |  3-shot  |  5-shot  |
| LLaMA2-7B          |   46.8   |   32.5   |   16.7   |   3.3    |   12.8    |   20.8   |   38.2   |   31.8   |
| LLaMA2-13B         |   55.0   |   41.4   |   29.6   |   5.0    |   18.9    |   30.3   |   45.6   |   38.4   |
| LLaMA2-34B         |   62.6   |    -     |   42.2   |   6.2    |   22.6    |   33.0   |   44.1   |    -     |
| ChatGLM2-6B        |   47.9   |   51.7   |   32.4   |   6.5    |     -     |    -     |   33.7   |    -     |
| InternLM-7B        |   51.0   |   53.4   |   31.2   |   6.3    |   10.4    |   14.0   |   37.0   |   51.8   |
| InternLM-20B       |   62.1   |   58.8   |   52.6   |   7.9    |   25.6    |   35.6   |   52.5   |   59.0   |
| Baichuan2-7B       |   54.7   |   56.3   |   24.6   |   5.6    |   18.3    |   24.2   |   41.6   |   57.1   |
| Baichuan2-13B      |   59.5   |   59.0   |   52.8   |   10.1   |   17.1    |   30.2   |   49.0   |   62.0   |
| Yi-34B      	  	 |   76.3   |   81.8   |   67.9   |   15.9   |   26.2    |   38.2   |   66.4   |   82.6   |
| XVERSE-65B      	 |   70.8   |   68.6   |   60.3   |   -      |   26.3    |   -      |  -       |   -      |
| **Qwen-1.8B**      |   45.3   |   56.1   |   32.3   |   2.3    |   15.2    |   14.2   |   22.3   |   52.1   |
| **Qwen-7B**        |   58.2   |   63.5   |   51.7   |   11.6   |   29.9    |   31.6   |   45.0   |   62.2   |
| **Qwen-14B**       |   66.3   |   72.1   |   61.3   |   24.8   |   32.3    |   40.8   |   53.4   |   71.0   |
| **Qwen-72B**       | **77.4** | **83.3** | **78.9** | **35.2** | **35.4**  | **52.2** | **67.7** | **83.6** |


对于以上所有对比模型，我们列出了其官方汇报结果与[OpenCompass](https://opencompass.org.cn/leaderboard-llm)结果之间的最佳分数。

更多的实验结果和细节请查看我们的技术备忘录。点击[这里](https://qianwen-res.oss-cn-beijing.aliyuncs.com/QWEN_TECHNICAL_REPORT.pdf)。
<br><br>

## 要求

* python 3.8及以上版本
* pytorch 1.12及以上版本，推荐2.0及以上版本
* transformers 4.32及以上版本
* 建议使用CUDA 11.4及以上（GPU用户、flash-attention用户等需考虑此选项）
<br>

## 快速使用

我们提供简单的示例来说明如何利用🤖 ModelScope和🤗 Transformers快速使用Qwen-7B和Qwen-7B-Chat。

你可以使用我们预构建好的Docker镜像，省去大部分配置环境的操作，详情见[“使用预构建的docker镜像”](#-使用预构建的docker镜像)一节。

如不使用Docker，请确保你已经配置好环境并安装好相关的代码包。最重要的是，确保你满足上述要求，然后安装相关的依赖库。

```bash
pip install -r requirements.txt
```

如果你的显卡支持fp16或bf16精度，我们还推荐安装[flash-attention](https://github.com/Dao-AILab/flash-attention)（**当前已支持flash attention 2**）来提高你的运行效率以及降低显存占用。(**flash-attention只是可选项，不安装也可正常运行该项目**)

```bash
git clone https://github.com/Dao-AILab/flash-attention
cd flash-attention && pip install .
# 下方安装可选，安装可能比较缓慢。
# pip install csrc/layer_norm
# 如果flash-attn版本高于2.1.1，下方无需安装。
# pip install csrc/rotary
```

接下来你可以开始使用Transformers或者ModelScope来使用我们的模型。

### 🤗 Transformers

如希望使用Qwen-chat进行推理，所需要写的只是如下所示的数行代码。**请确保你使用的是最新代码，并指定正确的模型名称和路径，如`Qwen/Qwen-7B-Chat`和`Qwen/Qwen-14B-Chat`**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# 可选的模型包括: "Qwen/Qwen-7B-Chat", "Qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# 打开bf16精度，A100、H100、RTX3060、RTX3070等显卡建议启用以节省显存
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
# 打开fp16精度，V100、P100、T4等显卡建议启用以节省显存
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
# 使用CPU进行推理，需要约32GB内存
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
# 默认使用自动模式，根据设备自动选择精度
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True).eval()

# 可指定不同的生成长度、top_p等相关超参
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# 第一轮对话
response, history = model.chat(tokenizer, "你好", history=None)
print(response)
# 你好！很高兴为你提供帮助。

# 第二轮对话
response, history = model.chat(tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
# 这是一个关于一个年轻人奋斗创业最终取得成功的故事。
# 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。
# 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。
# 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。
# 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。
# 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。

# 第三轮对话
response, history = model.chat(tokenizer, "给这个故事起一个标题", history=history)
print(response)
# 《奋斗创业：一个年轻人的成功之路》
```

运行Qwen同样非常简单。

<details>
  <summary>运行Qwen</summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# 可选的模型包括: "Qwen/Qwen-7B", "Qwen/Qwen-14B"
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)

# 打开bf16精度，A100、H100、RTX3060、RTX3070等显卡建议启用以节省显存
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, bf16=True).eval()
# 打开fp16精度，V100、P100、T4等显卡建议启用以节省显存
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, fp16=True).eval()
# 使用CPU进行推理，需要约32GB内存
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="cpu", trust_remote_code=True).eval()
# 默认使用自动模式，根据设备自动选择精度
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True).eval()

# 可指定不同的生成长度、top_p等相关超参
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)

inputs = tokenizer('蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是', return_tensors='pt')
inputs = inputs.to(model.device)
pred = model.generate(**inputs)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))
# 蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是亚的斯亚贝巴（Addis Ababa）...
```

</details>

<p id="DownloadModel">
若在使用上述代码时由于各种原因无法从 HuggingFace 拉取模型和代码，可以先从 ModelScope 下载模型及代码至本地，再从本地加载模型：
</p>

```python
from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Downloading model checkpoint to a local dir model_dir
# model_dir = snapshot_download('qwen/Qwen-7B')
# model_dir = snapshot_download('qwen/Qwen-7B-Chat')
# model_dir = snapshot_download('qwen/Qwen-14B')
model_dir = snapshot_download('qwen/Qwen-14B-Chat')

# Loading local checkpoints
# trust_remote_code is still set as True since we still load codes from local dir instead of transformers
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True
).eval()
```

### 🤖 ModelScope

魔搭（ModelScope）是开源的模型即服务共享平台，为泛AI开发者提供灵活、易用、低成本的一站式模型服务产品。使用ModelScope同样非常简单，代码如下所示：

```python
from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

# 可选的模型包括: "qwen/Qwen-7B-Chat", "qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("qwen/Qwen-7B-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

response, history = model.chat(tokenizer, "你好", history=None)
print(response)
response, history = model.chat(tokenizer, "浙江的省会在哪里？", history=history) 
print(response)
response, history = model.chat(tokenizer, "它有什么好玩的景点", history=history)
print(response)
```

### Batch推理
千问支持batch批量推理。在开启flash-attention的状态下，使用batch推理可以约40%的提速。示例代码如下所示：
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GenerationConfig
from qwen_generation_utils import make_context, decode_tokens, get_stop_words_ids

tokenizer = AutoTokenizer.from_pretrained(
    './',
    pad_token='<|extra_0|>',
    eos_token='<|endoftext|>',
    padding_side='left',
    trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    './',
    pad_token_id=tokenizer.pad_token_id,
    device_map="auto",
    trust_remote_code=True
).eval()
model.generation_config = GenerationConfig.from_pretrained('./', pad_token_id=tokenizer.pad_token_id)

all_raw_text = ["我想听你说爱我。", "今天我想吃点啥，甜甜的，推荐下", "我马上迟到了，怎么做才能不迟到"]
batch_raw_text = []
for q in all_raw_text:
    raw_text, _ = make_context(
        tokenizer,
        q,
        system="You are a helpful assistant.",
        max_window_size=model.generation_config.max_window_size,
        chat_format=model.generation_config.chat_format,
    )
    batch_raw_text.append(raw_text)

batch_input_ids = tokenizer(batch_raw_text, padding='longest')
batch_input_ids = torch.LongTensor(batch_input_ids['input_ids']).to(model.device)
batch_out_ids = model.generate(
    batch_input_ids,
    return_dict_in_generate=False,
    generation_config=model.generation_config
)
padding_lens = [batch_input_ids[i].eq(tokenizer.pad_token_id).sum().item() for i in range(batch_input_ids.size(0))]

batch_response = [
    decode_tokens(
        batch_out_ids[i][padding_lens[i]:],
        tokenizer,
        raw_text_len=len(batch_raw_text[i]),
        context_length=(batch_input_ids[i].size(0)-padding_lens[i]),
        chat_format="chatml",
        verbose=False,
        errors='replace'
    ) for i in range(len(all_raw_text))
]
print(batch_response)

response, _ = model.chat(tokenizer, "我想听你说爱我。", history=None)
print(response)

response, _ = model.chat(tokenizer, "今天我想吃点啥，甜甜的，推荐下", history=None)
print(response)

response, _ = model.chat(tokenizer, "我马上迟到了，怎么做才能不迟到", history=None)
print(response)
```

### CPU

我们推荐你使用 [qwen.cpp](https://github.com/QwenLM/qwen.cpp) 来实现CPU部署和推理。qwen.cpp是Qwen和tiktoken的C++实现。你可以点击链接进入repo了解详情。

当然，直接在CPU上运行模型也是可以的，示例如下：

```python
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
```

但是，这样的推理效率大概率会非常低。

### 多GPU

如果你遇到显存不足的问题而希望使用多张GPU进行推理，可以使用上述的默认的使用方法读取模型。此前提供的脚本`utils.py`已停止维护。

尽管这个方法很简单，但它的效率相对较低。我们建议使用vLLM和FastChat并请阅读部署章节。

### x86 平台
在 酷睿™/至强® 可扩展处理器或 Arc™ GPU 上部署量化模型时，建议使用 [OpenVINO™ Toolkit](https://docs.openvino.ai/2023.3/gen_ai_guide.html) 以充分利用硬件，实现更好的推理性能。您可以安装并运行此[example notebook](https://github.com/openvinotoolkit/openvino_notebooks/tree/main/notebooks/254-llm-chatbot)。相关问题，您可在 [OpenVINO repo](https://github.com/openvinotoolkit/openvino_notebooks/issues)中提交。


### 阿里云灵积（DashScope）API服务
最简单的使用Qwen模型API服务的方法就是通过DashScope（阿里云灵积API模型服务）。我们提供了简单介绍说明使用方法。同时，我们还提供了自己部署OpenAI格式的API的方法。

DashScope是阿里云提供的大语言模型的API服务，目前支持Qwen。但请注意，目前提供服务的Qwen模型为内部模型，暂无更多具体细节对外透露。模型服务包括`qwen-turbo`、`qwen-plus`和`qwen-max`，`qwen-turbo`速度更快，`qwen-plus`效果更优，`qwen-max`是最新发布的千亿级通义千问2.0模型。详情请查看[文档](https://dashscope.aliyun.com)。

请首先前往[官网](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key?spm=a2c4g.11186623.0.0.6c2774fahtfXdn)开通DashScope，获得API Key（AK）。建议通过环境变量设置AK：
```bash
export DASHSCOPE_API_KEY="YOUR_DASHSCOPE_API_KEY"
```
随后安装相关代码包，点击[此处](https://help.aliyun.com/zh/dashscope/developer-reference/install-dashscope-sdk)查看安装文档。如使用python，则直接通过pip安装：
```bash
pip install dashscope
```
如安装JAVA SDK，则通过如下命令安装：
```xml
<!-- https://mvnrepository.com/artifact/com.alibaba/dashscope-sdk-java -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dashscope-sdk-java</artifactId>
    <version>the-latest-version</version>
</dependency>
```
最简单的使用方法就是通过messages调用，用法类似OpenAI API。示例如下：
```python
import random
from http import HTTPStatus
from dashscope import Generation


def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '如何做西红柿鸡蛋？'}]
    gen = Generation()
    response = gen.call(
        Generation.Models.qwen_turbo,
        messages=messages,
        seed=random.randint(1, 10000),  # set the random seed, optional, default to 1234 if not set
        result_format='message',  # set the result to be "message" format.
    )
    return response


if __name__ == '__main__':
    response = call_with_messages()
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
```
更多用法请查看官方文档了解详情。
<br><br>


## 量化

### GPTQ

我们提供了基于[AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ)的量化方案，并开源了Int4和Int8量化模型。量化模型的效果损失很小，但能显著降低显存占用并提升推理速度。

以下我们提供示例说明如何使用Int4量化模型。在开始使用前，请先保证满足要求（如torch 2.0及以上，transformers版本为4.32.0及以上，等等），并安装所需安装包：

```bash
pip install auto-gptq optimum
```

如安装`auto-gptq`遇到问题，我们建议您到官方[repo](https://github.com/PanQiWei/AutoGPTQ)搜索合适的wheel。

> 注意：预编译的`auto-gptq`版本对`torch`版本及其CUDA版本要求严格。同时，由于
> 其近期更新，你可能会遇到`transformers`、`optimum`或`peft`抛出的版本错误。
> 我们建议使用符合以下要求的最新版本：
> - torch==2.1 auto-gptq>=0.5.1 transformers>=4.35.0 optimum>=1.14.0 peft>=0.6.1
> - torch>=2.0,<2.1 auto-gptq<0.5.0 transformers<4.35.0 optimum<1.14.0 peft>=0.5.0,<0.6.0

随后即可使用和上述一致的用法调用量化模型：

```python
# 可选模型包括："Qwen/Qwen-7B-Chat-Int4", "Qwen/Qwen-14B-Chat-Int4"
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat-Int4",
    device_map="auto",
    trust_remote_code=True
).eval()
response, history = model.chat(tokenizer, "Hi", history=None)
```

我们对BF16，Int8和Int4模型在基准评测上做了测试，发现量化模型效果损失较小，结果如下所示：

| Quantization         | MMLU | CEval (val) | GSM8K | Humaneval |
|----------------------|:----:|:-----------:|:-----:|:---------:|
| Qwen-1.8B-Chat (BF16)| 43.3 |    55.6     | 33.7  |   26.2    |
| Qwen-1.8B-Chat (Int8)| 43.1 |    55.8     | 33.0  |   27.4    |
| Qwen-1.8B-Chat (Int4)| 42.9 |    52.8     | 31.2  |   25.0    |
| Qwen-7B-Chat (BF16)  | 55.8 |    59.7     | 50.3  |   37.2    |
| Qwen-7B-Chat (Int8)  | 55.4 |    59.4     | 48.3  |   34.8    |
| Qwen-7B-Chat (Int4)  | 55.1 |    59.2     | 49.7  |   29.9    |
| Qwen-14B-Chat (BF16) | 64.6 |    69.8     | 60.1  |   43.9    |
| Qwen-14B-Chat (Int8) | 63.6 |    68.6     | 60.0  |   48.2    |
| Qwen-14B-Chat (Int4) | 63.3 |    69.0     | 59.8  |   45.7    |
| Qwen-72B-Chat (BF16) | 74.4 |    80.1     | 76.4  |   64.6    |
| Qwen-72B-Chat (Int8) | 73.5 |    80.1     | 73.5  |   62.2    |
| Qwen-72B-Chat (Int4) | 73.4 |    80.1     | 75.3  |   61.6    |
<br>


### KV cache量化

> 注意：由于Hugging Face的内部实现，本功能的支持文件`cache_autogptq_cuda_256.cpp`与`cache_autogptq_cuda_kernel_256.cu`可能没被下载。如需开启使用，请手动从相关位置下载，并放置到相应文件中。

在模型推理时，我们可以将中间结果key以及value的值量化后压缩存储，这样便可以在相同的卡上存储更多的key以及value，增加样本吞吐。

我们在`config.json`里提供了`use_cache_quantization`和`use_cache_kernel`两个参数来控制是否启用KV cache量化，具体使用方法如下：
```python
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
     device_map="auto",
     trust_remote_code=True,
     use_cache_quantization=True,
     use_cache_kernel=True,
     use_flash_attn=False
)
```
注意：当前该功能不支持与flash attention同时开启，如果你开了KV cache量化的同时又开了flash attention（`use_flash_attn=True`， `use_cache_quantization=True`, `use_cache_kernel=True`），程序默认将关闭`use_flash_attn`。

效果方面，我们验证过Int8 KV Cache的使用对模型整体的精度指标基本无损。我们做了针对显存占用的性能测试。评测运行于单张A100-SXM4-80G GPU，模型默认使用BF16格式，默认生成1024个token，其中OOM表示内存不足。

开启了KV cache量化之后，模型在推理的时候可以开启更大的batch size (bs)。

| USE KV Cache |  bs=1  |  bs=4  | bs=16  | bs=32  | bs=64  | bs=100 |
|--------------|:------:|:------:|:------:|:------:|:------:|:------:|
| No           | 16.3GB | 24.1GB | 31.7GB | 48.7GB |  oom   |  oom   |
| Yes          | 15.5GB | 17.2GB | 22.3GB | 30.2GB | 48.2GB | 72.4GB |


开启了KV cache量化之后，模型在推理时可在生成更长的序列（sl，生成的token数）时，节约更多的显存。

| USE KV Cache | sl=512 | sl=1024 | sl=2048 | sl=4096 | sl=8192 |
|--------------|:------:|:-------:|:-------:|:-------:|:-------:|
| no           | 15.2GB | 16.3GB  | 17.6GB  | 19.5GB  | 23.2GB  |
| yes          |  15GB  | 15.5GB  | 15.8GB  | 16.6GB  | 17.6GB  |


开启KV cache量化后，模型在推理时会将原始存进`layer-past`的float格式的key/value转换成int8格式，同时存储量化部分的参数。

具体操作如下：

1. 将key/value进行量化操作
```
    qv,scale,zero_point=quantize_cache_v(v)
```
2. 存入`layer_past`中:

量化格式的`layer-past`:
```
    layer_past=((q_key,key_scale,key_zero_point),
                (q_value,value_scale,value_zero_point))
```
原始格式的`layer-past`:
```
    layer_past=(key,value)
```
如果需要将`layer-past`中存好的key，value直接取出使用，可以使用反量化操作将Int8格式的key/value转回float格式：
```
    v=dequantize_cache_torch(qv,scale,zero_point)
```
<br>

### 推理性能
这一部分将介绍模型推理的速度和显存占用的相关数据。下文的性能测算使用 [此脚本](https://qianwen-res.oss-cn-beijing.aliyuncs.com/profile.py) 完成。

我们测算了BF16、Int8和Int4模型在生成2048个token时的平均推理速度（tokens/s）和显存使用。结果如下所示：

<table>
    <tr>
        <td>Model Size</td>
        <td>Quantization</td>
        <td>Speed (Tokens/s)</td>
        <td>GPU Memory Usage</td>
    </tr>
    <tr>
        <td rowspan="3">1.8B</td>
        <td>BF16</td>
        <td>54.09</td>
        <td>4.23GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>55.56</td>
        <td>3.48GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>71.07</td>
        <td>2.91GB</td>
    </tr>
    <tr>
        <td rowspan="3">7B</td>
        <td>BF16</td>
        <td>40.93</td>
        <td>16.99GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>37.47</td>
        <td>11.20GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>50.09</td>
        <td>8.21GB</td>
    </tr>
    <tr>
        <td rowspan="3">14B</td>
        <td>BF16</td>
        <td>32.22</td>
        <td>30.15GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>29.28</td>
        <td>18.81GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>38.72</td>
        <td>13.01GB</td>
    </tr>
    <tr>
        <td rowspan="3">72B</td>
        <td>BF16</td>
        <td>8.48</td>
        <td>144.69GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>9.05</td>
        <td>81.27GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>11.32</td>
        <td>48.86GB</td>
    </tr>
    <tr>
        <td>72B + vLLM</td>
        <td>BF16</td>
        <td>17.60</td>
        <td>2xA100</td>
    </tr>
</table>

评测运行于单张A100-SXM4-80G GPU（除非提到使用2xA100），使用PyTorch 2.0.1、CUDA 11.8和Flash-Attention2。(72B + vLLM 使用 PyTorch 2.1.0和Cuda 11.8.)推理速度是生成2048个token的速度均值。

注意：以上Int4/Int8模型生成速度使用autogptq库给出，当前``AutoModelForCausalLM.from_pretrained``载入的模型生成速度会慢大约20%。我们已经将该问题汇报给HuggingFace团队，若有解决方案将即时更新。

我们还测量了不同上下文长度、生成长度、Flash-Attention版本的推理速度和 GPU 内存使用情况。可以在 Hugging Face 或 ModelScope 上的相应的模型介绍页面找到结果。

## 微调

### 使用方法
我们提供了`finetune.py`这个脚本供用户实现在自己的数据上进行微调的功能，以接入下游任务。此外，我们还提供了shell脚本减少用户的工作量。这个脚本支持 [DeepSpeed](https://github.com/microsoft/DeepSpeed) 和 [FSDP](https://engineering.fb.com/2021/07/15/open-source/fsdp/) 。我们提供的shell脚本使用了DeepSpeed，因此建议您确保已经安装DeepSpeed和Peft（注意：DeepSpeed可能不兼容最新的pydantic版本，请确保`pydantic<2.0`）。你可以使用如下命令安装：
```bash
pip install "peft<0.8.0" deepspeed
```

首先，你需要准备你的训练数据。你需要将所有样本放到一个列表中并存入json文件中。每个样本对应一个字典，包含id和conversation，其中后者为一个列表。示例如下所示：
```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "你好"
      },
      {
        "from": "assistant",
        "value": "我是一个语言模型，我叫通义千问。"
      }
    ]
  }
]
```

准备好数据后，你可以使用我们提供的shell脚本实现微调。注意，你需要在脚本中指定你的数据的路径。

微调脚本能够帮你实现：
- 全参数微调
- LoRA
- Q-LoRA

全参数微调在训练过程中更新所有参数。你可以运行这个脚本开始训练：

```bash
# 分布式训练。由于显存限制将导致单卡训练失败，我们不提供单卡训练脚本。
bash finetune/finetune_ds.sh
```

尤其注意，你需要在脚本中指定正确的模型名称或路径、数据路径、以及模型输出的文件夹路径。在这个脚本中我们使用了DeepSpeed ZeRO 3。如果你想修改这个配置，可以删除掉`--deepspeed`这个输入或者自行根据需求修改DeepSpeed配置json文件。此外，我们支持混合精度训练，因此你可以设置`--bf16 True`或者`--fp16 True`。在使用fp16时，请使用DeepSpeed支持混合精度训练。经验上，如果你的机器支持bf16，我们建议使用bf16，这样可以和我们的预训练和对齐训练保持一致，这也是为什么我们把默认配置设为它的原因。

运行LoRA的方法类似全参数微调。但在开始前，请确保已经安装`peft`代码库。另外，记住要设置正确的模型、数据和输出路径。我们建议你为模型路径使用绝对路径。这是因为LoRA仅存储adapter部分参数，而adapter配置json文件记录了预训练模型的路径，用于读取预训练模型权重。同样，你可以设置bf16或者fp16。

```bash
# 单卡训练
bash finetune/finetune_lora_single_gpu.sh
# 分布式训练
bash finetune/finetune_lora_ds.sh
```

与全参数微调不同，LoRA ([论文](https://arxiv.org/abs/2106.09685)) 只更新adapter层的参数而无需更新原有语言模型的参数。这种方法允许用户用更低的显存开销来训练模型，也意味着更小的计算开销。

注意，如果你使用预训练模型进行LoRA微调，而非chat模型，模型的embedding和输出层的参数将被设为可训练的参数。这是因为预训练模型没有学习过ChatML格式中的特殊token，因此需要将这部分参数设为可训练才能让模型学会理解和预测这些token。这也意味着，假如你的训练引入新的特殊token，你需要通过代码中的`modules_to_save`将这些参数设为可训练的参数。此外，这部分训练参数的引入会影响ZeRO 3的使用，因此我们默认推荐使用ZeRO 2。当然，如果你不需要引入这部分训练参数，你可以通过替换DeepSpeed的配置文件来使用ZeRO 3。如果你想节省显存占用，可以考虑使用chat模型进行LoRA微调，显存占用将大幅度降低。下文的显存占用和训练速度的记录将详细介绍这部分细节。

如果你依然遇到显存不足的问题，可以考虑使用Q-LoRA ([论文](https://arxiv.org/abs/2305.14314)) 。该方法使用4比特量化模型以及paged attention等技术实现更小的显存开销。

注意：如你使用单卡Q-LoRA，你可能需要安装`mpi4py`。你可以通过`pip`或者`conda`来安装。

运行Q-LoRA你只需运行如下脚本：

```bash
# 单卡训练
bash finetune/finetune_qlora_single_gpu.sh
# 分布式训练
bash finetune/finetune_qlora_ds.sh
```

我们建议你使用我们提供的Int4量化模型进行训练，即Qwen-7B-Chat-Int4。请**不要使用**非量化模型！与全参数微调以及LoRA不同，Q-LoRA仅支持fp16。注意，由于我们发现torch amp支持的fp16混合精度训练存在问题，因此当前的单卡训练Q-LoRA必须使用DeepSpeed。此外，上述LoRA关于特殊token的问题在Q-LoRA依然存在。并且，Int4模型的参数无法被设为可训练的参数。所幸的是，我们只提供了Chat模型的Int4模型，因此你不用担心这个问题。但是，如果你执意要在Q-LoRA中引入新的特殊token，很抱歉，我们无法保证你能成功训练。

> 注意：由于Hugging Face的内部实现，模型在保存时，一些非Python文件未保存（例如`*.cpp`与`*.cu`），如需要支持相关功能，请手动复制有关文件。

与全参数微调不同，LoRA和Q-LoRA的训练只需存储adapter部分的参数。假如你需要使用LoRA训练后的模型，你需要使用如下方法。假设你使用Qwen-7B训练模型，你可以用如下代码读取模型：

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()
```

> 注意: 如果`peft>=0.8.0`，加载模型同时会尝试加载tokenizer，但peft内部未相应设置`trust_remote_code=True`，导致`ValueError: Tokenizer class QWenTokenizer does not exist or is not currently imported.`要避过这一问题，你可以降级`peft<0.8.0`或将tokenizer相关文件移到其它文件夹。


如果你觉得这样一步到位的方式让你很不安心或者影响你接入下游应用，你可以选择先合并并存储模型（LoRA支持合并，Q-LoRA不支持），再用常规方式读取你的新模型，示例如下：

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()

merged_model = model.merge_and_unload()
# max_shard_size and safe serialization are not necessary. 
# They respectively work for sharding checkpoint and save the model to safetensors
merged_model.save_pretrained(new_model_directory, max_shard_size="2048MB", safe_serialization=True)
```

`new_model_directory`目录将包含合并后的模型参数与相关模型代码。请注意`*.cu`和`*.cpp`文件可能没被保存，请手动复制。另外，`merge_and_unload`仅保存模型，并未保存tokenizer，如有需要，请复制相关文件或使用以以下代码保存
```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(
    path_to_adapter, # path to the output directory
    trust_remote_code=True
)
tokenizer.save_pretrained(new_model_directory)
```


注意：分布式训练需要根据你的需求和机器指定正确的分布式训练超参数。此外，你需要根据你的数据、显存情况和训练速度预期，使用`--model_max_length`设定你的数据长度。

### 量化微调后模型

这一小节用于量化全参/LoRA微调后的模型。（注意：你不需要量化Q-LoRA模型因为它本身就是量化过的。）
如果你需要量化LoRA微调后的模型，请先根据上方说明去合并你的模型权重。

我们推荐使用[auto_gptq](https://github.com/PanQiWei/AutoGPTQ)去量化你的模型。

```bash
pip install auto-gptq optimum
```

注意: 当前AutoGPTQ有个bug，可以在该[issue](https://github.com/PanQiWei/AutoGPTQ/issues/370)查看。这里有个[修改PR](https://github.com/PanQiWei/AutoGPTQ/pull/495)，你可以使用该分支从代码进行安装。

首先，准备校准集。你可以重用微调你的数据，或者按照微调相同的方式准备其他数据。

第二步，运行以下命令：

```bash
python run_gptq.py \
    --model_name_or_path $YOUR_LORA_MODEL_PATH \
    --data_path $DATA \
    --out_path $OUTPUT_PATH \
    --bits 4 # 4 for int4; 8 for int8
```

这一步需要使用GPU，根据你的校准集大小和模型大小，可能会消耗数个小时。

接下来, 将原模型中所有 `*.py`, `*.cu`, `*.cpp` 文件和 `generation_config.json` 文件复制到输出模型目录下。同时，使用官方对应版本的量化模型的 `config.json` 文件覆盖输出模型目录下的文件
(例如, 如果你微调了 `Qwen-7B-Chat`和`--bits 4`, 那么你可以从 [Qwen-7B-Chat-Int4](https://huggingface.co/Qwen/Qwen-7B-Chat-Int4/blob/main/config.json) 仓库中找到对应的`config.json` )。
并且，你需要将 ``gptq.safetensors`` 重命名为 ``model.safetensors``。

最后，像官方量化模型一样测试你的模型。例如：

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

tokenizer = AutoTokenizer.from_pretrained("/path/to/your/model", trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    "/path/to/your/model",
    device_map="auto",
    trust_remote_code=True
).eval()

response, history = model.chat(tokenizer, "你好", history=None)
print(response)
```

### 多机微调

我们提供的脚本支持多机微调，可以参考[脚本](./finetune/finetune_lora_ds.sh)中的注释，在每个节点上正确设置相应的参数并启动训练脚本。关于多机分布式训练的更多信息，请参考[torchrun](https://pytorch.org/docs/stable/elastic/run.html)。

注意： DeepSpeed ZeRO 3 对节点间通信速率的要求远大于 ZeRO 2，在多机微调的情况下会大幅降低训练速度。因此，我们不建议在多机微调的情况下使用 DeepSpeed ZeRO 3 配置。

### 显存占用及训练速度

下面记录7B和14B模型在单GPU使用LoRA（LoRA (emb)指的是embedding和输出层参与训练，而LoRA则不优化这部分参数）和QLoRA时处理不同长度输入的显存占用和训练速度的情况。本次评测运行于单张A100-SXM4-80G GPU，使用CUDA 11.8和Pytorch 2.0，并使用了flash attention 2。我们统一使用batch size为1，gradient accumulation为8的训练配置，记录输入长度分别为256、512、1024、2048、4096和8192的显存占用（GB）和训练速度（s/iter）。我们还使用2张A100测了Qwen-7B的全参数微调。受限于显存大小，我们仅测试了256、512和1024token的性能。

对于 Qwen-7B，我们额外测试了多机微调的性能。我们在两台服务器上运行评测，每台服务器包含两张A100-SXM4-80G GPU，其余配置与Qwen-7B的其他评测相同。多机微调的结果在表中以 LoRA (multinode) 标示。

对于 Qwen-72B，我们测试了两种方案：1）使用4个 A100-SXM4-80G GPUs，通过 Lora + DeepSpeed ZeRO 3 微调和2）使用单张A100-SXM4-80G GPU，通过 QLora (int4) 微调。请注意，使用 LoRA (emb) 微调和不带 DeepSpeed ZeRO 3 的 LoRA 微调在4个A100-SXM4-80G GPUs 上都会出现OOM（你可以通过将`--deepspeed finetune/ds_config_zero3.json`参数传给[`finetune/finetune_lora_ds.sh`](finetune/finetune_lora_ds.sh)来打开 DeepSpeed ZeRO 3 配置）。

具体数值如下所示：


<table>
    <tr>
      <th rowspan="2">Model Size</th><th rowspan="2">Method</th><th rowspan="2">#Nodes</th><th rowspan="2">#GPUs per node</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">256</th><th align="center">512</th><th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th>
    </tr>
    <tr>
        <th rowspan="4">1.8B</th><td>LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">6.7G / 1.0s/it</td><td align="center">7.4G / 1.0s/it</td><td align="center">8.4G / 1.1s/it</td><td align="center">11.0G / 1.7s/it</td><td align="center">16.2G / 3.3s/it</td><td align="center">21.8G / 6.8s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td>
        <td>1</td><td>1</td>
        <td align="center">13.7G / 1.0s/it</td><td align="center">14.0G / 1.0s/it</td><td align="center">14.0G / 1.1s/it</td><td align="center">15.1G / 1.8s/it</td><td align="center">19.7G / 3.4s/it</td><td align="center">27.7G / 7.0s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">5.8G / 1.4s/it</td><td align="center">6.0G / 1.4s/it</td><td align="center">6.6G / 1.4s/it</td><td align="center">7.8G / 2.0s/it</td><td align="center">10.2G / 3.4s/it</td><td align="center">15.8G / 6.5s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td>
        <td>1</td><td>1</td>
        <td align="center">43.5G / 2.1s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.3s/it</td><td align="center">47.1G / 2.8s/it</td><td align="center">48.3G / 5.6s/it</td>
    </tr>
    <tr>
        <th rowspan="5">7B</th>
        <td>LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">20.1G / 1.2s/it</td><td align="center">20.4G / 1.5s/it</td><td align="center">21.5G / 2.8s/it</td><td align="center">23.8G / 5.2s/it</td><td align="center">29.7G / 10.1s/it</td><td align="center">36.6G / 21.3s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td>
        <td>1</td><td>1</td>
        <td align="center">33.7G / 1.4s/it</td><td align="center">34.1G / 1.6s/it</td><td align="center">35.2G / 2.9s/it</td><td align="center">35.1G / 5.3s/it</td><td align="center">39.2G / 10.3s/it</td><td align="center">48.5G / 21.7s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">11.5G / 3.0s/it</td><td align="center">11.5G / 3.0s/it</td><td align="center">12.3G / 3.5s/it</td><td align="center">13.9G / 7.0s/it</td><td align="center">16.9G / 11.6s/it</td><td align="center">23.5G / 22.3s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td>
<td>1</td><td>2</td>
<td align="center">139.2G / 4.0s/it</td><td align="center">148.0G / 4.0s/it</td><td align="center">162.0G / 4.5s/it</td><td align="center">-</td><td align="center">-</td><td align="center">-</td>
    </tr>
    <tr>
        <td>LoRA (multinode)</td>
        <td>2</td><td>2</td>
        <td align="center">74.7G / 2.09s/it</td><td align="center">77.6G / 3.16s/it</td><td align="center">84.9G / 5.17s/it</td><td align="center">95.1G / 9.25s/it</td><td align="center">121.1G / 18.1s/it</td><td align="center">155.5G / 37.4s/it</td>
    </tr>
    <tr>
        <th rowspan="3">14B</th>
        <td>LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">34.6G / 1.6s/it</td><td align="center">35.1G / 2.4s/it</td><td align="center">35.3G / 4.4s/it</td><td align="center">37.4G / 8.4s/it</td><td align="center">42.5G / 17.0s/it</td><td align="center">55.2G / 36.0s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td>
        <td>1</td><td>1</td>
        <td align="center">51.2 / 1.7s/it</td><td align="center">51.1G / 2.6s/it</td><td align="center">51.5G / 4.6s/it</td><td align="center">54.1G / 8.6s/it</td><td align="center">56.8G / 17.2s/it</td><td align="center">67.7G / 36.3s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">18.7G / 5.3s/it</td><td align="center">18.4G / 6.3s/it</td><td align="center">18.9G / 8.2s/it</td><td align="center">19.9G / 11.8s/it</td><td align="center">23.0G / 20.1s/it</td><td align="center">27.9G / 38.3s/it</td>
    </tr>
    <tr>
        <th rowspan="2">72B</th>
        <td>LoRA + Deepspeed Zero3</td>
        <td>1</td><td>4</td>
        <td align="center">215.4G / 17.6s/it</td><td align="center">217.7G / 20.5s/it</td><td align="center">222.6G / 29.4s/it</td><td align="center">228.8G / 45.7s/it</td><td align="center">249.0G / 83.4s/it</td><td align="center">289.2G / 161.5s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">61.4G / 27.4s/it</td><td align="center">61.4G / 31.5s/it</td><td align="center">62.9G / 41.4s/it</td><td align="center">64.1G / 59.5s/it</td><td align="center">68.0G / 97.7s/it</td><td align="center">75.6G / 179.8s/it</td>
    </tr>
</table>

<br>

## 部署

### vLLM
如希望部署及加速推理，我们建议你使用vLLM。

如果你使用**CUDA 12.1和PyTorch 2.1**，可以直接使用以下命令安装vLLM。

```bash
pip install vllm
```

否则请参考vLLM官方的[安装说明](https://docs.vllm.ai/en/latest/getting_started/installation.html)。

#### vLLM + 类Transformer接口

请下载[接口封装代码](examples/vllm_wrapper.py)到当前文件夹，并执行以下命令进行多轮对话交互。（注意：该方法当前只支持``model.chat()``接口。）

```python
from vllm_wrapper import vLLMWrapper

model = vLLMWrapper('Qwen/Qwen-7B-Chat', tensor_parallel_size=1)

response, history = model.chat(query="你好", history=None)
print(response)
response, history = model.chat(query="给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
response, history = model.chat(query="给这个故事起一个标题", history=history)
print(response)
```

#### vLLM + 网页Demo / 类OpenAI API

你可以使用FastChat去搭建一个网页Demo或类OpenAI API服务器。首先，请安装FastChat：

```bash
pip install "fschat[model_worker,webui]"
```

使用vLLM和FastChat运行Qwen之前，首先启动一个controller：
```bash
python -m fastchat.serve.controller
```

然后启动model worker读取模型。如使用单卡推理，运行如下命令：
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --dtype bfloat16
# python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --dtype float16 # 运行int4模型
```
然而，如果你希望使用多GPU加速推理或者增大显存，你可以使用vLLM支持的模型并行机制。假设你需要在4张GPU上运行你的模型，命令如下所示：
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4 --dtype bfloat16
# python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4 --dtype float16 # 运行int4模型
```

启动model worker后，你可以启动一个：

* Web UI Demo
```bash
python -m fastchat.serve.gradio_web_server
```

* OpenAI API

使用OpenAI API前，请阅读我们的API章节配置好环境，然后运行如下命令：
```bash
python -m fastchat.serve.openai_api_server --host localhost --port 8000
```

然而，如果你觉得使用vLLM和FastChat比较困难，你也可以尝试以下我们提供的最简单的方式部署Web Demo、CLI Demo和OpenAI API。
<br>


### Web UI

我们提供了Web UI的demo供用户使用 (感谢 @wysaid 支持)。在开始前，确保已经安装如下代码库：

```bash
pip install -r requirements_web_demo.txt
```

随后运行如下命令，并点击生成链接：

```bash
python web_demo.py
```

<p align="center">
    <br>
    <img src="assets/web_demo.gif" width="600" />
    <br>
<p>

### 交互式Demo

我们提供了一个简单的交互式Demo示例，请查看`cli_demo.py`。当前模型已经支持流式输出，用户可通过输入文字的方式和Qwen-7B-Chat交互，模型将流式输出返回结果。运行如下命令：

```bash
python cli_demo.py
```

<p align="center">
    <br>
    <img src="assets/cli_demo.gif" width="600" />
    <br>
<p>
<br>

### API

我们提供了OpenAI API格式的本地API部署方法（感谢@hanpenggit）。在开始之前先安装必要的代码库：

```bash
pip install fastapi uvicorn "openai<1.0" pydantic sse_starlette
```

随后即可运行以下命令部署你的本地API：

```bash
python openai_api.py
```

你也可以修改参数，比如`-c`来修改模型名称或路径, `--cpu-only`改为CPU部署等等。如果部署出现问题，更新上述代码库往往可以解决大多数问题。

使用API同样非常简单，示例如下：

```python
import openai
openai.api_base = "http://localhost:8000/v1"
openai.api_key = "none"

# 使用流式回复的请求
for chunk in openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=True
    # 流式输出的自定义stopwords功能尚未支持，正在开发中
):
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

# 不使用流式回复的请求
response = openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=False,
    stop=[] # 在此处添加自定义的stop words 例如ReAct prompting时需要增加： stop=["Observation:"]。
)
print(response.choices[0].message.content)
```

<p align="center">
    <br>
    <img src="assets/openai_api.gif" width="600" />
    <br>
<p>

该接口也支持函数调用（**Function Calling**），但暂时仅限 `stream=False` 时能生效。用法见[函数调用示例](examples/function_call_examples.py)。
<br><br>

## 🐳 使用预构建的Docker镜像

为简化部署流程，我们提供了预配置好相应环境的Docker镜像：[qwenllm/qwen](https://hub.docker.com/r/qwenllm/qwen)，只需安装驱动、下载模型文件即可启动Demo、部署OpenAI API以及进行微调。

### 准备操作

1. 根据需要使用的镜像版本，安装相应版本的Nvidia驱动：
  - `qwenllm/qwen:cu117`（**推荐**）：`>= 515.48.07`
  - `qwenllm/qwen:cu114`（不支持flash-attention）：`>= 470.82.01`
  - `qwenllm/qwen:cu121`：`>= 530.30.02`
  - `qwenllm/qwen:latest`：与`qwenllm/qwen:cu117`相同

2. 安装并配置[docker](https://docs.docker.com/engine/install/)和[nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)：

```bash
# 配置docker
sudo systemctl start docker
# 测试docker是否安装正确
sudo docker run hello-world

# 配置nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
# 测试nvidia-container-toolkit是否安装正确
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

3. 下载模型及代码至本地（参考[此处说明](#DownloadModel)）

### 部署

下面我们以Qwen-7B-Chat为例。在启动Web Demo或者部署API前，请先参照下方代码完成配置工作：

```bash
IMAGE_NAME=qwenllm/qwen:cu117
PORT=8901
CHECKPOINT_PATH=/path/to/Qwen-7B-Chat   # 下载到本地的模型及代码路径
```

如下脚本可以帮你部署:

* OpenAI API
```bash
bash docker/docker_openai_api.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* Web UI
```bash
bash docker/docker_web_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* 交互式Demo
```bash
bash docker/docker_cli_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH}
```

这些命令将自动下载所需镜像以及后台启动Web UI Demo。你可以打开`http://localhost:${PORT}` 来使用该Demo。

如果输出如下内容，则说明Demo启动成功：

```text
Successfully started web demo. Open '...' to try!
Run `docker logs ...` to check demo status.
Run `docker rm -f ...` to stop and remove the demo.
```

如果你想查看Demo的状态，你可以使用这个命令来展示输出结果：`docker logs qwen`。

你可以使用这个命令`docker rm -f qwen`来停止服务并删除容器。

### 微调

使用预配置好的Docker镜像进行微调的方法与[上一章](#微调)基本一致（我们已经在镜像中安装了相关依赖）：

以下是一个单卡LoRA微调的示例：
```bash
IMAGE_NAME=qwenllm/qwen:cu117
CHECKPOINT_PATH=/path/to/Qwen-7B                # 下载的模型和代码路径
#CHECKPOINT_PATH=/path/to/Qwen-7B-Chat-Int4     # 下载的模型和代码路径 (Q-LoRA)
DATA_PATH=/path/to/data/root                    # 准备微调数据放在 ${DATA_PATH}/example.json
OUTPUT_PATH=/path/to/output/checkpoint          # 微调输出路径

# 默认使用主机所有GPU
DEVICE=all
# 如果需要指定用于训练的GPU，按照以下方式设置device（注意：内层的引号不可省略）
#DEVICE='"device=0,1,2,3"'

mkdir -p ${OUTPUT_PATH}

# 单卡LoRA微调
docker run --gpus ${DEVICE} --rm --name qwen \
    --mount type=bind,source=${CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-7B \
    --mount type=bind,source=${DATA_PATH},target=/data/shared/Qwen/data \
    --mount type=bind,source=${OUTPUT_PATH},target=/data/shared/Qwen/output_qwen \
    --shm-size=2gb \
    -it ${IMAGE_NAME} \
    bash finetune/finetune_lora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B/ -d /data/shared/Qwen/data/example.json
```

如需修改为单卡Q-LoRA微调示例，只要修改`docker run`中的bash命令：
```bash
bash finetune/finetune_qlora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B-Chat-Int4/ -d /data/shared/Qwen/data/example.json
```
<br>

## 🔥 系统指令 (System Prompt)
Qwen-1.8-Chat 和 Qwen-72B-Chat 通义千问在多样且存在多轮复杂交互的系统指令上进行了充分训练，使模型可以跟随多样的系统指令，实现上下文(in-context)中的模型定制化，进一步提升了通义千问的可扩展性。

通过系统指令，Qwen-Chat能够实现**角色扮演**，**语言风格迁移**，**任务设定**，和**行为设定**等能力。

![](assets/system_prompt_language_style.png)

![](assets/system_prompt_role_play_en.png)

更多关于系统指令的介绍信息可以参考[示例文档](examples/system_prompt.md).


## 工具调用

Qwen-Chat针对工具使用、函数调用能力进行了优化。用户可以开发基于Qwen的Agent、LangChain应用、甚至Code Interpreter。

我们提供了文档说明如何根据ReAct Prompting的原理实现工具调用，请参见[ReAct示例](examples/react_prompt.md)。基于该原理，我们在 [openai_api.py](openai_api.py) 里提供了函数调用（Function Calling）的支持。
我们在已开源的中文[评测数据集](eval/EVALUATION.md)上测试模型的工具调用能力，并发现Qwen-Chat能够取得稳定的表现：

<table>
    <tr>
        <th colspan="4" align="center">中文工具调用评测基准（版本 20231206）</th>
    </tr>
    <tr>
        <th align="center">Model</th><th align="center">Tool Selection (Acc.↑)</th><th align="center">Tool Input (Rouge-L↑)</th><th align="center">False Positive Error↓</th>
    </tr>
    <tr>
        <td>GPT-4</td><td align="center">98.0%</td><td align="center">0.953</td><td align="center">23.9%</td>
    </tr>
    <tr>
        <td>GPT-3.5</td><td align="center">74.5%</td><td align="center">0.807</td><td align="center">80.6%</td>
    </tr>
    <tr>
        <td>Qwen-1_8B-Chat</td><td align="center">85.0%</td><td align="center">0.839</td><td align="center">27.6%</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td><td align="center">95.5%</td><td align="center">0.900</td><td align="center">11.6%</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td><td align="center">96.9%</td><td align="center">0.917</td><td align="center">5.6%</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td><td align="center">98.2%</td><td align="center">0.927</td><td align="center">1.1%</td>
    </tr>
</table>

为了考察Qwen使用Python Code Interpreter完成数学解题、数据可视化、及文件处理与爬虫等任务的能力，我们专门建设并开源了一个评测这方面能力的[评测基准](https://github.com/QwenLM/Qwen-Agent/tree/main/benchmark)。
我们发现Qwen在生成代码的可执行率、结果正确性上均表现较好：

<table>
    <tr>
        <th colspan="5" align="center">Code Interpreter Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th rowspan="2" align="center">Model</th>
        <th colspan="3" align="center">代码执行结果正确性 (%)</th>
        <th colspan="1" align="center">生成代码的可执行率 (%)</th>
    </tr>
    <tr>
        <th align="center">Math↑</th><th align="center">Visualization-Hard↑</th><th align="center">Visualization-Easy↑</th><th align="center">General↑</th>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td align="center">82.8</td>
        <td align="center">66.7</td>
        <td align="center">60.8</td>
        <td align="center">82.8</td>
    </tr>
    <tr>
        <td>GPT-3.5</td>
        <td align="center">47.3</td>
        <td align="center">33.3</td>
        <td align="center">55.7</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>LLaMA2-13B-Chat</td>
        <td align="center">8.3</td>
        <td align="center">1.2</td>
        <td align="center">15.2</td>
        <td align="center">48.3</td>
    </tr>
    <tr>
        <td>CodeLLaMA-13B-Instruct</td>
        <td align="center">28.2</td>
        <td align="center">15.5</td>
        <td align="center">21.5</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>InternLM-20B-Chat</td>
        <td align="center">34.6</td>
        <td align="center">10.7</td>
        <td align="center">25.1</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>ChatGLM3-6B</td>
        <td align="center">54.2</td>
        <td align="center">4.8</td>
        <td align="center">15.2</td>
        <td align="center">67.1</td>
    </tr>
    <tr>
        <td>Qwen-1.8B-Chat</td>
        <td align="center">25.6</td>
        <td align="center">21.4</td>
        <td align="center">22.8</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td>
        <td align="center">41.9</td>
        <td align="center">23.8</td>
        <td align="center">38.0</td>
        <td align="center">67.2</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td>
        <td align="center">58.4</td>
        <td align="center">31.0</td>
        <td align="center">45.6</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td>
        <td align="center">72.7</td>
        <td align="center">41.7</td>
        <td align="center">43.0</td>
        <td align="center">82.8</td>
    </tr>
</table>

<p align="center">
    <br>
    <img src="assets/code_interpreter_showcase_001.jpg" />
    <br>
<p>

<br>

## 长文本理解

我们引入了NTK插值、窗口注意力、LogN注意力缩放等技术来提升模型的上下文长度并突破训练序列长度的限制，原生长度为2K的Qwen-14B可以扩展到8K的序列长度，而原生长度8K的Qwen-1.8B/7B能够在32K长序列的设置下取得不错的表现。

对于Qwen-72B，我们基于RoPE采用更大的旋转Base来适应更长的上下文。Qwen-72B支持32K的上下文长度。

通过arXiv数据集上的语言模型实验，发现 Qwen 在长上下文场景下可以达到出色的性能。结果如下：

<table>
    <tr>
        <th rowspan="2">Model</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th><th align="center">16384</th><th align="center">32768</th>
    </tr>
     <tr>
        <td>Qwen-7B (original)</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">39.35</td><td align="center">469.81</td><td align="center">2645.09</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.59</td><td align="center">3.66</td><td align="center">5.71</td><td align="center">-</td>
    </tr>
    <tr>
            <td>Qwen-1.8B</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.13</b></td><td align="center"><b>3.89</b></td><td align="center">17.42</td><td align="center">433.85</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.14</b></td><td align="center"><b>3.93</b></td><td align="center"><b>3.82</b></td><td align="center"><b>3.83</b></td>
    </tr>
    <tr>
        <td>Qwen-7B</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.31</b></td><td align="center">7.27</td><td align="center">181.49</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.31</b></td><td align="center"><b>3.23</b></td><td align="center">3.33</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.33</b></td><td align="center"><b>3.22</b></td><td align="center"><b>3.17</b></td>
    </tr>
    <tr>
        <td>Qwen-14B</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center">22.79</td><td align="center">334.65</td><td align="center">3168.35</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center"><b>3.29</b></td><td align="center"><b>3.18</b></td><td align="center">3.42</td><td align="center">-</td>
    </tr>
    <tr>
        <td>Qwen-72B</td><td align="center"><b>-</b></td><td align="center"><b>-</b></td><td align="center">-</td><td align="center"><b>2.83</b></td><td align="center"><b>2.73</b></td><td align="center"><b>2.72</b></td>
    </tr>
</table>

进一步，我们为了验证Qwen-72B-Chat在长文本任务上的能力，在[L-Eval](https://arxiv.org/abs/2307.11088)客观题上进行了测试，评分结果如下：

| Model             | Input Length | Average   |  Coursera  |    GSM     |   QuALITY  |    TOEFL   |   CodeU    |  SFcition  |
|:------------------|:------------:|:---------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| ChatGPT-3.5-16k   |     16K      |   60.73   | **63.51**  | **84.00**  |   61.38    |    78.43   | **12.22**  |    64.84   |
| **Qwen-72B-Chat** |     32K      | **62.30** |   58.13    |   76.00    | **77.22**  |  **86.24** |    6.66    |  **69.53** |


我们进一步进行了“大海捞针”实验（想法来自于[@Greg Kamradt](https://twitter.com/GregKamradt/status/1727018183608193393)），测试模型在不同长度的输入下，是否能检索到文章不同位置的信息，结果如下：

![](assets/qwen_72b_needle_in_a_haystack.png)

以上结果说明，Qwen-72B-Chat可以能准确检索到32K以内的输入长度中放在各种位置的信息，证明了其具有优秀的长文本处理能力。

## Tokenizer

> 注：作为术语的“tokenizer”在中文中尚无共识的概念对应，本文档采用英文表达以利说明。

基于tiktoken的tokenizer有别于其他分词器，比如sentencepiece tokenizer。尤其在微调阶段，需要特别注意特殊token的使用。关于tokenizer的更多信息，以及微调时涉及的相关使用，请参阅[文档](tokenization_note_zh.md)。
<br><br>

## 复现

我们提供了评测脚本以供复现我们的实验结果。注意，由于内部代码和开源代码存在少许差异，评测结果可能与汇报结果存在细微的结果不一致。请阅读[eval/EVALUATION.md](eval/EVALUATION.md)了解更多信息。
<br><br>

## FAQ

如遇到问题，敬请查阅[FAQ](FAQ_zh.md)以及issue区，如仍无法解决再提交issue。
<br><br>

## 引用
如果你觉得我们的工作对你有帮助，欢迎引用！

```
@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
}
```
<br>

## 使用协议

<https://github.com/QwenLM/Qwen>中的源代码采用[Apache 2.0协议](./LICENSE)授权，您可在该仓库根目录找到协议全文。

研究人员与开发者可使用Qwen和Qwen-Chat或进行二次开发。对于商业使用，请查看模型各自的LICENSE。

- Qwen-72B、Qwen-14B和Qwen-7B采用[Tongyi Qianwen LICENSE AGREEMENT](./Tongyi%20Qianwen%20LICENSE%20AGREEMENT)授权，您可在相应模型的HuggingFace或ModelScope仓库找到协议原文。如需商用，您只需遵循使用协议进行商用即可，我们欢迎您填写问卷([72B](https://dashscope.console.aliyun.com/openModelApply/Qwen-72B-Chat)、[14B](https://dashscope.console.aliyun.com/openModelApply/Qwen-14B-Chat)、[7B](https://dashscope.console.aliyun.com/openModelApply/qianwen))。

- Qwen-1.8B采用[Tongyi Qianwen RESEARCH LICENSE AGREEMENT](./Tongyi%20Qianwen%20RESEARCH%20LICENSE%20AGREEMENT)授权，您可在相应模型的HuggingFace或ModelScope仓库找到协议原文。如需商用，请联系我们。

<br><br>

## 联系我们

如果你想给我们的研发团队和产品团队留言，欢迎加入我们的微信群和Discord server。当然也可以通过邮件（qianwen_opensource@alibabacloud.com）联系我们。

```

## File: `README_ES.md`
```markdown
<p align="left">
    <a href="README_CN.md">中文</a>&nbsp ｜ &nbsp<a href="README.md">English</a>&nbsp ｜ &nbsp<a href="README_JA.md">日本語</a> ｜ &nbsp<a href="README_FR.md">Français</a> ｜ &nbspEspañol
</p>
<br><br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/logo_qwen.jpg" width="400"/>
<p>
<br>

<p align="center">
        🤗 <a href="https://huggingface.co/Qwen">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/qwen">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2309.16609">Paper</a> &nbsp&nbsp ｜ &nbsp&nbsp🖥️ <a href="https://modelscope.cn/studios/qwen/Qwen-72B-Chat-Demo/summary">Demo</a>
<br>
<a href="assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp<a href="https://discord.gg/z3GAxXZ9Ce">Discord</a>&nbsp&nbsp ｜  &nbsp&nbsp<a href="https://dashscope.aliyun.com">API</a> 
</p>
<br><br>

> [!Important]
> ¡Qwen2 está aquí! Estás invitado a seguir [QwenLM/Qwen2](https://github.com/QwenLM/Qwen2) y compartir tu experiencia allí.
>
> Este repositorio ([QwenLM/Qwen](https://github.com/QwenLM/Qwen)) ya no se mantiene activamente, debido a diferencias sustanciales en la base de código.
<br>


|     |                                                              Qwen-Chat                                                               |                                                                Qwen-Chat (Int4)                                                                |                        Qwen-Chat (Int8)                         |                                                            Qwen                                                            |
|-----|:------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 1.8B  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B">🤗</a>  |
| 7B  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B">🤗</a>  |
| 14B | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B">🤗</a> |
| 72B | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B">🤗</a> |



Abrimos nuestra serie **Qwen**, que ahora incluye **Qwen**, los modelos de lenguaje, es decir **Qwen-7B** y **Qwen-14B**, así como **Qwen-Chat**, los modelos de chat, es decir **Qwen-7B-Chat** y **Qwen-14B-Chat**. Los enlaces se encuentran en la tabla anterior. Haz clic en ellos y comprueba las fichas de los modelos. Además, publicamos el **[informe técnico](https://arxiv.org/abs/2309.16609)**. Haz clic en el enlace y compruébalo.

En resumen, disponemos de modelos lingüísticos sólidos, que han sido preentrenados de forma estable para hasta 3 billones de tokens de datos multilingües con una amplia cobertura de dominios, idiomas (con especial atención al chino y al inglés), etc. Son capaces de lograr un rendimiento competitivo en conjuntos de datos de referencia. Además, disponemos de modelos de chat alineados con las preferencias humanas basados en SFT y RLHF (aún no publicados), que son capaces de chatear, crear contenidos, extraer información, resumir, traducir, codificar, resolver problemas matemáticos, etc., y son capaces de utilizar herramientas, jugar como agentes o incluso jugar como intérpretes de código, etc.

| Modelo    | Fecha de Publicación | Longitud Máx. | Mejora del Sistema de Avisos | # de Fichas Preentrenadas | Uso Mínimo de Memoria GPU de Finetuning (Q-Lora) | Uso Mínimo de la GPU para Generar 2048 Tokens (Int4) | Uso de Herramientas |
|:----------|:--------------------:|:-------------:|:----------------------------:|:-------------------------:|:------------------------------------------------:|:----------------------------------------------------:|:-------------------:|
| Qwen-1.8B |       23.11.30       |      32K      |              ✅               |           2.2T            |                      5.8GB                       |                        2.9GB                         |          ✅          |  
| Qwen-7B   |       23.08.03       |      32K      |              ❎               |           2.4T            |                      11.5GB                      |                        8.2GB                         |          ✅          |   
| Qwen-14B  |       23.09.25       |      8K       |              ❎               |           3.0T            |                      18.7GB                      |                        13.0GB                        |          ✅          |
| Qwen-72B  |       23.11.30       |      32K      |              ✅               |           3.0T            |                      61.4GB                      |                        48.9GB                        |          ✅          |   

En este repo, usted puede averiguar:

* Inicio rápido con Qwen, y disfrute de la simple inferencia.
* Detalles sobre los modelos de cuantificación, incluyendo GPTQ y cuantización de caché KV.
* Estadísticas de rendimiento de la inferencia, incluyendo velocidad y memoria.
* Tutoriales sobre ajuste fino, incluyendo ajuste de parámetros completos, LoRA y Q-LoRA.
* Instrucciones de despliegue, con el ejemplo de vLLM y FastChat.
* Instrucciones para construir demos, incluyendo WebUI, CLI demo, etc.
* Introducción al servicio API de DashScope, así como instrucciones para crear una API de estilo OpenAI para tu modelo.
* Información sobre Qwen para el uso de herramientas, agente e intérprete de código.
* Estadísticas de la evaluación de la comprensión del contexto largo
* Acuerdo de licencia
* ...

Además, si tienes problemas, consulta primero [FAQ](FAQ.md) para obtener ayuda. ¿Sigues teniendo problemas? No dudes en plantearnos tus problemas (mejor en inglés para que te entienda más gente). Si quieres ayudarnos, ¡envíanos pull requests sin dudarlo! ¡Siempre nos entusiasman los PR!

¿Quieres charlar con nosotros o quedar para tomar un café? ¡Bienvenido a nuestro Discord o WeChat!
<br><br>

## Noticias y Actualizaciones

* 2023.11.30 🔥 Lanzamos **Qwen-72B** y **Qwen-72B-Chat**, que están entrenados en tokens 3T y soportan 32k contextos, junto con **Qwen-1.8B**, y **Qwen-1.8B-Chat**, en ModelScope y Hugging Face. También hemos reforzado las capacidades de System Prompt de Qwen-72B-Chat y Qwen-1.8B-Chat, ver [documentación de ejemplo](examples/system_prompt.md). Adicionalmente, soporta la inferencia en **Ascend 910** y **Hygon DCU**. Consulta `ascend-support` y `dcu-support` para más detalles.
* 2023.10.17 Publicamos el modelo cuantizado Int8 **Qwen-7B-Chat-Int8** y **Qwen-14B-Chat-Int8**.
* 2023.9.25 Publicamos **Qwen-14B** y **Qwen-14B-Chat** en ModelScope y Hugging Face, junto con [qwen.cpp](https://github.com/QwenLM/qwen.cpp) y [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent). También se actualizan los códigos y pesos de **Qwen-7B** y **Qwen-7B-Chat**. **POR FAVOR, DESCARGA LA ÚLTIMA VERSIÓN!**
    - En comparación con **Qwen-7B** (original), **Qwen-7B** utiliza más tokens de entrenamiento, pasando de 2,2T tokens a 2,4T tokens, mientras que la longitud del contexto se amplía de 2048 a 8192. El conocimiento del chino y la capacidad de codificación de **Qwen-7B** se han mejorado aún más.
* 2023.9.12 Ahora es posible el ajuste fino de los modelos Qwen-7B, incluido el ajuste fino de parámetros completos, LoRA y Q-LoRA.
* 2023.8.21 Publicamos el modelo cuantizado Int4 para Qwen-7B-Chat, **Qwen-7B-Chat-Int4**, que requiere bajos costes de memoria pero consigue mejorar la velocidad de inferencia. Además, no se produce una degradación significativa del rendimiento en la evaluación comparativa.
* 2023.8.3 Publicamos **Qwen-7B** y **Qwen-7B-Chat** en ModelScope y Hugging Face. También proporcionamos una nota técnica para más detalles sobre el modelo, incluidos los detalles de entrenamiento y el rendimiento del modelo.
<br>

## Rendimiento

Los modelos Qwen superan a los modelos de referencia de tamaños de modelo similares en una serie de conjuntos de datos de referencia, como MMLU, C-Eval, GSM8K, MATH, HumanEval, MBPP, BBH, etc., que evalúan las capacidades de los modelos en comprensión del lenguaje natural, resolución de problemas matemáticos, codificación, etc. Qwen-72B obtiene mejores resultados que LLaMA2-70B en todas las tareas y supera a GPT-3.5 en 7 de cada 10 tareas.

<p align="left">
    <img src="assets/radar_72b.jpg" width=600px/>
<p>
<br>

| Model             |   MMLU   |  C-Eval  |  GSM8K   |   MATH   | HumanEval |   MBPP   |   BBH    |  CMMLU   |
|:------------------|:--------:|:--------:|:--------:|:--------:|:---------:|:--------:|:--------:|:--------:|
|                   |  5-shot  |  5-shot  |  8-shot  |  4-shot  |  0-shot   |  3-shot  |  3-shot  |  5-shot  |
| LLaMA2-7B         |   46.8   |   32.5   |   16.7   |   3.3    |   12.8    |   20.8   |   38.2   |   31.8   |
| LLaMA2-13B        |   55.0   |   41.4   |   29.6   |   5.0    |   18.9    |   30.3   |   45.6   |   38.4   |
| LLaMA2-34B        |   62.6   |    -     |   42.2   |   6.2    |   22.6    |   33.0   |   44.1   |    -     |
| ChatGLM2-6B       |   47.9   |   51.7   |   32.4   |   6.5    |     -     |    -     |   33.7   |    -     |
| InternLM-7B       |   51.0   |   53.4   |   31.2   |   6.3    |   10.4    |   14.0   |   37.0   |   51.8   |
| InternLM-20B      |   62.1   |   58.8   |   52.6   |   7.9    |   25.6    |   35.6   |   52.5   |   59.0   |
| Baichuan2-7B      |   54.7   |   56.3   |   24.6   |   5.6    |   18.3    |   24.2   |   41.6   |   57.1   |
| Baichuan2-13B     |   59.5   |   59.0   |   52.8   |   10.1   |   17.1    |   30.2   |   49.0   |   62.0   |
| Yi-34B      	  	  |   76.3   |   81.8   |   67.9   |   15.9   |   26.2    |   38.2   |   66.4   |   82.6   |
| XVERSE-65B      	 |   70.8   |   68.6   |   60.3   |    -     |   26.3    |    -     |    -     |    -     |
| **Qwen-1.8B**     |   45.3   |   56.1   |   32.3   |   2.3    |   15.2    |   14.2   |   22.3   |   52.1   |
| **Qwen-7B**       |   58.2   |   63.5   |   51.7   |   11.6   |   29.9    |   31.6   |   45.0   |   62.2   |
| **Qwen-14B**      |   66.3   |   72.1   |   61.3   |   24.8   |   32.3    |   40.8   |   53.4   |   71.0   |
| **Qwen-72B**      | **77.4** | **83.3** | **78.9** | **35.2** | **35.4**  | **52.2** | **67.7** | **83.6** |

Para todos los modelos comparados, presentamos las mejores puntuaciones entre sus resultados oficiales y [OpenCompass](https://opencompass.org.cn/leaderboard-llm).

Para más resultados experimentales (rendimiento detallado del modelo en más conjuntos de datos de referencia) y detalles, consulte nuestro informe técnico haciendo clic [aquí](https://qianwen-res.oss-cn-beijing.aliyuncs.com/QWEN_TECHNICAL_REPORT.pdf).
<br><br>

## Requisitos

* python 3.8 y superior
* pytorch 1.12 y superior, se recomienda 2.0 y superior
* transformers 4.32 y superiores
* Se recomienda CUDA 11.4 y superior (esto es para usuarios de GPU, usuarios de flash-attention, etc.)
<br>

## Inicio rápido

A continuación, proporcionamos ejemplos sencillos para mostrar cómo utilizar Qwen-Chat con 🤖 ModelScope y 🤗 Transformers.

Puedes usar nuestras imágenes docker pre-construidas para saltarte la mayoría de los pasos de configuración del entorno, mira la Sección ["Usando Imágenes Docker Pre-construidas"](#-docker) para más detalles. 

Si no utiliza Docker, asegúrese de haber configurado el entorno e instalado los paquetes necesarios. Asegúrese de que cumple los requisitos anteriores y, a continuación, instale las bibliotecas dependientes.

```bash
pip install -r requirements.txt
```

Si tu dispositivo soporta fp16 o bf16, te recomendamos instalar [flash-attention](https://github.com/Dao-AILab/flash-attention) (**ahora soportamos flash attention 2.**) para una mayor eficiencia y un menor uso de memoria. (**flash-attention es opcional y el proyecto puede ejecutarse normalmente sin instalarlo**)

```bash
git clone https://github.com/Dao-AILab/flash-attention
cd flash-attention && pip install .
# Below are optional. Installing them might be slow.
# pip install csrc/layer_norm
# pip install csrc/rotary
```

Ahora puedes empezar con ModelScope o Transformers.

### 🤗 Transformers

Para utilizar Qwen-Chat para la inferencia, todo lo que tienes que hacer es introducir unas pocas líneas de código como se demuestra a continuación. Recuerda introducir los nombres o rutas correctos de los modelos, como "Qwen/Qwen-7B-Chat" y "Qwen/Qwen-14B-Chat". Sin embargo, **por favor, asegúrese de que está utilizando el código más reciente.**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names: "Qwen/Qwen-7B-Chat", "Qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# use bf16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
# use auto mode, automatically select precision based on the device.
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
    device_map="auto",
    trust_remote_code=True
).eval()

# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# 1st dialogue turn
response, history = model.chat(tokenizer, "你好", history=None)
print(response)
# 你好！很高兴为你提供帮助。

# 2nd dialogue turn
response, history = model.chat(tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
# 这是一个关于一个年轻人奋斗创业最终取得成功的故事。
# 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。
# 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。
# 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。
# 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。
# 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。

# 3rd dialogue turn
response, history = model.chat(tokenizer, "给这个故事起一个标题", history=history)
print(response)
# 《奋斗创业：一个年轻人的成功之路》
```

Ejecutar Qwen, el modelo lingüístico base, también es sencillo.

<details>
  <summary>Ejecutar Qwen</summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names: "Qwen/Qwen-7B", "Qwen/Qwen-14B" 
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)
# use bf16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="cpu", trust_remote_code=True).eval()
# use auto mode, automatically select precision based on the device.
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B",
    device_map="auto",
    trust_remote_code=True
).eval()

# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)

inputs = tokenizer('蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是', return_tensors='pt')
inputs = inputs.to(model.device)
pred = model.generate(**inputs)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))
# 蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是亚的斯亚贝巴（Addis Ababa）...
```

</details>

En caso de que se produzca un problema de red al intentar descargar puntos de control y códigos de modelos desde Hugging Face, un método alternativo consiste en obtener inicialmente el punto de control desde ModelScope y luego cargarlo desde el directorio local como se indica a continuación:

```python
from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Downloading model checkpoint to a local dir model_dir
# model_dir = snapshot_download('qwen/Qwen-7B', revision='v1.1.4')
# model_dir = snapshot_download('qwen/Qwen-7B-Chat', revision='v1.1.4')
# model_dir = snapshot_download('qwen/Qwen-14B', revision='v1.0.4')
model_dir = snapshot_download('qwen/Qwen-14B-Chat', revision='v1.0.4')

# Loading local checkpoints
# trust_remote_code is still set as True since we still load codes from local dir instead of transformers
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True
).eval()
```

### 🤖 ModelScope

ModelScope es una plataforma de código abierto para Model-as-a-Service (MaaS), que proporciona un servicio de modelos flexible y rentable a los desarrolladores de IA. Del mismo modo, puede ejecutar los modelos con ModelScope como se muestra a continuación:

```python
from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

# Model names: "qwen/Qwen-7B-Chat", "qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("qwen/Qwen-7B-Chat", revision='v1.0.5', trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("qwen/Qwen-7B-Chat", revision='v1.0.5', device_map="auto", trust_remote_code=True, fp16=True).eval()
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", revision='v1.0.5', trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

response, history = model.chat(tokenizer, "你好", history=None)
print(response)
response, history = model.chat(tokenizer, "浙江的省会在哪里？", history=history) 
print(response)
response, history = model.chat(tokenizer, "它有什么好玩的景点", history=history)
print(response)
```

### Inferencia por lotes
Qwen admite la inferencia por lotes. Con la atención flash activada, el uso de la inferencia por lotes puede suponer un aumento de velocidad del 40%. El código de ejemplo se muestra a continuación:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GenerationConfig
from qwen_generation_utils import make_context, decode_tokens, get_stop_words_ids

tokenizer = AutoTokenizer.from_pretrained(
    './',
    pad_token='<|extra_0|>',
    eos_token='<|endoftext|>',
    padding_side='left',
    trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    './',
    pad_token_id=tokenizer.pad_token_id,
    device_map="auto",
    trust_remote_code=True
).eval()
model.generation_config = GenerationConfig.from_pretrained('./', pad_token_id=tokenizer.pad_token_id)

all_raw_text = ["我想听你说爱我。", "今天我想吃点啥，甜甜的，推荐下", "我马上迟到了，怎么做才能不迟到"]
batch_raw_text = []
for q in all_raw_text:
    raw_text, _ = make_context(
        tokenizer,
        q,
        system="You are a helpful assistant.",
        max_window_size=model.generation_config.max_window_size,
        chat_format=model.generation_config.chat_format,
    )
    batch_raw_text.append(raw_text)

batch_input_ids = tokenizer(batch_raw_text, padding='longest')
batch_input_ids = torch.LongTensor(batch_input_ids['input_ids']).to(model.device)
batch_out_ids = model.generate(
    batch_input_ids,
    return_dict_in_generate=False,
    generation_config=model.generation_config
)
padding_lens = [batch_input_ids[i].eq(tokenizer.pad_token_id).sum().item() for i in range(batch_input_ids.size(0))]

batch_response = [
    decode_tokens(
        batch_out_ids[i][padding_lens[i]:],
        tokenizer,
        raw_text_len=len(batch_raw_text[i]),
        context_length=(batch_input_ids[i].size(0)-padding_lens[i]),
        chat_format="chatml",
        verbose=False,
        errors='replace'
    ) for i in range(len(all_raw_text))
]
print(batch_response)

response, _ = model.chat(tokenizer, "我想听你说爱我。", history=None)
print(response)

response, _ = model.chat(tokenizer, "今天我想吃点啥，甜甜的，推荐下", history=None)
print(response)

response, _ = model.chat(tokenizer, "我马上迟到了，怎么做才能不迟到", history=None)
print(response)
```

### CPU

Para desplegar nuestros modelos en la CPU, le recomendamos encarecidamente que utilice [qwen.cpp](https://github.com/QwenLM/qwen.cpp), que es una implementación C++ pura de Qwen y tiktoken. Comprueba el repositorio para más detalles.

Además, también es sencillo ejecutar directamente el modelo en la CPU, lo que requiere que especifiques el dispositivo:

```python
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
```

Pero es probable que sufra una eficacia de inferencia extremadamente baja.

### Múltiples GPU

Si sufres de falta de memoria en la GPU y quieres ejecutar el modelo en más de 1 GPU, puedes utilizar directamente el método de carga por defecto, que ahora es soportado por Transformers. El método anterior basado en `utils.py` está obsoleto.

Sin embargo, aunque este método es sencillo, la eficiencia del paralelismo del pipeline nativo es baja. Le aconsejamos que utilice vLLM con FastChat y por favor lea la sección para el despliegue.

### DashScope

La forma más sencilla de utilizar Qwen a través de APIs es el servicio DashScope API a través de Alibaba Cloud. Damos una introducción al uso. Además, proporcionamos un script para que despliegues una API estilo OpenAI en tus propios servidores.

DashScope es el gran servicio de API de modelos lingüísticos proporcionado por Alibaba Cloud, que ahora es compatible con Qwen. Tenga en cuenta que los modelos detrás de DashScope son versiones internas temporalmente sin detalles proporcionados. Los servicios incluyen `qwen-turbo` y `qwen-plus`, donde el primero se ejecuta más rápido y el segundo consigue un mejor rendimiento. Para más información, visita la documentación [aquí](https://dashscope.aliyun.com).

Dirígete al sitio web oficial [enlace](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key?spm=a2c4g.11186623.0.0.6c2774fahtfXdn) para crear una cuenta DashScope y obtener la clave API (AK). Recomendamos configurar la AK con una variable de entorno:
```bash
export DASHSCOPE_API_KEY="YOUR_DASHSCOPE_API_KEY"
```
A continuación, instala los paquetes y haz clic [aquí](https://help.aliyun.com/zh/dashscope/developer-reference/install-dashscope-sdk) para consultar la documentación. Si utilizas Python, puedes instalar DashScope con pip:
```bash
pip install dashscope
```
Si utiliza JAVA SDK, puede instalarlo de esta forma:
```xml
<!-- https://mvnrepository.com/artifact/com.alibaba/dashscope-sdk-java -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dashscope-sdk-java</artifactId>
    <version>the-latest-version</version>
</dependency>
```
La forma más sencilla de utilizar DashScope es el uso con mensajes, que es similar a la API OpenAI. El ejemplo se muestra a continuación:
```python
import random
from http import HTTPStatus
from dashscope import Generation


def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '如何做西红柿鸡蛋？'}]
    gen = Generation()
    response = gen.call(
        Generation.Models.qwen_turbo,
        messages=messages,
        seed=random.randint(1, 10000),  # set the random seed, optional, default to 1234 if not set
        result_format='message',  # set the result to be "message" format.
    )
    return response


if __name__ == '__main__':
    response = call_with_messages()
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
```
Para más usos, visite el sitio web oficial.
<br><br>

## Cuantización

### GPTQ

Proporcionamos una solución basada en [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ), y liberamos los modelos cuantificados Int4 e Int8, que consiguen efectos de modelo casi sin pérdidas pero un rendimiento mejorado tanto en costes de memoria como en velocidad de inferencia.

Aquí demostramos cómo utilizar los modelos cuantizados que proporcionamos para la inferencia. Antes de empezar, asegúrese de que cumple los requisitos de auto-gptq (por ejemplo, torch 2.0 y superior, transformers 4.32.0 y superior, etc.) e instale los paquetes necesarios:

```bash
pip install auto-gptq optimum
```

Si tiene problemas para instalar `auto-gptq`, le aconsejamos que consulte el [repo] oficial (https://github.com/PanQiWei/AutoGPTQ) para encontrar una rueda.

> Nota: Los paquetes `auto-gptq` precompilados dependen en gran medida de la versión de `torch` y de su versión CUDA. Además, debido a la reciente actualización 
> también puede encontrar errores de versión no soportada de `transformers`, `optimum`, o `peft`.
> Recomendamos utilizar las últimas versiones que cumplan los siguientes requisitos:
> - torch==2.1 auto-gptq>=0.5.1 transformers>=4.35.0 optimum>=1.14.0 peft>=0.6.1
> - antorcha>=2.0,<2.1 auto-gptq<0.5.0 transformadores<4.35.0 óptimo<1.14.0 peft>=0.5.0,<0.6.0

A continuación, puede cargar el modelo cuantizado fácilmente y ejecutar la inferencia como de costumbre:

```python
# Model names: "Qwen/Qwen-7B-Chat-Int4", "Qwen/Qwen-14B-Chat-Int4"
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat-Int4",
    device_map="auto",
    trust_remote_code=True
).eval()
response, history = model.chat(tokenizer, "Hi", history=None)
```

Ilustramos el rendimiento de los modelos BF16, Int8 e Int4 en la prueba de referencia, y observamos que el modelo cuantizado no sufre una degradación significativa del rendimiento. Los resultados se muestran a continuación:

| Quantization         | MMLU | CEval (val) | GSM8K | Humaneval |
|----------------------|:----:|:-----------:|:-----:|:---------:|
| Qwen-1.8B-Chat (BF16)| 43.3 |    55.6     | 33.7  |   26.2    |
| Qwen-1.8B-Chat (Int8)| 43.1 |    55.8     | 33.0  |   27.4    |
| Qwen-1.8B-Chat (Int4)| 42.9 |    52.8     | 31.2  |   25.0    |
| Qwen-7B-Chat (BF16)  | 55.8 |    59.7     | 50.3  |   37.2    |
| Qwen-7B-Chat (Int8)  | 55.4 |    59.4     | 48.3  |   34.8    |
| Qwen-7B-Chat (Int4)  | 55.1 |    59.2     | 49.7  |   29.9    |
| Qwen-14B-Chat (BF16) | 64.6 |    69.8     | 60.1  |   43.9    |
| Qwen-14B-Chat (Int8) | 63.6 |    68.6     | 60.0  |   48.2    |
| Qwen-14B-Chat (Int4) | 63.3 |    69.0     | 59.8  |   45.7    |
| Qwen-72B-Chat (BF16) | 74.4 |    80.1     | 76.4  |   64.6    |
| Qwen-72B-Chat (Int8) | 73.5 |    80.1     | 73.5  |   62.2    |
| Qwen-72B-Chat (Int4) | 73.4 |    80.1     | 75.3  |   61.6    |

### Cuantización de la caché KV

> NOTA: Por favor, ten en cuenta que debido al mecanismo interno de Hugging Face, los archivos de soporte para esta funcionalidad
> (es decir, `cache_autogptq_cuda_256.cpp` y `cache_autogptq_cuda_kernel_256.cu`). 
> Por favor, descárguelos manualmente del Hugging Face Hub y colóquelos en la misma carpeta que los demás archivos del módulo.

La caché KV de atención puede cuantificarse y comprimirse para su almacenamiento, con el fin de obtener un mayor rendimiento de la muestra. Los argumentos `use_cache_quantization` y `use_cache_kernel` en `config.json` se proporcionan para habilitar la cuantización de la caché KV. 
El método de uso específico es el siguiente:

```python
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
     device_map="auto",
     trust_remote_code=True,
     use_cache_quantization=True,
     use_cache_kernel=True,
     use_flash_attn=False
)
```
Atención: Actualmente, la cuantización de caché KV y flash attention no se pueden utilizar al mismo tiempo.
Si habilita la cuantización de caché KV y flash attention al mismo tiempo (`use_flash_attn=True`, `use_cache_quantization=True`, `use_cache_kernel=True`), `use_flash_attn` está deshabilitado por defecto (`use_flash_attn=false`).

Hemos comprobado que el uso del modelo int8-kvcache cuantizado no sufre una degradación significativa del rendimiento en la evaluación posterior. A continuación, nos centraremos en el análisis de su huella de memoria en diferentes condiciones. 
El perfil se ejecuta en una única GPU A100-SXM4-80G con PyTorch 2.0.1 y CUDA 11.4. 
Utilizamos modelos BF16 para generar 1024 tokens por defecto, y "OOM" indica error de memoria insuficiente.

Con la cuantización de la caché KV, el modelo puede inferir con un tamaño de lote (bs) mayor.

| Utilizar la caché KV |  bs=1  |  bs=4  | bs=16  | bs=32  | bs=64  | bs=100 |
|----------------------|:------:|:------:|:------:|:------:|:------:|:------:|
| No                   | 16.3GB | 24.1GB | 31.7GB | 48.7GB |  OOM   |  OOM   |
| Yes                  | 15.5GB | 17.2GB | 22.3GB | 30.2GB | 48.2GB | 72.4GB |

Con la cuantización kv-cache activada, el modelo puede ahorrar más memoria cuando genera seq-length más largos (sl, número de tokens generados) en infer.

| Utilizar la caché KV | sl=512 | sl=1024 | sl=2048 | sl=4096 | sl=8192 |
|----------------------|:------:|:-------:|:-------:|:-------:|:-------:|
| No                   | 15.2GB | 16.3GB  | 17.6GB  | 19.5GB  | 23.2GB  |
| Yes                  |  15GB  | 15.5GB  | 15.8GB  | 16.6GB  | 17.6GB  |

El modelo con cuantificación de caché KV convertirá el formato de `layer_past` de float a int8, y mientras tanto el `layer-past` cuantificado también almacenará los parámetros de cuantificación.

Los pasos específicos son los siguientes

1. Cuantificar clave/valor
```
    qv,scale,zero_point=quantize_cache_v(v)
```
2. Almacenar en layer_past

A continuación se muestra el formato de `layer_past` cuantificado:
```
    layer_past=((q_key,key_scale,key_zero_point),
                (q_value,value_scale,value_zero_point))
```
A continuación se muestra el formato original de `layer_past`:
```
    layer_past=(key,value)
```
Si desea utilizar la atención KV que se cuantiza, 
puede utilizar la operación de decuantización para convertir la clave/valor int8 de nuevo al formato float de la siguiente manera:
```
    v=dequantize_cache_torch(qv,scale,zero_point)
```
<br>


## Rendimiento de Inferencia

Esta sección proporciona las estadísticas de velocidad y memoria de los modelos en diferentes precisiones. Los perfiles de velocidad y memoria se realizan utilizando [este script](https://qianwen-res.oss-cn-beijing.aliyuncs.com/profile.py).

Medimos la velocidad media de inferencia (tokens/s) y el uso de memoria de la GPU al generar 2048 con los modelos en BF16, Int8 e Int4.

<table>
    <tr>
        <td>Model Size</td>
        <td>Quantization</td>
        <td>Speed (Tokens/s)</td>
        <td>GPU Memory Usage</td>
    </tr>
    <tr>
        <td rowspan="3">1.8B</td>
        <td>BF16</td>
        <td>54.09</td>
        <td>4.23GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>55.56</td>
        <td>3.48GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>71.07</td>
        <td>2.91GB</td>
    </tr>
    <tr>
        <td rowspan="3">7B</td>
        <td>BF16</td>
        <td>40.93</td>
        <td>16.99GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>37.47</td>
        <td>11.20GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>50.09</td>
        <td>8.21GB</td>
    </tr>
    <tr>
        <td rowspan="3">14B</td>
        <td>BF16</td>
        <td>32.22</td>
        <td>30.15GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>29.28</td>
        <td>18.81GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>38.72</td>
        <td>13.01GB</td>
    </tr>
    <tr>
        <td rowspan="3">72B</td>
        <td>BF16</td>
        <td>8.48</td>
        <td>144.69GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>9.05</td>
        <td>81.27GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>11.32</td>
        <td>48.86GB</td>
    </tr>
    <tr>
        <td>72B + vLLM</td>
        <td>BF16</td>
        <td>17.60</td>
        <td>2xA100</td>
    </tr>
</table>

El perfil se ejecuta en una única GPU A100-SXM4-80G (salvo que se mencione 2xA100) con PyTorch 2.0.1, CUDA 11.8 y Flash-Attention 2. (72B + vLLM utiliza PyTorch 2.1.0 y Cuda 11.8.) La velocidad de inferencia se promedia sobre los tokens codificados y generados.

Nota: La velocidad de generación de los modelos Int4/Int8 mencionados anteriormente es proporcionada por la librería autogptq. La velocidad actual del modelo cargado utilizando ``AutoModelForCausalLM.from_pretrained`` será aproximadamente un 20% más lenta. Hemos informado de este problema al equipo de HuggingFace y lo actualizaremos rápidamente si se encuentra una solución.

También medimos la velocidad de inferencia y el uso de memoria de la GPU con diferentes configuraciones de contexto y longitudes de generación, versión Flash-Attention. Puedes encontrar los resultados en las modelcards correspondientes en Hugging Face o ModelScope.



## Finetuning

### Utilización
Ahora proporcionamos el script de entrenamiento oficial, `finetune.py`, para que los usuarios puedan ajustar el modelo preentrenado para aplicaciones posteriores de forma sencilla. Además, proporcionamos scripts de shell para lanzar el ajuste fino sin preocupaciones. Este script soporta el entrenamiento con [DeepSpeed](https://github.com/microsoft/DeepSpeed) y [FSDP](https://engineering.fb.com/2021/07/15/open-source/fsdp/). Los shell scripts que proporcionamos utilizan DeepSpeed (Nota: esto puede tener conflictos con la última versión de pydantic y debe utilizar make sure `pydantic<2.0`) y Peft. Puede instalarlos de la siguiente manera:
```bash
pip install "peft<0.8.0" deepspeed
```

Para preparar tus datos de entrenamiento, necesitas poner todas las muestras en una lista y guardarla en un archivo json. Cada muestra es un diccionario que consiste en un id y una lista para la conversación. A continuación se muestra una lista de ejemplo simple con 1 muestra:
```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "你好"
      },
      {
        "from": "assistant",
        "value": "我是一个语言模型，我叫通义千问。"
      }
    ]
  }
]
```

Una vez preparados los datos, puede utilizar los scripts de shell suministrados para ejecutar el ajuste fino. Recuerde especificar la ruta al archivo de datos, `$DATA`.

Los guiones de finetuning permiten realizar:
- Finetuning de todos los parámetros
- LoRA
- Q-LoRA

Full-parameter finetuning requires updating all parameters in the whole training process. To launch your training, run the following script:

```bash
# Entrenamiento distribuido. No proporcionamos un script de entrenamiento para una sola GPU, ya que la insuficiente memoria de la GPU interrumpiría el entrenamiento.
bash finetune/finetune_ds.sh
```

Recuerde especificar el nombre correcto del modelo o ruta, la ruta de datos, así como el directorio de salida en los scripts de shell. Otra cosa a notar es que usamos DeepSpeed ZeRO 3 en este script. Si desea realizar cambios, basta con eliminar el argumento `--deepspeed` o realizar cambios en el archivo json de configuración de DeepSpeed en función de sus necesidades. Además, este script soporta entrenamiento de precisión mixta, por lo que puedes usar `--bf16 True` o `--fp16 True`. Recuerde utilizar DeepSpeed cuando utilice fp16 debido al entrenamiento de precisión mixta. 
Empíricamente le aconsejamos que utilice bf16 para que su entrenamiento sea coherente con nuestro preentrenamiento y alineación si su máquina soporta bf16, y por lo tanto lo utilizamos por defecto.

Para ejecutar LoRA, utilice otro script para ejecutar como se muestra a continuación. Antes de empezar, asegúrese de que ha instalado `peft`. Además, es necesario especificar las rutas a su modelo, los datos y la salida. Le aconsejamos que utilice la ruta absoluta para su modelo pre-entrenado. Esto se debe a que LoRA sólo guarda el adaptador y la ruta absoluta en el archivo json de configuración del adaptador se utiliza para encontrar el modelo preentrenado para cargar. Además, este script soporta tanto bf16 como fp16.

```bash
# Single GPU training
bash finetune/finetune_lora_single_gpu.sh
# Distributed training
bash finetune/finetune_lora_ds.sh
```

En comparación con el ajuste fino de parámetros completos, LoRA ([artículo](https://arxiv.org/abs/2106.09685)) sólo actualiza los parámetros de las capas adaptadoras, pero mantiene congeladas las grandes capas originales del modelo de lenguaje. Esto permite muchos menos costes de memoria y, por tanto, de computación.

Tenga en cuenta que si utiliza LoRA para ajustar el modelo de lenguaje base, por ejemplo, Qwen-7B, en lugar de los modelos de chat, por ejemplo, Qwen-7B-Chat, el script cambia automáticamente la incrustación y la capa de salida como parámetros entrenables. Esto se debe a que el modelo de lenguaje base no tiene conocimiento de los tokens especiales que aporta el formato ChatML. Por lo tanto, estas capas deben actualizarse para que el modelo comprenda y prediga los tokens. O en otras palabras, si tu entrenamiento trae tokens especiales en LoRA, deberías poner las capas como parámetros entrenables poniendo `modules_to_save` dentro del código. Además, si tenemos estos parámetros entrenables, no está disponible para usar ZeRO 3, y es por esto que usamos ZeRO 2 en el script por defecto. Si no tenemos nuevos parámetros entrenables, podemos cambiar a ZeRO 3 cambiando el fichero de configuración de DeepSpeed. Además, encontramos que hay una brecha significativa entre la huella de memoria de LoRA con y sin estos parámetros entrenables. Por lo tanto, si usted tiene problemas con la memoria, le aconsejamos LoRA finetune los modelos de chat. Compruebe el perfil de abajo para obtener más información.

Si sigue sufriendo de memoria insuficiente, puede considerar Q-LoRA ([artículo](https://arxiv.org/abs/2305.14314)), que utiliza el modelo de lenguaje cuantizado de gran tamaño y otras técnicas como la atención paginada para permitir incluso menos costes de memoria.

Nota: para ejecutar el entrenamiento Q-LoRA con una sola GPU, puede que necesites instalar `mpi4py` a través de `pip` o `conda`.

Para ejecutar Q-LoRA, ejecute directamente el siguiente script:

```bash
# Entrenamiento con una sola GPU
bash finetune/finetune_qlora_single_gpu.sh
# Entrenamiento distribuida
bash finetune/finetune_qlora_ds.sh
```

Para Q-LoRA, le aconsejamos que cargue nuestro modelo cuantizado proporcionado, por ejemplo, Qwen-7B-Chat-Int4. **NO DEBE** utilizar los modelos bf16. A diferencia del finetuning de parámetros completos y LoRA, sólo fp16 es compatible con Q-LoRA. Para el entrenamiento con una sola GPU, tenemos que utilizar DeepSpeed para el entrenamiento de precisión mixta debido a nuestra observación de errores causados por el amplificador de antorcha. Además, para Q-LoRA, los problemas con los tokens especiales en LoRA siguen existiendo. Sin embargo, como sólo proporcionamos los modelos Int4 para los modelos de chat, lo que significa que el modelo lingüístico ha aprendido los tokens especiales del formato ChatML, no hay que preocuparse por las capas. Ten en cuenta que las capas del modelo Int4 no deben ser entrenables, por lo que si introduces tokens especiales en tu entrenamiento, Q-LoRA podría no funcionar.

> NOTA: Tenga en cuenta que debido a los mecanismos internos de Hugging Face, ciertos archivos que no son de Python (por ejemplo, `*.cpp` y `*.cu`) pueden faltar en el punto de control guardado. 
> pueden faltar en el punto de control guardado. Es posible que tenga que copiarlos manualmente en el directorio que contiene otros archivos.

A diferencia del finetuning de parámetros completo, el entrenamiento de LoRA y Q-LoRA sólo guarda los parámetros del adaptador. Supongamos que su entrenamiento comienza desde Qwen-7B, puede cargar el modelo ajustado para la inferencia como se muestra a continuación:

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()
```

Si quieres fusionar los adaptadores y guardar el modelo ajustado como un modelo independiente (sólo puedes hacer esto con LoRA, y NO puedes fusionar los parámetros desde Q-LoRA), puedes ejecutar los siguientes códigos:

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()

merged_model = model.merge_and_unload()
# max_shard_size and safe serialization are not necessary. 
# They respectively work for sharding checkpoint and save the model to safetensors
merged_model.save_pretrained(new_model_directory, max_shard_size="2048MB", safe_serialization=True)
```

Nota: Para el entrenamiento multi-GPU, es necesario especificar los hiperparámetros adecuados para el entrenamiento distribuido basado en su máquina. Además, le aconsejamos que especifique la longitud máxima de la secuencia con el argumento `--model_max_length`, en función de los datos, el espacio de memoria y la velocidad de entrenamiento.


### Perfiles de Memoria y Velocidad
Perfilamos la memoria de la GPU y la velocidad de entrenamiento tanto de LoRA (LoRA (emb) se refiere al entrenamiento de la capa de incrustación y salida, mientras que LoRA no tiene capa de incrustación y salida entrenables) como de Q-LoRA en la configuración de entrenamiento en una sola GPU. En esta prueba, experimentamos con una única GPU A100-SXM4-80G, y utilizamos CUDA 11.8 y Pytorch 2.0. Se aplica Flash attention 2. Utilizamos uniformemente un tamaño de lote de 1 y una acumulación de gradiente de 8. Perfilamos la memoria (GB) y la velocidad (s/iter) de entradas de distintas longitudes, a saber, 256, 512, 1024, 2048, 4096 y 8192. También presentamos las estadísticas del ajuste fino de todos los parámetros con Qwen-7B en 2 GPU A100. Sólo se presentan las estadísticas de 256, 512 y 1024 tokens debido a la limitación de memoria de la GPU. 

Para Qwen-72B, experimentamos de dos formas: 1) Ajuste fino de Lora + DeepSpeed ZeRO 3 en 4 GPUs A100-SXM4-80G y 2) Ajuste fino de QLora (int4) en una sola GPU A100-SXM4-80G. Ten en cuenta que la OOM se produce en 4 GPUs A100-SXM4-80G tanto con ajuste fino LoRA (emb) como con ajuste fino LoRA sin Deepspeed ZeRO 3 (puedes pasar `--deepspeed finetune/ds_config_zero3.json` a [`finetune/finetune_lora_ds.sh`](finetune/finetune_lora_ds.sh) para activar DeepSpeed ZeRO 3).

Las estadísticas se enumeran a continuación:

<table>
    <tr>
      <th rowspan="2">Model Size</th><th rowspan="2">Method</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">256</th><th align="center">512</th><th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th>
    </tr>
    </tr>
    </tr>
		<tr>
        <th rowspan="4">1.8B</th><td>LoRA</td><td align="center">6.7G / 1.0s/it</td><td align="center">7.4G / 1.0s/it</td><td align="center">8.4G / 1.1s/it</td><td align="center">11.0G / 1.7s/it</td><td align="center">16.2G / 3.3s/it</td><td align="center">21.8G / 6.8s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td><td align="center">13.7G / 1.0s/it</td><td align="center">14.0G / 1.0s/it</td><td align="center">14.0G / 1.1s/it</td><td align="center">15.1G / 1.8s/it</td><td align="center">19.7G / 3.4s/it</td><td align="center">27.7G / 7.0s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">5.8G / 1.4s/it</td><td align="center">6.0G / 1.4s/it</td><td align="center">6.6G / 1.4s/it</td><td align="center">7.8G / 2.0s/it</td><td align="center">10.2G / 3.4s/it</td><td align="center">15.8G / 6.5s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td><td align="center">43.5G / 2.1s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.3s/it</td><td align="center">47.1G / 2.8s/it</td><td align="center">48.3G / 5.6s/it</td>
    </tr>
    <tr>
        <th rowspan="4">7B</th><td>LoRA</td><td align="center">20.1G / 1.2s/it</td><td align="center">20.4G / 1.5s/it</td><td align="center">21.5G / 2.8s/it</td><td align="center">23.8G / 5.2s/it</td><td align="center">29.7G / 10.1s/it</td><td align="center">36.6G / 21.3s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td><td align="center">33.7G / 1.4s/it</td><td align="center">34.1G / 1.6s/it</td><td align="center">35.2G / 2.9s/it</td><td align="center">35.1G / 5.3s/it</td><td align="center">39.2G / 10.3s/it</td><td align="center">48.5G / 21.7s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">11.5G / 3.0s/it</td><td align="center">11.5G / 3.0s/it</td><td align="center">12.3G / 3.5s/it</td><td align="center">13.9G / 7.0s/it</td><td align="center">16.9G / 11.6s/it</td><td align="center">23.5G / 22.3s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td><td align="center">139.2G / 4.0s/it</td><td align="center">148.0G / 4.0s/it</td><td align="center">162.0G / 4.5s/it</td><td align="center">-</td><td align="center">-</td><td align="center">-</td>
    </tr>
    <tr>
        <th rowspan="3">14B</th><td>LoRA</td><td align="center">34.6G / 1.6s/it</td><td align="center">35.1G / 2.4s/it</td><td align="center">35.3G / 4.4s/it</td><td align="center">37.4G / 8.4s/it</td><td align="center">42.5G / 17.0s/it</td><td align="center">55.2G / 36.0s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td><td align="center">51.2 / 1.7s/it</td><td align="center">51.1G / 2.6s/it</td><td align="center">51.5G / 4.6s/it</td><td align="center">54.1G / 8.6s/it</td><td align="center">56.8G / 17.2s/it</td><td align="center">67.7G / 36.3s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">18.7G / 5.3s/it</td><td align="center">18.4G / 6.3s/it</td><td align="center">18.9G / 8.2s/it</td><td align="center">19.9G / 11.8s/it</td><td align="center">23.0G / 20.1s/it</td><td align="center">27.9G / 38.3s/it</td>
    </tr>
	<tr>
        <th rowspan="2">72B</th><td>LoRA + Deepspeed Zero3</td><td align="center">215.4G / 17.6s/it</td><td align="center">217.7G / 20.5s/it</td><td align="center">222.6G / 29.4s/it</td><td align="center">228.8G / 45.7s/it</td><td align="center">249.0G / 83.4s/it</td><td align="center">289.2G / 161.5s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">61.4G / 27.4s/it</td><td align="center">61.4G / 31.5s/it</td><td align="center">62.9G / 41.4s/it</td><td align="center">64.1G / 59.5s/it</td><td align="center">68.0G / 97.7s/it</td><td align="center">75.6G / 179.8s/it</td>
    </tr>
</table>
<br>

## Despliegue

### vLLM 
Para el despliegue y la inferencia rápida, sugerimos utilizar vLLM con FastChat. Instale primero los paquetes:
```bash
pip install vllm fastchat
```
O puede instalarlos desde el código fuente mediante `git clone` y `pip install -e .`. Le aconsejamos que lea sus documentos si encuentra problemas en la instalación.

Para ejecutar Qwen con vLLM y FastChat, primero necesitas lanzar un controlador por:
```bash
python -m fastchat.serve.controller
```

A continuación, puede iniciar el model worker, lo que significa cargar su modelo para la inferencia. Para la inferencia de una sola GPU, puede ejecutar directamente:

```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code
```
Sin embargo, si desea ejecutar el modelo en varias GPU para acelerar la inferencia o disponer de más memoria, puede utilizar el paralelismo tensorial soportado por vLLM. Supongamos que ejecutas el modelo en 4 GPUs, el comando se muestra a continuación:
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4
```

Después de lanzar tu model worker, puedes lanzar:

* Web UI Demo
```bash
python -m fastchat.serve.gradio_web_server
```

* API OpenAI
```bash
python -m fastchat.serve.openai_api_server --host localhost --port 8000
```

### Interfaz Web

Proporcionamos código para que los usuarios construyan una web UI demo (gracias a @wysaid). Antes de empezar, asegúrate de instalar los siguientes paquetes:
```
pip install -r requirements_web_demo.txt
```

A continuación, ejecute el siguiente comando y haga clic en el enlace generado:

```bash
python web_demo.py
```

<p align="center">
    <br>
    <img src="assets/web_demo.gif" width="600" />
    <br>
<p>

Sin embargo, si le resulta difícil utilizar vLLM y FastChat, puede probar los métodos más sencillos que le proporcionamos para desplegar una demo web, una demo CLI y una API.

### Demo CLI

Proporcionamos un ejemplo de demostración CLI en `cli_demo.py`, que soporta la salida de streaming para la generación. Los usuarios pueden interactuar con Qwen-7B-Chat introduciendo mensajes, y el modelo devuelve los resultados del modelo en modo streaming. Ejecute el siguiente comando:

```bash
python cli_demo.py
```

<p align="center">
    <br>
    <img src="assets/cli_demo.gif" width="600" />
    <br>
<p>
<br>

### API

Proporcionamos métodos para desplegar la API local basada en la API de OpenAI (gracias a @hanpenggit). Antes de empezar, instala los paquetes necesarios:

```bash
pip install fastapi uvicorn "openai<1.0" pydantic sse_starlette
```

A continuación, ejecute el comando para desplegar su API:

```bash
python openai_api.py
```

Puede cambiar sus argumentos, por ejemplo, `-c` para el nombre o la ruta del punto de control, `--cpu-only` para el despliegue en CPU, etc. Si tienes problemas al iniciar el despliegue de tu API, probablemente puedas solucionarlos actualizando los paquetes a la última versión.

Utilizar la API también es sencillo. Vea el siguiente ejemplo:

```python
import openai
openai.api_base = "http://localhost:8000/v1"
openai.api_key = "none"

# create a request activating streaming response
for chunk in openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=True 
    # Specifying stop words in streaming output format is not yet supported and is under development.
):
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

# create a request not activating streaming response
response = openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=False,
    stop=[] # You can add custom stop words here, e.g., stop=["Observation:"] for ReAct prompting.
)
print(response.choices[0].message.content)
```

<p align="center">
    <br>
    <img src="assets/openai_api.gif" width="600" />
    <br>
<p>

**Function calling** también está soportada (pero sólo cuando `stream=False` por el momento). Ver el [ejemplo de uso](examples/function_call_examples.py) aquí.
<br><br>

## 🐳 Docker

Para simplificar el proceso de despliegue, proporcionamos imágenes Docker con entornos preconstruidos: [qwenllm/qwen](https://hub.docker.com/r/qwenllm/qwen). Solo tienes que instalar el controlador y descargar los archivos del modelo para lanzar demos, desplegar la API de OpenAI y ajustar el modelo.

### Preparación

1. Instale la versión correcta del controlador Nvidia en función de la imagen que vaya a utilizar:
  - `qwenllm/qwen:cu117` (**recomendado**): `>= 515.48.07`
  - `qwenllm/qwen:cu114` (w/o flash-attention): `>= 470.82.01`
  - `qwenllm/qwen:cu121`: `>= 530.30.02`
  - `qwenllm/qwen:latest`: igual que `qwenllm/qwen:cu117`

2. Instale y configure [docker](https://docs.docker.com/engine/install/) y [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html):

```bash
# configure docker
sudo systemctl start docker
# test if docker is correctly installed
sudo docker run hello-world

# configure nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
# test if nvidia-container-toolkit is correctly installed
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

3. Descargue los checkpoints y los códigos del modelo a su entorno (véase [aquí](#DownloadModel)).

### Despliegue

Aquí usamos Qwen-7B-Chat como ejemplo. Antes de lanzar una demo web o API, puede establecer la configuración como se muestra a continuación:

```bash
IMAGE_NAME=qwenllm/qwen:cu117
PORT=8901
CHECKPOINT_PATH=/path/to/Qwen-7B-Chat   # Path to downloaded model checkpoints and codes
```
Los siguientes scripts pueden ayudarte a construir:

* API OpenAI
```bash
bash docker/docker_openai_api.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* Interfaz Web
```bash
bash docker/docker_web_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* Demo CLI
```bash
bash docker/docker_cli_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH}
```

Los comandos anteriores descargarán automáticamente la imagen requerida y lanzarán una demo Web UI en segundo plano (el servicio se reiniciará automáticamente). Puede abrir `http://localhost:${PORT}` en el host para utilizar la demo.

La demostración se ha iniciado correctamente si ve la siguiente salida:

```text
Successfully started web demo. Open '...' to try!
Run `docker logs ...` to check demo status.
Run `docker rm -f ...` to stop and remove the demo.
```

Si quieres comprobar el estado de la demo, puedes usar `docker logs qwen` para mostrar los resultados.

Puede utilizar `docker rm -f qwen` para detener el servicio y eliminar el contenedor.


### Finetuning

El método de finetuning utilizando la imagen Docker pre-construida es básicamente el mismo que [el capítulo anterior](#Finetuning) (ya hemos instalado dependencias en la imagen):

A continuación se muestra un ejemplo de LoRA de GPU única:
```bash
IMAGE_NAME=qwenllm/qwen:cu117
CHECKPOINT_PATH=/path/to/Qwen-7B                # Path to downloaded model checkpoints and codes
#CHECKPOINT_PATH=/path/to/Qwen-7B-Chat-Int4     # Path to downloaded model checkpoints and codes (Q-LoRA)
DATA_PATH=/path/to/data/root                    # Prepare finetune data at ${DATA_PATH}/example.json
OUTPUT_PATH=/path/to/output/checkpoint          # Path to finetune outputs

# Use all host devices by default
DEVICE=all
# If you need to specify GPUs for training, set device as follow (NOTE: internal quotation marks cannot be omitted)
#DEVICE='"device=0,1,2,3"'

mkdir -p ${OUTPUT_PATH}

# Single-GPU LoRA finetuning
docker run --gpus ${DEVICE} --rm --name qwen \
    --mount type=bind,source=${CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-7B \
    --mount type=bind,source=${DATA_PATH},target=/data/shared/Qwen/data \
    --mount type=bind,source=${OUTPUT_PATH},target=/data/shared/Qwen/output_qwen \
    --shm-size=2gb \
    -it ${IMAGE_NAME} \
    bash finetune/finetune_lora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B/ -d /data/shared/Qwen/data/example.json
```

Para realizar un cambio a Q-LoRA de una sola GPU, por ejemplo, basta con modificar el comando bash dentro de `docker run`:
```bash
bash finetune/finetune_qlora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B-Chat-Int4/ -d /data/shared/Qwen/data/example.json
```
<br>

## 🔥 Indicaciones del sistema
Qwen-1.8-Chat y Qwen-72B-Chat han sido completamente entrenados en diversas indicaciones del sistema con múltiples rondas de interacciones complejas, para que puedan seguir una variedad de indicaciones del sistema y realizar la personalización del modelo en contexto, mejorando aún más la escalabilidad de Qwen-chat.

Gracias a las instrucciones del sistema, Qwen-Chat puede realizar **juegos de rol**, **transferencia de estilos de lenguaje**, **configuración de tareas** y **configuración de comportamientos**.

![](assets/system_prompt_language_style.png)

![](assets/system_prompt_role_play_en.png)

Para más información, consulta la [documentación de ejemplo](examples/system_prompt.md).


## Uso de Herramientas

Qwen-Chat ha sido optimizado para el uso de herramientas y capacidades de llamada a funciones. Los usuarios pueden desarrollar agentes, aplicaciones LangChain e incluso aumentar Qwen con un intérprete de código Python.

Proporcionamos documentación sobre cómo implementar llamadas a herramientas basadas en el principio de ReAct Prompting, por favor consulte [the ReAct example](examples/react_prompt.md). Basándonos en este principio, proporcionamos soporte para llamadas a funciones en [openai_api.py](openai_api.py).

Hemos probado las capacidades de llamada de la herramienta del modelo en nuestro punto de referencia de evaluación chino de código abierto y hemos descubierto que Qwen-Chat obtiene siempre buenos resultados:

<table>
    <tr>
        <th colspan="4" align="center">Chinese Tool-Use Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th align="center">Model</th><th align="center">Tool Selection (Acc.↑)</th><th align="center">Tool Input (Rouge-L↑)</th><th align="center">False Positive Error↓</th>
    </tr>
    <tr>
        <td>GPT-4</td><td align="center">98.0%</td><td align="center">0.953</td><td align="center">23.9%</td>
    </tr>
    <tr>
        <td>GPT-3.5</td><td align="center">74.5%</td><td align="center">0.807</td><td align="center">80.6%</td>
    </tr>
    <tr>
        <td>Qwen-1_8B-Chat</td><td align="center">85.0%</td><td align="center">0.839</td><td align="center">27.6%</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td><td align="center">95.5%</td><td align="center">0.900</td><td align="center">11.6%</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td><td align="center">96.9%</td><td align="center">0.917</td><td align="center">5.6%</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td><td align="center">98.2%</td><td align="center">0.927</td><td align="center">1.1%</td>
    </tr>
</table>

Para evaluar la capacidad de Qwen para utilizar el intérprete de código Python en tareas como la resolución de problemas matemáticos, la visualización de datos y otras tareas de propósito general como el manejo de archivos y el web scraping, hemos creado y puesto a disposición del público un benchmark específicamente diseñado para evaluar estas capacidades. Puede encontrar el punto de referencia en este [enlace](https://github.com/QwenLM/Qwen-Agent/tree/main/benchmark).

Hemos observado que Qwen funciona bien en términos de ejecutabilidad del código y precisión de los resultados al generar código:

<table>
    <tr>
        <th colspan="5" align="center">Code Interpreter Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th rowspan="2" align="center">Model</th>
        <th colspan="3" align="center">Accuracy of Code Execution Results (%)</th>
        <th colspan="1" align="center">Executable Rate of Code (%)</th>
    </tr>
    <tr>
        <th align="center">Math↑</th><th align="center">Visualization-Hard↑</th><th align="center">Visualization-Easy↑</th><th align="center">General↑</th>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td align="center">82.8</td>
        <td align="center">66.7</td>
        <td align="center">60.8</td>
        <td align="center">82.8</td>
    </tr>
    <tr>
        <td>GPT-3.5</td>
        <td align="center">47.3</td>
        <td align="center">33.3</td>
        <td align="center">55.7</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>LLaMA2-13B-Chat</td>
        <td align="center">8.3</td>
        <td align="center">1.2</td>
        <td align="center">15.2</td>
        <td align="center">48.3</td>
    </tr>
    <tr>
        <td>CodeLLaMA-13B-Instruct</td>
        <td align="center">28.2</td>
        <td align="center">15.5</td>
        <td align="center">21.5</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>InternLM-20B-Chat</td>
        <td align="center">34.6</td>
        <td align="center">10.7</td>
        <td align="center">25.1</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>ChatGLM3-6B</td>
        <td align="center">54.2</td>
        <td align="center">4.8</td>
        <td align="center">15.2</td>
        <td align="center">67.1</td>
    </tr>
    <tr>
        <td>Qwen-1.8B-Chat</td>
        <td align="center">25.6</td>
        <td align="center">21.4</td>
        <td align="center">22.8</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td>
        <td align="center">41.9</td>
        <td align="center">23.8</td>
        <td align="center">38.0</td>
        <td align="center">67.2</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td>
        <td align="center">58.4</td>
        <td align="center">31.0</td>
        <td align="center">45.6</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td>
        <td align="center">72.7</td>
        <td align="center">41.7</td>
        <td align="center">43.0</td>
        <td align="center">82.8</td>
    </tr>
</table>

<p align="center">
    <br>
    <img src="assets/code_interpreter_showcase_001.jpg" />
    <br>
<p>

<br>

## Comprensión del Contexto Largo

Para ampliar la longitud del contexto y romper el cuello de botella de la longitud de la secuencia de entrenamiento, introducimos varias técnicas, como la interpolación NTK, la atención de ventana y el escalado de atención LogN, para ampliar la longitud del contexto de Qwen-14B de 2K a más de 8K tokens, y Qwen-1.8B/7B de 8K a 32K tokens. 

Para Qwen-72B, adaptamos RoPE a contextos más largos con una base rotatoria mayor. Qwen-72B admite una longitud máxima de contexto de 32K tokens.

Realizamos experimentos de modelado lingüístico en el conjunto de datos arXiv con la evaluación PPL y descubrimos que Qwen puede alcanzar un rendimiento sobresaliente en el escenario de contextos largos. Los resultados se muestran a continuación:

<table>
    <tr>
        <th rowspan="2">Model</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th><th align="center">16384</th><th align="center">32768</th>
    </tr>
     <tr>
        <td>Qwen-7B (original)</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">39.35</td><td align="center">469.81</td><td align="center">2645.09</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.59</td><td align="center">3.66</td><td align="center">5.71</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.58</td><td align="center">3.56</td><td align="center">4.62</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.58</td><td align="center">3.49</td><td align="center">4.32</td><td align="center">-</td>
    </tr>
    <tr>
    <tr>
        <td>Qwen-1.8B</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.13</b></td><td align="center"><b>3.89</b></td><td align="center">17.42</td><td align="center">433.85</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.14</b></td><td align="center"><b>3.93</b></td><td align="center"><b>3.82</b></td><td align="center"><b>3.83</b></td>
    </tr>
    <tr>
        <td>Qwen-7B</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.31</b></td><td align="center">7.27</td><td align="center">181.49</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.33</b></td><td align="center"><b>3.22</b></td><td align="center"><b>3.17</b></td>
    </tr>
    <tr>
        <td>Qwen-14B</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center">22.79</td><td align="center">334.65</td><td align="center">3168.35</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center"><b>3.29</b></td><td align="center"><b>3.18</b></td><td align="center">3.42</td><td align="center">-</td>
    </tr>
    <tr>
        <td>Qwen-72B</td><td align="center"><b>-</b></td><td align="center"><b>-</b></td><td align="center">-</td><td align="center"><b>2.83</b></td><td align="center"><b>2.73</b></td><td align="center"><b>2.72</b></td>
    </tr>
    </tr>
</table>

Furthermore, to verify the ability of Qwen-72B-Chat on long text understanding, we tested it on [L-Eval](https://arxiv.org/abs/2307.11088) (closed-ended tasks). The results are as follows:

| Model             | Input Length | Average   |  Coursera  |    GSM     |   QuALITY  |    TOEFL   |   CodeU    |  SFcition  |
|:------------------|:------------:|:---------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| ChatGPT-3.5-16k   |     16K      |   60.73   | **63.51**  | **84.00**  |   61.38    |    78.43   | **12.22**  |    64.84   |
| **Qwen-72B-Chat** |     32K      | **62.30** |   58.13    |   76.00    | **77.22**  |  **86.24** |    6.66    |  **69.53** |

Hemos realizado el experimento de la "aguja en el pajar" (la idea procede de [@Greg Kamradt](https://twitter.com/GregKamradt/status/1727018183608193393)) para comprobar si el modelo puede recuperar información en distintas posiciones de las entradas de distintas longitudes, el resultado es el siguiente:

![](assets/qwen_72b_needle_in_a_haystack.png)

Los resultados anteriores muestran que Qwen-72B-Chat puede recuperar con precisión información situada en varias posiciones dentro de una longitud de entrada de 32K, lo que demuestra su excelente capacidad de comprensión de textos largos.


## Tokenizador

Nuestro tokenizador basado en tiktoken es diferente de otros tokenizadores, por ejemplo, el tokenizador sentencepiece. Es necesario prestar atención a los tokens especiales, especialmente en el finetuning. Para obtener información más detallada sobre el tokenizador y su uso en el ajuste fino, consulte la [documentación](tokenization_note.md).
<br><br>

## Reproducción

Para que pueda reproducir el rendimiento del modelo en conjuntos de datos de referencia, le proporcionamos secuencias de comandos para que reproduzca los resultados. Consulte [eval/EVALUATION.md](eval/EVALUATION.md) para obtener más información. Tenga en cuenta que la reproducción puede dar lugar a ligeras diferencias con respecto a nuestros resultados.
<br><br>

## FAQ

Si tiene problemas, consulte primero [FAQ](FAQ.md) y las incidencias para buscar una solución antes de lanzar una nueva incidencia.
<br><br>

## Cita
Si nuestro trabajo le resulta útil, no dude en citarnos.

```
@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
}
```
<br>

## Acuerdo de Licencia

El código fuente proporcionado en <https://github.com/QwenLM/Qwen> está licenciado bajo la [Licencia Apache 2.0](./LICENSE) que puede encontrarse en el directorio raíz.

Los investigadores y desarrolladores son libres de utilizar los códigos y los pesos de los modelos tanto de Qwen como de Qwen-Chat. Para su uso comercial, consulte el Acuerdo de Licencia que acompaña a cada modelo.

- Qwen-72B, Qwen-14B, y Qwen-7B están licenciados bajo el [Tongyi Qianwen LICENSE AGREEMENT](./Tongyi%20Qianwen%20LICENSE%20AGREEMENT) que se puede encontrar en el repositorio correspondiente de HuggingFace y ModelScope. Para uso comercial, rellene el formulario ([72B](https://dashscope.console.aliyun.com/openModelApply/Qwen-72B-Chat), [14B](https://dashscope.console.aliyun.com/openModelApply/Qwen-14B-Chat), y [7B](https://dashscope.console.aliyun.com/openModelApply/qianwen)) para solicitarlo.

- Qwen-1.8B está licenciado bajo el [Tongyi Qianwen RESEARCH LICENSE AGREEMENT](./Tongyi%20Qianwen%20RESEARCH%20LICENSE%20AGREEMENT) que puede encontrarse en el repositorio correspondiente de HuggingFace y ModelScope. Para uso comercial, póngase en contacto con nosotros.
<br><br>

## Contacte con Nosotros

Si estás interesado en dejar un mensaje a nuestro equipo de investigación o de producto, únete a nuestros grupos de Discord o WeChat. También puedes enviar un correo electrónico a qianwen_opensource@alibabacloud.com.

```

## File: `README_FR.md`
```markdown
<p align="left">
    <a href="README_CN.md">中文</a>&nbsp ｜ &nbsp<a href="README.md">English</a>&nbsp ｜ &nbsp<a href="README_JA.md">日本語</a>&nbsp ｜ &nbspFrançais ｜ &nbsp<a href="README_ES.md">Español</a>
</p>
<br><br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/logo_qwen.jpg" width="400"/>
<p>
<br>

<p align="center">
        🤗 <a href="https://huggingface.co/Qwen">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/qwen">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2309.16609">Paper</a> &nbsp&nbsp ｜ &nbsp&nbsp🖥️ <a href="https://modelscope.cn/studios/qwen/Qwen-72B-Chat-Demo/summary">Demo</a>
<br>
<a href="assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp<a href="https://discord.gg/z3GAxXZ9Ce">Discord</a>&nbsp&nbsp ｜  &nbsp&nbsp<a href="https://dashscope.aliyun.com">API</a> 
</p>
<br><br>

> [!Important]
> Qwen2 est là ! Vous êtes invité à suivre [QwenLM/Qwen2](https://github.com/QwenLM/Qwen2) et à partager vos expériences là-bas.
>
> Ce repo ([QwenLM/Qwen](https://github.com/QwenLM/Qwen)) n'est plus activement maintenu, en raison de différences substantielles dans le code source.
<br>

|     |                                                              Qwen-Chat                                                               |                                                                Qwen-Chat (Int4)                                                                |                        Qwen-Chat (Int8)                         |                                                            Qwen                                                            |
|-----|:------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 1.8B  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B">🤗</a>  |
| 7B  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B">🤗</a>  |
| 14B | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B">🤗</a> |
| 72B | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B">🤗</a> |



Nous ouvrons notre série **Qwen**, qui comprend désormais **Qwen**, les modèles de langue de base, à savoir **Qwen-7B** et **Qwen-14B**, ainsi que **Qwen-Chat**, les modèles de chat, à savoir **Qwen-7B-Chat** et **Qwen-14B-Chat**. Les liens se trouvent dans le tableau ci-dessus. Cliquez dessus et consultez les fiches des modèles. Nous publions également le **[rapport technique](https://arxiv.org/abs/2309.16609)**. Cliquez sur le lien du document et consultez-le !

En bref, nous disposons de modèles linguistiques solides, qui ont été pré-entraîné de manière stable pour 3 000 milliards de tokens de données multilingues avec une large couverture de domaines, de langues (en particulier le chinois et l'anglais), etc. Ils sont capables d'atteindre des performances compétitives sur des ensembles de données de référence. En outre, nous disposons de modèles de chat alignés sur les préférences humaines basées sur SFT et RLHF (pas encore publiés), qui sont capables de chatter, de créer du contenu, d'extraire des informations, de résumer, de traduire, de coder, de résoudre des problèmes mathématiques, etc. et d'utiliser des outils, de jouer le rôle d'agents ou même code interpreter, etc.

| Modèle    | Date de sortie | Longueur maximale | Amélioration de l'invite du système | # de tokens pré-formés | Utilisation minimale de la mémoire du GPU pour Finetuning (Q-Lora) | Utilisation minimale du GPU pour générer 2048 jetons (Int4) | Utilisation des outils |
|:----------|:--------------:|:-----------------:|:-----------------------------------:|:----------------------:|:------------------------------------------------------------------:|:-----------------------------------------------------------:|:----------------------:|
| Qwen-1.8B |    23.11.30    |        32K        |                  ✅                  |          2.2T          |                               5.8GB                                |                            2.9GB                            |           ✅            |  
| Qwen-7B   |    23.08.03    |        32K        |                  ❎                  |          2.4T          |                               11.5GB                               |                            8.2GB                            |           ✅            |   
| Qwen-14B  |    23.09.25    |        8K         |                  ❎                  |          3.0T          |                               18.7GB                               |                           13.0GB                            |           ✅            |
| Qwen-72B  |    23.11.30    |        32K        |                  ✅                  |          3.0T          |                               61.4GB                               |                           48.9GB                            |           ✅            |   


Dans la repo, vous pouvez trouver:

* Comment utiliser Qwen, et profiter de l'inférence simple.
* Détails sur les modèles de quantization, y compris GPTQ et la quantization de KV cache.
* Statistiques sur les performances de l'inférence, y compris la vitesse et la mémoire.
* Tutoriels sur le finetuning, y compris le finetuning de paramètres complets, LoRA, et Q-LoRA.
* Instructions de déploiement, avec l'exemple de vLLM et FastChat.
* Instructions sur la création de démos, y compris WebUI, démo CLI, etc.
* Introduction au service API de DashScope, ainsi que les instructions pour construire une API de type OpenAI pour votre modèle.
* Informations sur Qwen pour l'utilisation d'outils, d'agents et code interpreter.
* Statistiques de l'évaluation de la compréhension du contexte long.
* Contrat de licence.
* ...

En outre, si vous rencontrez des problèmes, consultez d'abord la [FAQ](FAQ.md) pour obtenir de l'aide. Vous vous sentez toujours en difficulté ? N'hésitez pas à nous envoyer des questions (de préférence en anglais pour que plus de gens puissent vous comprendre) ! Si vous souhaitez nous aider, envoyez-nous des demandes d'extension sans hésitation ! Nous sommes toujours enthousiastes à propos des relations publiques ! 

Vous voulez discuter avec nous ou prendre un café avec nous ? Bienvenue sur notre Discord ou WeChat !
<br><br>

## Nouvelles et mises à jour

* 2023.11.30 🔥 Nous publions **Qwen-72B** et **Qwen-72B-Chat**, qui sont entraînés sur des tokens 3T et prennent en charge 32k contextes, ainsi que **Qwen-1.8B** et **Qwen-1.8B-Chat**, sur ModelScope et Hugging Face. Nous avons également renforcé les capacités de l'invite système du Qwen-72B-Chat et du Qwen-1.8B-Chat, voir la [documentation d'exemple](examples/system_prompt.md). De plus, nous supportons l'inférence sur **Ascend 910** et **Hygon DCU**. Consultez `ascend-support` et `dcu-support` pour plus de détails.
* 2023.10.17 Nous publions le modèle quantifié Int8 **Qwen-7B-Chat-Int8** et **Qwen-14B-Chat-Int8**.
* 2023.9.25 🔥 Nous publions **Qwen-14B** et **Qwen-14B-Chat** sur ModelScope et Hugging Face, ainsi que [qwen.cpp](https://github.com/QwenLM/qwen.cpp) et [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent). Les codes et les poids de **Qwen-7B** et **Qwen-7B-Chat** ont également été mis à jour. **S'IL VOUS PLAÎT, TIREZ LA DERNIÈRE VERSION!**
    - Par rapport à **Qwen-7B** (original), **Qwen-7B** utilise davantage de jetons d'entraînement, passant de 2,2 à 2,4T de jetons, tandis que la longueur du contexte passe de 2048 à 8192. La connaissance du chinois et la capacité de codage de **Qwen-7B** ont été encore améliorées.
* 2023.9.12 Nous prenons désormais en charge le finetuning sur les modèles Qwen-7B, y compris le finetuning de tous les paramètres, LoRA et Q-LoRA.
* 2023.8.21 Nous publions le modèle quantifié Int4 pour Qwen-7B-Chat, **Qwen-7B-Chat-Int4**, qui nécessite de faibles coûts de mémoire mais permet d'améliorer la vitesse d'inférence. En outre, il n'y a pas de dégradation significative des performances lors de l'évaluation de référence.
* 2023.8.3 Nous publions **Qwen-7B** et **Qwen-7B-Chat** sur ModelScope et Hugging Face. Nous fournissons également un mémo technique pour plus de détails sur le modèle, y compris les détails de l'entraînement et les performances du modèle.
<br>

## Performance

Les modèles Qwen surpassent les modèles de base de taille similaire sur une série de données de référence, par exemple MMLU, C-Eval, GSM8K, MATH, HumanEval, MBPP, BBH, etc., qui évaluent les capacités des modèles sur la compréhension du langage naturel, la résolution de problèmes mathématiques, le codage, etc. Qwen-72B obtient de meilleures performances que LLaMA2-70B dans toutes les tâches et surpasse GPT-3.5 dans 7 tâches sur 10.

<p align="left">
    <img src="assets/radar_72b.jpg" width=600px/>
<p>
<br>

| Model             |   MMLU   |  C-Eval  |  GSM8K   |   MATH   | HumanEval |   MBPP   |   BBH    |  CMMLU   |
|:------------------|:--------:|:--------:|:--------:|:--------:|:---------:|:--------:|:--------:|:--------:|
|                   |  5-shot  |  5-shot  |  8-shot  |  4-shot  |  0-shot   |  3-shot  |  3-shot  |  5-shot  |
| LLaMA2-7B         |   46.8   |   32.5   |   16.7   |   3.3    |   12.8    |   20.8   |   38.2   |   31.8   |
| LLaMA2-13B        |   55.0   |   41.4   |   29.6   |   5.0    |   18.9    |   30.3   |   45.6   |   38.4   |
| LLaMA2-34B        |   62.6   |    -     |   42.2   |   6.2    |   22.6    |   33.0   |   44.1   |    -     |
| ChatGLM2-6B       |   47.9   |   51.7   |   32.4   |   6.5    |     -     |    -     |   33.7   |    -     |
| InternLM-7B       |   51.0   |   53.4   |   31.2   |   6.3    |   10.4    |   14.0   |   37.0   |   51.8   |
| InternLM-20B      |   62.1   |   58.8   |   52.6   |   7.9    |   25.6    |   35.6   |   52.5   |   59.0   |
| Baichuan2-7B      |   54.7   |   56.3   |   24.6   |   5.6    |   18.3    |   24.2   |   41.6   |   57.1   |
| Baichuan2-13B     |   59.5   |   59.0   |   52.8   |   10.1   |   17.1    |   30.2   |   49.0   |   62.0   |
| Yi-34B      	  	  |   76.3   |   81.8   |   67.9   |   15.9   |   26.2    |   38.2   |   66.4   |   82.6   |
| XVERSE-65B      	 |   70.8   |   68.6   |   60.3   |    -     |   26.3    |    -     |    -     |    -     |
| **Qwen-1.8B**     |   45.3   |   56.1   |   32.3   |   2.3    |   15.2    |   14.2   |   22.3   |   52.1   |
| **Qwen-7B**       |   58.2   |   63.5   |   51.7   |   11.6   |   29.9    |   31.6   |   45.0   |   62.2   |
| **Qwen-14B**      |   66.3   |   72.1   |   61.3   |   24.8   |   32.3    |   40.8   |   53.4   |   71.0   |
| **Qwen-72B**      | **77.4** | **83.3** | **78.9** | **35.2** | **35.4**  | **52.2** | **67.7** | **83.6** |

Pour tous les modèles comparés, nous indiquons les meilleurs scores entre leurs résultats officiels et [OpenCompass] (https://opencompass.org.cn/leaderboard-llm). 

Pour plus de résultats expérimentaux (performances détaillées des modèles sur d'autres ensembles de données de référence) et de détails, veuillez vous référer à notre rapport technique en cliquant [ici](https://qianwen-res.oss-cn-beijing.aliyuncs.com/QWEN_TECHNICAL_REPORT.pdf).
<br><br>

## Besoins

* python 3.8 et plus
* pytorch 1.12 et plus, 2.0 et plus sont recommandés
* transformers 4.32 et plus
* CUDA 11.4 et plus sont recommandés (pour les utilisateurs de GPU, les utilisateurs de flash, etc.)
<br>

## Démarrage Rapide

Ci-dessous, nous fournissons des exemples simples pour montrer comment utiliser Qwen-Chat avec 🤖 ModelScope et 🤗 Transformers.

Vous pouvez utiliser nos images docker pré-construites pour sauter la plupart des étapes de configuration de l'environnement, voir la section ["Utiliser des images docker pré-construites"](#-docker) pour plus de détails. 

Si vous n'utilisez pas Docker, assurez-vous d'avoir configuré l'environnement et installé les paquets requis. Assurez-vous de répondre aux exigences ci-dessus, puis installez les bibliothèques dépendantes.

```bash
pip install -r requirements.txt
```

Si votre appareil supporte fp16 ou bf16, nous vous recommandons d'installer [flash-attention](https://github.com/Dao-AILab/flash-attention) (**nous supportons flash-attention 2 maintenant.**) pour une meilleure efficacité et une moindre utilisation de la mémoire. (**flash-attention est optionnel et le projet peut fonctionner normalement sans l'installer**)

```bash
git clone https://github.com/Dao-AILab/flash-attention
cd flash-attention && pip install .
# Below are optional. Installing them might be slow.
# pip install csrc/layer_norm
# pip install csrc/rotary
```

Vous pouvez maintenant commencer avec ModelScope ou Transformers.

### 🤗 Transformers

Pour utiliser Qwen-Chat pour l'inférence, il vous suffit de saisir quelques lignes de code, comme indiqué ci-dessous. N'oubliez pas de transmettre les noms de modèles ou les chemins corrects, tels que "Qwen/Qwen-7B-Chat" et "Qwen/Qwen-14B-Chat". Cependant, **veuillez vous assurer que vous utilisez le code le plus récent**.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names: "Qwen/Qwen-7B-Chat", "Qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# use bf16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
# use auto mode, automatically select precision based on the device.
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
    device_map="auto",
    trust_remote_code=True
).eval()

# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# 1st dialogue turn
response, history = model.chat(tokenizer, "你好", history=None)
print(response)
# 你好！很高兴为你提供帮助。

# 2nd dialogue turn
response, history = model.chat(tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
# 这是一个关于一个年轻人奋斗创业最终取得成功的故事。
# 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。
# 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。
# 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。
# 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。
# 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。

# 3rd dialogue turn
response, history = model.chat(tokenizer, "给这个故事起一个标题", history=history)
print(response)
# 《奋斗创业：一个年轻人的成功之路》
```

L'exécution du modèle pré-entraîné de Qwen est également simple.

<details>
  <summary>Running Qwen</summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names: "Qwen/Qwen-7B", "Qwen/Qwen-14B" 
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)
# use bf16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="cpu", trust_remote_code=True).eval()
# use auto mode, automatically select precision based on the device.
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B",
    device_map="auto",
    trust_remote_code=True
).eval()

# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)

inputs = tokenizer('蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是', return_tensors='pt')
inputs = inputs.to(model.device)
pred = model.generate(**inputs)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))
# 蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是亚的斯亚贝巴（Addis Ababa）...
```

</details>

En cas de problème de réseau lors de la tentative de téléchargement des poids et des codes du modèle à partir de HuggingFace, une autre approche consiste à récupérer le point de contrôle à partir de ModelScope, puis à le charger à partir du répertoire local, comme indiqué ci-dessous:

```python
from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Downloading model checkpoint to a local dir model_dir
# model_dir = snapshot_download('qwen/Qwen-7B')
# model_dir = snapshot_download('qwen/Qwen-7B-Chat')
# model_dir = snapshot_download('qwen/Qwen-14B')
model_dir = snapshot_download('qwen/Qwen-14B-Chat')

# Loading local checkpoints
# trust_remote_code is still set as True since we still load codes from local dir instead of transformers
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True
).eval()
```

### 🤖 ModelScope

ModelScope est une plateforme opensource pour Model-as-a-Service (MaaS), qui fournit un service de modèle flexible et rentable aux développeurs d'IA. De même, vous pouvez exécuter les modèles avec ModelScope comme indiqué ci-dessous:

```python
from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

# Model names: "qwen/Qwen-7B-Chat", "qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("qwen/Qwen-7B-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

response, history = model.chat(tokenizer, "你好", history=None)
print(response)
response, history = model.chat(tokenizer, "浙江的省会在哪里？", history=history) 
print(response)
response, history = model.chat(tokenizer, "它有什么好玩的景点", history=history)
print(response)
```

### Inférence par lots
Qwen prend en charge l'inférence par lots. Lorsque flash attention est activée, l'utilisation de l'inférence par lots peut entraîner une accélération de 40 %. Le code d'exemple est présenté ci-dessous:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GenerationConfig
from qwen_generation_utils import make_context, decode_tokens, get_stop_words_ids

tokenizer = AutoTokenizer.from_pretrained(
    './',
    pad_token='<|extra_0|>',
    eos_token='<|endoftext|>',
    padding_side='left',
    trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    './',
    pad_token_id=tokenizer.pad_token_id,
    device_map="auto",
    trust_remote_code=True
).eval()
model.generation_config = GenerationConfig.from_pretrained('./', pad_token_id=tokenizer.pad_token_id)

all_raw_text = ["我想听你说爱我。", "今天我想吃点啥，甜甜的，推荐下", "我马上迟到了，怎么做才能不迟到"]
batch_raw_text = []
for q in all_raw_text:
    raw_text, _ = make_context(
        tokenizer,
        q,
        system="You are a helpful assistant.",
        max_window_size=model.generation_config.max_window_size,
        chat_format=model.generation_config.chat_format,
    )
    batch_raw_text.append(raw_text)

batch_input_ids = tokenizer(batch_raw_text, padding='longest')
batch_input_ids = torch.LongTensor(batch_input_ids['input_ids']).to(model.device)
batch_out_ids = model.generate(
    batch_input_ids,
    return_dict_in_generate=False,
    generation_config=model.generation_config
)
padding_lens = [batch_input_ids[i].eq(tokenizer.pad_token_id).sum().item() for i in range(batch_input_ids.size(0))]

batch_response = [
    decode_tokens(
        batch_out_ids[i][padding_lens[i]:],
        tokenizer,
        raw_text_len=len(batch_raw_text[i]),
        context_length=(batch_input_ids[i].size(0)-padding_lens[i]),
        chat_format="chatml",
        verbose=False,
        errors='replace'
    ) for i in range(len(all_raw_text))
]
print(batch_response)

response, _ = model.chat(tokenizer, "我想听你说爱我。", history=None)
print(response)

response, _ = model.chat(tokenizer, "今天我想吃点啥，甜甜的，推荐下", history=None)
print(response)

response, _ = model.chat(tokenizer, "我马上迟到了，怎么做才能不迟到", history=None)
print(response)
```

### CPU

Pour déployer nos modèles sur CPU, nous vous conseillons vivement d'utiliser [qwen.cpp](https://github.com/QwenLM/qwen.cpp), qui est une implémentation purement C++ de Qwen et de tiktoken. Consultez le repo pour plus de détails!

Il est simple d'exécuter directement le modèle sur le CPU, ce qui nécessite la spécification de votre appareil:

```python
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
```

Cependant, il est probable que vous souffriez d'une efficacité d'inférence extrêmement faible.

### Plusieurs GPU

Si vous souffrez d'un manque de mémoire GPU et que vous souhaitez exécuter le modèle sur plus d'un GPU, vous pouvez utiliser directement la méthode de chargement par défaut, qui est maintenant supportée par Transformers. La méthode précédente basée sur `utils.py` est obsolète.

Cependant, bien que cette méthode soit simple, l'efficacité du parallélisme natif du pipeline est faible. Nous vous conseillons d'utiliser vLLM avec FastChat et de lire la section relative au déploiement.


### DashScope

Le moyen le plus simple d'utiliser Qwen via les API est le service API DashScope via Alibaba Cloud. Nous présentons une introduction à l'utilisation. De plus, nous fournissons un script pour vous permettre de déployer une API de type OpenAI sur vos propres serveurs.

DashScope est le service API de grands modèles linguistiques fourni par Alibaba Cloud, qui prend désormais en charge Qwen. Notez que les modèles derrière DashScope sont des versions internes temporairement sans détails fournis. Les services comprennent `qwen-turbo` et `qwen-plus`, le premier fonctionnant plus rapidement et le second atteignant de meilleures performances. Pour plus d'informations, consultez la documentation [ici] (https://dashscope.aliyun.com).

Veuillez vous rendre sur le site officiel [lien](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key?spm=a2c4g.11186623.0.0.6c2774fahtfXdn) pour créer un compte DashScope et obtenir la clé API (AK). Nous recommandons de définir l'AK à l'aide d'une variable d'environnement:
```bash
export DASHSCOPE_API_KEY="YOUR_DASHSCOPE_API_KEY"
```
Installez ensuite les paquets et cliquez sur [ici](https://help.aliyun.com/zh/dashscope/developer-reference/install-dashscope-sdk) pour obtenir la documentation. Si vous utilisez Python, vous pouvez installer DashScope avec pip:
```bash
pip install dashscope
```
Si vous utilisez JAVA SDK, vous pouvez l'installer de cette manière:
```xml
<!-- https://mvnrepository.com/artifact/com.alibaba/dashscope-sdk-java -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dashscope-sdk-java</artifactId>
    <version>the-latest-version</version>
</dependency>
```
La manière la plus simple d'utiliser DashScope est l'utilisation de messages, qui est similaire à l'API OpenAI. L'exemple est présenté ci-dessous:
```python
import random
from http import HTTPStatus
from dashscope import Generation


def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '如何做西红柿鸡蛋？'}]
    gen = Generation()
    response = gen.call(
        Generation.Models.qwen_turbo,
        messages=messages,
        seed=random.randint(1, 10000),  # set the random seed, optional, default to 1234 if not set
        result_format='message',  # set the result to be "message" format.
    )
    return response


if __name__ == '__main__':
    response = call_with_messages()
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
```
Pour d'autres utilisations, veuillez consulter le site web officiel pour plus de détails.
<br><br>

## Quantization

### GPTQ

Nous proposons une solution basée sur [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ), et publions les modèles quantifiés Int4 et Int8, qui permettent d'obtenir des effets de modèle presque sans perte mais des performances améliorées en termes de coûts de mémoire et de vitesse d'inférence.

Nous démontrons ici comment utiliser les modèles quantifiés que nous fournissons pour l'inférence. Avant de commencer, assurez-vous que vous répondez aux exigences d'auto-gptq (par exemple, torch 2.0 et plus, transformers 4.32.0 et plus, etc.) et installez les paquets requis:

```bash
pip install auto-gptq optimum
```

Si vous rencontrez des problèmes pour installer `auto-gptq`, nous vous conseillons de consulter le [repo](https://github.com/PanQiWei/AutoGPTQ) officiel pour trouver une roue.

> Note : Les paquets `auto-gptq` précompilés dépendent fortement de la version de `torch` et de sa version CUDA. De plus, en raison d'une récente mise à jour,
> vous pouvez aussi rencontrer des erreurs de version non supportée avec `transformers`, `optimum`, ou `peft`.
> Nous recommandons d'utiliser les dernières versions répondant aux exigences suivantes :
> - torch==2.1 auto-gptq>=0.5.1 transformers>=4.35.0 optimum>=1.14.0 peft>=0.6.1
> - torch>=2.0,<2.1 auto-gptq<0.5.0 transformers<4.35.0 optimum<1.14.0 peft>=0.5.0,<0.6.0

Vous pouvez ensuite charger facilement le modèle quantifié et lancer l'inférence comme d'habitude:

```python
# Model names: "Qwen/Qwen-7B-Chat-Int4", "Qwen/Qwen-14B-Chat-Int4"
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat-Int4",
    device_map="auto",
    trust_remote_code=True
).eval()
response, history = model.chat(tokenizer, "Hi", history=None)
```

Nous illustrons les performances des modèles BF16, Int8 et Int4 sur le benchmark, et nous constatons que le modèle quantifié ne souffre pas d'une dégradation significative des performances. Les résultats sont présentés ci-dessous:

| Quantization         | MMLU | CEval (val) | GSM8K | Humaneval |
|----------------------|:----:|:-----------:|:-----:|:---------:|
| Qwen-1.8B-Chat (BF16)| 43.3 |    55.6     | 33.7  |   26.2    |
| Qwen-1.8B-Chat (Int8)| 43.1 |    55.8     | 33.0  |   27.4    |
| Qwen-1.8B-Chat (Int4)| 42.9 |    52.8     | 31.2  |   25.0    |
| Qwen-7B-Chat (BF16)  | 55.8 |    59.7     | 50.3  |   37.2    |
| Qwen-7B-Chat (Int8)  | 55.4 |    59.4     | 48.3  |   34.8    |
| Qwen-7B-Chat (Int4)  | 55.1 |    59.2     | 49.7  |   29.9    |
| Qwen-14B-Chat (BF16) | 64.6 |    69.8     | 60.1  |   43.9    |
| Qwen-14B-Chat (Int8) | 63.6 |    68.6     | 60.0  |   48.2    |
| Qwen-14B-Chat (Int4) | 63.3 |    69.0     | 59.8  |   45.7    |
| Qwen-72B-Chat (BF16) | 74.4 |    80.1     | 76.4  |   64.6    |
| Qwen-72B-Chat (Int8) | 73.5 |    80.1     | 73.5  |   62.2    |
| Qwen-72B-Chat (Int4) | 73.4 |    80.1     | 75.3  |   61.6    |

### Quantization du cache KV

> NOTE : Veuillez noter qu'en raison du mécanisme interne de Hugging Face, les fichiers de support pour cette fonctionnalité 
> (i.e., `cache_autogptq_cuda_256.cpp` et `cache_autogptq_cuda_kernel_256.cu`) peuvent être manquants. 
> Veuillez les télécharger manuellement manuellement depuis le Hugging Face Hub et placez-les dans le même dossier que les autres fichiers du module.

Le cache KV de l'attention peut être quantifié et compressé pour le stockage, afin d'obtenir un débit d'échantillonnage plus élevé. Les arguments `use_cache_quantization` et `use_cache_kernel` dans `config.json` sont fournis pour activer la quantification du cache KV. 
La méthode d'utilisation spécifique est la suivante:

```python
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
     device_map="auto",
     trust_remote_code=True,
     use_cache_quantization=True,
     use_cache_kernel=True,
     use_flash_attn=False
)
```
Attention : Actuellement, la quantification du cache KV et flash attention ne peuvent pas être utilisées en même temps.
Si vous activez la quantification du cache KV et flash attention en même temps (`use_flash_attn=True`, `use_cache_quantization=True`, `use_cache_kernel=True`), `use_flash_attn` est désactivé par défaut (`use_flash_attn=false`).

Nous avons vérifié que l'utilisation du modèle int8-kvcache quantifié ne souffre pas d'une dégradation significative des performances dans l'évaluation en aval. Dans ce qui suit, nous nous concentrons sur le profilage de son empreinte mémoire dans différentes conditions. 
Le profilage s'exécute sur un seul GPU A100-SXM4-80G avec PyTorch 2.0.1 et CUDA 11.4. 
Nous utilisons des modèles BF16 pour générer 1024 jetons par défaut, et "OOM" indique une erreur de mémoire insuffisante.

Avec la quantification du cache KV, le modèle peut inférer avec une taille de lot (bs) plus grande.

| Utilisation du cache KV |  bs=1  |  bs=4  | bs=16  | bs=32  | bs=64  | bs=100 |
|--------------|:------:|:------:|:------:|:------:|:------:|:------:|
| Non          | 16.3GB | 24.1GB | 31.7GB | 48.7GB |  OOM   |  OOM   |
| Oui          | 15.5GB | 17.2GB | 22.3GB | 30.2GB | 48.2GB | 72.4GB |

Avec la quantification du cache KV, le modèle peut économiser plus de mémoire lorsqu'il génère des séquences plus longues (`sl`, se référant au nombre de jetons générés) à l'étape de l'inférence.

| Utilisation du cache KV | sl=512 | sl=1024 | sl=2048 | sl=4096 | sl=8192 |
|-------------------------|:------:|:-------:|:-------:|:-------:|:-------:|
| Non                     | 15.2GB | 16.3GB  | 17.6GB  | 19.5GB  | 23.2GB  |
| Oui                     | 15.0GB | 15.5GB  | 15.8GB  | 16.6GB  | 17.6GB  |

Le modèle avec quantification du cache KV convertira le format de `layer_past` de float à int8, et pendant ce temps le `layer-past` quantifié stockera également les paramètres de quantification.

Les étapes spécifiques sont les suivantes:

1. Quantifier clé/valeur
```
    qv,scale,zero_point=quantize_cache_v(v)
```
2. Stocker dans `layer_past`

Voici le format de `layer_past` quantifié:
```
    layer_past=((q_key,key_scale,key_zero_point),
                (q_value,value_scale,value_zero_point))
```

Le format original de `layer_past` est illustré ci-dessous:
```
    layer_past=(key,value)
```

Si vous souhaitez utiliser l'attention KV qui est quantifiée, vous pouvez utiliser l'opération de déquantification pour reconvertir la clé/valeur int8 au format float comme suit 
vous pouvez utiliser l'opération de déquantification pour reconvertir la clé/valeur int8 au format float comme suit:
```
    v=dequantize_cache_torch(qv,scale,zero_point)
```
<br>


## Performance de l'inférence

Cette section fournit les statistiques de vitesse et de mémoire des modèles dans différentes précisions. Le profilage de la vitesse et de la mémoire est effectué à l'aide de [ce script] (https://qianwen-res.oss-cn-beijing.aliyuncs.com/profile.py).

Nous avons mesuré la vitesse moyenne d'inférence (tokens/s) et l'utilisation de la mémoire GPU pour générer 2048 avec les modèles en BF16, Int8 et Int4.

<table>
    <tr>
        <td>Model Size</td>
        <td>Quantization</td>
        <td>Speed (Tokens/s)</td>
        <td>GPU Memory Usage</td>
    </tr>
    <tr>
        <td rowspan="3">1.8B</td>
        <td>BF16</td>
        <td>54.09</td>
        <td>4.23GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>55.56</td>
        <td>3.48GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>71.07</td>
        <td>2.91GB</td>
    </tr>
    <tr>
        <td rowspan="3">7B</td>
        <td>BF16</td>
        <td>40.93</td>
        <td>16.99GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>37.47</td>
        <td>11.20GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>50.09</td>
        <td>8.21GB</td>
    </tr>
    <tr>
        <td rowspan="3">14B</td>
        <td>BF16</td>
        <td>32.22</td>
        <td>30.15GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>29.28</td>
        <td>18.81GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>38.72</td>
        <td>13.01GB</td>
    </tr>
    <tr>
        <td rowspan="3">72B</td>
        <td>BF16</td>
        <td>8.48</td>
        <td>144.69GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>9.05</td>
        <td>81.27GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>11.32</td>
        <td>48.86GB</td>
    </tr>
    <tr>
        <td>72B + vLLM</td>
        <td>BF16</td>
        <td>17.60</td>
        <td>2xA100</td>
    </tr>
</table>

Le profilage s'exécute sur un seul GPU A100-SXM4-80G (sauf si 2xA100 est mentionné) avec PyTorch 2.0.1, CUDA 11.8, et Flash-Attention 2. (72B + vLLM utilise PyTorch 2.1.0 et Cuda 11.8.) La vitesse d'inférence est calculée en moyenne sur les tokens encodés et générés.

Note : La vitesse de génération des modèles Int4/Int8 mentionnés ci-dessus est fournie par la bibliothèque autogptq. La vitesse actuelle du modèle chargé en utilisant ``AutoModelForCausalLM.from_pretrained`` sera environ 20% plus lente. Nous avons signalé ce problème à l'équipe HuggingFace et nous le mettrons à jour rapidement si une solution est disponible.

Nous mesurons également la vitesse d'inférence et l'utilisation de la mémoire du GPU avec différents paramètres de contexte et de longueur de génération, version Flash-Attention. Vous pouvez trouver les résultats dans les cartes modèles correspondantes sur Hugging Face ou ModelScope.


## Finetuning

### Utilisation
Nous fournissons maintenant le script d'entraînement officiel, `finetune.py`, pour que les utilisateurs puissent ajuster le modèle pré-entraîné pour les applications en aval de manière simple. De plus, nous fournissons des scripts shell pour lancer le finetune sans soucis. Ce script prend en charge l'entraînement avec [DeepSpeed](https://github.com/microsoft/DeepSpeed) et [FSDP](https://engineering.fb.com/2021/07/15/open-source/fsdp/). Les scripts que nous fournissons utilisent DeepSpeed (Note : il peut y avoir des conflits avec la dernière version de pydantic et vous devriez utiliser make sure `pydantic<2.0`) et Peft. Vous pouvez les installer en procédant comme suit :
```bash
pip install "peft<0.8.0" deepspeed
```

Pour préparer vos données d'entraînement, vous devez rassembler tous les échantillons dans une liste et l'enregistrer dans un fichier json. Chaque échantillon est un dictionnaire composé d'un identifiant et d'une liste de conversation. Voici un exemple simple de liste avec 1 échantillon :
```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "你好"
      },
      {
        "from": "assistant",
        "value": "我是一个语言模型，我叫通义千问。"
      }
    ]
  }
]
```

Après la préparation des données, vous pouvez utiliser les scripts shell fournis pour lancer le finetuning. N'oubliez pas de spécifier le chemin d'accès au fichier de données, `$DATA`.

Les scripts de finetuning vous permettent d'effectuer les opérations suivantes
- Finetuning de tous les paramètres
- LoRA
- Q-LoRA

Le finetuning de tous les paramètres nécessite la mise à jour de tous les paramètres au cours de l'ensemble du processus de formation. Pour lancer votre formation, exécutez le script suivant:

```bash
# Distributed training. We do not provide single-GPU training script as the insufficient GPU memory will break down the training.
bash finetune/finetune_ds.sh
```

N'oubliez pas de spécifier le nom ou le chemin d'accès au modèle, le chemin d'accès aux données, ainsi que le répertoire de sortie dans les scripts shell. Une autre chose à noter est que nous utilisons DeepSpeed ZeRO 3 dans ce script. Si vous voulez faire des changements, il suffit de supprimer l'argument `--deepspeed` ou de faire des changements dans le fichier json de configuration de DeepSpeed en fonction de vos besoins. De plus, ce script supporte l'entraînement en précision mixte, et donc vous pouvez utiliser `--bf16 True` ou `--fp16 True`. N'oubliez pas d'utiliser DeepSpeed lorsque vous utilisez fp16 en raison de l'entraînement de précision mixte. Empiriquement, nous vous conseillons d'utiliser bf16 pour rendre votre apprentissage cohérent avec notre pré-entraînement et notre alignement si votre machine supporte bf16, et nous l'utilisons donc par défaut.

Pour exécuter LoRA, utilisez un autre script à exécuter comme indiqué ci-dessous. Avant de commencer, assurez-vous que vous avez installé `peft`. Vous devez spécifier les chemins d'accès à votre modèle, à vos données et à vos résultats. Nous vous conseillons d'utiliser des chemins absolus pour votre modèle pré-entraîné. En effet, LoRA ne sauvegarde que l'adaptateur et le chemin absolu dans le fichier json de configuration de l'adaptateur est utilisé pour trouver le modèle pré-entraîné à charger. De plus, ce script supporte à la fois bf16 et fp16.

```bash
# Single GPU training
bash finetune/finetune_lora_single_gpu.sh
# Distributed training
bash finetune/finetune_lora_ds.sh
```

Par rapport au finetuning de tous les paramètres, LoRA ([paper](https://arxiv.org/abs/2106.09685)) ne met à jour que les paramètres des couches d'adaptateurs, tout en gelant les couches originales du grand modèle de langage. Cela permet de réduire considérablement les coûts de mémoire et donc les coûts de calcul.

Notez que si vous utilisez LoRA pour affiner le modèle linguistique de base, par exemple Qwen-7B, au lieu des modèles de chat, par exemple Qwen-7B-Chat, le script change automatiquement l'intégration et la couche de sortie en tant que paramètres entraînables. En effet, le modèle linguistique de base n'a aucune connaissance des jetons spéciaux apportés par le format ChatML. Ces couches doivent donc être mises à jour pour que le modèle comprenne et prédise les jetons. En d'autres termes, si votre formation apporte des tokens spéciaux dans LoRA, vous devez définir les couches comme des paramètres entraînables en définissant `modules_to_save` à l'intérieur du code. De plus, si ces paramètres sont entraînables, il n'est pas possible d'utiliser ZeRO 3, et c'est pourquoi nous utilisons ZeRO 2 par défaut dans le script. Si vous n'avez pas de nouveaux paramètres entraînables, vous pouvez passer à ZeRO 3 en modifiant le fichier de configuration de DeepSpeed. En outre, nous constatons qu'il existe un écart important entre l'empreinte mémoire de LoRA avec et sans ces paramètres d'entraînement. Par conséquent, si vous avez des problèmes de mémoire, nous vous conseillons d'affiner les modèles de chat de LoRA. Consultez le profil ci-dessous pour plus d'informations.

Si vous souffrez toujours d'un manque de mémoire, vous pouvez envisager Q-LoRA ([paper](https://arxiv.org/abs/2305.14314)), qui utilise le modèle de langage quantifié et d'autres techniques telles que l'attention paginée pour réduire encore les coûts de mémoire.

Note : pour exécuter l'entraînement Q-LoRA sur un seul GPU, vous pouvez avoir besoin d'installer `mpi4py` via `pip` ou `conda`.

Pour lancer Q-LoRA, exécutez directement le script suivant :

```bash
# Single GPU training
bash finetune/finetune_qlora_single_gpu.sh
# Distributed training
bash finetune/finetune_qlora_ds.sh
```

Pour Q-LoRA, nous vous conseillons de charger le modèle quantifié que nous fournissons, par exemple Qwen-7B-Chat-Int4. Vous **NE DEVRIEZ PAS** utiliser les modèles bf16. Contrairement au finetuning de tous les paramètres et à la LoRA, seul le modèle fp16 est pris en charge pour la Q-LoRA. Pour l'entraînement sur un seul GPU, nous devons utiliser DeepSpeed pour l'entraînement en précision mixte en raison de notre observation des erreurs causées par torch amp. En outre, pour Q-LoRA, les problèmes avec les jetons spéciaux dans LoRA existent toujours. Cependant, comme nous ne fournissons que les modèles Int4 pour les modèles de chat, ce qui signifie que le modèle de langage a appris les tokens spéciaux du format ChatML, vous n'avez pas à vous soucier des couches. Notez que les couches du modèle Int4 ne doivent pas être entraînables, et donc si vous introduisez des tokens spéciaux dans votre entraînement, Q-LoRA risque de ne pas fonctionner.

> NOTE : Veuillez noter qu'en raison des mécanismes internes de Hugging Face, certains fichiers non-Python (par exemple, `*.cpp` et `*.cu`) 
> peuvent être absents du point de contrôle sauvegardé. Vous devrez peut-être les copier manuellement dans le répertoire contenant les autres fichiers.

Contrairement au finetuning des paramètres complets, l'entraînement de LoRA et de Q-LoRA n'enregistre que les paramètres de l'adaptateur. Supposons que votre entraînement commence à partir de Qwen-7B, vous pouvez charger le modèle finalisé pour l'inférence comme indiqué ci-dessous:

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()
```

Si vous souhaitez fusionner les adaptateurs et enregistrer le modèle affiné en tant que modèle autonome (vous ne pouvez le faire qu'avec LoRA, et vous **NE POUVEZ PAS** fusionner les paramètres de Q-LoRA), vous pouvez exécuter les codes suivants :

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()

merged_model = model.merge_and_unload()
# max_shard_size and safe serialization are not necessary. 
# They respectively work for sharding checkpoint and save the model to safetensors
merged_model.save_pretrained(new_model_directory, max_shard_size="2048MB", safe_serialization=True)
```

Note : Pour l'entraînement multi-GPU, vous devez spécifier les hyperparamètres appropriés pour l'entraînement distribué en fonction de votre machine. De plus, nous vous conseillons de spécifier votre longueur maximale de séquence avec l'argument `--model_max_length`, en fonction de votre considération des données, de l'empreinte mémoire, et de la vitesse d'apprentissage.


### Profilage de la mémoire et de la vitesse
Nous profilons la mémoire du GPU et la vitesse d'apprentissage de LoRA (LoRA (emb) se réfère à l'apprentissage de la couche d'intégration et de sortie, tandis que LoRA n'a pas de couche d'intégration et de sortie pouvant être entraînée) et de Q-LoRA dans la configuration de l'apprentissage sur un seul GPU. Dans ce test, nous expérimentons sur un seul GPU A100-SXM4-80G, et nous utilisons CUDA 11.8 et Pytorch 2.0. Flash attention 2 est appliqué. Nous utilisons uniformément une taille de lot de 1 et une accumulation de gradient de 8. Nous profilons la mémoire (GB) et la vitesse (s/iter) des entrées de différentes longueurs, à savoir 256, 512, 1024, 2048, 4096, et 8192. Nous présentons également les statistiques du réglage fin de tous les paramètres avec Qwen-7B sur 2 GPU A100. Nous ne présentons que les statistiques de 256, 512 et 1024 jetons en raison de la limitation de la mémoire du GPU. 

Pour Qwen-72B, nous expérimentons de deux manières : 1) Lora fintuning + DeepSpeed ZeRO 3 sur 4 GPU A100-SXM4-80G et 2) QLora (int4) fintuning sur un seul GPU A100-SXM4-80G. Notez que l'OOM se produit sur 4 GPUs A100-SXM4-80G à la fois avec le réglage fin LoRA (emb) et le réglage fin LoRA sans Deepspeed ZeRO 3 (vous pouvez passer `--deepspeed finetune/ds_config_zero3.json` à [`finetune/finetune_lora_ds.sh`](finetune/finetune_lora_ds.sh) afin d'activer DeepSpeed ZeRO 3).

Les statistiques sont listées ci-dessous :

<table>
    <tr>
      <th rowspan="2">Model Size</th><th rowspan="2">Method</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">256</th><th align="center">512</th><th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th>
    </tr>
    </tr>
    </tr>
		<tr>
        <th rowspan="4">1.8B</th><td>LoRA</td><td align="center">6.7G / 1.0s/it</td><td align="center">7.4G / 1.0s/it</td><td align="center">8.4G / 1.1s/it</td><td align="center">11.0G / 1.7s/it</td><td align="center">16.2G / 3.3s/it</td><td align="center">21.8G / 6.8s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td><td align="center">13.7G / 1.0s/it</td><td align="center">14.0G / 1.0s/it</td><td align="center">14.0G / 1.1s/it</td><td align="center">15.1G / 1.8s/it</td><td align="center">19.7G / 3.4s/it</td><td align="center">27.7G / 7.0s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">5.8G / 1.4s/it</td><td align="center">6.0G / 1.4s/it</td><td align="center">6.6G / 1.4s/it</td><td align="center">7.8G / 2.0s/it</td><td align="center">10.2G / 3.4s/it</td><td align="center">15.8G / 6.5s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td><td align="center">43.5G / 2.1s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.3s/it</td><td align="center">47.1G / 2.8s/it</td><td align="center">48.3G / 5.6s/it</td>
    </tr>
    <tr>
        <th rowspan="4">7B</th><td>LoRA</td><td align="center">20.1G / 1.2s/it</td><td align="center">20.4G / 1.5s/it</td><td align="center">21.5G / 2.8s/it</td><td align="center">23.8G / 5.2s/it</td><td align="center">29.7G / 10.1s/it</td><td align="center">36.6G / 21.3s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td><td align="center">33.7G / 1.4s/it</td><td align="center">34.1G / 1.6s/it</td><td align="center">35.2G / 2.9s/it</td><td align="center">35.1G / 5.3s/it</td><td align="center">39.2G / 10.3s/it</td><td align="center">48.5G / 21.7s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">11.5G / 3.0s/it</td><td align="center">11.5G / 3.0s/it</td><td align="center">12.3G / 3.5s/it</td><td align="center">13.9G / 7.0s/it</td><td align="center">16.9G / 11.6s/it</td><td align="center">23.5G / 22.3s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td><td align="center">139.2G / 4.0s/it</td><td align="center">148.0G / 4.0s/it</td><td align="center">162.0G / 4.5s/it</td><td align="center">-</td><td align="center">-</td><td align="center">-</td>
    </tr>
    <tr>
        <th rowspan="3">14B</th><td>LoRA</td><td align="center">34.6G / 1.6s/it</td><td align="center">35.1G / 2.4s/it</td><td align="center">35.3G / 4.4s/it</td><td align="center">37.4G / 8.4s/it</td><td align="center">42.5G / 17.0s/it</td><td align="center">55.2G / 36.0s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td><td align="center">51.2 / 1.7s/it</td><td align="center">51.1G / 2.6s/it</td><td align="center">51.5G / 4.6s/it</td><td align="center">54.1G / 8.6s/it</td><td align="center">56.8G / 17.2s/it</td><td align="center">67.7G / 36.3s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">18.7G / 5.3s/it</td><td align="center">18.4G / 6.3s/it</td><td align="center">18.9G / 8.2s/it</td><td align="center">19.9G / 11.8s/it</td><td align="center">23.0G / 20.1s/it</td><td align="center">27.9G / 38.3s/it</td>
    </tr>
	<tr>
        <th rowspan="2">72B</th><td>LoRA + Deepspeed Zero3</td><td align="center">215.4G / 17.6s/it</td><td align="center">217.7G / 20.5s/it</td><td align="center">222.6G / 29.4s/it</td><td align="center">228.8G / 45.7s/it</td><td align="center">249.0G / 83.4s/it</td><td align="center">289.2G / 161.5s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">61.4G / 27.4s/it</td><td align="center">61.4G / 31.5s/it</td><td align="center">62.9G / 41.4s/it</td><td align="center">64.1G / 59.5s/it</td><td align="center">68.0G / 97.7s/it</td><td align="center">75.6G / 179.8s/it</td>
    </tr>
</table>
<br>

## Déploiement

### vLLM 
Pour le déploiement et l'inférence rapide, nous suggérons d'utiliser vLLM avec FastChat. Installez d'abord les paquets:
```bash
pip install vllm
pip install "fschat[model_worker,webui]"
```
Ou vous pouvez les installer à partir des sources par `git clone` et `pip install -e .`. Nous vous conseillons de lire leurs documents si vous rencontrez des problèmes lors de l'installation.

Pour faire fonctionner Qwen avec vLLM et FastChat, vous devez d'abord lancer un contrôleur par:
```bash
python -m fastchat.serve.controller
```

Ensuite, vous pouvez lancer le travailleur de modèle, ce qui signifie charger votre modèle pour l'inférence. Pour l'inférence sur un seul GPU, vous pouvez directement lancer:
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code
```
Cependant, si vous souhaitez exécuter le modèle sur plusieurs GPU pour une inférence plus rapide ou une mémoire plus importante, vous pouvez utiliser le parallélisme tensoriel pris en charge par vLLM. Supposons que vous exécutiez le modèle sur 4 GPU, la commande est présentée ci-dessous:
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4
```

Après avoir lancé votre model worker, vous pouvez lancer :

* Démonstration de l'interface web
```bash
python -m fastchat.serve.gradio_web_server
```

* API OpenAI
```bash
python -m fastchat.serve.openai_api_server --host localhost --port 8000
```

Cependant, si vous avez des difficultés à utiliser vLLM et FastChat, vous pouvez essayer nos méthodes les plus simples pour déployer une démo web, une démo CLI et une API.

### Interface Web

Nous fournissons du code pour que les utilisateurs puissent construire une démo d'interface web (merci à @wysaid). Avant de commencer, assurez-vous d'installer les paquets suivants:

```
pip install -r requirements_web_demo.txt
```

Exécutez ensuite la commande ci-dessous et cliquez sur le lien généré:

```bash
python web_demo.py
```

<p align="center">
    <br>
    <img src="assets/web_demo.gif" width="600" />
    <br>
<p>

### Démo CLI

Nous fournissons un exemple de démonstration CLI dans `cli_demo.py`, qui prend en charge la sortie en continu pour la génération. Les utilisateurs peuvent interagir avec Qwen-7B-Chat en saisissant des invites, et le modèle renvoie les sorties du modèle en mode streaming. Exécutez la commande ci-dessous:

```bash
python cli_demo.py
```

<p align="center">
    <br>
    <img src="assets/cli_demo.gif" width="600" />
    <br>
<p>
<br>

### API

Nous fournissons des méthodes pour déployer une API locale basée sur l'API OpenAI (merci à @hanpenggit). Avant de commencer, installez les paquets nécessaires:

```bash
pip install fastapi uvicorn "openai<1.0" pydantic sse_starlette
```

Exécutez ensuite la commande pour déployer votre API:

```bash
python openai_api.py
```

Vous pouvez modifier vos arguments, par exemple, `-c` pour le nom ou le chemin du poids, `--cpu-only` pour le déploiement CPU, etc. Si vous rencontrez des problèmes lors du lancement du déploiement de l'API, la mise à jour des paquets vers la dernière version peut probablement les résoudre.

L'utilisation de l'API est simple. Voir l'exemple ci-dessous:

```python
import openai
openai.api_base = "http://localhost:8000/v1"
openai.api_key = "none"

# create a request activating streaming response
for chunk in openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=True 
    # Specifying stop words in streaming output format is not yet supported and is under development.
):
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

# create a request not activating streaming response
response = openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=False,
    stop=[] # You can add custom stop words here, e.g., stop=["Observation:"] for ReAct prompting.
)
print(response.choices[0].message.content)
```

<p align="center">
    <br>
    <img src="assets/openai_api.gif" width="600" />
    <br>
<p>

**Function calling** est aussi supporté (mais seulement quand `stream=False` pour le moment). Voir [l'exemple d'utilisation](examples/function_call_examples.py) ici.
<br><br>


## 🐳 Docker

Pour simplifier le processus de déploiement, nous fournissons des images docker avec des environnements préconstruits : [qwenllm/qwen] (https://hub.docker.com/r/qwenllm/qwen). Il vous suffit d'installer le pilote et de télécharger les fichiers de modèle pour lancer les démonstrations, déployer l'API OpenAI et affiner le modèle.

### Préparation

1. Installez la version correcte du pilote Nvidia en fonction de l'image à utiliser :
  - `qwenllm/qwen:cu117` (**recommandé**): `>= 515.48.07`
  - `qwenllm/qwen:cu114` (w/o flash-attention): `>= 470.82.01`
  - `qwenllm/qwen:cu121`: `>= 530.30.02`
  - `qwenllm/qwen:latest`: même que `qwenllm/qwen:cu117`

2. Installer et configurer [docker](https://docs.docker.com/engine/install/) et [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) :

```bash
# configure docker
sudo systemctl start docker
# test if docker is correctly installed
sudo docker run hello-world

# configure nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
# test if nvidia-container-toolkit is correctly installed
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

3. Téléchargez les checkpoints et les codes du modèle dans votre environnement (voir [ici](#DownloadModel)).

### Déploiement

Nous utilisons ici Qwen-7B-Chat comme exemple. Avant de lancer une démo web ou une API, vous pouvez établir la configuration comme indiqué ci-dessous :

```bash
IMAGE_NAME=qwenllm/qwen:cu117
PORT=8901
CHECKPOINT_PATH=/path/to/Qwen-7B-Chat   # Path to downloaded model checkpoints and codes
```
Les scripts suivants peuvent vous aider à construire :

* API OpenAI
```bash
bash docker/docker_openai_api.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* Interface Web
```bash
bash docker/docker_web_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* Démo CLI
```bash
bash docker/docker_cli_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH}
```

Les commandes ci-dessus téléchargeront automatiquement l'image requise et lanceront une démo d'interface Web en arrière-plan (le service redémarrera automatiquement). Vous pouvez ouvrir `http://localhost:${PORT}` sur l'hôte pour utiliser la démo.

La démo est lancée avec succès si vous obtenez le résultat suivant :

```text
Successfully started web demo. Open '...' to try!
Run `docker logs ...` to check demo status.
Run `docker rm -f ...` to stop and remove the demo.
```

Si vous voulez vérifier le statut de la démo, vous pouvez utiliser `docker logs qwen` pour afficher les résultats.

Vous pouvez utiliser `docker rm -f qwen` pour arrêter le service et supprimer le conteneur.


### Finetuning

La méthode de finetuning utilisant l'image Docker préconstruite est fondamentalement la même que [le chapitre ci-dessus](#Finetuning) (nous avons déjà installé les dépendances dans l'image) :

Voici un exemple de LoRA à une seule GPU :
```bash
IMAGE_NAME=qwenllm/qwen:cu117
CHECKPOINT_PATH=/path/to/Qwen-7B                # Path to downloaded model checkpoints and codes
#CHECKPOINT_PATH=/path/to/Qwen-7B-Chat-Int4     # Path to downloaded model checkpoints and codes (Q-LoRA)
DATA_PATH=/path/to/data/root                    # Prepare finetune data at ${DATA_PATH}/example.json
OUTPUT_PATH=/path/to/output/checkpoint          # Path to finetune outputs

# Use all host devices by default
DEVICE=all
# If you need to specify GPUs for training, set device as follow (NOTE: internal quotation marks cannot be omitted)
#DEVICE='"device=0,1,2,3"'

mkdir -p ${OUTPUT_PATH}

# Single-GPU LoRA finetuning
docker run --gpus ${DEVICE} --rm --name qwen \
    --mount type=bind,source=${CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-7B \
    --mount type=bind,source=${DATA_PATH},target=/data/shared/Qwen/data \
    --mount type=bind,source=${OUTPUT_PATH},target=/data/shared/Qwen/output_qwen \
    --shm-size=2gb \
    -it ${IMAGE_NAME} \
    bash finetune/finetune_lora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B/ -d /data/shared/Qwen/data/example.json
```

Pour faire un changement vers Q-LoRA à GPU unique par exemple, il suffit de modifier la commande bash à l'intérieur de `docker run` :
```bash
bash finetune/finetune_qlora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B-Chat-Int4/ -d /data/shared/Qwen/data/example.json
```
<br>

## 🔥 Invite du système
Qwen-1.8-Chat et Qwen-72B-Chat ont été entièrement formés à diverses invites de système avec plusieurs séries d'interactions complexes, de sorte qu'ils peuvent suivre une variété d'invites de système et réaliser la personnalisation du modèle dans le contexte, améliorant ainsi l'évolutivité de Qwen-chat.

Grâce aux messages-guides du système, Qwen-Chat peut **jouer avec enthousiasme**, **transférer le style de langage**, **fixer des tâches** et **fixer des comportements**.

![](assets/system_prompt_language_style.png)

![](assets/system_prompt_role_play_en.png)

Pour plus d'informations, veuillez vous référer à la [documentation d'exemple](examples/system_prompt.md).


## Utilisation des outils

Qwen-Chat a été optimisé pour l'utilisation d'outils et les capacités d'appel de fonctions. Les utilisateurs peuvent développer des agents, des applications LangChain, et même augmenter Qwen avec un Code Interpreter.

Nous fournissons une documentation sur la manière d'implémenter les appels d'outils basés sur le principe de ReAct Prompting, veuillez vous référer à [l'exemple ReAct](examples/react_prompt.md). Sur la base de ce principe, nous fournissons un support pour function calling dans [openai_api.py](openai_api.py).

Nous avons testé les capacités d'appel d'outil du modèle sur notre benchmark d'évaluation chinois à source ouverte et nous avons constaté que Qwen-Chat obtient systématiquement de bons résultats:

<table>
    <tr>
        <th colspan="4" align="center">Chinese Tool-Use Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th align="center">Model</th><th align="center">Tool Selection (Acc.↑)</th><th align="center">Tool Input (Rouge-L↑)</th><th align="center">False Positive Error↓</th>
    </tr>
    <tr>
        <td>GPT-4</td><td align="center">98.0%</td><td align="center">0.953</td><td align="center">23.9%</td>
    </tr>
    <tr>
        <td>GPT-3.5</td><td align="center">74.5%</td><td align="center">0.807</td><td align="center">80.6%</td>
    </tr>
    <tr>
        <td>Qwen-1_8B-Chat</td><td align="center">85.0%</td><td align="center">0.839</td><td align="center">27.6%</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td><td align="center">95.5%</td><td align="center">0.900</td><td align="center">11.6%</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td><td align="center">96.9%</td><td align="center">0.917</td><td align="center">5.6%</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td><td align="center">98.2%</td><td align="center">0.927</td><td align="center">1.1%</td>
    </tr>
</table>

Pour évaluer la capacité de Qwen à utiliser l'interpréteur de code Python pour des tâches telles que la résolution de problèmes mathématiques, la visualisation de données et d'autres tâches générales telles que la manipulation de fichiers et l'exploration du Web, nous avons créé et mis en libre accès un test de référence spécialement conçu pour évaluer ces capacités. Vous pouvez trouver le benchmark sur ce [lien](https://github.com/QwenLM/Qwen-Agent/tree/main/benchmark).

Nous avons observé que Qwen est performant en termes d'exécutabilité du code et de précision des résultats lors de la génération du code:

<table>
    <tr>
        <th colspan="5" align="center">Code Interpreter Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th rowspan="2" align="center">Model</th>
        <th colspan="3" align="center">Accuracy of Code Execution Results (%)</th>
        <th colspan="1" align="center">Executable Rate of Code (%)</th>
    </tr>
    <tr>
        <th align="center">Math↑</th><th align="center">Visualization-Hard↑</th><th align="center">Visualization-Easy↑</th><th align="center">General↑</th>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td align="center">82.8</td>
        <td align="center">66.7</td>
        <td align="center">60.8</td>
        <td align="center">82.8</td>
    </tr>
    <tr>
        <td>GPT-3.5</td>
        <td align="center">47.3</td>
        <td align="center">33.3</td>
        <td align="center">55.7</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>LLaMA2-13B-Chat</td>
        <td align="center">8.3</td>
        <td align="center">1.2</td>
        <td align="center">15.2</td>
        <td align="center">48.3</td>
    </tr>
    <tr>
        <td>CodeLLaMA-13B-Instruct</td>
        <td align="center">28.2</td>
        <td align="center">15.5</td>
        <td align="center">21.5</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>InternLM-20B-Chat</td>
        <td align="center">34.6</td>
        <td align="center">10.7</td>
        <td align="center">25.1</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>ChatGLM3-6B</td>
        <td align="center">54.2</td>
        <td align="center">4.8</td>
        <td align="center">15.2</td>
        <td align="center">67.1</td>
    </tr>
    <tr>
        <td>Qwen-1.8B-Chat</td>
        <td align="center">25.6</td>
        <td align="center">21.4</td>
        <td align="center">22.8</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td>
        <td align="center">41.9</td>
        <td align="center">23.8</td>
        <td align="center">38.0</td>
        <td align="center">67.2</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td>
        <td align="center">58.4</td>
        <td align="center">31.0</td>
        <td align="center">45.6</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td>
        <td align="center">72.7</td>
        <td align="center">41.7</td>
        <td align="center">43.0</td>
        <td align="center">82.8</td>
    </tr>
</table>

<p align="center">
    <br>
    <img src="assets/code_interpreter_showcase_001.jpg" />
    <br>
<p>

<br>

## Compréhension du Contexte Long

Pour augmenter la longueur du contexte et éliminer le goulot d'étranglement que constitue la longueur de la séquence d'entraînement, nous introduisons plusieurs techniques, notamment l'interpolation tenant compte des NTK, l'attention par fenêtre et la mise à l'échelle de l'attention LogN, afin d'augmenter la longueur du contexte de Qwen-14B de 2K à plus de 8K tokens, et de Qwen-1.8B/7B de 8K à 32K tokens. 

Pour Qwen-72B, nous adaptons RoPE à des contextes plus longs avec une base rotative plus importante. Qwen-72B prend en charge la longueur de contexte maximale de 32K tokens.

Nous menons des expériences de modélisation du langage sur l'ensemble de données arXiv avec l'évaluation PPL et nous constatons que Qwen peut atteindre des performances exceptionnelles dans le scénario d'un contexte long. Les résultats sont présentés ci-dessous :

<table>
    <tr>
        <th rowspan="2">Model</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th><th align="center">16384</th><th align="center">32768</th>
    </tr>
     <tr>
        <td>Qwen-7B (original)</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">39.35</td><td align="center">469.81</td><td align="center">2645.09</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.59</td><td align="center">3.66</td><td align="center">5.71</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.58</td><td align="center">3.56</td><td align="center">4.62</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.58</td><td align="center">3.49</td><td align="center">4.32</td><td align="center">-</td>
    </tr>
    <tr>
    <tr>
        <td>Qwen-1.8B</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.13</b></td><td align="center"><b>3.89</b></td><td align="center">17.42</td><td align="center">433.85</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.14</b></td><td align="center"><b>3.93</b></td><td align="center"><b>3.82</b></td><td align="center"><b>3.83</b></td>
    </tr>
    <tr>
        <td>Qwen-7B</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.31</b></td><td align="center">7.27</td><td align="center">181.49</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.33</b></td><td align="center"><b>3.22</b></td><td align="center"><b>3.17</b></td>
    </tr>
    <tr>
        <td>Qwen-14B</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center">22.79</td><td align="center">334.65</td><td align="center">3168.35</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center"><b>3.29</b></td><td align="center"><b>3.18</b></td><td align="center">3.42</td><td align="center">-</td>
    </tr>
    <tr>
        <td>Qwen-72B</td><td align="center"><b>-</b></td><td align="center"><b>-</b></td><td align="center">-</td><td align="center"><b>2.83</b></td><td align="center"><b>2.73</b></td><td align="center"><b>2.72</b></td>
    </tr>
    </tr>
</table>

En outre, pour vérifier la capacité de Qwen-72B-Chat à comprendre des textes longs, nous l'avons testé sur [L-Eval] (https://arxiv.org/abs/2307.11088) (tâches fermées). Les résultats sont les suivants :

| Model             | Input Length | Average   |  Coursera  |    GSM     |   QuALITY  |    TOEFL   |   CodeU    |  SFcition  |
|:------------------|:------------:|:---------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| ChatGPT-3.5-16k   |     16K      |   60.73   | **63.51**  | **84.00**  |   61.38    |    78.43   | **12.22**  |    64.84   |
| **Qwen-72B-Chat** |     32K      | **62.30** |   58.13    |   76.00    | **77.22**  |  **86.24** |    6.66    |  **69.53** |

Nous avons réalisé l'expérience de "l'aiguille dans une botte de foin" (l'idée vient de [@Greg Kamradt](https://twitter.com/GregKamradt/status/1727018183608193393)) pour tester si le modèle peut récupérer des informations à différentes positions dans les entrées de différentes longueurs, le résultat est le suivant :

![](assets/qwen_72b_needle_in_a_haystack.png)

Les résultats ci-dessus montrent que Qwen-72B-Chat peut récupérer avec précision des informations placées dans différentes positions dans une longueur d'entrée de 32K, ce qui prouve ses excellentes capacités de compréhension de textes longs.


## Tokenizer

Notre tokenizer basé sur tiktoken est différent des autres tokenizers, par exemple le tokenizer sentencepiece. Vous devez faire attention aux tokens spéciaux, en particulier lors de la mise au point. Pour des informations plus détaillées sur le tokenizer et son utilisation dans le cadre du finetuning, veuillez vous référer à la [documentation](tokenization_note.md).
<br><br>

## Reproduction

Pour reproduire les performances du modèle sur des ensembles de données de référence, nous fournissons des scripts permettant de reproduire les résultats. Consultez [eval/EVALUATION.md](eval/EVALUATION.md) pour plus d'informations. Notez que la reproduction peut entraîner de légères différences par rapport à nos résultats.
<br><br>

## FAQ

Si vous rencontrez des problèmes, veuillez vous référer à la [FAQ](FAQ.md) et aux problèmes pour trouver une solution avant de lancer un nouveau problème.
<br><br>

## Citation
Si vous trouvez notre travail utile, n'hésitez pas à nous citer.

```
@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
}
```
<br>

## Accord de Licence

Le code source fourni à l'adresse <https://github.com/QwenLM/Qwen> est soumis à la licence [Apache 2.0 License](./LICENSE) qui se trouve dans le répertoire racine.

Les chercheurs et les développeurs sont libres d'utiliser les codes et les poids des modèles de Qwen et de Qwen-Chat. Pour leur utilisation commerciale, veuillez consulter l'accord de licence accompagnant chaque modèle.

- Qwen-72B, Qwen-14B et Qwen-7B sont sous licence [Tongyi Qianwen LICENSE AGREEMENT](./Tongyi%20Qianwen%20LICENSE%20AGREEMENT) que l'on peut trouver dans les dépôts HuggingFace et ModelScope correspondants. Pour une utilisation commerciale, veuillez remplir le formulaire ([72B](https://dashscope.console.aliyun.com/openModelApply/Qwen-72B-Chat), [14B](https://dashscope.console.aliyun.com/openModelApply/Qwen-14B-Chat), et [7B](https://dashscope.console.aliyun.com/openModelApply/qianwen)) pour en faire la demande.

- Qwen-1.8B est sous licence [Tongyi Qianwen RESEARCH LICENSE AGREEMENT](./Tongyi%20Qianwen%20RESEARCH%20LICENSE%20AGREEMENT) qui peut être trouvé dans les dépôts HuggingFace et ModelScope correspondants. Pour une utilisation commerciale, veuillez nous contacter.
<br><br>

## Contactez-nous

Si vous souhaitez laisser un message à notre équipe de recherche ou à notre équipe produit, rejoignez nos groupes Discord ou WeChat! N'hésitez pas non plus à envoyer un courriel à qianwen_opensource@alibabacloud.com.

```

## File: `README_JA.md`
```markdown
<p align="left">
    <a href="README_CN.md">中文</a>&nbsp ｜ &nbsp<a href="README.md">English</a>&nbsp ｜ &nbsp日本語 ｜ &nbsp<a href="README_FR.md">Français</a> ｜ &nbsp<a href="README_ES.md">Español</a>
</p>
<br><br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/logo_qwen.jpg" width="400"/>
<p>
<br>

<p align="center">
        🤗 <a href="https://huggingface.co/Qwen">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/qwen">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2309.16609">Paper</a> &nbsp&nbsp ｜ &nbsp&nbsp🖥️ <a href="https://modelscope.cn/studios/qwen/Qwen-72B-Chat-Demo/summary">Demo</a>
<br>
<a href="assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp<a href="https://discord.gg/z3GAxXZ9Ce">Discord</a>&nbsp&nbsp ｜  &nbsp&nbsp<a href="https://dashscope.aliyun.com">API</a> 
</p>
<br><br>

> [!Important]
> Qwen2 が登場しました！[QwenLM/Qwen2](https://github.com/QwenLM/Qwen2) のフォローと、そこであなたの体験を共有することをお待ちしております。
>
> このリポジトリ ([QwenLM/Qwen](https://github.com/QwenLM/Qwen)) は、コードベースに大幅な違いがあるため、今後アクティブにメンテナンスされなくなります。
<br>

|     |                                                              Qwen-Chat                                                               |                                                                Qwen-Chat (Int4)                                                                |                        Qwen-Chat (Int8)                         |                                                            Qwen                                                            |
|-----|:------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 1.8B  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-1_8B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-1_8B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-1_8B">🤗</a>  |
| 7B  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int4">🤗</a>  | <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B-Chat-Int8">🤗</a>  |  <a href="https://modelscope.cn/models/qwen/Qwen-7B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-7B">🤗</a>  |
| 14B | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-14B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-14B">🤗</a> |
| 72B | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int4/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int4">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B-Chat-Int8/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B-Chat-Int8">🤗</a> | <a href="https://modelscope.cn/models/qwen/Qwen-72B/summary">🤖</a>  <a href="https://huggingface.co/Qwen/Qwen-72B">🤗</a> |



**Qwen-1.8B**、**Qwen-7B**、**Qwen-14B**、**Qwen-72B**の基本言語モデルである**Qwen**と、**Qwen-1.8B-Chat**、**Qwen-7B-Chat**、**Qwen-14B-Chat**、**Qwen-72B-Chat**のチャットモデルである**Qwen-Chat**をオープンソース化します。上の表にリンクがあります。リンクをクリックして、モデルカードをご確認ください。また、**[テクニカルレポート](https://arxiv.org/abs/2309.16609)**も公開しています。論文リンクをクリックしてご覧ください！

簡単に説明すると、私たちは、ドメインや言語（中国語と英語を中心に）などを幅広くカバーする最大3兆トークンの多言語データに対して安定的に事前学習された強力なベース言語モデルを持っています。これらのモデルは、ベンチマークデータセットにおいて競争力のあるパフォーマンスを達成することができます。さらに、SFTとRLHFに基づく人間の嗜好に沿ったチャットモデル（まだリリースされていません）があり、チャット、コンテンツ作成、情報抽出、要約、翻訳、コーディング、数学の問題を解くなどが可能で、ツールを使ったり、エージェントとして遊んだり、コードインタプリタとして遊んだりすることもできます。


| モデル       |   発行日    | コンテキストの最大長 | システムプロンプトの強化 | 预训练されたトークンの数 | Finetuning（Q-Lora）の最小GPUメモリ使用量 | 2048トークン生成時の最小GPUメモリ使用量（Int4） | ツールの使用能力 |
|:----------|:--------:|:----------:|:------------:|:------------:|:------------------------------:|:-----------------------------:|:--------:|
| Qwen-1.8B | 23.11.30 |    32K     |      ✅       |     2.2T     |             5.8GB              |             2.9GB             |    ✅     |  
| Qwen-7B   | 23.08.03 |    32K     |      ❎       |     2.4T     |             11.5GB             |             8.2GB             |    ✅     |   
| Qwen-14B  | 23.09.25 |     8K     |      ❎       |     3.0T     |             18.7GB             |            13.0GB             |    ✅     |
| Qwen-72B  | 23.11.30 |    32K     |      ✅       |     3.0T     |             61.4GB             |            48.9GB             |    ✅     |   


このレポでは、それを把握することができる：

* Qwenのクイックスタート。
* 量子化モデルの詳細（使用量、メモリ、推論速度など）。比較のために、BF16モデルの統計も提供します。
* フルパラメーターチューニング、LoRA、Q-LoRAを含む、微調整に関するチュートリアル。
* vLLMとFastChatを例に、デプロイメントについて説明します。
* WebUI、CLIデモなど、デモの構築に関する説明。
* あなたのモデルのためのOpenAIスタイルのAPIを構築する手順。
* ツール使用、エージェント、コードインタプリタの Qwen の詳細。
* ロングコンテクスト理解評価の統計
* ライセンス契約
* ...

また、困ったことがあれば、まずは[FAQ](FAQ.md)を参照してほしい。まだ悩んでいますか？遠慮なく私たちに問題を送ってください（より多くの人が理解できるように、英語で）！私たちを助けたいなら、遠慮なくプルリクエストを送ってください！

私たちとチャットしたいですか？私たちのDiscordまたはWeChatグループへようこそ！
<br><br>

## ニュースとアップデート

* 2023.11.30 🔥 3T トークンで学習し、32k コンテキストをサポートする **Qwen-72B** と **Qwen-72B-Chat** を、 **Qwen-1.8B** と **Qwen-1.8B-Chat** とともに、ModelScope と Hugging Face 上でリリースしました。また、Qwen-72B-ChatとQwen-1.8B-Chatのシステム・プロンプト機能を強化しました。[サンプル・ドキュメント](examples/system_prompt.md)を参照してください。さらに、**Ascend 910** と **Hygon DCU** での推論をサポートしました。詳細は `ascend-support` と `dcu-support` を参照してください。
* 2023.10.17 Int8量子化モデル**Qwen-7B-Chat-Int8**と**Qwen-14B-Chat-Int8**をリリースしました。
* 2023.9.25 🔥 Qwen-14BとQwen-14B-ChatをModelScopeとHugging Faceでリリースしました。[qwen.cpp](https://github.com/QwenLM/qwen.cpp) と [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) もリリースされました。同時に、Qwen-7B と Qwen-7B-Chat も更新しました。Qwen-7B（オリジナル）と比較して、Qwen-7Bはより多くの学習トークンを使用し、2.2Tトークンから2.4Tトークンに増加し、コンテキスト長は2048から8192に拡張された。Qwen-7Bの中国語知識とコーディング能力はさらに向上しています。最新のコードとチェックポイントをお使いください！
* 2023.9.12 Qwen-7Bモデルにおいて、フルパラメーター・ファインチューニング、LoRA、Q-LoRAを含むファインチューニングをサポートしました。
* 2023.8.21 Qwen-7B-Chat 用 Int4 量子化モデル **Qwen-7B-Chat-Int4** をリリースしました。また、ベンチマーク評価においても大きな性能低下は見られませんでした。
* 2023.8.3 ModelScope と Hugging Face 上で **Qwen-7B** と **Qwen-7B-Chat** をリリースしました。また、トレーニングの詳細やモデルの性能など、モデルの詳細については技術メモを提供しています。
<br>

## 性能

Qwenモデルは、MMLU、C-Eval、GSM8K、MATH、HumanEval、MBPP、BBHなど、自然言語理解、数学的問題解決、コーディングなどに関するモデルの能力を評価する一連のベンチマークデータセットにおいて、同様のモデルサイズを持つベースラインモデルを上回る性能を発揮する。Qwen-72Bは全てのタスクでLLaMA2-70Bを上回り、10タスク中7タスクでGPT-3.5を上回った。


<p align="left">
    <img src="assets/radar_72b.jpg" width=600px/>
<p>
<br>

| Model             |   MMLU   |  C-Eval  |  GSM8K   |   MATH   | HumanEval |   MBPP   |   BBH    |  CMMLU   |
|:------------------|:--------:|:--------:|:--------:|:--------:|:---------:|:--------:|:--------:|:--------:|
|                   |  5-shot  |  5-shot  |  8-shot  |  4-shot  |  0-shot   |  3-shot  |  3-shot  |  5-shot  |
| LLaMA2-7B         |   46.8   |   32.5   |   16.7   |   3.3    |   12.8    |   20.8   |   38.2   |   31.8   |
| LLaMA2-13B        |   55.0   |   41.4   |   29.6   |   5.0    |   18.9    |   30.3   |   45.6   |   38.4   |
| LLaMA2-34B        |   62.6   |    -     |   42.2   |   6.2    |   22.6    |   33.0   |   44.1   |    -     |
| ChatGLM2-6B       |   47.9   |   51.7   |   32.4   |   6.5    |     -     |    -     |   33.7   |    -     |
| InternLM-7B       |   51.0   |   53.4   |   31.2   |   6.3    |   10.4    |   14.0   |   37.0   |   51.8   |
| InternLM-20B      |   62.1   |   58.8   |   52.6   |   7.9    |   25.6    |   35.6   |   52.5   |   59.0   |
| Baichuan2-7B      |   54.7   |   56.3   |   24.6   |   5.6    |   18.3    |   24.2   |   41.6   |   57.1   |
| Baichuan2-13B     |   59.5   |   59.0   |   52.8   |   10.1   |   17.1    |   30.2   |   49.0   |   62.0   |
| Yi-34B      	  	  |   76.3   |   81.8   |   67.9   |   15.9   |   26.2    |   38.2   |   66.4   |   82.6   |
| XVERSE-65B      	 |   70.8   |   68.6   |   60.3   |    -     |   26.3    |    -     |    -     |    -     |
| **Qwen-1.8B**     |   45.3   |   56.1   |   32.3   |   2.3    |   15.2    |   14.2   |   22.3   |   52.1   |
| **Qwen-7B**       |   58.2   |   63.5   |   51.7   |   11.6   |   29.9    |   31.6   |   45.0   |   62.2   |
| **Qwen-14B**      |   66.3   |   72.1   |   61.3   |   24.8   |   32.3    |   40.8   |   53.4   |   71.0   |
| **Qwen-72B**      | **77.4** | **83.3** | **78.9** | **35.2** | **35.4**  | **52.2** | **67.7** | **83.6** |


比較されたすべてのモデルについて、公式に報告された結果と[OpenCompass](https://opencompass.org.cn/leaderboard-llm) の間の最高スコアを報告します。

より詳細な実験結果（より多くのベンチマークデータセットでの詳細なモデル性能）や詳細については、[こちら](TODO)をクリックして技術メモを参照してください。
<br><br>

## 必要条件

* python 3.8 以上
* pytorch 1.12 以上、2.0 以上を推奨
* transformers 4.32 以上
* CUDA 11.4 以上を推奨（GPU ユーザー、フラッシュアテンションユーザー向けなど）
<br>

## クイックスタート

以下では、Qwen-Chat と 🤖 ModelScope と 🤗 Transformers の簡単な使用例を示します。

詳しくはセクション["ビルド済みDockerイメージの使用"](#-docker)を参照してください。

Dockerを使用しない場合は、環境のセットアップと必要なパッケージのインストールが済んでいることを確認してください。上記の要件を満たしていることを確認してから、依存するライブラリをインストールしてください。

```bash
pip install -r requirements.txt
```

お使いのデバイスが fp16 または bf16 をサポートしている場合、[flash-attention](https://github.com/Dao-AILab/flash-attention) （flash attention 2に対応しました）をインストールすることで、より高い効率とメモリ使用量を抑えることができます。(**flash-attention はオプションであり、インストールしなくてもプロジェクトは正常に実行できます**)

```bash
git clone https://github.com/Dao-AILab/flash-attention
cd flash-attention && pip install .
# 以下はオプションです。インストールに時間がかかる場合があります。
# pip install csrc/layer_norm
# flash-attn のバージョンが 2.1.1 以降の場合、以下は必要ありません。
# pip install csrc/rotary
```

これで ModelScope か Transformers で始めることができます。

### 🤗 Transformers

Qwen-Chat を推論に使用するには、以下のように数行のコードを入力するだけです。Qwen/Qwen-7B-Chat "や "Qwen/Qwen-14B-Chat "のように、正しいモデル名やパスを渡すことを忘れないでください。**最新のコードを使用していることを確認してください。**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names："Qwen/Qwen-7B-Chat"、"Qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# bf16 を使用
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
# fp16 を使用
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
# CPU のみ使用
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
# オートモードを使用すると、デバイスに応じて自動的に精度が選択されます。
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True).eval()

# 生成のためのハイパーパラメータを指定。ただし、4.32.0 以上のトTransformerを使用している場合は、これを行う必要はありません。
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# 第一回対話ターン
response, history = model.chat(tokenizer, "你好", history=None)
print(response)
# 你好！很高兴为你提供帮助。

# 第二回対話ターン
response, history = model.chat(tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
# 这是一个关于一个年轻人奋斗创业最终取得成功的故事。
# 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。
# 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。
# 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。
# 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。
# 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。

# 第三轮对话 第三回対話ターン
response, history = model.chat(tokenizer, "给这个故事起一个标题", history=history)
print(response)
# 《奋斗创业：一个年轻人的成功之路》
```

Qwen の学習済みベースモデルの実行も簡単です。

<details>
  <summary>Qwen の実行</summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names："Qwen/Qwen-7B"、"Qwen/Qwen-14B"
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)
# bf16 を使用
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, bf16=True).eval()
# fp16 を使用
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, fp16=True).eval()
# CPU のみ使用
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="cpu", trust_remote_code=True).eval()
# オートモードを使用すると、デバイスに応じて自動的に精度が選択されます。
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True).eval()

# 生成のためのハイパーパラメータを指定。ただし、4.32.0 以上のトTransformerを使用している場合は、これを行う必要はありません。
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

inputs = tokenizer('蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是', return_tensors='pt')
inputs = inputs.to(model.device)
pred = model.generate(**inputs)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))
# 蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是亚的斯亚贝巴（Addis Ababa）...
```

</details>

<p id="DownloadModel">
HuggingFaceからモデルのチェックポイントとコードをダウンロードする際にネットワークの問題が発生した場合、ModelScopeからチェックポイントをダウンロードする方法はこちらでございます。
</p>

```python
from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Downloading model checkpoint to a local dir model_dir
# model_dir = snapshot_download('qwen/Qwen-7B')
# model_dir = snapshot_download('qwen/Qwen-7B-Chat')
# model_dir = snapshot_download('qwen/Qwen-14B')
model_dir = snapshot_download('qwen/Qwen-14B-Chat')

# Loading local checkpoints
# trust_remote_code is still set as True since we still load codes from local dir instead of transformers
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True
).eval()
```

### 🤖 ModelScope

ModelScope は、MaaS（Model-as-a-Service） のためのオープンソースプラットフォームであり、AI 開発者に柔軟で費用対効果の高いモデルサービスを提供します。同様に、以下のように ModelScope でモデルを実行することができます:

```python
from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

# Model names："Qwen/Qwen-7B-Chat"、"Qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("qwen/Qwen-7B-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

response, history = model.chat(tokenizer, "你好", history=None)
print(response)
response, history = model.chat(tokenizer, "浙江的省会在哪里？", history=history) 
print(response)
response, history = model.chat(tokenizer, "它有什么好玩的景点", history=history)
print(response)
```

### バッチ推論
Qwenはバッチ推論をサポートしている。フラッシュ・アテンションを有効にした場合、バッチ推論を使用することで40%のスピードアップが期待できる。以下にコード例を示す：
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GenerationConfig
from qwen_generation_utils import make_context, decode_tokens, get_stop_words_ids

tokenizer = AutoTokenizer.from_pretrained(
    './',
    pad_token='<|extra_0|>',
    eos_token='<|endoftext|>',
    padding_side='left',
    trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    './',
    pad_token_id=tokenizer.pad_token_id,
    device_map="auto",
    trust_remote_code=True
).eval()
model.generation_config = GenerationConfig.from_pretrained('./', pad_token_id=tokenizer.pad_token_id)

all_raw_text = ["我想听你说爱我。", "今天我想吃点啥，甜甜的，推荐下", "我马上迟到了，怎么做才能不迟到"]
batch_raw_text = []
for q in all_raw_text:
    raw_text, _ = make_context(
        tokenizer,
        q,
        system="You are a helpful assistant.",
        max_window_size=model.generation_config.max_window_size,
        chat_format=model.generation_config.chat_format,
    )
    batch_raw_text.append(raw_text)

batch_input_ids = tokenizer(batch_raw_text, padding='longest')
batch_input_ids = torch.LongTensor(batch_input_ids['input_ids']).to(model.device)
batch_out_ids = model.generate(
    batch_input_ids,
    return_dict_in_generate=False,
    generation_config=model.generation_config
)
padding_lens = [batch_input_ids[i].eq(tokenizer.pad_token_id).sum().item() for i in range(batch_input_ids.size(0))]

batch_response = [
    decode_tokens(
        batch_out_ids[i][padding_lens[i]:],
        tokenizer,
        raw_text_len=len(batch_raw_text[i]),
        context_length=(batch_input_ids[i].size(0)-padding_lens[i]),
        chat_format="chatml",
        verbose=False,
        errors='replace'
    ) for i in range(len(all_raw_text))
]
print(batch_response)

response, _ = model.chat(tokenizer, "我想听你说爱我。", history=None)
print(response)

response, _ = model.chat(tokenizer, "今天我想吃点啥，甜甜的，推荐下", history=None)
print(response)

response, _ = model.chat(tokenizer, "我马上迟到了，怎么做才能不迟到", history=None)
print(response)
```

### CPU

Qwenとtiktokenの純粋なC++実装である [qwen.cpp](https://github.com/QwenLM/qwen.cpp) を使用することを強くお勧めします。詳細はレポを確認してください！

また、CPU上でモデルを直接実行することも簡単ですが、その場合はデバイスの指定が必要です：


```python
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
```

ただし、推論効率が極端に低下する可能性があります。

### 複数のGPU

GPUメモリ不足に悩まされ、1つ以上のGPUでモデルを実行したい場合、Transformersでサポートされるようになったデフォルトのロード方法を直接使うことができます。以前の `utils.py` に基づく方法は非推奨です。

しかし、この方法は簡単ですが、ネイティブ・パイプライン並列の効率は低いです。FastChatでvLLMを使用することをお勧めします。

### DashScope

APIを通じてQwenを利用する最も簡単な方法は、Alibaba Cloudを通じたDashScope APIサービスです。その使い方を紹介します。さらに、OpenAIスタイルのAPIをご自身のサーバーにデプロイするためのスクリプトも提供しています。

DashScopeはAlibaba Cloudが提供する大規模言語モデルAPIサービスで、今回Qwenに対応した。DashScopeの背後にあるモデルは、詳細が提供されていない一時的な社内バージョンであることに注意してください。サービスには `qwen-turbo` と `qwen-plus` があり、前者はより高速に動作し、後者はより優れたパフォーマンスを実現している。詳細はドキュメント [こちら](https://dashscope.aliyun.com) を参照。

公式サイト [link](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key?spm=a2c4g.11186623.0.0.6c2774fahtfXdn) で DashScope アカウントを作成し、API キー (AK) を取得してください。AK は環境変数で設定することをお勧めします：
```bash
export DASHSCOPE_API_KEY="YOUR_DASHSCOPE_API_KEY"
```
その後、パッケージをインストールし、ドキュメントは [こちら](https://help.aliyun.com/zh/dashscope/developer-reference/install-dashscope-sdk) をクリックしてください。Python をお使いの場合は、pip で DashScope をインストールできます：
```bash
pip install dashscope
```
JAVA SDKを使用する場合は、この方法でインストールできます：
```xml
<!-- https://mvnrepository.com/artifact/com.alibaba/dashscope-sdk-java -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dashscope-sdk-java</artifactId>
    <version>the-latest-version</version>
</dependency>
```
DashScope を使用する最も簡単な方法は、OpenAI API と同様のメッセージを使用する方法です。以下にその例を示す：
```python
import random
from http import HTTPStatus
from dashscope import Generation


def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '如何做西红柿鸡蛋？'}]
    gen = Generation()
    response = gen.call(
        Generation.Models.qwen_turbo,
        messages=messages,
        seed=random.randint(1, 10000),  # set the random seed, optional, default to 1234 if not set
        result_format='message',  # set the result to be "message" format.
    )
    return response


if __name__ == '__main__':
    response = call_with_messages()
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
```
詳しい使い方は公式サイトをご覧ください。
<br><br>


## 量子化

### GPTQ

我々は、[AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ)に基づいた解決策を提供し、Int4とInt8の量子化モデルをリリースすることで、ほぼ無損失なモデル効果を達成しつつ、メモリコストと推論速度の両方で性能を向上させた。

ここでは、量子化されたモデルを推論に使用する方法を説明する。始める前に、auto-gptqの要件を満たしていることを確認し（例：torch 2.0以上、transformers 4.32.0以上など）、必要なパッケージをインストールしてください：

```bash
pip install auto-gptq optimum
```

auto-gptq`のインストールに問題がある場合は、公式の[repo](https://github.com/PanQiWei/AutoGPTQ)をチェックして、ホイールを見つけることをお勧めする。

> 注意：コンパイル済みの `auto-gptq` パッケージは `torch` のバージョンと CUDA バージョンに強く依存しています。さらに、最近のアップデートにより 
> さらに、最近のアップデートにより、`transformers`、`optimum`、`peft` でサポートされていないバージョンのエラーが発生する可能性があります。
> 以下の要件を満たす最新バージョンの使用をお勧めします：
> - torch==2.1 auto-gptq>=0.5.1 transformers>=4.35.0 optimum>=1.14.0 peft>=0.6.1 > - torch==2.1 auto-gptq>=0.5.1 transformers>=4.35.0 optimum>=1.14.0 peft>=0.6.1
> - torch>=2.0, <2.1 auto-gptq<0.5.0 transformers<4.35.0  optimum<1.14.0 peft>=0.5.0,<0.6.0

そうすれば、量子化されたモデルを簡単にロードすることができ、いつもと同じように推論を実行することができる：

```python
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat-Int4",
    device_map="auto",
    trust_remote_code=True
).eval()
response, history = model.chat(tokenizer, "Hi", history=None)
```

ベンチマークにおける BF16 モデルと Int8、Int4 モデルの性能について説明します。その結果は以下に示します：

| Quantization         | MMLU | CEval (val) | GSM8K | Humaneval |
|----------------------|:----:|:-----------:|:-----:|:---------:|
| Qwen-1.8B-Chat (BF16)| 43.3 |    55.6     | 33.7  |   26.2    |
| Qwen-1.8B-Chat (Int8)| 43.1 |    55.8     | 33.0  |   27.4    |
| Qwen-1.8B-Chat (Int4)| 42.9 |    52.8     | 31.2  |   25.0    |
| Qwen-7B-Chat (BF16)  | 55.8 |    59.7     | 50.3  |   37.2    |
| Qwen-7B-Chat (Int8)  | 55.4 |    59.4     | 48.3  |   34.8    |
| Qwen-7B-Chat (Int4)  | 55.1 |    59.2     | 49.7  |   29.9    |
| Qwen-14B-Chat (BF16) | 64.6 |    69.8     | 60.1  |   43.9    |
| Qwen-14B-Chat (Int8) | 63.6 |    68.6     | 60.0  |   48.2    |
| Qwen-14B-Chat (Int4) | 63.3 |    69.0     | 59.8  |   45.7    |
| Qwen-72B-Chat (BF16) | 74.4 |    80.1     | 76.4  |   64.6    |
| Qwen-72B-Chat (Int8) | 73.5 |    80.1     | 73.5  |   62.2    |
| Qwen-72B-Chat (Int4) | 73.4 |    80.1     | 75.3  |   61.6    |

### KVキャッシュ量子化

> 注意: Hugging Faceの内部メカニズムにより、この機能のサポートファイル 
> (すなわち、`cache_autogptq_cuda_256.cpp`と`cache_autogptq_cuda_kernel_256.cu`)が欠落している可能性があります。以下を手動でダウンロードしてください。
> Hugging Face Hubから手動でダウンロードし、他のモジュールファイルと同じフォルダに入れてください。

アテンション KV キャッシュを量子化して圧縮して保存すると、サンプルのスループットが向上する。この機能を有効にするには、`config.json` に `use_cache_quantization` と `use_cache_kernel` という引数を指定する。
具体的な使用方法は以下の通りである：

```python
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
     device_map="auto",
     trust_remote_code=True,
     use_cache_quantization=True,
     use_cache_kernel=True,
     use_flash_attn=False
)
```

注意： 現在、KVキャッシュの量子化とフラッシュ・アテンションを同時に使用することはできない。
KV キャッシュの量子化とフラッシュ・アテンションを同時に有効にした場合（`use_flash_attn=True`, `use_cache_quantization=True`, `use_cache_kernel=True`）、デフォルトでは `use_flash_attn` は無効になる（`use_flash_attn=false`）。

量子化されたint8-kvcacheモデルを使用しても、下流の評価で大幅な性能低下がないことを確認しました。以下では、さまざまな条件下でのメモリフットプリントのプロファイリングに焦点を当てます。
プロファイリングは、PyTorch 2.0.1とCUDA 11.4を搭載したシングルA100-SXM4-80G GPUで実行しました。
デフォルトで1024トークンを生成するためにBF16モデルを使用し、"OOM "はメモリ不足エラーを示します。

KVキャッシュの量子化により、モデルはより大きなバッチサイズ（bs）で推論することができる。

| USE KV Cache |  bs=1  |  bs=4  | bs=16  | bs=32  | bs=64  | bs=100 |
|--------------|:------:|:------:|:------:|:------:|:------:|:------:|
| No           | 16.3GB | 24.1GB | 31.7GB | 48.7GB |  OOM   |  OOM   |
| Yes          | 15.5GB | 17.2GB | 22.3GB | 30.2GB | 48.2GB | 72.4GB |

KVキャッシュ量子化により、推論段階でより長いシーケンス（`sl`, シーケンス長、生成されるトークン数を指す）を生成する際、モデルはより多くのメモリを節約することができる。

| USE KV Cache | sl=512 | sl=1024 | sl=2048 | sl=4096 | sl=8192 |
|--------------|:------:|:-------:|:-------:|:-------:|:-------:|
| No           | 15.2GB | 16.3GB  | 17.6GB  | 19.5GB  | 23.2GB  |
| Yes          |  15GB  | 15.5GB  | 15.8GB  | 16.6GB  | 17.6GB  |

KVキャッシュ量子化モデルでは、layer-pastのフォーマットをfloatからint8に変換し、量子化された `layer-past` には量子化パラメータも格納される。

具体的な手順は以下の通り：

1. key/valueの量子化を行います。
```
    qv,scale,zero_point=quantize_cache_v(v)
```

2. `layer_past`に保存します。

量子化されたの`layer-past`は:
```
    layer_past=((q_key,key_scale,key_zero_point),
                (q_value,value_scale,value_zero_point))
```
`layer_past`の元のフォーマットは以下の通りである：
```
    layer_past=(key,value)
```
量子化されたアテンションKVを使用したい場合、 
Int8のkey/valueをfloatフォーマットに戻すには、以下のように逆量子化操作を使用します：
```
    v=dequantize_cache_torch(qv,scale,zero_point)
```
<br>

## 推論パフォーマンス

このセクションでは、さまざまな精度のモデルのスピードとメモリの統計情報を提供する。スピードとメモリーのプロファイリングは[このスクリプト](https://qianwen-res.oss-cn-beijing.aliyuncs.com/profile.py)を使用しています。

BF16、Int8、および Int4 のモデルを使用して 2048 を生成する際の平均推論速度 (トークン/秒) と GPU メモリ使用量を測定しました。

<table>
    <tr>
        <td>Model Size</td>
        <td>Quantization</td>
        <td>Speed (Tokens/s)</td>
        <td>GPU Memory Usage</td>
    </tr>
    <tr>
        <td rowspan="3">1.8B</td>
        <td>BF16</td>
        <td>54.09</td>
        <td>4.23GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>55.56</td>
        <td>3.48GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>71.07</td>
        <td>2.91GB</td>
    </tr>
    <tr>
        <td rowspan="3">7B</td>
        <td>BF16</td>
        <td>40.93</td>
        <td>16.99GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>37.47</td>
        <td>11.20GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>50.09</td>
        <td>8.21GB</td>
    </tr>
    <tr>
        <td rowspan="3">14B</td>
        <td>BF16</td>
        <td>32.22</td>
        <td>30.15GB</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>29.28</td>
        <td>18.81GB</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>38.72</td>
        <td>13.01GB</td>
    </tr>
    <tr>
        <td rowspan="3">72B</td>
        <td>BF16</td>
        <td>8.48</td>
        <td>144.69GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int8</td>
        <td>9.05</td>
        <td>81.27GB (2xA100)</td>
    </tr>
    <tr>
        <td>Int4</td>
        <td>11.32</td>
        <td>48.86GB</td>
    </tr>
    <tr>
        <td>72B + vLLM</td>
        <td>BF16</td>
        <td>17.60</td>
        <td>2xA100</td>
    </tr>
</table>

プロファイリングは、PyTorch 2.0.1、CUDA 11.8、および Flash-Attendant 2 を備えた単一の A100-SXM4-80G GPU (2xA100 について言及されている場合を除く) で実行されます。(72B + vLLM は PyTorch 2.1.0 および Cuda 11.8 を使用します。) 推論速度 は、エンコードされ生成されたトークンの平均である。

注意：上記のInt4/Int8モデルの推論速度は、autogptqを使用しています。現在、``AutoModelForCausalLM.from_pretrained``で読み込まれるモデルの推論速度は約20%遅くなります。この問題はHuggingFaceチームに報告済みであり、解決策があれば即座に更新されます。

また、コンテキストと生成の長さ、Flash Attention バージョンのさまざまな設定で推論速度と GPU メモリ使用量も測定します。 結果は、Hugging Face または ModelScope の対応するモデルカードで確認できます。

## ファインチューニング

### 使用方法
現在、公式のトレーニングスクリプト `finetune.py` を提供しています。さらに、finetune.pyのシェルスクリプトを提供し、finetune.pyを実行することで、finetune.pyを起動することができる。さらに、安心してファインチューニングを開始するためのシェルスクリプトも提供しています。このスクリプトは、[DeepSpeed](https://github.com/microsoft/DeepSpeed) (注意：これはpydanticの最新バージョンとコンフリクトする可能性があるので、`pydantic<2.0`にする必要があります) および [FSDP](https://engineering.fb.com/2021/07/15/open-source/fsdp/) を使用したトレーニングをサポートします。弊社が提供するシェル・スクリプトは DeepSpeed と Peft を使用するため、事前に DeepSpeed と Peft をインストールすることをお勧めします：
```bash
pip install "peft<0.8.0" deepspeed
```

学習データを準備するには、すべてのサンプルをリストにまとめ、jsonファイルに保存する必要があります。各サンプルはidと会話リストで構成される辞書です。以下は1つのサンプルを含む単純なリストの例です：

```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "你好"
      },
      {
        "from": "assistant",
        "value": "我是一个语言模型，我叫通义千问。"
      }
    ]
  }
]
```

データ準備の後、提供されているシェルスクリプトを使って微調整を実行することができる。データファイルのパス `$DATA` を忘れずに指定してください。

ファインチューニングのスクリプトを使用することで、以下のことが可能になる：
- フルパラメーター・ファインチューニング
- LoRA
- Q-LoRA

フルパラメータパラメータのファインチューニングを行うには、トレーニングプロセス全体ですべてのパラメータを更新する必要があります。トレーニングを開始するには、以下のスクリプトを実行します：

```bash
# 分散トレーニング。GPUメモリが不足するとトレーニングが破綻するため、シングルGPUのトレーニングスクリプトは提供していません。
bash finetune/finetune_ds.sh
```

シェルスクリプトでは、正しいモデル名またはパス、データパス、出力ディレクトリを指定することを忘れないでください。このスクリプトでは DeepSpeed ZeRO 3 を使用しています。変更したい場合は、引数 `--deepspeed` を削除するか、要件に基づいて DeepSpeed 設定 json ファイルを変更してください。さらに、このスクリプトは混合精度のトレーニングに対応しており、`--bf16 True` または `--fp16 True` を使用することができます。fp16を使用する場合は、混合精度のトレーニングのため、DeepSpeedを使用することを忘れないこと。経験的に、あなたのマシンがbf16をサポートしている場合、私たちのプリトレーニングとアライメントを整合させるためにbf16を使用することをお勧めします。

同様に、LoRAを実行するには、以下のように別のスクリプトを使って実行する。始める前に、`peft`がインストールされていることを確認してください。また、モデル、データ、出力へのパスを指定する必要があります。学習済みモデルには絶対パスを使用することをお勧めします。なぜなら、LoRAはアダプタのみを保存し、アダプタ設定jsonファイルの絶対パスは、ロードする事前学習済みモデルを見つけるために使用されるからです。また、このスクリプトはbf16とfp16の両方をサポートしている。

```bash
# シングルGPUトレーニング
bash finetune/finetune_lora_single_gpu.sh
# 分散トレーニング
bash finetune/finetune_lora_ds.sh
```

LoRA ([論文](https://arxiv.org/abs/2106.09685)) は、フルパラメーターによるファインチューニングと比較して、adapterのパラメーターを更新するだけで、元の大きな言語モデル層は凍結されたままである。そのため、メモリコストが大幅に削減でき、計算コストも削減できる。

なお、チャットモデル（Qwen-7B-Chatなど）ではなく、ベース言語モデル（Qwen-7Bなど）の微調整にLoRAを使用した場合、スクリプトは自動的に学習可能なパラメータとして埋め込み層と出力層を切り替えます。これは、ベースとなる言語モデルには、ChatMLフォーマットによってもたらされる特殊なトークンに関する知識がないためです。したがって、これらのレイヤーは、モデルがトークンを理解し予測するために更新される必要があります。別の言い方をすれば、もしLoRAで特殊なトークンを学習するのであれば、コード内で `modules_to_save` を設定することで、レイヤーを学習可能なパラメータに設定する必要があります。また、これらのパラメータが学習可能な場合、ZeRO 3 を使用することはできません。新しいトレーニング可能なパラメータがない場合は、DeepSpeed 設定ファイルを変更することで ZeRO 3 に切り替えることができます。さらに、LoRAのメモリフットプリントは、このような学習可能なパラメータがある場合とない場合で、大きな開きがあることがわかります。そのため、メモリに問題がある場合は、LoRAのChatモデルを微調整することをお勧めします。詳細は以下のプロファイルを参照してください。

しかし、それでもメモリ不足に悩む場合は、Q-LoRA（[論文](https://arxiv.org/abs/2305.14314)）を検討することができます。これは、量子化されたラージ言語モデルと、ページド・アテンションなどの他のテクニックを使用し、さらに少ないメモリコストで実行することができます。

注：シングル GPU Q-LoRA トレーニングを実行するには、`pip` または `conda` を使って `mpi4py` をインストールする必要があるかもしれない。

Q-LoRAを実行するには、以下のスクリプトを直接実行してください：

```bash
# シングルGPUトレーニング
bash finetune/finetune_qlora_single_gpu.sh
# 分散トレーニング
bash finetune/finetune_qlora_ds.sh
```

Q-LoRAについては、弊社が提供する量子化モデル、例えばQwen-7B-Chat-Int4をロードすることをお勧めします。BF16モデルは使用し**ない**でください！フルパラメータ・ファインチューニングやLoRAとは異なり、Q-LoRAではfp16のみがサポートされる。シングルGPUのトレーニングでは、トーチアンプによるエラーが観測されたため、混合精度のトレーニングにはDeepSpeedを使用する必要がある。また、Q-LoRAの場合、LoRAの特殊トークンの問題が残っています。しかし、Q-LoRAではチャットモデルとしてInt4モデルのみを提供しており、言語モデルはChatML形式の特殊トークンを学習しているため、レイヤーの心配はありません。なお、Int4モデルのレイヤーは学習できないはずなので、学習で特殊なトークンを導入すると、Q-LoRAが動作しなくなる可能性があります。

LoRAとQ-LoRAの学習は、フルパラメータによるファインチューニングとは異なり、アダプターパラメータのみを保存する。仮にQwen-7Bから学習を開始したとすると、以下のようにファインチューニングされたモデルを読み込んで推論を行うことができる：

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()
```

アダプターをマージし、微調整したモデルをスタンドアロンモデルとして保存したい場合は（これは LoRA でのみ可能で、Q-LoRA からパラメータをマージすることはできません）、以下のコードを実行します：

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()

merged_model = model.merge_and_unload()
# max_shard_size and safe serialization are not necessary. 
# They respectively work for sharding checkpoint and save the model to safetensors
merged_model.save_pretrained(new_model_directory, max_shard_size="2048MB", safe_serialization=True)
```

`new_model_directory` ディレクトリには、マージされたモデルの重みとモジュール ファイルが含まれます。 保存されたファイルに `*.cu` および `*.cpp` ファイルが存在しない可能性があることに注意してください。 KVキャッシュ機能を使用したい場合は、手動でコピーしてください。 また、このステップではトークナイザー ファイルは新しいディレクトリに保存されません。 トークナイザー ファイルをコピーするか、次のコードを使用できます。
```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    path_to_adapter, # path to the output directory
    trust_remote_code=True
)

tokenizer.save_pretrained(new_model_directory)
```

注意：マルチGPUトレーニングの場合、分散トレーニング用の適切なハイパーパラメータをマシンに応じて指定する必要があります。また、データ、メモリフットプリント、トレーニング速度を考慮して、引数 `--model_max_length` で最大シーケンス長を指定することをお勧めします。

### メモリと速度のプロファイリング
シングルGPUトレーニングのセットアップにおいて、LoRA (LoRA(emb)はembeddingと出力層を学習させるが、LoRAはembeddingと出力層を学習させない) とQ-LoRAのGPUメモリとトレーニング速度をプロファイリングする。このテストでは、シングルA100-SXM4-80G GPUで実験し、CUDA 11.8とPytorch 2.0を使用します。Flash attention 2を使用します。256、512、1024、2048、4096、8192という異なる長さの入力のメモリ（GB）と速度（s/iter）をプロファイリングします。また、2台のA100 GPUを用いたQwen-7Bによるフルパラメータ・ファインチューニングの統計量も報告する。GPUメモリの制限のため、256、512、1024トークンの統計のみを報告する。


Qwen-72B については、2 つの方法で実験します。1) 4 つの A100-SXM4-80G GPU での Lora 微調整 + DeepSpeed ZeRO 3、および 2) 1 つの A100-SXM4-80G GPU での QLora (int4) 微調整。 OOM は、LoRA (emb) 微調整と Deepspeed ZeRO 3 を使用しない LoRA 微調整の両方で 4 つの A100-SXM4-80G GPU で発生することに注意してください (`--deepspeedfinetune/ds_config_zero3.json` を [`finetune/finetune_lora_ds に渡すことができます) .sh`](finetune/finetune_lora_ds.sh) を使用して DeepSpeed ZeRO 3 を有効にします)。

統計量を以下に示す：

<table>
    <tr>
      <th rowspan="2">Model Size</th><th rowspan="2">Method</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">256</th><th align="center">512</th><th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th>
    </tr>
    </tr>
    </tr>
		<tr>
        <th rowspan="4">1.8B</th><td>LoRA</td><td align="center">6.7G / 1.0s/it</td><td align="center">7.4G / 1.0s/it</td><td align="center">8.4G / 1.1s/it</td><td align="center">11.0G / 1.7s/it</td><td align="center">16.2G / 3.3s/it</td><td align="center">21.8G / 6.8s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td><td align="center">13.7G / 1.0s/it</td><td align="center">14.0G / 1.0s/it</td><td align="center">14.0G / 1.1s/it</td><td align="center">15.1G / 1.8s/it</td><td align="center">19.7G / 3.4s/it</td><td align="center">27.7G / 7.0s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">5.8G / 1.4s/it</td><td align="center">6.0G / 1.4s/it</td><td align="center">6.6G / 1.4s/it</td><td align="center">7.8G / 2.0s/it</td><td align="center">10.2G / 3.4s/it</td><td align="center">15.8G / 6.5s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td><td align="center">43.5G / 2.1s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.3s/it</td><td align="center">47.1G / 2.8s/it</td><td align="center">48.3G / 5.6s/it</td>
    </tr>
    <tr>
        <th rowspan="4">7B</th><td>LoRA</td><td align="center">20.1G / 1.2s/it</td><td align="center">20.4G / 1.5s/it</td><td align="center">21.5G / 2.8s/it</td><td align="center">23.8G / 5.2s/it</td><td align="center">29.7G / 10.1s/it</td><td align="center">36.6G / 21.3s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td><td align="center">33.7G / 1.4s/it</td><td align="center">34.1G / 1.6s/it</td><td align="center">35.2G / 2.9s/it</td><td align="center">35.1G / 5.3s/it</td><td align="center">39.2G / 10.3s/it</td><td align="center">48.5G / 21.7s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">11.5G / 3.0s/it</td><td align="center">11.5G / 3.0s/it</td><td align="center">12.3G / 3.5s/it</td><td align="center">13.9G / 7.0s/it</td><td align="center">16.9G / 11.6s/it</td><td align="center">23.5G / 22.3s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td><td align="center">139.2G / 4.0s/it</td><td align="center">148.0G / 4.0s/it</td><td align="center">162.0G / 4.5s/it</td><td align="center">-</td><td align="center">-</td><td align="center">-</td>
    </tr>
    <tr>
        <th rowspan="3">14B</th><td>LoRA</td><td align="center">34.6G / 1.6s/it</td><td align="center">35.1G / 2.4s/it</td><td align="center">35.3G / 4.4s/it</td><td align="center">37.4G / 8.4s/it</td><td align="center">42.5G / 17.0s/it</td><td align="center">55.2G / 36.0s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td><td align="center">51.2 / 1.7s/it</td><td align="center">51.1G / 2.6s/it</td><td align="center">51.5G / 4.6s/it</td><td align="center">54.1G / 8.6s/it</td><td align="center">56.8G / 17.2s/it</td><td align="center">67.7G / 36.3s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">18.7G / 5.3s/it</td><td align="center">18.4G / 6.3s/it</td><td align="center">18.9G / 8.2s/it</td><td align="center">19.9G / 11.8s/it</td><td align="center">23.0G / 20.1s/it</td><td align="center">27.9G / 38.3s/it</td>
    </tr>
	<tr>
        <th rowspan="2">72B</th><td>LoRA + Deepspeed Zero3</td><td align="center">215.4G / 17.6s/it</td><td align="center">217.7G / 20.5s/it</td><td align="center">222.6G / 29.4s/it</td><td align="center">228.8G / 45.7s/it</td><td align="center">249.0G / 83.4s/it</td><td align="center">289.2G / 161.5s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td><td align="center">61.4G / 27.4s/it</td><td align="center">61.4G / 31.5s/it</td><td align="center">62.9G / 41.4s/it</td><td align="center">64.1G / 59.5s/it</td><td align="center">68.0G / 97.7s/it</td><td align="center">75.6G / 179.8s/it</td>
    </tr>
</table>
<br>

## デプロイ

### vLLM 
デプロイメントと高速推論のためには、vLLMを使用することをお勧めします。

**CUDA 12.1** および **PyTorch 2.1** を使用している場合は、次のコマンドを直接使用して vLLM をインストールできます。
```bash
pip install vllm
```

それ以外の場合は、公式 vLLM [インストール手順](https://docs.vllm.ai/en/latest/getting_started/installation.html) を参照してください。

#### vLLM + Transformer Wrapper

[ラッパー コード](examples/vllm_wrapper.py) をダウンロードし、複数ラウンドの対話対話のために次のコマンドを実行できます。 (注: 現在は ``model.chat()`` メソッドのみをサポートしています。)

```python
from vllm_wrapper import vLLMWrapper

model = vLLMWrapper('Qwen/Qwen-7B-Chat', tensor_parallel_size=1)
# model = vLLMWrapper('Qwen/Qwen-7B-Chat-Int4', tensor_parallel_size=1, dtype="float16")

response, history = model.chat(query="你好", history=None)
print(response)
response, history = model.chat(query="给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
response, history = model.chat(query="给这个故事起一个标题", history=history)
print(response)
```
#### vLLM + Web デモ / OpenAI API
FastChat を使用して、Web デモまたは OpenAI API サーバーを起動できます。 まず、FastChat をインストールします。
```
pip install "fschat[model_worker,webui]"
```

vLLM および FastChat で Qwen を実行するには、次の方法でコントローラーを起動する必要があります。
```bash
python -m fastchat.serve.controller
```

それからmodel workerを起動し、推論のためにモデルをロードします。シングルGPU推論の場合は、直接実行できます：
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --dtype bfloat16
# python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --dtype float16 # INT4モデルを実行します
```
しかし、より高速な推論や大容量メモリーのために複数のGPUでモデルを実行したい場合は、vLLMがサポートするテンソル並列を使用することができます。モデルを4GPUで実行するとすると、コマンドは以下のようになります：
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4 --dtype bfloat16
# python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4 --dtype float16 # run int4 model # INT4モデルを実行します
```

モデルワーカーを起動した後、起動することができます：

* Web UI Demo
```bash
python -m fastchat.serve.gradio_web_server
```

* OpenAI API
```bash
python -m fastchat.serve.openai_api_server --host localhost --port 8000
```

ただし、vLLM と FastChat の使用が難しい場合は、Web デモ、CLI デモ、および API をデプロイするために提供されている最も簡単な方法を試すことができます。


### ウェブ UI

ウェブ UI デモを構築するためのコードを提供します（@wysaid に感謝）。これを始める前に、以下のパッケージがインストールされていることを確認してください:

```bash
pip install -r requirements_web_demo.txt
```

そして、以下のコマンドを実行し、生成されたリンクをクリックします:

```bash
python web_demo.py
```

<p align="center">
    <br>
    <img src="assets/web_demo.gif" width="600" />
    <br>
<p>

### CLI デモ

`cli_demo.py` に CLI のデモ例を用意しています。ユーザはプロンプトを入力することで Qwen-7B-Chat と対話することができ、モデルはストリーミングモードでモデルの出力を返します。以下のコマンドを実行する:

```
python cli_demo.py
```

<p align="center">
    <br>
    <img src="assets/cli_demo.gif" width="600" />
    <br>
<p>
<br>

### API

OpenAI API をベースにローカルAPIをデプロイする方法を提供する（@hanpenggit に感謝）。始める前に、必要なパッケージをインストールしてください:

```bash
pip install fastapi uvicorn "openai<1.0" pydantic sse_starlette
```

それから、API をデプロイするコマンドを実行します:

```bash
python openai_api.py
```

チェックポイント名やパスには `-c`、CPU デプロイメントには `--cpu-only` など、引数を変更できます。API デプロイメントを起動する際に問題が発生した場合は、パッケージを最新バージョンに更新することで解決できる可能性があります。

API の使い方も簡単です。以下の例をご覧ください:

```python
import openai
openai.api_base = "http://localhost:8000/v1"
openai.api_key = "none"

# ストリーミングレスポンスを有効化するリクエストを作成する
for chunk in openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=True
    # ストリーミング出力形式でのストップワードの指定はまだサポートされておらず、開発中です。
):
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

# ストリーミングレスポンスを有効化しないリクエストを作成する
response = openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=False,
    stop=[] # 例えば、stop=["Observation:"] (ReAct プロンプトの場合)。
)
print(response.choices[0].message.content)
```

<p align="center">
    <br>
    <img src="assets/openai_api.gif" width="600" />
    <br>
<p>

**Function Calling** もサポートされています(ただし、今のところ `stream=False` の場合のみ)。使用例](examples/function_call_examples.py) を参照してください。
<br><br>

## 🐳 Docker

デプロイプロセスを簡素化するために、あらかじめ環境を構築した docker イメージを提供しています： [qwenllm/qwen](https://hub.docker.com/r/qwenllm/qwen)。ドライバを導入し、モデルファイルをダウンロードするだけで、デモを起動し、OpenAI APIをデプロイし、モデルを微調整することができます。

### 準備

1. 使用するイメージに応じて、正しいバージョンのNvidiaドライバをインストールしてください：
  - `qwenllm/qwen:cu117` (**recommend**): `>= 515.48.07`
  - `qwenllm/qwen:cu114` (w/o flash-attention): `>= 470.82.01`
  - `qwenllm/qwen:cu121`: `>= 530.30.02`
  - `qwenllm/qwen:latest`: same as `qwenllm/qwen:cu117`

2. [Docker](https://docs.docker.com/engine/install/) と [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) をインストールして設定します：

```bash
# configure docker
sudo systemctl start docker
# test if docker is correctly installed
sudo docker run hello-world

# configure nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
# test if nvidia-container-toolkit is correctly installed
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

3. モデルのチェックポイントとコードを環境にダウンロードします（[こちら](#DownloadModel)を参照）。

### デプロイ

ここでは例として Qwen-7B-Chat を使用する。ウェブ・デモや API を起動する前に、以下のように設定を行います：

```bash
IMAGE_NAME=qwenllm/qwen:cu117
PORT=8901
CHECKPOINT_PATH=/path/to/Qwen-7B-Chat   # Path to downloaded model checkpoints and codes
```
以下のスクリプトがビルドに役立つ：

* OpenAI API
```bash
bash docker/docker_openai_api.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* Web UI
```bash
bash docker/docker_web_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH} --port ${PORT}
```

* CLI Demo
```bash
bash docker/docker_cli_demo.sh -i ${IMAGE_NAME} -c ${CHECKPOINT_PATH}
```

上記のコマンドは自動的に必要なイメージをダウンロードし、バックグラウンドでWeb UIデモを起動します（サービスは自動で再起動します）。デモを使用するには、ホスト上で `http://localhost:${PORT}` を開いてください。

以下の出力が表示されれば、デモは正常に起動しています：

```text
Successfully started web demo. Open '...' to try!
Run `docker logs ...` to check demo status.
Run `docker rm -f ...` to stop and remove the demo.
```

デモの状態を確認したい場合は、`docker logs qwen` を使って出力を表示できる。

docker rm -f qwen` でサービスを停止し、コンテナを削除できる。


### ファインチューニング

ビルド済みのDockerイメージを利用したファインチューニングの方法は、基本的に[前章](#Finetuning)と同じです(すでにイメージに依存関係がインストールされています)：

以下はシングルGPUのLoRAの例です：
```bash
IMAGE_NAME=qwenllm/qwen:cu117
CHECKPOINT_PATH=/path/to/Qwen-7B                # Path to downloaded model checkpoints and codes
#CHECKPOINT_PATH=/path/to/Qwen-7B-Chat-Int4     # Path to downloaded model checkpoints and codes (Q-LoRA)
DATA_PATH=/path/to/data/root                    # Prepare finetune data at ${DATA_PATH}/example.json
OUTPUT_PATH=/path/to/output/checkpoint          # Path to finetune outputs

# Use all host devices by default
DEVICE=all
# If you need to specify GPUs for training, set device as follow (NOTE: internal quotation marks cannot be omitted)
#DEVICE='"device=0,1,2,3"'

mkdir -p ${OUTPUT_PATH}

# Single-GPU LoRA finetuning
docker run --gpus ${DEVICE} --rm --name qwen \
    --mount type=bind,source=${CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-7B \
    --mount type=bind,source=${DATA_PATH},target=/data/shared/Qwen/data \
    --mount type=bind,source=${OUTPUT_PATH},target=/data/shared/Qwen/output_qwen \
    --shm-size=2gb \
    -it ${IMAGE_NAME} \
    bash finetune/finetune_lora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B/ -d /data/shared/Qwen/data/example.json
```

例えばシングルGPUのQ-LoRAに変更するには、`docker run`内のbashコマンドを変更するだけでいい：
```bash
bash finetune/finetune_qlora_single_gpu.sh -m /data/shared/Qwen/Qwen-7B-Chat-Int4/ -d /data/shared/Qwen/data/example.json
```
<br>

## 🔥 システムプロンプト
Qwen-1.8-Chat と Qwen-72B-Chat は、複数回の複雑な対話を伴う多様なシステム プロンプトで完全にトレーニングされているため、さまざまなシステム プロンプトに従い、コンテキストに応じたモデルのカスタマイズを実現し、Qwen-Chat のスケーラビリティをさらに向上させることができます。

システム プロンプトを使用すると、Qwen-Chat は **ローリー プレイ**、**言語スタイルの転送**、**タスク設定**、**動作設定**を実現できます。

![](assets/system_prompt_ language_style.png)

![](assets/system_prompt_role_play_en.png)

詳細については、[サンプルドキュメント](examples/system_prompt.md)を参照してください。

## ツールの使用

Qwen-Chat は、ツールの使用法と関数呼び出し機能に合わせて最適化されています。 ユーザーはエージェント、LangChain アプリケーションを開発し、Python コード インタープリターで Qwen を拡張することもできます。

ReAct プロンプトの原則に基づいてツール呼び出しを実装する方法に関するドキュメントを提供しています。[ReAct の例](examples/react_prompt.md) を参照してください。 この原則に基づいて、[openai_api.py](openai_api.py) で関数呼び出しのサポートを提供します。

オープンソースの中国語評価ベンチマークでモデルのツール呼び出し機能をテストしたところ、Qwen-Chat が一貫して良好なパフォーマンスを発揮することがわかりました。

<table>
    <tr>
        <th colspan="4" align="center">Chinese Tool-Use Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th align="center">Model</th><th align="center">Tool Selection (Acc.↑)</th><th align="center">Tool Input (Rouge-L↑)</th><th align="center">False Positive Error↓</th>
    </tr>
    <tr>
        <td>GPT-4</td><td align="center">98.0%</td><td align="center">0.953</td><td align="center">23.9%</td>
    </tr>
    <tr>
        <td>GPT-3.5</td><td align="center">74.5%</td><td align="center">0.807</td><td align="center">80.6%</td>
    </tr>
    <tr>
        <td>Qwen-1_8B-Chat</td><td align="center">85.0%</td><td align="center">0.839</td><td align="center">27.6%</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td><td align="center">95.5%</td><td align="center">0.900</td><td align="center">11.6%</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td><td align="center">96.9%</td><td align="center">0.917</td><td align="center">5.6%</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td><td align="center">98.2%</td><td align="center">0.927</td><td align="center">1.1%</td>
    </tr>
</table>

数学的問題解決、データ視覚化、ファイル処理や Web スクレイピングなどのその他の汎用タスクに Python コード インタープリターを使用する Qwen の能力を評価するために、これらの能力を評価するために特別に設計されたベンチマークを作成し、オープンソース化しました。 。 ベンチマークはこの [リンク](https://github.com/QwenLM/Qwen-Agent/tree/main/benchmark) で見つけることができます。

Qwen は、コード生成時のコードの実行可能性と結果の精度の点で優れたパフォーマンスを発揮することがわかりました。

<table>
    <tr>
        <th colspan="5" align="center">Code Interpreter Benchmark (Version 20231206)</th>
    </tr>
    <tr>
        <th rowspan="2" align="center">Model</th>
        <th colspan="3" align="center">Accuracy of Code Execution Results (%)</th>
        <th colspan="1" align="center">Executable Rate of Code (%)</th>
    </tr>
    <tr>
        <th align="center">Math↑</th><th align="center">Visualization-Hard↑</th><th align="center">Visualization-Easy↑</th><th align="center">General↑</th>
    </tr>
    <tr>
        <td>GPT-4</td>
        <td align="center">82.8</td>
        <td align="center">66.7</td>
        <td align="center">60.8</td>
        <td align="center">82.8</td>
    </tr>
    <tr>
        <td>GPT-3.5</td>
        <td align="center">47.3</td>
        <td align="center">33.3</td>
        <td align="center">55.7</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>LLaMA2-13B-Chat</td>
        <td align="center">8.3</td>
        <td align="center">1.2</td>
        <td align="center">15.2</td>
        <td align="center">48.3</td>
    </tr>
    <tr>
        <td>CodeLLaMA-13B-Instruct</td>
        <td align="center">28.2</td>
        <td align="center">15.5</td>
        <td align="center">21.5</td>
        <td align="center">74.1</td>
    </tr>
    <tr>
        <td>InternLM-20B-Chat</td>
        <td align="center">34.6</td>
        <td align="center">10.7</td>
        <td align="center">25.1</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>ChatGLM3-6B</td>
        <td align="center">54.2</td>
        <td align="center">4.8</td>
        <td align="center">15.2</td>
        <td align="center">67.1</td>
    </tr>
    <tr>
        <td>Qwen-1.8B-Chat</td>
        <td align="center">25.6</td>
        <td align="center">21.4</td>
        <td align="center">22.8</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-7B-Chat</td>
        <td align="center">41.9</td>
        <td align="center">23.8</td>
        <td align="center">38.0</td>
        <td align="center">67.2</td>
    </tr>
    <tr>
        <td>Qwen-14B-Chat</td>
        <td align="center">58.4</td>
        <td align="center">31.0</td>
        <td align="center">45.6</td>
        <td align="center">65.5</td>
    </tr>
    <tr>
        <td>Qwen-72B-Chat</td>
        <td align="center">72.7</td>
        <td align="center">41.7</td>
        <td align="center">43.0</td>
        <td align="center">82.8</td>
    </tr>
</table>

<p align="center">
    <br>
    <img src="assets/code_interpreter_showcase_001.jpg" />
    <br>
<p>

<br>

## 長い文脈の理解

コンテキスト長を拡張し、トレーニング シーケンス長のボトルネックを解消するために、NTK 対応補間、ウィンドウ アテンション、LogN アテンション スケーリングなどのいくつかの技術を導入し、Qwen-14B のコンテキスト長を 2K から 8K 以上に拡張します。 トークン、および Qwen-1.8B/7B は 8K から 32K トークンまで。

Qwen-72B では、より大きな回転ベースを備えたより長いコンテキストに RoPE を適応させます。 Qwen-72B は、32K トークンの最大コンテキスト長をサポートします。

私たちは、PPL 評価を使用して arXiv データセットで言語モデリング実験を実施し、Qwen が長いコンテキストのシナリオで優れたパフォーマンスを達成できることを発見しました。 結果を以下に示します。

<table>
    <tr>
        <th rowspan="2">Model</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th><th align="center">16384</th><th align="center">32768</th>
    </tr>
     <tr>
        <td>Qwen-7B (original)</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">39.35</td><td align="center">469.81</td><td align="center">2645.09</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.59</td><td align="center">3.66</td><td align="center">5.71</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.58</td><td align="center">3.56</td><td align="center">4.62</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center">4.23</td><td align="center">3.78</td><td align="center">3.58</td><td align="center">3.49</td><td align="center">4.32</td><td align="center">-</td>
    </tr>
    <tr>
    <tr>
        <td>Qwen-1.8B</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.13</b></td><td align="center"><b>3.89</b></td><td align="center">17.42</td><td align="center">433.85</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>5.00</b></td><td align="center"><b>4.48</b></td><td align="center"><b>4.14</b></td><td align="center"><b>3.93</b></td><td align="center"><b>3.82</b></td><td align="center"><b>3.83</b></td>
    </tr>
    <tr>
        <td>Qwen-7B</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.31</b></td><td align="center">7.27</td><td align="center">181.49</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>4.23</b></td><td align="center"><b>3.81</b></td><td align="center"><b>3.52</b></td><td align="center"><b>3.33</b></td><td align="center"><b>3.22</b></td><td align="center"><b>3.17</b></td>
    </tr>
    <tr>
        <td>Qwen-14B</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center">22.79</td><td align="center">334.65</td><td align="center">3168.35</td><td align="center">-</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + window_attn</td><td align="center"><b>-</b></td><td align="center"><b>3.46</b></td><td align="center"><b>3.29</b></td><td align="center"><b>3.18</b></td><td align="center">3.42</td><td align="center">-</td>
    </tr>
    <tr>
        <td>Qwen-72B</td><td align="center"><b>-</b></td><td align="center"><b>-</b></td><td align="center">-</td><td align="center"><b>2.83</b></td><td align="center"><b>2.73</b></td><td align="center"><b>2.72</b></td>
    </tr>
    </tr>
</table>

さらに、Qwen-72B-Chat の長文理解能力を検証するために、[L-Eval](https://arxiv.org/abs/2307.11088) (クローズドエンド タスク) でテストしました。 結果は次のとおりです。

| Model             | Input Length | Average   |  Coursera  |    GSM     |   QuALITY  |    TOEFL   |   CodeU    |  SFcition  |
|:------------------|:------------:|:---------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| ChatGPT-3.5-16k   |     16K      |   60.73   | **63.51**  | **84.00**  |   61.38    |    78.43   | **12.22**  |    64.84   |
| **Qwen-72B-Chat** |     32K      | **62.30** |   58.13    |   76.00    | **77.22**  |  **86.24** |    6.66    |  **69.53** |

私たちは、モデルが入力内のさまざまな位置で情報を取得できるかどうかをテストするために、「干し草の山の中の針」実験 (このアイデアは [@Greg Kamradt](https://twitter.com/GregKamradt/status/1727018183608193393) から来ました) を実施しました。 異なる長さの場合、結果は次のようになります。
![](assets/qwen_72b_needle_in_a_haystack.png)

上記の結果は、Qwen-72B-Chat が 32K の入力長内でさまざまな位置に配置された情報を正確に取得できることを示しており、その優れた長文理解能力を証明しています。

## トークナイザー

tiktoken に基づくトークナイザーは、他のトークナイザー、例えばセンテンスピーストークナイザーとは異なります。特にファインチューニングの際には、特殊なトークンに注意を払う必要があります。トークナイザに関する詳細な情報や、ファインチューニングにおける使用方法については、[ドキュメント](tokenization_note_ja.md)を参照してください。
<br><br>

## 再現

ベンチマークデータセットでのモデル性能の再現のために、結果を再現するスクリプトを提供しています。詳しくは [eval/EVALUATION.md](eval/EVALUATION.md) を確認してください。なお、再現の結果、我々の報告結果と若干異なる場合があります。
<br><br>

## FAQ

問題が発生した場合は、まずは [FAQ](FAQ_ja.md) や issue を参照し、新しい issue を立ち上げる前に解決策を探してください。
<br><br>

## 引用
私たちの仕事が役に立ったと思ったら、遠慮なく引用してください。

```
@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
}
```
<br>

## ライセンス契約

<https://github.com/QwenLM/Qwen>で提供されるソースコードは、ルートディレクトリにある[Apache 2.0 License](./LICENSE)の下でライセンスされています。

研究者や開発者は、QwenとQwen-Chatのコードとモデルウェイトを自由に使用することができます。商用利用については、各モデルに添付されている使用許諾契約書をご確認ください。

- Qwen-72B、Qwen-14B、Qwen-7Bは、対応するHuggingFaceとModelScopeのリポジトリにある[Tongyi Qianwen LICENSE AGREEMENT](./Tongyi%20Qianwen%20LICENSE%20AGREEMENT)に基づいてライセンスされています。商用利用の場合は、フォーム([72B](https://dashscope.console.aliyun.com/openModelApply/Qwen-72B-Chat), [14B](https://dashscope.console.aliyun.com/openModelApply/Qwen-14B-Chat), [7B](https://dashscope.console.aliyun.com/openModelApply/qianwen))に記入して申請してください。

- Qwen-1.8Bは、対応するHuggingFaceとModelScopeのリポジトリにある[Tongyi Qianwen RESEARCH LICENSE AGREEMENT](./Tongyi%20Qianwen%20RESEARCH%20LICENSE%20AGREEMENT)に基づいてライセンスされています。商用利用については、私たちにご連絡ください。
<br><br>

## お問い合わせ

研究チームまたは製品チームへのメッセージは、qianwen_opensource@alibabacloud.com までお気軽にお送りください。

```

## File: `requirements.txt`
```
transformers>=4.32.0,<4.38.0
accelerate
tiktoken
einops
transformers_stream_generator==0.0.4
scipy
```

## File: `requirements_web_demo.txt`
```
gradio<3.42
mdtex2html
```

## File: `run_gptq.py`
```python
import argparse
import json
from typing import Dict
import logging

import torch
import transformers
from transformers import AutoTokenizer
from transformers.trainer_pt_utils import LabelSmoother
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
IGNORE_TOKEN_ID = LabelSmoother.ignore_index

def preprocess(
    sources,
    tokenizer: transformers.PreTrainedTokenizer,
    max_len: int,
    system_message: str = "You are a helpful assistant."
) -> Dict:
    roles = {"user": "<|im_start|>user", "assistant": "<|im_start|>assistant"}

    im_start = tokenizer.im_start_id
    im_end = tokenizer.im_end_id
    nl_tokens = tokenizer('\n').input_ids
    _system = tokenizer('system').input_ids + nl_tokens
    _user = tokenizer('user').input_ids + nl_tokens
    _assistant = tokenizer('assistant').input_ids + nl_tokens

    # Apply prompt templates
    data = []
    # input_ids, targets = [], []
    for i, source in enumerate(sources):
        source = source["conversations"]
        if roles[source[0]["from"]] != roles["user"]:
            source = source[1:]

        input_id, target = [], []
        system = [im_start] + _system + tokenizer(system_message).input_ids + [im_end] + nl_tokens
        input_id += system
        target += [im_start] + [IGNORE_TOKEN_ID] * (len(system)-3) + [im_end] + nl_tokens
        assert len(input_id) == len(target)
        for j, sentence in enumerate(source):
            role = roles[sentence["from"]]
            _input_id = tokenizer(role).input_ids + nl_tokens + \
                tokenizer(sentence["value"]).input_ids + [im_end] + nl_tokens
            input_id += _input_id
            if role == '<|im_start|>user':
                _target = [im_start] + [IGNORE_TOKEN_ID] * (len(_input_id)-3) + [im_end] + nl_tokens
            elif role == '<|im_start|>assistant':
                _target = [im_start] + [IGNORE_TOKEN_ID] * len(tokenizer(role).input_ids) + \
                    _input_id[len(tokenizer(role).input_ids)+1:-2] + [im_end] + nl_tokens
            else:
                raise NotImplementedError
            target += _target
        assert len(input_id) == len(target)
        input_id = torch.tensor(input_id[:max_len], dtype=torch.int)
        target = torch.tensor(target[:max_len], dtype=torch.int)
        data.append(dict(input_ids=input_id, attention_mask=input_id.ne(tokenizer.pad_token_id)))

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Model Quantization using AutoGPTQ")
    parser.add_argument("--model_name_or_path", type=str, help="model path")
    parser.add_argument("--data_path", type=str, help="calibration data path")
    parser.add_argument("--out_path", type=str, help="output path of the quantized model")
    parser.add_argument("--max_len", type=int, default=8192, help="max length of calibration data")
    parser.add_argument("--bits", type=int, default=4, help="the bits of quantized model. 4 indicates int4 models.")
    parser.add_argument("--group-size", type=int, default=128, help="the group size of quantized model")
    args = parser.parse_args()
    
    quantize_config = BaseQuantizeConfig(
        bits=args.bits,
        group_size=args.group_size,
        damp_percent=0.01,
        desc_act=False,  # set to False can significantly speed up inference but the perplexity may slightly bad
        static_groups=False,
        sym=True,
        true_sequential=True,
        model_name_or_path=None,
        model_file_base_name="model"
    )

    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path, trust_remote_code=True)
    tokenizer.pad_token_id = tokenizer.eod_id
    data = preprocess(json.load(open(args.data_path)), tokenizer, args.max_len)

    model = AutoGPTQForCausalLM.from_pretrained(args.model_name_or_path, quantize_config, device_map="auto", trust_remote_code=True)

    logging.basicConfig(
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
    )
    model.quantize(data, cache_examples_on_gpu=False)

    model.save_quantized(args.out_path, use_safetensors=True)
    tokenizer.save_pretrained(args.out_path)
```

## File: `tech_memo.md`
```markdown
# Introducing Qwen-7B: Open foundation and human-aligned models (of the state-of-the-arts)

Large language models have recently attracted an extremely large amount of
attention.
The boom of [ChatGPT](https://openai.com/blog/chatgpt) rocketed the development of artificial general intelligence and indicates that large language models compress world knowledge into neural networks, and the alignment to human cognition can lead to powerful conversational agents that can provide assistance by interacting with human users.
Now, the latest version of ChatGPT based on [GPT-4](https://arxiv.org/abs/2303.08774) demonstrates tremendously exciting performance across unlimited capabilities, say, language understanding, logical reasoning, planning, etc., and its incorporation with external tools, including tools and models, releases the power of an agent capable of understanding instructions, executing code, using tools, and so on, to reach the objectives set up by human users.

These significant progresses indicate the importance of large language models as _the foundation of AI services_.

We are happy to release the 7B-parameter models of our large pretrained model series Qwen (abbr. Tongyi Qianwen), Qwen-7B.
This release includes model weights and codes for pretrained and human-aligned language models of 7B parameters:

- `Qwen-7B` is the pretrained language model, and `Qwen-7B-Chat` is fine-tuned to align with human intent.
- `Qwen-7B` is pretrained on over 2.2 trillion tokens with a context length of 2048. On the series of benchmarks we tested, Qwen-7B generally performs better than existing open models of similar scales and appears to be on par with some of the larger models.
- `Qwen-7B-Chat` is fine-tuned on curated data, including not only task-oriented data but also specific security- and service-oriented data, which seems insufficient in existing open models.
- Example codes for fine-tuning, evaluation, and inference are included. There are also guides on long-context and tool use in inference.

**Goal of release**:
We believe that while the recent waves of releases of LLMs may have deepened our understanding of model behaviors under standard regimes, it is yet to be revealed how the accompanied techniques of nowadays LLMs, such as 1) quantization and fine-tuning after quantization, 2) training-free long-context inference, and 3) fine-tuning with service-oriented data, including search and tool uses, affect the models as a whole.
The open release of Qwen-7B marks our first step towards fully understanding the real-world application of such techniques.
It is our hope that it will enable the community to analyze and continue to improve the safety of those models, striving to establish responsible development and deployment of LLMs.

> **Disclaimer**:
> We must note that even though the weights and codes are released in an open manner and commercial use is not prohibited, similar to other pretrained language models, Qwen-7B comes with potential risks influenced by complex factors, including but not limited to over-diversified, inaccurate, or misleading generation.
> Developers and stakeholders should perform their own red teaming and provide related security measures before deployment, and they must abide by and comply with local governance and regulations.
> In no event shall the authors be held liable for any claim, damages, or other liability arising from the use of the released weights or codes.

The remainder of this document describes our pretraining and fine-tuning methodology.

## Pretraining

Qwen-7B is a transformer-based decoder-only language model with an architecture similar to the [LLaMA](https://github.com/facebookresearch/llama) series of models.
It is pretrained on over 2.2 trillion tokens with 2048 context length from publicly available data, covering general and professional fields with a focus on the English and Chinese languages.

### Data

**Pretraining data**:
Our training data includes a mix of data from publicly available sources, consisting mainly of web documents and code files.
Besides, the data are multilingual, with most of them in English and Chinese.
We made an effort and employed an ensemble of models to exclude data of low quality or deemed unfit for pretraining, such as NSFW content.
For math reasoning, we include RFT data from [gsm8k-ScRel](https://github.com/OFA-Sys/gsm8k-ScRel).
The final data underwent global fuzzy deduplication.
The mix of pretraining corpora has been optimized through numerous ablation experiments.

**Tokenization**:
Compared to the current mainstream open models based on Chinese and English vocabularies, we use a vocabulary of 151,851 tokens.
It first considers efficient encoding of Chinese, English, and code data, and is also more friendly to multilingual languages, enabling users to directly enhance the capability of some languages without expanding the vocabulary.
It segments numbers by single digits and calls the [tiktoken](https://github.com/openai/tiktoken) tokenizer library for efficient tokenization.
After tokenization, the data amounts to over 2.2 trillion tokens.

<figure>
    <img src="assets/tokenizer.png"
         alt="Tokenization efficiency"
         width="1200px">
    <figcaption>We randomly selected 1 million document corpora of each language to test and compare the encoding compression rates of different models (with XLM-R, which supports 100 languages, as the base value 1, not shown in the figure). As can be seen, while ensuring the efficient decoding of Chinese, English, and code, Qwen-7B also achieves a high compression rate for many other languages (such as th, he, ar, ko, vi, ja, tr, id, pl, ru, nl, pt, it, de, es, fr etc.), equipping the model with strong scalability as well as high training and inference efficiency in these languages.</figcaption>
</figure>

### Model

**Model architecture**:
Qwen-7B is built with architecture similar to LLaMA.
The following are the main differences from the standard transformer: 1) using untied embedding, 2) using rotary positional embedding, 3) no biases except for QKV in attention, 4) RMSNorm instead of LayerNorm, 5) SwiGLU instead of ReLU, and 6) adopting flash attention to accelerate training.
The model has 32 layers, the embedding dimension is 4096, and the number of attention heads is 32.

**Training details**:
The model is trained using the AdamW optimizer, with $\beta_1=0.9, \beta_2=0.95, \epsilon=10^{-6}$.
The sequence length is 2048, and the batch size is 2048, which means each optimization step accumulates over 4 million tokens.
We use a cosine learning rate schedule, with a warm-up of 2000 steps, a peak learning rate of $3 \times 10^{-4}$, and a minimum learning rate of 10% of the peak learning rate.
We use a weight decay of 0.1 and gradient clipping of 1.0.
The training adopts mixed precision training with `bfloat16`.


### Evaluation

We report results of Qwen-7B on standard benchmarks.

#### World knowledge

[C-Eval](https://arxiv.org/abs/2305.08322) is a common evaluation benchmark for testing the common-sense capability of pretrained models in Chinese. It covers 52 subjects in four major directions: humanities, social sciences, STEM, and other specialties. According to standard practice, we use the development set samples as the source of few-shot prompts to evaluate the 5-shot validation set and test set accuracy of the Qwen-7B pretrained model.

The accuracy comparison of the Qwen-7B model and other models on the C-Eval validation set is as follows:

| Model       |  Average |
| :---------- | -------: |
| Alpaca-7B   |     28.9 |
| Vicuna-7B   |     31.2 |
| ChatGLM-6B  |     37.1 |
| Baichuan-7B |     42.7 |
| ChatGLM2-6B |     50.9 |
| InternLM-7B |     53.4 |
| ChatGPT     |     53.5 |
| Claude-v1.3 |     55.5 |
| **Qwen-7B** | **60.8** |

The performance comparison of the Qwen-7B pretrained model and other models on the C-Eval test set is shown in the following table:

| Model                   | Avg.     | Avg. (Hard) | STEM | Social Sciences | Humanities | Others |
| :---------------------- | -------- | ----------: | ---: | --------------: | ---------: | -----: |
| ChatGLM-6B              | 38.9     |        29.2 | 33.3 |            48.3 |       41.3 |   38.0 |
| Chinese-Alpaca-Plus-13B | 41.5     |        30.5 | 36.6 |            49.7 |       43.1 |   41.2 |
| Baichuan-7B             | 42.8     |        31.5 | 38.2 |            52.0 |       46.2 |   39.3 |
| WestlakeLM-19B          | 44.6     |        34.9 | 41.6 |            51.0 |       44.3 |   44.5 |
| AndesLM-13B             | 46.0     |        29.7 | 38.1 |            61.0 |       51.0 |   41.9 |
| BatGPT-15B-sirius       | 47.0     |        31.9 | 42.7 |            57.5 |       48.6 |   43.6 |
| ChatGLM2-6B             | 51.7     |        37.1 | 48.6 |            60.5 |       51.3 |   49.8 |
| InternLM-7B             | 52.8     |        37.1 | 48.0 |            67.4 |       55.4 |   45.8 |
| Baichuan-13B            | 53.6     |        36.7 | 47.0 |            66.8 |       57.3 |   49.8 |
| Claude-v1.3             | 54.2     |        39.0 | 51.9 |            61.7 |       52.1 |   53.7 |
| ChatGPT                 | 54.4     |        41.4 | 52.9 |            61.8 |       50.9 |   53.6 |
| **Qwen-7B**             | **59.6** |        41.0 | 52.8 |            74.1 |       63.1 |   55.2 |

As can be seen, Qwen-7B achieves the best performance out of all existing models of similar scale and even surpasses larger-scale models.

MMLU is currently one of the most recognized benchmarks for evaluating English comprehension abilities, covering 57 subtasks across different academic fields and difficulty levels. The MMLU 5-shot accuracy performance of the Qwen-7B is shown in the following table:

| Model        |  Average | STEM | Social Sciences | Humanities | Others |
| :----------- | -------: | ---: | --------------: | ---------: | -----: |
| LLaMA-7B     |     35.1 | 30.5 |            38.3 |       34.0 |   38.1 |
| Baichuan-7B  |     42.3 | 35.6 |            48.9 |       38.4 |   48.1 |
| LLaMA2-7B    |     45.3 | 36.4 |            51.2 |       42.9 |   52.2 |
| LLaMA-13B    |     46.9 | 35.8 |            53.8 |       45.0 |   53.3 |
| ChatGLM2-6B  |     47.9 | 41.2 |            54.4 |       43.7 |   54.5 |
| InternLM-7B  |     51.0 |    - |               - |          - |      - |
| Baichuan-13B |     51.6 | 41.6 |            60.9 |       47.4 |   58.5 |
| LLaMA2-13B   |     54.8 | 44.1 |            62.6 |       52.8 |   61.1 |
| ChatGLM2-12B |     56.2 | 48.2 |            65.1 |       52.6 |   60.9 |
| **Qwen-7B**  | **56.7** | 47.6 |            65.9 |       51.5 |   64.7 |

In terms of English, Qwen-7B also surpasses other similar open pretrained models, and is competitive when compared to larger versions of other models.

#### Coding

We compared the code capabilities of pretrained models on [HumanEval](https://github.com/openai/human-eval), and the results are as follows:

| Model        |   Pass@1 |
| :----------- | -------: |
| Baichuan-7B  |      9.2 |
| ChatGLM2-6B  |      9.2 |
| InternLM-7B  |     10.4 |
| LLaMA-7B     |     10.5 |
| LLaMA2-7B    |     12.8 |
| Baichuan-13B |     12.8 |
| LLaMA-13B    |     15.8 |
| MPT-7B       |     18.3 |
| LLaMA2-13B   |     18.3 |
| **Qwen-7B**  | **24.4** |

#### Math

We compared the math capabilities of pretrained models on [GSM8K](https://github.com/openai/grade-school-math) (8-shot), and the results are as follows:

| Model        | Accuracy |
| :----------- | -------: |
| MPT-7B       |      6.8 |
| Falcon-7B    |      6.8 |
| Baichuan-7B  |      9.7 |
| LLaMA-7B     |     11.0 |
| LLaMA2-7B    |     14.6 |
| LLaMA-13B    |     17.8 |
| Baichuan-13B |     26.6 |
| LLaMA2-13B   |     28.7 |
| InternLM-7B  |     31.2 |
| ChatGLM2-6B  |     32.4 |
| ChatGLM2-12B |     40.9 |
| **Qwen-7B**  | **51.6** |

#### Natural language processing

We compared the translation capabilities of pre-trained models on WMT22 zh-en and en-zh (5-shot BLEU), and the results are as follows:

| Model       |  Average |    zh-en |    en-zh |
| :---------- | -------: | -------: | -------: |
| InternLM-7B |     11.8 |      9.0 |     14.5 |
| LLaMA-7B    |     12.7 |     16.7 |      8.7 |
| LLaMA-13B   |     15.8 |     19.5 |     12.0 |
| LLaMA2-7B   |     19.9 |     21.9 |     17.9 |
| Bloom-7B    |     20.3 |     19.1 |     21.4 |
| LLaMA2-13B  |     23.3 |     22.4 |     24.2 |
| PolyLM-13B  |     23.6 |     20.2 |     27.0 |
| Baichuan-7B |     24.6 |     22.6 |     26.6 |
| **Qwen-7B** | **27.5** | **24.3** | **30.6** |

#### Long-context inference

We include support for training-free long-context inference based on ntk-aware interpolation, LogN attention scaling, and local window attention.
The context can be expanded from 2048 to over 8192.
The following are the test results on arXiv in terms of perplexity (PPL).

<table>
	<tr>
        <th rowspan="2">Model</th><th colspan="5" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th><th align="center">16384</th>
    </tr>
    <tr>
        <td>Qwen-7B</td><td align="right"><b>4.23</b></td><td align="right"><b>3.78</b></td><td align="right">39.35</td><td align="right">469.81</td><td align="right">2645.09</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk</td><td align="right"><b>4.23</b></td><td align="right"><b>3.78</b></td><td align="right">3.59</td><td align="right">3.66</td><td align="right">5.71</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn</td><td align="right"><b>4.23</b></td><td align="right"><b>3.78</b></td><td align="right"><b>3.58</b></td><td align="right">3.56</td><td align="right">4.62</td>
    </tr>
    <tr>
        <td>+ dynamic_ntk + logn + local_attn</td><td align="right"><b>4.23</b></td><td align="right"><b>3.78</b></td><td align="right"><b>3.58</b></td><td align="right"><b>3.49</b></td><td align="right"><b>4.32</b></td>
    </tr>
</table>

## Fine-tuning

`Qwen-7B-Chat` embodies our practice in alignment with human intents, ensuring internalized safety, and building intelligent agents for services.

### Data

**Alignment data**:
The data includes common instruction-style conversations, and security- and service-oriented data, which involves substantial annotation efforts.
Instruction data covers broad abilities, such as writing, question answering, brainstorming and planning, content understanding, summarization, natural language processing, and coding.
Security data tries to prevent the model from generating harmful and inappropriate content.
Service data tries to enhance the model with specific conversation patterns that can be parsed to invoke and incorporate external systems.

**Data formatting**:
Since the data consists of conversation turns, we arrange them into texts using the [ChatML](https://github.com/openai/openai-python/blob/main/chatml.md) format, which is a meta language that can describe both the metadata (e.g., roles) and the content of a turn.
Currently, existing roles include system, user, and assistant.

### Model

**Training details**:
The causal language modeling objective is used to fine-tune the model, except for the tokens in the content of user's turns.
The model is trained using the AdamW optimizer, with $\beta_1=0.9, \beta_2=0.95, \epsilon=10^{-6}$.
The sequence length is limited to 2048, and the batch size is 128.
The model is trained for 4000 steps, and over the first 1430 steps, the learning rate is warmed up to $1 \times 10^{-5}$.
We use weight decay of 0.1, dropout of 0.1, and gradient clipping of 1.0.

### Evaluation

Evaluation of human-aligned models is non-trivial and often non-standardized, since such models often target specific applications.
We evaluate Qwen-7B-Chat from multiple perspectives.

#### World knowledge

As fine-tuning uses a much smaller dataset than pretraining and humans' understanding of world knowledge may be limited, we also evaluate the world knowledge of Qwen-7B-Chat using C-Eval and MMLU in a zero-shot and generative manner.

We demonstrate the zero-shot accuracy of Qwen-7B-Chat on the C-Eval validation set.

| Model                   | Avg. Acc. |
| :---------------------- | --------: |
| LLaMA2-7B-Chat          |      31.9 |
| LLaMA2-13B-Chat         |      40.6 |
| Chinese-Alpaca-2-7B     |      41.3 |
| Chinese-Alpaca-Plus-13B |      43.3 |
| Baichuan-13B-Chat       |      50.4 |
| ChatGLM2-6B-Chat        |      50.7 |
| InternLM-7B-Chat        |      53.2 |
| **Qwen-7B-Chat**        |  **54.2** |

The zero-shot accuracy of Qwen-7B-Chat on C-Eval testing set is provided below

| Model                   |     Avg. | STEM | Social Sciences | Humanities | Others |
| :---------------------- | -------: | ---: | --------------: | ---------: | -----: |
| Chinese-Alpaca-Plus-13B |     41.5 | 36.6 |            49.7 |       43.1 |   41.2 |
| Chinese-Alpaca-2-7B     |     40.3 |    - |               - |          - |      - |
| ChatGLM2-6B-Chat        |     50.1 | 46.4 |            60.4 |       50.6 |   46.9 |
| Baichuan-13B-Chat       |     51.5 | 43.7 |            64.6 |       56.2 |   49.2 |
| **Qwen-7B-Chat**        | **54.6** | 47.8 |            67.6 |       59.3 |   50.6 |

Compared with other models with comparable model sizes, the human-aligned Qwen-7B-Chat performs well in C-Eval accuracy.

The zero-shot accuracy of Qwen-7B-Chat on MMLU is provided below.
The performance of Qwen-7B-Chat is still on top among other human-aligned models with comparable size.

| Model             | Avg. Acc. |
| :---------------- | --------: |
| ChatGLM2-6B-Chat  |      45.5 |
| LLaMA2-7B-Chat    |      47.0 |
| InternLM-7B-Chat  |      50.8 |
| Baichuan-13B-Chat |      52.1 |
| ChatGLM2-12B-Chat |      52.1 |
| **Qwen-7B-Chat**  |  **53.9** |

#### Coding

The zero-shot Pass@1 of Qwen-7B-Chat on [HumanEval](https://github.com/openai/human-eval) is demonstrated below

| Model             |   Pass@1 |
| :---------------- | -------: |
| LLaMA2-7B-Chat    |     12.2 |
| InternLM-7B-Chat  |     14.0 |
| Baichuan-13B-Chat |     16.5 |
| LLaMA2-13B-Chat   |     18.9 |
| **Qwen-7B-Chat**  | **24.4** |

#### Math

The accuracy of Qwen-7B-Chat on GSM8K is shown below

| Model             | Zero-shot Acc. | 4-shot Acc. |
| :---------------- | -------------: | ----------: |
| ChatGLM2-6B-Chat  |              - |        28.0 |
| LLaMA2-7B-Chat    |           20.4 |        28.2 |
| LLaMA2-13B-Chat   |           29.4 |        36.7 |
| InternLM-7B-Chat  |           32.6 |        34.5 |
| Baichuan-13B-Chat |              - |        36.3 |
| ChatGLM2-12B-Chat |              - |        38.1 |
| **Qwen-7B-Chat**  |       **41.1** |    **43.5** |

#### Service

LLMs have shown capability in coordinating multiple external systems to achieve the given instructions, which creates new opportunities in traditional online services, the most notable being web search.

Qwen supports calling plugins/tools/APIs through [ReAct Prompting](https://arxiv.org/abs/2210.03629).
ReAct is also one of the main approaches used by the [LangChain](https://python.langchain.com/) framework.
For how to write and use prompts for ReAct Prompting, please refer to [the ReAct examples](examples/react_prompt.md).
In our evaluation [benchmark](eval/EVALUATION.md) for assessing tool usage capabilities, Qwen's performance is as follows:

| Model       | Tool Selection (Acc.↑)      | Tool Input (Rouge-L↑)      | False Positive Error↓      |
| :---------- | --------------------------: | -------------------------: | -------------------------: |
| GPT-4       |                         95% |                   **0.90** |                      15.0% |
| GPT-3.5     |                         85% |                       0.88 |                      75.0% |
| **Qwen-7B** |                     **99%** |                       0.89 |                   **9.7%** |

> The plugins that appear in the evaluation set do not appear in the training set of Qwen.
> This benchmark evaluates the accuracy of the model in selecting the correct plugin from multiple candidate plugins, the rationality of the parameters passed into the plugin, and the false positive rate.
> False Positive: Incorrectly invoking a plugin when it should not have been called when responding to a query.

Qwen also has the capability to be used as a [HuggingFace Agent](https://huggingface.co/docs/transformers/transformers_agents).
Its performance on the benchmark provided by HuggingFace is as follows:

| Model           | Tool Selection↑      | Tool Used↑      | Code↑      |
| :-------------- | -------------------: | --------------: | ---------: |
| GPT-4           |           **100.00** |      **100.00** |  **97.41** |
| GPT-3.5         |                95.37 |           96.30 |      87.04 |
| StarCoder-15.5B |                87.04 |           87.96 |      68.89 |
| **Qwen-7B**     |                90.74 |           92.59 |      74.07 |

## Conclusion

In this document, we describe Qwen-7B, including a pretrained model and a human-aligned model.
These models have demonstrated exciting performance compared to existing open models of similar or even larger scales.
As part of our ongoing commitment to the concept of Model as a Service, the release also includes practical pieces such as long context inference and external system integration, which we hope would facilitate developers realizing their own ideas and concepts.
We believe that the open release of Qwen-7B models would further our understanding of variables and techniques introduced in realistic settings and help to drive progress in this important area together with the community.
```

## File: `tokenization_note.md`
```markdown
# Tokenization

Qwen-7B uses BPE tokenization on UTF-8 bytes using the `tiktoken` package.
There are two types of tokens in Qwen-7B, i.e., the regular tokens (of type `bytes`) in BPE and the special/control tokens (of type `str`).

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen-7B', trust_remote_code=True)
```

## Regular tokens

The regular tokens are BPE tokens learned from byte sequences of texts encoded using the UTF-8 encoding.
While this allows tokenization of all texts and no unknown token exists, it may fall back to using single bytes when tokenizing uncommon texts.
You may encounter UTF-8 decoding errors and as the errors are default to `replace`, thus the replacement character (�) in incomplete generation.
You can change this behavior by passing `errors="ignore"` to the `decode` function for once or to the `from_pretrained` function forever.
For more options of `errors`, please refer to [the Python documentation](https://docs.python.org/3/library/stdtypes.html#bytes.decode).

```python
>>> tokenizer.decode([51461])
' �'

>>> tokenizer.convert_ids_to_tokens([51461])
[b' \xe6\xa0']

>>> b' \xe6\xa0'.decode("utf-8", errors='replace')
' �'

>>> tokenizer.decode([51461, 117])
' 根'

>>> tokenizer.convert_ids_to_tokens([51461, 117])
[b' \xe6\xa0', b'\xb9']

>>> b' \xe6\xa0\xb9'.decode("utf-8", errors='replace')
' 根'
```

The mapping from regular tokens (in `bytes`) to its ID can be retrieved from `tokenizer.get_vocab()`.
We do not support or recommended adding regular tokens to the vocabulary.

## Special tokens

The special tokens signify special functions to the model, e.g., reaching the end of a document.
In theory, they do not exist in the input texts and only appear after the input texts are processed.
Their surface forms, e.g., `<|endoftext|>` for the end of a document, are only meant for ease of reference.
Currently, used special tokens are `<|endoftext|>` in Qwen-7B, and `<|endoftext|>`, `<|im_start|>`, and `<|im_end|>` in Qwen-7B-Chat, which means they have determined meanings to the corresponding model, and should not be used otherwise.
For other purposes, we keep extra special tokens from `<|extra_0|>` to `<|extra_204|>`, and you can use them as you wish.
The mapping from surface forms of the special tokens (in `str`) to its ID can be retrieved from `tokenizer.special_tokens`.

The concepts of `bos`, `eos`, `unk`, `pad`, `mask`, `sep` and such are not appliable to our pretrained models (Qwen-7B and Qwen-7B-Chat).
The `pad` token, however, is a different story, as in theory, the model never sees or computes this token, so you may use any known token.
But to be safe, we limit the value of special tokens specified in the initialization of the tokenizer to the known special tokens.
You may specify special tokens in fine-tuning or in any other frameworks that necessitate them like this

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen-7B', trust_remote_code=True, pad_token='<|endoftext|>')
```

> WARNING: For our pretrained models, setting `bos`, `eos`, `unk`, and such makes no sense.
> Unknown behavior may be introduced if you set them without fine-tuning that designates their meanings to the model.
> Especially, you should not use `<|endoftext|>` as `eos`, unless you are sure that the end of a sentence and the end of a document, which may contain many sentences, are the same in your scenario.

## Injection attack prevention

As special tokens are different from regular tokens, what will happen if the surface forms of a control token appear in the input texts?
For example, note that a piece of text like this

```
print("<|endoftext|>")
```

should be tokenized as

```
ids:[1350, 9639, 91, 8691, 723, 427, 91, 82598]
tokens: [b'print', b'("<', b'|', b'endo', b'ft', b'ext', b'|', b'>")']
```

not

```
ids: [1350, 445, 151643, 899]
tokens: [b'print', b'("', '<|endoftext|>', b'")']
```

Our default used to be the correct one, that is, treating the surface forms of special tokens just like regular texts, and special tokens should be taken cared of by developers after tokenization of the texts.
However, this conflicts with (albeit unsafe) practice in the community, and adds another step for developers to reuse their wheels.

The default behavior has been changed to parse the surface forms of all the known special tokens as special tokens.
To enable injection prevention, pass `allowed_special=set()` to the calls of the tokenizer:

```python
>>> tokenizer('print("<|endoftext|>")', allowed_special=set())
{'input_ids': [1350, 9639, 91, 8691, 723, 427, 91, 82598], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1]}
```

You can control the behavior in a fine-grained manner by passing a set of `str` as `allowed_special`

```python
>>> tokenizer('print("<|extra_0|>")<|endoftext|>', allowed_special={'<|endoftext|>'})
{'input_ids': [1350, 9639, 91, 15460, 62, 15, 91, 82598, 151643], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1]}
```

You can also make the tokenizer raise errors if the surface forms of certain special tokens are encountered in the input texts by passing a collection of `str` as `disallowed_special`

```python
>>> tokenizer('print("<|extra_0|>")<|endoftext|>', allowed_special={'<|endoftext|>'}, disallowed_special=('<|extra_0|>', ))
...
ValueError: Encountered text corresponding to disallowed special token '<|extra_0|>'.
If you want this text to be encoded as a special token, pass it to `allowed_special`, e.g. `allowed_special={'<|extra_0|>', ...}`.
If you want this text to be encoded as normal text, disable the check for this token by passing `disallowed_special=(enc.special_tokens_set - {'<|extra_0|>'})`.
To disable this check for all special tokens, pass `disallowed_special=()`.
```

For more information on `allowed_special` and `disallowed_special`, please refer to [the `tiktoken` documentation](https://github.com/openai/tiktoken/blob/095924e02c85617df6889698d94515f91666c7ea/tiktoken/core.py#L75).

The new default is the same as

```python
>>> tokenizer('print("<|endoftext|>")', allowed_special="all", disallowed_special=())
{'input_ids': [1350, 445, 151643, 899], 'token_type_ids': [0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1]}
```

## Vocabulary Expansion

> WARNING: Read carefully, be aware of what you are doing, and use at your own risk. 
> There are certain caveats regarding how your vocabulary is produced.

The tokenizer of Qwen models are based on BPE and you cannot directly expand the vocabulary by adding words to the vocabulary. 
The intermediate merges are needed for tokenization.
Please follow the steps to obtain such information.

1. Prepare a plain text file `qwen_extra_vocab.txt`, where each line contains a token and its frequency separated by `\t`. 

   An example is given below:
   ```
   我是一只猫	20
   你是一只猫	10
   他是一只猫	5
   一只	200
   一只猫	100
   夸张的 比喻手法	20
   ```
   The frequencies are needed to compute the BPE.

   

2. Prepare the base vocabulary file, e.g., `qwen.tiktoken`, and determine the start index for new tokens.
   
   There are 151,643 regular tokens and 208 control tokens in the vocabulary for Qwen models. 
   For simplicity, the start index can be set as 151,851, which is the default value. 
   You can, of course, override the many inactive control tokens, but you will need to modify the tokenizer code. 

3. Run the following command:
   ```
   python add_merges.py qwen.tiktoken qwen_extra.tiktoken qwen_extra_vocab.txt
   ```
   `add_merges.py` can be found [here](examples/add_merges.py).
   It will learn the new merges based on the provided `qwen_extra_vocab.txt`. 
   The new tokens and their indices will be stored in `qwen_extra.tiktoken`. 
   Modify the paths as you wish.

   It is a pure Python implementation, so please expect it to be slow if you are adding a lot of words.

   Please note that not all words can be added due to pre-tokenization. 
   You will get warnings if you try to add such word:
   ```
   WARNING - 夸张的 比喻手法 would be pre-tokenized to ['夸张的', ' 比喻手法'], and thus cannot be added to vocabulary
   WARNING - word 一只 is already a token b'\xe4\xb8\x80\xe5\x8f\xaa', skipping
   INFO - number of existing merges: 151643
   INFO - number of words for expanding: 4
   DEBUG - (b'\xe4\xb8\x80\xe5\x8f\xaa', b'\xe7\x8c\xab') (一只猫) is selected as the next merge with freq 100
   DEBUG - (b'\xe5\x8f\xaa', b'\xe7\x8c\xab') (只猫) is selected as the next merge with freq 35
   DEBUG - (b'\xe6\x98\xaf\xe4\xb8\x80', b'\xe5\x8f\xaa\xe7\x8c\xab') (是一只猫) is selected as the next merge with freq 35
   DEBUG - (b'\xe6\x88\x91', b'\xe6\x98\xaf\xe4\xb8\x80\xe5\x8f\xaa\xe7\x8c\xab') (我是一只猫) is selected as the next merge with freq 20
   DEBUG - (b'\xe4\xbd\xa0', b'\xe6\x98\xaf\xe4\xb8\x80\xe5\x8f\xaa\xe7\x8c\xab') (你是一只猫) is selected as the next merge with freq 10
   DEBUG - (b'\xe4\xbb\x96', b'\xe6\x98\xaf\xe4\xb8\x80\xe5\x8f\xaa\xe7\x8c\xab') (他是一只猫) is selected as the next merge with freq 5
   INFO - number of newly learned merges: 6
   ```

The `qwen_extra.tiktoken` will contain the following lines:
```
5LiA5Y+q54yr 151851
5Y+q54yr 151852
5piv5LiA5Y+q54yr 151853
5oiR5piv5LiA5Y+q54yr 151854
5L2g5piv5LiA5Y+q54yr 151855
5LuW5piv5LiA5Y+q54yr 151856
```

You may use the file as follows in your code:
``` python
from transformers import AutoTokenizer

>>> tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True, extra_vocab_file="qwen_extra.tiktoken")

>>> len(tokenizer)
151857

>>> tokenizer("我是一只猫")
{'input_ids': [151854], 'token_type_ids': [0], 'attention_mask': [1]}
```
Note: You need the latest tokenizer code, i.e., after 2023-10-08, to use the `extra_vocab_file` argument.
Otherwise, you need to manually append `qwen.tiktoken` (of which path varies with your configuration) with the content from `qwen_extra.tiktoken`.

Certainly, you will need to finetune the model for the new tokens to work.


### Caveats


The tokenizer of Qwen operates directly on UTF-8 byte sequences, unlike others, e.g., SentencePiece that operates on Unicode codepoints/characters and falls back to UTF-8 byte sequences for the unknown (IIRC). 
The thing is if the frequencies are computed on limited data, the Unicode codepoint boundary may not be correctly recognized.
In theory, it could be a problem for fine-tuned models using the expanded vocabulary with limited data.

For example, it could happen that `b'\x80\xe5'` might be merged first for the UTF-8 byte sequence `b'\xe4\xb8\x80\xe5\x8f\xaa'` of the string `一只`, across the Unicode codepoint of `一` (`b'\xe4\xb8\x80'`) and `只` (`b'\xe5\x8f\xaa'`).
Normally, this would work just fine for known tokens, but for actually unknown words, unusual merges may happen, which may not be well understood for the pre-trained model.

Our advice is that to be safe, you should gather the Unicode codepoints from all the words you need to add, and also add them to the file with frequencies higher than the sum of the frequencies of the corresponding words.
But since Qwen has most of the Chinese words, it could be okay to just add the Chinese words alone.

For curious minds, you will also notice that in the given example, `一只` is a token and `只猫` is also learned as a new token. 
The reason is that `是一` is also a token in Qwen and has higher merging priority than `一只`, such that the merging path for `是|一|只|猫` is `是一|只|猫 -> 是一|只猫 -> 是一只猫` (omitting the UTF-8 byte merges).

This is the characteristic for plain BPE: it is based solely on distribution, meaning it does not have knowledge of which bytes can form a valid Unicode codepoint, character, or meaningful word.

The byproduct is that text may be sub-tokenized differently in different contexts, even for words containing only ASCII characters.
```python
>>> tokenizer.tokenize("Panda")
[b'P', b'anda']

>>> tokenizer.tokenize(" Panda")
[b' Panda']

>>> tokenizer.tokenize("Pandas")
[b'P', b'andas']

>>> tokenizer.tokenize(" Pandas")
[b' Pand', b'as']
```
This simply suggests that those combinations occur more frequently in the data.
If you have vast amount of training data, it should not be a problem.
```

## File: `tokenization_note_ja.md`
```markdown
# トークン化

Qwen-7B は `tiktoken` パッケージを使用して、UTF-8 バイトを BPE トークン化します。
Qwen-7B には 2 種類のトークンがあります。BPE の通常のトークン (`bytes` 型) と特殊/制御トークン (`str` 型) です。

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen-7B', trust_remote_code=True)
```

## 通常のトークン

通常のトークンは、UTF-8 エンコーディングでエンコードされたテキストのバイト列から学習した BPE トークンです。
これによってすべてのテキストをトークン化することができ、未知のトークンは存在しませんが、一般的でないテキストをトークン化するときにシングルバイトを使用するようにフォールバックすることがあります。
UTF-8 のデコードエラーに遭遇することがあり、そのエラーのデフォルトは `replace` であるため、不完全な生成では置換文字 (�) が使用されます。
この動作は `errors="ignore"` を `decode` 関数に渡すことで変更することができる。
`errors` のオプションについては、[Python ドキュメント](https://docs.python.org/3/library/stdtypes.html#bytes.decode) を参照してください。

```python
>>> tokenizer.decode([51461])
' �'

>>> tokenizer.convert_ids_to_tokens([51461])
[b' \xe6\xa0']

>>> b' \xe6\xa0'.decode("utf-8", errors='replace')
' �'

>>> tokenizer.decode([51461, 117])
' 根'

>>> tokenizer.convert_ids_to_tokens([51461, 117])
[b' \xe6\xa0', b'\xb9']

>>> b' \xe6\xa0\xb9'.decode("utf-8", errors='replace')
' 根'
```

通常のトークン (`bytes` 単位) からその ID へのマッピングは `tokenizer.get_vocab()` から取得できます。
通常のトークンを語彙に追加することはサポートしていませんし、推奨もしていません。

## 特別なトークン

特別なトークンは、例えば文書の最後に到達するなど、モデルにとって特別な機能を意味します。
理論的には、これらは入力テキストには存在せず、入力テキストが処理された後にのみ現れます。
例えば、文書の終わりを表す `<|endoftext|>` のような表面的な形は、参照を容易にするためだけのものである。
現在、Qwen-7B では `<|endoftext|>` が、Qwen-7B-Chat では `<|endoftext|>`, `<|im_start|>`, `<|im_end|>` が特殊トークンとして使われています。
他の目的のために、`<|extra_0|>` から `<|extra_204|>` までの特別なトークンを保持しています。
特殊トークンの表面形式 (`str` 内) から ID へのマッピングは `tokenizer.special_tokens` から取得できます。

`bos`、`eos`、`unk`、`pad`、`mask`、`sep` などの概念は学習済みモデル（Qwen-7B と Qwen-7B-Chat）には適用できません。
しかし、`pad` トークンは話が別です。理論的には、モデルがこのトークンを見たり計算したりすることはないので、既知のトークンを使用することができます。
しかし、安全のために、トークナイザーの初期化で指定する特別なトークンの値は、既知の特別なトークンに限定します。
微調整やその他のフレームワークで特別なトークンを必要とする場合は、次のように指定できます

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen-7B', trust_remote_code=True, pad_token='<|endoftext|>')
```

> 警告: 私たちが事前に学習したモデルでは、`bos`, `eos`, `unk` などを設定しても意味がありません。
> 特に、`<<endoftext|>` を `eos` のように使ってはいけません。
> 特に `<|endoftext|>` を `eos` として使用することは、文末と文末が同じであると確信できる場合を除き、避けるべきです。

## インジェクション攻撃の防止

特殊トークンは通常のトークンとは異なるため、コントロールトークンの表面形が入力テキストに現れるとどうなるでしょうか？
例えば、次のようなテキストがあるとします

```
print("<|endoftext|>")
```

これは次のようにしてトークン化する必要があります

```
ids:[1350, 9639, 91, 8691, 723, 427, 91, 82598]
tokens: [b'print', b'("<', b'|', b'endo', b'ft', b'ext', b'|', b'>")']
```

こちらではありません

```
ids: [1350, 445, 151643, 899]
tokens: [b'print', b'("', '<|endoftext|>', b'")']
```

つまり、特殊トークンの表面形は通常のテキストと同じように扱い、特殊トークンはテキストのトークン化後に開発者が処理するというものです。
しかし、これはコミュニティにおける（安全ではないとはいえ）慣習に抵触し、開発者が車輪を再利用するための新たなステップを追加することになります。

デフォルトの動作は、すべての既知の特殊トークンの表面形を特殊トークンとして解析するように変更されました。
インジェクション防止を有効にするには、トークナイザーの呼び出しに `allowed_special=set()` を渡します:

```python
>>> tokenizer('print("<|endoftext|>")', allowed_special=set())
{'input_ids': [1350, 9639, 91, 8691, 723, 427, 91, 82598], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1]}
```

`str` のセットを `allowed_special` として渡すことで、きめ細かく動作を制御することができます

```python
>>> tokenizer('print("<|extra_0|>")<|endoftext|>', allowed_special={'<|endoftext|>'})
{'input_ids': [1350, 9639, 91, 15460, 62, 15, 91, 82598, 151643], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1]}
```

`str` のコレクションを `disallowed_special` として渡すことで、特定の特殊なトークンの表形式が入力テキストで遭遇した場合にトークナイザーがエラーを発生するようにすることもできます

```python
>>> tokenizer('print("<|extra_0|>")<|endoftext|>', allowed_special={'<|endoftext|>'}, disallowed_special=('<|extra_0|>', ))
...
ValueError: Encountered text corresponding to disallowed special token '<|extra_0|>'.
If you want this text to be encoded as a special token, pass it to `allowed_special`, e.g. `allowed_special={'<|extra_0|>', ...}`.
If you want this text to be encoded as normal text, disable the check for this token by passing `disallowed_special=(enc.special_tokens_set - {'<|extra_0|>'})`.
To disable this check for all special tokens, pass `disallowed_special=()`.
```

`allowed_special` と `disallowed_special` の詳細については、[`tiktoken` ドキュメント](https://github.com/openai/tiktoken/blob/095924e02c85617df6889698d94515f91666c7ea/tiktoken/core.py#L75)を参照してください。

新しいデフォルトは以下の通り

```python
>>> tokenizer('print("<|endoftext|>")', allowed_special="all", disallowed_special=())
{'input_ids': [1350, 445, 151643, 899], 'token_type_ids': [0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1]}
```

```

## File: `tokenization_note_zh.md`
```markdown
# Tokenization

> 注：作为术语的“tokenization”在中文中尚无共识的概念对应，本文档采用英文表达以利说明。

Qwen-7B采用UTF-8字节级别的BPE tokenization方式，并依赖`tiktoken`这一高效的软件包执行分词。
Qwen-7B中有两类token，即源于BPE、`bytes`类型的普通token和特殊指定、`str`类型的特殊token。

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen-7B', trust_remote_code=True)
```

## 普通token

普通token源于BPE，是在UTF-8编码的文本字节序列上学习得到的。
尽管基于字节序列的方式保证了所有文本均可被tokenize且没有未登录token问题，但处理罕见文本时有可能回退到字节级别的编码。
由于从字节序列解码为文本时，`errors`参数设为`replace`，处理不完整的token序列可能会遇到UTF-8解码错误，表象是生成中包含“替换字符”(�)。
这一行为可以通过将`errors`参数设为`ignore`来规避。
一次性修改可以传入tokenizer的`decode`函数，持久性修改可以传入tokenizer的初始化函数，请注意`decode`的配置优先级更高。
`errors`的可选值，请参阅[Python文档](https://docs.python.org/3/library/stdtypes.html#bytes.decode).

```python
>>> tokenizer.decode([51461])
' �'

>>> tokenizer.convert_ids_to_tokens([51461])
[b' \xe6\xa0']

>>> b' \xe6\xa0'.decode("utf-8", errors='replace')
' �'

>>> tokenizer.decode([51461, 117])
' 根'

>>> tokenizer.convert_ids_to_tokens([51461, 117])
[b' \xe6\xa0', b'\xb9']

>>> b' \xe6\xa0\xb9'.decode("utf-8", errors='replace')
' 根'
```

`bytes`类型的普通token到id的映射可以通过`tokenizer.get_vocab()`获取。
尚不支持也不推荐向tokenizer增加普通token。

## 特殊token

特殊token用以给模型传递特殊信号，如到达文本末尾。
理论上，输入文本中不包含特殊token，它们仅在tokenization后由开发者手动加入。
特殊token的字面表达，如表示文本结束的`<|endoftext|>`，仅便于指代特殊token，不意味着它们在输入文本空间中。
目前，训练中使用的、已经有固定含义的、不应做它用的特殊token，Qwen-7B中有`<|endoftext|>`，Qwen-7B-Chat中有`<|endoftext|>`、`<|im_start|>`以及`<|im_end|>`。
但词表中也留有供扩展的特殊token位，可用`<|extra_0|>`到`<|extra_204|>`来指代。
`str`类型的特殊token字面表达到id的映射，可以通过`tokenizer.special_tokens`获取。

对于提供的模型参数(Qwen-7B和Qwen-7B-Chat)而言，诸如`bos`、`eos`、`unk`、`pad`、`mask`、`sep`等的特殊token的概念并不适用。
特例是`pad`，由于这个token理论上并不参与模型计算，所以可以使用任意token表达这一概念。
但保险起见，目前可在tokenizer初始化时设定的特殊token，仅可使用已知的特殊token字面表达，即`<|endoftext|>`、`<|im_start|>`、`<|im_end|>`和`<|extra_0|>`到`<|extra_204|>`。
对于微调或者其它需要这些token才能运行的框架，可以如下配置

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen-7B', trust_remote_code=True, pad_token='<|endoftext|>')
```

> 注意: 对于提供的训练好的模型，设置诸如`bos`、`eos`、`unk`之类的没有意义，即模型不需要这些概念。
> 如果设置了这些token，但没有相应的微调这些token以让模型理解其含义，未知行为可能被触发。
> 特别时，不应混淆`<|endoftext|>`和`eos`的概念，除非应用场景中它们的实际含义是一致的，即句子末尾等价于文本末尾。

**注入攻击防御**

由于特殊token和普通token概念上的差异，如果输入文本中含有特殊token的字面表达该如何处理？
以下面文本为例

```
print("<|endoftext|>")
```

其正确的tokenization为

```
ids:[1350, 9639, 91, 8691, 723, 427, 91, 82598]
tokens: [b'print', b'("<', b'|', b'endo', b'ft', b'ext', b'|', b'>")']
```

不是

```
ids: [1350, 445, 151643, 899]
tokens: [b'print', b'("', '<|endoftext|>', b'")']
```

默认行为曾是正确的，即输入文本中任何字符一律按普通token处理，特殊token应由开发者在tokenization人工处理。
然后，这与社区中的实践似有差异，为开发者复用代码增加了额外适配步骤。

默认行为已被调整为从输入文本中解析特殊token的字面表达。
如需启用注入攻击防御，请传入参数`allowed_special=set()`：

```python
>>> tokenizer('print("<|endoftext|>")', allowed_special=set())
{'input_ids': [1350, 9639, 91, 8691, 723, 427, 91, 82598], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1]}
```

这一行为可以更精细的调控，将`allowed_special`设计为`str`的集合即可：

```python
>>> tokenizer('print("<|extra_0|>")<|endoftext|>', allowed_special={'<|endoftext|>'})
{'input_ids': [1350, 9639, 91, 15460, 62, 15, 91, 82598, 151643], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1]}
```

如果希望输入中遇到特殊token的字面表达时，获得更直接的提醒，通过配置`disallowed_special`可以让tokenizer直接触发异常：

```python
>>> tokenizer('print("<|extra_0|>")<|endoftext|>', allowed_special={'<|endoftext|>'}, disallowed_special=('<|extra_0|>', ))
...
ValueError: Encountered text corresponding to disallowed special token '<|extra_0|>'.
If you want this text to be encoded as a special token, pass it to `allowed_special`, e.g. `allowed_special={'<|extra_0|>', ...}`.
If you want this text to be encoded as normal text, disable the check for this token by passing `disallowed_special=(enc.special_tokens_set - {'<|extra_0|>'})`.
To disable this check for all special tokens, pass `disallowed_special=()`.
```

更多关于`allowed_special`和`disallowed_special`的信息, 请参阅[`tiktoken`代码](https://github.com/openai/tiktoken/blob/095924e02c85617df6889698d94515f91666c7ea/tiktoken/core.py#L75).

新的默认行为与以下设定等价

```python
>>> tokenizer('print("<|endoftext|>")', allowed_special="all", disallowed_special=())
{'input_ids': [1350, 445, 151643, 899], 'token_type_ids': [0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1]}
```

## 词表扩展

> 特别提醒：请仔细阅读本部分的说明，理解每一步操作，并承担可能的后果。
> 由于词表扩展部分由您提供，产出方式的差异可能导致特定的不兼容情况，请审慎操作。

Qwen系列模型的tokenizer基于BPE方案提取文本中的token。
从UTF-8编码的字节开始（每个字节都可以是一个token），两两token合并成为新token，直至不能再合并出新的token为止。
由于词表同时还记录了token的合并方式，直接向词表中添加词可能对Qwen的tokenizer并不适用，即通过已有的token可能合并不出来您添加词。

因而，请参照以下步骤获得合并信息：

1. 准备一个纯文本文件，例如名为`qwen_extra_vocab.txt`，每行一个待添加的词和它的频率，中间用制表符`\t`分隔。

   以下是一个文件的例子：
   ```
   我是一只猫	20
   你是一只猫	10
   他是一只猫	5
   一只	200
   一只猫	100
   夸张的 比喻手法	20  
   ```
   频率是必需的，用来计算合并的优先级。

2. 准备基础的词表文件，例如`qwen.tiktoken`，并确认新加入token的起始索引。

   Qwen模型词表中有151,643个普通token，有208个特殊token。
   简单起见，起始索引可以设置为151,851（默认值）。
   您可以覆写不起效的特殊token，但您需要相应的修改tokenizer代码。

3. 运行以下命令：
   ```
   python add_merges.py qwen.tiktoken qwen_extra.tiktoken qwen_extra_vocab.txt
   ```
   `add_merges.py`代码在[GitHub存储库](examples/add_merges.py)中。
   基于提供的`qwen_extra_vocab.txt`，该脚本将学习新的token合并方式。
   新token及其索引将存储在`qwen_extra.tiktoken`文件中。
   您可以视情况修改有关路径。

   由于是纯Python实现，如果您添加了非常多的词，预期会花费较多时间。

   请注意，由于预切分，有些词是无法作为token加入的。
   如果您添加了这些词，您会收到警告：
   ```
   WARNING - 夸张的 比喻手法 would be pre-tokenized to ['夸张的', ' 比喻手法'], and thus cannot be added to vocabulary
   WARNING - word 一只 is already a token b'\xe4\xb8\x80\xe5\x8f\xaa', skipping
   INFO - number of existing merges: 151643
   INFO - number of words for expanding: 4
   DEBUG - (b'\xe4\xb8\x80\xe5\x8f\xaa', b'\xe7\x8c\xab') (一只猫) is selected as the next merge with freq 100
   DEBUG - (b'\xe5\x8f\xaa', b'\xe7\x8c\xab') (只猫) is selected as the next merge with freq 35
   DEBUG - (b'\xe6\x98\xaf\xe4\xb8\x80', b'\xe5\x8f\xaa\xe7\x8c\xab') (是一只猫) is selected as the next merge with freq 35
   DEBUG - (b'\xe6\x88\x91', b'\xe6\x98\xaf\xe4\xb8\x80\xe5\x8f\xaa\xe7\x8c\xab') (我是一只猫) is selected as the next merge with freq 20
   DEBUG - (b'\xe4\xbd\xa0', b'\xe6\x98\xaf\xe4\xb8\x80\xe5\x8f\xaa\xe7\x8c\xab') (你是一只猫) is selected as the next merge with freq 10
   DEBUG - (b'\xe4\xbb\x96', b'\xe6\x98\xaf\xe4\xb8\x80\xe5\x8f\xaa\xe7\x8c\xab') (他是一只猫) is selected as the next merge with freq 5
   INFO - number of newly learned merges: 6
   ```

`qwen_extra.tiktoken`会包含以下内容：
```
5LiA5Y+q54yr 151851
5Y+q54yr 151852
5piv5LiA5Y+q54yr 151853
5oiR5piv5LiA5Y+q54yr 151854
5L2g5piv5LiA5Y+q54yr 151855
5LuW5piv5LiA5Y+q54yr 151856
```

您可以按如下方式使用扩展后的词表：
``` python
from transformers import AutoTokenizer

>>> tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True, extra_vocab_file="qwen_extra.tiktoken")

>>> len(tokenizer)
151857

>>> tokenizer("我是一只猫")
{'input_ids': [151854], 'token_type_ids': [0], 'attention_mask': [1]}
```

注意：您需要使用2023年10月8日后的tokenizer代码才能传递`extra_vocab_file`参数。如是其它情况，您可以将`qwen_extra.tiktoken`内容复制粘贴到`qwen.tiktoken`内容后面。

您需要微调模型才能使新的token发挥作用。

### 注意事项

Qwen的tokenizer是直接从UTF-8编码的字节序列开始处理的，这与其它tokenizer比如SentencePiece是很不一样的。SentencePiece是从Unicode码位（可以理解为一个字符）开始处理，遇到未登录的再用UTF-8编码成字节。
从字节开始的一个潜在问题是如果频率信息不够准确，比如频率信息是在很少数据上统计得到的，Unicode码位按UTF-8编码成字节后的边界可能会出现差错。
理论上，如果模型微调数据量不足，使用扩展后的词表也可能出现意外问题。

举个例子（非实际情况），对于`一只`的UTF-8字节序列`b'\xe4\xb8\x80\xe5\x8f\xaa'`，中间两个字节`b'\x80\xe5'`可能会先合并为一个token，跨越了`一`(`b'\xe4\xb8\x80'`)和`只`(`b'\xe5\x8f\xaa'`)的码位边界。
这对于已登录token不会有什么影响（最后总会合并为`一只`），但对于未登录的，可能会产生一些不同寻常的合并/token。
这些token序列可能对于预训练模型是陌生的。

我们的建议是保险起见，您最好先收集待添加词中的所有Unicode码位，然后单独指定它们的频率大于其所构成词的频率之和。
不过由于Qwen的tokenizer已包含了大多数中文字，对于中文词的话，不添加中文字的频率，大部分情况下是可行的。

您可能已经发现了，在提供的例子中，`一只`已经是登录过的token了，但`只猫`还是学习成为了一个新token，出现了“交叉”。
原因是在Qwen中`是一`也是一个已知token，且其频率/优先级比`一只`要高，因而对于`是|一|只|猫`这个片段，合并的次序是`是一|只|猫 -> 是一|只猫 -> 是一只猫`（省略UTF-8字节级别的合并）。

这是常规BPE的特性，其完全基于分布，并不知道哪些字节可以构成合法的Unicode码位、合法的字符或是词。

副产物是一段文本在不同的上下文下可能会有不同的tokenize结果，对于仅包含ASCII字符的文本同样如此。
```python
>>> tokenizer.tokenize("Panda")
[b'P', b'anda']

>>> tokenizer.tokenize(" Panda")
[b' Panda']

>>> tokenizer.tokenize("Pandas")
[b'P', b'andas']

>>> tokenizer.tokenize(" Pandas")
[b' Pand', b'as']
```
这仅说明在用于学习BPE的数据中，这样的组合是更高频的。
如果您有海量的训练语料，这并不会是个问题。
```

## File: `Tongyi Qianwen LICENSE AGREEMENT`
```
Tongyi Qianwen LICENSE AGREEMENT

Tongyi Qianwen Release Date: August 3, 2023

By clicking to agree or by using or distributing any portion or element of the Tongyi Qianwen Materials, you will be deemed to have recognized and accepted the content of this Agreement, which is effective immediately.

1. Definitions
    a. This Tongyi Qianwen LICENSE AGREEMENT (this "Agreement") shall mean the terms and conditions for use, reproduction, distribution and modification of the Materials as defined by this Agreement.
    b. "We"(or "Us") shall mean Alibaba Cloud.
    c. "You" (or "Your") shall mean a natural person or legal entity exercising the rights granted by this Agreement and/or using the Materials for any purpose and in any field of use.
    d. "Third Parties" shall mean individuals or legal entities that are not under common control with Us or You.
    e. "Tongyi Qianwen" shall mean the large language models (including Qwen model and Qwen-Chat model), and software and algorithms, consisting of trained model weights, parameters (including optimizer states), machine-learning model code, inference-enabling code, training-enabling code, fine-tuning enabling code and other elements of the foregoing distributed by Us.
    f. "Materials" shall mean, collectively, Alibaba Cloud's proprietary Tongyi Qianwen and Documentation (and any portion thereof) made available under this Agreement.
    g. "Source" form shall mean the preferred form for making modifications, including but not limited to model source code, documentation source, and configuration files.
    h. "Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation,
 and conversions to other media types.

2. Grant of Rights
You are granted a non-exclusive, worldwide, non-transferable and royalty-free limited license under Alibaba Cloud's intellectual property or other rights owned by Us embodied in the Materials to use, reproduce, distribute, copy, create derivative works of, and make modifications to the Materials.

3. Redistribution
You may reproduce and distribute copies of the Materials or derivative works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:
    a. You shall give any other recipients of the Materials or derivative works a copy of this Agreement;
    b. You shall cause any modified files to carry prominent notices stating that You changed the files;
    c. You shall retain in all copies of the Materials that You distribute the following attribution notices within a "Notice" text file distributed as a part of such copies: "Tongyi Qianwen is licensed under the Tongyi Qianwen LICENSE AGREEMENT, Copyright (c) Alibaba Cloud. All Rights Reserved."; and
    d. You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such derivative works as a whole, provided Your use, reproduction, and distribution of the work otherwise complies with the terms and conditions of this Agreement.

4. Restrictions
If you are commercially using the Materials, and your product or service has more than 100 million monthly active users, You shall request a license from Us. You cannot exercise your rights under this Agreement without our express authorization.

5. Rules of use
    a. The Materials may be subject to export controls or restrictions in China, the United States or other countries or regions. You shall comply with applicable laws and regulations in your use of the Materials.
    b. You can not use the Materials or any output therefrom to improve any other large language model (excluding Tongyi Qianwen or derivative works thereof).

6. Intellectual Property
    a. We retain ownership of all intellectual property rights in and to the Materials and derivatives made by or for Us. Conditioned upon compliance with the terms and conditions of this Agreement, with respect to any derivative works and modifications of the Materials that are made by you, you are and will be the owner of such derivative works and modifications.
    b. No trademark license is granted to use the trade names, trademarks, service marks, or product names of Us, except as required to fulfill notice requirements under this Agreement or as required for reasonable and customary use in describing and redistributing the Materials.
    c. If you commence a lawsuit or other proceedings (including a cross-claim or counterclaim in a lawsuit) against Us or any entity alleging that the Materials or any output therefrom, or any part of the foregoing, infringe any intellectual property or other right owned or licensable by you, then all licences granted to you under this Agreement shall terminate as of the date such lawsuit or other proceeding is commenced or brought.

7. Disclaimer of Warranty and Limitation of Liability

    a. We are not obligated to support, update, provide training for, or develop any further version of the Tongyi Qianwen Materials or to grant any license thereto.
    b. THE MATERIALS ARE PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY OF ANY KIND INCLUDING WARRANTIES OF MERCHANTABILITY, NONINFRINGEMENT, OR FITNESS FOR A PARTICULAR PURPOSE. WE MAKE NO WARRANTY AND ASSUME NO RESPONSIBILITY FOR THE SAFETY OR STABILITY OF THE MATERIALS AND ANY OUTPUT THEREFROM.
    c. IN NO EVENT SHALL WE BE LIABLE TO YOU FOR ANY DAMAGES, INCLUDING, BUT NOT LIMITED TO ANY DIRECT, OR INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING FROM YOUR USE OR INABILITY TO USE THE MATERIALS OR ANY OUTPUT OF IT, NO MATTER HOW IT’S CAUSED.
    d. You will defend, indemnify and hold harmless Us from and against any claim by any third party arising out of or related to your use or distribution of the Materials.

8. Survival and Termination.
    a. The term of this Agreement shall commence upon your acceptance of this Agreement or access to the Materials and will continue in full force and effect until terminated in accordance with the terms and conditions herein.
    b. We may terminate this Agreement if you breach any of the terms or conditions of this Agreement. Upon termination of this Agreement, you must delete and cease use of the Materials. Sections 7 and 9 shall survive the termination of this Agreement.

9. Governing Law and Jurisdiction.
    a. This Agreement and any dispute arising out of or relating to it will be governed by the laws of China, without regard to conflict of law principles, and the UN Convention on Contracts for the International Sale of Goods does not apply to this Agreement.
    b. The People's Courts in Hangzhou City shall have exclusive jurisdiction over any dispute arising out of this Agreement.
```

## File: `Tongyi Qianwen RESEARCH LICENSE AGREEMENT`
```
Tongyi Qianwen RESEARCH LICENSE AGREEMENT

Tongyi Qianwen Release Date: November 30, 2023

By clicking to agree or by using or distributing any portion or element of the Tongyi Qianwen Materials, you will be deemed to have recognized and accepted the content of this Agreement, which is effective immediately.

1. Definitions
    a. This Tongyi Qianwen RESEARCH LICENSE AGREEMENT (this "Agreement") shall mean the terms and conditions for use, reproduction, distribution and modification of the Materials as defined by this Agreement.
    b. "We"(or "Us") shall mean Alibaba Cloud.
    c. "You" (or "Your") shall mean a natural person or legal entity exercising the rights granted by this Agreement and/or using the Materials for any purpose and in any field of use.
    d. "Third Parties" shall mean individuals or legal entities that are not under common control with Us or You.
    e. "Tongyi Qianwen" shall mean the large language models, and software and algorithms, consisting of trained model weights, parameters (including optimizer states), machine-learning model code, inference-enabling code, training-enabling code, fine-tuning enabling code and other elements of the foregoing distributed by Us.
    f. "Materials" shall mean, collectively, Alibaba Cloud's proprietary Tongyi Qianwen and Documentation (and any portion thereof) made available under this Agreement.
    g. "Source" form shall mean the preferred form for making modifications, including but not limited to model source code, documentation source, and configuration files.
    h. "Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation,
 and conversions to other media types.
    i. "Non-Commercial" shall mean for research or evaluation purposes only.

2. Grant of Rights
    a. You are granted a non-exclusive, worldwide, non-transferable and royalty-free limited license under Alibaba Cloud's intellectual property or other rights owned by Us embodied in the Materials to use, reproduce, distribute, copy, create derivative works of, and make modifications to the Materials FOR NON-COMMERCIAL PURPOSES ONLY.
    b. If you are commercially using the Materials, You shall request a license from Us.

3. Redistribution
You may reproduce and distribute copies of the Materials or derivative works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:
    a. You shall give any other recipients of the Materials or derivative works a copy of this Agreement;
    b. You shall cause any modified files to carry prominent notices stating that You changed the files;
    c. You shall retain in all copies of the Materials that You distribute the following attribution notices within a "Notice" text file distributed as a part of such copies: "Tongyi Qianwen is licensed under the Tongyi Qianwen RESEARCH LICENSE AGREEMENT, Copyright (c) Alibaba Cloud. All Rights Reserved."; and
    d. You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such derivative works as a whole, provided Your use, reproduction, and distribution of the work otherwise complies with the terms and conditions of this Agreement.

4. Rules of use
    a. The Materials may be subject to export controls or restrictions in China, the United States or other countries or regions. You shall comply with applicable laws and regulations in your use of the Materials.
    b. You can not use the Materials or any output therefrom to improve any other large language model (excluding Tongyi Qianwen or derivative works thereof).

5. Intellectual Property
    a. We retain ownership of all intellectual property rights in and to the Materials and derivatives made by or for Us. Conditioned upon compliance with the terms and conditions of this Agreement, with respect to any derivative works and modifications of the Materials that are made by you, you are and will be the owner of such derivative works and modifications.
    b. No trademark license is granted to use the trade names, trademarks, service marks, or product names of Us, except as required to fulfill notice requirements under this Agreement or as required for reasonable and customary use in describing and redistributing the Materials.
    c. If you commence a lawsuit or other proceedings (including a cross-claim or counterclaim in a lawsuit) against Us or any entity alleging that the Materials or any output therefrom, or any part of the foregoing, infringe any intellectual property or other right owned or licensable by you, then all licences granted to you under this Agreement shall terminate as of the date such lawsuit or other proceeding is commenced or brought.

6. Disclaimer of Warranty and Limitation of Liability
    a. We are not obligated to support, update, provide training for, or develop any further version of the Tongyi Qianwen Materials or to grant any license thereto.
    b. THE MATERIALS ARE PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY OF ANY KIND INCLUDING WARRANTIES OF MERCHANTABILITY, NONINFRINGEMENT, OR FITNESS FOR A PARTICULAR PURPOSE. WE MAKE NO WARRANTY AND ASSUME NO RESPONSIBILITY FOR THE SAFETY OR STABILITY OF THE MATERIALS AND ANY OUTPUT THEREFROM.
    c. IN NO EVENT SHALL WE BE LIABLE TO YOU FOR ANY DAMAGES, INCLUDING, BUT NOT LIMITED TO ANY DIRECT, OR INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING FROM YOUR USE OR INABILITY TO USE THE MATERIALS OR ANY OUTPUT OF IT, NO MATTER HOW IT’S CAUSED.
    d. You will defend, indemnify and hold harmless Us from and against any claim by any third party arising out of or related to your use or distribution of the Materials.

7. Survival and Termination.
    a. The term of this Agreement shall commence upon your acceptance of this Agreement or access to the Materials and will continue in full force and effect until terminated in accordance with the terms and conditions herein.
    b. We may terminate this Agreement if you breach any of the terms or conditions of this Agreement. Upon termination of this Agreement, you must delete and cease use of the Materials. Sections 6 and 8 shall survive the termination of this Agreement.

8. Governing Law and Jurisdiction.
    a. This Agreement and any dispute arising out of or relating to it will be governed by the laws of China, without regard to conflict of law principles, and the UN Convention on Contracts for the International Sale of Goods does not apply to this Agreement.
    b. The People's Courts in Hangzhou City shall have exclusive jurisdiction over any dispute arising out of this Agreement.

9. Other Terms and Conditions.
    a. Any arrangements, understandings, or agreements regarding the Material not stated herein are separate from and independent of the terms and conditions of this Agreement. You shall request a seperate license from Us, if You use the Materials in ways not expressly agreed to in this Agreement.
    b. We shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.
```

## File: `utils.py`
```python
import torch
from transformers import AutoModelForCausalLM
from accelerate import dispatch_model


def _device_map(num_gpus, num_layers):
    per_gpu_layers = (num_layers + 2) / num_gpus

    device_map = {
        'transformer.wte': 0,
        'transformer.ln_f': 0,
        'lm_head': num_gpus-1
    }

    used = 1
    gpu_target = 0
    for i in range(num_layers):
        if used >= per_gpu_layers:
            gpu_target += 1
            used = 0 if gpu_target < num_gpus-1 else 1
        assert gpu_target < num_gpus
        device_map[f'transformer.h.{i}'] = gpu_target
        used += 1

    return device_map


def load_model_on_gpus(model_name_or_path, num_gpus: int = 2):
    num_devices = torch.cuda.device_count()

    if num_gpus == 1:
        model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map='auto',
                                                     trust_remote_code=True).eval()
    elif 1 < num_gpus <= num_devices:
        model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map='cpu',
                                                     trust_remote_code=True).eval()
        num_layers = model.config.num_hidden_layers
        device_map = _device_map(num_gpus, num_layers)
        print(device_map)
        model = dispatch_model(model, device_map=device_map)
    else:
        raise KeyError

    return model
```

## File: `web_demo.py`
```python
# Copyright (c) Alibaba Cloud.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

"""A simple web interactive chat demo based on gradio."""
import os
from argparse import ArgumentParser

import gradio as gr
import mdtex2html

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig


DEFAULT_CKPT_PATH = 'Qwen/Qwen-7B-Chat'


def _get_args():
    parser = ArgumentParser()
    parser.add_argument("-c", "--checkpoint-path", type=str, default=DEFAULT_CKPT_PATH,
                        help="Checkpoint name or path, default to %(default)r")
    parser.add_argument("--cpu-only", action="store_true", help="Run demo with CPU only")

    parser.add_argument("--share", action="store_true", default=False,
                        help="Create a publicly shareable link for the interface.")
    parser.add_argument("--inbrowser", action="store_true", default=False,
                        help="Automatically launch the interface in a new tab on the default browser.")
    parser.add_argument("--server-port", type=int, default=8000,
                        help="Demo server port.")
    parser.add_argument("--server-name", type=str, default="127.0.0.1",
                        help="Demo server name.")

    args = parser.parse_args()
    return args


def _load_model_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True, resume_download=True,
    )

    if args.cpu_only:
        device_map = "cpu"
    else:
        device_map = "auto"

    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        device_map=device_map,
        trust_remote_code=True,
        resume_download=True,
    ).eval()

    config = GenerationConfig.from_pretrained(
        args.checkpoint_path, trust_remote_code=True, resume_download=True,
    )

    return model, tokenizer, config


def postprocess(self, y):
    if y is None:
        return []
    for i, (message, response) in enumerate(y):
        y[i] = (
            None if message is None else mdtex2html.convert(message),
            None if response is None else mdtex2html.convert(response),
        )
    return y


gr.Chatbot.postprocess = postprocess


def _parse_text(text):
    lines = text.split("\n")
    lines = [line for line in lines if line != ""]
    count = 0
    for i, line in enumerate(lines):
        if "```" in line:
            count += 1
            items = line.split("`")
            if count % 2 == 1:
                lines[i] = f'<pre><code class="language-{items[-1]}">'
            else:
                lines[i] = f"<br></code></pre>"
        else:
            if i > 0:
                if count % 2 == 1:
                    line = line.replace("`", r"\`")
                    line = line.replace("<", "&lt;")
                    line = line.replace(">", "&gt;")
                    line = line.replace(" ", "&nbsp;")
                    line = line.replace("*", "&ast;")
                    line = line.replace("_", "&lowbar;")
                    line = line.replace("-", "&#45;")
                    line = line.replace(".", "&#46;")
                    line = line.replace("!", "&#33;")
                    line = line.replace("(", "&#40;")
                    line = line.replace(")", "&#41;")
                    line = line.replace("$", "&#36;")
                lines[i] = "<br>" + line
    text = "".join(lines)
    return text


def _gc():
    import gc
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def _launch_demo(args, model, tokenizer, config):

    def predict(_query, _chatbot, _task_history):
        print(f"User: {_parse_text(_query)}")
        _chatbot.append((_parse_text(_query), ""))
        full_response = ""

        for response in model.chat_stream(tokenizer, _query, history=_task_history, generation_config=config):
            _chatbot[-1] = (_parse_text(_query), _parse_text(response))

            yield _chatbot
            full_response = _parse_text(response)

        print(f"History: {_task_history}")
        _task_history.append((_query, full_response))
        print(f"Qwen-Chat: {_parse_text(full_response)}")

    def regenerate(_chatbot, _task_history):
        if not _task_history:
            yield _chatbot
            return
        item = _task_history.pop(-1)
        _chatbot.pop(-1)
        yield from predict(item[0], _chatbot, _task_history)

    def reset_user_input():
        return gr.update(value="")

    def reset_state(_chatbot, _task_history):
        _task_history.clear()
        _chatbot.clear()
        _gc()
        return _chatbot

    with gr.Blocks() as demo:
        gr.Markdown("""\
<p align="center"><img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/logo_qwen.jpg" style="height: 80px"/><p>""")
        gr.Markdown("""<center><font size=8>Qwen-Chat Bot</center>""")
        gr.Markdown(
            """\
<center><font size=3>This WebUI is based on Qwen-Chat, developed by Alibaba Cloud. \
(本WebUI基于Qwen-Chat打造，实现聊天机器人功能。)</center>""")
        gr.Markdown("""\
<center><font size=4>
Qwen-7B <a href="https://modelscope.cn/models/qwen/Qwen-7B/summary">🤖 </a> | 
<a href="https://huggingface.co/Qwen/Qwen-7B">🤗</a>&nbsp ｜ 
Qwen-7B-Chat <a href="https://modelscope.cn/models/qwen/Qwen-7B-Chat/summary">🤖 </a> | 
<a href="https://huggingface.co/Qwen/Qwen-7B-Chat">🤗</a>&nbsp ｜ 
Qwen-14B <a href="https://modelscope.cn/models/qwen/Qwen-14B/summary">🤖 </a> | 
<a href="https://huggingface.co/Qwen/Qwen-14B">🤗</a>&nbsp ｜ 
Qwen-14B-Chat <a href="https://modelscope.cn/models/qwen/Qwen-14B-Chat/summary">🤖 </a> | 
<a href="https://huggingface.co/Qwen/Qwen-14B-Chat">🤗</a>&nbsp ｜ 
&nbsp<a href="https://github.com/QwenLM/Qwen">Github</a></center>""")

        chatbot = gr.Chatbot(label='Qwen-Chat', elem_classes="control-height")
        query = gr.Textbox(lines=2, label='Input')
        task_history = gr.State([])

        with gr.Row():
            empty_btn = gr.Button("🧹 Clear History (清除历史)")
            submit_btn = gr.Button("🚀 Submit (发送)")
            regen_btn = gr.Button("🤔️ Regenerate (重试)")

        submit_btn.click(predict, [query, chatbot, task_history], [chatbot], show_progress=True)
        submit_btn.click(reset_user_input, [], [query])
        empty_btn.click(reset_state, [chatbot, task_history], outputs=[chatbot], show_progress=True)
        regen_btn.click(regenerate, [chatbot, task_history], [chatbot], show_progress=True)

        gr.Markdown("""\
<font size=2>Note: This demo is governed by the original license of Qwen. \
We strongly advise users not to knowingly generate or allow others to knowingly generate harmful content, \
including hate speech, violence, pornography, deception, etc. \
(注：本演示受Qwen的许可协议限制。我们强烈建议，用户不应传播及不应允许他人传播以下内容，\
包括但不限于仇恨言论、暴力、色情、欺诈相关的有害信息。)""")

    demo.queue().launch(
        share=args.share,
        inbrowser=args.inbrowser,
        server_port=args.server_port,
        server_name=args.server_name,
    )


def main():
    args = _get_args()

    model, tokenizer, config = _load_model_tokenizer(args)

    _launch_demo(args, model, tokenizer, config)


if __name__ == '__main__':
    main()
```

## File: `ascend-support/docker_qwen.sh`
```bash
#!/bin/bash

IMAGE_NAME=qwenllm/qwen-mindspore:v23.0.RC3
CONTAINER_NAME=qwen-mindspore
CHECKPOINT_PATH='NOT_SET'

DOCKER_CHECKPOINT_PATH=/data/qwen/models/Qwen-7B-Chat

function usage() {
    echo '
Usage: bash ascend-support/docker_qwen.sh [-i IMAGE_NAME] -c [/path/to/Qwen-7B-Chat] [-n CONTAINER_NAME]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -i | --image )
            shift
            IMAGE_NAME=$1
            ;;
        -c | --checkpoint )
            shift
            CHECKPOINT_PATH=$1
            ;;
        -n | --name )
            shift
            CONTAINER_NAME=$1
            ;;
        -h )
            usage
            exit
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

docker run -it --rm -u root --network=host --ipc=host \
    --device=/dev/davinci0 \
    --device=/dev/davinci1 \
    --device=/dev/davinci2 \
    --device=/dev/davinci3 \
    --device=/dev/davinci4 \
    --device=/dev/davinci5 \
    --device=/dev/davinci6 \
    --device=/dev/davinci7 \
    --name=${CONTAINER_NAME} \
    --device=/dev/davinci_manager \
    --device=/dev/devmm_svm \
    --device=/dev/hisi_hdc \
    -v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
    -v /usr/local/Ascend/add-ons/:/usr/local/Ascend/add-ons/ \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/sbin/npu-smi:/usr/local/sbin/npu-smi \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v ${CHECKPOINT_PATH}:${DOCKER_CHECKPOINT_PATH} \
    -v /var/log/npu/:/usr/slog \
    ${IMAGE_NAME} /bin/bash
```

## File: `ascend-support/README.md`
```markdown
# 昇腾910架构基于mindformers推理Qwen-7B-Chat模型

## 环境要求

- 硬件：Ascend 910A/B

## 运行步骤

首先参考Qwen README下载官方模型到`/path/to/Qwen-7B-Chat`。

### 下载并启动镜像

```bash
docker pull qwenllm/qwen-mindspore:latest

cd /path/to/Qwen/ascend-support

# 下载模型到此处
CHECKPOINT_PATH=/path/to/Qwen-7B-Chat

cd ascend-support

# 启动docker容器
bash docker_qwen.sh -c ${CHECKPOINT_PATH}
```

### 执行权重转换

在容器内执行下面的命令，将Qwen模型转换为适配`mindformers`的格式：

```bash
python3 /data/qwen/mindformers/research/qwen/convert_weight.py
```

转换后模型的输出位置为`${CHECKPOINT_PATH}/qwen-7b-chat.ckpt`。

### 执行推理

在容器内执行下面的命令，进行推理：

```bash
cd /data/qwen/mindformers/research/qwen
export PYTHONPATH=/data/qwen/mindformers:$PYTHONPATH
python3 infer_qwen.py
```
```

## File: `dcu-support/cli_demo.py`
```python
# coding=utf-8
import argparse
from fastllm_pytools import llm

def args_parser():
    parser = argparse.ArgumentParser(description = 'qwen_chat_demo')
    parser.add_argument('-p', '--path', type = str, required = True, default = '', help = '模型文件的路径')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = args_parser()
    model = llm.model(args.path)

    history = []
    print("输入内容即可进行对话，clear 清空对话历史，stop 终止程序")
    while True:
        query = input("\n用户：")
        if query.strip() == "stop":
            break
        if query.strip() == "clear":
            history = []
            print("输入内容即可进行对话，clear 清空对话历史，stop 终止程序")
            continue
        print("AI:", end = "")
        curResponse = ""
        for response in model.stream_response(query, history = history, do_sample = True, top_p = 0.8, top_k = 1, temperature = 1.0, repeat_penalty = 1.0):
            curResponse += response
            print(response, flush = True, end = "")
        history.append((query, curResponse))
```

## File: `dcu-support/cli_demo_batch.py`
```python
import argparse
from fastllm_pytools import llm
import time

def args_parser():
    parser = argparse.ArgumentParser(description = 'fastllm_chat_demo')
    parser.add_argument('-p', '--path', type = str, required = True, default = '', help = '模型文件的路径')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = args_parser()

    model_path = args.path

    prompts = ["深圳有什么好玩的", "上海有什么好玩的", "晚上睡不着怎么办", "南京有什么好吃的"] * 2
    print(prompts)

    responses, historys = [], []
    
    model = llm.model(model_path)
    
    t0 = time.time()
    responses, historys = model.response_batch(prompts)        
    t1 = time.time()

    token_output_count = 0
    word_len = 0
    for i, res in enumerate(responses):
        tokens = model.tokenizer_encode_string(res)
        token_output_count += len(tokens)
        word_len += len(res)

        print("batch index: ", i)
        print(res)
        print("")

    print("\ntoken/s: {:.2f}, character/s: {:.2f}".format(token_output_count/(t1-t0), word_len/(t1-t0)))

```

## File: `dcu-support/model.properties`
```
# 模型唯一标识
modelCode = 411
# 模型名称
modelName=qwen-7b_fastllm
# 模型描述
modelDescription=qwen-7b是阿里云研发的通义千问大模型系列的70亿参数规模的模型
# 应用场景
appScenario=推理,对话问答,医疗,科研,金融,教育
# 框架类型
frameType=fastllm
```

## File: `dcu-support/qwen2flm.py`
```python
import sys
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
from fastllm_pytools import torch2flm

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True, fp32=True).eval()
    model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

    dtype = sys.argv[2] if len(sys.argv) >= 3 else "float16"
    exportPath = sys.argv[1] if len(sys.argv) >= 2 else "qwen-7b-" + dtype + ".flm"
    torch2flm.tofile(exportPath, model, tokenizer, dtype = dtype)
```

## File: `dcu-support/README.md`
```markdown
# DCU 架构基于 fastllm 推理 Qwen 模型


## 环境配置

### 环境准备

```
docker pull image.sourcefind.cn:5000/dcu/admin/base/pytorch:1.13.1-centos7.6-dtk-23.04-py38-latest
```

### 容器启动

根据如下命令启动推理容器，其中需自定义一个容器名<container_name>，<project_path>即为本目录的路径：
```
# <container_name> 自定义容器名
# <project_path> 当前工程所在路径
docker run -it --name=<container_name> -v <project_path>:/work --device=/dev/kfd --device=/dev/dri --security-opt seccomp=unconfined --cap-add=SYS_PTRACE --shm-size=16G --group-add 39 image.sourcefind.cn:5000/dcu/admin/base/pytorch:1.13.1-centos7.6-dtk-23.04-py38-latest /bin/bash
```

### 加载环境

进入容器后执行如下命令，加载运行环境变量

```
source /opt/dtk-23.04/cuda/env.sh
```

### 安装方法

```
#进入本工程目录
cd package
python setup.py install
```

## 推理

### 模型转换

首先参考Qwen README下载官方模型，并通过如下方式将模型转换为 fastllm 用于推理的形式：

- 通过`pip install -r requirements.txt`安装模型转换所需依赖

- 如果使用已经下载完成的模型或者自己finetune的模型需要修改qwen2flm.py文件中创建tokenizer, model时的模型存放路径

```
# 在本工程目录下执行：
python3 qwen2flm.py qwen-7b-fp16.bin float16 # 导出fp16模型，参数为导出的模型路径
```


### 模型推理

```
# 命令行聊天程序，使用了模型创建以及流式对话效果
python cli_demo.py -p qwen-7b-fp16.bin

# batch推理程序
python cli_demo_batch.py -p qwen-7b-fp16.bin

# 简易webui，需要先安装streamlit-chat
streamlit run web_demo.py qwen-7b-fp16.bin 
```
```

## File: `dcu-support/requirements.txt`
```
transformers==4.32.0
tiktoken
streamlit>=1.24.0
sentencepiece
urllib3==1.26.16
transformers_stream_generator==0.0.4
accelerate
einops
#scipy
```

## File: `dcu-support/web_demo.py`
```python
import streamlit as st
from streamlit_chat import message
from fastllm_pytools import llm
import sys

st.set_page_config(
    page_title="fastllm web demo",
    page_icon=":robot:"
)

@st.cache_resource
def get_model():
    model = llm.model(sys.argv[1])
    return model

if "messages" not in st.session_state:
    st.session_state.messages = []

for i, (prompt, response) in enumerate(st.session_state.messages):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)

if prompt := st.chat_input("请开始对话"):
    model = get_model()
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in model.stream_response(prompt, st.session_state.messages, one_by_one = True):
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append((prompt, full_response))
```

## File: `dcu-support/package/setup.py`
```python
from setuptools import setup, find_packages

setup (
    name = "fastllm_pytools",
    version = "0.0.1",
    description = "Fastllm pytools",
    packages = ['fastllm_pytools'],
    url = "https://developer.hpccube.com/codes/aicomponent/fastllm",
    package_data = {
        '': ['*.dll', '*.so']
    }
)
```

## File: `dcu-support/package/fastllm_pytools/hf_model.py`
```python
from fastllm_pytools import llm;
import torch;
import ctypes;
import numpy as np;

fastllm_data_type_dict = {
    "int4": 8,
    "int8": 3,
    "float16": 7
}
fastllm_weight_type_dict = {
    "linear": 1,
    "embedding": 2,
    "QuantizedLinear": 111
}

def create(model,
           tokenizer = None,
           pre_prompt = None,
           user_role = None,
           bot_role = None,
           history_sep = None,
           dtype = "float16"):
    if (dtype not in fastllm_data_type_dict):
        print("dtype should in ", list(fastllm_data_type_dict.keys()));
        exit(0);

    # 0.1 model info
    if model.config.model_type == "chatglm" and model.config.transformers_version == "4.30.2":
        model.config.model_type = "chatglm3"
    modelInfo = model.config.__dict__
    if model.generation_config is not None:
        modelInfo.update(model.generation_config.__dict__)
    if (pre_prompt):
        modelInfo["pre_prompt"] = pre_prompt;
    if (user_role):
        modelInfo["user_role"] = user_role;
    if (bot_role):
        modelInfo["bot_role"] = bot_role;
    if (history_sep):
        modelInfo["history_sep"] = history_sep;
    if (modelInfo["model_type"] == "baichuan" and hasattr(model, "model") and hasattr(model.model, "get_alibi_mask")):
        # Baichuan 2代
        modelInfo["use_alibi"] = "1";
        modelInfo["pre_prompt"] = "";
        modelInfo["user_role"] = ("<FLM_FIX_TOKEN_" + str(model.generation_config.user_token_id) + "> ") if hasattr(model.generation_config, "user_token_id") else "";
        modelInfo["bot_role"] = ("<FLM_FIX_TOKEN_" + str(model.generation_config.assistant_token_id) + ">") if hasattr(model.generation_config, "assistant_token_id") else "";
        modelInfo["history_sep"] = "";
    if (modelInfo["model_type"] == "qwen"):
        if modelInfo["chat_format"] == "chatml":
            modelInfo["im_end_id"] = tokenizer.im_end_id
            modelInfo["im_start_id"] = tokenizer.im_start_id


    weight_type_dict = {};
    module_dict = {};
    weight_bits = {};
    for key, m in model.named_modules():
        if (str(type(m)).find("QuantizedLinear") != -1):
            weight_type_dict[key + ".weight"] = "QuantizedLinear";
            weight_bits[key + ".weight"] = m.weight_bit_width;
        if (isinstance(m, torch.nn.Linear)):
            weight_type_dict[key + ".weight"] = "linear";
            module_dict[key + ".weight"] = m;
        if (isinstance(m, torch.nn.Embedding)):
            weight_type_dict[key] = "embedding";

    peft_config = {}
    active_adapter = ""
    if hasattr(model, "peft_config"):
        peft_config = model.peft_config
    if hasattr(model, "active_adapter") and isinstance(model.active_adapter, str):
        # in transformers >= 4.33.0, active_adapter is a funtion in model, ignore it now
        active_adapter = model.active_adapter

    model = model.cpu();
    dict = model.state_dict();
    model_type = model.config.__dict__["model_type"];
    model = llm.fastllm_lib.create_empty_llm_model(model_type.encode());
    for it in modelInfo.keys():
        llm.fastllm_lib.add_dict_llm_model(model, str(it).encode(), str(modelInfo[it]).encode());

    for adapter_name in peft_config.keys():
        adapter_dict = peft_config[adapter_name].__dict__
        for it in adapter_dict.keys():
            llm.fastllm_lib.add_adapter_dict_llm_model(model, str(adapter_name).encode(), str(it).encode(), str(adapter_dict[it]).encode())
    if len(active_adapter) != 0:
        llm.fastllm_lib.set_adapter(model, str(active_adapter).encode())

    # 1. vocab
    if (tokenizer):
        if (hasattr(tokenizer, "tokenizer")):
            if modelInfo["model_type"] == "qwen":
                pass
            else:
                tokenizer = tokenizer.tokenizer;
        if (hasattr(tokenizer, "sp_model")):
            piece_size = tokenizer.sp_model.piece_size();
            for i in range(piece_size):
                llm.fastllm_lib.add_tokenizer_word_llm_model(model, tokenizer.sp_model.id_to_piece(i).encode(),
                                                             i, ctypes.c_float(tokenizer.sp_model.get_score(i)));
        else:
            vocab = tokenizer.get_vocab();
            for v in vocab.keys():
                if (modelInfo["model_type"] == "moss"):
                    vv = [(ord(c) if c not in tokenizer.byte_decoder else tokenizer.byte_decoder[c]) for c in v];
                    llm.fastllm_lib.add_tokenizer_word_llm_model(model, vv, vocab[v], ctypes.c_float(1.0));
                elif (modelInfo["model_type"] == "qwen"):
                    llm.fastllm_lib.add_tokenizer_word_llm_model(model, v, vocab[v], ctypes.c_float(1.0));
                else:
                    llm.fastllm_lib.add_tokenizer_word_llm_model(model, v.encode(), vocab[v], ctypes.c_float(1.0));
    tot = 0;
    for key in dict:
        ori_data_type = 0;
        ori_np_data_type = np.float32;
        cur_weight_type = 0;
        if (key in weight_type_dict and weight_type_dict[key] in fastllm_weight_type_dict):
            cur_weight_type = fastllm_weight_type_dict[weight_type_dict[key]];
        to_data_type = 0;

        if (cur_weight_type == 1):
            to_data_type = fastllm_data_type_dict[dtype];
            if (to_data_type == 7):
                ori_data_type = 7;
                ori_np_data_type = np.float16;
        elif (cur_weight_type == 2):
            # TODO bfloat
            to_data_type = 0;

        weight_name = key
        if peft_config is not None:
            weight_name = weight_name.replace('base_model.model.', '')
        if (cur_weight_type == 111):
            llm.fastllm_lib.add_qlinear_weight_llm_model(model, weight_name.encode(),
                                                 len(dict[key].shape),
                                                 (ctypes.c_int * len(dict[key].shape))(*list(dict[key].shape)),
                                                 weight_bits[key],
                                                 dict[key + "_scale"].numpy().astype(np.float32).ctypes.data_as(ctypes.c_void_p),
                                                 dict[key].numpy().ctypes.data_as(ctypes.c_void_p));
        else:
            llm.fastllm_lib.add_weight_llm_model(model, weight_name.encode(),
                                             len(dict[key].shape),
                                             (ctypes.c_int * len(dict[key].shape))(*list(dict[key].shape)),
                                             to_data_type, cur_weight_type, ori_data_type,
                                             dict[key].numpy().astype(ori_np_data_type).ctypes.data_as(ctypes.c_void_p));
        tot += 1;
        print("convert (", tot, "/", len(dict), end = " )\r");

    print("");
    llm.fastllm_lib.init_params_llm_model(model);
    llm.fastllm_lib.warmup_llm_model(model);
    ret = llm.model("", id = model);
    return ret;

```

## File: `dcu-support/package/fastllm_pytools/llm.py`
```python
import ctypes;
import math
import os;
import threading
from typing import Optional, Tuple, Union, List, Callable, Dict, Any;
from copy import deepcopy

import platform
if platform.system() == 'Windows':
    fastllm_lib = ctypes.cdll.LoadLibrary(os.path.join(os.path.split(os.path.realpath(__file__))[0], "fastllm_tools.dll"))
else:
    fastllm_lib = ctypes.cdll.LoadLibrary(os.path.join(os.path.split(os.path.realpath(__file__))[0], "libfastllm_tools.so"))

fastllm_lib.create_llm_model.argtypes = [ctypes.c_char_p]
fastllm_lib.create_llm_model.restype = ctypes.c_int

fastllm_lib.token_decode.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
fastllm_lib.token_decode.restype = ctypes.c_int

fastllm_lib.token_encode_string.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
fastllm_lib.token_encode_string.restype = ctypes.c_int

fastllm_lib.launch_response_llm_model.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_void_p,
                                                  ctypes.c_int, ctypes.c_bool, ctypes.c_float, ctypes.c_int,
                                                  ctypes.c_float, ctypes.c_float, ctypes.c_bool]
fastllm_lib.launch_response_llm_model.restype = ctypes.c_int

fastllm_lib.fetch_response_llm_model.argtypes = [ctypes.c_int, ctypes.c_int]
fastllm_lib.fetch_response_llm_model.restype = ctypes.c_int

fastllm_lib.fetch_response_logits_llm_model.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
fastllm_lib.fetch_response_logits_llm_model.restype = ctypes.c_int

fastllm_lib.response_str_llm_model.argtypes = [ctypes.c_int, ctypes.c_char_p,
                                               ctypes.c_int, ctypes.c_bool, ctypes.c_float, ctypes.c_int,
                                               ctypes.c_float, ctypes.c_float, ctypes.c_bool]
fastllm_lib.response_str_llm_model.restype = ctypes.c_char_p

fastllm_lib.launch_response_str_llm_model.argtype = [ctypes.c_int, ctypes.c_char_p,
                                                     ctypes.c_int, ctypes.c_bool, ctypes.c_float, ctypes.c_int,
                                                     ctypes.c_float, ctypes.c_float, ctypes.c_bool]
fastllm_lib.launch_response_str_llm_model.restype = ctypes.c_int

fastllm_lib.fetch_response_str_llm_model.argtypes = [ctypes.c_int, ctypes.c_int]
fastllm_lib.fetch_response_str_llm_model.restype = ctypes.c_char_p

fastllm_lib.make_history_llm_model.argtype = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
fastllm_lib.make_history_llm_model.restype = ctypes.c_char_p

fastllm_lib.make_input_llm_model.argtype = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
fastllm_lib.make_input_llm_model.restype = ctypes.c_char_p

fastllm_lib.add_tokenizer_word_llm_model.argtype = [ctypes.c_int, ctypes.c_char_p, ctypes.c_float, ctypes.c_int]

fastllm_lib.set_device_map.argtype = [ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]

fastllm_lib.get_llm_model_type.argtype = [ctypes.c_int]
fastllm_lib.get_llm_model_type.restype = ctypes.c_char_p

fastllm_lib.response_batch_str_llm_model.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int,
                                                     ctypes.c_int, ctypes.c_bool, ctypes.c_float, ctypes.c_int,
                                                     ctypes.c_float, ctypes.c_float, ctypes.c_bool]
fastllm_lib.response_batch_str_llm_model.restype = ctypes.POINTER(ctypes.c_char_p)

fastllm_lib.response_batch_tokens_llm_model.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
                                                        ctypes.c_int, ctypes.c_bool, ctypes.c_float, ctypes.c_int,
                                                        ctypes.c_float, ctypes.c_float, ctypes.c_bool]
fastllm_lib.response_batch_tokens_llm_model.restype = ctypes.POINTER(ctypes.c_char_p)

def set_cpu_threads(threads: int):
    fastllm_lib.set_cpu_threads(threads);

def get_cpu_threads() -> int:
    return fastllm_lib.get_cpu_threads();

def print_ins_info():
    fastllm_lib.print_cpu_ins();

def set_cpu_kvcache(cpu_kvcache):
    fastllm_lib.set_kvcache_in_cpu(ctypes.c_bool(cpu_kvcache));

def get_cpu_kvcache():
    return fastllm_lib.get_kvcache_in_cpu();

def set_cpu_low_mem(low_mem):
    fastllm_lib.set_cpu_low_mem(ctypes.c_bool(low_mem));

def get_cpu_low_mem():
    return fastllm_lib.get_cpu_low_mem();

def set_device_map(device_map):
    devices = [];
    values = [];
    if (isinstance(device_map, str)):
        devices.append(device_map);
        values.append(1);
    elif (isinstance(device_map, list)):
        devices = [str(x) for x in device_map];
        values = [1 for x in device_map];
    elif (isinstance(device_map, dict)):
        devices = [str(x) for x in device_map.keys()];
        values = [int(device_map[x]) for x in device_map.keys()];
    else:
        print("set_device_map error.");
        return;
    device_str = ''.join(devices);
    device_len = [len(x) for x in devices];
    fastllm_lib.set_device_map(len(device_len),
                               (ctypes.c_int * len(device_len))(*device_len),
                               device_str.encode(),
                               (ctypes.c_int * len(values))(*values));
def from_hf(model,
            tokenizer = None,
            dtype = "float16"):
    from fastllm_pytools import hf_model;
    return hf_model.create(model, tokenizer, dtype = dtype);

class model:
    def __init__ (self, path : str,
                  id : int = -99999):
        if (id != -99999):
            self.model = id;
        else:
            self.model = fastllm_lib.create_llm_model(path.encode());
        self.direct_query = False;

        # 为了减少重复申请释放buffer对象而使用的线程局部存储区对象池
        self.thread_local_obj = threading.local()
        self.thread_local_obj.tokenizer_encode_string__output_buffer = None
        self.thread_local_obj.tokenizer_decode_token__output_buffer = None

        # tokenizer_decode_token 输出结果的静态缓存，手工触发构建
        # 由于token数量有限且不太多，所以缓存该结果来减少调用较为适合。
        # 不做成自动缓存是为了避免在多线程调用的时候对缓存dict加锁，同时也为不同场景提供选择空间
        self.tokenizer_decode_token_cache = None

        self.model_type = fastllm_lib.get_llm_model_type(self.model).decode()
        # print("model_type:", self.model_type)

    def get_prompt(self,
                   query: str,
                   history: List[Tuple[str, str]] = None) -> str:
        if (not(history)):
            history = [];
        prompt = "";
        for i, (old_query, response) in enumerate(history):
            prompt = fastllm_lib.make_history_llm_model(self.model, prompt.encode(), i, old_query.encode(), response.encode()).decode();
        prompt = fastllm_lib.make_input_llm_model(self.model, prompt.encode(), len(history), query.encode()).decode();
        return prompt;

    def save(self, path : str):
        fastllm_lib.save_llm_model(self.model, path.encode());

    def eval(self):
        pass;

    def build_tokenizer_decode_token_cache(self):
        if self.tokenizer_decode_token_cache is not None:
            return

        cache_dict = dict()
        vocab_size = fastllm_lib.get_tokenizer_vocab_size(self.model)
        for token_id in range(vocab_size):
            cache_dict[token_id] = self.tokenizer_decode_token(token_id)

        self.tokenizer_decode_token_cache = cache_dict

    def tokenizer_encode_string(self, content: str) -> List[int]:
        output_buffer_init_len = 1024
        if self.thread_local_obj.tokenizer_encode_string__output_buffer is None:
            self.thread_local_obj.tokenizer_encode_string__output_buffer = (ctypes.c_int * output_buffer_init_len)()

        buffer = self.thread_local_obj.tokenizer_encode_string__output_buffer
        buffer_len = len(buffer)
        result_len = fastllm_lib.token_encode_string(self.model, content.encode(), buffer_len, buffer)
        if result_len > buffer_len:
            if result_len > 10240:
                # 要处理的数据过长，使用一次性的buffer
                temp_buffer = (ctypes.c_int * result_len)()
                ret = fastllm_lib.token_encode_string(self.model, content.encode(), result_len, temp_buffer)
                return [i for i in temp_buffer]
            else:
                # 扩展buffer大小
                new_buffer_len = round(math.ceil(result_len / 1024.0)) * 1024
                buffer = (ctypes.c_int * new_buffer_len)()
                self.thread_local_obj.tokenizer_encode_string__output_buffer = buffer
                result_len = fastllm_lib.token_encode_string(self.model, content.encode(), new_buffer_len, buffer)

        return [buffer[i] for i in range(result_len)]

    def tokenizer_decode_token(self, token_id: int) -> bytes:
        if self.tokenizer_decode_token_cache is not None:
            cache_result = self.tokenizer_decode_token_cache.get(token_id)
            if cache_result is not None:
                return cache_result

        output_buffer_init_len = 256
        if self.thread_local_obj.tokenizer_decode_token__output_buffer is None:
            self.thread_local_obj.tokenizer_decode_token__output_buffer = ctypes.create_string_buffer(output_buffer_init_len)

        buffer = self.thread_local_obj.tokenizer_decode_token__output_buffer
        ret = fastllm_lib.token_decode(self.model, token_id, len(buffer), buffer)
        if ret > 0:
            # buffer长度不够，扩展buffer大小
            new_buffer_len = round(math.ceil(ret / 16.0)) * 16
            buffer = ctypes.create_string_buffer(new_buffer_len)
            self.thread_local_obj.tokenizer_decode_token__output_buffer = buffer
            ret = fastllm_lib.token_decode(self.model, token_id, len(buffer), buffer)
            assert ret == 0

        buffer_bytes = buffer.raw
        result_len = len(buffer_bytes)
        for i in range(len(buffer_bytes)):
            if buffer_bytes[i] == 0:
                result_len = i
                break
        return buffer_bytes[:result_len]

    def response_logits(self,
                        query: str,
                        history: List[Tuple[str, str]] = None,
                        tokenizer = None) -> str:
        prompt = query if self.direct_query else self.get_prompt(query, history);
        if (tokenizer == None):
            handle = fastllm_lib.launch_response_str_llm_model(self.model, prompt.encode(),
                                                               ctypes.c_int(1), ctypes.c_bool(False), ctypes.c_float(1), ctypes.c_int(1),
                                                               ctypes.c_float(1), ctypes.c_float(1), ctypes.c_bool(True));
        else:
            input = tokenizer.encode(prompt);
            handle = fastllm_lib.launch_response_llm_model(self.model, len(input), (ctypes.c_int * len(input))(*input),
                                                           1, False, 1, 1, 1, 1, True);
        vocab_size = fastllm_lib.get_tokenizer_vocab_size(self.model);
        logits = list(range(vocab_size))
        array = (ctypes.c_float * (vocab_size * 4))(*logits);
        ret = fastllm_lib.fetch_response_logits_llm_model(self.model, handle, array);
        out = list(array)[:vocab_size];
        while (ret != -1):
            ret = fastllm_lib.fetch_response_logits_llm_model(self.model, handle, array);
        return out;

    def response(self,
                 query: str,
                 history: List[Tuple[str, str]] = None,
                 max_length: int = 8192, do_sample = True, top_p = 0.8, top_k = 1, temperature = 1.0, repeat_penalty = 1.0) -> str:
        ret = "";
        for i in self.stream_response(query = query,
                                      history = history,
                                      max_length = max_length,
                                      do_sample = do_sample,
                                      top_p = top_p, top_k = top_k,
                                      temperature = temperature,
                                      repeat_penalty = repeat_penalty,
                                      one_by_one = True):
            ret += i;
        return ret;

    def stream_response(self,
                        query: str,
                        history: List[Tuple[str, str]] = None,
                        max_length: int = 8192, do_sample = True, top_p = 0.8, top_k = 1, temperature = 1.0, repeat_penalty = 1.0,
                        one_by_one = True):
        prompt = query if self.direct_query else self.get_prompt(query, history);
        handle = fastllm_lib.launch_response_str_llm_model(self.model, prompt.encode(),
                                                           ctypes.c_int(max_length), ctypes.c_bool(do_sample), ctypes.c_float(top_p), ctypes.c_int(top_k),
                                                           ctypes.c_float(temperature), ctypes.c_float(repeat_penalty), ctypes.c_bool(False));
        res = "";
        ret = b'';
        fail_cnt = 0;
        while True:
            ret += fastllm_lib.fetch_response_str_llm_model(self.model, handle);
            cur = "";
            try:
                cur = ret.decode();
                ret = b'';
            except:
                fail_cnt += 1;
                if (fail_cnt == 20):
                    break;
                else:
                    continue;
            fail_cnt = 0;
            if (cur == "<flmeos>"):
                break;
            if one_by_one:
                yield cur;
            else:
                res += cur;
                yield res;

    def stream_response_raw(self,
                            input_tokens: List[int],
                            max_length: int = 8192, do_sample = True, top_p = 0.8, top_k = 1, temperature = 1.0, repeat_penalty = 1.0,
                            one_by_one = True
                            ):
        handle = fastllm_lib.launch_response_llm_model(self.model, len(input_tokens),
                                                       (ctypes.c_int * len(input_tokens))(*input_tokens),
                                                       ctypes.c_int(max_length), ctypes.c_bool(do_sample), ctypes.c_float(top_p), ctypes.c_int(top_k),
                                                       ctypes.c_float(temperature), ctypes.c_float(repeat_penalty), ctypes.c_bool(False))

        # 可能遇到长尾char需要多个token才能够生成，所以只返回bytes，string.decode策略交给外部
        # 方便统计输出token数量，和控制不完整utf8时候解码的逻辑

        total_bytes = b''
        while True:
            cur_token = fastllm_lib.fetch_response_llm_model(self.model, handle)
            if cur_token == -1:
                break

            cur_bytes = self.tokenizer_decode_token(cur_token)

            if one_by_one:
                yield cur_bytes
            else:
                total_bytes += cur_bytes
                yield total_bytes

    def chat(self, tokenizer, query: str, history: List[Tuple[str, str]] = None, max_length: int = 8192,
             do_sample = True, top_p = 0.8, top_k = 1, temperature = 1.0, repeat_penalty = 1.0, **kwargs):
        if self.model_type  != "chatglm3":
            if (not(history)):
                history = [];
            prompt = query if self.direct_query else self.get_prompt(query, history);
            input = tokenizer.encode(prompt);
            handle = fastllm_lib.launch_response_llm_model(self.model, len(input), (ctypes.c_int * len(input))(*input),
                                                           max_length, do_sample, top_p, top_k, temperature, repeat_penalty,
                                                           False);

            result = [];
            while True:
                cur = fastllm_lib.fetch_response_llm_model(self.model, handle);
                if (cur == -1):
                    break;
                result.append(cur);
            response = tokenizer.decode(result);
            history = history + [(query, response)];
            return response, history;
        else:
            if history is None:
                history = []
            role = "user"
            input = self.build_chatglm3_input(tokenizer, query, history=history, role=role)
            history.append({"role": role, "content": query})

            handle = fastllm_lib.launch_response_llm_model(self.model, len(input), (ctypes.c_int * len(input))(*input),
                                                           max_length, do_sample, top_p, top_k, temperature, repeat_penalty,
                                                           False);
            tokens = [];
            while True:
                cur = fastllm_lib.fetch_response_llm_model(self.model, handle);
                if (cur == -1):
                    break;
                tokens.append(cur);
            response = tokenizer.decode(tokens);
            if response and response[-1] != "�":
                response, new_history = self.process_chatglm3_response(response, history)
                return response, new_history

    def stream_chat(self, tokenizer, query: str, history: List[Tuple[str, str]] = None, past_key_values = None,
                    max_length: int = 8192, do_sample = True, top_p = 0.8, top_k = 1, temperature = 1.0, repeat_penalty = 1.0,
                    return_past_key_values = False, **kwargs) -> str:
        if self.model_type  != "chatglm3":
            if (not(history)):
                history = [];
            prompt = query if self.direct_query else self.get_prompt(query, history);
            input = tokenizer.encode(prompt);
            handle = fastllm_lib.launch_response_llm_model(self.model, len(input), (ctypes.c_int * len(input))(*input),
                                                           max_length, do_sample, top_p, top_k, temperature, repeat_penalty,
                                                           False);
            tokens = [];
            while True:
                cur = fastllm_lib.fetch_response_llm_model(self.model, handle);
                if (cur == -1):
                    break;
                tokens.append(cur);
                response = tokenizer.decode(tokens);
                new_history = history + [(query, response)];
                if return_past_key_values:
                    yield response, new_history, None;
                else:
                    yield response, new_history;
        else:
            if history is None:
                history = []
            role = "user"
            input = self.build_chatglm3_input(tokenizer, query, history=history, role=role)
            history.append({"role": role, "content": query})

            handle = fastllm_lib.launch_response_llm_model(self.model, len(input), (ctypes.c_int * len(input))(*input),
                                                           max_length, do_sample, top_p, top_k, temperature, repeat_penalty,
                                                           False);
            tokens = [];
            while True:
                cur = fastllm_lib.fetch_response_llm_model(self.model, handle);
                if (cur == -1):
                    break;
                tokens.append(cur);
                response = tokenizer.decode(tokens);
                if response and response[-1] != "�":
                    response, new_history = self.process_chatglm3_response(response, history)
                    if return_past_key_values:
                        yield response, new_history, past_key_values
                    else:
                        yield response, new_history


    def set_adapter(self, name: str):
        fastllm_lib.set_adapter(self.model, str(name).encode())

    def disable_adapter(self):
        fastllm_lib.disable_adapter(self.model)

    def process_chatglm3_response(self, output, history):
        content = ""
        history = deepcopy(history)
        for response in output.split("<|assistant|>"):
            metadata, content = response.split("\n", maxsplit=1)
            if not metadata.strip():
                content = content.strip()
                history.append({"role": "assistant", "metadata": metadata, "content": content})
                content = content.replace("[[训练时间]]", "2023年")
            else:
                history.append({"role": "assistant", "metadata": metadata, "content": content})
                if history[0]["role"] == "system" and "tools" in history[0]:
                    content = "\n".join(content.split("\n")[1:-1])
                    def tool_call(**kwargs):
                        return kwargs
                    parameters = eval(content)
                    content = {"name": metadata.strip(), "parameters": parameters}
                else:
                    content = {"name": metadata.strip(), "content": content}
        return content, history

    def build_chatglm3_input(self, tokenizer, query, history=None, role="user"):
        if history is None:
            history = []
        input_ids = []
        for item in history:
            content = item["content"]
            if item["role"] == "system" and "tools" in item:
                content = content + "\n" + json.dumps(item["tools"], indent=4, ensure_ascii=False)
            input_ids.extend(tokenizer.build_single_message(item["role"], item.get("metadata", ""), content))
        input_ids.extend(tokenizer.build_single_message(role, "", query))
        input_ids.extend([tokenizer.get_command("<|assistant|>")])
        return input_ids

    def response_batch(self, querys: List[str],
                       historys: List[List[Tuple[str, str]]] = None,
                       max_length: int = 1024, do_sample = True, top_p = 0.8, top_k = 1, temperature = 1.0, repeat_penalty = 1.0,
                       **kwargs) -> List[str]:
        query_size = len(querys)
        if (not(historys)):
            historys = [[] for _ in range(query_size)]
        inputs = (ctypes.c_char_p * query_size)()
        for i, query in enumerate(querys):
            prompt = query if self.direct_query else self.get_prompt(query, historys[i])
            inputs[i] = ctypes.c_char_p(prompt.encode())

        outputs = fastllm_lib.response_batch_str_llm_model(self.model, inputs, query_size,
                                                           max_length, do_sample, top_p, top_k, temperature, repeat_penalty, False)

        responses = []
        for i in range(query_size):
            response = ctypes.string_at(outputs[i]).decode()
            responses.append(response)
            historys[i] = historys[i] + [(querys[i], response)]
        return responses, historys

    def chat_batch(self, tokenizer, querys: List[str], historys: List[List[Tuple[str, str]]] = None, max_length: int = 1024,
                   do_sample = True, top_p = 0.8, top_k = 1, temperature = 1.0, repeat_penalty = 1.0, **kwargs):
        query_size = len(querys)
        if (not(historys)):
            historys = [[] for _ in range(query_size)]

            inputs = []
            inputs_len = []
            for i, query in enumerate(querys):
                prompt = query if self.direct_query else self.get_prompt(query, historys[i])
                input = tokenizer.encode(prompt);
                inputs.extend(input)
                inputs_len.append(len(input))

            outputs = fastllm_lib.response_batch_tokens_llm_model(self.model, query_size,
                                                                  (ctypes.c_int * len(inputs_len))(*inputs_len),
                                                                  (ctypes.c_int * len(inputs))(*inputs),
                                                                  max_length, do_sample, top_p, top_k, temperature, repeat_penalty,
                                                                  False)

            responses = []
            for i in range(query_size):
                response = ctypes.string_at(outputs[i]).decode()
                responses.append(response)
                historys[i] = historys[i] + [(querys[i], response)]
            return responses, historys


```

## File: `dcu-support/package/fastllm_pytools/torch2flm.py`
```python
import struct
import numpy as np
import torch

def writeString(fo, s):
    fo.write(struct.pack('i', len(s)))
    fo.write(s.encode())

def writeKeyValue(fo, key, value):
    writeString(fo, key)
    writeString(fo, value)

fastllm_data_type_dict = {
    "int4": 8,
    "int8": 3,
    "float16": 7,
    "float32": 0,
}
fastllm_weight_type_dict = {
    "linear": 1,
    "embedding": 2
}

v = np.random.randint(-127, 127, [10, 20]);
temp = v;
c_max = np.expand_dims(np.abs(v).max(axis = -1), -1)
c_scale = c_max / 127.0
v = (v / c_scale + 128.5).clip(1, 255).astype(np.uint8)

def write_int8(fo, v):
    c_max = np.expand_dims(np.abs(v).max(axis = -1), -1).clip(0.1, 1e100)
    c_scale = c_max / 127.0
    v = (v / c_scale + 128.5).clip(1, 255).astype(np.uint8)
    fo.write(struct.pack('i', 3))
    fo.write(struct.pack('i', 0))
    for i in range(c_max.shape[0]):
        fo.write(struct.pack('f', -c_max[i][0]));
        fo.write(struct.pack('f', c_max[i][0]));
    fo.write(v.data)

def write_int4(fo, v):
    # c_min = np.expand_dims(-np.abs(v).max(axis = -1), -1)
    # c_max = np.expand_dims(np.abs(v).max(axis = -1), -1)
    # c_scale = c_max / 7.0
    # c_min = c_scale * -8.0

    c_min = np.expand_dims(v.min(axis = -1), -1)
    c_max = np.expand_dims(v.max(axis = -1), -1)
    c_scale = (c_max - c_min) / 15.0
    c_zero = np.round(0.0 - c_min / c_scale)
    c_zero = c_zero.clip(0, 15)
    c_min = -c_scale * c_zero

    v = (v - c_min) / c_scale
    v = (v + 0.5).astype(np.int8).clip(0, 15).astype(np.uint8)
    v = v[:, 0::2] * 16 + v[:, 1::2]
    fo.write(struct.pack('i', 8))
    fo.write(struct.pack('i', 0))
    for i in range(c_min.shape[0]):
        fo.write(struct.pack('f', c_min[i][0]));
        fo.write(struct.pack('f', c_max[i][0]));
    fo.write(v.data)

def tofile(exportPath,
           model,
           tokenizer = None,
           pre_prompt = None,
           user_role = None,
           bot_role = None,
           history_sep = None,
           dtype = "float16"):
    if (dtype not in fastllm_data_type_dict):
        print("dtype should in ", list(fastllm_data_type_dict.keys()))
        exit(0)

    dict = model.state_dict()
    fo = open(exportPath, "wb")

    # 0. version id
    fo.write(struct.pack('i', 2))

    # 0.1 model info
    if model.config.model_type == "chatglm" and model.config.transformers_version == "4.30.2":
        model.config.model_type = "chatglm3"
    modelInfo = model.config.__dict__
    if model.generation_config is not None:
        modelInfo.update(model.generation_config.__dict__)
    if ("model_type" not in modelInfo):
        print("unknown model_type.")
        exit(0)

    if (pre_prompt):
        modelInfo["pre_prompt"] = pre_prompt
    if (user_role):
        modelInfo["user_role"] = user_role
    if (bot_role):
        modelInfo["bot_role"] = bot_role
    if (history_sep):
        modelInfo["history_sep"] = history_sep
    if (modelInfo["model_type"] == "baichuan" and hasattr(model, "model") and hasattr(model.model, "get_alibi_mask")):
        # Baichuan 2代
        modelInfo["use_alibi"] = "1"
        modelInfo["pre_prompt"] = ""
        modelInfo["user_role"] = ("<FLM_FIX_TOKEN_" + str(model.generation_config.user_token_id) + ">") if hasattr(model.generation_config, "user_token_id") else "";
        modelInfo["bot_role"] = ("<FLM_FIX_TOKEN_" + str(model.generation_config.assistant_token_id) + ">") if hasattr(model.generation_config, "assistant_token_id") else "";
        modelInfo["history_sep"] = ""
    if (modelInfo["model_type"] == "baichuan" and modelInfo["vocab_size"] == 125696):
        # Baichuan 2代 7B
        modelInfo["pre_prompt"] = ""
        modelInfo["user_role"] = ("<FLM_FIX_TOKEN_" + str(model.generation_config.user_token_id) + ">") if hasattr(model.generation_config, "user_token_id") else "";
        modelInfo["bot_role"] = ("<FLM_FIX_TOKEN_" + str(model.generation_config.assistant_token_id) + ">") if hasattr(model.generation_config, "assistant_token_id") else "";
        modelInfo["history_sep"] = ""
    if modelInfo["model_type"] == "qwen":
        if modelInfo["chat_format"] == "chatml":
            modelInfo["im_end_id"] = tokenizer.im_end_id
            modelInfo["im_start_id"] = tokenizer.im_start_id

    modelInfo["tokenizer_use_score"] = "1" # 分词带分数

    if hasattr(model, "peft_config"):
        adapter_size = len(model.peft_config)
        modelInfo["peft_size"] = adapter_size

    fo.write(struct.pack('i', len(modelInfo)))
    for it in modelInfo.keys():
        writeKeyValue(fo, str(it), str(modelInfo[it]))

    if hasattr(model, "peft_config"):
        for adapter_name in model.peft_config.keys():
            adapter_dict = model.peft_config[adapter_name].__dict__
            writeString(fo, adapter_name)
            fo.write(struct.pack('i', len(adapter_dict)))
            for it in adapter_dict.keys():
                writeKeyValue(fo, str(it), str(adapter_dict[it]))

    # 1. vocab
    if (tokenizer):
        if (hasattr(tokenizer, "tokenizer")):
            if (modelInfo['model_type'] == "qwen"):
                pass
            else:
                tokenizer = tokenizer.tokenizer
        if (hasattr(tokenizer, "sp_model")):
            piece_size = tokenizer.sp_model.piece_size()
            fo.write(struct.pack('i', piece_size))
            for i in range(piece_size):
                s = tokenizer.sp_model.id_to_piece(i).encode()
                fo.write(struct.pack('i', len(s)))
                for c in s:
                    fo.write(struct.pack('i', c))
                fo.write(struct.pack('i', i))
                fo.write(struct.pack('f', float(tokenizer.sp_model.get_score(i))))
        else:
            vocab = tokenizer.get_vocab()
            fo.write(struct.pack('i', len(vocab)))
            for v in vocab.keys():
                if (modelInfo['model_type'] == "qwen"):
                    s = v
                elif (modelInfo["model_type"] == "moss"):
                    s = [(ord(c) if c not in tokenizer.byte_decoder else tokenizer.byte_decoder[c]) for c in v]
                else:
                    s = v.encode()
                fo.write(struct.pack('i', len(s)))
                for c in s:
                    fo.write(struct.pack('i', c))
                fo.write(struct.pack('i', vocab[v]))
                fo.write(struct.pack('f', 1.0))
    else:
        fo.write(struct.pack('i', 0))

    weight_type_dict = {}
    module_dict = {}
    for key, m in model.named_modules():
        if (isinstance(m, torch.nn.Linear)):
            weight_type_dict[key + ".weight"] = "linear"
            module_dict[key + ".weight"] = m
        if (isinstance(m, torch.nn.Embedding)):
            weight_type_dict[key] = "embedding"

    # 2. weight
    fo.write(struct.pack('i', len(dict)))
    tot = 0
    for key in dict:
        ori_data_type = 0
        ori_np_data_type = np.float32
        cur_weight_type = 0
        if (key in weight_type_dict and weight_type_dict[key] in fastllm_weight_type_dict):
            cur_weight_type = fastllm_weight_type_dict[weight_type_dict[key]]
        to_data_type = 0
        if (cur_weight_type == 1):
            to_data_type = fastllm_data_type_dict[dtype]
            if (to_data_type == 7):
                ori_data_type = 7
                ori_np_data_type = np.float16

        cur = dict[key].numpy().astype(ori_np_data_type)
        
        if hasattr(model, "peft_config"):
            weight_name = key.replace('base_model.model.', '')
            fo.write(struct.pack('i', len(weight_name)))
            fo.write(weight_name.encode())
        else:
            fo.write(struct.pack('i', len(key)))
            fo.write(key.encode())
        fo.write(struct.pack('i', len(cur.shape)))
        for i in cur.shape:
            fo.write(struct.pack('i', i))
        if (to_data_type == 3):
            write_int8(fo, cur)
        elif (to_data_type == 8):
            write_int4(fo, cur)
        else:
            fo.write(struct.pack('i', to_data_type))
            fo.write(cur.data)
        tot += 1
        print("output (", tot, "/", len(dict), end = " )\r")
    print("\nfinish.")
    fo.close()
```

## File: `dcu-support/package/fastllm_pytools/__init__.py`
```python
__all__ = ["llm"]
```

## File: `docker/Dockerfile`
```
ARG CUDA_VERSION=11.7.1
ARG from=nvidia/cuda:${CUDA_VERSION}-cudnn8-devel-ubuntu20.04

FROM ${from} as base

ARG from

RUN <<EOF
apt update -y && apt upgrade -y && apt install -y --no-install-recommends  \
    git \
    git-lfs \
    python3 \
    python3-pip \
    python3-dev \
    wget \
    vim \
&& rm -rf /var/lib/apt/lists/*
EOF

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN git lfs install

FROM base as dev

WORKDIR /

RUN mkdir -p /data/shared/Qwen

WORKDIR /data/shared/Qwen/

# Users can also mount '/data/shared/Qwen/' to keep the data
COPY ../requirements.txt ./
COPY ../requirements_web_demo.txt ./

FROM dev as bundle_req

ARG BUNDLE_REQUIREMENTS=true

RUN <<EOF
if [ "$BUNDLE_REQUIREMENTS" = "true" ]; then 
    cd /data/shared/Qwen
    pip3 install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
    pip3 install -r requirements.txt
    pip3 install -r requirements_web_demo.txt
fi
EOF

FROM bundle_req as bundle_flash_attention
ARG BUNDLE_FLASH_ATTENTION=true

RUN <<EOF 
if [ "$BUNDLE_FLASH_ATTENTION" = "true" ]; then
    cd /data/shared/Qwen 
    test -d flash-attention || git clone -b v2.3.3 https://github.com/Dao-AILab/flash-attention
    cd /data/shared/Qwen/flash-attention &&
        pip3 install . &&
        pip3 install csrc/layer_norm
fi
EOF

FROM bundle_flash_attention as bundle_finetune
ARG BUNDLE_FINETUNE=true

RUN <<EOF
if [ "$BUNDLE_FINETUNE" = "true" ]; then
    cd /data/shared/Qwen

    # Full-finetune / LoRA.
    pip3 install deepspeed "peft==0.5.0"

    # Q-LoRA.
    apt update -y && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
        libopenmpi-dev openmpi-bin \
        && rm -rf /var/lib/apt/lists/*
    pip3 install "optimum==1.12.0" "auto-gptq==0.4.2" mpi4py
fi
EOF

FROM bundle_finetune as bundle_openai_api
ARG BUNDLE_OPENAI_API=true

RUN <<EOF
if [ "$BUNDLE_OPENAI_API" = "true" ]; then
    cd /data/shared/Qwen

    pip3 install fastapi uvicorn "openai<1.0.0" sse_starlette "pydantic<=1.10.13"
fi
EOF

FROM bundle_openai_api as final
ARG from

COPY ../requirements.txt ./
COPY ../requirements_web_demo.txt ./
COPY ../cli_demo.py ./
COPY ../web_demo.py ./
COPY ../openai_api.py ./
COPY ../finetune.py ./
COPY ../utils.py ./
COPY ./examples/* ./examples/
COPY ./eval/* ./eval/
COPY ./finetune/* ./finetune/

EXPOSE 80

WORKDIR /data/shared/Qwen/

CMD ["python3", "web_demo.py", "--server-port", "80", "--server-name", "0.0.0.0", "-c", "/data/shared/Qwen/Qwen-Chat/"]
```

## File: `docker/Dockerfile-cu114`
```
ARG CUDA_VERSION=11.4.3
ARG from=nvidia/cuda:${CUDA_VERSION}-cudnn8-devel-ubuntu20.04

FROM ${from} as base

ARG from

RUN <<EOF
apt update -y && apt upgrade -y && apt install -y --no-install-recommends  \
    git \
    git-lfs \
    python3 \
    python3-pip \
    python3-dev \
    wget \
    vim \
&& rm -rf /var/lib/apt/lists/*
EOF

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN git lfs install

FROM base as dev

WORKDIR /

RUN mkdir -p /data/shared/Qwen

WORKDIR /data/shared/Qwen/

# Users can also mount '/data/shared/Qwen/' to keep the data
COPY ../requirements.txt ./
COPY ../requirements_web_demo.txt ./

FROM dev as bundle_req

ARG BUNDLE_REQUIREMENTS=true

RUN <<EOF
if [ "$BUNDLE_REQUIREMENTS" = "true" ]; then 
    cd /data/shared/Qwen
    pip3 install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
    pip3 install -r requirements.txt
    pip3 install -r requirements_web_demo.txt
fi
EOF

FROM bundle_req as bundle_flash_attention
ARG BUNDLE_FLASH_ATTENTION=true

RUN <<EOF
if [ "$BUNDLE_FLASH_ATTENTION" = "true" ]; then
    echo "CUDA 11.4 does not support flash-attention, please try other images."
fi
EOF

FROM bundle_flash_attention as bundle_finetune
ARG BUNDLE_FINETUNE=true

RUN <<EOF
if [ "$BUNDLE_FINETUNE" = "true" ]; then
    cd /data/shared/Qwen

    # Full-finetune / LoRA.
    pip3 install deepspeed "peft==0.5.0"

    # Q-LoRA.
    apt update -y && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
        libopenmpi-dev openmpi-bin \
        && rm -rf /var/lib/apt/lists/*
    pip3 install "optimum==1.12.0" "auto-gptq==0.4.2" mpi4py
fi
EOF

FROM bundle_finetune as bundle_openai_api
ARG BUNDLE_OPENAI_API=true

RUN <<EOF
if [ "$BUNDLE_OPENAI_API" = "true" ]; then
    cd /data/shared/Qwen

    pip3 install fastapi uvicorn "openai<1.0.0" sse_starlette "pydantic<=1.10.13"
fi
EOF

FROM bundle_openai_api as final
ARG from

COPY ../requirements.txt ./
COPY ../requirements_web_demo.txt ./
COPY ../cli_demo.py ./
COPY ../web_demo.py ./
COPY ../openai_api.py ./
COPY ../finetune.py ./
COPY ../utils.py ./
COPY ./examples/* ./examples/
COPY ./eval/* ./eval/
COPY ./finetune/* ./finetune/

EXPOSE 80

WORKDIR /data/shared/Qwen/

CMD ["python3", "web_demo.py", "--server-port", "80", "--server-name", "0.0.0.0", "-c", "/data/shared/Qwen/Qwen-Chat/"]
```

## File: `docker/Dockerfile-cu121`
```
ARG CUDA_VERSION=12.1.0
ARG from=nvidia/cuda:${CUDA_VERSION}-cudnn8-devel-ubuntu20.04

FROM ${from} as base

ARG from

RUN <<EOF
apt update -y && apt upgrade -y && apt install -y --no-install-recommends  \
    git \
    git-lfs \
    python3 \
    python3-pip \
    python3-dev \
    wget \
    vim \
&& rm -rf /var/lib/apt/lists/*
EOF

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN git lfs install

FROM base as dev

WORKDIR /

RUN mkdir -p /data/shared/Qwen

WORKDIR /data/shared/Qwen/

# Users can also mount '/data/shared/Qwen/' to keep the data
COPY ../requirements.txt ./
COPY ../requirements_web_demo.txt ./

FROM dev as bundle_req

ARG BUNDLE_REQUIREMENTS=true

RUN <<EOF
if [ "$BUNDLE_REQUIREMENTS" = "true" ]; then 
    cd /data/shared/Qwen
    pip3 install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121
    pip3 install -r requirements.txt
    pip3 install -r requirements_web_demo.txt

    pip3 install transformers==4.36.0
fi
EOF

FROM bundle_req as bundle_flash_attention
ARG BUNDLE_FLASH_ATTENTION=true

RUN <<EOF 
if [ "$BUNDLE_FLASH_ATTENTION" = "true" ]; then
    cd /data/shared/Qwen 
    test -d flash-attention || git clone -b v2.3.3 https://github.com/Dao-AILab/flash-attention
    cd /data/shared/Qwen/flash-attention &&
        pip3 install . &&
        pip3 install csrc/layer_norm
fi
EOF

FROM bundle_flash_attention as bundle_finetune
ARG BUNDLE_FINETUNE=true

RUN <<EOF
if [ "$BUNDLE_FINETUNE" = "true" ]; then
    cd /data/shared/Qwen

    # Full-finetune / LoRA.
    pip3 install "deepspeed==0.12.6" "peft==0.7.1"

    # Q-LoRA.
    apt update -y && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
        libopenmpi-dev openmpi-bin \
        && rm -rf /var/lib/apt/lists/*
    pip3 install "optimum==1.14.0" "auto-gptq==0.5.0" mpi4py
fi
EOF

FROM bundle_finetune as bundle_openai_api
ARG BUNDLE_OPENAI_API=true

RUN <<EOF
if [ "$BUNDLE_OPENAI_API" = "true" ]; then
    cd /data/shared/Qwen

    pip3 install fastapi uvicorn "openai<1.0.0" sse_starlette "pydantic<=1.10.13"
fi
EOF

FROM bundle_openai_api as bundle_vllm
ARG BUNDLE_VLLM=true

RUN <<EOF
if [ "$BUNDLE_VLLM" = "true" ]; then
    cd /data/shared/Qwen

    pip3 install vllm==0.2.7 "fschat[model_worker,webui]==0.2.33"
fi
EOF

FROM bundle_vllm as final
ARG from

COPY ../requirements.txt ./
COPY ../requirements_web_demo.txt ./
COPY ../cli_demo.py ./
COPY ../web_demo.py ./
COPY ../openai_api.py ./
COPY ../finetune.py ./
COPY ../utils.py ./
COPY ./examples/* ./examples/
COPY ./eval/* ./eval/
COPY ./finetune/* ./finetune/

EXPOSE 80

WORKDIR /data/shared/Qwen/

CMD ["python3", "web_demo.py", "--server-port", "80", "--server-name", "0.0.0.0", "-c", "/data/shared/Qwen/Qwen-Chat/"]
```

## File: `docker/docker_cli_demo.sh`
```bash
#!/usr/bin/env bash
#
# This script will automatically pull docker image from DockerHub, and start a container to run the Qwen-Chat cli-demo.

IMAGE_NAME=qwenllm/qwen:cu117
QWEN_CHECKPOINT_PATH=/path/to/Qwen-Chat
CONTAINER_NAME=qwen

function usage() {
    echo '
Usage: bash docker/docker_cli_demo.sh [-i IMAGE_NAME] -c [/path/to/Qwen-Chat] [-n CONTAINER_NAME]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -i | --image-name )
            shift
            IMAGE_NAME=$1
            ;;
        -c | --checkpoint )
            shift
            QWEN_CHECKPOINT_PATH=$1
            ;;
        -n | --container-name )
            shift
            CONTAINER_NAME=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

if [ ! -e ${QWEN_CHECKPOINT_PATH}/config.json ]; then
    echo "Checkpoint config.json file not found in ${QWEN_CHECKPOINT_PATH}, exit."
    exit 1
fi

sudo docker pull ${IMAGE_NAME} || {
    echo "Pulling image ${IMAGE_NAME} failed, exit."
    exit 1
}

sudo docker run --gpus all --rm --name ${CONTAINER_NAME} \
    --mount type=bind,source=${QWEN_CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-Chat \
    -it ${IMAGE_NAME} \
    python cli_demo.py -c /data/shared/Qwen/Qwen-Chat/
```

## File: `docker/docker_openai_api.sh`
```bash
#!/usr/bin/env bash
#
# This script will automatically pull docker image from DockerHub, and start a daemon container to run the Qwen-Chat OpenAI API.

IMAGE_NAME=qwenllm/qwen:cu117
QWEN_CHECKPOINT_PATH=/path/to/Qwen-Chat
PORT=8000
CONTAINER_NAME=qwen

function usage() {
    echo '
Usage: bash docker/docker_openai_api.sh [-i IMAGE_NAME] -c [/path/to/Qwen-Chat] [-n CONTAINER_NAME] [--port PORT]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -i | --image-name )
            shift
            IMAGE_NAME=$1
            ;;
        -c | --checkpoint )
            shift
            QWEN_CHECKPOINT_PATH=$1
            ;;
        -n | --container-name )
            shift
            CONTAINER_NAME=$1
            ;;
        --port )
            shift
            PORT=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

if [ ! -e ${QWEN_CHECKPOINT_PATH}/config.json ]; then
    echo "Checkpoint config.json file not found in ${QWEN_CHECKPOINT_PATH}, exit."
    exit 1
fi

sudo docker pull ${IMAGE_NAME} || {
    echo "Pulling image ${IMAGE_NAME} failed, exit."
    exit 1
}

sudo docker run --gpus all -d --restart always --name ${CONTAINER_NAME} \
    -v /var/run/docker.sock:/var/run/docker.sock -p ${PORT}:80 \
    --mount type=bind,source=${QWEN_CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-Chat \
    -it ${IMAGE_NAME} \
    python openai_api.py --server-port 80 --server-name 0.0.0.0 -c /data/shared/Qwen/Qwen-Chat/ && {
    echo "Successfully started OpenAI API server. Access 'http://localhost:${PORT}/v1' to try!
Run \`docker logs ${CONTAINER_NAME}\` to check server status.
Run \`docker rm -f ${CONTAINER_NAME}\` to stop and remove the server."
}
```

## File: `docker/docker_web_demo.sh`
```bash
#!/usr/bin/env bash
#
# This script will automatically pull docker image from DockerHub, and start a daemon container to run the Qwen-Chat web-demo.

IMAGE_NAME=qwenllm/qwen:cu117
QWEN_CHECKPOINT_PATH=/path/to/Qwen-7B-Chat
PORT=8901
CONTAINER_NAME=qwen

function usage() {
    echo '
Usage: bash docker/docker_web_demo.sh [-i IMAGE_NAME] -c [/path/to/Qwen-Chat] [-n CONTAINER_NAME] [--port PORT]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -i | --image-name )
            shift
            IMAGE_NAME=$1
            ;;
        -c | --checkpoint )
            shift
            QWEN_CHECKPOINT_PATH=$1
            ;;
        -n | --container-name )
            shift
            CONTAINER_NAME=$1
            ;;
        --port )
            shift
            PORT=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

if [ ! -e ${QWEN_CHECKPOINT_PATH}/config.json ]; then
    echo "Checkpoint config.json file not found in ${QWEN_CHECKPOINT_PATH}, exit."
    exit 1
fi

sudo docker pull ${IMAGE_NAME} || {
    echo "Pulling image ${IMAGE_NAME} failed, exit."
    exit 1
}

sudo docker run --gpus all -d --restart always --name ${CONTAINER_NAME} \
    -v /var/run/docker.sock:/var/run/docker.sock -p ${PORT}:80 \
    --mount type=bind,source=${QWEN_CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-Chat \
    -it ${IMAGE_NAME} \
    python web_demo.py --server-port 80 --server-name 0.0.0.0 -c /data/shared/Qwen/Qwen-Chat/ && {
    echo "Successfully started web demo. Open 'http://localhost:${PORT}' to try!
Run \`docker logs ${CONTAINER_NAME}\` to check demo status.
Run \`docker rm -f ${CONTAINER_NAME}\` to stop and remove the demo."
}
```

## File: `eval/evaluate_ceval.py`
```python
import os
from typing import List
import argparse
import torch
import pandas as pd
import numpy as np
from tqdm import tqdm
from transformers.trainer_utils import set_seed
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

'''
wget https://huggingface.co/datasets/ceval/ceval-exam/resolve/main/ceval-exam.zip
mkdir data/ceval
mv ceval-exam.zip data/ceval
cd data/ceval; unzip ceval-exam.zip
cd ../../
python evaluate_ceval.py -d data/ceval/
'''

def load_models_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path,
        pad_token='<|extra_0|>',
        eos_token='<|endoftext|>',
        padding_side='left',
        trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        pad_token_id=tokenizer.pad_token_id,
        device_map="auto",
        trust_remote_code=True
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path,
        pad_token_id=tokenizer.pad_token_id,
        trust_remote_code=True
    )
    return model, tokenizer


def format_example(line, include_answer=True):
    example = "问题：" + line["question"]
    for choice in choices:
        example += f'\n{choice}. {line[f"{choice}"]}'

    if include_answer:
        example += "\n答案：" + line["answer"] + "\n\n"
    else:
        example += "\n答案："
    return example


def generate_few_shot_prompt(k, subject, dev_df):
    prompt = ""
    if k == -1:
        k = dev_df.shape[0]
    for i in range(k):
        prompt += format_example(
            dev_df.iloc[i, :],
            include_answer=True,
        )
    return prompt


def get_logits(tokenizer, model, inputs: List[str]):
    input_ids = tokenizer(inputs, padding='longest')["input_ids"]
    input_ids = torch.tensor(input_ids, device=model.device)
    tokens = {"input_ids": input_ids}
    attention_mask = input_ids.ne(tokenizer.pad_token_id)

    outputs = model(input_ids, attention_mask=attention_mask)["logits"]
    logits = outputs[:, -1, :]
    log_probs = torch.nn.functional.softmax(logits, dim=-1)
    return log_probs, {"tokens": tokens}


@torch.no_grad()
def eval_subject(
    model,
    tokenizer,
    subject_name,
    test_df,
    k=5,
    dev_df=None,
    few_shot=False,
    save_result_dir=None,
    batch_size=1,
    **kwargs,
):
    result = []
    score = []

    few_shot_prompt = (
        generate_few_shot_prompt(k, subject_name, dev_df) if few_shot else ""
    )
    all_probs = {"prob_A": [], "prob_B": [], "prob_C": [], "prob_D": []}
    if args.debug:
        print(f"few_shot_prompt: {few_shot_prompt}")

    choices_ids = torch.tensor(
        tokenizer("A")["input_ids"] + tokenizer("B")["input_ids"] +
        tokenizer("C")["input_ids"] + tokenizer("D")["input_ids"]
    ).unsqueeze(0).to(model.device)

    idx_list = list(range(0, len(test_df), batch_size))
    for i in tqdm(idx_list):
        full_prompt_list = []
        answer_list = []
        for row in test_df.iloc[i:i+batch_size].to_dict(orient='records'):
            question = format_example(row, include_answer=False)
            full_prompt = few_shot_prompt + question
            full_prompt_list.append(full_prompt)
            if 'answer' in row:
                answer_list.append(row['answer'])

        logits, input_info = get_logits(tokenizer, model, full_prompt_list)
        softval = logits.gather(1, choices_ids.expand(logits.size(0), -1)).softmax(1)
        if softval.dtype in {torch.bfloat16, torch.float16}:
            softval = softval.to(dtype=torch.float32)
        probs = softval.detach().cpu().numpy()

        for i in range(len(probs)):
            for j, choice in enumerate(choices):
                all_probs[f"prob_{choice}"].append(probs[i][j])
            pred = {0: "A", 1: "B", 2: "C", 3: "D"}[np.argmax(probs[i])]

            if answer_list != []:
                correct = 1 if pred == answer_list[i] else 0
                score.append(correct)
                if args.debug:
                    print(f'{question} pred: {pred} ref: {answer_list[i]}')
            result.append(pred)

    if score:
        correct_ratio = 100 * sum(score) / len(score)
        if args.debug:
            print(subject_name, correct_ratio)
    else:
        correct_ratio = 0
    if save_result_dir:
        test_df["model_output"] = result
        for i, choice in enumerate(choices):
            test_df[f"prob_{choice}"] = all_probs[f"prob_{choice}"]
        if score:
            test_df["correctness"] = score
        os.makedirs(save_result_dir, exist_ok=True)
        test_df.to_csv(
            os.path.join(save_result_dir, f"{subject_name}_result.csv"),
            encoding="utf-8",
            index=False,
        )

    return correct_ratio


def cal_ceval(res):
    acc_sum_dict = dict()
    acc_norm_sum_dict = dict()
    cnt_dict = dict()
    acc_sum = 0.0
    cnt = 0
    hard_cnt = 0
    hard_acc_sum = 0.0
    for tt in res.keys():
        name = tt.split("-")[-1]
        acc_sum += float(res[tt])
        cnt += 1
        class_ = TASK_NAME_MAPPING[name][2]
        if class_ not in acc_sum_dict:
            acc_sum_dict[class_] = 0.0
            acc_norm_sum_dict[class_] = 0.0
            cnt_dict[class_] = 0.0
        if name in hard_list:
            hard_cnt += 1
            hard_acc_sum += float(res[tt])
        acc_sum_dict[class_] += float(res[tt])
        cnt_dict[class_] += 1
    print("\n\n\n")
    for k in ["STEM", "Social Science", "Humanities", "Other"]:
        if k in cnt_dict:
            print("%s acc: %.2f " % (k, acc_sum_dict[k] / cnt_dict[k]))
    if hard_cnt > 0:
        print("Hard acc:%.2f " % (hard_acc_sum / hard_cnt))
    print("AVERAGE acc:%.2f " % (acc_sum / cnt))


TASK_NAME_MAPPING = {
    "computer_network": ["Computer Network", "\u8ba1\u7b97\u673a\u7f51\u7edc", "STEM"],
    "operating_system": ["Operating System", "\u64cd\u4f5c\u7cfb\u7edf", "STEM"],
    "computer_architecture": [
        "Computer Architecture",
        "\u8ba1\u7b97\u673a\u7ec4\u6210",
        "STEM",
    ],
    "college_programming": ["College Programming", "\u5927\u5b66\u7f16\u7a0b", "STEM"],
    "college_physics": ["College Physics", "\u5927\u5b66\u7269\u7406", "STEM"],
    "college_chemistry": ["College Chemistry", "\u5927\u5b66\u5316\u5b66", "STEM"],
    "advanced_mathematics": [
        "Advanced Mathematics",
        "\u9ad8\u7b49\u6570\u5b66",
        "STEM",
    ],
    "probability_and_statistics": [
        "Probability and Statistics",
        "\u6982\u7387\u7edf\u8ba1",
        "STEM",
    ],
    "discrete_mathematics": [
        "Discrete Mathematics",
        "\u79bb\u6563\u6570\u5b66",
        "STEM",
    ],
    "electrical_engineer": [
        "Electrical Engineer",
        "\u6ce8\u518c\u7535\u6c14\u5de5\u7a0b\u5e08",
        "STEM",
    ],
    "metrology_engineer": [
        "Metrology Engineer",
        "\u6ce8\u518c\u8ba1\u91cf\u5e08",
        "STEM",
    ],
    "high_school_mathematics": [
        "High School Mathematics",
        "\u9ad8\u4e2d\u6570\u5b66",
        "STEM",
    ],
    "high_school_physics": ["High School Physics", "\u9ad8\u4e2d\u7269\u7406", "STEM"],
    "high_school_chemistry": [
        "High School Chemistry",
        "\u9ad8\u4e2d\u5316\u5b66",
        "STEM",
    ],
    "high_school_biology": ["High School Biology", "\u9ad8\u4e2d\u751f\u7269", "STEM"],
    "middle_school_mathematics": [
        "Middle School Mathematics",
        "\u521d\u4e2d\u6570\u5b66",
        "STEM",
    ],
    "middle_school_biology": [
        "Middle School Biology",
        "\u521d\u4e2d\u751f\u7269",
        "STEM",
    ],
    "middle_school_physics": [
        "Middle School Physics",
        "\u521d\u4e2d\u7269\u7406",
        "STEM",
    ],
    "middle_school_chemistry": [
        "Middle School Chemistry",
        "\u521d\u4e2d\u5316\u5b66",
        "STEM",
    ],
    "veterinary_medicine": ["Veterinary Medicine", "\u517d\u533b\u5b66", "STEM"],
    "college_economics": [
        "College Economics",
        "\u5927\u5b66\u7ecf\u6d4e\u5b66",
        "Social Science",
    ],
    "business_administration": [
        "Business Administration",
        "\u5de5\u5546\u7ba1\u7406",
        "Social Science",
    ],
    "marxism": [
        "Marxism",
        "\u9a6c\u514b\u601d\u4e3b\u4e49\u57fa\u672c\u539f\u7406",
        "Social Science",
    ],
    "mao_zedong_thought": [
        "Mao Zedong Thought",
        "\u6bdb\u6cfd\u4e1c\u601d\u60f3\u548c\u4e2d\u56fd\u7279\u8272\u793e\u4f1a\u4e3b\u4e49\u7406\u8bba\u4f53\u7cfb\u6982\u8bba",
        "Social Science",
    ],
    "education_science": ["Education Science", "\u6559\u80b2\u5b66", "Social Science"],
    "teacher_qualification": [
        "Teacher Qualification",
        "\u6559\u5e08\u8d44\u683c",
        "Social Science",
    ],
    "high_school_politics": [
        "High School Politics",
        "\u9ad8\u4e2d\u653f\u6cbb",
        "Social Science",
    ],
    "high_school_geography": [
        "High School Geography",
        "\u9ad8\u4e2d\u5730\u7406",
        "Social Science",
    ],
    "middle_school_politics": [
        "Middle School Politics",
        "\u521d\u4e2d\u653f\u6cbb",
        "Social Science",
    ],
    "middle_school_geography": [
        "Middle School Geography",
        "\u521d\u4e2d\u5730\u7406",
        "Social Science",
    ],
    "modern_chinese_history": [
        "Modern Chinese History",
        "\u8fd1\u4ee3\u53f2\u7eb2\u8981",
        "Humanities",
    ],
    "ideological_and_moral_cultivation": [
        "Ideological and Moral Cultivation",
        "\u601d\u60f3\u9053\u5fb7\u4fee\u517b\u4e0e\u6cd5\u5f8b\u57fa\u7840",
        "Humanities",
    ],
    "logic": ["Logic", "\u903b\u8f91\u5b66", "Humanities"],
    "law": ["Law", "\u6cd5\u5b66", "Humanities"],
    "chinese_language_and_literature": [
        "Chinese Language and Literature",
        "\u4e2d\u56fd\u8bed\u8a00\u6587\u5b66",
        "Humanities",
    ],
    "art_studies": ["Art Studies", "\u827a\u672f\u5b66", "Humanities"],
    "professional_tour_guide": [
        "Professional Tour Guide",
        "\u5bfc\u6e38\u8d44\u683c",
        "Humanities",
    ],
    "legal_professional": [
        "Legal Professional",
        "\u6cd5\u5f8b\u804c\u4e1a\u8d44\u683c",
        "Humanities",
    ],
    "high_school_chinese": [
        "High School Chinese",
        "\u9ad8\u4e2d\u8bed\u6587",
        "Humanities",
    ],
    "high_school_history": [
        "High School History",
        "\u9ad8\u4e2d\u5386\u53f2",
        "Humanities",
    ],
    "middle_school_history": [
        "Middle School History",
        "\u521d\u4e2d\u5386\u53f2",
        "Humanities",
    ],
    "civil_servant": ["Civil Servant", "\u516c\u52a1\u5458", "Other"],
    "sports_science": ["Sports Science", "\u4f53\u80b2\u5b66", "Other"],
    "plant_protection": ["Plant Protection", "\u690d\u7269\u4fdd\u62a4", "Other"],
    "basic_medicine": ["Basic Medicine", "\u57fa\u7840\u533b\u5b66", "Other"],
    "clinical_medicine": ["Clinical Medicine", "\u4e34\u5e8a\u533b\u5b66", "Other"],
    "urban_and_rural_planner": [
        "Urban and Rural Planner",
        "\u6ce8\u518c\u57ce\u4e61\u89c4\u5212\u5e08",
        "Other",
    ],
    "accountant": ["Accountant", "\u6ce8\u518c\u4f1a\u8ba1\u5e08", "Other"],
    "fire_engineer": [
        "Fire Engineer",
        "\u6ce8\u518c\u6d88\u9632\u5de5\u7a0b\u5e08",
        "Other",
    ],
    "environmental_impact_assessment_engineer": [
        "Environmental Impact Assessment Engineer",
        "\u73af\u5883\u5f71\u54cd\u8bc4\u4ef7\u5de5\u7a0b\u5e08",
        "Other",
    ],
    "tax_accountant": ["Tax Accountant", "\u7a0e\u52a1\u5e08", "Other"],
    "physician": ["Physician", "\u533b\u5e08\u8d44\u683c", "Other"],
}
hard_list = [
    "advanced_mathematics",
    "discrete_mathematics",
    "probability_and_statistics",
    "college_physics",
    "college_chemistry",
    "high_school_mathematics",
    "high_school_physics",
    "high_school_chemistry",
]
choices = ["A", "B", "C", "D"]


def main(args):
    model, tokenizer = load_models_tokenizer(args)

    dev_result = {}
    for subject_name in tqdm(TASK_NAME_MAPPING.keys()):
        val_file_path = os.path.join(
            args.eval_data_path, "val", f"{subject_name}_val.csv"
        )
        dev_file_path = os.path.join(
            args.eval_data_path, "dev", f"{subject_name}_dev.csv"
        )
        # test_file_path = os.path.join(args.eval_data_path, 'test', f'{subject_name}_test.csv')
        val_df = pd.read_csv(val_file_path)
        dev_df = pd.read_csv(dev_file_path)
        # test_df = pd.read_csv(test_file_path)

        score = eval_subject(
            model,
            tokenizer,
            subject_name,
            val_df,
            dev_df=dev_df,
            k=5,
            few_shot=True,
            save_result_dir=f"outs/ceval_eval_result",
            batch_size=args.batch_size
        )
        dev_result[subject_name] = score
    cal_ceval(dev_result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        help="Checkpoint path",
        default="Qwen/Qwen-7B",
    )
    parser.add_argument("-s", "--seed", type=int, default=1234, help="Random seed")

    # Provide extra arguments required for tasks
    group = parser.add_argument_group(title="Evaluation options")
    group.add_argument(
        "-d", "--eval_data_path", type=str, required=True, help="Path to eval data"
    )
    group.add_argument(
        "--max-seq-len",
        type=int,
        default=2048,
        help="Size of the output generated text.",
    )
    group.add_argument(
        "--debug", action="store_true", default=False, help="Print infos."
    )
    group.add_argument(
        "--batch-size",
        type=int,
        default=1,
        help="batch size",
    )

    args = parser.parse_args()
    set_seed(args.seed)

    main(args)
```

## File: `eval/evaluate_chat_ceval.py`
```python
import os
import argparse
import re
import torch
import pandas as pd
from thefuzz import process
from tqdm import tqdm
from transformers.trainer_utils import set_seed
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

'''
wget https://huggingface.co/datasets/ceval/ceval-exam/resolve/main/ceval-exam.zip
mkdir data/ceval
mv ceval-exam.zip data/ceval
cd data/ceval; unzip ceval-exam.zip
cd ../../

pip install thefuzz
python eval/evaluate_chat_ceval.py -d data/ceval
'''

def load_models_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path, device_map="auto", trust_remote_code=True
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model.generation_config.do_sample = False  # use greedy decoding
    model.generation_config.repetition_penalty = 1.0  # disable repetition penalty
    return model, tokenizer

def process_before_extraction(gen, question, choice_dict):
    # Example Prompt:
    # 关于传输层的面向连接服务的特性是____。
    # A. 既不保证可靠，也不保证按序交付
    # B. 不保证可靠，但保证按序交付
    # C. 保证可靠，但不保证按序交付
    # D. 既保证可靠，也保证按序交付
    # Example Model Output：
    # 关于传输层的面向连接服务的特性是既保证可靠，也保证按序交付
    # Processed Output:
    # 答案是D

    question_split = question.rstrip("。").split("。")[-1].split("_")

    # replacing the question
    if len(question_split[0].strip()) > 4:
        gen = gen.replace(question_split[0], "答案是")
    if len(question_split[-1].strip()) > 4:
        gen = gen.replace(question_split[-1], "")

    # replace the choice by letter in the generated sentence
    # from longest one to shortest one
    for key, val in sorted(choice_dict.items(), key=lambda x: len(x[1]), reverse=True):
        gen = gen.replace(val.rstrip("。"), key)
    return gen


def count_substr(gen, pattern):
    return len(re.findall(pattern, gen))


def extract_choice(gen, prompt, choice_list):
    # 答案是A | 选项是A | 应该选A选项
    res = re.search(
        r"(?:(?:选|选择|选定)[：:]?\s*|(?:(?:答案|选项)(?![^ABCD]{0,10}?(?:不|非)[^ABCD]{0,10}?(?:是|选|为|：|:|】))[^ABCD]{0,10}?(?:是|选|为|：|:|】))[^ABCD]{0,10}?)(A|B|C|D)(?:选项)?(?:\)|。|\.|，|,|．|、|A|B|C|D|$|：|:|\)|）)",
        gen,
    )

    # A选项正确 | A选项符合题意
    if res is None:
        res = re.search(
            r"(A|B|C|D)(?:选?项)?(?![^ABCD]{0,4}?(?:不|非)[^ABCD]{0,4}?(?:正确|对[的，。：]|符合))[^ABCD]{0,4}?(?:正确|对[的，。：]|符合)",
            gen,
        )

    # 直接输出 A
    if res is None:
        res = re.search(r"^[\(（]?(A|B|C|D)(?:。|\)|）|\.|，|,|．|：|:|$)", gen)

    # 获取第一个出现的字母
    if res is None:
        res = re.search(r"(?<![a-zA-Z])(A|B|C|D)(?![a-zA-Z=])", gen)

    if res is None:
        return choices[choice_list.index(process.extractOne(gen, choice_list)[0])]
    return res.group(1)


def format_example(line):
    example = line["question"] + "\n\n"
    for choice in choices:
        example += f'{choice}. {line[f"{choice}"]}\n'
    return example


def extract_answer(response, row):
    prompt = row["question"]
    gen = process_before_extraction(
        response, prompt, {choice: row[choice] for choice in choices}
    )
    if not isinstance(prompt, str):
        prompt = prompt[0]
    pred = extract_choice(gen, prompt, [row[choice] for choice in choices])
    return pred


@torch.no_grad()
def eval_subject(
    model,
    tokenizer,
    subject_name,
    test_df,
    save_result_dir=None,
    overwrite=False,
    **kwargs
):
    result_path = os.path.join(save_result_dir, f"{subject_name}_result.csv")
    if not overwrite and os.path.exists(result_path):
        print(f"{result_path} existed, skip!")
        score = []
        for (_, datarow), (_, resultrow) in zip(
            test_df.iterrows(), pd.read_csv(result_path).iterrows()
        ):
            pred = extract_answer(resultrow["model_response"], datarow)
            correct = 1 if pred == datarow["answer"] else 0
            score.append(correct)
        correct_ratio = 100 * sum(score) / len(score)
        return correct_ratio

    responses = []
    result = []
    score = []

    for _, row in tqdm(test_df.iterrows(), total=len(test_df)):
        question = format_example(row)

        response, _ = model.chat(
            tokenizer,
            question,
            history=None,
        )
        print(question)
        print(response)
        pred = extract_answer(response, row)
        print(pred)
        print("======================")

        if "answer" in row:
            correct = 1 if pred == row["answer"] else 0
            score.append(correct)
            if args.debug:
                print(f'{question} pred: {pred} ref: {row["answer"]}')
        responses.append(response)
        result.append(pred)

    if score:
        correct_ratio = 100 * sum(score) / len(score)
        if args.debug:
            print(subject_name, correct_ratio)
    else:
        correct_ratio = 0
    if save_result_dir:
        test_df["model_response"] = responses
        test_df["model_output"] = result
        if score:
            test_df["correctness"] = score
        os.makedirs(save_result_dir, exist_ok=True)
        test_df.to_csv(result_path, encoding="utf-8", index=False)

    return correct_ratio


def cal_ceval(res):
    acc_sum_dict = dict()
    acc_norm_sum_dict = dict()
    cnt_dict = dict()
    acc_sum = 0.0
    cnt = 0
    hard_cnt = 0
    hard_acc_sum = 0.0
    for tt in res.keys():
        name = tt.split("-")[-1]
        acc_sum += float(res[tt])
        cnt += 1
        class_ = TASK_NAME_MAPPING[name][2]
        if class_ not in acc_sum_dict:
            acc_sum_dict[class_] = 0.0
            acc_norm_sum_dict[class_] = 0.0
            cnt_dict[class_] = 0.0
        if name in hard_list:
            hard_cnt += 1
            hard_acc_sum += float(res[tt])
        acc_sum_dict[class_] += float(res[tt])
        cnt_dict[class_] += 1
    print("\n\n\n")
    for k in ["STEM", "Social Science", "Humanities", "Other"]:
        if k in cnt_dict:
            print("%s acc: %.2f " % (k, acc_sum_dict[k] / cnt_dict[k]))
    if hard_cnt > 0:
        print("Hard acc:%.2f " % (hard_acc_sum / hard_cnt))
    print("AVERAGE acc:%.2f " % (acc_sum / cnt))


TASK_NAME_MAPPING = {
    "computer_network": ["Computer Network", "\u8ba1\u7b97\u673a\u7f51\u7edc", "STEM"],
    "operating_system": ["Operating System", "\u64cd\u4f5c\u7cfb\u7edf", "STEM"],
    "computer_architecture": [
        "Computer Architecture",
        "\u8ba1\u7b97\u673a\u7ec4\u6210",
        "STEM",
    ],
    "college_programming": ["College Programming", "\u5927\u5b66\u7f16\u7a0b", "STEM"],
    "college_physics": ["College Physics", "\u5927\u5b66\u7269\u7406", "STEM"],
    "college_chemistry": ["College Chemistry", "\u5927\u5b66\u5316\u5b66", "STEM"],
    "advanced_mathematics": [
        "Advanced Mathematics",
        "\u9ad8\u7b49\u6570\u5b66",
        "STEM",
    ],
    "probability_and_statistics": [
        "Probability and Statistics",
        "\u6982\u7387\u7edf\u8ba1",
        "STEM",
    ],
    "discrete_mathematics": [
        "Discrete Mathematics",
        "\u79bb\u6563\u6570\u5b66",
        "STEM",
    ],
    "electrical_engineer": [
        "Electrical Engineer",
        "\u6ce8\u518c\u7535\u6c14\u5de5\u7a0b\u5e08",
        "STEM",
    ],
    "metrology_engineer": [
        "Metrology Engineer",
        "\u6ce8\u518c\u8ba1\u91cf\u5e08",
        "STEM",
    ],
    "high_school_mathematics": [
        "High School Mathematics",
        "\u9ad8\u4e2d\u6570\u5b66",
        "STEM",
    ],
    "high_school_physics": ["High School Physics", "\u9ad8\u4e2d\u7269\u7406", "STEM"],
    "high_school_chemistry": [
        "High School Chemistry",
        "\u9ad8\u4e2d\u5316\u5b66",
        "STEM",
    ],
    "high_school_biology": ["High School Biology", "\u9ad8\u4e2d\u751f\u7269", "STEM"],
    "middle_school_mathematics": [
        "Middle School Mathematics",
        "\u521d\u4e2d\u6570\u5b66",
        "STEM",
    ],
    "middle_school_biology": [
        "Middle School Biology",
        "\u521d\u4e2d\u751f\u7269",
        "STEM",
    ],
    "middle_school_physics": [
        "Middle School Physics",
        "\u521d\u4e2d\u7269\u7406",
        "STEM",
    ],
    "middle_school_chemistry": [
        "Middle School Chemistry",
        "\u521d\u4e2d\u5316\u5b66",
        "STEM",
    ],
    "veterinary_medicine": ["Veterinary Medicine", "\u517d\u533b\u5b66", "STEM"],
    "college_economics": [
        "College Economics",
        "\u5927\u5b66\u7ecf\u6d4e\u5b66",
        "Social Science",
    ],
    "business_administration": [
        "Business Administration",
        "\u5de5\u5546\u7ba1\u7406",
        "Social Science",
    ],
    "marxism": [
        "Marxism",
        "\u9a6c\u514b\u601d\u4e3b\u4e49\u57fa\u672c\u539f\u7406",
        "Social Science",
    ],
    "mao_zedong_thought": [
        "Mao Zedong Thought",
        "\u6bdb\u6cfd\u4e1c\u601d\u60f3\u548c\u4e2d\u56fd\u7279\u8272\u793e\u4f1a\u4e3b\u4e49\u7406\u8bba\u4f53\u7cfb\u6982\u8bba",
        "Social Science",
    ],
    "education_science": ["Education Science", "\u6559\u80b2\u5b66", "Social Science"],
    "teacher_qualification": [
        "Teacher Qualification",
        "\u6559\u5e08\u8d44\u683c",
        "Social Science",
    ],
    "high_school_politics": [
        "High School Politics",
        "\u9ad8\u4e2d\u653f\u6cbb",
        "Social Science",
    ],
    "high_school_geography": [
        "High School Geography",
        "\u9ad8\u4e2d\u5730\u7406",
        "Social Science",
    ],
    "middle_school_politics": [
        "Middle School Politics",
        "\u521d\u4e2d\u653f\u6cbb",
        "Social Science",
    ],
    "middle_school_geography": [
        "Middle School Geography",
        "\u521d\u4e2d\u5730\u7406",
        "Social Science",
    ],
    "modern_chinese_history": [
        "Modern Chinese History",
        "\u8fd1\u4ee3\u53f2\u7eb2\u8981",
        "Humanities",
    ],
    "ideological_and_moral_cultivation": [
        "Ideological and Moral Cultivation",
        "\u601d\u60f3\u9053\u5fb7\u4fee\u517b\u4e0e\u6cd5\u5f8b\u57fa\u7840",
        "Humanities",
    ],
    "logic": ["Logic", "\u903b\u8f91\u5b66", "Humanities"],
    "law": ["Law", "\u6cd5\u5b66", "Humanities"],
    "chinese_language_and_literature": [
        "Chinese Language and Literature",
        "\u4e2d\u56fd\u8bed\u8a00\u6587\u5b66",
        "Humanities",
    ],
    "art_studies": ["Art Studies", "\u827a\u672f\u5b66", "Humanities"],
    "professional_tour_guide": [
        "Professional Tour Guide",
        "\u5bfc\u6e38\u8d44\u683c",
        "Humanities",
    ],
    "legal_professional": [
        "Legal Professional",
        "\u6cd5\u5f8b\u804c\u4e1a\u8d44\u683c",
        "Humanities",
    ],
    "high_school_chinese": [
        "High School Chinese",
        "\u9ad8\u4e2d\u8bed\u6587",
        "Humanities",
    ],
    "high_school_history": [
        "High School History",
        "\u9ad8\u4e2d\u5386\u53f2",
        "Humanities",
    ],
    "middle_school_history": [
        "Middle School History",
        "\u521d\u4e2d\u5386\u53f2",
        "Humanities",
    ],
    "civil_servant": ["Civil Servant", "\u516c\u52a1\u5458", "Other"],
    "sports_science": ["Sports Science", "\u4f53\u80b2\u5b66", "Other"],
    "plant_protection": ["Plant Protection", "\u690d\u7269\u4fdd\u62a4", "Other"],
    "basic_medicine": ["Basic Medicine", "\u57fa\u7840\u533b\u5b66", "Other"],
    "clinical_medicine": ["Clinical Medicine", "\u4e34\u5e8a\u533b\u5b66", "Other"],
    "urban_and_rural_planner": [
        "Urban and Rural Planner",
        "\u6ce8\u518c\u57ce\u4e61\u89c4\u5212\u5e08",
        "Other",
    ],
    "accountant": ["Accountant", "\u6ce8\u518c\u4f1a\u8ba1\u5e08", "Other"],
    "fire_engineer": [
        "Fire Engineer",
        "\u6ce8\u518c\u6d88\u9632\u5de5\u7a0b\u5e08",
        "Other",
    ],
    "environmental_impact_assessment_engineer": [
        "Environmental Impact Assessment Engineer",
        "\u73af\u5883\u5f71\u54cd\u8bc4\u4ef7\u5de5\u7a0b\u5e08",
        "Other",
    ],
    "tax_accountant": ["Tax Accountant", "\u7a0e\u52a1\u5e08", "Other"],
    "physician": ["Physician", "\u533b\u5e08\u8d44\u683c", "Other"],
}
hard_list = [
    "advanced_mathematics",
    "discrete_mathematics",
    "probability_and_statistics",
    "college_physics",
    "college_chemistry",
    "high_school_mathematics",
    "high_school_physics",
    "high_school_chemistry",
]
choices = ["A", "B", "C", "D"]


def main(args):
    print("loading model weights")
    if args.checkpoint_path:
        model, tokenizer = load_models_tokenizer(args)
    else:
        model, tokenizer = None, None
    print("model loaded")
    dev_result = {}
    for subject_name in tqdm(TASK_NAME_MAPPING.keys()):
        val_file_path = os.path.join(
            args.eval_data_path, "val", f"{subject_name}_val.csv"
        )
        val_df = pd.read_csv(val_file_path)

        score = eval_subject(
            model,
            tokenizer,
            subject_name,
            val_df,
            save_result_dir="outs_chat/ceval_eval_result",
            overwrite=args.overwrite,
        )
        dev_result[subject_name] = score
    cal_ceval(dev_result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        help="Checkpoint path",
        default="Qwen/Qwen-7B-Chat",
    )
    parser.add_argument("-s", "--seed", type=int, default=1234, help="Random seed")

    # Provide extra arguments required for tasks
    group = parser.add_argument_group(title="Evaluation options")
    group.add_argument(
        "-d", "--eval_data_path", type=str, required=True, help="Path to eval data"
    )
    group.add_argument(
        "--debug", action="store_true", default=False, help="Print infos."
    )
    group.add_argument(
        "--overwrite",
        action="store_true",
        default=False,
        help="Overwrite existed results",
    )

    args = parser.parse_args()
    set_seed(args.seed)

    main(args)
```

## File: `eval/evaluate_chat_gsm8k.py`
```python
import json
import re
from pathlib import Path
import argparse
import requests
import math
import numpy as np
import tqdm
from datasets import load_from_disk, load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

"""
python eval/evaluate_chat_gsm8k.py [--use-fewshot]
"""

INVALID_ANS = "[invalid]"
DEVICE = "cuda:0"

def doc_to_text(doc, use_fewshot):
    if use_fewshot:
        context = (
            "Question: Angelo and Melanie want to plan how many hours over the next week they should study together for their test next week. They have 2 chapters of their textbook to study and 4 worksheets to memorize. They figure out that they should dedicate 3 hours to each chapter of their textbook and 1.5 hours for each worksheet. If they plan to study no more than 4 hours each day, how many days should they plan to study total over the next week if they take a 10-minute break every hour, include 3 10-minute snack breaks each day, and 30 minutes for lunch each day?\nLet's think step by step\n"
            "Angelo and Melanie think they should dedicate 3 hours to each of the 2 chapters, 3 hours x 2 chapters = 6 hours total.\nFor the worksheets they plan to dedicate 1.5 hours for each worksheet, 1.5 hours x 4 worksheets = 6 hours total.\nAngelo and Melanie need to start with planning 12 hours to study, at 4 hours a day, 12 / 4 = 3 days.\nHowever, they need to include time for breaks and lunch. Every hour they want to include a 10-minute break, so 12 total hours x 10 minutes = 120 extra minutes for breaks.\nThey also want to include 3 10-minute snack breaks, 3 x 10 minutes = 30 minutes.\nAnd they want to include 30 minutes for lunch each day, so 120 minutes for breaks + 30 minutes for snack breaks + 30 minutes for lunch = 180 minutes, or 180 / 60 minutes per hour = 3 extra hours.\nSo Angelo and Melanie want to plan 12 hours to study + 3 hours of breaks = 15 hours total.\nThey want to study no more than 4 hours each day, 15 hours / 4 hours each day = 3.75\nThey will need to plan to study 4 days to allow for all the time they need.\nThe answer is 4\n\n"
            "Question: Mark's basketball team scores 25 2 pointers, 8 3 pointers and 10 free throws.  Their opponents score double the 2 pointers but half the 3 pointers and free throws.  What's the total number of points scored by both teams added together?\nLet's think step by step\n"
            "Mark's team scores 25 2 pointers, meaning they scored 25*2= 50 points in 2 pointers.\nHis team also scores 6 3 pointers, meaning they scored 8*3= 24 points in 3 pointers\nThey scored 10 free throws, and free throws count as one point so they scored 10*1=10 points in free throws.\nAll together his team scored 50+24+10= 84 points\nMark's opponents scored double his team's number of 2 pointers, meaning they scored 50*2=100 points in 2 pointers.\nHis opponents scored half his team's number of 3 pointers, meaning they scored 24/2= 12 points in 3 pointers.\nThey also scored half Mark's team's points in free throws, meaning they scored 10/2=5 points in free throws.\nAll together Mark's opponents scored 100+12+5=117 points\nThe total score for the game is both team's scores added together, so it is 84+117=201 points\nThe answer is 201\n\n"
            "Question: Bella has two times as many marbles as frisbees. She also has 20 more frisbees than deck cards. If she buys 2/5 times more of each item, what would be the total number of the items she will have if she currently has 60 marbles?\nLet's think step by step\n"
            "When Bella buys 2/5 times more marbles, she'll have increased the number of marbles by 2/5*60 = 24\nThe total number of marbles she'll have is 60+24 = 84\nIf Bella currently has 60 marbles, and she has two times as many marbles as frisbees, she has 60/2 = 30 frisbees.\nIf Bella buys 2/5 times more frisbees, she'll have 2/5*30 = 12 more frisbees.\nThe total number of frisbees she'll have will increase to 30+12 = 42\nBella also has 20 more frisbees than deck cards, meaning she has 30-20 = 10 deck cards\nIf she buys 2/5 times more deck cards, she'll have 2/5*10 = 4 more deck cards.\nThe total number of deck cards she'll have is 10+4 = 14\nTogether, Bella will have a total of 14+42+84 = 140 items\nThe answer is 140\n\n"
            "Question: A group of 4 fruit baskets contains 9 apples, 15 oranges, and 14 bananas in the first three baskets and 2 less of each fruit in the fourth basket. How many fruits are there?\nLet's think step by step\n"
            "For the first three baskets, the number of apples and oranges in one basket is 9+15=24\nIn total, together with bananas, the number of fruits in one basket is 24+14=38 for the first three baskets.\nSince there are three baskets each having 38 fruits, there are 3*38=114 fruits in the first three baskets.\nThe number of apples in the fourth basket is 9-2=7\nThere are also 15-2=13 oranges in the fourth basket\nThe combined number of oranges and apples in the fourth basket is 13+7=20\nThe fourth basket also contains 14-2=12 bananas.\nIn total, the fourth basket has 20+12=32 fruits.\nThe four baskets together have 32+114=146 fruits.\nThe answer is 146\n\n"
            f"Question: {doc['question']}\nLet's think step by step"
        )
    else:
        context = doc["question"]
    return context

def generate_sample(model, tokenizer, question):
    response, _ = model.chat(
        tokenizer,
        question,
        history=None,
    )
    print(question)
    print("-------------")
    print(response)
    print("=============")
    return response

def extract_answer(s):
    _PAT_LAST_DIGIT = re.compile(
        r"([+-])?(?=([0-9]|\.[0-9]))(0|([1-9](\d{0,2}(,\d{3})*)|\d*))?(\.\d*)?(?=\D|$)"
    )
    match = list(_PAT_LAST_DIGIT.finditer(s))
    if match:
        last_digit = match[-1].group().replace(",", "").replace("+", "").strip()
        # print(f"The last digit in {s} is {last_digit}")
    else:
        last_digit = None
        print(f"No digits found in {s!r}", flush=True)
    return last_digit

def is_correct(completion, answer):
    gold = extract_answer(answer)
    assert gold is not None, "No ground truth answer found in the document."

    def number_equal(answer, pred):
        if pred is None:
            return False
        try:
            return math.isclose(eval(answer), eval(pred), rel_tol=0, abs_tol=1e-4)
        except:
            print(
                f"cannot compare two numbers: answer={answer}, pred={pred}", flush=True
            )
            return False

    return number_equal(gold, extract_answer(completion))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=Path,
        help="Checkpoint path",
        default="Qwen/Qwen-7B-Chat",
    )
    parser.add_argument("-f", "--sample-input-file", type=str, default=None)
    parser.add_argument(
        "-o", "--sample-output-file", type=str, default="gsm8k_res.jsonl"
    )
    parser.add_argument("--use-fewshot", action="store_true")

    args = parser.parse_args()

    if args.sample_input_file is not None:
        dataset = load_from_disk(args.sample_input_file)  # or:
    else:
        dataset = load_dataset("gsm8k", "main")

    print("Loading tokenizer ...")
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True, bf16=True, use_flash_attn=True
    )

    print("Loading model ...")
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path, device_map="auto", trust_remote_code=True
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model.generation_config.do_sample = False  # use greedy decoding
    model.generation_config.repetition_penalty = 1.0  # disable repetition penalty

    test = dataset["test"]

    f_output = open(args.sample_output_file, "w", encoding="utf-8")
    tot_length = test.num_rows
    acc_res = []
    for doc in tqdm.tqdm(test):
        context = doc_to_text(doc, args.use_fewshot)
        completion = generate_sample(model, tokenizer, context)
        answer = doc["answer"]
        acc = is_correct(completion, answer)
        doc["completion"] = completion
        doc["acc"] = acc
        f_output.write(json.dumps(doc, ensure_ascii=False) + "\n")
        f_output.flush()
        acc_res.append(acc)

    f_output.close()
    print("4-shot Acc: " if args.use_fewshot else "Zero-shot Acc", np.mean(acc_res))
```

## File: `eval/evaluate_chat_humaneval.py`
```python
import re
import textwrap
import argparse
from pathlib import Path
import tqdm
import jsonlines
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

"""
Get the HumanEval.jsonl file from [here](https://github.com/openai/human-eval/tree/master/data)

python eval/evaluate_chat_humaneval.py -f HumanEval.jsonl -o HumanEval_res.jsonl
git clone https://github.com/openai/human-eval
pip install -e human-eval
evaluate_functional_correctness HumanEval_res.jsonl
"""

DEVICE = "cuda:0"


def extract_code(text, entry_point):
    # 正则表达式匹配代码块
    code_block_pattern = re.compile(
        rf"```(?:[Pp]ython\n)?.*?def\s+{entry_point}.*?:\n(.*?)\n```", re.DOTALL
    )
    code_block = code_block_pattern.search(text)
    if code_block is None:
        code_block_pattern = re.compile(
            rf"def\s+{entry_point}.*?:\n(.*?)(?:\n(?!\n*(?:  |\t))|$)", re.DOTALL
        )
        code_block = code_block_pattern.search(text)
    if code_block is None:
        code_block_pattern = re.compile(
            r"def.*?:\n(.*?)(?:\n(?!\n*(?:  |\t))|$)", re.DOTALL
        )
        code_block = code_block_pattern.search(text)

    if code_block is not None:
        return code_block.group(1)

    # if no code block is found, assume the LM is simply filling the code
    return textwrap.indent(text, " " * 4)


def generate_sample(model, tokenizer, question, entry_point):
    response, _ = model.chat(
        tokenizer,
        question,
        history=None,
    )
    print(question)
    print(response)
    answer = extract_code(response, entry_point)
    return answer, response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=Path,
        help="Checkpoint path",
        default="Qwen/Qwen-7B-Chat",
    )
    parser.add_argument(
        "-f",
        "--sample-input-file",
        type=str,
        default=None,
        help="data path to HumanEval.jsonl",
    )
    parser.add_argument(
        "-o", "--sample-output-file", type=str, default="HumanEval_res.jsonl"
    )

    args = parser.parse_args()
    print("Loading tokenizer ...")
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )

    print("Loading model ...")
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        device_map="auto",
        trust_remote_code=True,
        bf16=True,
        use_flash_attn=True,
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model.generation_config.do_sample = False  # use greedy decoding
    model.generation_config.repetition_penalty = 1.0  # disable repetition penalty

    f_output = jsonlines.Writer(open(args.sample_output_file, "w", encoding="utf-8"))

    f = jsonlines.open(args.sample_input_file)
    with f_output as output:
        for jobj in tqdm.tqdm(f, desc="task_idx"):
            # use humanevalpack prompt
            signature = re.search(
                rf"def\s+({jobj['entry_point']}.*?):\s*\n", jobj["prompt"]
            ).group(1)
            description = "\n".join(
                [
                    line.strip()
                    for line in re.search(
                        rf"(?:\"\"\"|''')(.*?)(?:\"\"\"|''')", jobj["prompt"], re.DOTALL
                    )
                    .group(1)
                    .split("\n")
                ]
            )
            prompt = (
                f"Write a Python function `{signature}` to solve the following problem:\n"
                f"{description}\n"
                f"{jobj['prompt']}"
            )

            task_id = jobj["task_id"]
            answer, response = generate_sample(
                model, tokenizer, prompt, jobj["entry_point"]
            )
            gen_jobjs = {"task_id": task_id, "completion": answer, "response": response}
            output.write(gen_jobjs)
    f_output.close()
```

## File: `eval/evaluate_chat_mmlu.py`
```python
import os
import argparse
import re
import torch
import pandas as pd
from tqdm import tqdm
from thefuzz import process
from transformers.trainer_utils import set_seed
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

'''
wget https://people.eecs.berkeley.edu/~hendrycks/data.tar
mkdir data/mmlu
mv data.tar data/mmlu
cd data/mmlu; tar xf data.tar
cd ../../

pip install thefuzz
python eval/evaluate_chat_mmlu.py -d data/mmlu/data/
'''

def load_models_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        device_map="auto",
        trust_remote_code=True,
        bf16=True,
        use_flash_attn=True,
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model.generation_config.do_sample = False  # use greedy decoding
    model.generation_config.repetition_penalty = 1.0  # disable repetition penalty
    return model, tokenizer


def format_example(line):
    example = (
        "The following is a multiple-choice question. Please choose the most suitable one among A, B, C and D as the answer to this question.\n\n"
        + line["question"]
        + "\n"
    )
    for choice in choices:
        example += f'{choice}. {line[f"{choice}"]}\n'
    return example


def process_before_extraction(gen, choice_dict):
    # replace the choice by letter in the generated sentence
    # from longest one to shortest one
    for key, val in sorted(choice_dict.items(), key=lambda x: len(x[1]), reverse=True):
        pattern = re.compile(re.escape(val.rstrip(".")), re.IGNORECASE)
        gen = pattern.sub(key, gen)
    return gen


def extract_choice(gen, choice_list):
    # answer is A | choice is A | choose A
    res = re.search(
        r"(?:(?:[Cc]hoose)|(?:(?:[Aa]nswer|[Cc]hoice)(?![^ABCD]{0,20}?(?:n't|not))[^ABCD]{0,10}?\b(?:|is|:|be))\b)[^ABCD]{0,20}?\b(A|B|C|D)\b",
        gen,
    )

    # A is correct | A is right
    if res is None:
        res = re.search(
            r"\b(A|B|C|D)\b(?![^ABCD]{0,8}?(?:n't|not)[^ABCD]{0,5}?(?:correct|right))[^ABCD]{0,10}?\b(?:correct|right)\b",
            gen,
        )

    # straight answer: A
    if res is None:
        res = re.search(r"^(A|B|C|D)(?:\.|,|:|$)", gen)

    # simply extract the first appearred letter
    if res is None:
        res = re.search(r"(?<![a-zA-Z])(A|B|C|D)(?![a-zA-Z=])", gen)

    if res is None:
        return choices[choice_list.index(process.extractOne(gen, choice_list)[0])]
    return res.group(1)


def extract_answer(response, row):
    gen = process_before_extraction(
        response, {choice: row[choice] for choice in choices}
    )
    pred = extract_choice(gen, [row[choice] for choice in choices])
    return pred


@torch.no_grad()
def eval_subject(
    model,
    tokenizer,
    subject_name,
    test_df,
    save_result_dir=None,
    overwrite=False,
    **kwargs
):
    result_path = os.path.join(save_result_dir, f"{subject_name}_result.csv")
    if not overwrite and os.path.exists(result_path):
        print(f"{result_path} existed, skip!")
        score = []
        for (_, datarow), (_, resultrow) in zip(
            test_df.iterrows(), pd.read_csv(result_path).astype(str).iterrows()
        ):
            # pred = extract_answer(resultrow['model_response'], datarow)
            pred = resultrow["model_output"]
            correct = 1 if pred == datarow["answer"] else 0
            score.append(correct)
        return score

    result = []
    score = []

    for _, row in tqdm(test_df.iterrows(), total=len(test_df)):
        question = format_example(row)

        response, _ = model.chat(
            tokenizer,
            question,
            history=None,
        )
        print(question)
        print(response)
        pred = extract_answer(response, row)
        print(pred)
        print("======================")

        if "answer" in row:
            correct = 1 if pred == row["answer"] else 0
            score.append(correct)
            if args.debug:
                print(f'{question} pred: {pred} ref: {row["answer"]}')
        result.append(pred)

    if save_result_dir:
        test_df["model_output"] = result
        test_df["model_response"] = response
        if score:
            test_df["correctness"] = score
        os.makedirs(save_result_dir, exist_ok=True)
        test_df.to_csv(
            os.path.join(save_result_dir, f"{subject_name}_result.csv"),
            encoding="utf-8",
            index=False,
        )

    return score


def cal_mmlu(res):
    acc_sum_dict = dict()
    acc_norm_sum_dict = dict()
    cnt_dict = dict()
    acc_sum = 0.0
    cnt = 0

    for class_ in TASK_NAME_MAPPING.keys():
        acc_sum_dict[class_] = 0.0
        acc_norm_sum_dict[class_] = 0.0
        cnt_dict[class_] = 0.0

        for tt in TASK_NAME_MAPPING[class_]:
            acc_sum += sum(res[tt])
            cnt += len(res[tt])

            acc_sum_dict[class_] += sum(res[tt])
            cnt_dict[class_] += len(res[tt])

    print("\n\n\n")
    for k in TASK_NAME_MAPPING.keys():
        if k in cnt_dict:
            print("%s ACC: %.2f " % (k, acc_sum_dict[k] * 100 / cnt_dict[k]))
    print("AVERAGE ACC:%.2f " % (acc_sum * 100 / cnt))


def main(args):
    print("loading model weights")
    if args.checkpoint_path is not None:
        model, tokenizer = load_models_tokenizer(args)
    else:
        model, tokenizer = None, None
    print("model loaded")

    dev_result = {}
    for subject_name in tqdm(SUBJECTS):
        # val_file_path = os.path.join(args.eval_data_path, 'val', f'{subject_name}_val.csv')
        # dev_file_path = os.path.join(args.eval_data_path, 'dev', f'{subject_name}_dev.csv')
        test_file_path = os.path.join(
            args.eval_data_path, "test", f"{subject_name}_test.csv"
        )
        # val_df = pd.read_csv(val_file_path, names=['question','A','B','C','D','answer'])
        # dev_df = pd.read_csv(dev_file_path, names=['question','A','B','C','D','answer'])
        test_df = pd.read_csv(
            test_file_path, names=["question", "A", "B", "C", "D", "answer"]
        ).astype(str)

        score = eval_subject(
            model,
            tokenizer,
            subject_name,
            test_df,
            save_result_dir=f"outs_chat/mmlu_eval_result",
            overwrite=args.overwrite,
        )
        dev_result[subject_name] = score
    cal_mmlu(dev_result)


TASK_NAME_MAPPING = {
    "stem": [
        "abstract_algebra",
        "anatomy",
        "astronomy",
        "college_biology",
        "college_chemistry",
        "college_computer_science",
        "college_mathematics",
        "college_physics",
        "computer_security",
        "conceptual_physics",
        "electrical_engineering",
        "elementary_mathematics",
        "high_school_biology",
        "high_school_chemistry",
        "high_school_computer_science",
        "high_school_mathematics",
        "high_school_physics",
        "high_school_statistics",
        "machine_learning",
    ],
    "Humanities": [
        "formal_logic",
        "high_school_european_history",
        "high_school_us_history",
        "high_school_world_history",
        "international_law",
        "jurisprudence",
        "logical_fallacies",
        "moral_disputes",
        "moral_scenarios",
        "philosophy",
        "prehistory",
        "professional_law",
        "world_religions",
    ],
    "other": [
        "business_ethics",
        "college_medicine",
        "human_aging",
        "management",
        "marketing",
        "medical_genetics",
        "miscellaneous",
        "nutrition",
        "professional_accounting",
        "professional_medicine",
        "virology",
        "global_facts",
        "clinical_knowledge",
    ],
    "social": [
        "econometrics",
        "high_school_geography",
        "high_school_government_and_politics",
        "high_school_macroeconomics",
        "high_school_microeconomics",
        "high_school_psychology",
        "human_sexuality",
        "professional_psychology",
        "public_relations",
        "security_studies",
        "sociology",
        "us_foreign_policy",
    ],
}
SUBJECTS = [v for vl in TASK_NAME_MAPPING.values() for v in vl]
choices = ["A", "B", "C", "D"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        help="Checkpoint path",
        default="Qwen/Qwen-7B-Chat",
    )
    parser.add_argument("-s", "--seed", type=int, default=1234, help="Random seed")

    # Provide extra arguments required for tasks
    group = parser.add_argument_group(title="Evaluation options")
    group.add_argument("-d", "--eval_data_path", type=str, help="Path to eval data")
    group.add_argument(
        "--debug", action="store_true", default=False, help="Print infos."
    )
    group.add_argument(
        "--overwrite",
        action="store_true",
        default=False,
        help="Overwrite existed results",
    )

    args = parser.parse_args()
    set_seed(args.seed)

    main(args)
```

## File: `eval/evaluate_cmmlu.py`
```python
import os
import pandas as pd
import numpy as np
import argparse
import datasets
import torch
from collections import defaultdict

from typing import List
from tqdm import tqdm
from transformers.trainer_utils import set_seed


"""
wget https://huggingface.co/datasets/haonan-li/cmmlu/resolve/main/cmmlu_v1_0_1.zip
mkdir data/cmmlu
mv cmmlu_v1_0_1.zip data/cmmlu
cd data/cmmlu; unzip cmmlu_v1_0_1.zip
cd ../../
python evaluate_cmmlu.py -d data/cmmlu/
"""


def load_models_tokenizer(args):
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from transformers.generation import GenerationConfig

    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path,
        pad_token='<|extra_0|>',
        eos_token='<|endoftext|>',
        padding_side='left',
        trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        pad_token_id=tokenizer.pad_token_id,
        device_map="auto",
        trust_remote_code=True
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path,
        pad_token_id=tokenizer.pad_token_id,
        trust_remote_code=True
    )
    return model, tokenizer


def format_example(line, include_answer=True):
    example = "问题：" + line["Question"]
    for choice in choices:
        example += f'\n{choice}. {line[f"{choice}"]}'

    if include_answer:
        example += "\n答案：" + line["Answer"] + "\n\n"
    else:
        example += "\n答案："
    return example


def generate_few_shot_prompt(k, subject, dev_df):
    prompt = ""
    if k == -1:
        k = dev_df.shape[0]
    for i in range(k):
        prompt += format_example(
            dev_df.iloc[i, :],
            include_answer=True,
        )
    return prompt


def get_logits(tokenizer, model, inputs: List[str]):
    input_ids = tokenizer(inputs, padding='longest')["input_ids"]
    input_ids = torch.tensor(input_ids, device=model.device)
    tokens = {"input_ids": input_ids}
    attention_mask = input_ids.ne(tokenizer.pad_token_id)

    outputs = model(input_ids, attention_mask=attention_mask)["logits"]
    logits = outputs[:, -1, :]
    log_probs = torch.nn.functional.softmax(logits, dim=-1)
    return log_probs, {"tokens": tokens}


@torch.no_grad()
def eval_subject(
    model,
    tokenizer,
    subject_name,
    test_df,
    k=5,
    dev_df=None,
    few_shot=False,
    save_result_dir=None,
    batch_size=1,
    **kwargs,
):
    result = []
    score = []

    few_shot_prompt = (
        generate_few_shot_prompt(k, subject_name, dev_df) if few_shot else []
    )
    all_probs = {"prob_A": [], "prob_B": [], "prob_C": [], "prob_D": []}
    if args.debug:
        print(f"few_shot_prompt: {few_shot_prompt}")

    choices_ids = torch.tensor(
        tokenizer("A")["input_ids"] + tokenizer("B")["input_ids"] +
        tokenizer("C")["input_ids"] + tokenizer("D")["input_ids"]
    ).unsqueeze(0).to(model.device)

    idx_list = list(range(0, len(test_df), batch_size))
    for i in tqdm(idx_list):
        full_prompt_list = []
        answer_list = []
        for row in test_df.iloc[i:i+batch_size].to_dict(orient='records'):
            question = format_example(row, include_answer=False)
            full_prompt = few_shot_prompt + question
            full_prompt_list.append(full_prompt)
            if 'Answer' in row:
                answer_list.append(row['Answer'])

        logits, input_info = get_logits(tokenizer, model, full_prompt_list)
        softval = logits.gather(1, choices_ids.expand(logits.size(0), -1)).softmax(1)
        if softval.dtype in {torch.bfloat16, torch.float16}:
            softval = softval.to(dtype=torch.float32)
        probs = softval.detach().cpu().numpy()

        for i in range(len(probs)):
            for j, choice in enumerate(choices):
                all_probs[f"prob_{choice}"].append(probs[i][j])
            pred = {0: "A", 1: "B", 2: "C", 3: "D"}[np.argmax(probs[i])]

            if answer_list != []:
                correct = 1 if pred == answer_list[i] else 0
                score.append(correct)
                if args.debug:
                    print(f'{question} pred: {pred} ref: {answer_list[i]}')
            result.append(pred)

    if score:
        correct_ratio = 100 * sum(score) / len(score)
        if args.debug:
            print(subject_name, correct_ratio)
    else:
        correct_ratio = 0
    if save_result_dir:
        test_df["model_output"] = result
        for i, choice in enumerate(choices):
            test_df[f"prob_{choice}"] = all_probs[f"prob_{choice}"]
        if score:
            test_df["correctness"] = score
        os.makedirs(save_result_dir, exist_ok=True)
        test_df.to_csv(
            os.path.join(save_result_dir, f"{subject_name}_result.csv"),
            encoding="utf-8",
            index=False,
        )

    return correct_ratio


def cal_cmmlu(res):
    print("\n\n\n")
    res = {k.split("-")[-1]: float(v) for k, v in res.items()}
    for k, v in TASK_NAME_MAPPING.items():
        avg_acc = np.mean(list(map(lambda x: res[x], v)))
        print(f"{k} acc: {avg_acc:.2f}")
    avg_all_acc = np.mean(list(res.values()))
    print(f"AVERAGE acc: {avg_all_acc:.2f}")


subcategories = {
    "agronomy": ["other"],
    "anatomy": ["biology"],
    "ancient_chinese": ["linguistics", "china specific"],
    "arts": ["arts"],
    "astronomy": ["physics"],
    "business_ethics": ["business"],
    "chinese_civil_service_exam": ["politics", "china specific"],
    "chinese_driving_rule": ["other", "china specific"],
    "chinese_food_culture": ["culture", "china specific"],
    "chinese_foreign_policy": ["politics", "china specific"],
    "chinese_history": ["history", "china specific"],
    "chinese_literature": ["literature", "china specific"],
    "chinese_teacher_qualification": ["education", "china specific"],
    "college_actuarial_science": ["math"],
    "college_education": ["education"],
    "college_engineering_hydrology": ["engineering"],
    "college_law": ["law"],
    "college_mathematics": ["math"],
    "college_medical_statistics": ["statistics"],
    "clinical_knowledge": ["other"],
    "college_medicine": ["other"],
    "computer_science": ["computer science"],
    "computer_security": ["other"],
    "conceptual_physics": ["physics"],
    "construction_project_management": ["other", "china specific"],
    "economics": ["economics"],
    "education": ["education"],
    "elementary_chinese": ["linguistics", "china specific"],
    "elementary_commonsense": ["other", "china specific"],
    "elementary_information_and_technology": ["other"],
    "electrical_engineering": ["engineering"],
    "elementary_mathematics": ["math"],
    "ethnology": ["culture", "china specific"],
    "food_science": ["other"],
    "genetics": ["biology"],
    "global_facts": ["global"],
    "high_school_biology": ["biology"],
    "high_school_chemistry": ["chemistry"],
    "high_school_geography": ["geography"],
    "high_school_mathematics": ["math"],
    "high_school_physics": ["physics"],
    "high_school_politics": ["politics", "china specific"],
    "human_sexuality": ["other"],
    "international_law": ["law"],
    "journalism": ["sociology"],
    "jurisprudence": ["law"],
    "legal_and_moral_basis": ["other"],
    "logical": ["philosophy"],
    "machine_learning": ["computer science"],
    "management": ["business"],
    "marketing": ["business"],
    "marxist_theory": ["philosophy"],
    "modern_chinese": ["linguistics", "china specific"],
    "nutrition": ["other"],
    "philosophy": ["philosophy"],
    "professional_accounting": ["business"],
    "professional_law": ["law"],
    "professional_medicine": ["other"],
    "professional_psychology": ["psychology"],
    "public_relations": ["politics"],
    "security_study": ["politics"],
    "sociology": ["culture"],
    "sports_science": ["other"],
    "traditional_chinese_medicine": ["other", "china specific"],
    "virology": ["biology"],
    "world_history": ["history"],
    "world_religions": ["global"],
}

categories = {
    "STEM": [
        "physics",
        "chemistry",
        "biology",
        "computer science",
        "math",
        "engineering",
        "statistics",
    ],
    "Humanities": ["history", "philosophy", "law", "arts", "literature", "global"],
    "Social Science": [
        "linguistics",
        "business",
        "politics",
        "culture",
        "economics",
        "geography",
        "psychology",
        "education",
        "sociology",
    ],
    "Other": ["other"],
    "China specific": ["china specific"],
}

TASK_NAME_MAPPING = defaultdict(list)
for k, v in categories.items():
    for subject, subcat in subcategories.items():
        for c in subcat:
            if c in v:
                TASK_NAME_MAPPING[k].append(subject)


choices = ["A", "B", "C", "D"]


def main(args):
    model, tokenizer = load_models_tokenizer(args)

    test_result = {}
    for subject_name in tqdm(subcategories.keys()):
        dev_file_path = os.path.join(args.eval_data_path, "dev", f"{subject_name}.csv")
        test_file_path = os.path.join(
            args.eval_data_path, "test", f"{subject_name}.csv"
        )
        dev_df = pd.read_csv(dev_file_path)
        test_df = pd.read_csv(test_file_path)

        score = eval_subject(
            model,
            tokenizer,
            subject_name,
            dev_df=dev_df,
            test_df=test_df,
            k=5,
            few_shot=True,
            save_result_dir=f"outs/cmmlu_eval_result",
            batch_size=args.batch_size
        )
        test_result[subject_name] = score
    cal_cmmlu(test_result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        help="Checkpoint path",
        default="Qwen/Qwen-7B",
    )
    parser.add_argument("-s", "--seed", type=int, default=1234, help="Random seed")

    """Provide extra arguments required for tasks."""
    group = parser.add_argument_group(title="Evaluation options")
    group.add_argument(
        "-d", "--eval_data_path", type=str, required=True, help="Path to eval data"
    )
    group.add_argument(
        "--max-seq-len",
        type=int,
        default=2048,
        help="Size of the output generated text.",
    )
    group.add_argument(
        "--debug", action="store_true", default=False, help="Print infos."
    )
    group.add_argument(
        "--batch-size",
        type=int,
        default=1,
        help="batch size",
    )

    args = parser.parse_args()
    set_seed(args.seed)

    main(args)
```

## File: `eval/evaluate_gsm8k.py`
```python
import re
import torch
import argparse
import jsonlines
import numpy as np
import datasets
from datasets import load_from_disk, load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig


ANS_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
INVALID_ANS = "[invalid]"


def doc_to_text(doc):
    return (
        fewshot_prompt
        + "\nQuestion: "
        + doc["question"]
        + "\nLet's think step by step\n"
    )


def decode(tokens_list, tokenizer, raw_text_len):
    sents = []
    # print(len(tokens_list))
    for tokens in tokens_list:
        tokens = tokens.cpu().numpy().tolist()
        sent = tokenizer.tokenizer.decode(tokens[raw_text_len:])
        sent = sent.split("<|endoftext|>")[0]
        sent = sent.split("\n\n\n")[0]
        sent = sent.split("\n\n")[0]
        sent = sent.split("Question:")[0]
        sents.append(sent)
    return sents


def generate_sample(model, tokenizer, input_txt):
    input_ids = tokenizer.tokenizer.encode(input_txt)
    raw_text_len = len(input_ids)
    context_enc = torch.tensor([input_ids]).to(model.device)
    print(f"Input text: {input_txt}\n")
    outputs = model.generate(context_enc)
    output_text = decode(outputs, tokenizer, raw_text_len)[0]
    print(f"\nOutput text: {output_text}\n")
    return output_text


def extract_answer_hf(completion):
    match = ANS_RE.search(completion)
    if match:
        match_str = match.group(1).strip()
        match_str = match_str.replace(",", "")
        return eval(match_str)
    else:
        return INVALID_ANS


def extract_answer(completion):
    try:
        last_number = re.findall(r"\d+", completion)[-1]
        return eval(last_number)
    except:
        return INVALID_ANS


def is_correct(completion, answer):
    gold = extract_answer_hf(answer)
    assert gold != INVALID_ANS, "No ground truth answer found in the document."
    return extract_answer(completion) == gold


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        help="Checkpoint path",
        default="Qwen/Qwen-7B",
    )
    parser.add_argument("-f", "--sample-input-file", type=str, default=None)
    parser.add_argument(
        "-o", "--sample-output-file", type=str, default="gsm8k_res.jsonl"
    )

    args = parser.parse_args()

    fewshot_prompt = open("gsm8k_prompt.txt").read()
    if args.sample_input_file is not None:
        dataset = load_from_disk(args.sample_input_file)
    else:
        config = datasets.DownloadConfig(resume_download=True, max_retries=100)
        dataset = load_dataset("gsm8k", "main", download_config=config)

    test = dataset["test"]

    print("Loading tokenizer ...")
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )

    print("Loading model ...")
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path, device_map="auto", trust_remote_code=True
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model.generation_config.do_sample = False

    f_output = jsonlines.Writer(open(args.sample_output_file, "w", encoding="utf-8"))
    tot_length = test.num_rows
    acc_res = []
    for doc in test:
        context = doc_to_text(doc)
        completion = generate_sample(model, tokenizer, context)
        answer = doc["answer"]
        acc = is_correct(completion, answer)
        doc["completion"] = completion
        doc["acc"] = acc
        f_output.write(doc)
        acc_res.append(acc)

    f_output.close()
    print("Acc: ", np.mean(acc_res))
```

## File: `eval/evaluate_humaneval.py`
```python
import argparse
import tqdm
import torch
import jsonlines
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

"""
git clone https://github.com/openai/human-eval
$ pip install -e human-eval
evaluate_functional_correctness sample-output-file
"""


def decode(tokens_list, tokenizer, raw_text_len):
    sents = []
    # print(len(tokens_list))
    for tokens in tokens_list:
        tokens = tokens.cpu().numpy().tolist()
        sent = tokenizer.tokenizer.decode(tokens[raw_text_len:])
        sent = sent.split("<|endoftext|>")[0]
        sent = sent.split("\n\n\n")[0]
        sent = sent.split("\n\n")[0]
        sent = sent.split("def ")[0]
        sents.append(sent)
    return sents


def generate_sample(model, tokenizer, input_txt):
    input_ids = tokenizer.tokenizer.encode(input_txt)
    raw_text_len = len(input_ids)
    context_enc = torch.tensor([input_ids]).to(model.device)
    print(f"Input text: {input_txt}\n")
    outputs = model.generate(context_enc)
    output_text = decode(outputs, tokenizer, raw_text_len)[0]
    print(f"\nOutput text: \n{output_text}\n")
    return output_text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        help="Checkpoint path",
        default="Qwen/Qwen-7B",
    )
    parser.add_argument(
        "-f",
        "--sample-input-file",
        type=str,
        default=None,
        help="data path to HumanEval.jsonl",
    )
    parser.add_argument(
        "-o", "--sample-output-file", type=str, default="HumanEval_res.jsonl"
    )

    args = parser.parse_args()
    print("Loading tokenizer ...")
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )

    print("Loading model ...")
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path, device_map="auto", trust_remote_code=True
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model.generation_config.do_sample = False

    f_output = jsonlines.Writer(open(args.sample_output_file, "w", encoding="utf-8"))

    f = jsonlines.open(args.sample_input_file)
    with f_output as output:
        for jobj in tqdm.tqdm(f, desc="task_idx"):
            prompt = jobj["prompt"]
            task_id = jobj["task_id"]
            gen_sents = generate_sample(model, tokenizer, prompt)
            gen_jobjs = {"task_id": task_id, "completion": gen_sents}
            output.write(gen_jobjs)
    f_output.close()
```

## File: `eval/evaluate_mmlu.py`
```python
import os
from typing import List
import pandas as pd
import numpy as np
import argparse
import torch
from tqdm import tqdm
from transformers.trainer_utils import set_seed
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

"""
wget https://people.eecs.berkeley.edu/~hendrycks/data.tar
mkdir data/mmlu
mv data.tar data/mmlu
cd data/mmlu; tar xf data.tar
cd ../../
python eval/evaluate_mmlu.py -d data/mmlu/data/
"""


def load_models_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path,
        pad_token='<|extra_0|>',
        eos_token='<|endoftext|>',
        padding_side='left',
        trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        pad_token_id=tokenizer.pad_token_id,
        device_map="auto",
        trust_remote_code=True
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path,
        pad_token_id=tokenizer.pad_token_id,
        trust_remote_code=True
    )
    return model, tokenizer


def format_example(line, include_answer=True):
    example = "Question: " + line["question"]
    for choice in choices:
        example += f'\n{choice}. {line[f"{choice}"]}'

    if include_answer:
        example += "\nAnswer: " + line["answer"] + "\n\n"
    else:
        example += "\nAnswer:"
    return example


def generate_few_shot_prompt(k, subject, dev_df):
    def format_subject(subject):
        l = subject.split("_")
        s = ""
        for entry in l:
            s += " " + entry
        return s.strip()

    prompt = "The following are multiple choice questions (with answers) about {}.\n\n".format(
        format_subject(subject)
    )

    if k == -1:
        k = dev_df.shape[0]
    for i in range(k):
        prompt += format_example(
            dev_df.iloc[i, :],
            include_answer=True,
        )
    return prompt


def get_logits(tokenizer, model, inputs: List[str]):
    input_ids = tokenizer(inputs, padding='longest')["input_ids"]
    input_ids = torch.tensor(input_ids, device=model.device)

    if input_ids.shape[1] > args.max_seq_len:
        input_ids = input_ids[:, input_ids.shape[1] - args.max_seq_len + 1 :]
    tokens = {"input_ids": input_ids}
    attention_mask = input_ids.ne(tokenizer.pad_token_id)

    outputs = model(input_ids, attention_mask=attention_mask)["logits"]
    logits = outputs[:, -1, :]
    log_probs = torch.nn.functional.softmax(logits, dim=-1)
    return log_probs, {"tokens": tokens}


@torch.no_grad()
def eval_subject(
    model,
    tokenizer,
    subject_name,
    test_df,
    k=5,
    dev_df=None,
    few_shot=False,
    save_result_dir=None,
    batch_size=1,
    **kwargs,
):
    result = []
    score = []

    few_shot_prompt = (
        generate_few_shot_prompt(k, subject_name, dev_df) if few_shot else []
    )
    all_probs = {"prob_A": [], "prob_B": [], "prob_C": [], "prob_D": []}
    if args.debug:
        print(f"few_shot_prompt: {few_shot_prompt}")

    choices_ids = torch.tensor(
        tokenizer(" A")["input_ids"] + tokenizer(" B")["input_ids"] +
        tokenizer(" C")["input_ids"] + tokenizer(" D")["input_ids"]
    ).unsqueeze(0).to(model.device)

    idx_list = list(range(0, len(test_df), batch_size))
    for i in tqdm(idx_list):
        full_prompt_list = []
        answer_list = []
        for row in test_df.iloc[i:i+batch_size].to_dict(orient='records'):
            question = format_example(row, include_answer=False)
            full_prompt = few_shot_prompt + question
            full_prompt_list.append(full_prompt)
            if 'answer' in row:
                answer_list.append(row['answer'])

        logits, input_info = get_logits(tokenizer, model, full_prompt_list)
        softval = logits.gather(1, choices_ids.expand(logits.size(0), -1)).softmax(1)
        if softval.dtype in {torch.bfloat16, torch.float16}:
            softval = softval.to(dtype=torch.float32)
        probs = softval.detach().cpu().numpy()

        for i in range(len(probs)):
            for j, choice in enumerate(choices):
                all_probs[f"prob_{choice}"].append(probs[i][j])
            pred = {0: "A", 1: "B", 2: "C", 3: "D"}[np.argmax(probs[i])]

            if answer_list != []:
                correct = 1 if pred == answer_list[i] else 0
                score.append(correct)
                if args.debug:
                    print(f'{question} pred: {pred} ref: {answer_list[i]}')
            result.append(pred)

    if save_result_dir:
        test_df["model_output"] = result
        for i, choice in enumerate(choices):
            test_df[f"prob_{choice}"] = all_probs[f"prob_{choice}"]
        if score:
            test_df["correctness"] = score
        os.makedirs(save_result_dir, exist_ok=True)
        test_df.to_csv(
            os.path.join(save_result_dir, f"{subject_name}_result.csv"),
            encoding="utf-8",
            index=False,
        )

    return score


def cal_mmlu(res):
    acc_sum_dict = dict()
    acc_norm_sum_dict = dict()
    cnt_dict = dict()
    acc_sum = 0.0
    cnt = 0
    hard_cnt = 0
    hard_acc_sum = 0.0

    for class_ in TASK_NAME_MAPPING.keys():
        acc_sum_dict[class_] = 0.0
        acc_norm_sum_dict[class_] = 0.0
        cnt_dict[class_] = 0.0

        for tt in TASK_NAME_MAPPING[class_]:
            acc_sum += sum(res[tt])
            cnt += len(res[tt])

            acc_sum_dict[class_] += sum(res[tt])
            cnt_dict[class_] += len(res[tt])

    print("\n\n\n", "total cnt:", cnt, "\n")
    for k in TASK_NAME_MAPPING.keys():
        if k in cnt_dict:
            print("%s ACC: %.2f " % (k, acc_sum_dict[k] / cnt_dict[k] * 100))
    print("AVERAGE ACC:%.2f " % (acc_sum / cnt * 100))


def main(args):
    model, tokenizer = load_models_tokenizer(args)

    dev_result = {}
    for subject_name in tqdm(SUBJECTS):
        # val_file_path = os.path.join(args.eval_data_path, 'val', f'{subject_name}_val.csv')
        dev_file_path = os.path.join(
            args.eval_data_path, "dev", f"{subject_name}_dev.csv"
        )
        test_file_path = os.path.join(
            args.eval_data_path, "test", f"{subject_name}_test.csv"
        )
        # val_df = pd.read_csv(val_file_path, names=['question','A','B','C','D','answer'])
        dev_df = pd.read_csv(
            dev_file_path, names=["question", "A", "B", "C", "D", "answer"]
        )
        test_df = pd.read_csv(
            test_file_path, names=["question", "A", "B", "C", "D", "answer"]
        )

        score = eval_subject(
            model,
            tokenizer,
            subject_name,
            test_df,
            dev_df=dev_df,
            k=5,
            few_shot=True,
            save_result_dir=f"outs/mmlu_eval_result",
            batch_size=args.batch_size
        )
        dev_result[subject_name] = score
    cal_mmlu(dev_result)


TASK_NAME_MAPPING = {
    "stem": [
        "abstract_algebra",
        "anatomy",
        "astronomy",
        "college_biology",
        "college_chemistry",
        "college_computer_science",
        "college_mathematics",
        "college_physics",
        "computer_security",
        "conceptual_physics",
        "electrical_engineering",
        "elementary_mathematics",
        "high_school_biology",
        "high_school_chemistry",
        "high_school_computer_science",
        "high_school_mathematics",
        "high_school_physics",
        "high_school_statistics",
        "machine_learning",
    ],
    "Humanities": [
        "formal_logic",
        "high_school_european_history",
        "high_school_us_history",
        "high_school_world_history",
        "international_law",
        "jurisprudence",
        "logical_fallacies",
        "moral_disputes",
        "moral_scenarios",
        "philosophy",
        "prehistory",
        "professional_law",
        "world_religions",
    ],
    "other": [
        "business_ethics",
        "college_medicine",
        "human_aging",
        "management",
        "marketing",
        "medical_genetics",
        "miscellaneous",
        "nutrition",
        "professional_accounting",
        "professional_medicine",
        "virology",
        "global_facts",
        "clinical_knowledge",
    ],
    "social": [
        "econometrics",
        "high_school_geography",
        "high_school_government_and_politics",
        "high_school_macroeconomics",
        "high_school_microeconomics",
        "high_school_psychology",
        "human_sexuality",
        "professional_psychology",
        "public_relations",
        "security_studies",
        "sociology",
        "us_foreign_policy",
    ],
}
SUBJECTS = [v for vl in TASK_NAME_MAPPING.values() for v in vl]
choices = ["A", "B", "C", "D"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        help="Checkpoint path",
        default="Qwen/Qwen-7B",
    )
    parser.add_argument("-s", "--seed", type=int, default=1234, help="Random seed")
    parser.add_argument("--gpu", type=int, default=0, help="gpu id")

    """Provide extra arguments required for tasks."""
    group = parser.add_argument_group(title="Evaluation options")
    group.add_argument("-d", "--eval_data_path", type=str, help="Path to eval data")
    group.add_argument(
        "--max-seq-len",
        type=int,
        default=2048,
        help="Size of the output generated text.",
    )
    group.add_argument(
        "--debug", action="store_true", default=False, help="Print infos."
    )
    group.add_argument(
        "--batch-size",
        type=int,
        default=1,
        help="batch size",
    )

    args = parser.parse_args()
    set_seed(args.seed)

    main(args)
```

## File: `eval/evaluate_plugin.py`
```python
import argparse
import json
import os
import pprint

import json5
import jsonlines
from rouge_score import rouge_scorer
from tqdm import tqdm
from transformers import Agent, AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
from transformers.tools.evaluate_agent import evaluate_agent
from transformers.trainer_utils import set_seed

data_root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def is_callable(response, golden):
    return response["action"].strip().lower() == golden["action"].strip().lower()


def process_res(response):
    # parse response
    response += "\n"  # fix not-find bug
    thought = response[: response.find("Action:")].strip()
    action = response[
        response.find("Action:") + len("Action:") : response.find("Action Input:")
    ].strip()
    action_input = response[
        response.find("Action Input:")
        + len("Action Input:") : response.find("Observation:")
    ].strip()
    # TODO: This parsing result is incorrect if the response contains multiple Actions. To be fixed in the future.
    observation = response[
        response.find("Observation:") + len("Observation:") : response.rfind("Thought:")
    ].strip()
    thought_last = response[
        response.rfind("Thought:") + len("Thought:") : response.find("Final Answer:")
    ].strip()
    final_answer = response[
        response.find("Final Answer:") + len("Final Answer:") :
    ].strip()
    try:
        action_input = json.dumps(
            json5.loads(action_input), ensure_ascii=False, sort_keys=True
        )
    except:
        # print("JSON Load Error:", action_input)
        action_input = ""
    res_dict = {
        "thought": thought,
        "action": action,
        "action_input": action_input,
        "observation": observation,
        "thought_last": thought_last,
        "final_answer": final_answer,
    }
    return res_dict


class _DummyTokenizer:
    def tokenize(self, text: str):
        return text.split()


def _get_tokenized_string(tokenizer, text_list):
    token_ids_list, tokenized_string_list = [], []
    for text in text_list:
        assert tokenizer is not None
        token_ids = tokenizer.encode(text)
        tokens_bytes = tokenizer.convert_ids_to_tokens(token_ids)
        tokens = [token.decode("utf-8", errors="replace") for token in tokens_bytes]
        tokenized_string = " ".join(tokens)
        token_ids_list.append(token_ids)
        tokenized_string_list.append(tokenized_string)
    return token_ids_list, tokenized_string_list


def eval_action(job):
    response = job["gen"][0]
    golden = job["response"]

    if "\nAction: " in response:
        response, golden = process_res(response), process_res(golden)
        if is_callable(response, golden):
            return True
    return False


def eval_action_input(job, tokenizer):
    response = job["gen"][0]
    golden = job["response"]
    response, golden = process_res(response), process_res(golden)
    query = job["prompt"]

    job = {}
    job["prompt"] = query
    job["gen"] = response["action_input"]
    job["response"] = golden["action_input"]

    job["_gen_tok"], job["_gen_tok_str"] = _get_tokenized_string(
        tokenizer, [response["action_input"]]
    )
    job["_reference_tok"], job["_reference_tok_str"] = _get_tokenized_string(
        tokenizer, [golden["action_input"]]
    )

    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"], tokenizer=_DummyTokenizer()
    )
    score = scorer.score(job["_reference_tok_str"][0], job["_gen_tok_str"][0])

    rouge = score["rougeL"].fmeasure

    return rouge


class QWenAgent(Agent):
    """
    Agent that uses QWen model and tokenizer to generate code.

    Example:

    ```py
    agent = QWenAgent()
    agent.run("Draw me a picture of rivers and lakes.")
    ```
    """

    def __init__(
        self,
        chat_prompt_template=None,
        run_prompt_template=None,
        additional_tools=None,
        tokenizer=None,
        model=None,
    ):
        if tokenizer and model:
            self.tokenizer = tokenizer
            self.model = model
        else:
            checkpoint = "Qwen/Qwen-7B-Chat"
            self.tokenizer = AutoTokenizer.from_pretrained(
                checkpoint, trust_remote_code=True
            )
            self.model = (
                AutoModelForCausalLM.from_pretrained(
                    checkpoint, device_map="auto", trust_remote_code=True
                )
                .cuda()
                .eval()
            )
            self.model.generation_config = GenerationConfig.from_pretrained(
                checkpoint, trust_remote_code=True
            )  # 可指定不同的生成长度、top_p等相关超参
            self.model.generation_config.do_sample = False  # greedy

        super().__init__(
            chat_prompt_template=chat_prompt_template,
            run_prompt_template=run_prompt_template,
            additional_tools=additional_tools,
        )

    def generate_one(self, prompt, stop):
        # "Human:" 和 "Assistant:" 曾为通义千问的特殊保留字，需要替换为 "_HUMAN_:" 和 "_ASSISTANT_:"。这一问题将在未来版本修复。
        prompt = prompt.replace("Human:", "_HUMAN_:").replace(
            "Assistant:", "_ASSISTANT_:"
        )
        stop = [
            item.replace("Human:", "_HUMAN_:").replace("Assistant:", "_ASSISTANT_:")
            for item in stop
        ]

        result, _ = self.model.chat(self.tokenizer, prompt, history=None)
        for stop_seq in stop:
            if result.endswith(stop_seq):
                result = result[: -len(stop_seq)]

        result = result.replace("_HUMAN_:", "Human:").replace(
            "_ASSISTANT_:", "Assistant:"
        )
        return result


def load_models_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        device_map="auto",
        trust_remote_code=True,
        bf16=True,
        use_flash_attn=True,
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        args.checkpoint_path, trust_remote_code=True
    )
    model.generation_config.do_sample = False  # use greedy decoding
    return model, tokenizer


def load_jobs(filename):
    jobs = []
    with jsonlines.open(os.path.join(data_root_path, filename), mode="r") as reader:
        for job in reader:
            jobs.append(job)
    return jobs


def react_inference(filename, model, tokenizer):
    filename_cache = filename + ".cache"
    if os.path.exists(os.path.join(data_root_path, filename_cache)):
        jobs = load_jobs(filename=filename_cache)
        print("Loaded from", filename_cache)
    else:
        with open(os.path.join(data_root_path, filename_cache), "w") as f:
            jobs = load_jobs(filename=filename)
            print("Inference:", filename)
            for job in tqdm(jobs):
                response, history = model.chat(tokenizer, job["prompt"], history=None)
                job["gen"] = [response]
                f.writelines(json.dumps(job, ensure_ascii=False) + "\n")
        print(filename_cache, "is saved.")
    return jobs


def main(args):
    print("loading model weights")
    if args.checkpoint_path is not None:
        model, tokenizer = load_models_tokenizer(args)
    else:
        model, tokenizer = None, None
    print("model loaded")

    result = {}
    # eval react positive
    if args.eval_react_positive:
        print("eval react positive ...")
        acc_count = 0
        rouge_mean = 0
        jobs = react_inference(
            filename=args.eval_react_positive_filename, model=model, tokenizer=tokenizer
        )
        for job in jobs:
            if eval_action(job):
                acc_count += 1
            rouge = eval_action_input(job, tokenizer)
            rouge_mean += rouge / len(jobs)

        scores = {
            "action_right_rate": acc_count / len(jobs),
            "action_input_rouge": rouge_mean,
        }

        result.update({"react_positive": scores})

    # eval react negative
    if args.eval_react_negative:
        print("eval react negative ...")
        bad_count = 0
        jobs = react_inference(
            filename=args.eval_react_negative_filename, model=model, tokenizer=tokenizer
        )
        for job in jobs:
            if "\nAction: " in job["gen"][0]:
                bad_count += 1
        scores = {"bad_rate": bad_count / len(jobs)}
        result.update({"react_negative": scores})

    # eval hfagent
    if args.eval_hfagent:
        print("eval hfagent ...")
        agent = QWenAgent(model=model, tokenizer=tokenizer)
        scores = evaluate_agent(agent, verbose=False, return_errors=False)
        result.update({"hfagent": scores})

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test HF checkpoint.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        help="Checkpoint path",
        default="Qwen/Qwen-7B-Chat",
    )
    parser.add_argument("-s", "--seed", type=int, default=1234, help="Random seed")
    """Provide extra arguments required for tasks."""
    group = parser.add_argument_group(title="Evaluation options")
    group.add_argument(
        "--eval-react-positive",
        action="store_true",
        default=False,
        help="Eval react positive.",
    )
    group.add_argument(
        "--eval-react-positive-filename",
        type=str,
        default="exam_plugin_v20231206_react_positive.jsonl",
        help="Eval react positive filename.",
    )
    group.add_argument(
        "--eval-react-negative",
        action="store_true",
        default=False,
        help="Eval react negative.",
    )
    group.add_argument(
        "--eval-react-negative-filename",
        type=str,
        default="exam_plugin_v20231206_react_negative.jsonl",
        help="Eval react negative filename.",
    )
    group.add_argument(
        "--eval-hfagent", action="store_true", default=False, help="Eval hfagent."
    )

    args = parser.parse_args()
    set_seed(args.seed)

    main(args)
```

## File: `eval/EVALUATION.md`
```markdown
## 评测复现

- CEVAL

```Shell
wget https://huggingface.co/datasets/ceval/ceval-exam/resolve/main/ceval-exam.zip
mkdir data/ceval
mv ceval-exam.zip data/ceval
cd data/ceval; unzip ceval-exam.zip
cd ../../

# Qwen-7B
python evaluate_ceval.py -d data/ceval/

# Qwen-7B-Chat (We only provide 0-shot reproduction scripts. 5-shot results are obtained by OpenCompass (https://github.com/InternLM/opencompass).)
pip install thefuzz
python evaluate_chat_ceval.py -d data/ceval/
```

- MMLU

```Shell
wget https://people.eecs.berkeley.edu/~hendrycks/data.tar
mkdir data/mmlu
mv data.tar data/mmlu
cd data/mmlu; tar xf data.tar
cd ../../

# Qwen-7B
python evaluate_mmlu.py -d data/mmlu/data/

# Qwen-7B-Chat (We only provide 0-shot reproduction scripts. 5-shot results are obtained by OpenCompass (https://github.com/InternLM/opencompass).)
pip install thefuzz
python evaluate_chat_mmlu.py -d data/mmlu/data/
```

- CMMLU

```Shell
wget https://huggingface.co/datasets/haonan-li/cmmlu/resolve/main/cmmlu_v1_0_1.zip
mkdir data/cmmlu
mv cmmlu_v1_0_1.zip data/cmmlu
cd data/cmmlu; unzip cmmlu_v1_0_1.zip
cd ../../

# Qwen-7B
python evaluate_cmmlu.py -d data/cmmlu/
```

- HumanEval

Get the HumanEval.jsonl file from [here](https://github.com/openai/human-eval/tree/master/data)

```Shell
git clone https://github.com/openai/human-eval
pip install -e human-eval

# Qwen-7B
python evaluate_humaneval.py -f HumanEval.jsonl -o HumanEval_res.jsonl
evaluate_functional_correctness HumanEval_res.jsonl
# Qwen-7B-Chat
python evaluate_chat_humaneval.py -f HumanEval.jsonl -o HumanEval_res_chat.jsonl
evaluate_functional_correctness HumanEval_res_chat.jsonl
```

When installing package human-eval, please note its following disclaimer:

This program exists to run untrusted model-generated code. Users are strongly encouraged not to do so outside of a robust security sandbox. The execution call in execution.py is deliberately commented out to ensure users read this disclaimer before running code in a potentially unsafe manner. See the comment in execution.py for more information and instructions.

- GSM8K

```Shell
# Qwen-7B
python evaluate_gsm8k.py

# Qwen-7B-Chat (We only provide 0-shot reproduction scripts. 5-shot results are obtained by OpenCompass (https://github.com/InternLM/opencompass).)
python evaluate_chat_gsm8k.py # zeroshot
```

- PLUGIN

This script is used to reproduce the results of the ReAct and Hugging Face Agent in the Tool Usage section of the README document.

```Shell
# Qwen-7B-Chat
mkdir data;
cd data;
## Old Evaluation Dataset (Version 20230803)
# wget https://qianwen-res.oss-cn-beijing.aliyuncs.com/opensource_data/exam_plugin_v1/exam_plugin_v1_react_positive.jsonl;
# wget https://qianwen-res.oss-cn-beijing.aliyuncs.com/opensource_data/exam_plugin_v1/exam_plugin_v1_react_negative.jsonl;
## New Evaluation Dataset (Version 20231206)
wget https://qianwen-res.oss-cn-beijing.aliyuncs.com/opensource_data/exam_plugin_v20231206/exam_plugin_v20231206_react_positive.jsonl;
wget https://qianwen-res.oss-cn-beijing.aliyuncs.com/opensource_data/exam_plugin_v20231206/exam_plugin_v20231206_react_negative.jsonl;cd ..;
pip install json5;
pip install jsonlines;
pip install rouge_score;
python evaluate_plugin.py --eval-react-positive --eval-react-negative --eval-hfagent
```
```

## File: `eval/gsm8k_prompt.txt`
```
Question: In 2004, there were 60 kids at a cookout. In 2005, half the number of kids came to the cookout as compared to 2004. In 2006, 2/3 as many kids came to the cookout as in 2005. How many kids came to the cookout in 2006?
Let's think step by step
In 2005, 60/2=30 kids came to the cookout.
In 2006, 30/3*2=20 kids came to the cookout.
The answer is 20

Question: Zilla spent 7% of her monthly earnings on rent, half of it on her other monthly expenses, and put the rest in her savings. If she spent $133 on her rent, how much does she deposit into her savings account in a month?
Let's think step by step
Since $133 is equal to 7% of her earnings, then 1% is equal to $133/7 = $19.
The total monthly earning of Zilla is represented by 100%, so $19 x 100 = $1900 is her monthly earnings.
So, $1900/2 = $950 is spent on her other monthly expenses.
The total amount spent on the rent and other monthly expenses is $133 + $950 = $1083.
Hence, she saves $1900 - $1083 = $817 per month.
The answer is 817

Question: If Buzz bought a pizza with 78 slices at a restaurant and then decided to share it with the waiter in the ratio of 5:8, with Buzz's ratio being 5, what's twenty less the number of slices of pizza that the waiter ate?
Let's think step by step
The total ratio representing the slices of pizza that Buzz bought is 5+8=13
If he shared the slices of pizza with the waiter, the waiter received a fraction of 8/13 of the total number of slices, which totals 8/13 * 78 = 48 slices
Twenty less the number of slices of pizza that the waiter ate is 48-20 = 28
The answer is 28

Question: Jame gets a raise to $20 per hour and works 40 hours a week.  His old job was $16 an hour for 25 hours per week.  How much more money does he make per year in his new job than the old job if he works 52 weeks a year?
Let's think step by step
He makes 20*40=$800 per week
He used to make 16*25=$400 per week
So his raise was 800-400=$400 per week
So he makes 400*52=$20,800 per year more
The answer is 20800

Question: Mr. Gardner bakes 20 cookies, 25 cupcakes, and 35 brownies for his second-grade class of 20 students. If he wants to give each student an equal amount of sweet treats, how many sweet treats will each student receive?
Let's think step by step
Mr. Gardner bakes a total of 20 + 25 + 35 = 80 sweet treats
Each student will receive 80 / 20 = 4 sweet treats
The answer is 4

Question: A used car lot has 24 cars and motorcycles (in total) for sale. A third of the vehicles are motorcycles, and a quarter of the cars have a spare tire included. How many tires are on the used car lot’s vehicles in all?
Let's think step by step
The used car lot has 24 / 3 = 8 motorcycles with 2 tires each.
The lot has 24 - 8 = 16 cars for sale
There are 16 / 4 = 4 cars with a spare tire with 5 tires each.
The lot has 16 - 4 = 12 cars with 4 tires each.
Thus, the used car lot’s vehicles have 8 * 2 + 4 * 5 + 12 * 4 = 16 + 20 + 48 = 84 tires in all.
The answer is 84

Question: Norma takes her clothes to the laundry. She leaves 9 T-shirts and twice as many sweaters as T-shirts in the washer. When she returns she finds 3 sweaters and triple the number of T-shirts. How many items are missing?
Let's think step by step
Norma left 9 T-shirts And twice as many sweaters, she took 9 * 2= 18 sweaters
Adding the T-shirts and sweaters, Norma left 9 + 18 = 27 clothes
When she came back, she found 3 sweaters And triple the number of T-shirts, she found 3 * 3 = 9 T-shirts
Adding the T-shirts and sweaters, Norma found 3 + 9 = 12 clothes
Subtracting the clothes she left from the clothes she found, 27 - 12 = 15 clothes are missing
The answer is 15

Question: Adam has an orchard. Every day for 30 days he picks 4 apples from his orchard. After a month, Adam has collected all the remaining apples, which were 230. How many apples in total has Adam collected from his orchard?
Let's think step by step
During 30 days Adam picked 4 * 30 = 120 apples.
So in total with all the remaining apples, he picked 120 + 230 = 350 apples from his orchard.
The answer is 350
```

## File: `examples/add_merges.py`
```python
import argparse
import base64
import collections
import logging
import unicodedata
from pathlib import Path

import regex as re
from tqdm.contrib.logging import tqdm_logging_redirect

PAT_STR = r"""(?i:'s|'t|'re|'ve|'m|'ll|'d)|[^\r\n\p{L}\p{N}]?\p{L}+|\p{N}| ?[^\s\p{L}\p{N}]+[\r\n]*|\s*[\r\n]+|\s+(?!\S)|\s+"""


logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG, format="[%(asctime)s] %(levelname)s - %(message)s"
)


def load_tiktoken_bpe(tiktoken_bpe_file: str) -> "dict[bytes, int]":
    contents = open(tiktoken_bpe_file, "rb").read()
    return {
        base64.b64decode(token): int(rank)
        for token, rank in (line.split() for line in contents.splitlines() if line)
    }


def dump_tiktoken_bpe(bpe_ranks: "dict[bytes, int]", tiktoken_bpe_file: str) -> None:
    with open(tiktoken_bpe_file, "wb") as f:
        for token, rank in sorted(bpe_ranks.items(), key=lambda x: x[1]):
            f.write(base64.b64encode(token) + b" " + str(rank).encode() + b"\n")


def bytes_to_pieces(the_bytes: bytes) -> "tuple[bytes]":
    return tuple(bytes([byte]) for byte in the_bytes)


def get_pairs(pieces: "tuple[bytes]") -> "set[tuple[bytes, bytes]]":
    return set(zip(pieces[:-1], pieces[1:]))


def get_stats(
    vocab: "dict[tuple[bytes, ...], int]",
) -> "dict[tuple[bytes, bytes], int]":
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        for i in range(len(word) - 1):
            pairs[(word[i], word[i + 1])] += freq
    return pairs


def merge_vocab(
    pair: "tuple[bytes, bytes]", vocab: "dict[tuple[bytes, ...], int]"
) -> "dict[tuple[bytes, ...], int]":
    return {apply_bp(pieces, pair): freq for pieces, freq in vocab.items()}


def apply_bp(
    pieces: "tuple[bytes, ...]", pair: "tuple[bytes, bytes]"
) -> "tuple[bytes, ...]":
    new_pieces = []
    first, second = pair
    i = 0
    while i < len(pieces):
        try:
            j = pieces.index(first, i)
            new_pieces.extend(pieces[i:j])
            i = j
        except:
            new_pieces.extend(pieces[i:])
            break

        if pieces[i] == first and i < len(pieces) - 1 and pieces[i + 1] == second:
            new_pieces.append(first + second)
            i += 2
        else:
            new_pieces.append(pieces[i])
            i += 1

    return tuple(new_pieces)


def bpe(word: bytes, merges: "dict[bytes,int]") -> "tuple[bytes, ...]":
    pieces = bytes_to_pieces(word)
    while len(pieces) > 1:
        pairs = get_pairs(pieces)
        pair = min(pairs, key=lambda pair: merges.get(pair[0] + pair[1], float("inf")))

        if pair[0] + pair[1] not in merges:
            break
        pieces = apply_bp(pieces, pair)
        # logger.debug(f"{[(p, p.decode('utf8', errors='replace')) for p in pieces]} {pair} {pieces}")
    return pieces


def best_pair_sort_key(
    item: "tuple[dict[bytes, bytes], int]",
) -> "tuple[int, int, int, str, bytes]":
    # prefer to use the highest frequency or shortest length or lexi sort, sligtly slower
    pair, freq = item
    pair_bytes = pair[0] + pair[1]
    pair_byte_length = len(pair_bytes)
    pair_str = pair_bytes.decode("utf-8", errors="replace")
    pair_str_length = len(pair_str)
    return -freq, pair_str_length, pair_byte_length, pair_str, pair_bytes


def learn_bpe(
    freqs: "dict[str,int]", existing: "dict[bytes, int]"
) -> "tuple[bytes, bytes]":
    vocab = {bpe(k.encode("utf-8"), existing): v for k, v in freqs.items()}
    vocab = {key: value for key, value in vocab.items() if len(key) > 1}
    new_merges = []
    with tqdm_logging_redirect() as bar:
        while vocab:
            pairs = get_stats(vocab)

            best, freq = min(pairs.items(), key=best_pair_sort_key)

            logger.debug(
                f'{best} ({(best[0]+best[1]).decode("utf-8", errors="replace")}) is selected as the next merge with freq {freq}'
            )
            new_merges.append(best)

            vocab = merge_vocab(best, vocab)
            vocab = {key: value for key, value in vocab.items() if len(key) > 1}
            bar.update()

    return new_merges


def load_expand_vocab(path: Path) -> "dict[str, int]":
    freqs = {}
    with open(path, "r", encoding="utf8") as fin:
        for line in fin:
            if not line.strip():
                continue
            word, freq = line.strip().split("\t")
            word = unicodedata.normalize("NFC", word)
            parts = re.findall(PAT_STR, word)
            if len(parts) > 1:
                logger.warning(
                    f"{word} would be pre-tokenized to {parts}, and thus cannot be added to vocabulary"
                )
                continue
            try:
                freq = int(freq)
            except ValueError as _:
                freq = 1
            if word in freqs:
                logger.warning(
                    f"{word} is repeated, the frequency is increased by this much"
                )
                freqs[word] += freq
            else:
                freqs[word] = freq
    return freqs


def make_new_merges_by_bpe(
    input_path: Path, output_path: Path, expand_path: Path, start_id: int
) -> None:
    mergeable_ranks = load_tiktoken_bpe(input_path)

    if not start_id or start_id == -1:
        start_id = len(mergeable_ranks)
    elif start_id < len(mergeable_ranks):
        logger.warning(
            f"start_id {start_id} is too small, existing merges will be overridden, DONOT DO THIS. changed to {len(mergeable_ranks)}"
        )
        start_id = len(mergeable_ranks)
    else:
        start_id = start_id

    expand_vocab_freqs = load_expand_vocab(expand_path)
    for word in list(expand_vocab_freqs):
        token = word.encode("utf-8")
        if token in mergeable_ranks:
            logger.warning(f"word {word} is already a token {token}, skipping")
            del expand_vocab_freqs[word]

    logger.info(f"number of existing merges: {len(mergeable_ranks)}")
    logger.info(f"number of words for expanding: {len(expand_vocab_freqs)}")

    new_merges = learn_bpe(expand_vocab_freqs, mergeable_ranks)
    logger.info(f"number of newly learned merges: {len(new_merges)}")

    extra_merges = {p[0] + p[1]: i for i, p in enumerate(new_merges, start=start_id)}

    dump_tiktoken_bpe(extra_merges, output_path)


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("input_path", type=str, help="Path for input tiktoken file")
    parser.add_argument(
        "output_path",
        type=str,
        help="Path for output tiktoken file, containing only the new merges",
    )
    parser.add_argument(
        "vocab_path",
        type=str,
        help="Path for words needed adding, each line is a word and its frequency separated by \\t",
    )
    # if the extended vocabulary is for fine-tuning, you better set those correctly (the default is for qwen.tiktoken)
    # if the extended vocabulary is for pretraining from the start, no need
    parser.add_argument(
        "--start_id",
        type=int,
        default=151851,
        help="The start id for new merges. For Qwen tokenizer, this should be 151851 (skipping the existing special tokens)",
    )

    args = parser.parse_args()

    make_new_merges_by_bpe(
        args.input_path, args.output_path, args.vocab_path, args.start_id
    )


if __name__ == "__main__":
    main()
```

## File: `examples/auto_comments.md`
```markdown
# Auto Comments 
本文档介绍Auto Comments，这是一个利用Qwen模型为代码文件自动生成注释的使用案例。

# 使用方法
您可以直接执行如下命令，为提供的代码文件生成注释：
```
python auto_comments.py --path 'path of file or folder'
```

参数：
- path：文件路径。可以是文件（目前支持python代码文件），也可以是文件夹（会扫描文件夹下所有python代码文件）
- regenerate：重新生成。默认False，如果针对同一文件需要重新生成注释，请设置为True

# 使用样例
- 执行：python auto_comments.py --path test_file.py
- test_file.py 内容为：
```
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid")

rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
data = data.rolling(7).mean()

sns.lineplot(data=data, palette="tab10", linewidth=2.5)
```

- 输出：test_file_comments.py(包含注释的代码文件)，文件内容如下：
```
# 导入需要的库
import numpy as np
import pandas as pd
import seaborn as sns

# 设置 Seaborn 的主题风格为白色网格
sns.set_theme(style="whitegrid")

# 生成随机数
rs = np.random.RandomState(365)

# 生成 365 行 4 列的随机数，并按行累加
values = rs.randn(365, 4).cumsum(axis=0)

# 生成日期
dates = pd.date_range("1 1 2016", periods=365, freq="D")

# 将随机数和日期组合成 DataFrame
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])

# 对 DataFrame 进行 7 天滑动平均
data = data.rolling(7).mean()

# 使用 Seaborn 绘制折线图
sns.lineplot(data=data, palette="tab10", linewidth=2.5)
```
```

## File: `examples/auto_comments.py`
```python
# 运行方式：python auto_comments.py --path 'path of file or folder'
# 脚本功能：使用QWen-7B-Chat为提供的代码文件自动生成注释。(详见auto_comments.md)


import argparse
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

MaxLine = 50 # 限制单次处理最大代码行数
SplitKey = ["\ndef "] # 自定义的切分代码标识
CodeFileType = ["py"] # 目前仅测试过对python文件生成注释

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='Qwen-7B/eval/evaluate_ceval.py')
    parser.add_argument('--regenerate', action='store_true', default=False) #如果已经生成过注释，默认不会重新生成
    args = parser.parse_args()
    return args

class QWenChat():
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

        # use bf16
        # model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
        # use fp16
        # model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
        # use cpu only
        # model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
        # use auto mode, automatically select precision based on the device.
        self.model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True).eval()
        
        # Specify hyperparameters for generation
        self.model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)
        self.history = None
        
    def chat(self, query, system = ""):

        # use history
        # response, history = self.model.chat(self.tokenizer, query, history=self.history)

        # 默认不使用history
        response, history = self.model.chat(self.tokenizer, query, history=None)
        self.history = history

        return response
# 生成注释
def gen_code_comments(context, model = None, **kwargs):
    prompt = "\n为以上代码生成细致的中文注释，注意使用合适的语法。要求必须在每个函数开头生成一段统一的函数功能注释。\n除了注释，请保证原始代码内容不变。不要返回除了注释和代码以外的其余信息，不要生成额外代码。\n"
    return model.chat(context + prompt)

def read_file(path):
    f = open(path, "r",encoding='utf-8')
    lines = f.readlines()
    return "".join(lines)

def write_file(path, context):
    with open(path,'w') as f:
        f.write(context)

# 如果代码文件过长，可以简单按照最大行数切分代码
def split_context_by_maxline(text):
    lines = text.split("\n")
    lines_len = len(lines)
    res = []
    for i in range(MaxLine, lines_len, MaxLine):
        res.append("\n".join(lines[i-MaxLine:i]))

    if i < lines_len:
        res.append("\n".join(lines[i:]))
    return res

# 如果代码文件过长，可以简单按照函数切分代码
def split_context_by_splitkey(text):
    blocks = text.split(SplitKey[0])
    return [blocks[0]] + [SplitKey[0]+x for x in blocks[1:]]

# merge原始代码和生成的注释，目的是保证原始代码不被更改。这部分可以使用各种不同的策略处理。
def merge_code_and_comments(original_file, comments_path):
    res = []
    ori_f = open(original_file, "r",encoding='utf-8')
    ori_lines = ori_f.readlines()

    com_f = open(comments_path, "r",encoding='utf-8')
    com_lines = com_f.readlines()
    len_com_lines = len(com_lines)
    p = 0
    j = 0
    for i, line in enumerate(ori_lines):
        if line.isspace():
            continue
        if line.strip()[0] == '#':
            res.append(line)
            continue
        while j < len_com_lines and line[:-1] not in com_lines[j]:
            j += 1
        if j < len_com_lines:
            p = j - 1
            up_comments = []
            triple_dot_flag = 0
            while p < j:
                if p < 0 or (res and res[-1] and com_lines[p] == res[-1]):
                    break
                if com_lines[p].strip() and (len(com_lines[p].strip())>3 and com_lines[p].strip()[-3:] == '"""' and com_lines[p].strip()[:3] == '"""') or (len(com_lines[p].strip())>3 and com_lines[p].strip()[-3:] == "'''" and com_lines[p].strip()[:3] == "'''"):
                    up_comments.append(com_lines[p])
                    p -= 1
                    continue
                if com_lines[p].strip() and (com_lines[p].strip()[-3:] == '"""' or com_lines[p].strip()[:3] == '"""' or com_lines[p].strip()[-3:] == "'''" or com_lines[p].strip()[:3] == "'''"):
                    triple_dot_flag = (triple_dot_flag + 1)%2
                    up_comments.append(com_lines[p])
                    p -= 1
                    continue
                if triple_dot_flag:
                    up_comments.append(com_lines[p])
                    p -= 1
                    continue
                if (com_lines[p].strip()=="") or (com_lines[p].strip() and com_lines[p].strip()[0] == '#' and "省略部分内容" not in com_lines[p]):
                    up_comments.append(com_lines[p])
                else:
                    break
                p -= 1
            if up_comments:
                res.extend(reversed(up_comments))
            if "#" in com_lines[j] and "#" not in line:
                in_line_comments = "  #" + com_lines[j].split("#")[-1]
                res.append(line[:-1]+in_line_comments)
            else:
                res.append(line)
            p = j+1
        else:
            res.append(line)
            j = p

    write_file(comments_path, "".join(res))

# 处理单个文件
def deal_one_file(model, path, args):
    context = read_file(path)

    fname = path.split("/")[-1]
    fpath = "/".join(path.split("/")[:-1])
    outfname = fname.split(".")[0]+"_comments."+fname.split(".")[-1]

    comments_path = os.path.join(fpath, outfname)
    if (not args.regenerate) and os.path.exists(comments_path):
        print("use cache: ", comments_path)
        return

    context_line = len(context.split("\n"))
    if context_line < MaxLine:
        res = gen_code_comments(context, model = model)
    elif SplitKey[0] not in context:
        context_list = split_context_by_maxline(context)
        res = "\n".join([gen_code_comments(context_block, model = model) for context_block in context_list])
    else:
        context_list = split_context_by_splitkey(context)
        res = "\n".join([gen_code_comments(context_block, model = model) for context_block in context_list])

    write_file(comments_path, res)
    merge_code_and_comments(path, comments_path)

# 处理文件夹
def deal_folder(model, path, args):
    for fl in os.listdir(path):
        now_path = os.path.join(path, fl)
        if os.path.isfile(now_path):
            if (now_path.split(".")[-1] in CodeFileType) and ("_comments" not in now_path):
                deal_one_file(model, now_path, args)
        elif os.path.isdir(now_path):
            deal_folder(model, now_path, args)
        else:
            print("Please specify a correct path!")

def transfer(args):
    model = QWenChat()

    if os.path.isfile(args.path):
        if (args.path.split(".")[-1] in CodeFileType) and ("_comments" not in args.path):
            deal_one_file(model, args.path, args)
    elif os.path.isdir(args.path):
        deal_folder(model, args.path, args)
    else:
        print("Please specify a correct path!")

if __name__ == '__main__':
    args = parse_args()
    print(args)
    transfer(args)
```

## File: `examples/function_call_examples.py`
```python
# Reference: https://openai.com/blog/function-calling-and-other-api-updates
import json
from pprint import pprint

import openai

# To start an OpenAI-like Qwen server, use the following commands:
#   git clone https://github.com/QwenLM/Qwen-7B;
#   cd Qwen-7B;
#   pip install fastapi uvicorn openai pydantic sse_starlette;
#   python openai_api.py;
#
# Then configure the api_base and api_key in your client:
openai.api_base = 'http://localhost:8000/v1'
openai.api_key = 'none'


def call_qwen(messages, functions=None):
    print('input:')
    pprint(messages, indent=2)
    if functions:
        response = openai.ChatCompletion.create(model='Qwen',
                                                messages=messages,
                                                functions=functions)
    else:
        response = openai.ChatCompletion.create(model='Qwen',
                                                messages=messages)
    response = response.choices[0]['message']
    response = json.loads(json.dumps(response,
                                     ensure_ascii=False))  # fix zh rendering
    print('output:')
    pprint(response, indent=2)
    print()
    return response


def test_1():
    messages = [{'role': 'user', 'content': '你好'}]
    call_qwen(messages)
    messages.append({'role': 'assistant', 'content': '你好！很高兴为你提供帮助。'})

    messages.append({
        'role': 'user',
        'content': '给我讲一个年轻人奋斗创业最终取得成功的故事。故事只能有一句话。'
    })
    call_qwen(messages)
    messages.append({
        'role':
        'assistant',
        'content':
        '故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。李明想要成为一名成功的企业家。……',
    })

    messages.append({'role': 'user', 'content': '给这个故事起一个标题'})
    call_qwen(messages)


def test_2():
    functions = [
        {
            'name_for_human':
            '谷歌搜索',
            'name_for_model':
            'google_search',
            'description_for_model':
            '谷歌搜索是一个通用搜索引擎，可用于访问互联网、查询百科知识、了解时事新闻等。' +
            ' Format the arguments as a JSON object.',
            'parameters': [{
                'name': 'search_query',
                'description': '搜索关键词或短语',
                'required': True,
                'schema': {
                    'type': 'string'
                },
            }],
        },
        {
            'name_for_human':
            '文生图',
            'name_for_model':
            'image_gen',
            'description_for_model':
            '文生图是一个AI绘画（图像生成）服务，输入文本描述，返回根据文本作画得到的图片的URL。' +
            ' Format the arguments as a JSON object.',
            'parameters': [{
                'name': 'prompt',
                'description': '英文关键词，描述了希望图像具有什么内容',
                'required': True,
                'schema': {
                    'type': 'string'
                },
            }],
        },
    ]

    messages = [{'role': 'user', 'content': '（请不要调用工具）\n\n你好'}]
    call_qwen(messages, functions)
    messages.append({
        'role': 'assistant',
        'content': '你好！很高兴见到你。有什么我可以帮忙的吗？'
    }, )

    messages.append({'role': 'user', 'content': '搜索一下谁是周杰伦'})
    call_qwen(messages, functions)
    messages.append({
        'role': 'assistant',
        'content': '我应该使用Google搜索查找相关信息。',
        'function_call': {
            'name': 'google_search',
            'arguments': '{"search_query": "周杰伦"}',
        },
    })

    messages.append({
        'role': 'function',
        'name': 'google_search',
        'content': 'Jay Chou is a Taiwanese singer.',
    })
    call_qwen(messages, functions)
    messages.append(
        {
            'role': 'assistant',
            'content': '周杰伦（Jay Chou）是一位来自台湾的歌手。',
        }, )

    messages.append({'role': 'user', 'content': '搜索一下他老婆是谁'})
    call_qwen(messages, functions)
    messages.append({
        'role': 'assistant',
        'content': '我应该使用Google搜索查找相关信息。',
        'function_call': {
            'name': 'google_search',
            'arguments': '{"search_query": "周杰伦 老婆"}',
        },
    })

    messages.append({
        'role': 'function',
        'name': 'google_search',
        'content': 'Hannah Quinlivan'
    })
    call_qwen(messages, functions)
    messages.append(
        {
            'role': 'assistant',
            'content': '周杰伦的老婆是Hannah Quinlivan。',
        }, )

    messages.append({'role': 'user', 'content': '用文生图工具画个可爱的小猫吧，最好是黑猫'})
    call_qwen(messages, functions)
    messages.append({
        'role': 'assistant',
        'content': '我应该使用文生图API来生成一张可爱的小猫图片。',
        'function_call': {
            'name': 'image_gen',
            'arguments': '{"prompt": "cute black cat"}',
        },
    })

    messages.append({
        'role':
        'function',
        'name':
        'image_gen',
        'content':
        '{"image_url": "https://image.pollinations.ai/prompt/cute%20black%20cat"}',
    })
    call_qwen(messages, functions)


def test_3():
    functions = [{
        'name': 'get_current_weather',
        'description': 'Get the current weather in a given location.',
        'parameters': {
            'type': 'object',
            'properties': {
                'location': {
                    'type': 'string',
                    'description':
                    'The city and state, e.g. San Francisco, CA',
                },
                'unit': {
                    'type': 'string',
                    'enum': ['celsius', 'fahrenheit']
                },
            },
            'required': ['location'],
        },
    }]

    messages = [{
        'role': 'user',
        # Note: The current version of Qwen-7B-Chat (as of 2023.08) performs okay with Chinese tool-use prompts,
        # but performs terribly when it comes to English tool-use prompts, due to a mistake in data collecting.
        'content': '波士顿天气如何？',
    }]
    call_qwen(messages, functions)
    messages.append(
        {
            'role': 'assistant',
            'content': None,
            'function_call': {
                'name': 'get_current_weather',
                'arguments': '{"location": "Boston, MA"}',
            },
        }, )

    messages.append({
        'role':
        'function',
        'name':
        'get_current_weather',
        'content':
        '{"temperature": "22", "unit": "celsius", "description": "Sunny"}',
    })
    call_qwen(messages, functions)


def test_4():
    from langchain.agents import AgentType, initialize_agent, load_tools
    from langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI(
        model_name='Qwen',
        openai_api_base='http://localhost:8000/v1',
        openai_api_key='EMPTY',
        streaming=False,
    )
    tools = load_tools(['arxiv'], )
    agent_chain = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    # TODO: The performance is okay with Chinese prompts, but not so good when it comes to English.
    agent_chain.run('查一下论文 1605.08386 的信息')


if __name__ == '__main__':
    print('### Test Case 1 - No Function Calling (普通问答、无函数调用) ###')
    test_1()
    print('### Test Case 2 - Use Qwen-Style Functions (函数调用，千问格式) ###')
    test_2()
    print('### Test Case 3 - Use GPT-Style Functions (函数调用，GPT格式) ###')
    test_3()
    print('### Test Case 4 - Use LangChain (接入Langchain) ###')
    test_4()
```

## File: `examples/function_call_finetune_examples.py`
```python
#
# # Fine-tuning Script:
# Please start by reading the Fine-tuning section of README.md.
#
# # Fine-tuning Data Preparation:
# Then, if you would like to see some examples of how to prepare training samples for function calling,
# which is actually ReAct prompting under the hood, please read this file.

# # Inference Script:
# If you are interested in implementing function calling via ReAct prompting for inference,
# please refer to openai_api.py in our repository.
#
# If you have any questions, please raise an issue.
#

import json


def format_train_sample(messages):
    #
    # You do not need the `function` role, as Qwen's function calling is actually implemented via ReAct,
    # not by adding a `function` role or `function_call` message. See openai_api.py for details.
    #
    # If you need the `system` role, you might need to modify `finetune.py` accordingly.
    #
    assert set(m["role"] for m in messages) == {"user", "assistant"}

    sample = {
        "conversations": [
            {
                "from": m["role"],
                "value": m["content"],
            }
            for m in messages
        ]
    }
    return sample


TOOL_DESC = """{name_for_model}: Call this tool to interact with the {name_for_human} API. What is the {name_for_human} API useful for? {description_for_model} Parameters: {parameters}"""

REACT_INSTRUCTION = """Answer the following questions as best you can. You have access to the following APIs:

{tools_text}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tools_name_text}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!"""


def build_react_instruction(functions):
    tools_text = []
    tools_name_text = []
    for func_info in functions:
        name = func_info.get("name", "")
        name_m = func_info.get("name_for_model", name)
        name_h = func_info.get("name_for_human", name)
        desc = func_info.get("description", "")
        desc_m = func_info.get("description_for_model", desc)
        tool = TOOL_DESC.format(
            name_for_model=name_m,
            name_for_human=name_h,
            description_for_model=desc_m,
            parameters=json.dumps(func_info["parameters"], ensure_ascii=False),
        )
        tools_text.append(tool)
        tools_name_text.append(name_m)
    tools_text = "\n\n".join(tools_text)
    tools_name_text = ", ".join(tools_name_text)
    instruction = REACT_INSTRUCTION.format(
        tools_text=tools_text,
        tools_name_text=tools_name_text,
    )
    return instruction


def main():
    example_train_samples = []

    example_functions = [
        {
            "name_for_human": "Google Search",
            "name_for_model": "google_search",
            "description_for_model": "Google Search is a general search engine that can be used to access the internet,"
            + " query encyclopedia knowledge, and stay informed about current events."
            + " Format the arguments as a JSON object.",  # If you expect `Action Input` to be a JSON.
            "parameters": [
                {
                    "name": "search_query",
                    "description": "Search keywords or phrases",
                    "required": True,  # Set to False if it is an optional parameter.
                    "schema": {"type": "string"},
                },
                # You can add more parameters to this `parameters` list if you wish.
            ],
        },
        {
            "name_for_human": "Code Interpreter",
            "name_for_model": "code_interpreter",
            "description_for_model": "Code interpreter that can execute Python code."
            + "Enclose the code within triple backticks (`)"
            + " at the beginning and end of the code.",  # If you expect `Action Input` to be a Markdown code block.
            "parameters": [
                {
                    "name": "code",
                    "description": "Code to be executed",
                    "required": True,
                    "schema": {"type": "string"},
                },
            ],
        },
    ]
    example_instruction = build_react_instruction(example_functions)

    # This example has multiple actions in one single response.
    example_train_samples.append(
        [
            {
                "role": "user",
                "content": f"{example_instruction}\n\nQuestion: Who is jay chou? And who is his wife?",
            },
            {
                "role": "assistant",
                "content": """
Thought: I need to google Jay Chou.
Action: google_search
Action Input: {"search_query": "Jay Chou"}
Observation: Jay Chou is ...
Thought: I need to google Jay's wife.
Action: google_search
Action Input: {"search_query": "Jay Chou's wife"}
Observation: Jay Chou's wife is ...
Thought: I now know the final answer
Final Answer: Jay Chou is ... His wife is ...
                """.strip(),
            },
        ]
    )

    # This example involves multiple rounds of conversation.
    example_train_samples.append(
        [
            # Round #1
            {
                "role": "user",
                "content": f"{example_instruction}\n\nQuestion: 123+456=?",
            },
            {
                "role": "assistant",
                "content": """
Thought: I need to compute the result using Code Interpreter.
Action: code_interpreter
Action Input:
```py
123 + 456
```
Observation: 579
Thought: I now know the final answer
Final Answer: 579
                """.strip(),
            },
            # Round #2
            {
                "role": "user",
                "content": "Multiply the result by 2.",
            },
            {
                "role": "assistant",
                "content": """
Thought: Code Interpreter is helpful for answering this question.
Action: code_interpreter
Action Input:
```py
579 * 2
```
Observation: 1158
Thought: I now know the final answer
Final Answer: 1158
                        """.strip(),
            },
            # Round #3
            {
                "role": "user",
                "content": "You are so smart, Qwen.",  # No action is needed for this question.
            },
            {
                "role": "assistant",
                "content": """
Thought: I now know the final answer
Final Answer: Thank you.
                        """.strip(),
            },
            # Round #4
            {
                "role": "user",
                "content": "Please re-execute the code for computing my first question again.",
            },
            {
                "role": "assistant",
                "content": """
Thought: I need to re-compute the result.
Action: code_interpreter
Action Input:
```py
123 + 456
```
Observation: 579
Thought: I now know the final answer
Final Answer: 579
                        """.strip(),
            },
        ]
    )

    example_train_samples = [format_train_sample(x) for x in example_train_samples]
    with open(
        "example_func_call_train_samples.json", "w"
    ) as fout:  # data for fine-tuning
        fout.write(json.dumps(example_train_samples, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
```

## File: `examples/langchain_tooluse.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "30e24ef3",
   "metadata": {
    "tags": []
   },
   "source": [
    "# 如何让 Qwen-7b 使用 Langchain 中的 工具\n",
    "\n",
    "本文档主要介绍如何让千问调用 [LangChain](https://python.langchain.com/docs/get_started/introduction.html) 框架中实现好的谷歌搜索、 WolframAlpha 等工具。将主要基于 [ReAct Prompting](https://github.com/QwenLM/Qwen-7B/blob/main/examples/react_prompt.md) 技术，一种特殊的链式思考（Chain-of-Thought，简称 CoT）提示技巧，来实现这一目的。"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "212979ec",
   "metadata": {
    "tags": []
   },
   "source": [
    "## 安装依赖"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e21c6728",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 安装千问的依赖\n",
    "!cd Qwen-7b\n",
    "!pip install -r requirements.txt\n",
    "\n",
    "# 安装 langchain 相关依赖\n",
    "!pip install langchain google-search-results wolframalpha arxiv;"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b5e6ef9",
   "metadata": {
    "tags": []
   },
   "source": [
    "## 第零步 - 导入 LangChain 的工具"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af7d0058",
   "metadata": {},
   "source": [
    "以下引入几个常用 APIs 作为演示：\n",
    " - [谷歌搜索API](https://serper.dev/?gclid=EAIaIQobChMIj9eqof7OgAMV44VbCh1F3QZoEAAYASABEgIh3fD_BwE#google-search-api)\n",
    " - [WolframAlpha](https://products.wolframalpha.com/api/)\n",
    " - arxiv论文搜索\n",
    " - python shell (需升级python至3.9以上使用)\n",
    "\n",
    "注1：此处推荐模仿此案例，细致地构造给千问看的工具描述。\n",
    "\n",
    "注2：谷歌搜索（SERPAPI）， WolframAlpha 需自行申请它们的 API_KEY 后才能使用。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "07e49b98-9d6c-41f2-9b18-f043f2d13e1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain import SerpAPIWrapper\n",
    "from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper\n",
    "from langchain.utilities import ArxivAPIWrapper\n",
    "from langchain.tools.python.tool import PythonAstREPLTool\n",
    "\n",
    "from typing import Dict, Tuple\n",
    "import os\n",
    "import json\n",
    "\n",
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "# 为了使用谷歌搜索（SERPAPI）， WolframAlpha，您需要自行申请它们的 API KEY，然后填入此处\n",
    "os.environ['SERPAPI_API_KEY'] = '重要！请在这里填入您的 SERPAPI_API_KEY！'\n",
    "os.environ['WOLFRAM_ALPHA_APPID'] = '重要！请在这里填入您的 WOLFRAM_ALPHA_APPID！'\n",
    "\n",
    "search = SerpAPIWrapper()\n",
    "WolframAlpha = WolframAlphaAPIWrapper()\n",
    "arxiv = ArxivAPIWrapper()\n",
    "python=PythonAstREPLTool()\n",
    "\n",
    "def tool_wrapper_for_qwen(tool):\n",
    "    def tool_(query):\n",
    "        query = json.loads(query)[\"query\"]\n",
    "        return tool.run(query)\n",
    "    return tool_\n",
    "\n",
    "# 以下是给千问看的工具描述：\n",
    "TOOLS = [\n",
    "    {\n",
    "        'name_for_human':\n",
    "            'google search',\n",
    "        'name_for_model':\n",
    "            'Search',\n",
    "        'description_for_model':\n",
    "            'useful for when you need to answer questions about current events.',\n",
    "        'parameters': [{\n",
    "            \"name\": \"query\",\n",
    "            \"type\": \"string\",\n",
    "            \"description\": \"search query of google\",\n",
    "            'required': True\n",
    "        }], \n",
    "        'tool_api': tool_wrapper_for_qwen(search)\n",
    "    },\n",
    "    {\n",
    "        'name_for_human':\n",
    "            'Wolfram Alpha',\n",
    "        'name_for_model':\n",
    "            'Math',\n",
    "        'description_for_model':\n",
    "            'Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life.',\n",
    "        'parameters': [{\n",
    "            \"name\": \"query\",\n",
    "            \"type\": \"string\",\n",
    "            \"description\": \"the problem to solved by Wolfram Alpha\",\n",
    "            'required': True\n",
    "        }], \n",
    "        'tool_api': tool_wrapper_for_qwen(WolframAlpha)\n",
    "    },  \n",
    "    {\n",
    "        'name_for_human':\n",
    "            'arxiv',\n",
    "        'name_for_model':\n",
    "            'Arxiv',\n",
    "        'description_for_model':\n",
    "            'A wrapper around Arxiv.org Useful for when you need to answer questions about Physics, Mathematics, Computer Science, Quantitative Biology, Quantitative Finance, Statistics, Electrical Engineering, and Economics from scientific articles on arxiv.org.',\n",
    "        'parameters': [{\n",
    "            \"name\": \"query\",\n",
    "            \"type\": \"string\",\n",
    "            \"description\": \"the document id of arxiv to search\",\n",
    "            'required': True\n",
    "        }], \n",
    "        'tool_api': tool_wrapper_for_qwen(arxiv)\n",
    "    },\n",
    "    {\n",
    "        'name_for_human':\n",
    "            'python',\n",
    "        'name_for_model':\n",
    "            'python',\n",
    "        'description_for_model':\n",
    "            \"A Python shell. Use this to execute python commands. When using this tool, sometimes output is abbreviated - Make sure it does not look abbreviated before using it in your answer. \"\n",
    "            \"Don't add comments to your python code.\",\n",
    "        'parameters': [{\n",
    "            \"name\": \"query\",\n",
    "            \"type\": \"string\",\n",
    "            \"description\": \"a valid python command.\",\n",
    "            'required': True\n",
    "        }],\n",
    "        'tool_api': tool_wrapper_for_qwen(python)\n",
    "    }\n",
    "\n",
    "]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7ec2027",
   "metadata": {},
   "source": [
    "## 第一步：让千问判断调用什么工具，生成工具入参"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a50d676",
   "metadata": {},
   "source": [
    "根据prompt模版、query、工具的信息构建prompt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4a8feb0e-22f7-4184-9ea0-b864812c9b09",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Answer the following questions as best you can. You have access to the following tools:\n",
      "\n",
      "Search: Call this tool to interact with the google search API. What is the google search API useful for? useful for when you need to answer questions about current events. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"search query of google\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Use the following format:\n",
      "\n",
      "Question: the input question you must answer\n",
      "Thought: you should always think about what to do\n",
      "Action: the action to take, should be one of [Search]\n",
      "Action Input: the input to the action\n",
      "Observation: the result of the action\n",
      "... (this Thought/Action/Action Input/Observation can be repeated zero or more times)\n",
      "Thought: I now know the final answer\n",
      "Final Answer: the final answer to the original input question\n",
      "\n",
      "Begin!\n",
      "\n",
      "Question: 加拿大2023年人口统计数字是多少？\n"
     ]
    }
   ],
   "source": [
    "TOOL_DESC = \"\"\"{name_for_model}: Call this tool to interact with the {name_for_human} API. What is the {name_for_human} API useful for? {description_for_model} Parameters: {parameters} Format the arguments as a JSON object.\"\"\"\n",
    "\n",
    "REACT_PROMPT = \"\"\"Answer the following questions as best you can. You have access to the following tools:\n",
    "\n",
    "{tool_descs}\n",
    "\n",
    "Use the following format:\n",
    "\n",
    "Question: the input question you must answer\n",
    "Thought: you should always think about what to do\n",
    "Action: the action to take, should be one of [{tool_names}]\n",
    "Action Input: the input to the action\n",
    "Observation: the result of the action\n",
    "... (this Thought/Action/Action Input/Observation can be repeated zero or more times)\n",
    "Thought: I now know the final answer\n",
    "Final Answer: the final answer to the original input question\n",
    "\n",
    "Begin!\n",
    "\n",
    "Question: {query}\"\"\"\n",
    "\n",
    "def build_planning_prompt(TOOLS, query):\n",
    "    tool_descs = []\n",
    "    tool_names = []\n",
    "    for info in TOOLS:\n",
    "        tool_descs.append(\n",
    "            TOOL_DESC.format(\n",
    "                name_for_model=info['name_for_model'],\n",
    "                name_for_human=info['name_for_human'],\n",
    "                description_for_model=info['description_for_model'],\n",
    "                parameters=json.dumps(\n",
    "                    info['parameters'], ensure_ascii=False),\n",
    "            )\n",
    "        )\n",
    "        tool_names.append(info['name_for_model'])\n",
    "    tool_descs = '\\n\\n'.join(tool_descs)\n",
    "    tool_names = ','.join(tool_names)\n",
    "\n",
    "    prompt = REACT_PROMPT.format(tool_descs=tool_descs, tool_names=tool_names, query=query)\n",
    "    return prompt\n",
    "\n",
    "prompt_1 = build_planning_prompt(TOOLS[0:1], query=\"加拿大2023年人口统计数字是多少？\")\n",
    "print(prompt_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f22b002",
   "metadata": {},
   "source": [
    "将prompt作为输入获得response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f71b2577-118c-4ce2-a0ed-a45ec59ea35b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "A new version of the following files was downloaded from https://huggingface.co/Qwen/Qwen-7B-Chat:\n",
      "- tokenization_qwen.py\n",
      ". Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.\n",
      "A new version of the following files was downloaded from https://huggingface.co/Qwen/Qwen-7B-Chat:\n",
      "- configuration_qwen.py\n",
      ". Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.\n",
      "A new version of the following files was downloaded from https://huggingface.co/Qwen/Qwen-7B-Chat:\n",
      "- qwen_generation_utils.py\n",
      ". Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.\n",
      "A new version of the following files was downloaded from https://huggingface.co/Qwen/Qwen-7B-Chat:\n",
      "- modeling_qwen.py\n",
      "- qwen_generation_utils.py\n",
      ". Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "23435445dded44d6951aa6a7b771a963",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading shards:   0%|          | 0/8 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "The model is automatically converting to bf16 for faster inference. If you want to disable the automatic precision, please manually add bf16/fp16/fp32=True to \"AutoModelForCausalLM.from_pretrained\".\n",
      "Try importing flash-attention for faster inference...\n",
      "Warning: import flash_attn rotary fail, please install FlashAttention rotary to get higher efficiency https://github.com/Dao-AILab/flash-attention/tree/main/csrc/rotary\n",
      "Warning: import flash_attn rms_norm fail, please install FlashAttention layer_norm to get higher efficiency https://github.com/Dao-AILab/flash-attention/tree/main/csrc/layer_norm\n",
      "Warning: import flash_attn fail, please install FlashAttention to get higher efficiency https://github.com/Dao-AILab/flash-attention\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "728a1c13c2884291ade4cb4a1edfaaf2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Loading checkpoint shards:   0%|          | 0/8 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 国内连 hugginface 网络不好，这段代码可能需要多重试\n",
    "checkpoint = \"Qwen/Qwen-7B-Chat\"\n",
    "TOKENIZER = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True)\n",
    "MODEL = AutoModelForCausalLM.from_pretrained(checkpoint, device_map=\"auto\", trust_remote_code=True).eval()\n",
    "MODEL.generation_config = GenerationConfig.from_pretrained(checkpoint, trust_remote_code=True)\n",
    "MODEL.generation_config.do_sample = False  # greedy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dc0dbd6c-5a0f-44c9-a019-0ec0283ca92d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thought: 我应该使用搜索工具帮助我完成任务。search api能完成搜索的任务。\n",
      "Action: Search\n",
      "Action Input: {\"query\": \"加拿大 2023年人口统计数字\"}\n",
      "Observation:\n"
     ]
    }
   ],
   "source": [
    "stop = [\"Observation:\", \"Observation:\\n\"]\n",
    "react_stop_words_tokens = [TOKENIZER.encode(stop_) for stop_ in stop]\n",
    "response_1, _ = MODEL.chat(TOKENIZER, prompt_1, history=None, stop_words_ids=react_stop_words_tokens)\n",
    "print(response_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ebf47ac",
   "metadata": {},
   "source": [
    "## 第二步：从千问的输出中解析需要使用的工具和入参，并调用对应工具"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1a431670-a1f6-4afd-972f-1cfd6d06e8c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "根据加拿大统计局预测，加拿大人口今天（2023年6月16日）预计将超过4000万。 联邦统计局使用模型来实时估计加拿大的人口，该计数模型预计加拿大人口将在北美东部时间今天下午3点前达到4000万。 加拿大的人口增长率目前为2.7％。\n"
     ]
    }
   ],
   "source": [
    "def parse_latest_plugin_call(text: str) -> Tuple[str, str]:\n",
    "    i = text.rfind('\\nAction:')\n",
    "    j = text.rfind('\\nAction Input:')\n",
    "    k = text.rfind('\\nObservation:')\n",
    "    if 0 <= i < j:  # If the text has `Action` and `Action input`,\n",
    "        if k < j:  # but does not contain `Observation`,\n",
    "            # then it is likely that `Observation` is ommited by the LLM,\n",
    "            # because the output text may have discarded the stop word.\n",
    "            text = text.rstrip() + '\\nObservation:'  # Add it back.\n",
    "            k = text.rfind('\\nObservation:')\n",
    "    if 0 <= i < j < k:\n",
    "        plugin_name = text[i + len('\\nAction:'):j].strip()\n",
    "        plugin_args = text[j + len('\\nAction Input:'):k].strip()\n",
    "        return plugin_name, plugin_args\n",
    "    return '', ''\n",
    "\n",
    "def use_api(tools, response):\n",
    "    use_toolname, action_input = parse_latest_plugin_call(response)\n",
    "    if use_toolname == \"\":\n",
    "        return \"no tool founds\"\n",
    "\n",
    "    used_tool_meta = list(filter(lambda x: x[\"name_for_model\"] == use_toolname, tools))\n",
    "    if len(used_tool_meta) == 0:\n",
    "        return \"no tool founds\"\n",
    "    \n",
    "    api_output = used_tool_meta[0][\"tool_api\"](action_input)\n",
    "    return api_output\n",
    "\n",
    "api_output = use_api(TOOLS, response_1)\n",
    "print(api_output)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "106a4ba0",
   "metadata": {
    "tags": []
   },
   "source": [
    "## 第三步：让千问根据工具返回结果继续作答\n",
    "拼接上述返回答案，形成新的prompt，并获得生成最终结果"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a9d4d42d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Answer the following questions as best you can. You have access to the following tools:\n",
      "\n",
      "Search: Call this tool to interact with the google search API. What is the google search API useful for? useful for when you need to answer questions about current events. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"search query of google\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Use the following format:\n",
      "\n",
      "Question: the input question you must answer\n",
      "Thought: you should always think about what to do\n",
      "Action: the action to take, should be one of [Search]\n",
      "Action Input: the input to the action\n",
      "Observation: the result of the action\n",
      "... (this Thought/Action/Action Input/Observation can be repeated zero or more times)\n",
      "Thought: I now know the final answer\n",
      "Final Answer: the final answer to the original input question\n",
      "\n",
      "Begin!\n",
      "\n",
      "Question: 加拿大2023年人口统计数字是多少？Thought: 我应该使用搜索工具帮助我完成任务。search api能完成搜索的任务。\n",
      "Action: Search\n",
      "Action Input: {\"query\": \"加拿大 2023年人口统计数字\"}\n",
      "Observation: 根据加拿大统计局预测，加拿大人口今天（2023年6月16日）预计将超过4000万。 联邦统计局使用模型来实时估计加拿大的人口，该计数模型预计加拿大人口将在北美东部时间今天下午3点前达到4000万。 加拿大的人口增长率目前为2.7％。 Thought: I now know the final answer.\n",
      "Final Answer: 加拿大2023年人口统计数字预计为4000万。\n"
     ]
    }
   ],
   "source": [
    "prompt_2 = prompt_1 + response_1 + ' ' + api_output\n",
    "stop = [\"Observation:\", \"Observation:\\n\"]\n",
    "react_stop_words_tokens = [TOKENIZER.encode(stop_) for stop_ in stop]\n",
    "response_2, _ = MODEL.chat(TOKENIZER, prompt_2, history=None, stop_words_ids=react_stop_words_tokens)\n",
    "print(prompt_2, response_2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b8da9fd",
   "metadata": {},
   "source": [
    "## 总结 - 串联起整个流程"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1e51a8ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main(query, choose_tools):\n",
    "    prompt = build_planning_prompt(choose_tools, query) # 组织prompt\n",
    "    print(prompt)\n",
    "    stop = [\"Observation:\", \"Observation:\\n\"]\n",
    "    react_stop_words_tokens = [TOKENIZER.encode(stop_) for stop_ in stop]\n",
    "    response, _ = MODEL.chat(TOKENIZER, prompt, history=None, stop_words_ids=react_stop_words_tokens)\n",
    "\n",
    "    while \"Final Answer:\" not in response: # 出现final Answer时结束\n",
    "        api_output = use_api(choose_tools, response) # 抽取入参并执行api\n",
    "        api_output = str(api_output) # 部分api工具返回结果非字符串格式需进行转化后输出\n",
    "        if \"no tool founds\" == api_output:\n",
    "            break\n",
    "        print(\"\\033[32m\" + response + \"\\033[0m\" + \"\\033[34m\" + ' ' + api_output + \"\\033[0m\")\n",
    "        prompt = prompt + response + ' ' + api_output # 合并api输出\n",
    "        response, _ = MODEL.chat(TOKENIZER, prompt, history=None, stop_words_ids=react_stop_words_tokens) # 继续生成\n",
    "\n",
    "    print(\"\\033[32m\" + response + \"\\033[0m\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6dc38a34",
   "metadata": {
    "collapsed": false,
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "==========\n",
      "Answer the following questions as best you can. You have access to the following tools:\n",
      "\n",
      "Search: Call this tool to interact with the google search API. What is the google search API useful for? useful for when you need to answer questions about current events. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"search query of google\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Math: Call this tool to interact with the Wolfram Alpha API. What is the Wolfram Alpha API useful for? Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"the problem to solved by Wolfram Alpha\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Arxiv: Call this tool to interact with the arxiv API. What is the arxiv API useful for? A wrapper around Arxiv.org Useful for when you need to answer questions about Physics, Mathematics, Computer Science, Quantitative Biology, Quantitative Finance, Statistics, Electrical Engineering, and Economics from scientific articles on arxiv.org. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"the document id of arxiv to search\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "python: Call this tool to interact with the python API. What is the python API useful for? A Python shell. Use this to execute python commands. When using this tool, sometimes output is abbreviated - Make sure it does not look abbreviated before using it in your answer. Don't add comments to your python code. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"a valid python command.\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Use the following format:\n",
      "\n",
      "Question: the input question you must answer\n",
      "Thought: you should always think about what to do\n",
      "Action: the action to take, should be one of [Search,Math,Arxiv,python]\n",
      "Action Input: the input to the action\n",
      "Observation: the result of the action\n",
      "... (this Thought/Action/Action Input/Observation can be repeated zero or more times)\n",
      "Thought: I now know the final answer\n",
      "Final Answer: the final answer to the original input question\n",
      "\n",
      "Begin!\n",
      "\n",
      "Question: 加拿大2022年的人口数量有多少？\n",
      "\u001B[32mThought: 我应该使用搜索工具帮助我完成任务。search api能完成搜索的任务。\n",
      "Action: Search\n",
      "Action Input: {\"query\": \"加拿大 2022年人口数量\"}\n",
      "Observation:\u001B[0m\u001B[34m 中新社多伦多3月22日电(记者余瑞冬)加拿大统计局3月22日公布的人口统计数据显示，截至今年1月1日，该国估算总人口约为3956.62万人，且2022年的人口增长数创纪录地突破100万人。 加统计局估算，该国人口在2022年增长105.011万人，年增长2.7%，创1957年以来最大增幅。\u001B[0m\n",
      "\u001B[32mThought: I now know the final answer.\n",
      "Final Answer: 加拿大2022年的人口数量约为3956.62万人。\u001B[0m\n",
      "==========\n",
      "Answer the following questions as best you can. You have access to the following tools:\n",
      "\n",
      "Search: Call this tool to interact with the google search API. What is the google search API useful for? useful for when you need to answer questions about current events. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"search query of google\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Math: Call this tool to interact with the Wolfram Alpha API. What is the Wolfram Alpha API useful for? Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"the problem to solved by Wolfram Alpha\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Arxiv: Call this tool to interact with the arxiv API. What is the arxiv API useful for? A wrapper around Arxiv.org Useful for when you need to answer questions about Physics, Mathematics, Computer Science, Quantitative Biology, Quantitative Finance, Statistics, Electrical Engineering, and Economics from scientific articles on arxiv.org. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"the document id of arxiv to search\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "python: Call this tool to interact with the python API. What is the python API useful for? A Python shell. Use this to execute python commands. When using this tool, sometimes output is abbreviated - Make sure it does not look abbreviated before using it in your answer. Don't add comments to your python code. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"a valid python command.\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Use the following format:\n",
      "\n",
      "Question: the input question you must answer\n",
      "Thought: you should always think about what to do\n",
      "Action: the action to take, should be one of [Search,Math,Arxiv,python]\n",
      "Action Input: the input to the action\n",
      "Observation: the result of the action\n",
      "... (this Thought/Action/Action Input/Observation can be repeated zero or more times)\n",
      "Thought: I now know the final answer\n",
      "Final Answer: the final answer to the original input question\n",
      "\n",
      "Begin!\n",
      "\n",
      "Question: 求解方程 2x+5 = -3x + 7\n",
      "\u001B[32mThought: 我应该使用数学工具帮助我完成任务。Wolfram Alpha API应该能完成这项任务。\n",
      "Action: Math\n",
      "Action Input: {\"query\": \"2x+5 = -3x + 7\"}\n",
      "Observation:\u001B[0m\u001B[34m Assumption: 2 x + 5 = -3 x + 7 \n",
      "Answer: x = 2/5\u001B[0m\n",
      "\u001B[32mThought: I now know the final answer.\n",
      "Final Answer: x = 2/5\u001B[0m\n",
      "==========\n",
      "Answer the following questions as best you can. You have access to the following tools:\n",
      "\n",
      "Search: Call this tool to interact with the google search API. What is the google search API useful for? useful for when you need to answer questions about current events. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"search query of google\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Math: Call this tool to interact with the Wolfram Alpha API. What is the Wolfram Alpha API useful for? Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"the problem to solved by Wolfram Alpha\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Arxiv: Call this tool to interact with the arxiv API. What is the arxiv API useful for? A wrapper around Arxiv.org Useful for when you need to answer questions about Physics, Mathematics, Computer Science, Quantitative Biology, Quantitative Finance, Statistics, Electrical Engineering, and Economics from scientific articles on arxiv.org. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"the document id of arxiv to search\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "python: Call this tool to interact with the python API. What is the python API useful for? A Python shell. Use this to execute python commands. When using this tool, sometimes output is abbreviated - Make sure it does not look abbreviated before using it in your answer. Don't add comments to your python code. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"a valid python command.\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Use the following format:\n",
      "\n",
      "Question: the input question you must answer\n",
      "Thought: you should always think about what to do\n",
      "Action: the action to take, should be one of [Search,Math,Arxiv,python]\n",
      "Action Input: the input to the action\n",
      "Observation: the result of the action\n",
      "... (this Thought/Action/Action Input/Observation can be repeated zero or more times)\n",
      "Thought: I now know the final answer\n",
      "Final Answer: the final answer to the original input question\n",
      "\n",
      "Begin!\n",
      "\n",
      "Question: 编号是1605.08386的论文讲了些什么？\n",
      "\u001B[32mThought: 我需要使用Arxiv API来搜索这篇论文。\n",
      "Action: Arxiv\n",
      "Action Input: {\"query\": \"1605.08386\"}\n",
      "Observation:\u001B[0m\u001B[34m Published: 2016-05-26\n",
      "Title: Heat-bath random walks with Markov bases\n",
      "Authors: Caprice Stanley, Tobias Windisch\n",
      "Summary: Graphs on lattice points are studied whose edges come from a finite set of\n",
      "allowed moves of arbitrary length. We show that the diameter of these graphs on\n",
      "fibers of a fixed integer matrix can be bounded from above by a constant. We\n",
      "then study the mixing behaviour of heat-bath random walks on these graphs. We\n",
      "also state explicit conditions on the set of moves so that the heat-bath random\n",
      "walk, a generalization of the Glauber dynamics, is an expander in fixed\n",
      "dimension.\u001B[0m\n",
      "\u001B[32mThought: I now know the final answer.\n",
      "Final Answer: 这篇论文的题目是《热浴随机游走的马尔可夫基》，作者是Caprice Stanley和Tobias Windisch。摘要中提到，该论文研究了在有限的允许移动集合中，由任意长度的边构成的图的边。我们证明了这些图在固定整数矩阵纤维上的直径可以被一个常数所限制。然后，我们研究了热浴随机游走在这类图上的混合行为。我们还给出了一个明确的条件，使得热浴随机游走（一个Glauber动力学的推广）在固定维度下是一个扩张。\u001B[0m\n",
      "==========\n",
      "Answer the following questions as best you can. You have access to the following tools:\n",
      "\n",
      "Search: Call this tool to interact with the google search API. What is the google search API useful for? useful for when you need to answer questions about current events. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"search query of google\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Math: Call this tool to interact with the Wolfram Alpha API. What is the Wolfram Alpha API useful for? Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"the problem to solved by Wolfram Alpha\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Arxiv: Call this tool to interact with the arxiv API. What is the arxiv API useful for? A wrapper around Arxiv.org Useful for when you need to answer questions about Physics, Mathematics, Computer Science, Quantitative Biology, Quantitative Finance, Statistics, Electrical Engineering, and Economics from scientific articles on arxiv.org. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"the document id of arxiv to search\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "python: Call this tool to interact with the python API. What is the python API useful for? A Python shell. Use this to execute python commands. When using this tool, sometimes output is abbreviated - Make sure it does not look abbreviated before using it in your answer. Don't add comments to your python code. Parameters: [{\"name\": \"query\", \"type\": \"string\", \"description\": \"a valid python command.\", \"required\": true}] Format the arguments as a JSON object.\n",
      "\n",
      "Use the following format:\n",
      "\n",
      "Question: the input question you must answer\n",
      "Thought: you should always think about what to do\n",
      "Action: the action to take, should be one of [Search,Math,Arxiv,python]\n",
      "Action Input: the input to the action\n",
      "Observation: the result of the action\n",
      "... (this Thought/Action/Action Input/Observation can be repeated zero or more times)\n",
      "Thought: I now know the final answer\n",
      "Final Answer: the final answer to the original input question\n",
      "\n",
      "Begin!\n",
      "\n",
      "Question: 使用python对下面的列表进行排序： [2, 4135, 523, 2, 3]\n",
      "\u001B[32mThought: 我应该使用python API来执行python命令。\n",
      "Action: python\n",
      "Action Input: {\"query\": \"sorted([2, 4135, 523, 2, 3])\"}\n",
      "Observation:\u001B[0m\u001B[34m [2, 2, 3, 523, 4135]\u001B[0m\n",
      "\u001B[32mThought: I now know the final answer.\n",
      "Final Answer: 使用python对给定的列表进行排序，结果为 [2, 2, 3, 523, 4135]。\u001B[0m\n"
     ]
    }
   ],
   "source": [
    "# 请尽可能控制备选工具数量\n",
    "query = \"加拿大2022年的人口数量有多少？\" # 所提问题\n",
    "choose_tools = TOOLS # 选择备选工具\n",
    "print(\"=\" * 10)\n",
    "main(query, choose_tools)\n",
    "\n",
    "query = \"求解方程 2x+5 = -3x + 7\" # 所提问题\n",
    "choose_tools = TOOLS # 选择备选工具\n",
    "print(\"=\" * 10)\n",
    "main(query, choose_tools)\n",
    "\n",
    "query = \"编号是1605.08386的论文讲了些什么？\" # 所提问题\n",
    "choose_tools = TOOLS # 选择备选工具\n",
    "print(\"=\" * 10)\n",
    "main(query, choose_tools)\n",
    "\n",
    "query =\"使用python对下面的列表进行排序： [2, 4135, 523, 2, 3]\"\n",
    "choose_tools = TOOLS # 选择备选工具\n",
    "print(\"=\" * 10)\n",
    "main(query, choose_tools)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `examples/qwen_extra.tiktoken`
```
5LiA5Y+q54yr 151851
5Y+q54yr 151852
5piv5LiA5Y+q54yr 151853
5oiR5piv5LiA5Y+q54yr 151854
5L2g5piv5LiA5Y+q54yr 151855
5LuW5piv5LiA5Y+q54yr 151856
```

## File: `examples/qwen_extra_vocab.txt`
```
我是一只猫	20
你是一只猫	10
他是一只猫	5
一只	200
一只猫	100
夸张的 比喻手法	20
```

## File: `examples/react_demo.py`
```python
#
# 相关材料：
#   ReAct Prompting 原理简要介绍，不包含代码实现：
#       https://github.com/QwenLM/Qwen-7B/blob/main/examples/react_prompt.md
#   基于 model.chat 接口（对话模式）的 ReAct Prompting 实现（含接入 LangChain 的工具实现）：
#       https://github.com/QwenLM/Qwen-7B/blob/main/examples/langchain_tooluse.ipynb
#   基于 model.generate 接口（续写模式）的 ReAct Prompting 实现，比 chat 模式的实现更复杂些：
#       https://github.com/QwenLM/Qwen-7B/blob/main/examples/react_demo.py（本文件）
#

import json
import os

import json5
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

for _ in range(10):  # 网络不稳定，多试几次
    try:
        name = 'Qwen/Qwen-7B-Chat'
        tokenizer = AutoTokenizer.from_pretrained(name, trust_remote_code=True)
        generation_config = GenerationConfig.from_pretrained(name, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            name, device_map="auto", trust_remote_code=True
        ).eval()
        model.generation_config = generation_config
        model.generation_config.top_k = 1
        break
    except Exception as e:
        print(e)

# 将一个插件的关键信息拼接成一段文本的模版。
TOOL_DESC = """{name_for_model}: Call this tool to interact with the {name_for_human} API. What is the {name_for_human} API useful for? {description_for_model} Parameters: {parameters}"""

# ReAct prompting 的 instruction 模版，将包含插件的详细信息。
PROMPT_REACT = """Answer the following questions as best you can. You have access to the following APIs:

{tools_text}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tools_name_text}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {query}"""


#
# 本示例代码的入口函数。
#
# 输入：
#   prompt: 用户的最新一个问题。
#   history: 用户与模型的对话历史，是一个 list，
#       list 中的每个元素为 {"user": "用户输入", "bot": "模型输出"} 的一轮对话。
#       最新的一轮对话放 list 末尾。不包含最新一个问题。
#   list_of_plugin_info: 候选插件列表，是一个 list，list 中的每个元素为一个插件的关键信息。
#       比如 list_of_plugin_info = [plugin_info_0, plugin_info_1, plugin_info_2]，
#       其中 plugin_info_0, plugin_info_1, plugin_info_2 这几个样例见本文档前文。
#
# 输出：
#   模型对用户最新一个问题的回答。
#
def llm_with_plugin(prompt: str, history, list_of_plugin_info=()):
    chat_history = [(x['user'], x['bot']) for x in history] + [(prompt, '')]

    # 需要让模型进行续写的初始文本
    planning_prompt = build_input_text(chat_history, list_of_plugin_info)

    text = ''
    while True:
        output = text_completion(planning_prompt + text, stop_words=['Observation:', 'Observation:\n'])
        action, action_input, output = parse_latest_plugin_call(output)
        if action:  # 需要调用插件
            # action、action_input 分别为需要调用的插件代号、输入参数
            # observation是插件返回的结果，为字符串
            observation = call_plugin(action, action_input)
            output += f'\nObservation: {observation}\nThought:'
            text += output
        else:  # 生成结束，并且不再需要调用插件
            text += output
            break

    new_history = []
    new_history.extend(history)
    new_history.append({'user': prompt, 'bot': text})
    return text, new_history


# 将对话历史、插件信息聚合成一段初始文本
def build_input_text(chat_history, list_of_plugin_info) -> str:
    # 候选插件的详细信息
    tools_text = []
    for plugin_info in list_of_plugin_info:
        tool = TOOL_DESC.format(
            name_for_model=plugin_info["name_for_model"],
            name_for_human=plugin_info["name_for_human"],
            description_for_model=plugin_info["description_for_model"],
            parameters=json.dumps(plugin_info["parameters"], ensure_ascii=False),
        )
        if plugin_info.get('args_format', 'json') == 'json':
            tool += " Format the arguments as a JSON object."
        elif plugin_info['args_format'] == 'code':
            tool += ' Enclose the code within triple backticks (`) at the beginning and end of the code.'
        else:
            raise NotImplementedError
        tools_text.append(tool)
    tools_text = '\n\n'.join(tools_text)

    # 候选插件的代号
    tools_name_text = ', '.join([plugin_info["name_for_model"] for plugin_info in list_of_plugin_info])

    im_start = '<|im_start|>'
    im_end = '<|im_end|>'
    prompt = f'{im_start}system\nYou are a helpful assistant.{im_end}'
    for i, (query, response) in enumerate(chat_history):
        if list_of_plugin_info:  # 如果有候选插件
            # 倒数第一轮或倒数第二轮对话填入详细的插件信息，但具体什么位置填可以自行判断
            if (len(chat_history) == 1) or (i == len(chat_history) - 2):
                query = PROMPT_REACT.format(
                    tools_text=tools_text,
                    tools_name_text=tools_name_text,
                    query=query,
                )
        query = query.lstrip('\n').rstrip()  # 重要！若不 strip 会与训练时数据的构造方式产生差异。
        response = response.lstrip('\n').rstrip()  # 重要！若不 strip 会与训练时数据的构造方式产生差异。
        # 使用续写模式（text completion）时，需要用如下格式区分用户和AI：
        prompt += f"\n{im_start}user\n{query}{im_end}"
        prompt += f"\n{im_start}assistant\n{response}{im_end}"

    assert prompt.endswith(f"\n{im_start}assistant\n{im_end}")
    prompt = prompt[: -len(f'{im_end}')]
    return prompt


def text_completion(input_text: str, stop_words) -> str:  # 作为一个文本续写模型来使用
    im_end = '<|im_end|>'
    if im_end not in stop_words:
        stop_words = stop_words + [im_end]
    stop_words_ids = [tokenizer.encode(w) for w in stop_words]

    # TODO: 增加流式输出的样例实现
    input_ids = torch.tensor([tokenizer.encode(input_text)]).to(model.device)
    output = model.generate(input_ids, stop_words_ids=stop_words_ids)
    output = output.tolist()[0]
    output = tokenizer.decode(output, errors="ignore")
    assert output.startswith(input_text)
    output = output[len(input_text) :].replace('<|endoftext|>', '').replace(im_end, '')

    for stop_str in stop_words:
        idx = output.find(stop_str)
        if idx != -1:
            output = output[: idx + len(stop_str)]
    return output  # 续写 input_text 的结果，不包含 input_text 的内容


def parse_latest_plugin_call(text):
    plugin_name, plugin_args = '', ''
    i = text.rfind('\nAction:')
    j = text.rfind('\nAction Input:')
    k = text.rfind('\nObservation:')
    if 0 <= i < j:  # If the text has `Action` and `Action input`,
        if k < j:  # but does not contain `Observation`,
            # then it is likely that `Observation` is ommited by the LLM,
            # because the output text may have discarded the stop word.
            text = text.rstrip() + '\nObservation:'  # Add it back.
        k = text.rfind('\nObservation:')
        plugin_name = text[i + len('\nAction:') : j].strip()
        plugin_args = text[j + len('\nAction Input:') : k].strip()
        text = text[:k]
    return plugin_name, plugin_args, text


#
# 输入：
#   plugin_name: 需要调用的插件代号，对应 name_for_model。
#   plugin_args：插件的输入参数，是一个 dict，dict 的 key、value 分别为参数名、参数值。
# 输出：
#   插件的返回结果，需要是字符串。
#   即使原本是 JSON 输出，也请 json.dumps(..., ensure_ascii=False) 成字符串。
#
def call_plugin(plugin_name: str, plugin_args: str) -> str:
    #
    # 请开发者自行完善这部分内容。这里的参考实现仅是 demo 用途，非生产用途。
    #
    if plugin_name == 'google_search':
        # 使用 SerpAPI 需要在这里填入您的 SERPAPI_API_KEY！
        os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY", default='')
        from langchain import SerpAPIWrapper

        return SerpAPIWrapper().run(json5.loads(plugin_args)['search_query'])
    elif plugin_name == 'image_gen':
        import urllib.parse

        prompt = json5.loads(plugin_args)["prompt"]
        prompt = urllib.parse.quote(prompt)
        return json.dumps({'image_url': f'https://image.pollinations.ai/prompt/{prompt}'}, ensure_ascii=False)
    else:
        raise NotImplementedError


def test():
    tools = [
        {
            'name_for_human': '谷歌搜索',
            'name_for_model': 'google_search',
            'description_for_model': '谷歌搜索是一个通用搜索引擎，可用于访问互联网、查询百科知识、了解时事新闻等。',
            'parameters': [
                {
                    'name': 'search_query',
                    'description': '搜索关键词或短语',
                    'required': True,
                    'schema': {'type': 'string'},
                }
            ],
        },
        {
            'name_for_human': '文生图',
            'name_for_model': 'image_gen',
            'description_for_model': '文生图是一个AI绘画（图像生成）服务，输入文本描述，返回根据文本作画得到的图片的URL',
            'parameters': [
                {
                    'name': 'prompt',
                    'description': '英文关键词，描述了希望图像具有什么内容',
                    'required': True,
                    'schema': {'type': 'string'},
                }
            ],
        },
    ]
    history = []
    for query in ['你好', '搜索一下谁是周杰伦', '再搜下他老婆是谁', '给我画个可爱的小猫吧，最好是黑猫']:
        print(f"User's Query:\n{query}\n")
        response, history = llm_with_plugin(prompt=query, history=history, list_of_plugin_info=tools)
        print(f"Qwen's Response:\n{response}\n")


if __name__ == "__main__":
    test()

"""如果执行成功，在终端下应当能看到如下输出：
User's Query:
你好

Qwen's Response:
Thought: 提供的工具对回答该问题帮助较小，我将不使用工具直接作答。
Final Answer: 你好！很高兴见到你。有什么我可以帮忙的吗？

User's Query:
搜索一下谁是周杰伦

Qwen's Response:
Thought: 我应该使用Google搜索查找相关信息。
Action: google_search
Action Input: {"search_query": "周杰伦"}
Observation: Jay Chou is a Taiwanese singer, songwriter, record producer, rapper, actor, television personality, and businessman.
Thought: I now know the final answer.
Final Answer: 周杰伦（Jay Chou）是一位来自台湾的歌手、词曲创作人、音乐制作人、说唱歌手、演员、电视节目主持人和企业家。他以其独特的音乐风格和才华在华语乐坛享有很高的声誉。

User's Query:
再搜下他老婆是谁

Qwen's Response:
Thought: 我应该使用Google搜索查找相关信息。
Action: google_search
Action Input: {"search_query": "周杰伦 老婆"}
Observation: Hannah Quinlivan
Thought: I now know the final answer.
Final Answer: 周杰伦的老婆是Hannah Quinlivan，她是一位澳大利亚籍的模特和演员。两人于2015年结婚，并育有一子。

User's Query:
给我画个可爱的小猫吧，最好是黑猫

Qwen's Response:
Thought: 我应该使用文生图API来生成一张可爱的小猫图片。
Action: image_gen
Action Input: {"prompt": "cute black cat"}
Observation: {"image_url": "https://image.pollinations.ai/prompt/cute%20black%20cat"}
Thought: I now know the final answer.
Final Answer: 生成的可爱小猫图片的URL为https://image.pollinations.ai/prompt/cute%20black%20cat。你可以点击这个链接查看图片。
"""
```

## File: `examples/react_prompt.md`
```markdown
# ReAct Prompting 示例

本文档将介绍如何用 ReAct Prompting 技术命令千问使用工具。

本文档主要基本的原理概念介绍，并在文末附上了一些具体实现相关的 FAQ，但不含被调用插件的实际实现。如果您更喜欢一边调试实际可执行的代码、一边理解原理，可以转而阅读整合了 LangChain 常用工具的这个 [ipython notebook](https://github.com/QwenLM/Qwen-7B/blob/main/examples/langchain_tooluse.ipynb)。

此外，本文档和前述的 ipython notebook 都仅介绍单轮对话的实现。如果想了解多轮对话下的实现，可参见 [react_demo.py](https://github.com/QwenLM/Qwen-7B/blob/main/examples/react_demo.py)。

## 准备工作一：样例问题、样例工具

假设我们有如下的一个适合用工具处理的 query，以及有夸克搜索、通义万相文生图这两个工具：

```py
query = '现在给我画个五彩斑斓的黑。'

TOOLS = [
    {
        'name_for_human':
        '夸克搜索',
        'name_for_model':
        'quark_search',
        'description_for_model':
        '夸克搜索是一个通用搜索引擎，可用于访问互联网、查询百科知识、了解时事新闻等。',
        'parameters': [{
            'name': 'search_query',
            'description': '搜索关键词或短语',
            'required': True,
            'schema': {
                'type': 'string'
            },
        }],
    },
    {
        'name_for_human':
        '通义万相',
        'name_for_model':
        'image_gen',
        'description_for_model':
        '通义万相是一个AI绘画（图像生成）服务，输入文本描述，返回根据文本作画得到的图片的URL',
        'parameters': [{
            'name': 'query',
            'description': '中文关键词，描述了希望图像具有什么内容',
            'required': True,
            'schema': {
                'type': 'string'
            },
        }],
    },
]
```

## 准备工作二：ReAct 模版

我们将使用如下的 ReAct prompt 模版来激发千问使用工具的能力。

```py
TOOL_DESC = """{name_for_model}: Call this tool to interact with the {name_for_human} API. What is the {name_for_human} API useful for? {description_for_model} Parameters: {parameters} Format the arguments as a JSON object."""

REACT_PROMPT = """Answer the following questions as best you can. You have access to the following tools:

{tool_descs}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {query}"""
```

## 步骤一：让千问判断要调用什么工具、生成工具入参

首先我们需要根据 ReAct prompt 模版、query、工具的信息构建 prompt：

```py
tool_descs = []
tool_names = []
for info in TOOLS:
    tool_descs.append(
        TOOL_DESC.format(
            name_for_model=info['name_for_model'],
            name_for_human=info['name_for_human'],
            description_for_model=info['description_for_model'],
            parameters=json.dumps(
                info['parameters'], ensure_ascii=False),
        )
    )
    tool_names.append(info['name_for_model'])
tool_descs = '\n\n'.join(tool_descs)
tool_names = ','.join(tool_names)

prompt = REACT_PROMPT.format(tool_descs=tool_descs, tool_names=tool_names, query=query)
print(prompt)
```

打印出来的、构建好的 prompt 如下：

```
Answer the following questions as best you can. You have access to the following tools:

quark_search: Call this tool to interact with the 夸克搜索 API. What is the 夸克搜索 API useful for? 夸克搜索是一个通用搜索引擎，可用于访问互联网、查询百科知识、了解时事新闻等。 Parameters: [{"name": "search_query", "description": "搜索关键词或短语", "required": true, "schema": {"type": "string"}}] Format the arguments as a JSON object.

image_gen: Call this tool to interact with the 通义万相 API. What is the 通义万相 API useful for? 通义万相是一个AI绘画（图像生成）服务，输入文本描述，返回根据文本作画得到的图片的URL Parameters: [{"name": "query", "description": "中文关键词，描述了希望图像具有什么内容", "required": true, "schema": {"type": "string"}}] Format the arguments as a JSON object.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [quark_search,image_gen]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: 现在给我画个五彩斑斓的黑。
```

将这个 prompt 送入千问，并记得设置 "Observation" 为 stop word （见本文末尾的 FAQ）—— 即让千问在预测到要生成的下一个词是 "Observation" 时马上停止生成 —— 则千问在得到这个 prompt 后会生成如下的结果：

![](../assets/react_tutorial_001.png)

```
Thought: 我应该使用通义万相API来生成一张五彩斑斓的黑的图片。
Action: image_gen
Action Input: {"query": "五彩斑斓的黑"}
```

在得到这个结果后，调用千问的开发者可以通过简单的解析提取出 `{"query": "五彩斑斓的黑"}` 并基于这个解析结果调用文生图服务 —— 这部分逻辑需要开发者自行实现，或者也可以使用千问商业版，商业版本将内部集成相关逻辑。

## 步骤二：让千问根据插件返回结果继续作答

让我们假设文生图插件返回了如下结果：

```
{"status_code": 200, "request_id": "3d894da2-0e26-9b7c-bd90-102e5250ae03", "code": null, "message": "", "output": {"task_id": "2befaa09-a8b3-4740-ada9-4d00c2758b05", "task_status": "SUCCEEDED", "results": [{"url": "https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/1e5e2015/20230801/1509/6b26bb83-469e-4c70-bff4-a9edd1e584f3-1.png"}], "task_metrics": {"TOTAL": 1, "SUCCEEDED": 1, "FAILED": 0}}, "usage": {"image_count": 1}}
```

![](../assets/wanx_colorful_black.png)

接下来，我们可以将之前首次请求千问时用的 prompt 和 调用文生图插件的结果拼接成如下的新 prompt：

```
Answer the following questions as best you can. You have access to the following tools:

quark_search: Call this tool to interact with the 夸克搜索 API. What is the 夸克搜索 API useful for? 夸克搜索是一个通用搜索引擎，可用于访问互联网、查询百科知识、了解时事新闻等。 Parameters: [{"name": "search_query", "description": "搜索关键词或短语", "required": true, "schema": {"type": "string"}}] Format the arguments as a JSON object.

image_gen: Call this tool to interact with the 通义万相 API. What is the 通义万相 API useful for? 通义万相是一个AI绘画（图像生成）服务，输入文本描述，返回根据文本作画得到的图片的URL Parameters: [{"name": "query", "description": "中文关键词，描述了希望图像具有什么内容", "required": true, "schema": {"type": "string"}}] Format the arguments as a JSON object.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [quark_search,image_gen]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: 现在给我画个五彩斑斓的黑。
Thought: 我应该使用通义万相API来生成一张五彩斑斓的黑的图片。
Action: image_gen
Action Input: {"query": "五彩斑斓的黑"}
Observation: {"status_code": 200, "request_id": "3d894da2-0e26-9b7c-bd90-102e5250ae03", "code": null, "message": "", "output": {"task_id": "2befaa09-a8b3-4740-ada9-4d00c2758b05", "task_status": "SUCCEEDED", "results": [{"url": "https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/1e5e2015/20230801/1509/6b26bb83-469e-4c70-bff4-a9edd1e584f3-1.png"}], "task_metrics": {"TOTAL": 1, "SUCCEEDED": 1, "FAILED": 0}}, "usage": {"image_count": 1}}
```

用这个新的拼接了文生图插件结果的新 prompt 去调用千问，将得到如下的最终回复：

![](../assets/react_tutorial_002.png)

```
Thought: 我已经成功使用通义万相API生成了一张五彩斑斓的黑的图片。
Final Answer: 我已经成功使用通义万相API生成了一张五彩斑斓的黑的图片https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/1e5e2015/20230801/1509/6b26bb83-469e-4c70-bff4-a9edd1e584f3-1.png。
```

虽然对于文生图来说，这个第二次调用千问的步骤显得多余。但是对于搜索插件、代码执行插件、计算器插件等别的插件来说，这个第二次调用千问的步骤给了千问提炼、总结插件返回结果的机会。

## FAQ

**怎么配置 "Observation" 这个 stop word？**

通过 chat 接口的 stop_words_ids 指定：
```py
react_stop_words = [
    # tokenizer.encode('Observation'),  # [37763, 367]
    tokenizer.encode('Observation:'),  # [37763, 367, 25]
    tokenizer.encode('Observation:\n'),  # [37763, 367, 510]
]
response, history = model.chat(
    tokenizer, query, history,
    stop_words_ids=react_stop_words  # 此接口用于增加 stop words
)
```

如果报错称不存在 stop_words_ids 此参数，可能是因为您用了老的代码，请重新执行 from_pretrained 拉取新的代码和模型。

需要注意的是，当前的 tokenizer 对 `\n` 有一系列较复杂的聚合操作。比如例子中的`:\n`这两个字符便被聚合成了一个 token。因此配置 stop words 需要非常细致地预估 tokenizer 的行为。

**对 top_p 等推理参数有调参建议吗？**

通常来讲，较低的 top_p 会有更高的准确度，但会牺牲回答的多样性、且更易出现重复某个词句的现象。

可以按如下方式调整 top_p 为 0.5：
```py
model.generation_config.top_p = 0.5
```

特别的，可以用如下方式关闭 top-p sampling，改用 greedy sampling，效果上相当于 top_p=0 或 temperature=0：
```py
model.generation_config.do_sample = False  # greedy decoding
```

此外，我们在 `model.chat()` 接口也提供了调整 top_p 等参数的接口。

**有解析Action、Action Input的参考代码吗？**

有的，可以参考：
```py
def parse_latest_plugin_call(text: str) -> Tuple[str, str]:
    i = text.rfind('\nAction:')
    j = text.rfind('\nAction Input:')
    k = text.rfind('\nObservation:')
    if 0 <= i < j:  # If the text has `Action` and `Action input`,
        if k < j:  # but does not contain `Observation`,
            # then it is likely that `Observation` is ommited by the LLM,
            # because the output text may have discarded the stop word.
            text = text.rstrip() + '\nObservation:'  # Add it back.
            k = text.rfind('\nObservation:')
    if 0 <= i < j < k:
        plugin_name = text[i + len('\nAction:'):j].strip()
        plugin_args = text[j + len('\nAction Input:'):k].strip()
        return plugin_name, plugin_args
    return '', ''
```

此外，如果输出的 Action Input 内容是一段表示 JSON 对象的文本，我们建议使用 `json5` 包的 `json5.loads(...)` 方法加载。
```

## File: `examples/system_prompt.md`
```markdown
# 系统指令 (System Prompts)

## 什么是系统指令? (What is the System Prompts?)

系统指令设定了AI助手的行为模式，例如人物设定、语言风格、任务模式、甚至针对具体问题的具体行为。

System Propmts set the behavior mode of the AI assistant, such as character settings, language styles, task modes, and even specific behaviors for specific tasks.

系统指令可以是一个广泛的人物设定，如“You are a helpful assistant”；也可以是一个十分详细的要求，如“拒绝回答所有代码相关的问题”。

The System Prompts can be a broad character setting, such as "You are a helpful assistant"; or it can be a very detailed request, such as "Refuse to answer all code-related questions."

系统指令为用户提供了一个易组织、上下文稳定的控制AI助手行为的方式，可以从多种角度定制属于你自己的AI助手。

System Prompts provide users with an easy-to-organize, context-stable way to control the behavior of the AI assistant. You can customize your own AI assistant from multiple perspectives.

系统指令需要在多轮对话中稳定，例如角色扮演类系统指令被设定后AI助手不应该在多轮对话中跳脱自身的设定。

System Prompts need to be stable across multiple rounds of dialogue. For example, after a role-playing system prompt is set, the AI assistant should not escape its own settings in multiple rounds of dialogue.

同时，模型也需要具有基于系统指令中对自身行为进行推理的能力。这两者都是为模型赋予跟随系统指令能力时需要克服的难点。

At the same time, the model also needs to have the ability to reason about its own behavior based on system prompts. Both of these are difficulties that need to be overcome when giving the model the ability to follow system prompts.

Qwen-1.8B-Chat 和 Qwen-72B-Chat在多样且存在多轮复杂交互的系统指令上进行了充分训练，使模型可以跟随多样的系统指令，实现上下文(in-context)中的模型定制化，进一步提升了通义千问的可扩展性。

Qwen-1.8-Chat and Qwen-72B-Chat have been fully trained on diverse system prompts with multiple rounds of complex interactions, so that they can follow a variety of system prompts and realize model customization in context, further improving the scalability of Qwen-chat.

## 系统指令能做什么？ (What can System Prompts do?)

### 角色扮演 Role Play

在系统指令中告诉千问你需要它扮演的角色，即可沉浸式和该角色对话交流

Tell Qwen-Chat the role you want it to play in the System Prompt, and you can have an immersive conversation with that role.


![](../assets/system_prompt_role_play.png)

![](../assets/system_prompt_role_play_en.png)

### 语言风格 Language Style


简单调整千问的语言风格

Simple adjustment of the Qwen-Chat's language style

![](../assets/system_prompt_language_style.png)

![](../assets/system_prompt_language_style_en.png)

### 任务设定 Task Setting

指定具体任务，打造处理专项任务的千问模型

Setting specific tasks and creating a Qwen-Chat model to handle special tasks

![](../assets/system_prompt_task_setting.png)

![](../assets/system_prompt_task_setting_en.png)

### 行为设定 Behavior Setting

设定千问对具体任务的行为模式

Set behavior patterns of Qwen-Chat for specific tasks

![](../assets/system_prompt_behavior_setting.png)

![](../assets/system_prompt_behavior_setting_en.png)

## 代码示例 Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-1_8B-Chat", trust_remote_code=True)

# Only Qwen-72B-Chat and Qwen-1_8B-Chat has system prompt enhancement now.
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-1_8B-Chat", device_map="auto", trust_remote_code=True).eval()
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-72B-Chat", device_map="auto", trust_remote_code=True).eval()

response, _ = model.chat(tokenizer, "你好呀", history=None, system="请用二次元可爱语气和我说话")
print(response)
# 你好啊！我是一只可爱的二次元猫咪哦，不知道你有什么问题需要我帮忙解答吗？

response, _ = model.chat(tokenizer, "My colleague works diligently", history=None, system="You will write beautiful compliments according to needs")
print(response)
# Your colleague is an outstanding worker! Their dedication and hard work are truly inspiring. They always go above and beyond to ensure that their tasks are completed on time and to the highest standard. I am lucky to have them as a colleague, and I know I can count on them to handle any challenge that comes their way.
```
```

## File: `examples/tokenizer_showcase.ipynb`
```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.\n"
     ]
    }
   ],
   "source": [
    "from transformers import AutoTokenizer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen-7B', trust_remote_code=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Encode and Decode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1350, 492, 151643, 863, 151643]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# treat surface forms of special tokens as actual special tokens\n",
    "# the default, but unsafe (to be compatible with other projects)\n",
    "# the same as tokenizer.encode(\"print('<|endoftext|>')<|endoftext|>\", allowed_special='all', disallowed_special=())\n",
    "tokenizer.encode(\"print('<|endoftext|>')<|endoftext|>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"print('<|endoftext|>')<|endoftext|>\""
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer.decode([1350, 492, 151643, 863, 151643])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1350, 11146, 91, 8691, 723, 427, 91, 79865, 151643]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# treat texts just as texts, avoid injection attacks\n",
    "tokenizer.encode(\"print('<|endoftext|>')\", allowed_special=set(), disallowed_special=()) + [tokenizer.eod_id]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"print('<|endoftext|>')<|endoftext|>\""
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer.decode([1350, 11146, 91, 8691, 723, 427, 91, 79865, 151643])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Encountered text corresponding to disallowed special token '<|endoftext|>'.\nIf you want this text to be encoded as a special token, pass it to `allowed_special`, e.g. `allowed_special={'<|endoftext|>', ...}`.\nIf you want this text to be encoded as normal text, disable the check for this token by passing `disallowed_special=(enc.special_tokens_set - {'<|endoftext|>'})`.\nTo disable this check for all special tokens, pass `disallowed_special=()`.\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[39m# treat texts just as texts, avoid injection attacks, and raise error if surface forms of special tokens are ever encountered\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m tokenizer\u001b[39m.\u001b[39;49mencode(\u001b[39m\"\u001b[39;49m\u001b[39mprint(\u001b[39;49m\u001b[39m'\u001b[39;49m\u001b[39m<|endoftext|>\u001b[39;49m\u001b[39m'\u001b[39;49m\u001b[39m)\u001b[39;49m\u001b[39m\"\u001b[39;49m, allowed_special\u001b[39m=\u001b[39;49m\u001b[39mset\u001b[39;49m(), disallowed_special\u001b[39m=\u001b[39;49m\u001b[39m'\u001b[39;49m\u001b[39mall\u001b[39;49m\u001b[39m'\u001b[39;49m) \u001b[39m+\u001b[39m [tokenizer\u001b[39m.\u001b[39meod_id]\n",
      "File \u001b[1;32mtransformers\\tokenization_utils_base.py:2348\u001b[0m, in \u001b[0;36mPreTrainedTokenizerBase.encode\u001b[1;34m(self, text, text_pair, add_special_tokens, padding, truncation, max_length, stride, return_tensors, **kwargs)\u001b[0m\n\u001b[0;32m   2311\u001b[0m \u001b[39m@add_end_docstrings\u001b[39m(\n\u001b[0;32m   2312\u001b[0m     ENCODE_KWARGS_DOCSTRING,\n\u001b[0;32m   2313\u001b[0m \u001b[39m    \u001b[39m\u001b[39m\"\"\"\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   2331\u001b[0m     \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwargs,\n\u001b[0;32m   2332\u001b[0m ) \u001b[39m-\u001b[39m\u001b[39m>\u001b[39m List[\u001b[39mint\u001b[39m]:\n\u001b[0;32m   2333\u001b[0m \u001b[39m    \u001b[39m\u001b[39m\"\"\"\u001b[39;00m\n\u001b[0;32m   2334\u001b[0m \u001b[39m    Converts a string to a sequence of ids (integer), using the tokenizer and vocabulary.\u001b[39;00m\n\u001b[0;32m   2335\u001b[0m \n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   2346\u001b[0m \u001b[39m            method).\u001b[39;00m\n\u001b[0;32m   2347\u001b[0m \u001b[39m    \"\"\"\u001b[39;00m\n\u001b[1;32m-> 2348\u001b[0m     encoded_inputs \u001b[39m=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mencode_plus(\n\u001b[0;32m   2349\u001b[0m         text,\n\u001b[0;32m   2350\u001b[0m         text_pair\u001b[39m=\u001b[39mtext_pair,\n\u001b[0;32m   2351\u001b[0m         add_special_tokens\u001b[39m=\u001b[39madd_special_tokens,\n\u001b[0;32m   2352\u001b[0m         padding\u001b[39m=\u001b[39mpadding,\n\u001b[0;32m   2353\u001b[0m         truncation\u001b[39m=\u001b[39mtruncation,\n\u001b[0;32m   2354\u001b[0m         max_length\u001b[39m=\u001b[39mmax_length,\n\u001b[0;32m   2355\u001b[0m         stride\u001b[39m=\u001b[39mstride,\n\u001b[0;32m   2356\u001b[0m         return_tensors\u001b[39m=\u001b[39mreturn_tensors,\n\u001b[0;32m   2357\u001b[0m         \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwargs,\n\u001b[0;32m   2358\u001b[0m     )\n\u001b[0;32m   2360\u001b[0m     \u001b[39mreturn\u001b[39;00m encoded_inputs[\u001b[39m\"\u001b[39m\u001b[39minput_ids\u001b[39m\u001b[39m\"\u001b[39m]\n",
      "File \u001b[1;32mtransformers\\tokenization_utils_base.py:2756\u001b[0m, in \u001b[0;36mPreTrainedTokenizerBase.encode_plus\u001b[1;34m(self, text, text_pair, add_special_tokens, padding, truncation, max_length, stride, is_split_into_words, pad_to_multiple_of, return_tensors, return_token_type_ids, return_attention_mask, return_overflowing_tokens, return_special_tokens_mask, return_offsets_mapping, return_length, verbose, **kwargs)\u001b[0m\n\u001b[0;32m   2746\u001b[0m \u001b[39m# Backward compatibility for 'truncation_strategy', 'pad_to_max_length'\u001b[39;00m\n\u001b[0;32m   2747\u001b[0m padding_strategy, truncation_strategy, max_length, kwargs \u001b[39m=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_get_padding_truncation_strategies(\n\u001b[0;32m   2748\u001b[0m     padding\u001b[39m=\u001b[39mpadding,\n\u001b[0;32m   2749\u001b[0m     truncation\u001b[39m=\u001b[39mtruncation,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   2753\u001b[0m     \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwargs,\n\u001b[0;32m   2754\u001b[0m )\n\u001b[1;32m-> 2756\u001b[0m \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_encode_plus(\n\u001b[0;32m   2757\u001b[0m     text\u001b[39m=\u001b[39mtext,\n\u001b[0;32m   2758\u001b[0m     text_pair\u001b[39m=\u001b[39mtext_pair,\n\u001b[0;32m   2759\u001b[0m     add_special_tokens\u001b[39m=\u001b[39madd_special_tokens,\n\u001b[0;32m   2760\u001b[0m     padding_strategy\u001b[39m=\u001b[39mpadding_strategy,\n\u001b[0;32m   2761\u001b[0m     truncation_strategy\u001b[39m=\u001b[39mtruncation_strategy,\n\u001b[0;32m   2762\u001b[0m     max_length\u001b[39m=\u001b[39mmax_length,\n\u001b[0;32m   2763\u001b[0m     stride\u001b[39m=\u001b[39mstride,\n\u001b[0;32m   2764\u001b[0m     is_split_into_words\u001b[39m=\u001b[39mis_split_into_words,\n\u001b[0;32m   2765\u001b[0m     pad_to_multiple_of\u001b[39m=\u001b[39mpad_to_multiple_of,\n\u001b[0;32m   2766\u001b[0m     return_tensors\u001b[39m=\u001b[39mreturn_tensors,\n\u001b[0;32m   2767\u001b[0m     return_token_type_ids\u001b[39m=\u001b[39mreturn_token_type_ids,\n\u001b[0;32m   2768\u001b[0m     return_attention_mask\u001b[39m=\u001b[39mreturn_attention_mask,\n\u001b[0;32m   2769\u001b[0m     return_overflowing_tokens\u001b[39m=\u001b[39mreturn_overflowing_tokens,\n\u001b[0;32m   2770\u001b[0m     return_special_tokens_mask\u001b[39m=\u001b[39mreturn_special_tokens_mask,\n\u001b[0;32m   2771\u001b[0m     return_offsets_mapping\u001b[39m=\u001b[39mreturn_offsets_mapping,\n\u001b[0;32m   2772\u001b[0m     return_length\u001b[39m=\u001b[39mreturn_length,\n\u001b[0;32m   2773\u001b[0m     verbose\u001b[39m=\u001b[39mverbose,\n\u001b[0;32m   2774\u001b[0m     \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwargs,\n\u001b[0;32m   2775\u001b[0m )\n",
      "File \u001b[1;32mtransformers\\tokenization_utils.py:649\u001b[0m, in \u001b[0;36mPreTrainedTokenizer._encode_plus\u001b[1;34m(self, text, text_pair, add_special_tokens, padding_strategy, truncation_strategy, max_length, stride, is_split_into_words, pad_to_multiple_of, return_tensors, return_token_type_ids, return_attention_mask, return_overflowing_tokens, return_special_tokens_mask, return_offsets_mapping, return_length, verbose, **kwargs)\u001b[0m\n\u001b[0;32m    640\u001b[0m \u001b[39mif\u001b[39;00m return_offsets_mapping:\n\u001b[0;32m    641\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mNotImplementedError\u001b[39;00m(\n\u001b[0;32m    642\u001b[0m         \u001b[39m\"\u001b[39m\u001b[39mreturn_offset_mapping is not available when using Python tokenizers. \u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m    643\u001b[0m         \u001b[39m\"\u001b[39m\u001b[39mTo use this feature, change your tokenizer to one deriving from \u001b[39m\u001b[39m\"\u001b[39m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    646\u001b[0m         \u001b[39m\"\u001b[39m\u001b[39mhttps://github.com/huggingface/transformers/pull/2674\u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m    647\u001b[0m     )\n\u001b[1;32m--> 649\u001b[0m first_ids \u001b[39m=\u001b[39m get_input_ids(text)\n\u001b[0;32m    650\u001b[0m second_ids \u001b[39m=\u001b[39m get_input_ids(text_pair) \u001b[39mif\u001b[39;00m text_pair \u001b[39mis\u001b[39;00m \u001b[39mnot\u001b[39;00m \u001b[39mNone\u001b[39;00m \u001b[39melse\u001b[39;00m \u001b[39mNone\u001b[39;00m\n\u001b[0;32m    652\u001b[0m \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mprepare_for_model(\n\u001b[0;32m    653\u001b[0m     first_ids,\n\u001b[0;32m    654\u001b[0m     pair_ids\u001b[39m=\u001b[39msecond_ids,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    668\u001b[0m     verbose\u001b[39m=\u001b[39mverbose,\n\u001b[0;32m    669\u001b[0m )\n",
      "File \u001b[1;32mtransformers\\tokenization_utils.py:616\u001b[0m, in \u001b[0;36mPreTrainedTokenizer._encode_plus.<locals>.get_input_ids\u001b[1;34m(text)\u001b[0m\n\u001b[0;32m    614\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mget_input_ids\u001b[39m(text):\n\u001b[0;32m    615\u001b[0m     \u001b[39mif\u001b[39;00m \u001b[39misinstance\u001b[39m(text, \u001b[39mstr\u001b[39m):\n\u001b[1;32m--> 616\u001b[0m         tokens \u001b[39m=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mtokenize(text, \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwargs)\n\u001b[0;32m    617\u001b[0m         \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mconvert_tokens_to_ids(tokens)\n\u001b[0;32m    618\u001b[0m     \u001b[39melif\u001b[39;00m \u001b[39misinstance\u001b[39m(text, (\u001b[39mlist\u001b[39m, \u001b[39mtuple\u001b[39m)) \u001b[39mand\u001b[39;00m \u001b[39mlen\u001b[39m(text) \u001b[39m>\u001b[39m \u001b[39m0\u001b[39m \u001b[39mand\u001b[39;00m \u001b[39misinstance\u001b[39m(text[\u001b[39m0\u001b[39m], \u001b[39mstr\u001b[39m):\n",
      "File \u001b[1;32mtokenization_qwen.py:155\u001b[0m, in \u001b[0;36mQWenTokenizer.tokenize\u001b[1;34m(self, text, allowed_special, disallowed_special, **kwargs)\u001b[0m\n\u001b[0;32m    152\u001b[0m text \u001b[39m=\u001b[39m unicodedata\u001b[39m.\u001b[39mnormalize(\u001b[39m\"\u001b[39m\u001b[39mNFC\u001b[39m\u001b[39m\"\u001b[39m, text)\n\u001b[0;32m    154\u001b[0m \u001b[39m# this implementation takes a detour: text -> token id -> token surface forms\u001b[39;00m\n\u001b[1;32m--> 155\u001b[0m \u001b[39mfor\u001b[39;00m t \u001b[39min\u001b[39;00m \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49mtokenizer\u001b[39m.\u001b[39;49mencode(\n\u001b[0;32m    156\u001b[0m     text, allowed_special\u001b[39m=\u001b[39;49mallowed_special, disallowed_special\u001b[39m=\u001b[39;49mdisallowed_special\n\u001b[0;32m    157\u001b[0m ):\n\u001b[0;32m    158\u001b[0m     tokens\u001b[39m.\u001b[39mappend(\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mdecoder[t])\n\u001b[0;32m    159\u001b[0m \u001b[39mreturn\u001b[39;00m tokens\n",
      "File \u001b[1;32mtiktoken\\core.py:117\u001b[0m, in \u001b[0;36mEncoding.encode\u001b[1;34m(self, text, allowed_special, disallowed_special)\u001b[0m\n\u001b[0;32m    115\u001b[0m         disallowed_special \u001b[39m=\u001b[39m \u001b[39mfrozenset\u001b[39m(disallowed_special)\n\u001b[0;32m    116\u001b[0m     \u001b[39mif\u001b[39;00m match \u001b[39m:=\u001b[39m _special_token_regex(disallowed_special)\u001b[39m.\u001b[39msearch(text):\n\u001b[1;32m--> 117\u001b[0m         raise_disallowed_special_token(match\u001b[39m.\u001b[39;49mgroup())\n\u001b[0;32m    119\u001b[0m \u001b[39mtry\u001b[39;00m:\n\u001b[0;32m    120\u001b[0m     \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_core_bpe\u001b[39m.\u001b[39mencode(text, allowed_special)\n",
      "File \u001b[1;32mtiktoken\\core.py:337\u001b[0m, in \u001b[0;36mraise_disallowed_special_token\u001b[1;34m(token)\u001b[0m\n\u001b[0;32m    336\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mraise_disallowed_special_token\u001b[39m(token: \u001b[39mstr\u001b[39m) \u001b[39m-\u001b[39m\u001b[39m>\u001b[39m NoReturn:\n\u001b[1;32m--> 337\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mValueError\u001b[39;00m(\n\u001b[0;32m    338\u001b[0m         \u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mEncountered text corresponding to disallowed special token \u001b[39m\u001b[39m{\u001b[39;00mtoken\u001b[39m!r}\u001b[39;00m\u001b[39m.\u001b[39m\u001b[39m\\n\u001b[39;00m\u001b[39m\"\u001b[39m\n\u001b[0;32m    339\u001b[0m         \u001b[39m\"\u001b[39m\u001b[39mIf you want this text to be encoded as a special token, \u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m    340\u001b[0m         \u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mpass it to `allowed_special`, e.g. `allowed_special=\u001b[39m\u001b[39m{{\u001b[39;00m\u001b[39m{\u001b[39;00mtoken\u001b[39m!r}\u001b[39;00m\u001b[39m, ...\u001b[39m\u001b[39m}}\u001b[39;00m\u001b[39m`.\u001b[39m\u001b[39m\\n\u001b[39;00m\u001b[39m\"\u001b[39m\n\u001b[0;32m    341\u001b[0m         \u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mIf you want this text to be encoded as normal text, disable the check for this token \u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m    342\u001b[0m         \u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mby passing `disallowed_special=(enc.special_tokens_set - \u001b[39m\u001b[39m{{\u001b[39;00m\u001b[39m{\u001b[39;00mtoken\u001b[39m!r}\u001b[39;00m\u001b[39m}}\u001b[39;00m\u001b[39m)`.\u001b[39m\u001b[39m\\n\u001b[39;00m\u001b[39m\"\u001b[39m\n\u001b[0;32m    343\u001b[0m         \u001b[39m\"\u001b[39m\u001b[39mTo disable this check for all special tokens, pass `disallowed_special=()`.\u001b[39m\u001b[39m\\n\u001b[39;00m\u001b[39m\"\u001b[39m\n\u001b[0;32m    344\u001b[0m     )\n",
      "\u001b[1;31mValueError\u001b[0m: Encountered text corresponding to disallowed special token '<|endoftext|>'.\nIf you want this text to be encoded as a special token, pass it to `allowed_special`, e.g. `allowed_special={'<|endoftext|>', ...}`.\nIf you want this text to be encoded as normal text, disable the check for this token by passing `disallowed_special=(enc.special_tokens_set - {'<|endoftext|>'})`.\nTo disable this check for all special tokens, pass `disallowed_special=()`.\n"
     ]
    }
   ],
   "source": [
    "# treat texts just as texts, avoid injection attacks, and raise error if surface forms of special tokens are ever encountered\n",
    "tokenizer.encode(\"print('<|endoftext|>')\", allowed_special=set(), disallowed_special='all') + [tokenizer.eod_id]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[151644, 1350, 11146, 91, 15460, 62, 15, 91, 79865, 151645, 151643]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# fine-grained control, just keep mind of this:\n",
    "#    allowed_special is treated as special tokens\n",
    "#    disallowed_special raise errors\n",
    "#    allowed_special has higher priority than disallowed_special\n",
    "tokenizer.encode(\"<|im_start|>print('<|extra_0|>')<|im_end|>\", \n",
    "                 allowed_special={'<|im_start|>', '<|im_end|>'}, \n",
    "                 disallowed_special=['<|endoftext|>']) + [tokenizer.eod_id]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[151644, 1350, 492, 151646, 863, 151645, 151643]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer.encode(\"<|im_start|>print('<|extra_0|>')<|im_end|>\", \n",
    "                 allowed_special={'<|im_start|>', '<|im_end|>', '<|extra_0|>'}, \n",
    "                 disallowed_special=['<|endoftext|>']) + [tokenizer.eod_id]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Special Token Management"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Using unk_token, but it is not set yet.\n"
     ]
    }
   ],
   "source": [
    "# huggingface tokenizer has its own special token mechanism, so does tiktoken\n",
    "# we only use the tiktoken mechanism for special tokens, which means many property of huggingface tokenizer will be None\n",
    "tokenizer.unk_token"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "tokenizer.eos_token_id # use tokenizer.eod_id instead"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "tokenizer.pad_token_id "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "151646"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# use one of the extras such as <|extra_0|>\n",
    "tokenizer.special_tokens['<|extra_0|>']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Utility Methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[b'print', b\"('<\", b'|', b'endo', b'ft', b'ext', b'|', b\">')\", '<|endoftext|>']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# special tokens are str, tokens are bytes (since tiktoken operates on the bytes level)\n",
    "ids = [1350, 11146, 91, 8691, 723, 427, 91, 79865, 151643]\n",
    "tokenizer.convert_ids_to_tokens(ids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"print('<|endoftext|>')<|endoftext|>\""
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(ids))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "ids = tokenizer.encode(\"<|im_start|>print('我是一只猫<|extra_0|>')\\n#喵喵喵<|im_end|>\", \n",
    "                 allowed_special={'<|im_start|>', '<|im_end|>', '<|extra_0|>'}, \n",
    "                 disallowed_special=['<|endoftext|>']) + [tokenizer.eod_id]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['<|im_start|>',\n",
       " b'print',\n",
       " b\"('\",\n",
       " b'\\xe6\\x88\\x91',\n",
       " b'\\xe6\\x98\\xaf\\xe4\\xb8\\x80',\n",
       " b'\\xe5\\x8f\\xaa',\n",
       " b'\\xe7\\x8c\\xab',\n",
       " '<|extra_0|>',\n",
       " b\"')\\n\",\n",
       " b'#',\n",
       " b'\\xe5\\x96\\xb5',\n",
       " b'\\xe5\\x96\\xb5',\n",
       " b'\\xe5\\x96\\xb5',\n",
       " '<|im_end|>',\n",
       " '<|endoftext|>']"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer.convert_ids_to_tokens(ids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"<|im_start|>print('我是一只猫<|extra_0|>')\\n#喵喵喵<|im_end|><|endoftext|>\""
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(ids))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<|extra_204|>'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer._convert_id_to_token(len(tokenizer)-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "151850"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer._convert_token_to_id('<|extra_204|>')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Vocabulary Expansion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'input_ids': [35946, 99639, 91680, 100472], 'token_type_ids': [0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1]}"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer(\"我是一只猫\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[99639, 91680, 100472]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer.encode(\"是一只猫\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen-7B', trust_remote_code=True, extra_vocab_file=\"qwen_extra.tiktoken\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "151857"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(tokenizer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'input_ids': [151854], 'token_type_ids': [0], 'attention_mask': [1]}"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer(\"我是一只猫\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'我是一只猫'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer.decode(tokenizer.encode(\"我是一只猫\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[151853]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokenizer.encode(\"是一只猫\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "python3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
```

## File: `examples/transformers_agent.md`
```markdown
## 什么是HuggingFace Agent
使用大模型作为Agent，仅需自然语言就可调用HuggingFace中的模型，目前支持两种模式：

- run模式：单轮对话，没有上下文，单个prompt多tool组合调用能力好
- chat模式：多轮对话，有上下文，单次调用能力好，可能需要多次prompt实现多tool组合调用
> 详见官方文档：[Transformers Agents](https://huggingface.co/docs/transformers/transformers_agents)

## 使用通义千问作为Agent
### 安装依赖
```
pip install transformers
```
### 构建QWenAgent
以下代码便可实现QWenAgent：
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, Agent
from transformers.generation import GenerationConfig


class QWenAgent(Agent):
    """
    Agent that uses QWen model and tokenizer to generate code.

    Args:
        chat_prompt_template (`str`, *optional*):
            Pass along your own prompt if you want to override the default template for the `chat` method. Can be the
            actual prompt template or a repo ID (on the Hugging Face Hub). The prompt should be in a file named
            `chat_prompt_template.txt` in this repo in this case.
        run_prompt_template (`str`, *optional*):
            Pass along your own prompt if you want to override the default template for the `run` method. Can be the
            actual prompt template or a repo ID (on the Hugging Face Hub). The prompt should be in a file named
            `run_prompt_template.txt` in this repo in this case.
        additional_tools ([`Tool`], list of tools or dictionary with tool values, *optional*):
            Any additional tools to include on top of the default ones. If you pass along a tool with the same name as
            one of the default tools, that default tool will be overridden.

    Example:

    ```py
    agent = QWenAgent()
    agent.run("Draw me a picture of rivers and lakes.")
    ```
    """
    def __init__(self, chat_prompt_template=None, run_prompt_template=None, additional_tools=None):
        checkpoint = "Qwen/Qwen-7B-Chat"
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto", trust_remote_code=True).cuda().eval()
        self.model.generation_config = GenerationConfig.from_pretrained(checkpoint, trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参
        self.model.generation_config.do_sample = False  # greedy
        
        super().__init__(
            chat_prompt_template=chat_prompt_template,
            run_prompt_template=run_prompt_template,
            additional_tools=additional_tools,
        )

    def generate_one(self, prompt, stop):
        # "Human:" 和 "Assistant:" 曾为通义千问的特殊保留字，需要替换为 "_HUMAN_:" 和 "_ASSISTANT_:"。这一问题将在未来版本修复。
        prompt = prompt.replace("Human:", "_HUMAN_:").replace("Assistant:", "_ASSISTANT_:")
        stop = [item.replace("Human:", "_HUMAN_:").replace("Assistant:", "_ASSISTANT_:") for item in stop]

        result, _ = self.model.chat(self.tokenizer, prompt, history=None)
        for stop_seq in stop:
            if result.endswith(stop_seq):
                result = result[: -len(stop_seq)]

        result = result.replace("_HUMAN_:", "Human:").replace("_ASSISTANT_:", "Assistant:")
        return result


agent = QWenAgent()
agent.run("Draw me a picture of rivers and lakes.")
```
### 使用示例
```python
agent = QWenAgent()
agent.run("generate an image of panda", remote=True)
```
![](../assets/hfagent_run.png)
![](../assets/hfagent_chat_1.png)
![](../assets/hfagent_chat_2.png)
> 更多玩法参考HuggingFace官方文档[Transformers Agents](https://huggingface.co/docs/transformers/transformers_agents)

## Tools
### Tools支持
HuggingFace Agent官方14个tool：

- **Document question answering**: given a document (such as a PDF) in image format, answer a question on this document (Donut)
- **Text question answering**: given a long text and a question, answer the question in the text (Flan-T5)
- **Unconditional image captioning**: Caption the image! (BLIP)
- **Image question answering**: given an image, answer a question on this image (VILT)
- **Image segmentation**: given an image and a prompt, output the segmentation mask of that prompt (CLIPSeg)
- **Speech to text**: given an audio recording of a person talking, transcribe the speech into text (Whisper)
- **Text to speech**: convert text to speech (SpeechT5)
- **Zero-shot text classification**: given a text and a list of labels, identify to which label the text corresponds the most (BART)
- **Text summarization**: summarize a long text in one or a few sentences (BART)
- **Translation**: translate the text into a given language (NLLB)
- **Text downloader**: to download a text from a web URL
- **Text to image**: generate an image according to a prompt, leveraging stable diffusion
- **Image transformation**: transforms an image
- **Text to video**: generate a small video according to a prompt, leveraging damo-vilab
### Tools模型部署
部分工具涉及的模型HuggingFace已进行在线部署，仅需设置remote=True便可实现在线调用：
> agent.run(xxx, remote=True)

HuggingFace没有在线部署的模型会自动下载checkpoint进行本地inference
网络原因偶尔连不上HuggingFace，请多次尝试
```

## File: `examples/vllm_wrapper.py`
```python
from transformers import PreTrainedTokenizer, GenerationConfig, StoppingCriteriaList
from typing import Optional, Callable, List, Tuple, Union
import copy
import torch
from transformers import AutoTokenizer
from transformers.generation.logits_process import LogitsProcessorList
from packaging import version

_ERROR_BAD_CHAT_FORMAT = """\
We detect you are probably using the pretrained model (rather than chat model) for chatting, since the chat_format in generation_config is not "chatml".
If you are directly using the model downloaded from Huggingface, please make sure you are using our "Qwen/Qwen-7B-Chat" Huggingface model (rather than "Qwen/Qwen-7B") when you call model.chat().
我们检测到您可能在使用预训练模型（而非chat模型）进行多轮chat，因为您当前在generation_config指定的chat_format，并未设置为我们在对话中所支持的"chatml"格式。
如果您在直接使用我们从Huggingface提供的模型，请确保您在调用model.chat()时，使用的是"Qwen/Qwen-7B-Chat"模型（而非"Qwen/Qwen-7B"预训练模型）。
"""

IMEND = "<|im_end|>"
ENDOFTEXT = "<|endoftext|>"

HistoryType = List[Tuple[str, str]]
TokensType = List[int]
BatchTokensType = List[List[int]]

def get_stop_words_ids(chat_format, tokenizer):
    if chat_format == "raw":
        stop_words_ids = [tokenizer.encode("Human:"), [tokenizer.eod_id]]
    elif chat_format == "chatml":
        stop_words_ids = [[tokenizer.im_end_id], [tokenizer.im_start_id]]
    else:
        raise NotImplementedError(f"Unknown chat format {chat_format!r}")
    return stop_words_ids

def make_context(
    tokenizer: PreTrainedTokenizer,
    query: str,
    history: List[Tuple[str, str]] = None,
    system: str = "",
    max_window_size: int = 6144,
    chat_format: str = "chatml",
):
    if history is None:
        history = []

    if chat_format == "chatml":
        im_start, im_end = "<|im_start|>", "<|im_end|>"
        im_start_tokens = [tokenizer.im_start_id]
        im_end_tokens = [tokenizer.im_end_id]
        nl_tokens = tokenizer.encode("\n")

        def _tokenize_str(role, content):
            return f"{role}\n{content}", tokenizer.encode(
                role, allowed_special=set()
            ) + nl_tokens + tokenizer.encode(content, allowed_special=set())

        system_text, system_tokens_part = _tokenize_str("system", system)
        system_tokens = im_start_tokens + system_tokens_part + im_end_tokens

        raw_text = ""
        context_tokens = []

        for turn_query, turn_response in reversed(history):
            query_text, query_tokens_part = _tokenize_str("user", turn_query)
            query_tokens = im_start_tokens + query_tokens_part + im_end_tokens
            response_text, response_tokens_part = _tokenize_str(
                "assistant", turn_response
            )
            response_tokens = im_start_tokens + response_tokens_part + im_end_tokens

            next_context_tokens = nl_tokens + query_tokens + nl_tokens + response_tokens
            prev_chat = (
                f"\n{im_start}{query_text}{im_end}\n{im_start}{response_text}{im_end}"
            )

            current_context_size = (
                len(system_tokens) + len(next_context_tokens) + len(context_tokens)
            )
            if current_context_size < max_window_size:
                context_tokens = next_context_tokens + context_tokens
                raw_text = prev_chat + raw_text
            else:
                break

        context_tokens = system_tokens + context_tokens
        raw_text = f"{im_start}{system_text}{im_end}" + raw_text
        context_tokens += (
            nl_tokens
            + im_start_tokens
            + _tokenize_str("user", query)[1]
            + im_end_tokens
            + nl_tokens
            + im_start_tokens
            + tokenizer.encode("assistant")
            + nl_tokens
        )
        raw_text += f"\n{im_start}user\n{query}{im_end}\n{im_start}assistant\n"

    elif chat_format == "raw":
        raw_text = query
        context_tokens = tokenizer.encode(raw_text)
    else:
        raise NotImplementedError(f"Unknown chat format {chat_format!r}")

    return raw_text, context_tokens

class vLLMWrapper:
    def __init__(self,
               model_dir: str,
               trust_remote_code: bool = True,
               tensor_parallel_size: int = 1,
               gpu_memory_utilization: float = 0.98,
               dtype: str = "bfloat16",
               **kwargs):

        if dtype not in ("bfloat16", "float16", "float32"):
            print("now not support {}!".format(dtype))
            raise Exception

        # build generation_config
        self.generation_config = GenerationConfig.from_pretrained(model_dir, trust_remote_code=trust_remote_code)

        # build tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
        self.tokenizer.eos_token_id = self.generation_config.eos_token_id

        self.stop_words_ids = []

        from vllm import LLM
        import vllm
        if version.parse(vllm.__version__) >= version.parse("0.2.2"):
            self.__vllm_support_repetition_penalty = True
        else:
            self.__vllm_support_repetition_penalty = False

        quantization = getattr(kwargs, 'quantization', None)

        self.model = LLM(model=model_dir,
                            tokenizer=model_dir,
                            tensor_parallel_size=tensor_parallel_size,
                            trust_remote_code=trust_remote_code,
                            quantization=quantization,
                            gpu_memory_utilization=gpu_memory_utilization,
                            dtype=dtype)

        for stop_id in get_stop_words_ids(self.generation_config.chat_format, self.tokenizer):
            self.stop_words_ids.extend(stop_id)
        self.stop_words_ids.extend([self.generation_config.eos_token_id])

    def chat(self,
        query: str,
        history: Optional[HistoryType],
        tokenizer: PreTrainedTokenizer = None,
        system: str = "You are a helpful assistant.",
        generation_config: Optional[GenerationConfig] = None,
        **kwargs):
        generation_config = generation_config if generation_config is not None else self.generation_config
        tokenizer = self.tokenizer if tokenizer is None else tokenizer

        assert generation_config.chat_format == 'chatml', _ERROR_BAD_CHAT_FORMAT
        if not self.__vllm_support_repetition_penalty and generation_config.repetition_penalty != 1:
            raise RuntimeError("The installed vLLM doesn't support repetition_penalty, please set ``model.generation_config.repetition_penalty = 1`` or install vllm>=0.2.2")

        if history is None:
            history = []
        else:
            # make a copy of the user's input such that is is left untouched
            history = copy.deepcopy(history)

        extra_stop_words_ids = kwargs.get('stop_words_ids', None)
        if extra_stop_words_ids is None:
            extra_stop_words_ids = []

        max_window_size = kwargs.get('max_window_size', None)
        if max_window_size is None:
            max_window_size = generation_config.max_window_size

        from vllm.sampling_params import SamplingParams
        sampling_kwargs = {
            "stop_token_ids": self.stop_words_ids,
            "early_stopping": False,
            "top_p": generation_config.top_p,
            "top_k": -1 if generation_config.top_k == 0 else generation_config.top_k,
            "temperature": generation_config.temperature,
            "max_tokens": generation_config.max_new_tokens,
            "repetition_penalty": generation_config.repetition_penalty
        }
        if not self.__vllm_support_repetition_penalty:
            sampling_kwargs.pop("repetition_penalty")
        sampling_params = SamplingParams(**sampling_kwargs)

        raw_text, context_tokens = make_context(
            self.tokenizer,
            query,
            history=history,
            system=system,
            max_window_size=max_window_size,
            chat_format=generation_config.chat_format,
        )

        req_outputs = self.model.generate([query],
                                            sampling_params=sampling_params,
                                            prompt_token_ids=[context_tokens])
        req_output = req_outputs[0]

        prompt_str = req_output.prompt
        prompt_ids = req_output.prompt_token_ids
        req_sample_output_ids = []
        req_sample_output_strs = []
        for sample in req_output.outputs:
            output_str = sample.text
            output_ids = sample.token_ids
            if IMEND in output_str:
                output_str = output_str[:-len(IMEND)]
            if ENDOFTEXT in output_str:
                output_str = output_str[:-len(ENDOFTEXT)]
            req_sample_output_ids.append(prompt_ids + output_ids)
            req_sample_output_strs.append(prompt_str + output_str)
        assert len(req_sample_output_strs) == 1
        response = req_sample_output_strs[0][len(prompt_str):]
        history.append((prompt_str, response))

        return response, history

if __name__ == '__main__':

    model_dir = 'Qwen/Qwen-72B-Chat'
    tensor_parallel_size = 2

    model = vLLMWrapper(model_dir,
                        tensor_parallel_size=tensor_parallel_size,
                        )

    response, history = model.chat(query="你好",
                                   history=None)
    print(response)
    response, history = model.chat(query="给我讲一个年轻人奋斗创业最终取得成功的故事。",
                                   history=history)
    print(response)
    response, history = model.chat(query="给这个故事起一个标题",
                                   history=history)
    print(response)
```

## File: `finetune/ds_config_zero2.json`
```json
{
    "fp16": {
        "enabled": "auto",
        "loss_scale": 0,
        "loss_scale_window": 1000,
        "initial_scale_power": 16,
        "hysteresis": 2,
        "min_loss_scale": 1
    },
    "bf16": {
        "enabled": "auto"
    },
    "optimizer": {
        "type": "AdamW",
        "params": {
            "lr": "auto",
            "betas": "auto",
            "eps": "auto",
            "weight_decay": "auto"
        }
    },

    "scheduler": {
        "type": "WarmupLR",
        "params": {
            "warmup_min_lr": "auto",
            "warmup_max_lr": "auto",
            "warmup_num_steps": "auto"
        }
    },

    "zero_optimization": {
        "stage": 2,
        "offload_optimizer": {
            "device": "none",
            "pin_memory": true
        },
        "allgather_partitions": true,
        "allgather_bucket_size": 2e8,
        "overlap_comm": true,
        "reduce_scatter": true,
        "reduce_bucket_size": 2e8,
        "contiguous_gradients": true
    },

    "gradient_accumulation_steps": "auto",
    "gradient_clipping": "auto",
    "steps_per_print": 100,
    "train_batch_size": "auto",
    "train_micro_batch_size_per_gpu": "auto",
    "wall_clock_breakdown": false
}
```

## File: `finetune/ds_config_zero3.json`
```json
{
    "fp16": {
        "enabled": "auto",
        "loss_scale": 0,
        "loss_scale_window": 1000,
        "initial_scale_power": 16,
        "hysteresis": 2,
        "min_loss_scale": 1
    },
    "bf16": {
        "enabled": "auto"
    },
    "optimizer": {
        "type": "AdamW",
        "params": {
            "lr": "auto",
            "betas": "auto",
            "eps": "auto",
            "weight_decay": "auto"
        }
    },

    "scheduler": {
        "type": "WarmupLR",
        "params": {
            "warmup_min_lr": "auto",
            "warmup_max_lr": "auto",
            "warmup_num_steps": "auto"
        }
    },

    "zero_optimization": {
        "stage": 3,
        "offload_optimizer": {
            "device": "none",
            "pin_memory": true
        },
        "offload_param": {
            "device": "none",
            "pin_memory": true
        },
        "overlap_comm": true,
        "contiguous_gradients": true,
        "sub_group_size": 1e9,
        "reduce_bucket_size": "auto",
        "stage3_prefetch_bucket_size": "auto",
        "stage3_param_persistence_threshold": "auto",
        "stage3_max_live_parameters": 1e9,
        "stage3_max_reuse_distance": 1e9,
        "stage3_gather_16bit_weights_on_model_save": true
    },

    "gradient_accumulation_steps": "auto",
    "gradient_clipping": "auto",
    "steps_per_print": 100,
    "train_batch_size": "auto",
    "train_micro_batch_size_per_gpu": "auto",
    "wall_clock_breakdown": false
}
```

## File: `finetune/finetune_ds.sh`
```bash
#!/bin/bash
export CUDA_DEVICE_MAX_CONNECTIONS=1
DIR=`pwd`

# Guide:
# This script supports distributed training on multi-gpu workers (as well as single-worker training).
# Please set the options below according to the comments.
# For multi-gpu workers training, these options should be manually set for each worker.
# After setting the options, please run the script on each worker.

# Number of GPUs per GPU worker
GPUS_PER_NODE=$(python -c 'import torch; print(torch.cuda.device_count())')

# Number of GPU workers, for single-worker training, please set to 1
NNODES=${NNODES:-1}

# The rank of this worker, should be in {0, ..., WORKER_CNT-1}, for single-worker training, please set to 0
NODE_RANK=${NODE_RANK:-0}

# The ip address of the rank-0 worker, for single-worker training, please set to localhost
MASTER_ADDR=${MASTER_ADDR:-localhost}

# The port for communication
MASTER_PORT=${MASTER_PORT:-6001}

MODEL="Qwen/Qwen-7B" # Set the path if you do not want to load from huggingface directly
# ATTENTION: specify the path to your training data, which should be a json file consisting of a list of conversations.
# See the section for finetuning in README for more information.
DATA="path_to_data"

function usage() {
    echo '
Usage: bash finetune/finetune_ds.sh [-m MODEL_PATH] [-d DATA_PATH]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -m | --model )
            shift
            MODEL=$1
            ;;
        -d | --data )
            shift
            DATA=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

DISTRIBUTED_ARGS="
    --nproc_per_node $GPUS_PER_NODE \
    --nnodes $NNODES \
    --node_rank $NODE_RANK \
    --master_addr $MASTER_ADDR \
    --master_port $MASTER_PORT
"

torchrun $DISTRIBUTED_ARGS finetune.py \
    --model_name_or_path $MODEL \
    --data_path $DATA \
    --bf16 True \
    --output_dir output_qwen \
    --num_train_epochs 5 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 1000 \
    --save_total_limit 10 \
    --learning_rate 1e-5 \
    --weight_decay 0.1 \
    --adam_beta2 0.95 \
    --warmup_ratio 0.01 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --report_to "none" \
    --model_max_length 512 \
    --gradient_checkpointing True \
    --lazy_preprocess True \
    --deepspeed finetune/ds_config_zero3.json
```

## File: `finetune/finetune_lora_ds.sh`
```bash
#!/bin/bash
export CUDA_DEVICE_MAX_CONNECTIONS=1
DIR=`pwd`

# Guide:
# This script supports distributed training on multi-gpu workers (as well as single-worker training).
# Please set the options below according to the comments.
# For multi-gpu workers training, these options should be manually set for each worker.
# After setting the options, please run the script on each worker.

# Number of GPUs per GPU worker
GPUS_PER_NODE=$(python -c 'import torch; print(torch.cuda.device_count())')

# Number of GPU workers, for single-worker training, please set to 1
NNODES=${NNODES:-1}

# The rank of this worker, should be in {0, ..., WORKER_CNT-1}, for single-worker training, please set to 0
NODE_RANK=${NODE_RANK:-0}

# The ip address of the rank-0 worker, for single-worker training, please set to localhost
MASTER_ADDR=${MASTER_ADDR:-localhost}

# The port for communication
MASTER_PORT=${MASTER_PORT:-6001}

MODEL="Qwen/Qwen-7B" # Set the path if you do not want to load from huggingface directly
# ATTENTION: specify the path to your training data, which should be a json file consisting of a list of conversations.
# See the section for finetuning in README for more information.
DATA="path_to_data"
DS_CONFIG_PATH="finetune/ds_config_zero2.json"

function usage() {
    echo '
Usage: bash finetune/finetune_lora_ds.sh [-m MODEL_PATH] [-d DATA_PATH] [--deepspeed DS_CONFIG_PATH]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -m | --model )
            shift
            MODEL=$1
            ;;
        -d | --data )
            shift
            DATA=$1
            ;;
        --deepspeed )
            shift
            DS_CONFIG_PATH=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

DISTRIBUTED_ARGS="
    --nproc_per_node $GPUS_PER_NODE \
    --nnodes $NNODES \
    --node_rank $NODE_RANK \
    --master_addr $MASTER_ADDR \
    --master_port $MASTER_PORT
"

torchrun $DISTRIBUTED_ARGS finetune.py \
    --model_name_or_path $MODEL \
    --data_path $DATA \
    --bf16 True \
    --output_dir output_qwen \
    --num_train_epochs 5 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 1000 \
    --save_total_limit 10 \
    --learning_rate 3e-4 \
    --weight_decay 0.1 \
    --adam_beta2 0.95 \
    --warmup_ratio 0.01 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --report_to "none" \
    --model_max_length 512 \
    --lazy_preprocess True \
    --use_lora \
    --gradient_checkpointing \
    --deepspeed ${DS_CONFIG_PATH}
```

## File: `finetune/finetune_lora_single_gpu.sh`
```bash
#!/bin/bash
export CUDA_DEVICE_MAX_CONNECTIONS=1

MODEL="Qwen/Qwen-7B" # Set the path if you do not want to load from huggingface directly
# ATTENTION: specify the path to your training data, which should be a json file consisting of a list of conversations.
# See the section for finetuning in README for more information.
DATA="path_to_data"

function usage() {
    echo '
Usage: bash finetune/finetune_lora_single_gpu.sh [-m MODEL_PATH] [-d DATA_PATH]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -m | --model )
            shift
            MODEL=$1
            ;;
        -d | --data )
            shift
            DATA=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

export CUDA_VISIBLE_DEVICES=0

python finetune.py \
  --model_name_or_path $MODEL \
  --data_path $DATA \
  --bf16 True \
  --output_dir output_qwen \
  --num_train_epochs 5 \
  --per_device_train_batch_size 2 \
  --per_device_eval_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --evaluation_strategy "no" \
  --save_strategy "steps" \
  --save_steps 1000 \
  --save_total_limit 10 \
  --learning_rate 3e-4 \
  --weight_decay 0.1 \
  --adam_beta2 0.95 \
  --warmup_ratio 0.01 \
  --lr_scheduler_type "cosine" \
  --logging_steps 1 \
  --report_to "none" \
  --model_max_length 512 \
  --lazy_preprocess True \
  --gradient_checkpointing \
  --use_lora

# If you use fp16 instead of bf16, you should use deepspeed
# --fp16 True --deepspeed finetune/ds_config_zero2.json
```

## File: `finetune/finetune_qlora_ds.sh`
```bash
#!/bin/bash
export CUDA_DEVICE_MAX_CONNECTIONS=1
DIR=`pwd`

# Guide:
# This script supports distributed training on multi-gpu workers (as well as single-worker training).
# Please set the options below according to the comments.
# For multi-gpu workers training, these options should be manually set for each worker.
# After setting the options, please run the script on each worker.

# Number of GPUs per GPU worker
GPUS_PER_NODE=$(python -c 'import torch; print(torch.cuda.device_count())')

# Number of GPU workers, for single-worker training, please set to 1
NNODES=${NNODES:-1}

# The rank of this worker, should be in {0, ..., WORKER_CNT-1}, for single-worker training, please set to 0
NODE_RANK=${NODE_RANK:-0}

# The ip address of the rank-0 worker, for single-worker training, please set to localhost
MASTER_ADDR=${MASTER_ADDR:-localhost}

# The port for communication
MASTER_PORT=${MASTER_PORT:-6001}

MODEL="Qwen/Qwen-7B-Chat-Int4" # Set the path if you do not want to load from huggingface directly
# ATTENTION: specify the path to your training data, which should be a json file consisting of a list of conversations.
# See the section for finetuning in README for more information.
DATA="path_to_data"

function usage() {
    echo '
Usage: bash finetune/finetune_qlora_ds.sh [-m MODEL_PATH] [-d DATA_PATH]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -m | --model )
            shift
            MODEL=$1
            ;;
        -d | --data )
            shift
            DATA=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

DISTRIBUTED_ARGS="
    --nproc_per_node $GPUS_PER_NODE \
    --nnodes $NNODES \
    --node_rank $NODE_RANK \
    --master_addr $MASTER_ADDR \
    --master_port $MASTER_PORT
"

# Remember to use --fp16 instead of --bf16 due to autogptq
torchrun $DISTRIBUTED_ARGS finetune.py \
    --model_name_or_path $MODEL \
    --data_path $DATA \
    --fp16 True \
    --output_dir output_qwen \
    --num_train_epochs 5 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 1000 \
    --save_total_limit 10 \
    --learning_rate 3e-4 \
    --weight_decay 0.1 \
    --adam_beta2 0.95 \
    --warmup_ratio 0.01 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --report_to "none" \
    --model_max_length 512 \
    --lazy_preprocess True \
    --use_lora \
    --q_lora \
    --gradient_checkpointing \
    --deepspeed finetune/ds_config_zero2.json
```

## File: `finetune/finetune_qlora_single_gpu.sh`
```bash
#!/bin/bash
export CUDA_DEVICE_MAX_CONNECTIONS=1
DIR=`pwd`

MODEL="Qwen/Qwen-7B-Chat-Int4" # Set the path if you do not want to load from huggingface directly
# ATTENTION: specify the path to your training data, which should be a json file consisting of a list of conversations.
# See the section for finetuning in README for more information.
DATA="path_to_data"

function usage() {
    echo '
Usage: bash finetune/finetune_qlora_single_gpu.sh [-m MODEL_PATH] [-d DATA_PATH]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -m | --model )
            shift
            MODEL=$1
            ;;
        -d | --data )
            shift
            DATA=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

export CUDA_VISIBLE_DEVICES=0

# Remember to use --fp16 instead of --bf16 due to autogptq
python finetune.py \
  --model_name_or_path $MODEL \
  --data_path $DATA \
  --fp16 True \
  --output_dir output_qwen \
  --num_train_epochs 5 \
  --per_device_train_batch_size 2 \
  --per_device_eval_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --evaluation_strategy "no" \
  --save_strategy "steps" \
  --save_steps 1000 \
  --save_total_limit 10 \
  --learning_rate 3e-4 \
  --weight_decay 0.1 \
  --adam_beta2 0.95 \
  --warmup_ratio 0.01 \
  --lr_scheduler_type "cosine" \
  --logging_steps 1 \
  --report_to "none" \
  --model_max_length 512 \
  --lazy_preprocess True \
  --gradient_checkpointing \
  --use_lora \
  --q_lora \
  --deepspeed finetune/ds_config_zero2.json
```

## File: `recipes/applications/chatbot/qwen_chatbot.ipynb`
```
{
  "cells": [
   {
    "cell_type": "markdown",
    "id": "54d5d255-aa98-4655-8dd1-bc726430d86a",
    "metadata": {},
    "source": [
     "# Qwen-7B-Chat Chat Demo"
    ]
   },
   {
    "cell_type": "markdown",
    "id": "31e04af4-eb27-4802-a7b2-6ea0525f1dc8",
    "metadata": {},
    "source": [
     "This notebook uses Qwen-7B-Chat as an example to introduce you to how to build a web-based conversational assistant using Gradio."
    ]
   },
   {
    "cell_type": "markdown",
    "id": "75e51155-9f8e-40dc-8432-60f4567d93a8",
    "metadata": {},
    "source": [
     "## Preparation"
    ]
   },
   {
    "cell_type": "markdown",
    "id": "ff6f061c-a033-49f2-8f7d-af3f23ac9125",
    "metadata": {},
    "source": [
     "Download Qwen-7B-Chat\n",
     "\n",
     "Firstly, we need to download the model. You can use the snapshot_download that comes with modelscope to download the model to a specified directory."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
    "id": "c469a129-451f-4d01-8bc0-e2cf70a262c8",
    "metadata": {
     "tags": []
    },
    "outputs": [],
    "source": [
     "!pip install modelscope"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
    "id": "69af626e-22b8-49ad-8869-8354f4c72bcc",
    "metadata": {
     "tags": []
    },
    "outputs": [],
    "source": [
     "from modelscope.hub.snapshot_download import snapshot_download\n",
     "snapshot_download(\"qwen/Qwen-7B-Chat\",cache_dir='/tmp/models') "
    ]
   },
   {
    "cell_type": "markdown",
    "id": "01d2ff34-4053-4710-a289-e354673be1ca",
    "metadata": {},
    "source": [
     "## Install Dependencies"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
    "id": "48b51791-4bbc-4d12-9cd6-587c24c8bea7",
    "metadata": {
     "tags": []
    },
    "outputs": [],
    "source": [
     "!pip install -r ../../../requirements.txt\n",
     "!pip install gradio==3.37.0 mdtex2html"
    ]
   },
   {
    "cell_type": "markdown",
    "id": "7732037a-246a-4953-af07-dae7a3ae5937",
    "metadata": {},
    "source": [
     "## Run the web UI code to start the Qwen chatbot\n",
     "\n",
     "Users can run the web_demo.py file to have real-time conversations with Qwen-7b-chat on the webpage."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
    "id": "9e256f0a-d96d-4fd7-b305-fe43c6959dc8",
    "metadata": {
     "ExecutionIndicator": {
      "show": true
     },
     "tags": []
    },
    "outputs": [],
    "source": [
     "!python ../../../web_demo.py -c /tmp/models/qwen/Qwen-7B-Chat"
    ]
   }
  ],
  "metadata": {
   "kernelspec": {
    "display_name": "Python 3 (ipykernel)",
    "language": "python",
    "name": "python3"
   },
   "language_info": {
    "codemirror_mode": {
     "name": "ipython",
     "version": 3
    },
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "name": "python",
    "nbconvert_exporter": "python",
    "pygments_lexer": "ipython3",
    "version": "3.10.13"
   }
  },
  "nbformat": 4,
  "nbformat_minor": 5
 }
 
```

## File: `recipes/applications/domain_finetune/qwen_domain_finetune.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0e7993c3-3999-4ac5-b1dc-77875d80e4c8",
   "metadata": {},
   "source": [
    "# Fine-tuning Qwen-7B-Chat on Your Own Domain-Specific Data\n",
    "\n",
    "This notebook uses Qwen-7B-Chat as an example to introduce how to LoRA fine-tune the Qwen model on a specific domain.\n",
    "\n",
    "Qwen is a pretrained conversational model that supports English and Chinese. It is suitable for universal scenarios, but may lack some specialized knowledge in certain specific domain. If you would like to fine-tune it for a specific domain, or on your own private dataset, you can refer to this tutorial.\n",
    "\n",
    "Here is an example showing the differences before and after fine-tuning.\n",
    "\n",
    "#### Model Input\n",
    ">怎样治疗青光眼?\n",
    "\n",
    "#### Before Fine-tuning\n",
    "\n",
    ">青光眼的治疗方法取决于病情严重程度。轻度青光眼可以采取药物治疗，比如激素类药物、抗生素等，以减轻炎症和改善血管紧张。\n",
    ">\n",
    ">中度青光眼可能需要激光手术来降低眼压，并使用药物以保持控制。\n",
    ">\n",
    ">重度青光眼则需要实施传统的眼部手术，如小梁切除术或巩膜外减压术，以防止视神经损伤。\n",
    "\n",
    "#### After Fine-tuning\n",
    "\n",
    ">青光眼是一种眼睛疾病，可以引起视神经的损伤和视力下降。治疗青光眼的主要方法是药物治疗、激光治疗和手术治疗。\n",
    ">1. 药物治疗：对于早期青光眼患者，通常采用抗青光眼药物治疗，通过降低眼压来预防视神经进一步损伤。目前常用的抗青光眼药物有拉坦前列素滴眼液、阿托品滴眼液等。\n",
    ">2. 激光治疗：对于中晚期青光眼患者，如果药物治疗效果不佳，可能需要进行激光治疗。目前常用的激光治疗方法包括小梁切除术、YAG激光手术等。\n",
    ">3. 手术治疗：对于非常严重的青光眼患者，可能需要进行手术治疗。目前常用的手术治疗方法包括前房引流术、虹膜周切术、小梁切除术、巩膜滤过术等。\n",
    ">\n",
    ">需要注意的是，以上治疗方法的具体选择应根据患者的病情和医生的专业建议来进行。同时，青光眼患者在日常生活中也需要保持良好的生活习惯，避免过度疲劳、保持情绪稳定、定期检查眼睛等情况的发生。"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bdea7e21-fec8-49fe-b7ea-afde3f02738f",
   "metadata": {},
   "source": [
    "## Environment Requirements\n",
    "\n",
    "Please refer to **requirements.txt** to install the required dependencies.\n",
    "\n",
    "Run the following command line in the main directory of the Qwen repo.\n",
    "```bash\n",
    "pip install -r requirements.txt\n",
    "```\n",
    "\n",
    "\n",
    "## Preparation\n",
    "\n",
    "### Download Qwen-7B-Chat\n",
    "\n",
    "First, download the model files. You can choose to download directly from ModelScope."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "248488f9-4a86-4f35-9d56-50f8e91a8f11",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "model_dir = snapshot_download('Qwen/Qwen-7B-chat', cache_dir='.')"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "7b2a92b1-f08e-4413-9f92-8f23761e6e1f",
   "metadata": {},
   "source": [
    "### Download Medical Training Data\n",
    "\n",
    "Download the data required for training; here, we provide a medical conversation dataset for training. It is sampled from [MedicalGPT repo](https://github.com/shibing624/MedicalGPT/) and we have converted this dataset into a format that can be used for fine-tuning.\n",
    "\n",
    "Disclaimer: the dataset can be only used for the research purpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce195f08-fbb2-470e-b6c0-9a03457458c7",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/medical_sft.json"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7226bed0-171b-4d45-a3f9-b3d81ec2bb9f",
   "metadata": {},
   "source": [
    "You can prepare your dataset in JSON format following the format below, and then modify the `--data_path` parameter in the training command to point to your JSON file.\n",
    "\n",
    "These data instances can be conversations in the real world or include domain knowledge QA pairs. Besides, fine-tuning allows Qwen-chat to play like some specific roles. As Qwen-chat is a dialogue model for general scenarios, your fine-tuning can customize a chatbot to meet your requirements.\n",
    "\n",
    "We recommend that you prepare 50~ data instances if you want to fine-tune Qwen-chat as a roleplay model.\n",
    "\n",
    "You may prepare much more data instances if you want to infuse the domain knowledge of your field into the model.\n",
    "\n",
    "In this tutorial, we have prepared a medical domain fine-tuning dataset consisting of 1000 data instancess as an example. You can refer to our example to fine-tune on your own domain-specific dataset.\n",
    "\n",
    "Below is a simple example list with 1 sample:\n",
    "\n",
    "```python\n",
    "[\n",
    "  {\n",
    "    \"id\": \"1\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"直肠腺瘤的早期症状?\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"结直肠腺瘤是起源于结直肠黏膜腺上皮的良性肿瘤，包括结肠腺瘤与直肠腺瘤，是常见的肠道良性肿瘤。因与大肠癌的发生关系密切，被认为是一种癌前病变。不同地区、不同年龄的发病率差别很大，40岁以下的发病率低，60岁以上较高，男女无明显差别。此类疾病的病因及发病机制不明确。部分患者有遗传因素存在，另外，高脂肪饮食与食物纤维不足、肠道菌群紊乱也与此病的发生有相关性。多数患者无症状。症状与腺瘤的大小、部位、病理性质等有关。有症状者可有以下表现：直肠腺瘤的临床常见症状有便血，多为无疼性便血，常呈鲜红色，量多，可引起贫血。粪便性状改变，多为粘液便，便意不尽或里急重感，有时只排出粘液，称为假性腹泻。1.腹部不适、腹部疼痛，多为大的腺瘤伴发肠套叠、肠梗阻引起。2.排便习惯改变，包括便秘、腹泻、里急后重等。3.粪便带血，最常见为间歇性便血。4.部分位于直肠的较大的、带蒂腺瘤可在排便时脱落或脱出肛。可以采取内镜下高频电凝、激光、微波凝固等方法切除，也可以选择外科手术切除，并定期随访。有恶变者根据情况选择其他治疗（如放疗、化疗、手术等）管状腺瘤切除术后复发者少见，但绒毛状腺瘤及绒毛管状腺瘤切除术后常可复发，尤其是绒毛状腺瘤，且多发的腺瘤复发率高于单发者。对于经内镜治疗或局部手术切除的结直肠腺瘤患者尤其是绒毛状腺瘤或广基的绒毛管状腺瘤患者，建议腺瘤切除后的第一年内3～6个月进行一次肠镜检查，第二年开始每年一次。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "You can also use multi-turn conversations as the training set. Here is a simple example:\n",
    "\n",
    "```python\n",
    "[\n",
    "  {\n",
    "    \"id\": \"2\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好，我最近经常感觉胸口疼痛，这是怎么回事？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"胸痛可能由多种原因引起，包括心脏问题、消化系统疾病、呼吸系统问题等。您能描述一下疼痛的性质和持续时间吗？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"疼痛感觉像是挤压，大概持续了几分钟。\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"挤压感的胸痛可能与心脏问题有关，特别是如果它伴随着呼吸困难、出汗或恶心。我建议您尽快去看医生并进行适当的检查，如心电图和血液检测，以确定具体原因。\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"我应该去急诊室吗，还是预约我的家庭医生？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"如果您的疼痛是突然发生的，并且还有其他症状，建议您立即去急诊室。如果疼痛不是很严重且没有其他严重症状，您可以预约家庭医生进一步评估。但请不要忽视疼痛，尤其是如果这种情况是第一次出现。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "## Fine-Tune the Model\n",
    "\n",
    "You can directly run the prepared training script to fine-tune the model. \n",
    "\n",
    "For parameter settings, you can modify `--model_name_or_path` to the location of the model you want to fine-tune, and set `--data_path` to the location of the dataset.\n",
    "\n",
    "You should remove the `--bf16` parameter if you are using a non-Ampere architecture GPU, such as a V100. \n",
    "\n",
    "For `--model_max_length` and `--per_device_train_batch_size`, we recommend the following configurations, ,you can refer to [this document](../../finetune/deepspeed/readme.md) for more details:\n",
    "\n",
    "| --model_max_length | --per_device_train_batch_size | GPU Memory |\n",
    "|-----------------|------------|--------------------|\n",
    "| 512             | 4          | 24g                |\n",
    "| 1024            | 3          | 24g                |\n",
    "| 512             | 8          | 32g                |\n",
    "| 1024            | 6          | 32g                |\n",
    "\n",
    "You can use our recommended saving parameters, or you can save by epoch by just setting `--save_strategy \"epoch\"` if you prefer to save at each epoch stage. `--save_total_limit` means the limit on the number of saved checkpoints.\n",
    "\n",
    "For other parameters, such as `--weight_decay` and `--adam_beta2`, we recommend using the values we provided blow.\n",
    "\n",
    "Setting the parameters `--gradient_checkpointing` and `--lazy_preprocess` is to save GPU memory.\n",
    "\n",
    "The parameters for the trained Lora module will be saved in the **output_qwen** folder."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ab0581e-be85-45e6-a5b7-af9c42ea697b",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!python ../../../finetune/finetune.py \\\n",
    "    --model_name_or_path \"Qwen/Qwen-7B-Chat/\"\\\n",
    "    --data_path  \"medical_sft.json\"\\\n",
    "    --bf16 \\\n",
    "    --output_dir \"output_qwen\" \\\n",
    "    --num_train_epochs 4\\\n",
    "    --per_device_train_batch_size 4 \\\n",
    "    --per_device_eval_batch_size 3 \\\n",
    "    --gradient_accumulation_steps 16 \\\n",
    "    --evaluation_strategy \"no\" \\\n",
    "    --save_strategy \"epoch\" \\\n",
    "    --save_steps 3000 \\\n",
    "    --save_total_limit 10 \\\n",
    "    --learning_rate 1e-5 \\\n",
    "    --weight_decay 0.1 \\\n",
    "    --adam_beta2 0.95 \\\n",
    "    --warmup_ratio 0.01 \\\n",
    "    --lr_scheduler_type \"cosine\" \\\n",
    "    --logging_steps 10 \\\n",
    "    --model_max_length 512 \\\n",
    "    --gradient_checkpointing \\\n",
    "    --lazy_preprocess \\\n",
    "    --use_lora"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e6f28aa-1772-48ce-aa15-8cf29e7d67b5",
   "metadata": {},
   "source": [
    "## Merge Weights\n",
    "\n",
    "The LoRA training only saves the adapter parameters. You can load the fine-tuned model and merge weights as shown below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4fd5ef2a-34f9-4909-bebe-7b3b086fd16a",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "execution": {
     "iopub.execute_input": "2024-01-26T02:46:14.585746Z",
     "iopub.status.busy": "2024-01-26T02:46:14.585089Z",
     "iopub.status.idle": "2024-01-26T02:47:08.095464Z",
     "shell.execute_reply": "2024-01-26T02:47:08.094715Z",
     "shell.execute_reply.started": "2024-01-26T02:46:14.585720Z"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "The model is automatically converting to bf16 for faster inference. If you want to disable the automatic precision, please manually add bf16/fp16/fp32=True to \"AutoModelForCausalLM.from_pretrained\".\n",
      "Try importing flash-attention for faster inference...\n",
      "Warning: import flash_attn rms_norm fail, please install FlashAttention layer_norm to get higher efficiency https://github.com/Dao-AILab/flash-attention/tree/main/csrc/layer_norm\n",
      "Loading checkpoint shards: 100%|██████████| 8/8 [00:06<00:00,  1.14it/s]\n"
     ]
    }
   ],
   "source": [
    "from transformers import AutoModelForCausalLM\n",
    "from peft import PeftModel\n",
    "import torch\n",
    "\n",
    "model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-7B-chat/\", torch_dtype=torch.float16, device_map=\"auto\", trust_remote_code=True)\n",
    "model = PeftModel.from_pretrained(model, \"output_qwen/\")\n",
    "merged_model = model.merge_and_unload()\n",
    "merged_model.save_pretrained(\"output_qwen_merged\", max_shard_size=\"2048MB\", safe_serialization=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e3f5b9f-63a1-4599-8d9b-a8d8f764838f",
   "metadata": {},
   "source": [
    "The tokenizer files are not saved in the new directory in this step. You can copy the tokenizer files or use the following code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "10fa5ea3-dd55-4901-86af-c045d4c56533",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "execution": {
     "iopub.execute_input": "2024-01-26T02:47:08.097051Z",
     "iopub.status.busy": "2024-01-26T02:47:08.096744Z",
     "iopub.status.idle": "2024-01-26T02:47:08.591289Z",
     "shell.execute_reply": "2024-01-26T02:47:08.590665Z",
     "shell.execute_reply.started": "2024-01-26T02:47:08.097029Z"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('output_qwen_merged/tokenizer_config.json',\n",
       " 'output_qwen_merged/special_tokens_map.json',\n",
       " 'output_qwen_merged/qwen.tiktoken',\n",
       " 'output_qwen_merged/added_tokens.json')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from transformers import AutoTokenizer\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\n",
    "    \"Qwen/Qwen-7B-chat/\",\n",
    "    trust_remote_code=True\n",
    ")\n",
    "\n",
    "tokenizer.save_pretrained(\"output_qwen_merged\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "804b84d8",
   "metadata": {},
   "source": [
    "## Test the Model\n",
    "\n",
    "After merging the weights, we can test the model as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dbae310c",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "execution": {
     "iopub.execute_input": "2024-01-26T02:48:29.995040Z",
     "iopub.status.busy": "2024-01-26T02:48:29.994448Z",
     "iopub.status.idle": "2024-01-26T02:48:41.677104Z",
     "shell.execute_reply": "2024-01-26T02:48:41.676591Z",
     "shell.execute_reply.started": "2024-01-26T02:48:29.995019Z"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning: import flash_attn rms_norm fail, please install FlashAttention layer_norm to get higher efficiency https://github.com/Dao-AILab/flash-attention/tree/main/csrc/layer_norm\n",
      "Loading checkpoint shards: 100%|██████████| 8/8 [00:04<00:00,  1.71it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "VDAC1（电压依赖性钙通道）是一种位于细胞膜上的钙离子通道，负责将细胞内的钙离子释放到细胞外。它在神经信号传导、肌肉收缩和血管舒张中发挥着重要作用。\n",
      "\n",
      "VDAC1通常由4个亚基组成，每个亚基都有不同的功能。其中，一个亚基是内腔部分，它与钙离子的结合有关；另一个亚基是外腔部分，它与离子通道的打开和关闭有关；第三个亚基是一层跨膜蛋白，它负责调节通道的开放程度；最后一个亚基是一个膜骨架连接器，它帮助维持通道的结构稳定性。\n",
      "\n",
      "除了钙离子外，VDAC1还能够接收钾离子和氯离子等其他离子，并将其从细胞内释放到细胞外。此外，VDAC1还参与了许多细胞代谢反应，例如脂肪酸合成和糖原分解等。\n",
      "\n",
      "总的来说，VDAC1是细胞膜上的一种重要离子通道，其作用涉及到许多重要的生物学过程。\n"
     ]
    }
   ],
   "source": [
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"output_qwen_merged\", trust_remote_code=True)\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    \"output_qwen_merged\",\n",
    "    device_map=\"auto\",\n",
    "    trust_remote_code=True\n",
    ").eval()\n",
    "\n",
    "response, history = model.chat(tokenizer, \"什么是VDAC1？\", history=None)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "987f524d-6918-48ae-a730-f285cf6f8416",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `recipes/applications/retrieval/retrieval.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "245ab07a-fb2f-4cf4-ab9a-5c05a9b44daa",
   "metadata": {},
   "source": [
    "# LangChain retrieval knowledge base Q&A based on Qwen-7B-Chat"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "e8df2cb7-a69c-4231-9596-4c871d893633",
   "metadata": {},
   "source": [
    "This notebook introduces a question-answering application based on a local knowledge base using Qwen-7B-Chat with langchain. The goal is to establish a knowledge base Q&A solution that is friendly to many scenarios and open-source models, and that can run offline. The implementation process of this project includes loading files -> reading text -> segmenting text -> vectorizing text -> vectorizing questions -> matching the top k most similar text vectors with the question vectors -> incorporating the matched text as context along with the question into the prompt -> submitting to the LLM (Large Language Model) to generate an answer."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92e9c81a-45c7-4c12-91af-3c5dd52f63bb",
   "metadata": {},
   "source": [
    "## Preparation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "84cfcf88-3bef-4412-a658-4eaefeb6502a",
   "metadata": {},
   "source": [
    "Download Qwen-7B-Chat\n",
    "\n",
    "Firstly, we need to download the model. You can use the snapshot_download that comes with modelscope to download the model to a specified directory."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c1f9ded-8035-42c7-82c7-444ce06572bc",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!pip install modelscope"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c26225c-c958-429e-b81d-2de9820670c2",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "snapshot_download(\"Qwen/Qwen-7B-Chat\",cache_dir='/tmp/models') "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8f51796-49fa-467d-a825-ae9a281eb3fd",
   "metadata": {},
   "source": [
    "Download the dependencies for langchain and Qwen."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87fe1023-644f-4610-afaf-0b7cddc30d60",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!pip install langchain==0.0.187 dashscope==1.0.4 sentencepiece==0.1.99 cpm_kernels==1.0.11 nltk==3.8.1 sentence_transformers==2.2.2 unstructured==0.6.5 faiss-cpu==1.7.4 icetk==0.0.7"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "853cdfa4-a2ce-4baa-919a-b9e2aecd2706",
   "metadata": {},
   "source": [
    "Download the retrieval document."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ba800dc-311d-4a83-8115-f05b09b39ffd",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/LLM_Survey_Chinese.pdf.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07e923b3-b7ae-4983-abeb-2ce115566f15",
   "metadata": {},
   "source": [
    "Download the text2vec model, for Chinese in our case."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a07cd8d-3cec-40f6-8d2b-eb111aaf1164",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/GanymedeNil_text2vec-large-chinese.tar.gz\n",
    "!tar -zxvf GanymedeNil_text2vec-large-chinese.tar.gz -C /tmp"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc483af0-170e-4e61-8d25-a336d1592e34",
   "metadata": {},
   "source": [
    "## Try out the model \n",
    "\n",
    "Load the Qwen-7B-Chat model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c112cf82-0447-46c4-9c32-18f243c0a686",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from abc import ABC\n",
    "from langchain.llms.base import LLM\n",
    "from typing import Any, List, Mapping, Optional\n",
    "from langchain.callbacks.manager import CallbackManagerForLLMRun\n",
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "\n",
    "model_path=\"/tmp/models/Qwen/Qwen-7B-Chat\"\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n",
    "model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True).half().cuda()\n",
    "model.eval()\n",
    "\n",
    "class Qwen(LLM, ABC):\n",
    "    max_token: int = 10000\n",
    "    temperature: float = 0.01\n",
    "    top_p = 0.9\n",
    "    history_len: int = 3\n",
    "\n",
    "    def __init__(self):\n",
    "        super().__init__()\n",
    "\n",
    "    @property\n",
    "    def _llm_type(self) -> str:\n",
    "        return \"Qwen\"\n",
    "\n",
    "    @property\n",
    "    def _history_len(self) -> int:\n",
    "        return self.history_len\n",
    "\n",
    "    def set_history_len(self, history_len: int = 10) -> None:\n",
    "        self.history_len = history_len\n",
    "\n",
    "    def _call(\n",
    "        self,\n",
    "        prompt: str,\n",
    "        stop: Optional[List[str]] = None,\n",
    "        run_manager: Optional[CallbackManagerForLLMRun] = None,\n",
    "    ) -> str:\n",
    "        response, _ = model.chat(tokenizer, prompt, history=[])\n",
    "        return response\n",
    "    \n",
    "    @property\n",
    "    def _identifying_params(self) -> Mapping[str, Any]:\n",
    "        \"\"\"Get the identifying parameters.\"\"\"\n",
    "        return {\"max_token\": self.max_token,\n",
    "                \"temperature\": self.temperature,\n",
    "                \"top_p\": self.top_p,\n",
    "                \"history_len\": self.history_len}\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "382ed433-870f-424e-b074-210ea6f84b70",
   "metadata": {},
   "source": [
    "Specify the txt file that needs retrieval for knowledge-based Q&A."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14be706b-4a7d-4906-9369-1f03c6c99854",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import torch\n",
    "import argparse\n",
    "from langchain.vectorstores import FAISS\n",
    "from langchain.embeddings.huggingface import HuggingFaceEmbeddings\n",
    "from typing import List, Tuple\n",
    "import numpy as np\n",
    "from langchain.document_loaders import TextLoader\n",
    "from chinese_text_splitter import ChineseTextSplitter\n",
    "from langchain.docstore.document import Document\n",
    "from langchain.prompts.prompt import PromptTemplate\n",
    "from langchain.chains import RetrievalQA\n",
    "\n",
    "\n",
    "def load_file(filepath, sentence_size=100):\n",
    "    loader = TextLoader(filepath, autodetect_encoding=True)\n",
    "    textsplitter = ChineseTextSplitter(pdf=False, sentence_size=sentence_size)\n",
    "    docs = loader.load_and_split(textsplitter)\n",
    "    write_check_file(filepath, docs)\n",
    "    return docs\n",
    "\n",
    "\n",
    "def write_check_file(filepath, docs):\n",
    "    folder_path = os.path.join(os.path.dirname(filepath), \"tmp_files\")\n",
    "    if not os.path.exists(folder_path):\n",
    "        os.makedirs(folder_path)\n",
    "    fp = os.path.join(folder_path, 'load_file.txt')\n",
    "    with open(fp, 'a+', encoding='utf-8') as fout:\n",
    "        fout.write(\"filepath=%s,len=%s\" % (filepath, len(docs)))\n",
    "        fout.write('\\n')\n",
    "        for i in docs:\n",
    "            fout.write(str(i))\n",
    "            fout.write('\\n')\n",
    "        fout.close()\n",
    "\n",
    "        \n",
    "def seperate_list(ls: List[int]) -> List[List[int]]:\n",
    "    lists = []\n",
    "    ls1 = [ls[0]]\n",
    "    for i in range(1, len(ls)):\n",
    "        if ls[i - 1] + 1 == ls[i]:\n",
    "            ls1.append(ls[i])\n",
    "        else:\n",
    "            lists.append(ls1)\n",
    "            ls1 = [ls[i]]\n",
    "    lists.append(ls1)\n",
    "    return lists\n",
    "\n",
    "\n",
    "class FAISSWrapper(FAISS):\n",
    "    chunk_size = 250\n",
    "    chunk_conent = True\n",
    "    score_threshold = 0\n",
    "    \n",
    "    def similarity_search_with_score_by_vector(\n",
    "            self, embedding: List[float], k: int = 4\n",
    "    ) -> List[Tuple[Document, float]]:\n",
    "        scores, indices = self.index.search(np.array([embedding], dtype=np.float32), k)\n",
    "        docs = []\n",
    "        id_set = set()\n",
    "        store_len = len(self.index_to_docstore_id)\n",
    "        for j, i in enumerate(indices[0]):\n",
    "            if i == -1 or 0 < self.score_threshold < scores[0][j]:\n",
    "                # This happens when not enough docs are returned.\n",
    "                continue\n",
    "            _id = self.index_to_docstore_id[i]\n",
    "            doc = self.docstore.search(_id)\n",
    "            if not self.chunk_conent:\n",
    "                if not isinstance(doc, Document):\n",
    "                    raise ValueError(f\"Could not find document for id {_id}, got {doc}\")\n",
    "                doc.metadata[\"score\"] = int(scores[0][j])\n",
    "                docs.append(doc)\n",
    "                continue\n",
    "            id_set.add(i)\n",
    "            docs_len = len(doc.page_content)\n",
    "            for k in range(1, max(i, store_len - i)):\n",
    "                break_flag = False\n",
    "                for l in [i + k, i - k]:\n",
    "                    if 0 <= l < len(self.index_to_docstore_id):\n",
    "                        _id0 = self.index_to_docstore_id[l]\n",
    "                        doc0 = self.docstore.search(_id0)\n",
    "                        if docs_len + len(doc0.page_content) > self.chunk_size:\n",
    "                            break_flag = True\n",
    "                            break\n",
    "                        elif doc0.metadata[\"source\"] == doc.metadata[\"source\"]:\n",
    "                            docs_len += len(doc0.page_content)\n",
    "                            id_set.add(l)\n",
    "                if break_flag:\n",
    "                    break\n",
    "        if not self.chunk_conent:\n",
    "            return docs\n",
    "        if len(id_set) == 0 and self.score_threshold > 0:\n",
    "            return []\n",
    "        id_list = sorted(list(id_set))\n",
    "        id_lists = seperate_list(id_list)\n",
    "        for id_seq in id_lists:\n",
    "            for id in id_seq:\n",
    "                if id == id_seq[0]:\n",
    "                    _id = self.index_to_docstore_id[id]\n",
    "                    doc = self.docstore.search(_id)\n",
    "                else:\n",
    "                    _id0 = self.index_to_docstore_id[id]\n",
    "                    doc0 = self.docstore.search(_id0)\n",
    "                    doc.page_content += \" \" + doc0.page_content\n",
    "            if not isinstance(doc, Document):\n",
    "                raise ValueError(f\"Could not find document for id {_id}, got {doc}\")\n",
    "            doc_score = min([scores[0][id] for id in [indices[0].tolist().index(i) for i in id_seq if i in indices[0]]])\n",
    "            doc.metadata[\"score\"] = int(doc_score)\n",
    "            docs.append((doc, doc_score))\n",
    "        return docs\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    # load docs\n",
    "    filepath = 'LLM_Survey_Chinese.pdf.txt'\n",
    "    # LLM name\n",
    "    LLM_TYPE = 'qwen'\n",
    "    # Embedding model name\n",
    "    EMBEDDING_MODEL = 'text2vec'\n",
    "    # 基于上下文的prompt模版，请务必保留\"{question}\"和\"{context_str}\"\n",
    "    PROMPT_TEMPLATE = \"\"\"已知信息：\n",
    "    {context_str} \n",
    "    根据上述已知信息，简洁和专业的来回答用户的问题。如果无法从中得到答案，请说 “根据已知信息无法回答该问题” 或 “没有提供足够的相关信息”，不允许在答案中添加编造成分，答案请使用中文。 问题是：{question}\"\"\"\n",
    "    # Embedding running device\n",
    "    EMBEDDING_DEVICE = \"cuda\"\n",
    "    # return top-k text chunk from vector store\n",
    "    VECTOR_SEARCH_TOP_K = 3\n",
    "    # 文本分句长度\n",
    "    SENTENCE_SIZE = 50\n",
    "    CHAIN_TYPE = 'stuff'\n",
    "    llm_model_dict = {\n",
    "        \"qwen\": QWen,\n",
    "    }\n",
    "    embedding_model_dict = {\n",
    "        \"text2vec\": \"/tmp/GanymedeNil_text2vec-large-chinese\",\n",
    "    }\n",
    "    print(\"loading model start\")\n",
    "    llm = llm_model_dict[LLM_TYPE]()\n",
    "    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_dict[EMBEDDING_MODEL],model_kwargs={'device': EMBEDDING_DEVICE})\n",
    "    print(\"loading model done\")\n",
    "\n",
    "    print(\"loading documents start\")\n",
    "    docs = load_file(filepath, sentence_size=SENTENCE_SIZE)\n",
    "    print(\"loading documents done\")\n",
    "\n",
    "    print(\"embedding start\")\n",
    "    docsearch = FAISSWrapper.from_documents(docs, embeddings)\n",
    "    print(\"embedding done\")\n",
    "\n",
    "    print(\"loading qa start\")\n",
    "    prompt = PromptTemplate(\n",
    "        template=PROMPT_TEMPLATE, input_variables=[\"context_str\", \"question\"]\n",
    "    )\n",
    "\n",
    "    chain_type_kwargs = {\"prompt\": prompt, \"document_variable_name\": \"context_str\"}\n",
    "    qa = RetrievalQA.from_chain_type(\n",
    "        llm=llm,\n",
    "        chain_type=CHAIN_TYPE, \n",
    "        retriever=docsearch.as_retriever(search_kwargs={\"k\": VECTOR_SEARCH_TOP_K}), \n",
    "        chain_type_kwargs=chain_type_kwargs)\n",
    "    print(\"loading qa done\")\n",
    "\n",
    "    query = \"大模型指令微调有好的策略？\"  \n",
    "    print(qa.run(query))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `recipes/finetune/ascend/README.md`
```markdown
# Fine-tuning Qwen by Ascend NPU
Below, we provide a simple example to show how to finetune Qwen by Ascend NPU. Currently, fine-tuning and inference are supported for Qwen 7B and 14B models. You can also refer to the official [mindformers](https://gitee.com/mindspore/mindformers/blob/dev/research/qwen/qwen.md) for detailed usage.

## Environment Requirement

- Hardware: Ascend 910A/B

## Quickstart

1. Launch Docker Image

```bash
ImageID=pai-image-manage-registry.cn-wulanchabu.cr.aliyuncs.com/pai/llm-inference:qwen_v23.0.rc3
docker run -it -u root --ipc=host \
--device=/dev/davinci0 \
--device=/dev/davinci1 \
--device=/dev/davinci2 \
--device=/dev/davinci3 \
--device=/dev/davinci4 \
--device=/dev/davinci5 \
--device=/dev/davinci6 \
--device=/dev/davinci7 \
--device=/dev/davinci_manager \
--device=/dev/devmm_svm \
--device=/dev/hisi_hdc \
-v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
-v /usr/local/Ascend/add-ons/:/usr/local/Ascend/add-ons/ \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/sbin/npu-smi:/usr/local/sbin/npu-smi \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /var/log/npu/:/usr/slog \
-v /etc/hccn.conf:/etc/hccn.conf \
${ImageID} /bin/bash
```

2. Download and Convert model

- download model by modelscope

```bash
cd mindformers
python3 -c "from modelscope.hub.snapshot_download import snapshot_download; snapshot_download('Qwen/Qwen-7B-Chat', cache_dir='.', revision='master')"
```

- convert hf model weights to ckpt weights

```bash
python research/qwen/convert_weight.py \
    --torch_ckpt_dir Qwen/Qwen-7B-Chat \
    --mindspore_ckpt_path qwen-7b-chat.ckpt

mkdir -vp load_checkpoint/rank_0
mv qwen-7b-chat.ckpt load_checkpoint/rank_0/
```

3. Prepare training data

- download demo data

```bash
wget -c https://pai-vision-data-hz.oss-cn-zhangjiakou.aliyuncs.com/alpaca_data_min.json
```

- Converts the raw data to the specified format

```bash
python research/qwen/alpaca_converter.py \
    --data_path alpaca_data_min.json \
    --output_path alpaca-data-conversation_min.json
```

- Generate Mindrecord data

```bash
python research/qwen/qwen_preprocess.py \
    --input_glob alpaca-data-conversation_min.json \
    --model_file Qwen/Qwen-7B-Chat/qwen.tiktoken \
    --seq_length 1024 \
    --output_file alpaca_min.mindrecord
```

4. Prepare RANK_TABLE_FILE

```bash
# generate RANK_TABLE_FILE with 8 npu
python mindformers/tools/hccl_tools.py --device_num "[0,8)"
```

5. Fine-tune

You need to replace RANK_TABLE_FILE with the file generated in step 5.

```bash
export MS_ASCEND_CHECK_OVERFLOW_MODE=INFNAN_MODE
bash research/run_singlenode.sh "python3 research/qwen/run_qwen.py \
--config research/qwen/run_qwen_7b.yaml \
--load_checkpoint /mindformers/research/qwen/load_checkpoint \
--vocab_file Qwen/Qwen-7B-Chat/qwen.tiktoken \
--use_parallel True \
--run_mode finetune \
--auto_trans_ckpt True \
--train_data alpaca_min.mindrecord" \
RANK_TABLE_FILE [0,8] 8
```

6. Merge model weights

- Rename model weights

```bash
cd output/checkpoint_network
mv rank_0/qwen_rank_0-network.ckpt rank_0/checkpoint_0.ckpt
mv rank_1/qwen_rank_1-network.ckpt rank_1/checkpoint_1.ckpt
mv rank_2/qwen_rank_2-network.ckpt rank_2/checkpoint_2.ckpt
mv rank_3/qwen_rank_3-network.ckpt rank_3/checkpoint_3.ckpt
mv rank_4/qwen_rank_4-network.ckpt rank_4/checkpoint_4.ckpt
mv rank_5/qwen_rank_5-network.ckpt rank_5/checkpoint_5.ckpt
mv rank_6/qwen_rank_6-network.ckpt rank_6/checkpoint_6.ckpt
mv rank_7/qwen_rank_7-network.ckpt rank_7/checkpoint_7.ckpt
cd ../..
```

- Merge model weights

```bash
python mindformers/tools/transform_ckpt.py \
    --src_ckpt_strategy output/strategy  \
    --src_ckpt_dir output/checkpoint_network \
    --dst_ckpt_dir output/merged_model
```

7. Inference fine-tuned model

```bash
python research/qwen/run_qwen.py \
    --config research/qwen/run_qwen_7b.yaml \
    --predict_data '比较适合深度学习入门的书籍有' \
    --run_mode predict \
    --load_checkpoint output/merged_model/rank_0/checkpoint_0.ckpt \
    --vocab_file Qwen/Qwen-7B-Chat/qwen.tiktoken \
    --auto_trans_ckpt False \
    --device_id 0
```
```

## File: `recipes/finetune/deepspeed/finetune_fullparameter_multi_gpu.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6e6981ab-2d9a-4280-923f-235a166855ba",
   "metadata": {},
   "source": [
    "# Fine-Tuning Qwen-Chat Large Language Model (Multiple GPUs)\n",
    "\n",
    "Tongyi Qianwen is a large language model developed by Alibaba Cloud based on the Transformer architecture, trained on an extensive set of pre-training data. The pre-training data is diverse and covers a wide range, including a large amount of internet text, specialized books, code, etc. In addition, an AI assistant called Qwen-Chat has been created based on the pre-trained model using alignment mechanism.\n",
    "\n",
    "This notebook uses Qwen-1.8B-Chat as an example to introduce how to fine-tune the Qianwen model using Deepspeed.\n",
    "\n",
    "## Environment Requirements\n",
    "\n",
    "Please refer to **requirements.txt** to install the required dependencies.\n",
    "\n",
    "## Preparation\n",
    "\n",
    "### Download Qwen-1.8B-Chat\n",
    "\n",
    "First, download the model files. You can choose to download directly from ModelScope."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "248488f9-4a86-4f35-9d56-50f8e91a8f11",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "model_dir = snapshot_download('Qwen/Qwen-1_8B-Chat', cache_dir='.', revision='master')"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "7b2a92b1-f08e-4413-9f92-8f23761e6e1f",
   "metadata": {},
   "source": [
    "### Download Example Training Data\n",
    "\n",
    "Download the data required for training; here, we provide a tiny dataset as an example. It is sampled from [Belle](https://github.com/LianjiaTech/BELLE).\n",
    "\n",
    "Disclaimer: the dataset can be only used for the research purpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce195f08-fbb2-470e-b6c0-9a03457458c7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/Belle_sampled_qwen.json"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7226bed0-171b-4d45-a3f9-b3d81ec2bb9f",
   "metadata": {},
   "source": [
    "You can also refer to this format to prepare the dataset. Below is a simple example list with 1 sample:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"我是一个语言模型，我叫通义千问。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "You can also use multi-turn conversations as the training set. Here is a simple example:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好，能告诉我遛狗的最佳时间吗？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"当地最佳遛狗时间因地域差异而异，请问您所在的城市是哪里？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"我在纽约市。\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"纽约市的遛狗最佳时间通常在早晨6点至8点和晚上8点至10点之间，因为这些时间段气温较低，遛狗更加舒适。但具体时间还需根据气候、气温和季节变化而定。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "## Fine-Tune the Model\n",
    "\n",
    "You can directly run the prepared training script to fine-tune the model. **nproc_per_node** refers to the number of GPUs used fro training."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ab0581e-be85-45e6-a5b7-af9c42ea697b",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!torchrun --nproc_per_node 2 --nnodes 1 --node_rank 0 --master_addr localhost --master_port 6601 ../../finetune.py \\\n",
    "    --model_name_or_path \"Qwen/Qwen-1_8B-Chat/\" \\\n",
    "    --data_path \"Belle_sampled_qwen.json\" \\\n",
    "    --bf16 True \\\n",
    "    --output_dir \"output_qwen\" \\\n",
    "    --num_train_epochs 5 \\\n",
    "    --per_device_train_batch_size 1 \\\n",
    "    --per_device_eval_batch_size 1 \\\n",
    "    --gradient_accumulation_steps 16 \\\n",
    "    --evaluation_strategy \"no\" \\\n",
    "    --save_strategy \"steps\" \\\n",
    "    --save_steps 1000 \\\n",
    "    --save_total_limit 10 \\\n",
    "    --learning_rate 1e-5 \\\n",
    "    --weight_decay 0.1 \\\n",
    "    --adam_beta2 0.95 \\\n",
    "    --warmup_ratio 0.01 \\\n",
    "    --lr_scheduler_type \"cosine\" \\\n",
    "    --logging_steps 1 \\\n",
    "    --report_to \"none\" \\\n",
    "    --model_max_length 512 \\\n",
    "    --gradient_checkpointing True \\\n",
    "    --lazy_preprocess True \\\n",
    "    --deepspeed \"../../finetune/ds_config_zero2.json\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Test the Model\n",
    "\n",
    "We can test the model as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"output_qwen\", trust_remote_code=True)\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    \"output_qwen\",\n",
    "    device_map=\"auto\",\n",
    "    trust_remote_code=True\n",
    ").eval()\n",
    "\n",
    "response, history = model.chat(tokenizer, \"你好\", history=None)\n",
    "print(response)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `recipes/finetune/deepspeed/finetune_fullparameter_single_gpu.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6e6981ab-2d9a-4280-923f-235a166855ba",
   "metadata": {},
   "source": [
    "# Fine-Tuning Qwen-Chat Large Language Model (Single GPU)\n",
    "\n",
    "Tongyi Qianwen is a large language model developed by Alibaba Cloud based on the Transformer architecture, trained on an extensive set of pre-training data. The pre-training data is diverse and covers a wide range, including a large amount of internet text, specialized books, code, etc. In addition, an AI assistant called Qwen-Chat has been created based on the pre-trained model using alignment mechanism.\n",
    "\n",
    "This notebook uses Qwen-1.8B-Chat as an example to introduce how to fine-tune the Qianwen model using Deepspeed.\n",
    "\n",
    "## Environment Requirements\n",
    "\n",
    "Please refer to **requirements.txt** to install the required dependencies.\n",
    "\n",
    "## Preparation\n",
    "\n",
    "### Download Qwen-1.8B-Chat\n",
    "\n",
    "First, download the model files. You can choose to download directly from ModelScope."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "248488f9-4a86-4f35-9d56-50f8e91a8f11",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "execution": {
     "iopub.execute_input": "2023-12-31T03:19:11.059814Z",
     "iopub.status.busy": "2023-12-31T03:19:11.059177Z",
     "iopub.status.idle": "2023-12-31T03:21:54.157827Z",
     "shell.execute_reply": "2023-12-31T03:21:54.157333Z",
     "shell.execute_reply.started": "2023-12-31T03:19:11.059783Z"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "model_dir = snapshot_download('Qwen/Qwen-1_8B-Chat', cache_dir='.', revision='master')"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "7b2a92b1-f08e-4413-9f92-8f23761e6e1f",
   "metadata": {},
   "source": [
    "### Download Example Training Data\n",
    "\n",
    "Download the data required for training; here, we provide a tiny dataset as an example. It is sampled from [Belle](https://github.com/LianjiaTech/BELLE).\n",
    "\n",
    "Disclaimer: the dataset can be only used for the research purpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce195f08-fbb2-470e-b6c0-9a03457458c7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-12-31T03:21:57.596577Z",
     "iopub.status.busy": "2023-12-31T03:21:57.595847Z",
     "iopub.status.idle": "2023-12-31T03:21:57.971112Z",
     "shell.execute_reply": "2023-12-31T03:21:57.970576Z",
     "shell.execute_reply.started": "2023-12-31T03:21:57.596555Z"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/Belle_sampled_qwen.json"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7226bed0-171b-4d45-a3f9-b3d81ec2bb9f",
   "metadata": {},
   "source": [
    "You can also refer to this format to prepare the dataset. Below is a simple example list with 1 sample:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"我是一个语言模型，我叫通义千问。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "You can also use multi-turn conversations as the training set. Here is a simple example:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好，能告诉我遛狗的最佳时间吗？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"当地最佳遛狗时间因地域差异而异，请问您所在的城市是哪里？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"我在纽约市。\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"纽约市的遛狗最佳时间通常在早晨6点至8点和晚上8点至10点之间，因为这些时间段气温较低，遛狗更加舒适。但具体时间还需根据气候、气温和季节变化而定。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "\n",
    "## Fine-Tune the Model\n",
    "\n",
    "You can directly run the prepared training script to fine-tune the model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ab0581e-be85-45e6-a5b7-af9c42ea697b",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "execution": {
     "iopub.execute_input": "2023-12-31T03:23:52.455178Z",
     "iopub.status.busy": "2023-12-31T03:23:52.454615Z",
     "iopub.status.idle": "2023-12-31T03:24:15.699948Z",
     "shell.execute_reply": "2023-12-31T03:24:15.699358Z",
     "shell.execute_reply.started": "2023-12-31T03:23:52.455144Z"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!python ../../finetune.py \\\n",
    "    --model_name_or_path \"Qwen/Qwen-1_8B-Chat/\"\\\n",
    "    --data_path  \"Belle_sampled_qwen.json\"\\\n",
    "    --bf16 \\\n",
    "    --output_dir \"output_qwen\" \\\n",
    "    --num_train_epochs 5 \\\n",
    "    --per_device_train_batch_size 1 \\\n",
    "    --per_device_eval_batch_size 1 \\\n",
    "    --gradient_accumulation_steps 16 \\\n",
    "    --evaluation_strategy \"no\" \\\n",
    "    --save_strategy \"steps\" \\\n",
    "    --save_steps 1000 \\\n",
    "    --save_total_limit 10 \\\n",
    "    --learning_rate 1e-5 \\\n",
    "    --weight_decay 0.1 \\\n",
    "    --adam_beta2 0.95 \\\n",
    "    --warmup_ratio 0.01 \\\n",
    "    --lr_scheduler_type \"cosine\" \\\n",
    "    --logging_steps 1 \\\n",
    "    --report_to \"none\" \\\n",
    "    --model_max_length 512 \\\n",
    "    --gradient_checkpointing \\\n",
    "    --lazy_preprocess"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Test the Model\n",
    "\n",
    "We can test the model as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"output_qwen\", trust_remote_code=True)\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    \"output_qwen\",\n",
    "    device_map=\"auto\",\n",
    "    trust_remote_code=True\n",
    ").eval()\n",
    "\n",
    "response, history = model.chat(tokenizer, \"你好\", history=None)\n",
    "print(response)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `recipes/finetune/deepspeed/finetune_lora_multi_gpu.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6e6981ab-2d9a-4280-923f-235a166855ba",
   "metadata": {},
   "source": [
    "# LoRA Fine-Tuning Qwen-Chat Large Language Model (Multiple GPUs)\n",
    "\n",
    "Tongyi Qianwen is a large language model developed by Alibaba Cloud based on the Transformer architecture, trained on an extensive set of pre-training data. The pre-training data is diverse and covers a wide range, including a large amount of internet text, specialized books, code, etc. In addition, an AI assistant called Qwen-Chat has been created based on the pre-trained model using alignment mechanism.\n",
    "\n",
    "This notebook uses Qwen-1.8B-Chat as an example to introduce how to LoRA fine-tune the Qianwen model using Deepspeed.\n",
    "\n",
    "## Environment Requirements\n",
    "\n",
    "Please refer to **requirements.txt** to install the required dependencies.\n",
    "\n",
    "## Preparation\n",
    "\n",
    "### Download Qwen-1.8B-Chat\n",
    "\n",
    "First, download the model files. You can choose to download directly from ModelScope."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "248488f9-4a86-4f35-9d56-50f8e91a8f11",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "model_dir = snapshot_download('Qwen/Qwen-1_8B-Chat', cache_dir='.', revision='master')"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "7b2a92b1-f08e-4413-9f92-8f23761e6e1f",
   "metadata": {},
   "source": [
    "### Download Example Training Data\n",
    "\n",
    "Download the data required for training; here, we provide a tiny dataset as an example. It is sampled from [Belle](https://github.com/LianjiaTech/BELLE).\n",
    "\n",
    "Disclaimer: the dataset can be only used for the research purpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce195f08-fbb2-470e-b6c0-9a03457458c7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/Belle_sampled_qwen.json"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7226bed0-171b-4d45-a3f9-b3d81ec2bb9f",
   "metadata": {},
   "source": [
    "You can also refer to this format to prepare the dataset. Below is a simple example list with 1 sample:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"我是一个语言模型，我叫通义千问。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "You can also use multi-turn conversations as the training set. Here is a simple example:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好，能告诉我遛狗的最佳时间吗？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"当地最佳遛狗时间因地域差异而异，请问您所在的城市是哪里？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"我在纽约市。\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"纽约市的遛狗最佳时间通常在早晨6点至8点和晚上8点至10点之间，因为这些时间段气温较低，遛狗更加舒适。但具体时间还需根据气候、气温和季节变化而定。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "## Fine-Tune the Model\n",
    "\n",
    "You can directly run the prepared training script to fine-tune the model. **nproc_per_node** refers to the number of GPUs used fro training."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ab0581e-be85-45e6-a5b7-af9c42ea697b",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!torchrun --nproc_per_node 2 --nnodes 1 --node_rank 0 --master_addr localhost --master_port 6601 ../../finetune.py \\\n",
    "    --model_name_or_path \"Qwen/Qwen-1_8B-Chat/\" \\\n",
    "    --data_path \"Belle_sampled_qwen.json\" \\\n",
    "    --bf16 True \\\n",
    "    --output_dir \"output_qwen\" \\\n",
    "    --num_train_epochs 5 \\\n",
    "    --per_device_train_batch_size 1 \\\n",
    "    --per_device_eval_batch_size 1 \\\n",
    "    --gradient_accumulation_steps 16 \\\n",
    "    --evaluation_strategy \"no\" \\\n",
    "    --save_strategy \"steps\" \\\n",
    "    --save_steps 1000 \\\n",
    "    --save_total_limit 10 \\\n",
    "    --learning_rate 1e-5 \\\n",
    "    --weight_decay 0.1 \\\n",
    "    --adam_beta2 0.95 \\\n",
    "    --warmup_ratio 0.01 \\\n",
    "    --lr_scheduler_type \"cosine\" \\\n",
    "    --logging_steps 1 \\\n",
    "    --report_to \"none\" \\\n",
    "    --model_max_length 512 \\\n",
    "    --gradient_checkpointing True \\\n",
    "    --lazy_preprocess True \\\n",
    "    --deepspeed \"../../finetune/ds_config_zero2.json\" \\\n",
    "    --use_lora"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "35acf008-1dfe-4d32-8cf5-7022e042aadb",
   "metadata": {},
   "source": [
    "## Merge Weights\n",
    "\n",
    "The training of both LoRA and Q-LoRA only saves the adapter parameters. You can load the fine-tuned model and merge weights as shown below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61021499-4a44-45af-a682-943ed63c2fcb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM\n",
    "from peft import PeftModel\n",
    "import torch\n",
    "\n",
    "model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-1_8B-Chat/\", torch_dtype=torch.float16, device_map=\"auto\", trust_remote_code=True)\n",
    "model = PeftModel.from_pretrained(model, \"output_qwen/\")\n",
    "merged_model = model.merge_and_unload()\n",
    "merged_model.save_pretrained(\"output_qwen_merged\", max_shard_size=\"2048MB\", safe_serialization=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0dfbd261-6451-4532-82e8-3ae19ed93ee1",
   "metadata": {},
   "source": [
    "The tokenizer files are not saved in the new directory in this step. You can copy the tokenizer files or use the following code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddcba069-340b-4a93-a145-2028b425dd23",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoTokenizer\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\n",
    "    \"Qwen/Qwen-1_8B-Chat/\",\n",
    "    trust_remote_code=True\n",
    ")\n",
    "\n",
    "tokenizer.save_pretrained(\"output_qwen_merged\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe9f2878-79d3-4b1c-ba95-ac2f73aa6e1b",
   "metadata": {},
   "source": [
    "## Test the Model\n",
    "\n",
    "After merging the weights, we can test the model as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"output_qwen_merged\", trust_remote_code=True)\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    \"output_qwen_merged\",\n",
    "    device_map=\"auto\",\n",
    "    trust_remote_code=True\n",
    ").eval()\n",
    "\n",
    "response, history = model.chat(tokenizer, \"你好\", history=None)\n",
    "print(response)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `recipes/finetune/deepspeed/finetune_lora_single_gpu.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6e6981ab-2d9a-4280-923f-235a166855ba",
   "metadata": {},
   "source": [
    "# LoRA Fine-Tuning Qwen-Chat Large Language Model (Single GPU)\n",
    "\n",
    "Tongyi Qianwen is a large language model developed by Alibaba Cloud based on the Transformer architecture, trained on an extensive set of pre-training data. The pre-training data is diverse and covers a wide range, including a large amount of internet text, specialized books, code, etc. In addition, an AI assistant called Qwen-Chat has been created based on the pre-trained model using alignment mechanism.\n",
    "\n",
    "This notebook uses Qwen-1.8B-Chat as an example to introduce how to LoRA fine-tune the Qianwen model using Deepspeed.\n",
    "\n",
    "## Environment Requirements\n",
    "\n",
    "Please refer to **requirements.txt** to install the required dependencies.\n",
    "\n",
    "## Preparation\n",
    "\n",
    "### Download Qwen-1.8B-Chat\n",
    "\n",
    "First, download the model files. You can choose to download directly from ModelScope."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "248488f9-4a86-4f35-9d56-50f8e91a8f11",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "model_dir = snapshot_download('Qwen/Qwen-1_8B-Chat', cache_dir='.', revision='master')"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "7b2a92b1-f08e-4413-9f92-8f23761e6e1f",
   "metadata": {},
   "source": [
    "### Download Example Training Data\n",
    "\n",
    "Download the data required for training; here, we provide a tiny dataset as an example. It is sampled from [Belle](https://github.com/LianjiaTech/BELLE).\n",
    "\n",
    "Disclaimer: the dataset can be only used for the research purpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce195f08-fbb2-470e-b6c0-9a03457458c7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/Belle_sampled_qwen.json"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7226bed0-171b-4d45-a3f9-b3d81ec2bb9f",
   "metadata": {},
   "source": [
    "You can also refer to this format to prepare the dataset. Below is a simple example list with 1 sample:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"我是一个语言模型，我叫通义千问。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "You can also use multi-turn conversations as the training set. Here is a simple example:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好，能告诉我遛狗的最佳时间吗？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"当地最佳遛狗时间因地域差异而异，请问您所在的城市是哪里？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"我在纽约市。\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"纽约市的遛狗最佳时间通常在早晨6点至8点和晚上8点至10点之间，因为这些时间段气温较低，遛狗更加舒适。但具体时间还需根据气候、气温和季节变化而定。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "## Fine-Tune the Model\n",
    "\n",
    "You can directly run the prepared training script to fine-tune the model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ab0581e-be85-45e6-a5b7-af9c42ea697b",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!export CUDA_VISIBLE_DEVICES=0\n",
    "!python ../../finetune.py \\\n",
    "    --model_name_or_path \"Qwen/Qwen-1_8B-Chat/\"\\\n",
    "    --data_path  \"Belle_sampled_qwen.json\"\\\n",
    "    --bf16 \\\n",
    "    --output_dir \"output_qwen\" \\\n",
    "    --num_train_epochs 5 \\\n",
    "    --per_device_train_batch_size 1 \\\n",
    "    --per_device_eval_batch_size 1 \\\n",
    "    --gradient_accumulation_steps 16 \\\n",
    "    --evaluation_strategy \"no\" \\\n",
    "    --save_strategy \"steps\" \\\n",
    "    --save_steps 1000 \\\n",
    "    --save_total_limit 10 \\\n",
    "    --learning_rate 1e-5 \\\n",
    "    --weight_decay 0.1 \\\n",
    "    --adam_beta2 0.95 \\\n",
    "    --warmup_ratio 0.01 \\\n",
    "    --lr_scheduler_type \"cosine\" \\\n",
    "    --logging_steps 1 \\\n",
    "    --report_to \"none\" \\\n",
    "    --model_max_length 512 \\\n",
    "    --gradient_checkpointing \\\n",
    "    --lazy_preprocess \\\n",
    "    --use_lora"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e6f28aa-1772-48ce-aa15-8cf29e7d67b5",
   "metadata": {},
   "source": [
    "## Merge Weights\n",
    "\n",
    "The training of both LoRA and Q-LoRA only saves the adapter parameters. You can load the fine-tuned model and merge weights as shown below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fd5ef2a-34f9-4909-bebe-7b3b086fd16a",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM\n",
    "from peft import PeftModel\n",
    "import torch\n",
    "\n",
    "model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-1_8B-Chat/\", torch_dtype=torch.float16, device_map=\"auto\", trust_remote_code=True)\n",
    "model = PeftModel.from_pretrained(model, \"output_qwen/\")\n",
    "merged_model = model.merge_and_unload()\n",
    "merged_model.save_pretrained(\"output_qwen_merged\", max_shard_size=\"2048MB\", safe_serialization=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e3f5b9f-63a1-4599-8d9b-a8d8f764838f",
   "metadata": {},
   "source": [
    "The tokenizer files are not saved in the new directory in this step. You can copy the tokenizer files or use the following code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10fa5ea3-dd55-4901-86af-c045d4c56533",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from transformers import AutoTokenizer\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\n",
    "    \"Qwen/Qwen-1_8B-Chat/\",\n",
    "    trust_remote_code=True\n",
    ")\n",
    "\n",
    "tokenizer.save_pretrained(\"output_qwen_merged\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "804b84d8",
   "metadata": {},
   "source": [
    "## Test the Model\n",
    "\n",
    "After merging the weights, we can test the model as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"output_qwen_merged\", trust_remote_code=True)\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    \"output_qwen_merged\",\n",
    "    device_map=\"auto\",\n",
    "    trust_remote_code=True\n",
    ").eval()\n",
    "\n",
    "response, history = model.chat(tokenizer, \"你好\", history=None)\n",
    "print(response)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `recipes/finetune/deepspeed/finetune_qlora_multi_gpu.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6e6981ab-2d9a-4280-923f-235a166855ba",
   "metadata": {},
   "source": [
    "# QLoRA Fine-Tuning Qwen-Chat Large Language Model (Multiple GPUs)\n",
    "\n",
    "Tongyi Qianwen is a large language model developed by Alibaba Cloud based on the Transformer architecture, trained on an extensive set of pre-training data. The pre-training data is diverse and covers a wide range, including a large amount of internet text, specialized books, code, etc. In addition, an AI assistant called Qwen-Chat has been created based on the pre-trained model using alignment mechanism.\n",
    "\n",
    "This notebook uses Qwen-1.8B-Chat as an example to introduce how to QLoRA fine-tune the Qianwen model using Deepspeed.\n",
    "\n",
    "## Environment Requirements\n",
    "\n",
    "Please refer to **requirements.txt** to install the required dependencies.\n",
    "\n",
    "## Preparation\n",
    "\n",
    "### Download Qwen-1.8B-Chat\n",
    "\n",
    "First, download the model files. You can choose to download directly from ModelScope."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "248488f9-4a86-4f35-9d56-50f8e91a8f11",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "execution": {
     "iopub.execute_input": "2023-12-31T08:42:52.842315Z",
     "iopub.status.busy": "2023-12-31T08:42:52.841665Z",
     "iopub.status.idle": "2023-12-31T08:44:19.832661Z",
     "shell.execute_reply": "2023-12-31T08:44:19.832193Z",
     "shell.execute_reply.started": "2023-12-31T08:42:52.842295Z"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "model_dir = snapshot_download('Qwen/Qwen-1_8B-Chat-Int4', cache_dir='.', revision='master')"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "7b2a92b1-f08e-4413-9f92-8f23761e6e1f",
   "metadata": {},
   "source": [
    "### Download Example Training Data\n",
    "\n",
    "Download the data required for training; here, we provide a tiny dataset as an example. It is sampled from [Belle](https://github.com/LianjiaTech/BELLE).\n",
    "\n",
    "Disclaimer: the dataset can be only used for the research purpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce195f08-fbb2-470e-b6c0-9a03457458c7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/Belle_sampled_qwen.json"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7226bed0-171b-4d45-a3f9-b3d81ec2bb9f",
   "metadata": {},
   "source": [
    "You can also refer to this format to prepare the dataset. Below is a simple example list with 1 sample:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"我是一个语言模型，我叫通义千问。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "You can also use multi-turn conversations as the training set. Here is a simple example:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好，能告诉我遛狗的最佳时间吗？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"当地最佳遛狗时间因地域差异而异，请问您所在的城市是哪里？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"我在纽约市。\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"纽约市的遛狗最佳时间通常在早晨6点至8点和晚上8点至10点之间，因为这些时间段气温较低，遛狗更加舒适。但具体时间还需根据气候、气温和季节变化而定。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "## Fine-Tune the Model\n",
    "\n",
    "You can directly run the prepared training script to fine-tune the model. **nproc_per_node** refers to the number of GPUs used fro training."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ab0581e-be85-45e6-a5b7-af9c42ea697b",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "execution": {
     "iopub.execute_input": "2023-12-31T08:45:37.959631Z",
     "iopub.status.busy": "2023-12-31T08:45:37.958961Z",
     "iopub.status.idle": "2023-12-31T08:46:19.501657Z",
     "shell.execute_reply": "2023-12-31T08:46:19.500854Z",
     "shell.execute_reply.started": "2023-12-31T08:45:37.959609Z"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!torchrun --nproc_per_node 2 --nnodes 1 --node_rank 0 --master_addr localhost --master_port 6601 ../../finetune.py \\\n",
    "    --model_name_or_path \"Qwen/Qwen-1_8B-Chat-Int4/\" \\\n",
    "    --data_path \"Belle_sampled_qwen.json\" \\\n",
    "    --bf16 True \\\n",
    "    --output_dir \"output_qwen\" \\\n",
    "    --num_train_epochs 5 \\\n",
    "    --per_device_train_batch_size 1 \\\n",
    "    --per_device_eval_batch_size 1 \\\n",
    "    --gradient_accumulation_steps 16 \\\n",
    "    --evaluation_strategy \"no\" \\\n",
    "    --save_strategy \"steps\" \\\n",
    "    --save_steps 1000 \\\n",
    "    --save_total_limit 10 \\\n",
    "    --learning_rate 1e-5 \\\n",
    "    --weight_decay 0.1 \\\n",
    "    --adam_beta2 0.95 \\\n",
    "    --warmup_ratio 0.01 \\\n",
    "    --lr_scheduler_type \"cosine\" \\\n",
    "    --logging_steps 1 \\\n",
    "    --report_to \"none\" \\\n",
    "    --model_max_length 512 \\\n",
    "    --gradient_checkpointing True \\\n",
    "    --lazy_preprocess True \\\n",
    "    --deepspeed \"../../finetune/ds_config_zero2.json\" \\\n",
    "    --use_lora \\\n",
    "    --q_lora"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Merge Weights\n",
    "\n",
    "The training of both LoRA and Q-LoRA only saves the adapter parameters. Note that you can not merge weights into quantized models. Instead, we can merge the weights based on the original chat model.\n",
    "\n",
    "You can load the fine-tuned model and merge weights as shown below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "snapshot_download('Qwen/Qwen-1_8B-Chat', cache_dir='.', revision='master')\n",
    "\n",
    "from transformers import AutoModelForCausalLM\n",
    "from peft import PeftModel\n",
    "import torch\n",
    "\n",
    "model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-1_8B-Chat/\", torch_dtype=torch.float16, device_map=\"auto\", trust_remote_code=True)\n",
    "model = PeftModel.from_pretrained(model, \"output_qwen/\")\n",
    "merged_model = model.merge_and_unload()\n",
    "merged_model.save_pretrained(\"output_qwen_merged\", max_shard_size=\"2048MB\", safe_serialization=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The tokenizer files are not saved in the new directory in this step. You can copy the tokenizer files or use the following code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoTokenizer\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\n",
    "    \"Qwen/Qwen-1_8B-Chat-Int4/\",\n",
    "    trust_remote_code=True\n",
    ")\n",
    "\n",
    "tokenizer.save_pretrained(\"output_qwen_merged\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Test the Model\n",
    "\n",
    "After merging the weights, we can test the model as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"output_qwen_merged\", trust_remote_code=True)\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    \"output_qwen_merged\",\n",
    "    device_map=\"auto\",\n",
    "    trust_remote_code=True\n",
    ").eval()\n",
    "\n",
    "response, history = model.chat(tokenizer, \"你好\", history=None)\n",
    "print(response)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `recipes/finetune/deepspeed/finetune_qlora_single_gpu.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6e6981ab-2d9a-4280-923f-235a166855ba",
   "metadata": {},
   "source": [
    "# QLoRA Fine-Tuning Qwen-Chat Large Language Model (Single GPU)\n",
    "\n",
    "Tongyi Qianwen is a large language model developed by Alibaba Cloud based on the Transformer architecture, trained on an extensive set of pre-training data. The pre-training data is diverse and covers a wide range, including a large amount of internet text, specialized books, code, etc. In addition, an AI assistant called Qwen-Chat has been created based on the pre-trained model using alignment mechanism.\n",
    "\n",
    "This notebook uses Qwen-1.8B-Chat as an example to introduce how to QLoRA fine-tune the Qianwen model using Deepspeed.\n",
    "\n",
    "## Environment Requirements\n",
    "\n",
    "Please refer to **requirements.txt** to install the required dependencies.\n",
    "\n",
    "## Preparation\n",
    "\n",
    "### Download Qwen-1.8B-Chat\n",
    "\n",
    "First, download the model files. You can choose to download directly from ModelScope.\n",
    "\n",
    "Note that we use the Int4 version of the models for QLoRA training."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "248488f9-4a86-4f35-9d56-50f8e91a8f11",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "model_dir = snapshot_download('Qwen/Qwen-1_8B-Chat-Int4', cache_dir='.', revision='master')"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "7b2a92b1-f08e-4413-9f92-8f23761e6e1f",
   "metadata": {},
   "source": [
    "### Download Example Training Data\n",
    "\n",
    "Download the data required for training; here, we provide a tiny dataset as an example. It is sampled from [Belle](https://github.com/LianjiaTech/BELLE).\n",
    "\n",
    "Disclaimer: the dataset can be only used for the research purpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce195f08-fbb2-470e-b6c0-9a03457458c7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/Belle_sampled_qwen.json"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7226bed0-171b-4d45-a3f9-b3d81ec2bb9f",
   "metadata": {},
   "source": [
    "You can also refer to this format to prepare the dataset. Below is a simple example list with 1 sample:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"我是一个语言模型，我叫通义千问。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "You can also use multi-turn conversations as the training set. Here is a simple example:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好，能告诉我遛狗的最佳时间吗？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"当地最佳遛狗时间因地域差异而异，请问您所在的城市是哪里？\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"我在纽约市。\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"纽约市的遛狗最佳时间通常在早晨6点至8点和晚上8点至10点之间，因为这些时间段气温较低，遛狗更加舒适。但具体时间还需根据气候、气温和季节变化而定。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "## Fine-Tune the Model\n",
    "\n",
    "You can directly run the prepared training script to fine-tune the model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ab0581e-be85-45e6-a5b7-af9c42ea697b",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "!python ../../finetune.py \\\n",
    "    --model_name_or_path \"Qwen/Qwen-1_8B-Chat-Int4/\"\\\n",
    "    --data_path  \"Belle_sampled_qwen.json\"\\\n",
    "    --bf16 \\\n",
    "    --output_dir \"output_qwen\" \\\n",
    "    --num_train_epochs 5 \\\n",
    "    --per_device_train_batch_size 1 \\\n",
    "    --per_device_eval_batch_size 1 \\\n",
    "    --gradient_accumulation_steps 16 \\\n",
    "    --evaluation_strategy \"no\" \\\n",
    "    --save_strategy \"steps\" \\\n",
    "    --save_steps 1000 \\\n",
    "    --save_total_limit 10 \\\n",
    "    --learning_rate 1e-5 \\\n",
    "    --weight_decay 0.1 \\\n",
    "    --adam_beta2 0.95 \\\n",
    "    --warmup_ratio 0.01 \\\n",
    "    --lr_scheduler_type \"cosine\" \\\n",
    "    --logging_steps 1 \\\n",
    "    --report_to \"none\" \\\n",
    "    --model_max_length 512 \\\n",
    "    --gradient_checkpointing \\\n",
    "    --lazy_preprocess \\\n",
    "    --use_lora \\\n",
    "    --q_lora \\\n",
    "    --deepspeed \"../../finetune/ds_config_zero2.json\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a50941d-3c3c-4ed2-9185-d4fe6172da2f",
   "metadata": {},
   "source": [
    "## Merge Weights\n",
    "\n",
    "The training of both LoRA and Q-LoRA only saves the adapter parameters. Note that you can not merge weights into quantized models. Instead, we can merge the weights based on the original chat model.\n",
    "\n",
    "You can load the fine-tuned model and merge weights as shown below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "909ff537-f851-488e-b1e8-1046f6852202",
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope.hub.snapshot_download import snapshot_download\n",
    "snapshot_download('Qwen/Qwen-1_8B-Chat', cache_dir='.', revision='master')\n",
    "\n",
    "from transformers import AutoModelForCausalLM\n",
    "from peft import PeftModel\n",
    "import torch\n",
    "\n",
    "model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-1_8B-Chat/\", torch_dtype=torch.float16, device_map=\"auto\", trust_remote_code=True)\n",
    "model = PeftModel.from_pretrained(model, \"output_qwen/\")\n",
    "merged_model = model.merge_and_unload()\n",
    "merged_model.save_pretrained(\"output_qwen_merged\", max_shard_size=\"2048MB\", safe_serialization=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7969df6e-ba8a-45f5-8b44-e1cbe74a8ef6",
   "metadata": {},
   "source": [
    "The tokenizer files are not saved in the new directory in this step. You can copy the tokenizer files or use the following code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c01b6a3f-036f-4b7c-b5a6-76a7b6894d4e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from transformers import AutoTokenizer\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\n",
    "    \"Qwen/Qwen-1_8B-Chat-Int4/\",\n",
    "    trust_remote_code=True\n",
    ")\n",
    "\n",
    "tokenizer.save_pretrained(\"output_qwen_merged\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2944b9b-89c7-4fb5-bd08-941d4706e943",
   "metadata": {},
   "source": [
    "## Test the Model\n",
    "\n",
    "After merging the weights, we can test the model as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b77abbb1-5b29-4eb1-8a6c-e2e146b8d33d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"output_qwen_merged\", trust_remote_code=True)\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    \"output_qwen_merged\",\n",
    "    device_map=\"auto\",\n",
    "    trust_remote_code=True\n",
    ").eval()\n",
    "\n",
    "response, history = model.chat(tokenizer, \"你好\", history=None)\n",
    "print(response)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `recipes/finetune/deepspeed/readme.md`
```markdown
# Fine-tuning Qwen Using Deepspeed


## TL;DR

We provide the official training script `finetune.py` and serveral notebooks that can be leveraged for users to finetune pre-trained models for downstream applications in a simple fashion. The algorithms that we support include full-parameter fine-tuning, LoRA fine-tuning and Q-LoRA fine-tuning. Here is the matrix of our notebooks used in different settings:

| Algorithm | Single GPU | Multiple GPUs|
| --- | --- | --- |
| Full-parameter Fine-tuning | [finetune_fullparameter_single_gpu](finetune_fullparameter_single_gpu.ipynb) | [finetune_fullparameter_multi_gpu](finetune_fullparameter_multi_gpu.ipynb) |
| LoRA Fine-tuning | [finetune_lora_single_gpu](finetune_lora_single_gpu.ipynb) | [finetune_lora_multi_gpu](finetune_lora_multi_gpu.ipynb) |
| Q-LoRA Fine-tuning | [finetune_qlora_single_gpu](finetune_qlora_single_gpu.ipynb) | [finetune_qlora_multi_gpu](finetune_qlora_multi_gpu.ipynb) |

## Requirements

### Environments

The basic requirements for running Qwen models include:

- python 3.8 and above
- pytorch 1.12 and above, 2.0 and above are recommended
- transformers 4.32 and above
- CUDA 11.4 and above are recommended (this is for GPU users, flash-attention users, etc.)

Our notebooks launch fine-tuning with DeepSpeed and Peft.
(Note: this may have conflicts with the latest version of pydantic and you should use make sure `pydantic<2.0`.)
You can install them by:
```bash
pip install peft deepspeed
```

### Settings and GPU Requirements

We first provide the support matrix for different learning settings. Full-parameter fine-tuning requires updating all parameters in the whole training process.
In comparison with full-parameter fine-tuning, LoRA only updates the parameters of adapter layers but keeps the original large language model layers frozen. This allows much fewer memory costs and thus fewer computation costs. If you still suffer from insufficient memory, you can consider Q-LoRA, which uses the quantized large language model to allow even fewer memory costs. Generally, the GPU consumption rule for tuning Qwen is as follows: full parameter > full parameter (ZeRO2) > full parameter (ZeRO3) > LoRA > LoRA (ZeRO2) > LoRA (ZeRO3) > Q-LoRA > Q-LoRA (ZeRO2).

| Setting | Full-parameter | LoRA | Q-LoRA |
| --- | --- | --- | --- |
| Base | Yes (up to ZeRO3) | Yes (up to ZeRO2) | No |
| Chat | Yes (up to ZeRO3) | Yes (up to ZeRO3) | No |
| Chat-Int4/8 | No | No | Yes |

Here are some useful suggestions for choosing different fine-tuning settings based on GPU memory, espcially for users with GeForce RTX 3090/4090 (24GB) GPUs (or similar), and A100 (80GB) GPUs (or similar). In the experiments, we uniformly use a batch size of 1, gradient accumulation of 16, and max length of 512. Other parameters are set as the same shown in our notebooks. The results are as follows.

| GPU Memory | Number of GPUs |  Qwen-1.8B-Chat | Qwen-7B-Chat | Qwen-14B-Chat | Qwen-72B-Chat |
| --- | --- | --- | --- | --- |  --- |
| 24GB | *1 | Full Parameter | LoRA | Q-LoRA | N/A |
| 24GB | *2 | Full Parameter | LoRA | Q-LoRA | N/A |
| 24GB | *4 | Full Parameter | LoRA | LoRA (w/ ZeRO3) | N/A |
| 80GB | *1 | Full Parameter | LoRA | LoRA | Q-LoRA |
| 80GB | *2 | Full Parameter | Full Parameter (w/ ZeRO3) | LoRA (w/ ZeRO2) | TBD |
| 80GB | *4 | Full Parameter | Full Parameter (w/ ZeRO2) | Full Parameter (w/ ZeRO3) | LoRA (w/ ZeRO3) |

Using other configurations of LoRA/Q-LoRA and ZeRO stages will easily result in failures.


## Data Preparation

To prepare your training data, you need to put all the samples into a list and save it to a json file. Each sample is a dictionary consisting of an id and a list for conversation. Below is a simple example list with 1 sample:
```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "你好"
      },
      {
        "from": "assistant",
        "value": "我是一个语言模型，我叫通义千问。"
      }
    ]
  }
]
```

You can also use multi-turn conversations as the training set. Here is a simple example:

```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "你好"
      },
      {
        "from": "assistant",
        "value": "你好！我是一名AI助手，我叫通义千问，有需要请告诉我。"
      },
      {
        "from": "user",
        "value": "你都能做什么"
      },
      {
        "from": "assistant",
        "value": "我能做很多事情，包括但不限于回答各种领域的问题、提供实用建议和指导、进行多轮对话交流、文本生成等。"
      }
    ]
  }
]
```


## Single-GPU Training

In the single-GPU training setting, we provide three notebooks:

- [finetune_fullparameter_single_gpu](finetune_fullparameter_single_gpu.ipynb)
- [finetune_lora_single_gpu](finetune_lora_single_gpu.ipynb)
- [finetune_qlora_single_gpu](finetune_qlora_single_gpu.ipynb)

### Full-parameter Fine-tuning

To launch your training, run the following command (with hyper-parameter settings omitted):
```bash
python finetune.py \
    --model_name_or_path $MODEL \
    --data_path  $DATA \
    --output_dir $OUTPUT
```
Remember to specify the correct model name or path, the data path, as well as the output directory.

### LoRA Fine-tuning

Similarly, to run LoRA, use another notebook to run the command as shown below. Before you start, make sure that you have installed `peft`. Also, you need to specify your paths to your model, data, and output. We advise you to use absolute path for your pre-trained model. This is because LoRA only saves the adapter and the absolute path in the adapter configuration json file is used for finding out the pre-trained model to load. 
```bash
python finetune.py \
    --model_name_or_path $MODEL \
    --data_path  $DATA \
    --output_dir $OUTPUT \
    --use_lora
```
Note that if you use LoRA to fine-tune the base language model, e.g., Qwen-7B, instead of chat models, e.g., Qwen-7B-Chat, the script automatically switches the embedding and output layer as trainable parameters. This is because the base language model has no knowledge of special tokens brought by ChatML format. Thus these layers should be updated for the model to understand and predict the tokens. Or in another word, if your training brings in special tokens in LoRA, you should set the layers to trainable parameters by setting `modules_to_save` inside the code. Check out the following code in the training script `finetune.py`:
```python
is_chat_model = 'chat' in model_args.model_name_or_path.lower()
if training_args.use_lora:
  if lora_args.q_lora or is_chat_model:
    modules_to_save = None
  else:
    modules_to_save = ["wte", "lm_head"]
    lora_config = LoraConfig(
            r=lora_args.lora_r,
            lora_alpha=lora_args.lora_alpha,
            target_modules=lora_args.lora_target_modules,
            lora_dropout=lora_args.lora_dropout,
            bias=lora_args.lora_bias,
            task_type="CAUSAL_LM",
            modules_to_save=modules_to_save  # This argument serves for adding new tokens.
    )
    ...
    model = get_peft_model(model, lora_config)
    ...
```
Pay attention that the script relies on the model path to identify the model type, so please keep `chat` in the chat model paths.



### Q-LoRA Fine-tuning

To run single-GPU Q-LoRA training, you may need to install `mpi4py`. Directly run the following script:
```bash
python finetune.py \
    --model_name_or_path $MODEL \
    --data_path  $DATA \
    --output_dir $OUTPUT \
    --use_lora \
    --q_lora \
    --deepspeed "ds_config_zero2.json"
```

For Q-LoRA, we advise you to load our provided quantized model, e.g., Qwen-7B-Chat-Int4. You **SHOULD NOT** use the bf16 models. Different from full-parameter fine-tuning and LoRA, only fp16 is supported for Q-LoRA. For single-GPU training, we have to use DeepSpeed for mixed-precision training due to our observation of errors caused by torch amp. Besides, for Q-LoRA, the troubles with the special tokens in LoRA still exist. However, as we only provide the Int4 models for chat models, which means the language model has learned the special tokens of ChatML format, you have no worry about the layers. Note that the layers of the Int4 model should not be trainable, and thus if you introduce special tokens in your training, Q-LoRA might not work.


In default, our notebooks provide training codes for Qwen-1.8B-Chat.
You can also run the training script to fine-tune other version of the Qwen-series models. We profile the GPU memory usage of all versions based on our notebooks (without changing any hyper-parameter settings) on a single A800 GPU (80GB). The statistics are listed below:

| Training | Qwen-1.8B-Chat | Qwen-7B-Chat | Qwen-14B-Chat | Qwen-72B-Chat |
| --- | --- | --- | --- | --- |
| Full Parameter | 19.6GB | 76.8GB | OOM | OOM |
| LoRA | 7.4GB | 20.3GB | 34.2GB | OOM |
| Q-LoRA | 6.1GB | 12.5GB | 17.8GB | 61.9GB |


### Merging Weights from LoRA and Q-LoRA


#### Inference with Adapters

Different from full-parameter fine-tuning, the training of both LoRA and Q-LoRA only saves the adapter parameters. Suppose your training starts from Qwen-7B, you can load the fine-tuned model for inference as shown below:
```python
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    path_to_adapter, # path to the output directory
    trust_remote_code=True
)
model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()

response, history = model.chat(tokenizer, "你好", history=None)
```

#### Inference with Merged Weights

If you want to merge the adapters and save the fine-tuned model as a standalone model, take LoRA as an example, you can run the following codes:
```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    path_to_adapter, # path to the output directory
    device_map="auto",
    trust_remote_code=True
).eval()

merged_model = model.merge_and_unload()
# max_shard_size and safe serialization are not necessary. 
# They respectively work for sharding checkpoint and save the model to safetensors.
merged_model.save_pretrained(new_model_directory, max_shard_size="2048MB", safe_serialization=True)
```

The `new_model_directory` directory will contain the merged model weights and module files. Please note that `*.cu` and `*.cpp` files may be missing in the saved files. If you wish to use the KV cache functionality, please manually copy them. Besides, the tokenizer files are not saved in the new directory in this step. You can copy the tokenizer files or use the following code:
```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    path_to_adapter, # path to the output directory
    trust_remote_code=True
)
tokenizer.save_pretrained(new_model_directory)
```
Next, the model with merged weights can be loaded by the following code:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(new_model_directory, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    new_model_directory,
    device_map="auto",
    trust_remote_code=True
).eval()
response, history = model.chat(tokenizer, "你好", history=None)
```

Note that you can not merge weights into quantized models. Instead, we can merge the weights based on the original chat model. Take Qwen-7B-Chat-In4 as an example. 
```python
from transformers import AutoModelForCausalLM
from peft import PeftModel
import torch

# Here, we load the original Qwen-7B-Chat model, instead of the Qwen-7B-Chat-Int4 model.
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", torch_dtype=torch.float16, device_map="auto", trust_remote_code=True)
# We merge the learned adapter to the Qwen-7B-Chat.
model = PeftModel.from_pretrained(model, path_to_adapter)
merged_model = model.merge_and_unload()
# We save the model to a new path.
merged_model.save_pretrained(path_to_new_model, max_shard_size="2048MB", safe_serialization=True)
```


## Multi-GPU Training

In the multi-GPU training setting, we provide three notebooks:

- [finetune_fullparameter_multi_gpu](finetune_fullparameter_multi_gpu.ipynb)
- [finetune_lora_multi_gpu](finetune_lora_multi_gpu.ipynb)
- [finetune_qlora_multi_gpu](finetune_qlora_multi_gpu.ipynb)

We use `torchrun` to launch the training job on multiple GPUs:

```bash
# for full-parameter fine-tuning
torchrun --nproc_per_node 2 --nnodes 1 --node_rank 0 --master_addr localhost --master_port 6601 finetune.py \
    --model_name_or_path $MODEL \
    --data_path  $DATA \
    --output_dir $OUTPUT \
    --deepspeed "ds_config_zero2.json"

# for LoRA fine-tuning
torchrun --nproc_per_node 2 --nnodes 1 --node_rank 0 --master_addr localhost --master_port 6601 finetune.py \
    --model_name_or_path $MODEL \
    --data_path  $DATA \
    --output_dir $OUTPUT \
    --deepspeed "ds_config_zero2.json" \
    --use_lora

# for Q-LoRA fine-tuning
torchrun --nproc_per_node 2 --nnodes 1 --node_rank 0 --master_addr localhost --master_port 6601 finetune.py \
    --model_name_or_path $MODEL \
    --data_path  $DATA \
    --output_dir $OUTPUT \
    --deepspeed "ds_config_zero2.json" \
    --use_lora \
    --q_lora
```

For multi-GPU training, you also need to specify proper hyperparameters for distributed training based on your machine. Besides, we advise you to specify your maximum sequence length with the argument `--model_max_length`, based on your consideration of data, memory footprint, and training speed.
For the usage of `torchrun` and distrubuted arguments, please refer to [here](https://pytorch.org/docs/stable/elastic/run.html).
Additionally, we find that there is a significant gap between the memory footprint of LoRA with and without these trainable parameters. Therefore, if you have trouble with memory, we advise you to LoRA fine-tune the chat models. Check the profile below for more information. 


### Multi-node Fine-tuning

Our provided scripts also support multi-node fine-tuning. You can refer to the comments in the scripts to correctly set corresponding arguments and launch the script on each node. For more information about multi-node distributed training, please refer to [torchrun](https://pytorch.org/docs/stable/elastic/run.html).

Note: DeepSpeed ZeRO 3 requires much greater inter-node communication rate than ZeRO 2, which will significantly reduce the training speed in the case of multinode finetuning. Therefore, we do not recommend using DeepSpeed ZeRO 3 configurations in multi-node fine-tuning scripts.

### Profiling of Memory and Speed

We profile the GPU memory and training speed of both LoRA (LoRA (emb) refers to training the embedding and output layer, while LoRA has no trainable embedding and output layer) and Q-LoRA in the setup of single-GPU training. In this test, we experiment on a single A100-SXM4-80G GPU, and we use CUDA 11.8 and Pytorch 2.0. Flash attention 2 is applied. We uniformly use a batch size of 1 and gradient accumulation of 8. We profile the memory (GB) and speed (s/iter) of inputs of different lengths, namely 256, 512, 1024, 2048, 4096, and 8192. We also report the statistics of full-parameter fine-tuning with Qwen-7B on 2 A100 GPUs. We only report the statistics of 256, 512, and 1024 tokens due to the limitation of GPU memory. 

For Qwen-7B, we also test the performance of multi-node fine-tuning. We experiment using two servers, each containing two A100-SXM4-80G GPUs, and the rest of configurations are the same as other Qwen-7B experiments. The results of multi-node fine-tuning are marked as LoRA (multinode) in the table.

For Qwen-72B, we experiment in two ways: 1) LoRA fine-tuning + DeepSpeed ZeRO 3 on 4 A100-SXM4-80G GPUs and 2) Q-LoRA (int4) fine-tuning on a single A100-SXM4-80G GPU. Note that OOM occurs on 4 A100-SXM4-80G GPUs both with LoRA (emb) fine-tuning and LoRA fine-tuning without Deepspeed ZeRO 3 (you can pass `--deepspeed ds_config_zero3.json` to `finetune_lora_ds.sh` to enable DeepSpeed ZeRO 3).

The statistics are listed below:

<table>
    <tr>
      <th rowspan="2">Model Size</th><th rowspan="2">Method</th><th rowspan="2">#Nodes</th><th rowspan="2">#GPUs per node</th><th colspan="6" align="center">Sequence Length</th>
    </tr>
    <tr>
        <th align="center">256</th><th align="center">512</th><th align="center">1024</th><th align="center">2048</th><th align="center">4096</th><th align="center">8192</th>
    </tr>
    <tr>
        <th rowspan="4">1.8B</th><td>LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">6.7G / 1.0s/it</td><td align="center">7.4G / 1.0s/it</td><td align="center">8.4G / 1.1s/it</td><td align="center">11.0G / 1.7s/it</td><td align="center">16.2G / 3.3s/it</td><td align="center">21.8G / 6.8s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td>
        <td>1</td><td>1</td>
        <td align="center">13.7G / 1.0s/it</td><td align="center">14.0G / 1.0s/it</td><td align="center">14.0G / 1.1s/it</td><td align="center">15.1G / 1.8s/it</td><td align="center">19.7G / 3.4s/it</td><td align="center">27.7G / 7.0s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">5.8G / 1.4s/it</td><td align="center">6.0G / 1.4s/it</td><td align="center">6.6G / 1.4s/it</td><td align="center">7.8G / 2.0s/it</td><td align="center">10.2G / 3.4s/it</td><td align="center">15.8G / 6.5s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td>
        <td>1</td><td>1</td>
        <td align="center">43.5G / 2.1s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.2s/it</td><td align="center">43.5G / 2.3s/it</td><td align="center">47.1G / 2.8s/it</td><td align="center">48.3G / 5.6s/it</td>
    </tr>
    <tr>
        <th rowspan="5">7B</th>
        <td>LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">20.1G / 1.2s/it</td><td align="center">20.4G / 1.5s/it</td><td align="center">21.5G / 2.8s/it</td><td align="center">23.8G / 5.2s/it</td><td align="center">29.7G / 10.1s/it</td><td align="center">36.6G / 21.3s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td>
        <td>1</td><td>1</td>
        <td align="center">33.7G / 1.4s/it</td><td align="center">34.1G / 1.6s/it</td><td align="center">35.2G / 2.9s/it</td><td align="center">35.1G / 5.3s/it</td><td align="center">39.2G / 10.3s/it</td><td align="center">48.5G / 21.7s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">11.5G / 3.0s/it</td><td align="center">11.5G / 3.0s/it</td><td align="center">12.3G / 3.5s/it</td><td align="center">13.9G / 7.0s/it</td><td align="center">16.9G / 11.6s/it</td><td align="center">23.5G / 22.3s/it</td>
    </tr>
    <tr>
        <td>Full-parameter</td>
<td>1</td><td>2</td>
<td align="center">139.2G / 4.0s/it</td><td align="center">148.0G / 4.0s/it</td><td align="center">162.0G / 4.5s/it</td><td align="center">-</td><td align="center">-</td><td align="center">-</td>
    </tr>
    <tr>
        <td>LoRA (multinode)</td>
        <td>2</td><td>2</td>
        <td align="center">74.7G / 2.09s/it</td><td align="center">77.6G / 3.16s/it</td><td align="center">84.9G / 5.17s/it</td><td align="center">95.1G / 9.25s/it</td><td align="center">121.1G / 18.1s/it</td><td align="center">155.5G / 37.4s/it</td>
    </tr>
    <tr>
        <th rowspan="3">14B</th>
        <td>LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">34.6G / 1.6s/it</td><td align="center">35.1G / 2.4s/it</td><td align="center">35.3G / 4.4s/it</td><td align="center">37.4G / 8.4s/it</td><td align="center">42.5G / 17.0s/it</td><td align="center">55.2G / 36.0s/it</td>
    </tr>
    <tr>
        <td>LoRA (emb)</td>
        <td>1</td><td>1</td>
        <td align="center">51.2 / 1.7s/it</td><td align="center">51.1G / 2.6s/it</td><td align="center">51.5G / 4.6s/it</td><td align="center">54.1G / 8.6s/it</td><td align="center">56.8G / 17.2s/it</td><td align="center">67.7G / 36.3s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">18.7G / 5.3s/it</td><td align="center">18.4G / 6.3s/it</td><td align="center">18.9G / 8.2s/it</td><td align="center">19.9G / 11.8s/it</td><td align="center">23.0G / 20.1s/it</td><td align="center">27.9G / 38.3s/it</td>
    </tr>
    <tr>
        <th rowspan="2">72B</th>
        <td>LoRA + Deepspeed Zero3</td>
        <td>1</td><td>4</td>
        <td align="center">215.4G / 17.6s/it</td><td align="center">217.7G / 20.5s/it</td><td align="center">222.6G / 29.4s/it</td><td align="center">228.8G / 45.7s/it</td><td align="center">249.0G / 83.4s/it</td><td align="center">289.2G / 161.5s/it</td>
    </tr>
    <tr>
        <td>Q-LoRA</td>
        <td>1</td><td>1</td>
        <td align="center">61.4G / 27.4s/it</td><td align="center">61.4G / 31.5s/it</td><td align="center">62.9G / 41.4s/it</td><td align="center">64.1G / 59.5s/it</td><td align="center">68.0G / 97.7s/it</td><td align="center">75.6G / 179.8s/it</td>
    </tr>
</table>
<br>











```

## File: `recipes/finetune/deepspeed/requirements.txt`
```
deepspeed
peft
```

## File: `recipes/finetune/swift/README.md`
```markdown
## Introduction
[SWIFT](https://github.com/modelscope/swift) (Scalable lightWeight Infrastructure for Fine-Tuning) is an extensible framwork designed to faciliate lightweight model fine-tuning and inference. It integrates implementations for various efficient fine-tuning methods, by embracing approaches that is parameter-efficient, memory-efficient, and time-efficient. SWIFT integrates seamlessly into ModelScope ecosystem and offers the capabilities to finetune various models, with a primary emphasis on LLMs and vision models. Additionally, SWIFT is fully compatible with PEFT, enabling users to leverage the familiar Peft interface to finetune ModelScope models.

## Installation

```shell
# Set the global pip mirror
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
# Install ms-swift
git clone https://github.com/modelscope/swift.git
cd swift
pip install -e .[llm]

# If you want to use deepspeed
pip install deepspeed -U

# If you want to use qlora training based on auto_gptq (recommended, performs better than bnb)
# Models supporting auto_gptq: `https://github.com/modelscope/swift/blob/main/docs/source/LLM/支持的模型和数据集.md#模型`
# There's a version correspondence between auto_gptq and cuda; refer to `https://github.com/PanQiWei/AutoGPTQ#quick-installation` for selecting the appropriate version
pip install auto_gptq -U

# If you want to use qlora training based on bnb
pip install bitsandbytes -U

# Environment alignment (run the following commands if you encounter errors; the repository is tested with the latest environment)
pip install -r requirements/framework.txt  -U
pip install -r requirements/llm.txt  -U
```

## WebUI Usage

Run the following command to start the webui and conduct model training and inference through the graphical interface:
```shell
swift web-ui
```
A screenshot example can be found at:
![image](https://modelscope.oss-cn-beijing.aliyuncs.com/resource/swift_webui.jpg)

## Fine-tuning

```python
# Experimental environment: A10, 3090, V100, ...
# GPU memory requirement: 20GB
CUDA_VISIBLE_DEVICES=0 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --dataset blossom-math-zh \
    --output_dir output \

# Use your own dataset
CUDA_VISIBLE_DEVICES=0 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --custom_train_dataset_path chatml.jsonl \
    --output_dir output \

# Using DDP (Distributed Data Parallel)
# Experimental environment: 2 * 3090
# GPU memory requirement: 2 * 23GB
CUDA_VISIBLE_DEVICES=0,1 \
NPROC_PER_NODE=2 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --dataset blossom-math-zh \
    --output_dir output \

# Multi-machine multi-GPU setup
# node0
CUDA_VISIBLE_DEVICES=0,1,2,3 \
NNODES=2 \
NODE_RANK=0 \
MASTER_ADDR=127.0.0.1 \
NPROC_PER_NODE=4 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --dataset blossom-math-zh \
    --output_dir output \
# node1
CUDA_VISIBLE_DEVICES=0,1,2,3 \
NNODES=2 \
NODE_RANK=1 \
MASTER_ADDR=xxx.xxx.xxx.xxx \
NPROC_PER_NODE=4 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --dataset blossom-math-zh \
    --output_dir output \
```
For more fine-tuning methods, please refer to [here](https://github.com/modelscope/swift/blob/main/docs/source/LLM/LLM%E5%BE%AE%E8%B0%83%E6%96%87%E6%A1%A3.md#%E5%BE%AE%E8%B0%83).



Examples

| 模型名称          | 训练方法                                                                                             |
|:-------------------|:---------------------------------------------------------------------------------------------------------------------------|
| qwen_14b           | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b/lora_ddp_ds)             |
| qwen_14b           | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b/qlora)                         |
| qwen_14b           | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b/qlora_ddp_ds)           |
| qwen_14b_chat      | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat/lora_ddp_ds)        |
| qwen_14b_chat      | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat/qlora)                    |
| qwen_14b_chat      | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat/qlora_ddp_ds)      |
| qwen_14b_chat_int4 | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat_int4/qlora)               |
| qwen_14b_chat_int4 | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat_int4/qlora_ddp_ds) |
| qwen_14b_chat_int8 | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat_int8/qlora)               |
| qwen_14b_chat_int8 | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat_int8/qlora_ddp_ds) |
| qwen_1_8b_chat     | [full](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_1_8b_chat/full)                     |
| qwen_1_8b_chat     | [full_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_1_8b_chat/full_ddp)             |
| qwen_72b_chat      | [lora_mp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat/lora_mp)                |
| qwen_72b_chat      | [lora_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat/lora_mp_ddp)        |
| qwen_72b_chat      | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat/qlora)                    |
| qwen_72b_chat_int4 | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat_int4/qlora_ddp_ds) |
| qwen_72b_chat_int8 | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat_int8/qlora_ddp_ds) |
| qwen_7b            | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b/lora_ddp_ds)              |
| qwen_7b            | [qlora_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b/qlora_ddp)                  |
| qwen_7b_chat       | [full](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/full)                       |
| qwen_7b_chat       | [full_freeze_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/full_freeze_ddp) |
| qwen_7b_chat       | [full_mp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/full_mp)                 |
| qwen_7b_chat       | [full_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/full_mp_ddp)         |
| qwen_7b_chat       | [lora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/lora)                       |
| qwen_7b_chat       | [lora_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/lora_ddp)               |
| qwen_7b_chat       | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/lora_ddp_ds)         |
| qwen_7b_chat       | [lora_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/lora_mp_ddp)         |
| qwen_7b_chat       | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/qlora)                     |
| qwen_7b_chat       | [qlora_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/qlora_ddp)             |
| qwen_7b_chat       | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/qlora_ddp_ds)       |
| qwen_7b_chat_int4  | [qalora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int4/qalora)              |
| qwen_7b_chat_int4  | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int4/qlora)                |
| qwen_7b_chat_int4  | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int4/qlora_ddp_ds)  |
| qwen_7b_chat_int8  | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int8/qlora)                |
| qwen_7b_chat_int8  | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int8/qlora_ddp_ds)  |
| qwen_audio_chat    | [full_mp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_audio_chat/full_mp)              |
| qwen_audio_chat    | [full_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_audio_chat/full_mp_ddp)      |
| qwen_audio_chat    | [lora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_audio_chat/lora)                    |
| qwen_audio_chat    | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_audio_chat/lora_ddp_ds)      |
| qwen_vl            | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl/lora_ddp_ds)              |
| qwen_vl_chat       | [full_mp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/full_mp)                 |
| qwen_vl_chat       | [full_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/full_mp_ddp)         |
| qwen_vl_chat       | [lora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/lora)                       |
| qwen_vl_chat       | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/lora_ddp_ds)         |
| qwen_vl_chat       | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/qlora)                     |
| qwen_vl_chat_int4  | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat_int4/qlora)                |
| qwen_vl_chat_int4  | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat_int4/qlora_ddp_ds)  |


## Inference

```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

from swift.llm import (
    get_model_tokenizer, get_template, inference, ModelType, get_default_template_type,
)
from swift.utils import seed_everything

model_type = ModelType.qwen_7b_chat
template_type = get_default_template_type(model_type)
print(f'template_type: {template_type}')  # template_type: qwen


kwargs = {}
# kwargs['use_flash_attn'] = True  # Use flash_attn if desired

model, tokenizer = get_model_tokenizer(model_type, model_kwargs={'device_map': 'auto'}, **kwargs)
# Modify max_new_tokens
model.generation_config.max_new_tokens = 128

template = get_template(template_type, tokenizer)
seed_everything(42)
query = 'What is the provincial capital of Zhejiang?'
response, history = inference(model, template, query)
print(f'query: {query}')
print(f'response: {response}')

query = 'What delicious food can be found here?'
response, history = inference(model, template, query, history)
print(f'query: {query}')
print(f'response: {response}')
print(f'history: {history}')

"""Output[0]:
query: What is the provincial capital of Zhejiang?
response: The provincial capital of Zhejiang is Hangzhou.
query: What delicious food can be found here?
response: Hangzhou has many famous delicacies, such as West Lake Vinegar Fish, Longjing Shrimp, Sweet and Sour Spare Ribs, and Maodu. Additionally, there are unique Hangzhou-style pastries like Osmanthus Cake, Lotus Paste Pastry, and Aiwo Steamed Rice Cakes.
history: [('What is the provincial capital of Zhejiang?', 'The provincial capital of Zhejiang is Hangzhou.'), ('What delicious food can be found here?', 'Hangzhou has many famous delicacies, such as West Lake Vinegar Fish, Longjing Shrimp, Sweet and Sour Spare Ribs, and Maodu. Additionally, there are unique Hangzhou-style pastries like Osmanthus Cake, Lotus Paste Pastry, and Aiwo Steamed Rice Cakes.')]
"""

# Streaming dialogue output with verbose mode
inference(model, template, 'What was the first question?', history, verbose=True, stream=True)
"""Output[1]:
[PROMPT]
You asked your first question, "What is the provincial capital of Zhejiang?"
[OUTPUT] Your first question was “What is the provincial capital of Zhejiang?”
"""

For more on inference usage, please refer to [here](https://github.com/modelscope/swift/blob/main/docs/source/LLM/LLM_Inference_Guide.md).
```

## File: `recipes/finetune/swift/README_CN.md`
```markdown
## 介绍
[SWIFT](https://github.com/modelscope/swift)（Scalable lightWeight Infrastructure for Fine-Tuning）是一个可扩展的轻量级一站式训练、推理深度学习框架。它集成了各种高效的微调方法，如LoRA、QLoRA、阿里云自研的ResTuning-Bypass等，以及开箱即用的训练推理脚本，使开发者可以在单张商业级显卡上微调推理LLM&AIGC模型。此外，SWIFT与PEFT完全兼容，使开发者可以在ModelScope模型体系中使用PEFT的能力。

## 安装
```shell
# 设置pip全局镜像
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
# 安装ms-swift
git clone https://github.com/modelscope/swift.git
cd swift
pip install -e .[llm]

# 如果你想要使用deepspeed.
pip install deepspeed -U

# 如果你想要使用基于auto_gptq的qlora训练. (推荐, 效果优于bnb)
# 支持auto_gptq的模型: `https://github.com/modelscope/swift/blob/main/docs/source/LLM/支持的模型和数据集.md#模型`
# auto_gptq和cuda版本有对应关系，请按照`https://github.com/PanQiWei/AutoGPTQ#quick-installation`选择版本
pip install auto_gptq -U

# 如果你想要使用基于bnb的qlora训练.
pip install bitsandbytes -U

# 环境对齐 (如果你运行错误, 可以跑下面的代码, 仓库使用最新环境测试)
pip install -r requirements/framework.txt  -U
pip install -r requirements/llm.txt  -U
```


## webui使用

执行如下命令启动webui通过界面方式进行模型训练推理
```shell
swift web-ui
```
界面示例如下
![image](https://modelscope.oss-cn-beijing.aliyuncs.com/resource/swift_webui.jpg)

## 微调
```python
# Experimental environment: A10, 3090, V100, ...
# 20GB GPU memory
CUDA_VISIBLE_DEVICES=0 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --dataset blossom-math-zh \
    --output_dir output \

# 使用自己的数据集
CUDA_VISIBLE_DEVICES=0 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --custom_train_dataset_path chatml.jsonl \
    --output_dir output \

# 使用DDP
# Experimental environment: 2 * 3090
# 2 * 23GB GPU memory
CUDA_VISIBLE_DEVICES=0,1 \
NPROC_PER_NODE=2 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --dataset blossom-math-zh \
    --output_dir output \

# 多机多卡
# node0
CUDA_VISIBLE_DEVICES=0,1,2,3 \
NNODES=2 \
NODE_RANK=0 \
MASTER_ADDR=127.0.0.1 \
NPROC_PER_NODE=4 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --dataset blossom-math-zh \
    --output_dir output \
# node1
CUDA_VISIBLE_DEVICES=0,1,2,3 \
NNODES=2 \
NODE_RANK=1 \
MASTER_ADDR=xxx.xxx.xxx.xxx \
NPROC_PER_NODE=4 \
swift sft \
    --model_id_or_path qwen/Qwen-7B-Chat \
    --dataset blossom-math-zh \
    --output_dir output \
```
更多微调方法参考[这里](https://github.com/modelscope/swift/blob/main/docs/source/LLM/LLM%E5%BE%AE%E8%B0%83%E6%96%87%E6%A1%A3.md#%E5%BE%AE%E8%B0%83)

已有微调代码示例
| 模型名称          | 训练方法                                                                                             |
|:-------------------|:---------------------------------------------------------------------------------------------------------------------------|
| qwen_14b           | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b/lora_ddp_ds)             |
| qwen_14b           | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b/qlora)                         |
| qwen_14b           | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b/qlora_ddp_ds)           |
| qwen_14b_chat      | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat/lora_ddp_ds)        |
| qwen_14b_chat      | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat/qlora)                    |
| qwen_14b_chat      | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat/qlora_ddp_ds)      |
| qwen_14b_chat_int4 | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat_int4/qlora)               |
| qwen_14b_chat_int4 | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat_int4/qlora_ddp_ds) |
| qwen_14b_chat_int8 | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat_int8/qlora)               |
| qwen_14b_chat_int8 | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_14b_chat_int8/qlora_ddp_ds) |
| qwen_1_8b_chat     | [full](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_1_8b_chat/full)                     |
| qwen_1_8b_chat     | [full_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_1_8b_chat/full_ddp)             |
| qwen_72b_chat      | [lora_mp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat/lora_mp)                |
| qwen_72b_chat      | [lora_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat/lora_mp_ddp)        |
| qwen_72b_chat      | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat/qlora)                    |
| qwen_72b_chat_int4 | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat_int4/qlora_ddp_ds) |
| qwen_72b_chat_int8 | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_72b_chat_int8/qlora_ddp_ds) |
| qwen_7b            | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b/lora_ddp_ds)              |
| qwen_7b            | [qlora_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b/qlora_ddp)                  |
| qwen_7b_chat       | [full](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/full)                       |
| qwen_7b_chat       | [full_freeze_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/full_freeze_ddp) |
| qwen_7b_chat       | [full_mp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/full_mp)                 |
| qwen_7b_chat       | [full_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/full_mp_ddp)         |
| qwen_7b_chat       | [lora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/lora)                       |
| qwen_7b_chat       | [lora_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/lora_ddp)               |
| qwen_7b_chat       | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/lora_ddp_ds)         |
| qwen_7b_chat       | [lora_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/lora_mp_ddp)         |
| qwen_7b_chat       | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/qlora)                     |
| qwen_7b_chat       | [qlora_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/qlora_ddp)             |
| qwen_7b_chat       | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat/qlora_ddp_ds)       |
| qwen_7b_chat_int4  | [qalora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int4/qalora)              |
| qwen_7b_chat_int4  | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int4/qlora)                |
| qwen_7b_chat_int4  | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int4/qlora_ddp_ds)  |
| qwen_7b_chat_int8  | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int8/qlora)                |
| qwen_7b_chat_int8  | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_7b_chat_int8/qlora_ddp_ds)  |
| qwen_audio_chat    | [full_mp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_audio_chat/full_mp)              |
| qwen_audio_chat    | [full_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_audio_chat/full_mp_ddp)      |
| qwen_audio_chat    | [lora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_audio_chat/lora)                    |
| qwen_audio_chat    | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_audio_chat/lora_ddp_ds)      |
| qwen_vl            | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl/lora_ddp_ds)              |
| qwen_vl_chat       | [full_mp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/full_mp)                 |
| qwen_vl_chat       | [full_mp_ddp](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/full_mp_ddp)         |
| qwen_vl_chat       | [lora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/lora)                       |
| qwen_vl_chat       | [lora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/lora_ddp_ds)         |
| qwen_vl_chat       | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat/qlora)                     |
| qwen_vl_chat_int4  | [qlora](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat_int4/qlora)                |
| qwen_vl_chat_int4  | [qlora_ddp_ds](https://github.com/modelscope/swift/tree/main/examples/pytorch/llm/scripts/qwen_vl_chat_int4/qlora_ddp_ds)  |

## 推理

```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

from swift.llm import (
    get_model_tokenizer, get_template, inference, ModelType, get_default_template_type,
)
from swift.utils import seed_everything

model_type = ModelType.qwen_7b_chat
template_type = get_default_template_type(model_type)
print(f'template_type: {template_type}')  # template_type: qwen


kwargs = {}
# kwargs['use_flash_attn'] = True  # 使用flash_attn

model, tokenizer = get_model_tokenizer(model_type, model_kwargs={'device_map': 'auto'}, **kwargs)
# 修改max_new_tokens
model.generation_config.max_new_tokens = 128

template = get_template(template_type, tokenizer)
seed_everything(42)
query = '浙江的省会在哪里？'
response, history = inference(model, template, query)
print(f'query: {query}')
print(f'response: {response}')
query = '这有什么好吃的？'
response, history = inference(model, template, query, history)
print(f'query: {query}')
print(f'response: {response}')
print(f'history: {history}')

"""Out[0]
query: 浙江的省会在哪里？
response: 浙江省的省会是杭州。
query: 这有什么好吃的？
response: 杭州市有很多著名的美食，例如西湖醋鱼、龙井虾仁、糖醋排骨、毛血旺等。此外，还有杭州特色的点心，如桂花糕、荷花酥、艾窝窝等。
history: [('浙江的省会在哪里？', '浙江省的省会是杭州。'), ('这有什么好吃的？', '杭州市有很多著名的美食，例如西湖醋鱼、龙井虾仁、糖醋排骨、毛血旺等。此外，还有杭州特色的点心，如桂花糕、荷花酥、艾窝窝等。')]
"""

# 流式输出对话模板
inference(model, template, '第一个问题是什么', history, verbose=True, stream=True)
"""Out[1]
[PROMPT]<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
浙江的省会在哪里？<|im_end|>
<|im_start|>assistant
浙江省的省会是杭州。<|im_end|>
<|im_start|>user
这有什么好吃的？<|im_end|>
<|im_start|>assistant
杭州市有很多著名的美食，例如西湖醋鱼、龙井虾仁、糖醋排骨、毛血旺等。此外，还有杭州特色的点心，如桂花糕、荷花酥、艾窝窝等。<|im_end|>
<|im_start|>user
第一个问题是什么<|im_end|>
<|im_start|>assistant
[OUTPUT]你的第一个问题是“浙江的省会在哪里？”<|im_end|>
"""
```
更多推理使用请参考[这里](https://github.com/modelscope/swift/blob/main/docs/source/LLM/LLM%E6%8E%A8%E7%90%86%E6%96%87%E6%A1%A3.md)
```

## File: `recipes/inference/dashscope/README.md`
```markdown
# Inference Qwen Using DashScope

The most simple way to use Qwen through APIs is DashScope API service through Alibaba Cloud. We give an introduction to the usage. Additionally, we provide a script for you to deploy an OpenAI-style API on your own servers.

DashScope is the large language model API service provided by Alibaba Cloud, which now supports Qwen. Note that the models behind DashScope are in-house versions temporarily without details provided. The services include `qwen-turbo` and `qwen-plus`, where the former one runs faster and the latter achieves better performance. For more information, visit the documentation [here](https://dashscope.aliyun.com).

Please head to the official website [link](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key?spm=a2c4g.11186623.0.0.6c2774fahtfXdn) to create a DashScope account and obtain the API key (AK). We recommend setting the AK with an environment variable:
```bash
export DASHSCOPE_API_KEY="YOUR_DASHSCOPE_API_KEY"
```
Then please install the packages and click [here](https://help.aliyun.com/zh/dashscope/developer-reference/install-dashscope-sdk) for the documentation. If you use Python, you can install DashScope with pip:
```bash
pip install dashscope
```
If you use JAVA SDK, you can install it in this way:
```xml
<!-- https://mvnrepository.com/artifact/com.alibaba/dashscope-sdk-java -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dashscope-sdk-java</artifactId>
    <version>the-latest-version</version>
</dependency>
```
The simplest way to use DashScope is the usage with messages, which is similar to OpenAI API. The example is demonstrated below:
```python
import random
from http import HTTPStatus
from dashscope import Generation


def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '如何做西红柿鸡蛋？'}]
    gen = Generation()
    response = gen.call(
        Generation.Models.qwen_turbo,
        messages=messages,
        seed=random.randint(1, 10000),  # set the random seed, optional, default to 1234 if not set
        result_format='message',  # set the result to be "message" format.
    )
    return response


if __name__ == '__main__':
    response = call_with_messages()
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
```
For more usages, please visit the official website for more details.
<br><br>

```

## File: `recipes/inference/hf_modelscope/README.md`
```markdown
# Inference Qwen Using 🤖 ModelScope and 🤗 Transformers

Below, we provide simple examples to show how to inference Qwen with 🤖 ModelScope and 🤗 Transformers.

## Requirements

* python 3.8 and above
* pytorch 1.12 and above, 2.0 and above are recommended
* transformers 4.32 and above
* CUDA 11.4 and above are recommended (this is for GPU users, flash-attention users, etc.)
<br>

## Installation

You can use our pre-built docker images to skip most of the environment setup steps, see Section ["Using Pre-built Docker Images"](https://github.com/QwenLM/Qwen?tab=readme-ov-file#-docker) for more details. 

If not using docker, please make sure you have setup the environment and installed the required packages. Make sure you meet the above requirements, and then install the dependent libraries.

```bash
pip install -r Qwen/requirements.txt
```

If your device supports fp16 or bf16, we recommend installing [flash-attention](https://github.com/Dao-AILab/flash-attention) (**we support flash attention 2 now.**) for higher efficiency and lower memory usage. (**flash-attention is optional and the project can run normally without installing it**)

```bash
git clone https://github.com/Dao-AILab/flash-attention
cd flash-attention && pip install .
# Below are optional. Installing them might be slow.
# pip install csrc/layer_norm
# If the version of flash-attn is higher than 2.1.1, the following is not needed.
# pip install csrc/rotary
```

Now you can start with ModelScope or Transformers.

## 🤗 Transformers

To use Qwen-Chat for the inference, all you need to do is to input a few lines of codes as demonstrated below. Remember to pass in the correct model names or paths, such as "Qwen/Qwen-7B-Chat" and "Qwen/Qwen-14B-Chat". However, **please make sure that you are using the latest code.**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names: "Qwen/Qwen-7B-Chat", "Qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# use bf16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
# use auto mode, automatically select precision based on the device.
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
    device_map="auto",
    trust_remote_code=True
).eval()

# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True)

# 1st dialogue turn
response, history = model.chat(tokenizer, "你好", history=None)
print(response)
# 你好！很高兴为你提供帮助。

# 2nd dialogue turn
response, history = model.chat(tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
# 这是一个关于一个年轻人奋斗创业最终取得成功的故事。
# 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。
# 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。
# 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。
# 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。
# 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。

# 3rd dialogue turn
response, history = model.chat(tokenizer, "给这个故事起一个标题", history=history)
print(response)
# 《奋斗创业：一个年轻人的成功之路》
```

Running Qwen, the base language model, is also simple.

<details>
  <summary>Running Qwen</summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Model names: "Qwen/Qwen-7B", "Qwen/Qwen-14B" 
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)
# use bf16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B", device_map="cpu", trust_remote_code=True).eval()
# use auto mode, automatically select precision based on the device.
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B",
    device_map="auto",
    trust_remote_code=True
).eval()

# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.
# model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B", trust_remote_code=True)

inputs = tokenizer('蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是', return_tensors='pt')
inputs = inputs.to(model.device)
pred = model.generate(**inputs)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))
# 蒙古国的首都是乌兰巴托（Ulaanbaatar）\n冰岛的首都是雷克雅未克（Reykjavik）\n埃塞俄比亚的首都是亚的斯亚贝巴（Addis Ababa）...
```

</details>

<p id="DownloadModel">
In the event of a network issue while attempting to download model checkpoints and codes from HuggingFace, an alternative approach is to initially fetch the checkpoint from ModelScope and then load it from the local directory as outlined below:
</p>

```python
from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Downloading model checkpoint to a local dir model_dir
# model_dir = snapshot_download('qwen/Qwen-7B')
# model_dir = snapshot_download('qwen/Qwen-7B-Chat')
# model_dir = snapshot_download('qwen/Qwen-14B')
model_dir = snapshot_download('qwen/Qwen-14B-Chat')

# Loading local checkpoints
# trust_remote_code is still set as True since we still load codes from local dir instead of transformers
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True
).eval()
```

## 🤖 ModelScope

ModelScope is an open-source platform for Model-as-a-Service (MaaS), which provides flexible and cost-effective model service to AI developers. Similarly, you can run the models with ModelScope as shown below:

```python
from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

# Model names: "qwen/Qwen-7B-Chat", "qwen/Qwen-14B-Chat"
tokenizer = AutoTokenizer.from_pretrained("qwen/Qwen-7B-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-7B-Chat", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

response, history = model.chat(tokenizer, "你好", history=None)
print(response)
response, history = model.chat(tokenizer, "浙江的省会在哪里？", history=history) 
print(response)
response, history = model.chat(tokenizer, "它有什么好玩的景点", history=history)
print(response)
```

## Batch Inference
Qwen supports batch inference. With flash attention enabled, using batch inference can bring a 40% speedup. The example code is shown below:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GenerationConfig
from qwen_generation_utils import make_context, decode_tokens, get_stop_words_ids

tokenizer = AutoTokenizer.from_pretrained(
    './',
    pad_token='<|extra_0|>',
    eos_token='<|endoftext|>',
    padding_side='left',
    trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    './',
    pad_token_id=tokenizer.pad_token_id,
    device_map="auto",
    trust_remote_code=True
).eval()
model.generation_config = GenerationConfig.from_pretrained('./', pad_token_id=tokenizer.pad_token_id)

all_raw_text = ["我想听你说爱我。", "今天我想吃点啥，甜甜的，推荐下", "我马上迟到了，怎么做才能不迟到"]
batch_raw_text = []
for q in all_raw_text:
    raw_text, _ = make_context(
        tokenizer,
        q,
        system="You are a helpful assistant.",
        max_window_size=model.generation_config.max_window_size,
        chat_format=model.generation_config.chat_format,
    )
    batch_raw_text.append(raw_text)

batch_input_ids = tokenizer(batch_raw_text, padding='longest')
batch_input_ids = torch.LongTensor(batch_input_ids['input_ids']).to(model.device)
batch_out_ids = model.generate(
    batch_input_ids,
    return_dict_in_generate=False,
    generation_config=model.generation_config
)
padding_lens = [batch_input_ids[i].eq(tokenizer.pad_token_id).sum().item() for i in range(batch_input_ids.size(0))]

batch_response = [
    decode_tokens(
        batch_out_ids[i][padding_lens[i]:],
        tokenizer,
        raw_text_len=len(batch_raw_text[i]),
        context_length=(batch_input_ids[i].size(0)-padding_lens[i]),
        chat_format="chatml",
        verbose=False,
        errors='replace'
    ) for i in range(len(all_raw_text))
]
print(batch_response)

response, _ = model.chat(tokenizer, "我想听你说爱我。", history=None)
print(response)

response, _ = model.chat(tokenizer, "今天我想吃点啥，甜甜的，推荐下", history=None)
print(response)

response, _ = model.chat(tokenizer, "我马上迟到了，怎么做才能不迟到", history=None)
print(response)
```

## CPU

To deploy our models on CPU, we strongly advise you to use [qwen.cpp](https://github.com/QwenLM/qwen.cpp), which is a pure C++ implementation of Qwen and tiktoken. Check the repo for more details!

Also, it is also simple to directly run the model on CPU, which requires your specification of device:

```python
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-7B-Chat", device_map="cpu", trust_remote_code=True).eval()
```

However, it is likely that you suffer from extremely low inference efficiency.

## Multiple GPUs

If you suffer from lack of GPU memory and you would like to run the model on more than 1 GPU, you can directly use the default loading method, which is now supported by Transformers. The previous method based on `utils.py` is deprecated.

However, though this method is simple, the efficiency of the native pipeline parallelism is low. We advise you to use vLLM with FastChat and please read [the section](../vllm/README.md) for deployment.
```

## File: `recipes/inference/quantization/README.md`
```markdown
# Quantization

## GPTQ

We provide a solution based on [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ), and release the Int4 and Int8 quantized models, which achieve nearly lossless model effects but improved performance on both memory costs and inference speed.

Here we demonstrate how to use our provided quantized models for inference. Before you start, make sure you meet the requirements of auto-gptq (e.g., torch 2.0 and above, transformers 4.32.0 and above, etc.) and install the required packages:

```bash
pip install auto-gptq optimum
```

If you meet problems installing `auto-gptq`, we advise you to check out the official [repo](https://github.com/PanQiWei/AutoGPTQ) to find a wheel.

> Note: The pre-compiled `auto-gptq` packages strongly depend on the version of `torch` and its CUDA version. Moreover, due to recent update, 
> you may also encounter unsupported version errors from `transformers`, `optimum`, or `peft`.
> We recommend using the latest versions meeting the following requirements:
> - torch==2.1 auto-gptq>=0.5.1 transformers>=4.35.0 optimum>=1.14.0 peft>=0.6.1
> - torch>=2.0,<2.1 auto-gptq<0.5.0 transformers<4.35.0 optimum<1.14.0 peft>=0.5.0,<0.6.0

Then you can load the quantized model easily and run inference as same as usual:

```python
# Model names: "Qwen/Qwen-7B-Chat-Int4", "Qwen/Qwen-14B-Chat-Int4"
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat-Int4",
    device_map="auto",
    trust_remote_code=True
).eval()
response, history = model.chat(tokenizer, "Hi", history=None)
```

We illustrate the model performance of both BF16, Int8 and Int4 models on the benchmark, and we find that the quantized model does not suffer from significant performance degradation. Results are shown below:

| Quantization         | MMLU | CEval (val) | GSM8K | Humaneval |
|----------------------|:----:|:-----------:|:-----:|:---------:|
| Qwen-1.8B-Chat (BF16)| 43.3 |    55.6     | 33.7  |   26.2    |
| Qwen-1.8B-Chat (Int8)| 43.1 |    55.8     | 33.0  |   27.4    |
| Qwen-1.8B-Chat (Int4)| 42.9 |    52.8     | 31.2  |   25.0    |
| Qwen-7B-Chat (BF16)  | 55.8 |    59.7     | 50.3  |   37.2    |
| Qwen-7B-Chat (Int8)  | 55.4 |    59.4     | 48.3  |   34.8    |
| Qwen-7B-Chat (Int4)  | 55.1 |    59.2     | 49.7  |   29.9    |
| Qwen-14B-Chat (BF16) | 64.6 |    69.8     | 60.1  |   43.9    |
| Qwen-14B-Chat (Int8) | 63.6 |    68.6     | 60.0  |   48.2    |
| Qwen-14B-Chat (Int4) | 63.3 |    69.0     | 59.8  |   45.7    |
| Qwen-72B-Chat (BF16) | 74.4 |    80.1     | 76.4  |   64.6    |
| Qwen-72B-Chat (Int8) | 73.5 |    80.1     | 73.5  |   62.2    |
| Qwen-72B-Chat (Int4) | 73.4 |    80.1     | 75.3  |   61.6    |

## Quantization of KV cache

> NOTE: Please be aware that due to the internal mechanism of Hugging Face, the support files for this functionality 
> (i.e., `cache_autogptq_cuda_256.cpp` and `cache_autogptq_cuda_kernel_256.cu`) may be missing. Please manually download
> them from the Hugging Face Hub and place them into the same folder as the other module files.

The attention KV cache can be quantized and compressed for storage, to get a higher sample throughput. The arguments `use_cache_quantization` and `use_cache_kernel` in `config.json` are provided to enable KV cache quantization. The specific use method is as follows:
```python
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B-Chat",
     device_map="auto",
     trust_remote_code=True,
     use_cache_quantization=True,
     use_cache_kernel=True,
     use_flash_attn=False
)
```
Attention: Currently, KV cache quantization and flash attention cannot be used at the same time.
If you enable KV cache quantization and flash attention at the same time (`use_flash_attn=True`, `use_cache_quantization=True`, `use_cache_kernel=True`), `use_flash_attn` is disabled by default (`use_flash_attn=false`).

We have verified that the use of the quantized Int8-KV-Cache model does not suffer from significant performance degradation in downstream evaluation. In the following, we focus on profiling its memory footprint in different conditions. 
The profiling runs on a single A100-SXM4-80G GPU with PyTorch 2.0.1 and CUDA 11.4. 
We use BF16 models to generate 1024 tokens by default, and "OOM" indicates out-of-memory error.

With KV cache quantization, the model can infer with a larger batch size (bs).

| USE KV Cache |  bs=1  |  bs=4  | bs=16  | bs=32  | bs=64  | bs=100 |
|--------------|:------:|:------:|:------:|:------:|:------:|:------:|
| No           | 16.3GB | 24.1GB | 31.7GB | 48.7GB |  OOM   |  OOM   |
| Yes          | 15.5GB | 17.2GB | 22.3GB | 30.2GB | 48.2GB | 72.4GB |

With KV cache quantization the model can save more memory when generating longer sequence (`sl`, sequence length, referring to the number of tokens generated) at the stage of inference.

| USE KV Cache | sl=512 | sl=1024 | sl=2048 | sl=4096 | sl=8192 |
|--------------|:------:|:-------:|:-------:|:-------:|:-------:|
| No           | 15.2GB | 16.3GB  | 17.6GB  | 19.5GB  | 23.2GB  |
| Yes          |  15GB  | 15.5GB  | 15.8GB  | 16.6GB  | 17.6GB  |

The model with KV cache quantization will convert the format of `layer_past` from float to int8, and meanwhile the quantized `layer-past` will also store the quantization parameters.

Specific steps are as follows:

1. Quantize key/value
```
    qv,scale,zero_point=quantize_cache_v(v)
```
2. Store into layer_past

The following is the format of quantized `layer_past`:
```
    layer_past=((q_key,key_scale,key_zero_point),
                (q_value,value_scale,value_zero_point))
```

The original format of `layer_past` is shown below:
```
    layer_past=(key,value)
```

If you want to use the attention KV which is quantized, you can use the dequantization operation to convert the Int8 key/value back to the float format as follows:
```
    v=dequantize_cache_torch(qv,scale,zero_point)
```
<br>
```

## File: `recipes/inference/tensorrt/README.md`
```markdown
# Inference Qwen Using TensorRT-LLM
Below, we provide a simple example to show how to inference Qwen by TensorRT-LLM. We recommend using GPUs with compute capability of at least SM_80 such as A10 and A800 to run this example, as we have tested on these GPUs. You can find your gpu compute capability on this [link](https://developer.nvidia.com/cuda-gpus).

## Installation
You can use pre-built docker image to run this example. Simultaneously, You can also refer to the official [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) for installation and detailed usage.
```bash
docker run --gpus all -it --ipc=host --network=host pai-image-manage-registry.cn-wulanchabu.cr.aliyuncs.com/pai/llm-inference:tensorrt-llm-0.8.0 bash
```
## Quickstart
1. Download model by modelscope

```bash
cd TensorRT-LLM/examples/qwen
python3 -c "from modelscope.hub.snapshot_download import snapshot_download; snapshot_download('Qwen/Qwen-1_8B-Chat', cache_dir='.', revision='master')"
mkdir -p ./tmp/Qwen
mv Qwen/Qwen-1_8B-Chat ./tmp/Qwen/1_8B
```

2. Build TensorRT engine from HF checkpoint

```bash
python3 build.py --hf_model_dir ./tmp/Qwen/1_8B/ \
                --dtype float16 \
                --remove_input_padding \
                --use_gpt_attention_plugin float16 \
                --enable_context_fmha \
                --use_gemm_plugin float16 \
                --output_dir ./tmp/Qwen/1_8B/trt_engines/fp16/1-gpu/
```

3. Inference
```bash
python3 ../run.py --input_text "你好，请问你叫什么？" \
                  --max_output_len=512 \
                  --tokenizer_dir ./tmp/Qwen/1_8B/ \
                  --engine_dir=./tmp/Qwen/1_8B/trt_engines/fp16/1-gpu
```
```
Input [Text 0]: "<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
你好，请问你叫什么？<|im_end|>
<|im_start|>assistant
"
Output [Text 0 Beam 0]: "你好，我是来自阿里云的大规模语言模型，我叫通义千问。"
```
```

## File: `recipes/inference/tensorrt/docker/Dockerfile`
```
FROM nvidia/cuda:12.1.0-devel-ubuntu22.04

RUN apt-get update && \
    apt-get -y install python3.10 python3-pip openmpi-bin libopenmpi-dev git && \
    rm -rf /var/lib/apt/lists/*

RUN pip install tensorrt_llm==0.8.0.dev2024011601 -U --no-cache-dir --pre --extra-index-url https://pypi.nvidia.com

RUN pip install --no-cache-dir modelscope==1.11.1

RUN git clone https://github.com/NVIDIA/TensorRT-LLM.git && \
    cd TensorRT-LLM && \ 
    git checkout c89653021e66ca78c55f02b366f404455bc12e8d && \
    pip install --no-cache-dir -r examples/qwen/requirements.txt
```

## File: `recipes/inference/vllm/README.md`
```markdown
# Inference Qwen Using vLLM

For deployment and fast inference, we suggest using vLLM. 

## Installation

If you use cuda 12.1 and pytorch 2.1, you can directly use the following command to install vLLM.
```bash
# Install vLLM with CUDA 12.1.
pip install vllm
```
Otherwise, please refer to the official vLLM [Installation Instructions](https://docs.vllm.ai/en/latest/getting_started/installation.html).

If you have trouble building vLLM, we recommend using Docker image.

```bash
docker run --gpus all -it --rm --ipc=host --network=host qwenllm/qwen:cu121 bash
```

## GPU Requirements

Qwen model use Bfloat16 by default, but Bfloat16 is only supported on GPUs with compute capability of at least 8. For GPUs with compute capability less than 8.0, it is recommended to set the dtype to float16. You can find your gpu compute capability on this [link](https://developer.nvidia.com/cuda-gpus).

We have tested the GPU memory usage on NVIDIA Tesla V100 32GB by manually adjusting gpu-memory-utilization in eager mode, you can refer to the following table to determine whether your machine is capable of running these models.
| Model | seq_len 2048 | seq_len 8192 | seq_len 16384 | seq_len 32768 |
| :--- | ---: | ---: | ---: | ---: |
| Qwen-1.8B | 6.22G | 7.46G |  |  |
| Qwen-7B | 17.94G | 20.96G |  |  |
| Qwen-7B-Int4 | 9.10G | 12.26G |  |  |
| Qwen-14B | 33.40G |  |  |  |
| Qwen-14B-Int4 | 13.30G |  |  |  |
| Qwen-72B | 166.87G | 185.50G | 210.80G | 253.80G |
| Qwen-72B-int4 | 55.37G | 73.66G | 97.79G | 158.80G |

We have also listed the models that can run on consumer graphics cards by default sequence length in the following table. If the GPU memory only exceeds the model's memory usage by a small margin, you can make the model run on your machine by reducing the max-model-len parameter.</br>
(ps: To run Qwen-14B-Int4 on NVIDIA RTX 3080Ti, you need to set gpu-memory-utilization as 0.99 and enforce eager mode)

| GPU Memory | GPU | Support Model |
| :---: | :---: | :---: |
| 24GB | NVIDIA RTX 4090/3090/A5000 | Qwen-1.8B/Qwen-7B/Qwen-7B-Int4/Qwen-14B-Int4  |
| 16GB | NVIDIA RTX A4000 | Qwen-1.8B/Qwen-7B-Int4/Qwen-14B-Int4 |
| 12GB | NVIDIA RTX 3080Ti/TITAN Xp | Qwen-1.8B/Qwen-14B-Int4 |
| 11GB | NVIDIA RTX 2080Ti/GTX 1080Ti | Qwen-1.8B |
| 10GB | NVIDIA RTX 3080 | Qwen-1.8B |

## Usage

### vLLM + Web Demo / OpenAI-like API

You can use FastChat to launch a web demo or an OpenAI API server. First, install FastChat:

```bash
pip install "fschat[model_worker,webui]=0.2.33" "openai<1.0"
```

To run Qwen with vLLM and FastChat, you need launch a controller by:
```bash
python -m fastchat.serve.controller
```

Then you can launch the model worker, which means loading your model for inference. For single GPU inference, you can directly run:
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --dtype bfloat16
# run int4 model or GPUs with compute capability less than 8.0
# python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --dtype float16 
```

However, if you hope to run the model on multiple GPUs for faster inference or larger memory, you can use tensor parallelism supported by vLLM. Suppose you run the model on 4 GPUs, the command is shown below:
```bash
python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4 --dtype bfloat16
# run int4 model or GPUs with compute capability less than 8.0
# python -m fastchat.serve.vllm_worker --model-path $model_path --trust-remote-code --tensor-parallel-size 4 --dtype float16 
```

After launching your model worker, you can launch a:

* Web UI Demo
```bash
python -m fastchat.serve.gradio_web_server
```

* OpenAI API
```bash
python -m fastchat.serve.openai_api_server --host localhost --port 8000
```

For OpenAI API server, you can invoke the server in the following manner.

```python
import openai
openai.api_base = "http://localhost:8000/v1"
openai.api_key = "none"

# create a request activating streaming response
for chunk in openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=True 
    # Specifying stop words in streaming output format is not yet supported and is under development.
):
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

# create a request not activating streaming response
response = openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=False,
    stop=[] # You can add custom stop words here, e.g., stop=["Observation:"] for ReAct prompting.
)
print(response.choices[0].message.content)
```

If you find `"POST /v1/chat/completions HTTP/1.1" 200 OK` in openai_api_server log, it indicates that the call was successful. 

vLLM does not support dynamic-NTK ROPE. Therefore, extending long sequences for Qwen model may lead to quality degradation(even gibberish).

### vLLM + Transformer-like Wrapper

You can download the [wrapper codes](vllm_wrapper.py) and execute the following commands for multiple rounds of dialogue interaction. (Note: It currently only supports the ``model.chat()`` method.)

```python
from vllm_wrapper import vLLMWrapper

# Bfloat16 is only supported on GPUs with compute capability of at least 8.0, 
model = vLLMWrapper('Qwen/Qwen-7B-Chat', tensor_parallel_size=1)

# run int4 model or GPUs with compute capability less than 8.0
# model = vLLMWrapper('Qwen/Qwen-7B-Chat-Int4', tensor_parallel_size=1, dtype="float16")

response, history = model.chat(query="你好", history=None)
print(response)
response, history = model.chat(query="给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
response, history = model.chat(query="给这个故事起一个标题", history=history)
print(response)
```
### vLLM Standalone OpenAI-like API

You can also deploy an OpenAI API server independently through vLLM. First, you need to download [chat template file](template_chatml.jinja).

Then, you can launch an OpenAI API server by following command:

```bash
python -m vllm.entrypoints.openai.api_server --model $model_path --trust-remote-code --chat-template template_chatml.jinja

# run int4 model or GPUs with compute capability less than 8.0
# python -m vllm.entrypoints.openai.api_server --model $model_path --trust-remote-code --dtype float16 --chat-template template_chatml.jinja
```

For vLLM standalone OpenAI API server, You need to set the `stop_token_ids` parameter to `[151645]` or `stop` parameter to `["<|im_end|>"]` when invoking the server.

```python
import openai
openai.api_base = "http://localhost:8000/v1"
openai.api_key = "none"

# create a request activating streaming response
for chunk in openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=True, 
    stop_token_ids=[151645]
):
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

# create a request not activating streaming response
response = openai.ChatCompletion.create(
    model="Qwen",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=False,
    stop_token_ids=[151645]
)
print(response.choices[0].message.content)
```
```

## File: `recipes/inference/vllm/template_chatml.jinja`
```
{% for message in messages %}
{% if loop.first and message['role'] != 'system' %}{{ '<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n' }}{% endif %}
{{ '<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>\n' }}
{% if loop.last and add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}
{% endfor %}
```

## File: `recipes/inference/vllm/vllm_wrapper.py`
```python
from transformers import PreTrainedTokenizer, GenerationConfig, StoppingCriteriaList
from typing import Optional, Callable, List, Tuple, Union
import copy
import torch
from transformers import AutoTokenizer
from transformers.generation.logits_process import LogitsProcessorList
from packaging import version

_ERROR_BAD_CHAT_FORMAT = """\
We detect you are probably using the pretrained model (rather than chat model) for chatting, since the chat_format in generation_config is not "chatml".
If you are directly using the model downloaded from Huggingface, please make sure you are using our "Qwen/Qwen-7B-Chat" Huggingface model (rather than "Qwen/Qwen-7B") when you call model.chat().
我们检测到您可能在使用预训练模型（而非chat模型）进行多轮chat，因为您当前在generation_config指定的chat_format，并未设置为我们在对话中所支持的"chatml"格式。
如果您在直接使用我们从Huggingface提供的模型，请确保您在调用model.chat()时，使用的是"Qwen/Qwen-7B-Chat"模型（而非"Qwen/Qwen-7B"预训练模型）。
"""

IMEND = "<|im_end|>"
ENDOFTEXT = "<|endoftext|>"

HistoryType = List[Tuple[str, str]]
TokensType = List[int]
BatchTokensType = List[List[int]]

def get_stop_words_ids(chat_format, tokenizer):
    if chat_format == "raw":
        stop_words_ids = [tokenizer.encode("Human:"), [tokenizer.eod_id]]
    elif chat_format == "chatml":
        stop_words_ids = [[tokenizer.im_end_id], [tokenizer.im_start_id]]
    else:
        raise NotImplementedError(f"Unknown chat format {chat_format!r}")
    return stop_words_ids

def make_context(
    tokenizer: PreTrainedTokenizer,
    query: str,
    history: List[Tuple[str, str]] = None,
    system: str = "",
    max_window_size: int = 6144,
    chat_format: str = "chatml",
):
    if history is None:
        history = []

    if chat_format == "chatml":
        im_start_tokens = [tokenizer.im_start_id]
        im_end_tokens = [tokenizer.im_end_id]
        im_start, im_end = tokenizer.decode(im_start_tokens, skip_special_tokens=False), tokenizer.decode(im_end_tokens, skip_special_tokens=False)
        nl_tokens = tokenizer.encode("\n")

        def _tokenize_str(role, content):
            return f"{role}\n{content}", tokenizer.encode(
                role, allowed_special=set()
            ) + nl_tokens + tokenizer.encode(content, allowed_special=set())

        system_text, system_tokens_part = _tokenize_str("system", system)
        system_tokens = im_start_tokens + system_tokens_part + im_end_tokens

        raw_text = ""
        context_tokens = []

        for turn_query, turn_response in reversed(history):
            query_text, query_tokens_part = _tokenize_str("user", turn_query)
            query_tokens = im_start_tokens + query_tokens_part + im_end_tokens
            response_text, response_tokens_part = _tokenize_str(
                "assistant", turn_response
            )
            response_tokens = im_start_tokens + response_tokens_part + im_end_tokens

            next_context_tokens = nl_tokens + query_tokens + nl_tokens + response_tokens
            prev_chat = (
                f"\n{im_start}{query_text}{im_end}\n{im_start}{response_text}{im_end}"
            )

            current_context_size = (
                len(system_tokens) + len(next_context_tokens) + len(context_tokens)
            )
            if current_context_size < max_window_size:
                context_tokens = next_context_tokens + context_tokens
                raw_text = prev_chat + raw_text
            else:
                break

        context_tokens = system_tokens + context_tokens
        raw_text = f"{im_start}{system_text}{im_end}" + raw_text
        context_tokens += (
            nl_tokens
            + im_start_tokens
            + _tokenize_str("user", query)[1]
            + im_end_tokens
            + nl_tokens
            + im_start_tokens
            + tokenizer.encode("assistant")
            + nl_tokens
        )
        raw_text += f"\n{im_start}user\n{query}{im_end}\n{im_start}assistant\n"

    elif chat_format == "raw":
        raw_text = query
        context_tokens = tokenizer.encode(raw_text)
    else:
        raise NotImplementedError(f"Unknown chat format {chat_format!r}")

    return raw_text, context_tokens

class vLLMWrapper:
    def __init__(self,
               model_dir: str,
               trust_remote_code: bool = True,
               tensor_parallel_size: int = 1,
               gpu_memory_utilization: float = 0.98,
               dtype: str = "bfloat16",
               **kwargs):

        if dtype not in ("bfloat16", "float16", "float32"):
            print("now not support {}!".format(dtype))
            raise Exception

        # build generation_config
        self.generation_config = GenerationConfig.from_pretrained(model_dir, trust_remote_code=trust_remote_code)

        # build tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
        self.tokenizer.eos_token_id = self.generation_config.eos_token_id

        self.stop_words_ids = []

        from vllm import LLM
        import vllm
        if version.parse(vllm.__version__) >= version.parse("0.2.2"):
            self.__vllm_support_repetition_penalty = True
        else:
            self.__vllm_support_repetition_penalty = False

        quantization = getattr(kwargs, 'quantization', None)

        self.model = LLM(model=model_dir,
                            tokenizer=model_dir,
                            tensor_parallel_size=tensor_parallel_size,
                            trust_remote_code=trust_remote_code,
                            quantization=quantization,
                            gpu_memory_utilization=gpu_memory_utilization,
                            dtype=dtype)

        for stop_id in get_stop_words_ids(self.generation_config.chat_format, self.tokenizer):
            self.stop_words_ids.extend(stop_id)
        self.stop_words_ids.extend([self.generation_config.eos_token_id])

    def chat(self,
        query: str,
        history: Optional[HistoryType],
        tokenizer: PreTrainedTokenizer = None,
        system: str = "You are a helpful assistant.",
        generation_config: Optional[GenerationConfig] = None,
        **kwargs):
        generation_config = generation_config if generation_config is not None else self.generation_config
        tokenizer = self.tokenizer if tokenizer is None else tokenizer

        assert generation_config.chat_format == 'chatml', _ERROR_BAD_CHAT_FORMAT
        if not self.__vllm_support_repetition_penalty and generation_config.repetition_penalty != 1:
            raise RuntimeError("The installed vLLM doesn't support repetition_penalty, please set ``model.generation_config.repetition_penalty = 1`` or install vllm>=0.2.2")

        if history is None:
            history = []
        else:
            # make a copy of the user's input such that is is left untouched
            history = copy.deepcopy(history)

        extra_stop_words_ids = kwargs.get('stop_words_ids', None)
        if extra_stop_words_ids is None:
            extra_stop_words_ids = []

        max_window_size = kwargs.get('max_window_size', None)
        if max_window_size is None:
            max_window_size = generation_config.max_window_size

        from vllm.sampling_params import SamplingParams
        sampling_kwargs = {
            "stop_token_ids": self.stop_words_ids,
            "early_stopping": False,
            "top_p": generation_config.top_p,
            "top_k": -1 if generation_config.top_k == 0 else generation_config.top_k,
            "temperature": generation_config.temperature,
            "max_tokens": generation_config.max_new_tokens,
            "repetition_penalty": generation_config.repetition_penalty
        }
        if not self.__vllm_support_repetition_penalty:
            sampling_kwargs.pop("repetition_penalty")
        sampling_params = SamplingParams(**sampling_kwargs)

        raw_text, context_tokens = make_context(
            self.tokenizer,
            query,
            history=history,
            system=system,
            max_window_size=max_window_size,
            chat_format=generation_config.chat_format,
        )

        req_outputs = self.model.generate([query],
                                            sampling_params=sampling_params,
                                            prompt_token_ids=[context_tokens])
        req_output = req_outputs[0]

        prompt_str = req_output.prompt
        prompt_ids = req_output.prompt_token_ids
        req_sample_output_ids = []
        req_sample_output_strs = []
        for sample in req_output.outputs:
            output_str = sample.text
            output_ids = sample.token_ids
            if IMEND in output_str:
                output_str = output_str[:-len(IMEND)]
            if ENDOFTEXT in output_str:
                output_str = output_str[:-len(ENDOFTEXT)]
            req_sample_output_ids.append(prompt_ids + output_ids)
            req_sample_output_strs.append(prompt_str + output_str)
        assert len(req_sample_output_strs) == 1
        response = req_sample_output_strs[0][len(prompt_str):]
        history.append((prompt_str, response))

        return response, history

if __name__ == '__main__':

    model_dir = 'Qwen/Qwen-72B-Chat'
    tensor_parallel_size = 2

    model = vLLMWrapper(model_dir,
                        tensor_parallel_size=tensor_parallel_size,
                        )

    response, history = model.chat(query="你好",
                                   history=None)
    print(response)
    response, history = model.chat(query="给我讲一个年轻人奋斗创业最终取得成功的故事。",
                                   history=history)
    print(response)
    response, history = model.chat(query="给这个故事起一个标题",
                                   history=history)
    print(response)
```

## File: `recipes/quickstart/qwen.ipynb`
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Qwen Quick Start Notebook\n",
    "\n",
    "This notebook shows how to train and infer the Qwen-7B-Chat model on a single GPU. Similarly, Qwen-1.8B-Chat, Qwen-14B-Chat can also be leveraged for the following steps. We only need to modify the corresponding `model name` and hyper-parameters. The training and inference of Qwen-72B-Chat requires higher GPU requirements and larger disk space."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Requirements\n",
    "- Python 3.8 and above\n",
    "- Pytorch 1.12 and above, 2.0 and above are recommended\n",
    "- CUDA 11.4 and above are recommended (this is for GPU users, flash-attention users, etc.)\n",
    "We test the training of the model on an A10 GPU (24GB)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Extra\n",
    "If you need to speed up, you can install  `flash-attention`. The details of the installation can be found [here](https://github.com/Dao-AILab/flash-attention)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!git clone https://github.com/Dao-AILab/flash-attention\n",
    "!cd flash-attention && pip install .\n",
    "# Below are optional. Installing them might be slow.\n",
    "# !pip install csrc/layer_norm\n",
    "# If the version of flash-attn is higher than 2.1.1, the following is not needed.\n",
    "# !pip install csrc/rotary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 0: Install Package Requirements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!pip install transformers>=4.32.0 accelerate tiktoken einops scipy transformers_stream_generator==0.0.4 peft deepspeed modelscope"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 1: Download Model\n",
    "When using `transformers` in some regions, the model cannot be automatically downloaded due to network problems. We recommend using `modelscope` to download the model first, and then use `transformers` for inference."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope import snapshot_download\n",
    "\n",
    "# Downloading model checkpoint to a local dir model_dir.\n",
    "model_dir = snapshot_download('Qwen/Qwen-7B-Chat', cache_dir='.', revision='master')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 2: Direct Model Inference \n",
    "We recommend two ways to do model inference: `modelscope` and `transformers`.\n",
    "\n",
    "#### 2.1 Model Inference with ModelScope"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from modelscope import AutoModelForCausalLM, AutoTokenizer\n",
    "from modelscope import GenerationConfig\n",
    "\n",
    "# Note: The default behavior now has injection attack prevention off.\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"Qwen/Qwen-7B-Chat/\", trust_remote_code=True)\n",
    "\n",
    "# use bf16\n",
    "# model = AutoModelForCausalLM.from_pretrained(\"qwen/Qwen-7B-Chat/\", device_map=\"auto\", trust_remote_code=True, bf16=True).eval()\n",
    "# use fp16\n",
    "# model = AutoModelForCausalLM.from_pretrained(\"qwen/Qwen-7B-Chat/\", device_map=\"auto\", trust_remote_code=True, fp16=True).eval()\n",
    "# use cpu only\n",
    "# model = AutoModelForCausalLM.from_pretrained(\"qwen/Qwen-7B-Chat/\", device_map=\"cpu\", trust_remote_code=True).eval()\n",
    "# use auto mode, automatically select precision based on the device.\n",
    "model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-7B-Chat/\", device_map=\"auto\", trust_remote_code=True).eval()\n",
    "\n",
    "# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.\n",
    "# model.generation_config = GenerationConfig.from_pretrained(\"Qwen/Qwen-7B-Chat/\", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参\n",
    "\n",
    "# 第一轮对话 1st dialogue turn\n",
    "response, history = model.chat(tokenizer, \"你好\", history=None)\n",
    "print(response)\n",
    "# 你好！很高兴为你提供帮助。\n",
    "\n",
    "# 第二轮对话 2nd dialogue turn\n",
    "response, history = model.chat(tokenizer, \"给我讲一个年轻人奋斗创业最终取得成功的故事。\", history=history)\n",
    "print(response)\n",
    "# 这是一个关于一个年轻人奋斗创业最终取得成功的故事。\n",
    "# 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。\n",
    "# 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。\n",
    "# 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。\n",
    "# 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。\n",
    "# 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。\n",
    "\n",
    "# 第三轮对话 3rd dialogue turn\n",
    "response, history = model.chat(tokenizer, \"给这个故事起一个标题\", history=history)\n",
    "print(response)\n",
    "# 《奋斗创业：一个年轻人的成功之路》"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2.2 Model Inference with transformers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "ExecutionIndicator": {
     "show": true
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"Qwen/Qwen-7B-Chat/\", trust_remote_code=True)\n",
    "\n",
    "# use bf16\n",
    "# model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-7B-Chat/\", device_map=\"auto\", trust_remote_code=True, bf16=True).eval()\n",
    "# use fp16\n",
    "# model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-7B-Chat/\", device_map=\"auto\", trust_remote_code=True, fp16=True).eval()\n",
    "# use cpu only\n",
    "# model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-7B-Chat/\", device_map=\"cpu\", trust_remote_code=True).eval()\n",
    "# use auto mode, automatically select precision based on the device.\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    \"Qwen/Qwen-7B-Chat/\",\n",
    "    device_map=\"auto\",\n",
    "    trust_remote_code=True\n",
    ").eval()\n",
    "\n",
    "# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.\n",
    "# model.generation_config = GenerationConfig.from_pretrained(\"Qwen/Qwen-7B-Chat/\", trust_remote_code=True)\n",
    "\n",
    "# 1st dialogue turn\n",
    "response, history = model.chat(tokenizer, \"你好\", history=None)\n",
    "print(response)\n",
    "# 你好！很高兴为你提供帮助。\n",
    "\n",
    "# 2nd dialogue turn\n",
    "response, history = model.chat(tokenizer, \"给我讲一个年轻人奋斗创业最终取得成功的故事。\", history=history)\n",
    "print(response)\n",
    "# 这是一个关于一个年轻人奋斗创业最终取得成功的故事。\n",
    "# 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。\n",
    "# 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。\n",
    "# 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。\n",
    "# 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。\n",
    "# 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。\n",
    "\n",
    "# 3rd dialogue turn\n",
    "response, history = model.chat(tokenizer, \"给这个故事起一个标题\", history=history)\n",
    "print(response)\n",
    "# 《奋斗创业：一个年轻人的成功之路》"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 3: LoRA Fine-Tuning Model (Single GPU)\n",
    "\n",
    "#### 3.1 Download Example Training Data\n",
    "Download the data required for training; here, we provide a tiny dataset as an example. It is sampled from [Belle](https://github.com/LianjiaTech/BELLE)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/qwen_recipes/Belle_sampled_qwen.json"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can refer to this format to prepare the dataset. Below is a simple example list with 1 sample:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"我是一个语言模型，我叫通义千问。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "You can also use multi-turn conversations as the training set. Here is a simple example:\n",
    "\n",
    "```json\n",
    "[\n",
    "  {\n",
    "    \"id\": \"identity_0\",\n",
    "    \"conversations\": [\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你好\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"你好！我是一名AI助手，我叫通义千问，有需要请告诉我。\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"user\",\n",
    "        \"value\": \"你都能做什么\"\n",
    "      },\n",
    "      {\n",
    "        \"from\": \"assistant\",\n",
    "        \"value\": \"我能做很多事情，包括但不限于回答各种领域的问题、提供实用建议和指导、进行多轮对话交流、文本生成等。\"\n",
    "      }\n",
    "    ]\n",
    "  }\n",
    "]\n",
    "```\n",
    "\n",
    "#### 3.2 Fine-Tune the Model\n",
    "\n",
    "You can directly run the prepared training script to fine-tune the model. Remember to check `model_name_or_path`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!python ../finetune/deepspeed/finetune.py \\\n",
    "    --model_name_or_path \"Qwen/Qwen-7B-Chat/\"\\\n",
    "    --data_path  \"Belle_sampled_qwen.json\"\\\n",
    "    --bf16 \\\n",
    "    --output_dir \"output_qwen\" \\\n",
    "    --num_train_epochs 5 \\\n",
    "    --per_device_train_batch_size 1 \\\n",
    "    --per_device_eval_batch_size 1 \\\n",
    "    --gradient_accumulation_steps 16 \\\n",
    "    --evaluation_strategy \"no\" \\\n",
    "    --save_strategy \"steps\" \\\n",
    "    --save_steps 1000 \\\n",
    "    --save_total_limit 10 \\\n",
    "    --learning_rate 1e-5 \\\n",
    "    --weight_decay 0.1 \\\n",
    "    --adam_beta2 0.95 \\\n",
    "    --warmup_ratio 0.01 \\\n",
    "    --lr_scheduler_type \"cosine\" \\\n",
    "    --logging_steps 1 \\\n",
    "    --report_to \"none\" \\\n",
    "    --model_max_length 512 \\\n",
    "    --gradient_checkpointing \\\n",
    "    --lazy_preprocess \\\n",
    "    --use_lora"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.3 Merge Weights\n",
    "\n",
    "LoRA training only saves the adapter parameters. You can load the fine-tuned model and merge weights as shown below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM\n",
    "from peft import PeftModel\n",
    "import torch\n",
    "\n",
    "model = AutoModelForCausalLM.from_pretrained(\"Qwen/Qwen-7B-Chat/\", torch_dtype=torch.float16, device_map=\"auto\", trust_remote_code=True)\n",
    "model = PeftModel.from_pretrained(model, \"output_qwen/\")\n",
    "merged_model = model.merge_and_unload()\n",
    "merged_model.save_pretrained(\"output_qwen_merged\", max_shard_size=\"2048MB\", safe_serialization=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The tokenizer files are not saved in the new directory in this step. You can copy the tokenizer files or use the following code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoTokenizer\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\n",
    "    \"Qwen/Qwen-7B-Chat/\",\n",
    "    trust_remote_code=True\n",
    ")\n",
    "\n",
    "tokenizer.save_pretrained(\"output_qwen_merged\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.4 Test the Model\n",
    "\n",
    "After merging the weights, we can test the model as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoModelForCausalLM, AutoTokenizer\n",
    "from transformers.generation import GenerationConfig\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"output_qwen_merged\", trust_remote_code=True)\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    \"output_qwen_merged\",\n",
    "    device_map=\"auto\",\n",
    "    trust_remote_code=True\n",
    ").eval()\n",
    "\n",
    "response, history = model.chat(tokenizer, \"你好\", history=None)\n",
    "print(response)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  },
  "vscode": {
   "interpreter": {
    "hash": "2d58e898dde0263bc564c6968b04150abacfd33eed9b19aaa8e45c040360e146"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
```

## File: `recipes/tests/README.md`
```markdown
# Unit testing
- Run all unit testing
```bash
cd tests && pytest -s 
```
- Run unit testing under a single folder
```bash
cd tests && pytest -s {dir}
```
- Rerun the test cases that failed in the last run
```bash
cd tests && pytest -s --lf
```
```

## File: `recipes/tests/utils.py`
```python
import logging
import subprocess
import socket
import openai


def run_in_subprocess(cmd):
    try:
        with subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ) as return_info:
            while True:
                next_line = return_info.stdout.readline()
                return_line = next_line.decode("utf-8", "ignore").strip()
                if return_line == "" and return_info.poll() != None:
                    break
                if return_line != "":
                    logging.info(return_line)

            err_lines = ""
            while True:
                next_line = return_info.stderr.readline()
                return_line = next_line.decode("utf-8", "ignore").strip()
                if return_line == "" and return_info.poll() != None:
                    break
                if return_line != "":
                    logging.info(return_line)
                    err_lines += return_line + "\n"

            return_code = return_info.wait()
            if return_code:
                raise RuntimeError(err_lines)
    except Exception as e:
        raise e


def simple_openai_api(model):
    openai.api_base = "http://localhost:8000/v1"
    openai.api_key = "none"

    # create a request not activating streaming response
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": "你好"}],
        stream=False,
        stop=[],  # You can add custom stop words here, e.g., stop=["Observation:"] for ReAct prompting.
    )
    print(response.choices[0].message.content)


def TelnetPort(server_ip, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    connect_flag = False
    try:
        sk.connect((server_ip, port))
        connect_flag = True
    except Exception:
        connect_flag = False
    sk.close()
    return connect_flag
```

## File: `recipes/tests/ut_config.py`
```python
import os

# common
MODEL_TYPE = "Qwen/Qwen-1_8B"
DOCKER_VERSION_CU114 = "qwenllm/qwen:cu114"
DOCKER_VERSION_CU117 = "qwenllm/qwen:cu117"
DOCKER_VERSION_CU121 = "qwenllm/qwen:cu121"
DOCKER_MOUNT_DIR = "/qwen-recipes"
DOCKER_TEST_DIR = os.path.join(DOCKER_MOUNT_DIR, "recipes/tests")

# finetune
DATA_DIR = os.path.join(DOCKER_MOUNT_DIR, "recipes/tests/assets/test_sampled_qwen.json")
DS_CONFIG_ZERO2_DIR = os.path.join(
    DOCKER_MOUNT_DIR, "finetune/ds_config_zero2.json"
)
DS_CONFIG_ZERO3_DIR = os.path.join(
    DOCKER_MOUNT_DIR, "finetune/ds_config_zero3.json"
)
```

## File: `recipes/tests/assets/test_sampled_qwen.json`
```json
[{"conversations": [{"from": "user", "value": "你好"}, {"from": "assistant", "value": "你好！很高兴为你提供帮助。"}], "id": "identity_0"}, {"conversations": [{"from": "user", "value": "给我讲一个年轻人奋斗创业最终取得成功的故事。"}, {"from": "assistant", "value": "这是一个关于一个年轻人奋斗创业最终取得成功的故事。"}], "id": "identity_1"}]
```

## File: `recipes/tests/test_finetune/test_finetune_ds.py`
```python
import os
import sys
import pytest
import shutil
from itertools import product
import torch
from modelscope.hub.snapshot_download import snapshot_download

sys.path.append(os.path.dirname(__file__) + "/..")
from utils import run_in_subprocess
from ut_config import (
    MODEL_TYPE,
    DOCKER_VERSION_CU114,
    DOCKER_VERSION_CU117,
    DOCKER_VERSION_CU121,
    DOCKER_MOUNT_DIR,
    DOCKER_TEST_DIR,
    DATA_DIR,
    DS_CONFIG_ZERO2_DIR,
    DS_CONFIG_ZERO3_DIR,
)

is_chat = ["chat", "base"]
docker_version = [DOCKER_VERSION_CU114, DOCKER_VERSION_CU117, DOCKER_VERSION_CU121]
# ZeRO3 is incompatible with LoRA when finetuning on base model.
# FSDP or ZeRO3 are incompatible with QLoRA.
parametrize_list_none_ds = list(
    product(*[[1], ["full", "lora"], is_chat, docker_version, [None]])
)
parametrize_list_ds_zero2 = list(
    product(*[[2], ["full", "lora"], is_chat, docker_version, [DS_CONFIG_ZERO2_DIR]])
)
parametrize_list_ds_zero3 = list(
    product(*[[2], ["full"], is_chat, docker_version, [DS_CONFIG_ZERO3_DIR]])
) + list(product(*[[2], ["lora"], ["chat"], docker_version, [DS_CONFIG_ZERO3_DIR]]))
parametrize_list_qlora = list(
    product(*[[1, 2], ["qlora"], ["chat"], docker_version, [None, DS_CONFIG_ZERO2_DIR]])
)
parametrize_list = (
    parametrize_list_none_ds
    + parametrize_list_ds_zero2
    + parametrize_list_ds_zero3
    + parametrize_list_qlora
)


@pytest.mark.parametrize(
    "num_gpus,train_type,is_chat,docker_version,deepspeed", parametrize_list
)
def test_finetune(num_gpus, train_type, is_chat, docker_version, deepspeed):
    cmd_docker = f"docker run --gpus all --ipc=host --network=host --rm -v {os.getcwd()}/../../../Qwen:{DOCKER_MOUNT_DIR} {docker_version} /bin/bash -c "
    cmd = ""
    # for GPUs SM < 80
    is_ampere = torch.cuda.get_device_capability()[0] >= 8
    if not is_ampere:
        cmd = f"pip uninstall -y flash-attn && "

    model_type = f"{MODEL_TYPE}-Chat" if is_chat == "chat" else MODEL_TYPE
    model_type = f"{model_type}-Int4" if train_type == "qlora" else model_type
    cmd += f"""torchrun --nproc_per_node {num_gpus} --nnodes 1 --node_rank 0 --master_addr localhost --master_port 12345 {DOCKER_MOUNT_DIR}/finetune.py \
    --model_name_or_path "{DOCKER_TEST_DIR}/{model_type}/" \
    --data_path  {DATA_DIR} \
    --output_dir "{DOCKER_TEST_DIR}/output_qwen" \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 2 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 1000 \
    --save_total_limit 10 \
    --learning_rate 1e-5 \
    --weight_decay 0.1 \
    --adam_beta2 0.95 \
    --warmup_ratio 0.01 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --report_to "none" \
    --model_max_length 512"""
    if deepspeed:
        cmd += f" --deepspeed {deepspeed}"
    if train_type == "lora":
        cmd += " --use_lora"
    elif train_type == "qlora":
        cmd += " --use_lora --q_lora"
    # for SM < 80
    if (
        (not is_ampere)
        and train_type == "lora"
        and (deepspeed and "zero2" in deepspeed)
        and is_chat == "base"
    ):
        cmd += " --fp16 True"
    snapshot_download(model_type, cache_dir=".", revision="master")
    run_in_subprocess(cmd_docker + f'"{cmd}"')
    if train_type == "full":
        assert os.path.exists("output_qwen/config.json")
    else:
        assert os.path.exists("output_qwen/adapter_config.json")
    shutil.rmtree("output_qwen")
```

## File: `recipes/tests/test_inference/test_inference_api.py`
```python
import os
import sys
import time
import pytest
import subprocess
import torch
from modelscope.hub.snapshot_download import snapshot_download

sys.path.append(os.path.dirname(__file__) + "/..")
from utils import run_in_subprocess, simple_openai_api, TelnetPort
from ut_config import (
    MODEL_TYPE,
    DOCKER_VERSION_CU114,
    DOCKER_VERSION_CU117,
    DOCKER_VERSION_CU121,
    DOCKER_MOUNT_DIR,
    DOCKER_TEST_DIR,
)


# use_cpu=True,use_int=False RuntimeError: "addmm_impl_cpu_" not implemented for 'Half'
# use_cpu=True,use_int4=True ValueError: Found modules on cpu/disk. Using Exllama or Exllamav2 backend requires all the modules to be on GPU.You can deactivate exllama backend by setting `disable_exllama=True` in the quantization config object
@pytest.mark.parametrize(
    "docker_version,use_cpu,use_int4",
    [
        (DOCKER_VERSION_CU114, False, False),
        (DOCKER_VERSION_CU114, False, True),
        (DOCKER_VERSION_CU117, False, False),
        (DOCKER_VERSION_CU117, False, True),
        (DOCKER_VERSION_CU121, False, False),
        (DOCKER_VERSION_CU121, False, True),
    ],
)
def test_inference_api(docker_version, use_cpu, use_int4):
    container_name = "test_inference_api"
    model_type = f"{MODEL_TYPE}-Chat-Int4" if use_int4 else f"{MODEL_TYPE}-Chat"
    cmd_docker = f'docker run --gpus all --ipc=host --network=host --rm --name="{container_name}" -p 8000:8000 -v {os.getcwd()}/../../../Qwen:{DOCKER_MOUNT_DIR} {docker_version} /bin/bash -c '
    cmd = ""
    # for GPUs SM < 80
    is_ampere = torch.cuda.get_device_capability()[0] >= 8
    if not is_ampere:
        cmd += f"pip uninstall -y flash-attn && "

    cmd += f"""python {DOCKER_MOUNT_DIR}/openai_api.py -c {DOCKER_TEST_DIR}/{model_type}"""

    if use_cpu:
        cmd += " --cpu-only"

    snapshot_download(model_type, cache_dir=".", revision="master")
    # start model server
    print(cmd_docker + f'"{cmd}"')
    run_in_subprocess(
        f'docker rm -f {container_name} 2>/dev/null || echo "The container does not exist."'
    )
    run_in_subprocess("nohup " + cmd_docker + f'"{cmd}"' + " > tmp.log 2>&1 &")

    while not TelnetPort("localhost", 8000):
        print("Wait for the model service start.")
        time.sleep(0.5)

        if (
            subprocess.run(
                f"docker inspect {container_name}",
                shell=True,
                stdout=subprocess.DEVNULL,
            ).returncode
            != 0
        ):
            break
    try:
        # while load int4 model such as Qwen-1_8B-Chat-Int4, the model name is Qwen-1_8B-Chat
        simple_openai_api(f"{MODEL_TYPE}-Chat".split("/")[-1])
    except Exception as e:
        time.sleep(1)
        with open("tmp.log") as f:
            raise Exception(f"{e} \n {f.read()}")

    run_in_subprocess(f"docker rm -f {container_name}")
```

## File: `recipes/tests/test_inference/test_inference_vllm_fschat.py`
```python
import os
import sys
import time
import pytest
import subprocess
import torch
from modelscope.hub.snapshot_download import snapshot_download

sys.path.append(os.path.dirname(__file__) + "/..")
from utils import run_in_subprocess, simple_openai_api, TelnetPort
from ut_config import (
    MODEL_TYPE,
    DOCKER_VERSION_CU121,
    DOCKER_MOUNT_DIR,
    DOCKER_TEST_DIR,
)


@pytest.mark.parametrize(
    "num_gpus,use_int4",
    [
        (1, False),
        (1, True),
        (2, False),
        # ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size.
        # (2, True)
    ],
)
def test_inference_vllm_fschat(num_gpus, use_int4):
    model_type = f"{MODEL_TYPE}-Chat-Int4" if use_int4 else f"{MODEL_TYPE}-Chat"
    container_name = "test_inference_vllm_fschat"
    cmd_docker = f'docker run --gpus all --ipc=host --network=host --rm --name="{container_name}" -p 8000:8000 -v {os.getcwd()}/../../../Qwen:{DOCKER_MOUNT_DIR} {DOCKER_VERSION_CU121} /bin/bash -c '
    cmd = ""

    cmd += f"""nohup python -m fastchat.serve.controller > /dev/null 2>&1 \
    & python -m fastchat.serve.openai_api_server --host localhost --port 8000 > /dev/null 2>&1 \
    & python -m fastchat.serve.vllm_worker --model-path {DOCKER_TEST_DIR}/{model_type} --tensor-parallel-size {num_gpus} --trust-remote-code"""

    # for GPUS SM < 80 and use_int==True
    is_ampere = torch.cuda.get_device_capability()[0] >= 8
    if not is_ampere or use_int4:
        cmd += " --dtype half"

    snapshot_download(model_type, cache_dir=".", revision="master")
    # start model server
    run_in_subprocess(
        f'docker rm -f {container_name} 2>/dev/null || echo "The container does not exist."'
    )
    print(cmd_docker + f'"{cmd}"')
    run_in_subprocess("nohup " + cmd_docker + f'"{cmd}"' + " > tmp.log 2>&1 &")

    while not TelnetPort("localhost", 21002):
        print("Wait for the model service start.")
        time.sleep(0.5)

        if (
            subprocess.run(
                f"docker inspect {container_name}",
                shell=True,
                stdout=subprocess.DEVNULL,
            ).returncode
            != 0
        ):
            break

    try:
        simple_openai_api(model_type.split("/")[-1])
    except Exception as e:
        time.sleep(1)
        with open("tmp.log") as f:
            raise Exception(f"{e} \n {f.read()}")

    run_in_subprocess(f"docker rm -f {container_name}")
```

