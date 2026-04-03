---
id: end-to-end-chest-disease-classification-knowledge
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:21.908240
---

# KNOWLEDGE EXTRACT: End-to-End-Chest-Disease-Classification
> **Extracted on:** 2026-03-29 21:40:31
> **Source:** End-to-End-Chest-Disease-Classification

---

## File: `.dockerignore`
```
.github/
.jenkins/
docs/
Artifacts/
Logs/
Notebook_Experiments/
chestenv/
```

## File: `.dvcignore`
```
# Add patterns of files dvc should ignore, which could improve
# the performance. Learn more at
# https://dvc.org/doc/user-guide/dvcignore
```

## File: `.gitignore`
```
# Environments
chestenv
Notebook_Experiments/Data
mlruns
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
```

## File: `app.py`
```python
import os
from Respire.Utils import decodeImage
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, render_template
from Respire.Pipeline.Prediction_Pipeline import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #for AWS
```

## File: `docker-compose.yml`
```yaml
version: '3'
services:
  application:
    image: "${IMAGE_NAME}"
    ports:
      - "8080:8080"
```

## File: `Dockerfile`
```
FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
```

## File: `dvc.lock`
```
schema: '2.0'
stages:
  Data_Ingestion:
    cmd: python Respire\Pipeline\Data_Ingestion.py
    deps:
    - path: Config\config.yaml
      hash: md5
      md5: 0b75ac98a8aea3e04f42f671359b236c
      size: 560
    - path: Respire\Components\Data_Ingestion.py
      hash: md5
      md5: 64c516517af256dc44af001346813546
      size: 1439
    - path: Respire\Pipeline\Data_Ingestion.py
      hash: md5
      md5: 0380ed98a36cd2e9941f214f5c248017
      size: 591
    outs:
    - path: Artifacts\Data_Ingestion\Chest-CT-Scan-data
      hash: md5
      md5: 904fa45d934ce879b3b1933dca6cb2f1.dir
      size: 49247431
      nfiles: 343
  Base_Model:
    cmd: python Respire/Pipeline/Base_Model.py
    deps:
    - path: Config/config.yaml
      hash: md5
      md5: 0b75ac98a8aea3e04f42f671359b236c
      size: 560
    - path: Respire/Pipeline/Base_Model.py
      hash: md5
      md5: eb811c7cbed55a61c4db8f93b831c3c3
      size: 622
    params:
      params.yaml:
        CLASSES: 2
        IMAGE_SIZE:
        - 224
        - 224
        - 3
        INCLUDE_TOP: false
        LEARNING_RATE: 0.01
        WEIGHTS: imagenet
    outs:
    - path: Artifacts/Base_Model
      hash: md5
      md5: bc30f61379a1a1ef62f4989b315c189c.dir
      size: 118054560
      nfiles: 2
  Model_Training:
    cmd: python Respire/Pipeline/Model_Trainer.py
    deps:
    - path: Artifacts/Base_Model
      hash: md5
      md5: bc30f61379a1a1ef62f4989b315c189c.dir
      size: 118054560
      nfiles: 2
    - path: Artifacts/Data_Ingestion/Chest-CT-Scan-data
      hash: md5
      md5: 904fa45d934ce879b3b1933dca6cb2f1.dir
      size: 49247431
      nfiles: 343
    - path: Respire/Pipeline/Model_Trainer.py
      hash: md5
      md5: 003a73720aeeebec6d2034ff8374c07b
      size: 563
    - path: config/config.yaml
      hash: md5
      md5: 0b75ac98a8aea3e04f42f671359b236c
      size: 560
    params:
      params.yaml:
        AUGMENTATION: true
        BATCH_SIZE: 16
        EPOCHS: 2
        IMAGE_SIZE:
        - 224
        - 224
        - 3
    outs:
    - path: Artifacts/Model_Training/Trained_Model.h5
      hash: md5
      md5: 6b2b79135ff1d9a4bb30735e0c807888
      size: 59337520
  Model_Evaluation:
    cmd: python Respire/Pipeline/Model_Evaluation.py
    deps:
    - path: Artifacts/Data_Ingestion/Chest-CT-Scan-data
      hash: md5
      md5: 904fa45d934ce879b3b1933dca6cb2f1.dir
      size: 49247431
      nfiles: 343
    - path: Artifacts/Model_Training/Trained_model.h5
      hash: md5
      md5: 6b2b79135ff1d9a4bb30735e0c807888
      size: 59337520
    - path: Respire/Pipeline/Model_Evaluation.py
      hash: md5
      md5: addf806b28a72b94a8c8e2d7e471ca9b
      size: 557
    - path: config/config.yaml
      hash: md5
      md5: 0b75ac98a8aea3e04f42f671359b236c
      size: 560
    params:
      params.yaml:
        BATCH_SIZE: 16
        IMAGE_SIZE:
        - 224
        - 224
        - 3
    outs:
    - path: scores.json
      hash: md5
      md5: 62f2cefffb99b4b5cfc4c33d6d12e776
      size: 58
```

## File: `dvc.yaml`
```yaml
stages:

  Data_Ingestion:
    cmd: python Respire\Pipeline\Training_Pipeline\Data_Ingestion.py
    deps:
      - Respire\Pipeline\Training_Pipeline\Data_Ingestion.py
      - Respire\Components\Data_Ingestion.py
      - Config\config.yaml
    outs:
      - Artifacts\Data_Ingestion\Chest-CT-Scan-data
    
  Base_Model:
    cmd: python Respire\Pipeline\Training_Pipeline\Base_Model.py
    deps:
      - Respire\Pipeline\Training_Pipeline\Base_Model.py
      - Respire\Components\Base_Model.py
      - Config\config.yaml
    params:
      - IMAGE_SIZE
      - INCLUDE_TOP
      - CLASSES
      - WEIGHTS
      - LEARNING_RATE
    outs:
      - Artifacts\Base_Model

  
  Model_Training:
    cmd: python Respire\Pipeline\Training_Pipeline\Model_Trainer.py
    deps:
      - Respire\Pipeline\Training_Pipeline\Model_Trainer.py
      - config\config.yaml
      - Artifacts\Data_Ingestion\Chest-CT-Scan-data
      - Artifacts\Base_Model
    params:
      - IMAGE_SIZE
      - EPOCHS
      - BATCH_SIZE
      - AUGMENTATION
    outs:
      - Artifacts\Model_Training\Trained_Model.h5


  Model_Evaluation:
    cmd: python Respire\Pipeline\Training_Pipeline\Model_Evaluation.py
    deps:
      - Respire\Pipeline\Training_Pipeline\Model_Evaluation.py
      - config\config.yaml
      - Artifacts\Data_Ingestion\Chest-CT-Scan-data
      - Artifacts\Model_Training\Trained_model.h5
    params:
      - IMAGE_SIZE
      - BATCH_SIZE
    metrics:
    - scores.json:
        cache: false
```

## File: `main.py`
```python
from Respire.Logger import logging
from Respire.Pipeline.Training_Pipeline.Data_Ingestion import DataIngestionTrainingPipeline
from Respire.Pipeline.Training_Pipeline.Base_Model import PrepareBaseModelTrainingPipeline
from Respire.Pipeline.Training_Pipeline.Model_Trainer import ModelTrainingPipeline
from Respire.Pipeline.Training_Pipeline.Model_Evaluation import EvaluationPipeline


try:
    logging.info("<----------------- Data Ingestion Initiated ----------------->")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info("<----------------- Data Ingestion completed ----------------->")

    
    logging.info("<----------------- Base Model Preparation Initiated ----------------->")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info("<----------------- Base Model Preparation completed ----------------->")

    
    logging.info("<----------------- Model Training Initiated ----------------->")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logging.info("<----------------- Model Training completed ----------------->")

 
    logging.info("<----------------- Model Evaluation Initiated ----------------->")
    model_evalution = EvaluationPipeline()
    model_evalution.main()
    logging.info("<----------------- Model Evaluation completed ----------------->")

except Exception as e:
    logging.exception(e)
    raise e
```

## File: `params.yaml`
```yaml
AUGMENTATION: True
IMAGE_SIZE: [224, 224, 3] # as per VGG 16 model
BATCH_SIZE: 16
INCLUDE_TOP: False
EPOCHS: 2
CLASSES: 2
WEIGHTS: imagenet
LEARNING_RATE: 0.01
```

## File: `README.md`
```markdown
# End-to-End-Chest-Disease-Classification
By [<b>Hema Kalyan Murapaka</b>](https://kalyanm45.github.io)

Connect with me on social media and explore my work:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/hemakalyan)&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/KalyanM45)&nbsp;
[![Medium](https://img.shields.io/badge/Medium-Follow-03a57a?style=flat-square&logo=medium)](https://medium.com/@kalyan45)&nbsp;
![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/mhemakalyan)
[![Sponsor Hema Kalyan Murapaka](https://img.shields.io/badge/Sponsor-Hema_Kalyan-28a745?style=flat-square&logo=github-sponsors)](https://github.com/sponsors/KalyanMurapaka45)

**Special Thanks to GitHub Sponsors**

## About The Project

Medical imaging has transformed healthcare by providing detailed insights into various diseases, particularly in the chest area. However, the current reliance on manual interpretation of imaging data by radiologists leads to delays, errors, and inefficiencies in diagnosing chest diseases. With a growing demand for healthcare services and a shortage of radiologists in some areas, there's an urgent need for automated systems to accurately detect and classify chest diseases from imaging data. These systems would not only improve diagnostic accuracy and efficiency but also alleviate strain on healthcare resources, enhancing patient care and outcomes.

## Library Requirements

 - Tensorflow==2.12.0
 - Pandas
 - GDown
 - DVC
 - MLFlow==2.2.2
 - Flask

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/KalyanM45/End-to-End-Chest-Disease-Classification.git
     ```

2. **Create a Virtual Environment** (Optional but recommended)
   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)
   - Activate the virtual environment based on your operating system:
       ```
       conda activate <Environment_Name>/
       ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**
   - Start the project by running the appropriate command.
     ```
     python app.py
     ```

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.


### Option 2: Installation from DockerHub

If you prefer to use Docker, you can install and run the project using a Docker container from DockerHub:

1. **Pull the Docker Image**
   - Open your terminal or command prompt.
   - Run the following command to pull the Docker image from DockerHub:
     ```
     docker pull kalyan45/Chest-detection-app
     ```
     This command downloads the Docker image from the DockerHub.

2. **Run the Docker Container**
   - Start the Docker container by running the following command. Adjust the port mapping as needed:
     ```
     docker run -p 5000:5000 kalyan45/Chest-detection-app
     ```
     This command launches the project within a Docker container.

3. **Access the Project**
   - Open a web browser or the appropriate client to access the project.<br>


## API Key Setup

To use this project, you need an API key from Google Gemini Large Language Model. Follow these steps to obtain and set up your API key:

1. **Get API Key:**
   - Visit the Provided Link [Click Here](https://aws.amazon.com/console).
   - Follow the instructions to create an account and obtain your API key.

2. **Set Up API Key:**
   - Create a file named `.env` in the project root.
   - Add your API key to the `.env` file:
     ```dotenv
     API_KEY=your_api_key_here
     ```

   **Note:** Keep your API key confidential. Do not share it publicly or expose it in your code.<br>


## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

• **Report bugs**: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.

• **Contribute code**: If you are a developer and want to contribute, follow the instructions below to get started!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

• **Suggestions**: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or improvements you would like to see!

#### Don't forget to give the project a star! Thanks again!

## License

This project is licensed under the [Open Source Initiative (OSI)](https://opensource.org/) approved GNU General Public License v3.0 License - see the [LICENSE.txt](LICENSE.txt) file for details.<br>


## Contact Details

Hema Kalyan Murapaka - [kalyanmurapaka274@gmail.com](kalyanmurapaka274@gmail.com)<br>


## Acknowledgements

We'd like to extend our gratitude to all individuals and organizations who have played a role in the development and success of this project. Your support, whether through contributions, inspiration, or encouragement, has been invaluable. Thank you for being a part of our journey.
```

## File: `requirements.txt`
```
tensorflow==2.12.0
pandas 
gdown
dvc
mlflow==2.2.2
notebook
numpy
matplotlib
seaborn
python-box==6.0.2
pyYAML
tqdm
ensure==1.0.2
joblib
types-PyYAML
scipy
Flask
Flask-Cors
dagshub
-e .
```

## File: `scores.json`
```json
{
    "loss": 49.472511291503906,
    "accuracy": 0.0
}
```

## File: `setup.py`
```python
from setuptools import setup, find_packages

setup(
    name="ChestDiseaseClassifier",
    version="0.0.1",
    author="KalyanM45",
    author_email="kalyanmurapaka274@gmail.com",
    url=f"https://github.com/KalyanM45/End-to-End-Chest-Disease-Classification",
    packages=find_packages(),   
)
```

## File: `template.py`
```python
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    f"src/__init__.py",
    f"src/Components/__init__.py",
    f"src/Utils/__init__.py",
    f"src/Config/__init__.py",
    f"src/Config/configuration.py",
    f"src/Pipeline/__init__.py",
    f"src/Entity/__init__.py",
    f"src/Constants/__init__.py",
    "Config/config.yaml",
    ".gitignore",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "Notebook_Experiments/Model_Training.ipynb",
    "templates/index.html",
    "app.py"
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
```

## File: `Artifacts/Base_Model/.gitignore`
```
Base_Model.h5
Updated_Model.h5
```

## File: `Artifacts/Data_Ingestion/.gitignore`
```
/Chest-CT-Scan-data
Data.zip
```

## File: `Artifacts/Model_Training/.gitignore`
```
/Trained_Model.h5
```

## File: `Config/config.yaml`
```yaml
Artifacts_Root: Artifacts

Data_Ingestion:
  Root_Dir: Artifacts/Data_Ingestion
  Source_URL: https://drive.google.com/file/d/1qBIDYFx0aLa9MUqBEv0F3oyHIfFopt0j/view?usp=sharing
  Local_Data_File: Artifacts/Data_Ingestion/Data.zip
  Unzip_Dir: Artifacts/Data_Ingestion

Base_Model:
  Root_Dir: Artifacts/Base_Model
  Base_Model_Path: Artifacts/Base_Model/Base_Model.h5
  Updated_Model_Path: Artifacts/Base_Model/Updated_Model.h5

Model_Training:
  Root_Dir: Artifacts/Model_Training
  Trained_Model_Path: Artifacts/Model_Training/Trained_Model.h5
```

## File: `docs/ec2_setup.sh`
```bash
#!bin/bash

sudo apt update 

sudo apt-get update 

sudo apt upgrade -y

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker $USER

newgrp docker

sudo apt install awscli -y



## AWS configuration

aws configure


## Now setup elastic IP on AWS
```

## File: `docs/jenkins.sh`
```bash
#!bin/bash

sudo apt update 

sudo apt install openjdk-8-jdk -y

https://pkg.jenkins.io/
https://pkg.jenkins.io/debian-stable/

sudo systemctl start jenkins

sudo systemctl enable jenkins

sudo systemctl status jenkins



## Installing Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker $USER

sudo usermod -aG docker jenkins


newgrp docker

sudo apt install awscli -y

sudo usermod -a -G docker jenkins


## AWS configuration & restarts jenkins

aws configure


## Now setup elastic IP on AWS



## For getting the admin password for jenkins

sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

## File: `docs/README.md`
```markdown
git add .* ```config.yaml```: Paths to the Artifacts in each phase

* ```params.yaml```: Configuration of Hyperparamters for the Deep Learning Model (VGG-16)

* ```Entity Directory```: Datatypes and Schema for the Data used in the pipeline.

* ```Configuration.py```: Configuration of the pipeline

* ```requirements.txt```: Required Libraries for pipeline execution


## Workflows Order

1. Update ```config.yaml```
2. Update ```params.yaml```
3. Update the ```Entity Directory```
4. Update the ```Configuration manager``` in src config
5. Update the ```Components```
6. Update the ```Training anf Prediction Pipeline```
7. Update the ```main.py```
8. Update the ```dvc.yaml```
```

## File: `Notebook_Experiments/Model_Training.ipynb`
```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
```

## File: `Respire/Components/Base_Model.py`
```python
import os
import tensorflow as tf
from pathlib import Path
from Respire.Entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

        self.save_model(path=self.config.Base_Model_Path, model=self.model)


    
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.Updated_Model_Path, model=self.full_model)
    


    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
```

## File: `Respire/Components/Data_Ingestion.py`
```python
import os
import gdown
import zipfile
from Respire.Utils import *
from Respire.Logger import logging
from Respire.Exception import CustomException
from Respire.Entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self)-> str:
        try: 
            dataset_url, zip_download_dir = self.config.Source_URL, self.config.Local_Data_File
            os.makedirs("Artifacts/Data_Ingestion", exist_ok=True)
            logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)

            logging.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise CustomException(e)
        
    
    def extract_zip_file(self):
        try:
            unzip_path = self.config.Unzip_Dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.Local_Data_File, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logging.info(f"Extracted data from {self.config.Local_Data_File} into {unzip_path}")

        except Exception as e:
            raise CustomException(e)
```

## File: `Respire/Components/Model_Evaluation.py`
```python
import mlflow
import dagshub
import mlflow.keras
import tensorflow as tf
from pathlib import Path
from urllib.parse import urlparse
from Respire.Entity import EvaluationConfig
from Respire.Utils import read_yaml, create_directories,save_json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.Training_Data,
            subset="validation",
            shuffle=True,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.Path_of_Model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    
    def log_into_mlflow(self):
        dagshub.init(repo_owner='HemaKalyan45', repo_name='End-to-End-Chest-Disease-Classification', mlflow=True)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            )

            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model, "model")
```

## File: `Respire/Components/Model_Trainer.py`
```python
import tensorflow as tf
from pathlib import Path
from Respire.Entity import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.Updated_Model_Path)

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.Training_Data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.Training_Data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)



    
    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(
            path=self.config.Trained_Model_Path,
            model=self.model
        )
```

## File: `Respire/Config/configuration.py`
```python
import os
from Respire.Utils import *
from Respire.Constants import *
from Respire.Entity import DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig, EvaluationConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.Artifacts_Root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.Data_Ingestion

        create_directories([config.Root_Dir])

        data_ingestion_config = DataIngestionConfig(
            Root_Dir=config.Root_Dir,
            Source_URL=config.Source_URL,
            Local_Data_File=config.Local_Data_File,
            Unzip_Dir=config.Unzip_Dir 
        )

        return data_ingestion_config
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.Base_Model
        
        create_directories([config.Root_Dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            Root_Dir = Path(config.Root_Dir),
            Base_Model_Path = Path(config.Base_Model_Path),
            Updated_Model_Path = Path(config.Updated_Model_Path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )

        return prepare_base_model_config


    def get_training_config(self) -> TrainingConfig:
        training = self.config.Model_Training
        prepare_base_model = self.config.Base_Model
        params = self.params
        training_data = os.path.join(self.config.Data_Ingestion.Unzip_Dir, "Chest-CT-Scan-data")
        create_directories([
            Path(training.Root_Dir)
        ])

        training_config = TrainingConfig(
            Root_Dir = Path(training.Root_Dir),
            Trained_Model_Path = Path(training.Trained_Model_Path),
            Updated_Model_Path = Path(prepare_base_model.Updated_Model_Path),
            Training_Data = Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            Path_of_Model = Path(self.config.Model_Training.Trained_Model_Path),
            Training_Data = Path(self.config.Data_Ingestion.Unzip_Dir),
            mlflow_uri="https://dagshub.com/HemaKalyan45/End-to-End-Chest-Disease-Classification.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config
```

## File: `Respire/Constants/__init__.py`
```python
from pathlib import Path

CONFIG_FILE_PATH = Path("Config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
```

## File: `Respire/Entity/__init__.py`
```python
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    Root_Dir: Path
    Source_URL: str
    Local_Data_File: Path
    Unzip_Dir: Path



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    Root_Dir: Path
    Base_Model_Path: Path
    Updated_Model_Path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int



@dataclass(frozen=True)
class TrainingConfig:
    Root_Dir: Path
    Trained_Model_Path: Path
    Updated_Model_Path: Path
    Training_Data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list



@dataclass(frozen=True)
class EvaluationConfig:
    Path_of_Model: Path
    Training_Data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int
```

## File: `Respire/Exception/__init__.py`
```python
import os
import sys
from Respire.Logger import logging

def error_message_detail(error, error_detail:sys):
    # Retreiving TraceBack information
    # exc_info() returns a tuple - (Exception type, Exception value, traceback)
    _, _, exc_tb = error_detail.exc_info()
    # Extracting file name, line number and error message
    file_name = exc_tb.tb_frame.f_code.co_filename
    ermsg = f"Error in Script: {file_name} - Line: {exc_tb.tb_lineno} - Message: {str(error)}" 
    logging.info(ermsg)
    return ermsg

class CustomException(Exception):
    def __init__(self, ermsg, error_detail):
        super().__init__(ermsg)
        self.error_message = error_message_detail(
            ermsg, error_detail=error_detail)

    def __str__(self):
        return self.error_message
```

## File: `Respire/Logger/__init__.py`
```python
import os
import logging
from datetime import datetime

log_dir = 'Logs'
date_subdir = datetime.now().strftime('%d_%m_%Y')
LOG_FILE = datetime.now().strftime('%H_%M_%S - %d_%m_%Y.log')
logs_path = os.path.join(os.getcwd(), log_dir, date_subdir, LOG_FILE)

os.makedirs(os.path.join(os.getcwd(), log_dir, date_subdir), exist_ok=True)

logging.basicConfig(
    filename = logs_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level = logging.DEBUG
    )
```

## File: `Respire/Pipeline/Prediction_Pipeline.py`
```python
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename
    
    def predict(self):
        ## load model
        
        model = load_model(os.path.join("Artifacts","Model_Training", "Trained_Model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Normal'
            return [{ "image" : prediction}]
        else:
            prediction = 'Adenocarcinoma Cancer'
            return [{ "image" : prediction}]
```

## File: `Respire/Pipeline/Training_Pipeline/Base_Model.py`
```python
from Respire.Config.configuration import ConfigurationManager
from Respire.Components.Base_Model import PrepareBaseModel


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model() 

if __name__ == "__main__":
    pipeline = PrepareBaseModelTrainingPipeline()
    pipeline.main()
```

## File: `Respire/Pipeline/Training_Pipeline/Data_Ingestion.py`
```python
from Respire.Config.configuration import ConfigurationManager
from Respire.Components.Data_Ingestion import DataIngestion

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()      

if __name__ == "__main__":
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
```

## File: `Respire/Pipeline/Training_Pipeline/Model_Evaluation.py`
```python
from Respire.Config.configuration import ConfigurationManager
from Respire.Components.Model_Evaluation import Evaluation

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()            

if __name__ == "__main__":
    pipeline = EvaluationPipeline()
    pipeline.main()
```

## File: `Respire/Pipeline/Training_Pipeline/Model_Trainer.py`
```python
from Respire.Config.configuration import ConfigurationManager
from Respire.Components.Model_Trainer import Training

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()         

if __name__ == "__main__":
    pipeline = ModelTrainingPipeline()
    pipeline.main()
```

## File: `Respire/Utils/__init__.py`
```python
import os
import yaml
import json
import joblib
import base64
from typing import Any
from pathlib import Path
from box import ConfigBox
from Respire.Logger import logging
from ensure import ensure_annotations
from Respire.Exception import CustomException



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"Yaml file: {path_to_yaml} loaded")
            return ConfigBox(content)

    except Exception as e:
        raise CustomException(e)
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"Directory created at: {path}")
    
    except Exception as e:
        raise CustomException(e)


@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        logging.info(f"json file saved at: {path}")
    
    except Exception as e:
        raise CustomException(e)


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path) as f:
            content = json.load(f)

        logging.info(f"json file loaded succesfully from: {path}")
        return ConfigBox(content)
    
    except Exception as e:
        raise CustomException(e)


@ensure_annotations
def save_bin(data: Any, path: Path):
    try:
        joblib.dump(value=data, filename=path)
        logging.info(f"binary file saved at: {path}")
    
    except Exception as e:
        raise CustomException(e)


@ensure_annotations
def load_bin(path: Path) -> Any:
    try:
        data = joblib.load(path)
        logging.info(f"binary file loaded from: {path}")
        return data
    except Exception as e:
        raise CustomException(e)
    

@ensure_annotations
def get_size(path: Path) -> str:
    try:

        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
    
    except Exception as e:
        raise CustomException(e)


def decodeImage(imgstring, fileName):
    try:
        imgdata = base64.b64decode(imgstring)
        with open(fileName, 'wb') as f:
            f.write(imgdata)
            f.close()

    except Exception as e:
        raise CustomException(e)


def encodeImageIntoBase64(croppedImagePath):
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())
    except Exception as e:
        raise CustomException(e)
```

## File: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Chest Disease Classification</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<style>
		body{background-color: #eff2f9;}
		.iupload h3{color: #1b2d6b;font-size: 30px;font-weight: 700;}
		.img-part{height:300px;width:300px;margin:0px auto;}
		.image-part{height:300px;width:300px;border:1px solid #1b2d6b;}
		.image-part img{position:absolute;height: 300px;width:300px;display:none;padding:5px;}
		.image-part #video{display:block;height: 300px;width:300px;padding:5px;}
		.res-part{border:1px solid #dedede;margin-left:20px;height: 310px;width:100%;padding:5px;margin:0px auto;overflow:auto;}
		.res-part2{border:1px solid #dedede;height: 310px;width:100%;padding:5px;margin:0px auto;}
		.resp-img{height: 298px;width: 233px;margin:0px auto;}
		.jsonRes{margin-left:30px;}
		#send{cursor:pointer;}
		.btn-part{width:325px;}
		textarea,
		select,
		.form-control,
		.custom-select,
		button.btn,
		.btn-primary,
		input[type="text"],
		input[type="url"],
		.uneditable-input{
			border: 1px solid #363e75;
			outline: 0 !important;
			border-radius:0px;
			box-shadow: none;
		   -webkit-box-shadow: none;
		   -moz-box-shadow: none;
		   -moz-transition: none;
		   -webkit-transition: none;
		}
		textarea:focus,
		select:focus,
		.form-control:focus,
		.btn:focus,
		.btn-primary:focus,
		.custom-select:focus,
		input[type="text"]:focus,
		.uneditable-input:focus{
			border: 1px solid #007bff;
			outline: 0 !important;
			border-radius:0px;
			box-shadow: none;
		   -webkit-box-shadow: none;
		   -moz-box-shadow: none;
		   -moz-transition: none;
		   -webkit-transition: none;
		}
		#loading {
			position: fixed;
			left: 0px;
			top: 0px;
			width: 100%;
			height: 100%;
			z-index: 9999999999;
			overflow: hidden;
			background: rgba(255, 255, 255, 0.7);
		}
		.loader {
			border: 8px solid #f3f3f3;
			border-top: 8px solid #363e75;
			border-radius: 50%;
			width: 60px;
			height: 60px;
			left: 50%;
			margin-left: -4em;
			display: block;
			animation: spin 2s linear infinite;
		}
		.loader,
		.loader:after {display: block;position: absolute;top: 50%;margin-top: -4.05em;}
		@keyframes spin {
			0% {
				transform: rotate(0deg);
			}
			100% {
				transform: rotate(360deg);
			}
		}
		.right-part{border:1px solid #dedede;padding:5px;}
		.logo{position:absolute;right:0px;bottom:0px;margin-right:30px;margin-bottom:30px;}
	</style>
</head>
<body>
    <div class="main container">
		<section class="iupload">
			<h3 class="text-center py-4">End to End Chest Disease Classification</h3>
			<div class="row">
				<div class="img-part col-md-6">
					<div class="image-part">
						<video autoplay id="video" poster="https://img.freepik.com/free-vector/group-young-people-posing-photo_52683-18824.jpg?size=338&ext=jpg"></video>
						<img src="" id="photo">
						<canvas style="display:none;" id="canvas"></canvas>
					</div>
					<div class="btn-part">
						<form id="upload-data pt-3" class="">
							<div class="input-group mt-3 row">
								<button type="button" class="btn btn-primary col-md-5 col-xs-5 ml-3 mr-4" id="uload">Upload</button>
								<button id="send" type="button" class="btn btn-success col-md-5 col-xs-5">Predict</button>
							</div>






							<!-- change url value  -->




							<input type="hidden" class="form-control mr-2" id="url" placeholder="Enter REST Api url..." value="../predict"/>
							<input name="upload" type="file" id="fileinput" style="position:absolute;top:-500px;"/><br/>
						</form>
					</div>
				</div>
				<div class="col-md-6 col-xs-12 right-part">
					<h5 class="mb-2"><center>Prediction Results</center></h5>
					<div class="row">
						<div class="res-part2 col-md-5 col-xs-12"></div>
						<div class="res-part col-md-5 col-xs-12"><div class="jsonRes"></div></div>
					</div>
				</div>
			</div>
		</section>
	</div>


<div id="loading"><div class="loader"></div></div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<script>
var mybtn = document.getElementById('startbtn');
var myvideo = document.getElementById('video');
var mycanvas = document.getElementById('canvas');
var myphoto = document.getElementById('photo');
var base_data = "";

function sendRequest(base64Data){
	var type = "json";
	if(base64Data != "" || base64Data != null){
		if(type == "imgtobase"){
			$(".res-part").html("");
			$(".res-part").html(base64Data);
		}
		else if(type == "basetoimg"){
			var imageData = $("#imgstring").val();
			$(".res-part").html("");
			$(".res-part").append("<img src='data:image/jpeg;base64," + imageData + "' alt='' />");
		}
		else{
			var url = $("#url").val();
			$("#loading").show();
			$.ajax({
				url : url,
				type: "post",
				cache: false,
				async: true,
				crossDomain: true,
				headers: {
					'Content-Type': 'application/json',
					'Access-Control-Allow-Origin':'*'
				},
				data:JSON.stringify({image:base64Data}),
				success: function(res){
					$(".res-part").html("");
					$(".res-part2").html("");
					try{
						var imageData = res[1].image;
						if(imageData.length > 100){
							if(imageData.length > 10){$(".res-part2").append("<img class='resp-img' src='data:image/jpeg;base64," + imageData + "' alt='' />");}
						}
					}catch(e){}
					$(".res-part").html("<pre>" + JSON.stringify(res[0], undefined, 2) + "</pre>");
					$("#loading").hide();
				}
			});
		}
	}
}

$(document).ready(function(){
	$("#loading").hide();

	$('#send').click(function(evt){
		sendRequest(base_data);
    });

    $('#uload').click(function(evt) {
        $('#fileinput').focus().trigger('click');
    });
	$("#fileinput").change(function(){
		if (this.files && this.files[0]){
			var reader = new FileReader();
			reader.onload = function (e){
				var url = e.target.result;
				var img = new Image();
				img.crossOrigin = 'Anonymous';
				img.onload = function(){
					var canvas = document.createElement('CANVAS');
					var ctx = canvas.getContext('2d');
					canvas.height = this.height;
					canvas.width = this.width;
					ctx.drawImage(this, 0, 0);
					base_data = canvas.toDataURL('image/jpeg', 1.0).replace(/^data:image.+;base64,/, '');
					canvas = null;
				};
				img.src = url;
				$('#photo').attr('src', url);
				$('#photo').show();
				$('#video').hide();
			}
			reader.readAsDataURL(this.files[0]);
		}
	});
});

</script>
</body>
</html>
```

