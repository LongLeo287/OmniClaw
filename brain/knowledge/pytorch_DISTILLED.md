---
id: pytorch
type: knowledge
owner: OA_Triage
---
# pytorch
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

<img alt="Lightning" src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/ptl_banner.png" width="800px" style="max-width: 100%;">

<br/>
<br/>

**The deep learning framework to pretrain and finetune AI models.**

**Serving models?** Use [LitServe](https://github.com/Lightning-AI/litserve?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) to build custom inference servers in pure Python.

______________________________________________________________________

<p align="center">
    <a href="#quick-start" style="margin: 0 10px;">Quick start</a> •
  <a href="#examples">Examples</a> •
  <a href="#why-pytorch-lightning">PyTorch Lightning</a> •
  <a href="#lightning-fabric-expert-control">Fabric</a> •
  <a href="https://lightning.ai/?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme">Lightning Cloud</a> •   
  <a href="#community">Community</a> •
  <a href="https://pytorch-lightning.readthedocs.io/en/stable/">Docs</a>
</p>

<!-- DO NOT ADD CONDA DOWNLOADS... README CHANGES MUST BE APPROVED BY EDEN OR WILL -->

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytorch-lightning)](https://pypi.org/project/pytorch-lightning/)
[![PyPI Status](https://badge.fury.io/py/pytorch-lightning.svg)](https://badge.fury.io/py/pytorch-lightning)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pytorch-lightning)](https://pepy.tech/project/pytorch-lightning)
[![Conda](https://img.shields.io/conda/v/conda-forge/lightning?label=conda&color=success)](https://anaconda.org/conda-forge/lightning)
[![codecov](https://codecov.io/gh/Lightning-AI/pytorch-lightning/graph/badge.svg?token=SmzX8mnKlA)](https://codecov.io/gh/Lightning-AI/pytorch-lightning)

[![Discord](https://img.shields.io/discord/1077906959069626439?style=plastic)](https://discord.gg/VptPCZkGNa)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/lightning-ai/lightning)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/Lightning-AI/pytorch-lightning/blob/master/LICENSE)

<!--
[![CodeFactor](https://www.codefactor.io/repository/github/Lightning-AI/lightning/badge)](https://www.codefactor.io/repository/github/Lightning-AI/lightning)
-->

</div>

<div align="center">
  
<p align="center">

&nbsp;

<a target="_blank" href="https://lightning.ai/docs/pytorch/latest/starter/introduction.html?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme#define-a-lightningmodule">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/get-started-badge.svg" height="36px" alt="Get started"/>
</a>

</p>

</div>

&nbsp;

<a id="why-pytorch-lightning"></a>
# Why PyTorch Lightning?   
Training models in plain PyTorch requires writing and maintaining a lot of repetitive engineering code. Handling backpropagation, mixed precision, multi-GPU, and distributed training is error-prone and often reimplemented for every project. PyTorch Lightning organizes PyTorch code to automate this infrastructure while keeping full control over your model logic. You write the science. Lightning handles the engineering, and scales from CPU to multi-node GPUs without changing your core code. PyTorch experts can still opt into [expert-level control](#lightning-fabric-expert-control).   

Fun analogy: If PyTorch is Javascript, PyTorch Lightning is ReactJS or NextJS.

# Looking for GPUs?
[Lightning Cloud](https://lightning.ai/?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) is the easiest way to run PyTorch Lightning without managing infrastructure. Start training with one command and get GPUs, autoscaling, monitoring, and a free tier. No cloud setup required.

You can also run PyTorch Lightning on your own hardware or cloud.

# Lightning has 2 core packages

[PyTorch Lightning: Train and deploy PyTorch at scale](#why-pytorch-lightning).
<br/>
[Lightning Fabric: Expert control](#lightning-fabric-expert-control).

Lightning gives you granular control over how much abstraction you want to add over PyTorch.

<div align="center">
    <img src="https://pl-public-data.s3.amazonaws.com/assets_lightning/continuum.png" width="80%">
</div>

&nbsp;

# Quick start
Install Lightning:

```bash
pip install lightning
```

<!-- following section will be skipped from PyPI description -->

<details>
  <summary>Advanced install options</summary>
    <!-- following section will be skipped from PyPI description -->

#### Install with optional dependencies

```bash
pip install lightning['extra']
```

#### Conda

```bash
conda install lightning -c conda-forge
```

#### Install stable version

Install future release from the source

```bash
pip install https://github.com/Lightning-AI/lightning/archive/refs/heads/release/stable.zip -U
```

#### Install bleeding-edge

Install nightly from the source (no guarantees)

```bash
pip install https://github.com/Lightning-AI/lightning/archive/refs/heads/master.zip -U
```

or from testing PyPI

```bash
pip install -iU https://test.pypi.org/simple/ pytorch-lightning
```

</details>
<!-- end skipping PyPI description -->

### PyTorch Lightning example
Define the training workflow. Here's a toy example ([explore real examples](https://lightning.ai/lightning-ai/studios?view=public&section=featured&query=pytorch+lightning&utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme)):

```python
# main.py
# ! pip install torchvision
import torch, torch.nn as nn, torch.utils.data as data, torchvision as tv, torch.nn.functional as F
import lightning as L

# --------------------------------
# Step 1: Define a LightningModule
# --------------------------------
# A LightningModule (nn.Module subclass) defines a full *system*
# (ie: an LLM, diffusion model, autoencoder, or simple image classifier).


class LitAutoEncoder(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(28 * 28, 128), nn.ReLU(), nn.Linear(128, 3))
        self.decoder = nn.Sequential(nn.Linear(3, 128), nn.ReLU(), nn.Linear(128, 28 * 28))

    def forward(self, x):
        # in lightning, forward defines the prediction/inference actions
        embedding = self.encoder(x)
        return embedding

    def training_step(self, batch, batch_idx):
        # training_step defines the train loop. It is independent of forward
        x, _ = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = F.mse_loss(x_hat, x)
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer


# -------------------
# Step 2: Define data
# -------------------
dataset = tv.datasets.MNIST(".", download=True, transform=tv.transforms.ToTensor())
train, val = data.random_split(dataset, [55000, 5000])

# -------------------
# Step 3: Train
# -------------------
autoencoder = LitAutoEncoder()
trainer = L.Trainer()
trainer.fit(autoencoder, data.DataLoader(train), data.DataLoader(val))
```

Run the model on your terminal

```bash
pip install torchvision
python main.py
```

&nbsp;


# Convert from PyTorch to PyTorch Lightning

PyTorch Lightning is just organized PyTorch - Lightning disentangles PyTorch code to decouple the science from the engineering.

![PT to PL](docs/source-pytorch/_static/images/general/pl_quick_start_full_compressed.gif)

&nbsp;

----

### Examples
Explore various types of training possible with PyTorch Lightning. Pretrain and finetune ANY kind of model to perform ANY task like classification, segmentation, summarization and more:    

| Task | Description | Run |
|------|--------------|-----|
| [Hello world](https://lightning.ai/lightning-ai/studios/pytorch-lightning-hello-world?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Pretrain - Hello world example | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/pytorch-lightning-hello-world?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Image classification](https://lightning.ai/lightning-ai/studios/image-classification-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Finetune - ResNet-34 model to classify images of cars | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/image-classification-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Image segmentation](https://lightning.ai/lightning-ai/studios/image-segmentation-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Finetune - ResNet-50 model to segment images | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/image-segmentation-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Object detection](https://lightning.ai/lightning-ai/studios/object-detection-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Finetune - Faster R-CNN model to detect objects | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/object-detection-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Text classification](https://lightning.ai/lightning-ai/studios/text-classification-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Finetune - text classifier (BERT model) | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/text-classification-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Text summarization](https://lightning.ai/lightning-ai/studios/text-summarization-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Finetune - text summarization (Hugging Face transformer model) | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/text-summarization-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Audio generation](https://lightning.ai/lightning-ai/studios/finetune-a-personal-ai-music-generator?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Finetune - audio generator (transformer model) | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/finetune-a-personal-ai-music-generator?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [LLM finetuning](https://lightning.ai/lightning-ai/studios/finetune-an-llm-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Finetune - LLM (Meta Llama 3.1 8B) | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/finetune-an-llm-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Image generation](https://lightning.ai/lightning-ai/studios/train-a-diffusion-model-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Pretrain - Image generator (diffusion model) | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/train-a-diffusion-model-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Recommendation system](https://lightning.ai/lightning-ai/studios/recommendation-system-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Train - recommendation system (factorization and embedding) | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/recommendation-system-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Time-series forecasting](https://lightning.ai/lightning-ai/studios/time-series-forecasting-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) | Train - Time-series forecasting with LSTM | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/time-series-forecasting-with-pytorch-lightning?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |


______________________________________________________________________

## Advanced features

Lightning has over [40+ advanced features](https://lightning.ai/docs/pytorch/stable/common/trainer.html?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme#trainer-flags)
designed for professional AI research at scale.

Here are some examples:

<div align="center">
    <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/features_2.jpg" max-height="600px">
  </div>

<details>
  <summary>Train on 1000s of GPUs without code changes</summary>

```python
# 8 GPUs
# no code changes needed
trainer = Trainer(accelerator="gpu", devices=8)

# 256 GPUs
trainer = Trainer(accelerator="gpu", devices=8, num_nodes=32)
```

</details>

<details>
  <summary>Train on other accelerators like TPUs without code changes</summary>

```python
# no code changes needed
trainer = Trainer(accelerator="tpu", devices=8)
```

</details>

<details>
  <summary>16-bit precision</summary>

```python
# no code changes needed
trainer = Trainer(precision=16)
```

</details>

<details>
  <summary>Experiment managers</summary>

```python
from lightning import loggers

# litlogger
trainer = Trainer(logger=LitLogger())

# tensorboard
trainer = Trainer(logger=TensorBoardLogger("logs/"))

# weights and biases
trainer = Trainer(logger=loggers.WandbLogger())

# comet
trainer = Trainer(logger=loggers.CometLogger())

# mlflow
trainer = Trainer(logger=loggers.MLFlowLogger())

# ... and dozens more
```

</details>

<details>

<summary>Early Stopping</summary>

```python
es = EarlyStoppin
... [TRUNCATED]
```

### File: requirements.txt
```txt
# the default package dependencies

-r ./requirements/fabric/base.txt
-r ./requirements/pytorch/base.txt

```

### File: setup.py
```py
#!/usr/bin/env python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This is the main and only one setup entry point for installing each package as stand-alone as well as joint
installation for all packages.

There are considered three main scenarios for installing this project:

1. Using PyPI registry when you can install `pytorch-lightning`, etc. or `lightning` for all.

2. Installation from source code after cloning repository.
    In such case we recommend to use command `pip install .` or `pip install -e .` for development version
     (development ver. do not copy python files to your pip file system, just create links, so you can edit here)
    In case you want to install just one package you need to export env. variable before calling `pip`

     - for `pytorch-lightning` use `export PACKAGE_NAME=pytorch ; pip install .`
     - for `lightning-fabric` use `export PACKAGE_NAME=fabric ; pip install .`

3. Building packages as sdist or binary wheel and installing or publish to PyPI afterwards you use command
    `python setup.py sdist` or `python setup.py bdist_wheel` accordingly.
   In case you want to build just a particular package you want to set an environment variable:
   `PACKAGE_NAME=lightning|pytorch|fabric python setup.py sdist|bdist_wheel`

4. Automated releasing with GitHub action is natural extension of 3) is composed of three consecutive steps:
    a) determine which packages shall be released based on version increment in `__version__.py` and eventually
     compared against PyPI registry
    b) with a parameterization build desired packages in to standard `dist/` folder
    c) validate packages and publish to PyPI

"""

import contextlib
import glob
import logging
import os
import tempfile
from collections.abc import Generator, Mapping
from importlib.util import module_from_spec, spec_from_file_location
from types import ModuleType
from typing import Optional

import setuptools
import setuptools.command.egg_info

_PACKAGE_NAME = os.environ.get("PACKAGE_NAME")
_PACKAGE_MAPPING = {
    "lightning": "lightning",
    "pytorch": "pytorch_lightning",
    "fabric": "lightning_fabric",
}
# https://packaging.python.org/guides/single-sourcing-package-version/
# http://blog.ionelmc.ro/2014/05/25/python-packaging/
_PATH_ROOT = os.path.dirname(__file__)
_PATH_SRC = os.path.join(_PATH_ROOT, "src")
_PATH_REQUIRE = os.path.join(_PATH_ROOT, "requirements")
_FREEZE_REQUIREMENTS = os.environ.get("FREEZE_REQUIREMENTS", "0").lower() in ("1", "true")


def _load_py_module(name: str, location: str) -> ModuleType:
    spec = spec_from_file_location(name, location)
    assert spec, f"Failed to load module {name} from {location}"
    py = module_from_spec(spec)
    assert spec.loader, f"ModuleSpec.loader is None for {name} from {location}"
    spec.loader.exec_module(py)
    return py


def _named_temporary_file(directory: Optional[str] = None) -> str:
    # `tempfile.NamedTemporaryFile` has issues in Windows
    # https://github.com/deepchem/deepchem/issues/707#issuecomment-556002823
    if directory is None:
        directory = tempfile.gettempdir()
    return os.path.join(directory, os.urandom(24).hex())


@contextlib.contextmanager
def _set_manifest_path(manifest_dir: str, aggregate: bool = False, mapping: Mapping = _PACKAGE_MAPPING) -> Generator:
    if aggregate:
        # aggregate all MANIFEST.in contents into a single temporary file
        manifest_path = _named_temporary_file(manifest_dir)
        lines = []
        # load manifest and aggregated all manifests
        for pkg in mapping.values():
            pkg_manifest = os.path.join(_PATH_SRC, pkg, "MANIFEST.in")
            if os.path.isfile(pkg_manifest):
                with open(pkg_manifest) as fh:
                    lines.extend(fh.readlines())
        # convert lightning_foo to lightning/foo
        for new, old in mapping.items():
            if old == "lightning":
                continue  # avoid `lightning` -> `lightning/lightning`
            lines = [ln.replace(old, f"lightning/{new}") for ln in lines]
        lines = sorted(set(filter(lambda ln: not ln.strip().startswith("#"), lines)))
        logging.debug(f"aggregated manifest consists of: {lines}")
        with open(manifest_path, mode="w") as fp:
            fp.writelines(lines)
    else:
        manifest_path = os.path.join(manifest_dir, "MANIFEST.in")
        assert os.path.exists(manifest_path)
    # avoid error: setup script specifies an absolute path
    manifest_path = os.path.relpath(manifest_path, _PATH_ROOT)
    # Use lazy logging formatting
    logging.info("Set manifest path to %s", manifest_path)
    setuptools.command.egg_info.manifest_maker.template = manifest_path
    yield
    # cleanup
    setuptools.command.egg_info.manifest_maker.template = "MANIFEST.in"
    if aggregate:
        os.remove(manifest_path)


if __name__ == "__main__":
    assistant = _load_py_module(name="assistant", location=os.path.join(_PATH_ROOT, ".actions", "assistant.py"))

    if os.path.isdir(_PATH_SRC):
        # copy the version information to all packages
        assistant.distribute_version(_PATH_SRC)
    print(f"Requested package: '{_PACKAGE_NAME}'")  # requires `-v` to appear

    local_pkgs = [
        os.path.basename(p)
        for p in glob.glob(os.path.join(_PATH_SRC, "*"))
        if os.path.isdir(p) and not p.endswith(".egg-info")
    ]
    print(f"Local package candidates: {local_pkgs}")
    is_source_install = len(local_pkgs) > 2
    print(f"Installing from source: {is_source_install}")
    if is_source_install:
        if _PACKAGE_NAME is not None and _PACKAGE_NAME not in _PACKAGE_MAPPING:
            raise ValueError(
                f"Unexpected package name: {_PACKAGE_NAME}. Possible choices are: {list(_PACKAGE_MAPPING)}"
            )
        package_to_install = _PACKAGE_MAPPING.get(_PACKAGE_NAME, "lightning")
        if package_to_install == "lightning":
            # merge all requirements files
            assistant._load_aggregate_requirements(_PATH_REQUIRE, _FREEZE_REQUIREMENTS)
        else:
            # replace imports and copy the code
            assistant.create_mirror_package(_PATH_SRC, _PACKAGE_MAPPING)
    else:
        assert len(local_pkgs) > 0
        # PL as a package is distributed together with Fabric, so in such case there are more than one candidate
        package_to_install = "pytorch_lightning" if "pytorch_lightning" in local_pkgs else local_pkgs[0]
    print(f"Installing package: {package_to_install}")

    # going to install with `setuptools.setup`
    pkg_path = os.path.join(_PATH_SRC, package_to_install)
    pkg_setup = os.path.join(pkg_path, "__setup__.py")
    if not os.path.exists(pkg_setup):
        raise RuntimeError(f"Something's wrong, no package was installed. Package name: {_PACKAGE_NAME}")
    setup_module = _load_py_module(name=f"{package_to_install}_setup", location=pkg_setup)
    setup_args = setup_module._setup_args()
    is_main_pkg = package_to_install == "lightning"
    print(f"Installing as the main package: {is_main_pkg}")
    if is_source_install:
        # we are installing from source, set the correct manifest path
        with _set_manifest_path(pkg_path, aggregate=is_main_pkg):
            setuptools.setup(**setup_args)
    else:
        setuptools.setup(**setup_args)
    print("Finished setup configuration.")

```

### File: .actions\requirements.txt
```txt
jsonargparse
requests
packaging

```

### File: docs\README.md
```md
# PyTorch-Lightning Docs

We are using Sphinx with Napoleon extension.
Moreover, we set Google style to follow with type convention.

- [Napoleon formatting with Google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- [ReStructured Text (reST)](https://docs.pylonsproject.org/projects/docs-style-guide/)
- [Paragraph-level markup](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#paragraphs)

See following short example of a sample function taking one position string and optional

```python
from typing import Optional


def my_func(param_a: int, param_b: Optional[float] = None) -> str:
    """Sample function.

    Args:
        param_a: first parameter
        param_b: second parameter

    Return:
        sum of both numbers

    Example::

        >>> my_func(1, 2)
        3

    Note:
        If you want to add something.
    """
    p = param_b if param_b else 0
    return str(param_a + p)
```

## Building Docs

When updating the docs, make sure to build them first locally and visually inspect the html files in your browser for
formatting errors. In certain cases, a missing blank line or a wrong indent can lead to a broken layout.
Run these commands

```bash
git submodule update --init --recursive
make docs
```

and open `docs/build/html/index.html` in your browser.

When you send a PR the continuous integration will run tests and build the docs.

Notes:

- You need to have LaTeX installed for rendering math equations. You can for example install TeXLive with the necessary extras by doing one of the following:
  - on Ubuntu (Linux) run `sudo apt-get update && sudo apt-get install -y texlive-latex-extra dvipng texlive-pictures`
  - use the [RTD docker image](https://hub.docker.com/r/readthedocs/build)
- You need to have pandoc installed for rendering Jupyter Notebooks. On Ubuntu (Linux), you can run: `sudo apt-get install pandoc`

## Developing docs

When developing the docs, building docs can be VERY slow locally because of the notebook tutorials.
To speed this up, enable this flag in before building docs:

```bash
# builds notebooks which is slow
export FAST_DOCS_DEV=0

# fast notebook build which is fast
export FAST_DOCS_DEV=1
```

## docs CSS/theme

To change the CSS theme of the docs, go [here](https://github.com/Lightning-AI/lightning_sphinx_theme).
Apologies in advance... this is a bit complex to build and requires basic understanding of javascript/npm.

```

### File: examples\README.md
```md
# Examples

*Note that some examples may rely on new features that are only available in the development branch and may be incompatible with any releases.*
*If you see any errors, you might want to consider switching to a version tag you would like to run examples with.*
*For example, if you're using `pytorch-lightning==1.6.4` in your environment and seeing issues, run examples of the tag [1.6.4](https://github.com/Lightning-AI/lightning/tree/1.6.4/pl_examples).*

______________________________________________________________________

## Lightning Fabric Examples

We show how to accelerate your PyTorch code with [Lightning Fabric](https://lightning.ai/docs/fabric) with minimal code changes.
You stay in full control of the training loop.

- [MNIST: Vanilla PyTorch vs. Fabric](fabric/image_classifier/README.md)
- [DCGAN: Vanilla PyTorch vs. Fabric](fabric/dcgan/README.md)

______________________________________________________________________

## Lightning Trainer Examples

In this folder, we have 2 simple examples that showcase the power of the Lightning Trainer.

- [Image Classifier](pytorch/basics/backbone_image_classifier.py) (trains arbitrary datasets with arbitrary backbones).
- [Autoencoder](pytorch/basics/autoencoder.py)

```

### File: requirements\README.md
```md
# Project Requirements

This root requirements folder branches into sub-folders depending on the python package.
Within the folder, we have grouped requirements files/lists per focus, which shall closely match package extra
So, for example, when you install PL as `pip install pytorch-lightning[extra]`, this list is stored in `requirements/pytorch/extra.txt`.

## CI/CD upper bounds

For Ci stability, we have set for all package versions upper bounds (the latest version), so with any sudden release, we won't put our development on fire.
The continues updated of these upper bounds are managed by dependabot.
Note that these upper bounds are lifters when installing a package from the source or as a package.
If you want to preserve/enforce restrictions on the latest compatible version, add "strict" as an in-line comment.

```

### File: tests\README.md
```md
# PyTorch-Lightning Tests

Most of the tests in PyTorch Lightning train a [BoringModel](https://github.com/Lightning-AI/pytorch-lightning/blob/master/src/lightning/pytorch/demos/boring_classes.py) under various trainer conditions (ddp, amp, etc...). Want to add a new test case and not sure how? [Talk to us!](https://www.pytorchlightning.ai/community)

## Running tests

**Local:** Testing your work locally will help you speed up the process since it allows you to focus on particular (failing) test-cases.
To setup a local development environment, install both local and test dependencies:

```bash
# clone the repo
git clone https://github.com/Lightning-AI/lightning.git
cd lightning

# install required dependencies
export PACKAGE_NAME=pytorch
python -m pip install ".[dev, examples]"
# install pre-commit (optional)
python -m pip install pre-commit
pre-commit install
```

Additionally, for testing backward compatibility with older versions of PyTorch Lightning, you also need to download all saved version-checkpoints from the public AWS storage. Run the following script to get all saved version-checkpoints:

```bash
bash .actions/pull_legacy_checkpoints.sh
```

Note: These checkpoints are generated to set baselines for maintaining backward compatibility with legacy versions of PyTorch Lightning. Details of checkpoints for back-compatibility can be found [here](https://github.com/Lightning-AI/pytorch-lightning/tree/master/tests/legacy/README.md).

You can run the full test suite in your terminal via this make script:

```bash
make test
```

Note: if your computer does not have multi-GPU or TPU these tests are skipped.

**GitHub Actions:** For convenience, you can also use your own GHActions building which will be triggered with each commit.
This is useful if you do not test against all required dependency versions.

**Docker:** Another option is to utilize the [pytorch lightning cuda base docker image](https://hub.docker.com/r/pytorchlightning/pytorch_lightning/tags?name=cuda). You can then run:

```bash
python -m pytest src/lightning/pytorch tests/tests_pytorch -v
```

You can also run a single test as follows:

```bash
python -m pytest -v tests/tests_pytorch/trainer/test_trainer_cli.py::test_default_args
```

### Conditional Tests

To test models that require GPU make sure to run the above command on a GPU machine.
The GPU machine must have at least 2 GPUs to run distributed tests.

Note that this setup will not run tests that require specific packages installed
You can rely on our CI to make sure all these tests pass.

### Standalone Tests

There are certain standalone tests, which you can run using:

```bash
cd tests/
wget https://raw.githubusercontent.com/Lightning-AI/utilities/main/scripts/run_standalone_tests.sh
./tests/run_standalone_tests.sh tests_pytorch/
```

## Running Coverage

Make sure to run coverage on a GPU machine with at least 2 GPUs.

```bash
# generate coverage (coverage is also installed as part of dev dependencies)
coverage run --source src/lightning/pytorch -m pytest src/lightning/pytorch tests/tests_pytorch -v

# print coverage stats
coverage report -m

# exporting results
coverage xml
```

```

### File: .github\workflows\README.md
```md
<!-- Note: This document cannot be in `.github/README.md` because it will overwrite the repo README.md -->

# Continuous Integration and Delivery

Brief description of all our automation tools used for boosting development performances.

## Unit and Integration Testing

| workflow file                          | action                                                                                    | accelerator |
| -------------------------------------- | ----------------------------------------------------------------------------------------- | ----------- |
| .github/workflows/ci-tests-fabric.yml  | Run all tests except for accelerator-specific and standalone.                             | CPU         |
| .github/workflows/ci-tests-pytorch.yml | Run all tests except for accelerator-specific and standalone.                             | CPU         |
| .github/workflows/ci-tests-data.yml    | Run unit and integration tests with data pipelining.                                      | CPU         |
| .azure-pipelines/gpu-tests-fabric.yml  | Run only GPU-specific tests, standalone\*, and examples.                                  | GPU         |
| .azure-pipelines/gpu-tests-pytorch.yml | Run only GPU-specific tests, standalone\*, and examples.                                  | GPU         |
| .azure-pipelines/gpu-benchmarks.yml    | Run speed/memory benchmarks for parity with vanila PyTorch.                               | GPU         |
| .github/workflows/ci-flagship-apps.yml | Run end-2-end tests with full applications, including deployment to the production cloud. | CPU         |
| .github/workflows/ci-tests-pytorch.yml | Run all tests except for accelerator-specific, standalone and slow tests.                 | CPU         |
| .github/workflows/tpu-tests.yml        | Run only TPU-specific tests. Requires that the PR title contains '[TPU]'                  | TPU         |

\* Each standalone test needs to be run in separate processes to avoid unwanted interactions between test cases.

- Accelerators used in CI

  - GPU: 2 x NVIDIA RTX 3090
  - TPU: [Google TPU v4-8](https://cloud.google.com/tpu/docs)

- To check which versions of Python or PyTorch are used for testing in our CI, see the corresponding workflow files or checkgroup config file at [`.github/checkgroup.yml`](../checkgroup.yml).

## Documentation

| workflow file                                                                   | action                                                                   |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| .github/workflows/docs-build.yml                                                | Run doctest, linkcheck and full HTML build.                              |
| .github/workflows/ci-rtfd.yml                                                   | Append link to the PR description with temporaty ReadTheDocs build docs. |
| .github/workflows/ci-check-md-links.yml <br> .github/markdown.links.config.json | Validate links in markdown files.                                        |

## Code Quality

| workflow file                     | action                                                                                    |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| .codecov.yml                      | Measure test coverage with [codecov.io](https://app.codecov.io/gh/Lightning-AI/lightning) |
| .github/workflows/code-checks.yml | Check Python typing with [MyPy](https://mypy.readthedocs.io/en/stable/).                  |
| .github/workflows/ci-schema.yml   | Validate the syntax of workflow files.                                                    |

## Others

| workflow file                        | action                                                                                          |
| ------------------------------------ | ----------------------------------------------------------------------------------------------- |
| .github/workflows/docker-build.yml   | Build docker images used for testing in CI. If run on nightly schedule, push to the Docker Hub. |
| .github/workflows/ci-pkg-install.yml | Test if pytorch-lightning is successfully installed using pip.                                  |
| .github/workflows/ci-checkpoints.yml | Build checkpoints that are will be tested on release to ensure backwards-compatibility          |

The published Docker Hub project is https://hub.docker.com/r/pytorchlightning/pytorch_lightning.

## Deployment

| workflow file                              | action                                                                         |
| ------------------------------------------ | ------------------------------------------------------------------------------ |
| .github/workflows/docs-build.yml           | Build the docs for each project and puch it to GCS with automatics deployment. |
| .github/workflows/docker-build.yml         | Build docker images used for releases and push them to the Docker Hub.         |
| .github/workflows/release-pkg.yml          | Publish a release to PyPI and upload to the GH release page as artifact.       |
| .github/workflows/\_legacy-checkpoints.yml | Add on request generate legacy checkpoints and upload them to AWS S3.          |

## Bots

| workflow file                                                          | action                                                                                                                                                   |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .github/mergify.yml                                                    | Label PRs as conflicts or ready, and request reviews if needed.                                                                                          |
| .github/workflows/probot-auto-cc.yml <br> .github/lightning-probot.yml | Notify maintainers of interest depending on labels added to an issue We utilize lightning-probot forked from PyTorch’s probot.                           |
| .github/workflows/probot-check-group.yml <br> .github/checkgroup.yml   | Checks whether the relevant jobs were successfully run based on the changed files in the PR                                                              |
| .pre-commit-config.yaml                                                | It applies a set of linters and formatters and can be registered with your local dev. If needed [bot](https://pre-commit.ci/) pushc changes to each PRs. |
| .github/workflows/labeler-pr.yml, .github/label-change.yml             | Integration of https://github.com/actions/labeler                                                                                                        |
| .github/workflows/labeler-issue.yml                                    | Parse user provided `lightning` version and set it as label.                                                                                             |

```

### File: tests\legacy\README.md
```md
# Maintaining backward compatibility with legacy versions

The aim of this section is to set some baselines and workflows/guidelines for maintaining backward compatibility with some legacy versions of PyTorch Lightning.

At this moment, we focus on ability to run old checkpoints, so the flow here is to create a checkpoint with every release and store it in our public AWS storage. Stored legacy checkpoints are then used in each CI to test loading and resuming training with the archived checkpoints.

## Download legacy checkpoints

If you want to pull all saved version-checkpoints for local testing/development, call

```bash
bash .actions/pull_legacy_checkpoints.sh
```

## Generate legacy checkpoints locally

To back populate collection with past versions you can use the following command:

```bash
bash generate_checkpoints.sh "1.3.7" "1.3.8"
zip -r checkpoints.zip checkpoints/
```

```

### File: examples\pytorch\basics\README.md
```md
## Basic Examples

Use these examples to test how Lightning works.

### AutoEncoder

This script shows you how to implement a CNN auto-encoder.

```bash
# CPU
python autoencoder.py

# GPUs (any number)
python autoencoder.py --trainer.accelerator 'gpu' --trainer.devices 2

# Distributed Data Parallel (DDP)
python autoencoder.py --trainer.accelerator 'gpu' --trainer.devices 2 --trainer.strategy 'ddp'
```

______________________________________________________________________

### Backbone Image Classifier

This script shows you how to implement a `LightningModule` as a system.
A system describes a `LightningModule` which takes a single `torch.nn.Module` which makes exporting to producion simpler.

```bash
# CPU
python backbone_image_classifier.py

# GPUs (any number)
python backbone_image_classifier.py --trainer.accelerator 'gpu' --trainer.devices 2

# Distributed Data Parallel (DDP)
python backbone_image_classifier.py --trainer.accelerator 'gpu' --trainer.devices 2 --trainer.strategy 'ddp'
```

______________________________________________________________________

### Transformers

This example contains a simple training loop for next-word prediction with a [Transformer model](https://arxiv.org/abs/1706.03762) on a subset of the [WikiText2](https://www.salesforce.com/products/einstein/ai-research/the-wikitext-dependency-language-modeling-dataset/) dataset.

```bash
python transformer.py
```

______________________________________________________________________

### PyTorch Profiler

This script shows you how to activate the [PyTorch Profiler](https://github.com/pytorch/kineto) with Lightning.

```bash
python profiler_example.py
```

```

### File: .pre-commit-config.yaml
```yaml
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

default_language_version:
  python: python3

ci:
  autofix_prs: true
  autoupdate_commit_msg: "[pre-commit.ci] pre-commit suggestions"
  autoupdate_schedule: quarterly
  # submodules: true

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
        exclude: README.md # keep formatting in README flexible
      - id: check-json
      - id: check-yaml
      - id: check-toml
      - id: check-docstring-first
      - id: check-executables-have-shebangs
      - id: check-case-conflict
      - id: check-added-large-files
        args: ["--maxkb=350", "--enforce-all"]
        exclude: |
          (?x)^(
              docs/source-pytorch/_static/images/general/fast_2.gif|
              docs/source-pytorch/_static/images/mnist_imgs/pt_to_pl.jpg|
              docs/source-pytorch/_static/images/lightning_module/pt_to_pl.png|
              docs/source-pytorch/_static/images/general/pl_quick_start_full_compressed.gif|
              docs/source-pytorch/_static/images/general/pl_overview_flat.jpg|
              docs/source-pytorch/_static/images/general/pl_overview.gif|
              src/lightning/fabric/CHANGELOG.md|
              src/lightning/pytorch/CHANGELOG.md
          )$
      - id: detect-private-key

  - repo: https://github.com/codespell-project/codespell
    rev: v2.4.1
    hooks:
      - id: codespell
        additional_dependencies: [tomli]
        #args: ["--write-changes"] # uncomment if you want to get automatic fixing

  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.7
    hooks:
      - id: docformatter
        # TODO: remove language_version pin once docformatter drops the `untokenize` dependency
        # which uses `ast.Constant.s` — removed in Python 3.14, causing pre-commit.ci to fail
        language_version: python3.12
        additional_dependencies: [tomli]
        args: ["--in-place"]

  - repo: https://github.com/sphinx-contrib/sphinx-lint
    rev: v1.0.2
    hooks:
      - id: sphinx-lint

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.10
    hooks:
      # try to fix what is possible
      - id: ruff
        args: ["--fix", "--unsafe-fixes"]
      # perform formatting updates
      - id: ruff-format
      # validate if all is fine with preview mode
      - id: ruff

  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.22
    hooks:
      - id: mdformat
        additional_dependencies:
          - mdformat-gfm
          #- mdformat-black
          - mdformat_frontmatter
        exclude: |
          (?x)^(
              src/lightning/fabric/CHANGELOG.md|
              src/lightning/pytorch/CHANGELOG.md|
              README.md
          )$

  - repo: https://github.com/JoC0de/pre-commit-prettier
    rev: v3.7.4
    hooks:
      - id: prettier
        # https://prettier.io/docs/en/options.html#print-width
        files: \.(json|yml|yaml|toml)
        args: ["--print-width=120"]

```

### File: SECURITY.md
```md
developer@lightning.ai

```

### File: .actions\assistant.py
```py
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import glob
import logging
import os
import re
import shutil
import tempfile
import urllib.request
from collections.abc import Iterable, Iterator, Sequence
from itertools import chain
from os.path import dirname, isfile
from pathlib import Path
from typing import Any, Optional

from packaging.requirements import Requirement
from packaging.version import Version

REQUIREMENT_FILES = {
    "pytorch": (
        "requirements/pytorch/base.txt",
        "requirements/pytorch/extra.txt",
        "requirements/pytorch/strategies.txt",
        "requirements/pytorch/examples.txt",
    ),
    "fabric": (
        "requirements/fabric/base.txt",
        "requirements/fabric/strategies.txt",
    ),
    "data": ("requirements/data/data.txt",),
}
REQUIREMENT_FILES_ALL = list(chain(*REQUIREMENT_FILES.values()))

_PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))


class _RequirementWithComment(Requirement):
    strict_cmd = "strict"

    def __init__(self, *args: Any, comment: str = "", pip_argument: Optional[str] = None, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.comment = comment
        assert pip_argument is None or pip_argument  # sanity check that it's not an empty str
        self.pip_argument = pip_argument
        self.strict = self.strict_cmd in comment.lower()

    def adjust(self, unfreeze: str) -> str:
        """Remove version restrictions unless they are strict.

        >>> _RequirementWithComment("arrow<=1.2.2,>=1.2.0", comment="# anything").adjust("none")
        'arrow<=1.2.2,>=1.2.0'
        >>> _RequirementWithComment("arrow<=1.2.2,>=1.2.0", comment="# strict").adjust("none")
        'arrow<=1.2.2,>=1.2.0  # strict'
        >>> _RequirementWithComment('arrow<=1.2.2,>=1.2.0; python_version >= "3.10"', comment="# my name").adjust("all")
        'arrow>=1.2.0; python_version >= "3.10"'
        >>> _RequirementWithComment("arrow>=1.2.0, <=1.2.2", comment="# strict").adjust("all")
        'arrow<=1.2.2,>=1.2.0  # strict'
        >>> _RequirementWithComment('arrow; python_version >= "3.10"').adjust("all")
        'arrow; python_version >= "3.10"'
        >>> _RequirementWithComment("arrow>=1.2.0, <=1.2.2", comment="# cool").adjust("major")
        'arrow<2.0,>=1.2.0'
        >>> _RequirementWithComment("arrow>=1.2.0, <=1.2.2", comment="# strict").adjust("major")
        'arrow<=1.2.2,>=1.2.0  # strict'
        >>> _RequirementWithComment('arrow>=1.2.0; python_version >= "3.10"').adjust("major")
        'arrow>=1.2.0; python_version >= "3.10"'
        >>> _RequirementWithComment("arrow").adjust("major")
        'arrow'

        """
        out = str(self)
        if self.strict:
            return f"{out}  # {self.strict_cmd}"

        specs = [(spec.operator, spec.version) for spec in self.specifier]
        if unfreeze == "major":
            for operator, version in specs:
                if operator in ("<", "<="):
                    major = Version(version).major
                    # replace upper bound with major version increased by one
                    return out.replace(f"{operator}{version}", f"<{major + 1}.0")
        elif unfreeze == "all":
            for operator, version in specs:
                if operator in ("<", "<="):
                    # drop upper bound
                    return out.replace(f"{operator}{version},", "")
        elif unfreeze != "none":
            raise ValueError(f"Unexpected unfreeze: {unfreeze!r} value.")
        return out


def _parse_requirements(lines: Iterable[str]) -> Iterator[_RequirementWithComment]:
    """Adapted from `pkg_resources.parse_requirements` to include comments.

    >>> txt = ['# ignored', '', 'this # is an', '--piparg', 'example', 'foo # strict', 'thing', '-r different/file.txt']
    >>> [r.adjust('none') for r in _parse_requirements(txt)]
    ['this', 'example', 'foo  # strict', 'thing']

    """
    pip_argument = None
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Drop comments -- a hash without a space may be in a URL.
        if " #" in line:
            comment_pos = line.find(" #")
            line, comment = line[:comment_pos], line[comment_pos:]
        else:
            comment = ""
        # If there's a pip argument, save it
        if line.startswith("--"):
            pip_argument = line
            continue
        if line.startswith("-r "):
            # linked requirement files are unsupported
            continue
        yield _RequirementWithComment(line, comment=comment, pip_argument=pip_argument)
        pip_argument = None


def load_requirements(path_dir: str, file_name: str = "base.txt", unfreeze: str = "all") -> list[str]:
    """Loading requirements from a file.

    >>> path_req = os.path.join(_PROJECT_ROOT, "requirements")
    >>> load_requirements(path_req, "docs.txt", unfreeze="major")  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    ['sphinx<...]

    """
    assert unfreeze in {"none", "major", "all"}
    path = Path(path_dir) / file_name
    if not path.exists():
        logging.warning(f"Folder {path_dir} does not have any base requirements.")
        return []
    assert path.exists(), (path_dir, file_name, path)
    text = path.read_text().splitlines()
    return [req.adjust(unfreeze) for req in _parse_requirements(text)]


def load_readme_description(path_dir: str, homepage: str, version: str) -> str:
    """Load readme as decribtion.

    >>> load_readme_description(_PROJECT_ROOT, "", "")  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    '...PyTorch Lightning is just organized PyTorch...'

    """
    path_readme = os.path.join(path_dir, "README.md")
    with open(path_readme, encoding="utf-8") as fopen:
        text = fopen.read()

    # drop images from readme
    text = text.replace(
        "![PT to PL](docs/source-pytorch/_static/images/general/pl_quick_start_full_compressed.gif)", ""
    )

    # https://github.com/Lightning-AI/lightning/raw/master/docs/source/_static/images/lightning_module/pt_to_pl.png
    github_source_url = os.path.join(homepage, "raw", version)
    # replace relative repository path to absolute link to the release
    #  do not replace all "docs" as in the readme we reger some other sources with particular path to docs
    text = text.replace(
        "docs/source-pytorch/_static/", f"{os.path.join(github_source_url, 'docs/source-app/_static/')}"
    )

    # readthedocs badge
    text = text.replace("badge/?version=stable", f"badge/?version={version}")
    text = text.replace("pytorch-lightning.readthedocs.io/en/stable/", f"pytorch-lightning.readthedocs.io/en/{version}")
    # codecov badge
    text = text.replace("/branch/master/graph/badge.svg", f"/release/{version}/graph/badge.svg")
    # github actions badge
    text = text.replace("badge.svg?branch=master&event=push", f"badge.svg?tag={version}")
    # azure pipelines badge
    text = text.replace("?branchName=master", f"?branchName=refs%2Ftags%2F{version}")

    skip_begin = r"<!-- following section will be skipped from PyPI description -->"
    skip_end = r"<!-- end skipping PyPI description -->"
    # todo: wrap content as commented description
    return re.sub(rf"{skip_begin}.+?{skip_end}", "<!--  -->", text, flags=re.IGNORECASE + re.DOTALL)

    # # https://github.com/Borda/pytorch-lightning/releases/download/1.1.0a6/codecov_badge.png
    # github_release_url = os.path.join(homepage, "releases", "download", version)
    # # download badge and replace url with local file
    # text = _parse_for_badge(text, github_release_url)


def distribute_version(src_folder: str, ver_file: str = "version.info") -> None:
    """Copy the global version to all packages."""
    ls_ver = glob.glob(os.path.join(src_folder, "*", "__version__.py"))
    ver_template = os.path.join(src_folder, ver_file)
    for fpath in ls_ver:
        fpath = os.path.join(os.path.dirname(fpath), ver_file)
        print("Distributing the version to", fpath)
        if os.path.isfile(fpath):
            os.remove(fpath)
        shutil.copy2(ver_template, fpath)


def _load_aggregate_requirements(req_dir: str = "requirements", freeze_requirements: bool = False) -> None:
    """Load all base requirements from all particular packages and prune duplicates.

    >>> _load_aggregate_requirements(os.path.join(_PROJECT_ROOT, "requirements"))

    """
    requires = [
        load_requirements(d, unfreeze="none" if freeze_requirements else "major")
        for d in glob.glob(os.path.join(req_dir, "*"))
        # skip empty folder (git artifacts), and resolving Will's special issue
        if os.path.isdir(d) and len(glob.glob(os.path.join(d, "*"))) > 0 and not os.path.basename(d).startswith("_")
    ]
    if not requires:
        return
    # TODO: add some smarter version aggregation per each package
    requires = sorted(set(chain(*requires)))
    with open(os.path.join(req_dir, "base.txt"), "w") as fp:
        fp.writelines([ln + os.linesep for ln in requires] + [os.linesep])


def _retrieve_files(directory: str, *ext: str) -> list[str]:
    all_files = []
    for root, _, files in os.walk(directory):
        for fname in files:
            if not ext or any(os.path.split(fname)[1].lower().endswith(e) for e in ext):
                all_files.append(os.path.join(root, fname))

    return all_files


def _replace_imports(lines: list[str], mapping: list[tuple[str, str]], lightning_by: str = "") -> list[str]:
    """Replace imports of standalone package to lightning.

    >>> lns = [
    ...     '"lightning_app"',
    ...     "lightning_app",
    ...     "lightning_app/",
    ...     "delete_cloud_lightning_apps",
    ...     "from lightning_app import",
    ...     "lightning_apps = []",
    ...     "lightning_app and pytorch_lightning are ours",
    ...     "def _lightning_app():",
    ...     ":class:`~lightning_app.core.flow.LightningFlow`",
    ...     "http://pytorch_lightning.ai",
    ...     "from lightning import __version__",
    ...     "@lightning.ai"
    ... ]
    >>> mapping = [("lightning_app", "lightning.app"), ("pytorch_lightning", "lightning.pytorch")]
    >>> _replace_imports(lns, mapping, lightning_by="lightning_fabric")  # doctest: +NORMALIZE_WHITESPACE
    ['"lightning.app"', \
     'lightning.app', \
     'lightning_app/', \
     'delete_cloud_lightning_apps', \
     'from lightning.app import', \
     'lightning_apps = []', \
     'lightning.app and lightning.pytorch are ours', \
     'def _lightning_app():', \
     ':class:`~lightning.app.core.flow.LightningFlow`', \
     'http://pytorch_lightning.ai', \
     'from lightning_fabric import __version__', \
     '@lightning.ai']

    """
    out = lines[:]
    for source_import, target_import in mapping:
        for i, ln in enumerate(out):
            out[i] = re.sub(
                rf"([^_/@]|^){source_import}([^_\w/]|$)",
                rf"\1{target_import}\2",
                ln,
            )
            if lightning_by:  # in addition, replace base package
                out[i] = out[i].replace("from lightning import ", f"from {lightning_by} import ")
                out[i] = out[i].replace("import lightning ", f"import {lightning_by} ")
    return out


def copy_replace_imports(
    source_dir: str,
    source_imports: Sequence[str],
    target_imports: Sequence[str],
    target_dir: Optional[str] = None,
    lightning_by: str = "",
) -> None:
    """Copy package content with import adjustments."""
    print(f"Replacing imports: {locals()}")
    assert len(source_imports) == len(target_imports), (
        "source and target imports must have the same length, "
        f"source: {len(source_imports)}, target: {len(target_imports)}"
    )
    if target_dir is None:
        target_dir = source_dir

    ls = _retrieve_files(source_dir)
    for fp in ls:
        fp_new = fp.replace(source_dir, target_dir)
        _, ext = os.path.splitext(fp)
        if ext in (".png", ".jpg", ".ico"):
            os.makedirs(dirname(fp_new), exist_ok=True)
            if not isfile(fp_new):
                shutil.copy(fp, fp_new)
            continue
        if ext in (".pyc",):
            continue
        # Try to parse everything else
        with open(fp, encoding="utf-8") as fopen:
            try:
                lines = fopen.readlines()
            except UnicodeDecodeError:
                # a binary file, skip
                print(f"Skipped replacing imports for {fp}")
                continue
        lines = _replace_imports(lines, list(zip(source_imports, target_imports)), lightning_by=lightning_by)
        os.makedirs(os.path.dirname(fp_new), exist_ok=True)
        with open(fp_new, "w", encoding="utf-8") as fopen:
            fopen.writelines(lines)


def create_mirror_package(source_dir: str, package_mapping: dict[str, str]) -> None:
    """Create a mirror package with adjusted imports."""
    # replace imports and copy the code
    mapping = package_mapping.copy()
    mapping.pop("lightning", None)  # pop this key to avoid replacing `lightning` to `lightning.lightning`

    mapping = {f"lightning.{sp}": sl for sp, sl in mapping.items()}
    for pkg_from, pkg_to in mapping.items():
        source_imports, target_imports = zip(*mapping.items())
        copy_replace_imports(
            source_dir=os.path.join(source_dir, pkg_from.replace(".", os.sep)),
            # pytorch_lightning uses lightning_fabric, so we need to replace all imports for all directories
            source_imports=source_imports,
            target_imports=target_imports,
            target_dir=os.path.join(source_dir, pkg_to.replace(".", os.sep)),
            lightning_by=pkg_from,
        )


class AssistantCLI:
    @staticmethod
    def copy_replace_imports(
        source_dir: str,
        source_import: str,
        target_import: str,
        target_dir: Optional[str] = None,
        lightning_by: str = "",
    ) -> None:
        """Copy package content with import adjustments."""
        source_imports = source_import.strip().split(",")
        target_imports = target_import.strip().split(",")
        copy_replace_imports(
            source_dir, source_imports, target_imports, target_dir=target_dir, lightning_by=lightning_by
        )

    @staticmethod
    def pull_docs_files(
        gh_user_repo: str,
        target_dir: str = "docs/source-pytorch/XXX",
        checkout: str = "refs/tags/1.0.0",
        source_dir: str = 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
