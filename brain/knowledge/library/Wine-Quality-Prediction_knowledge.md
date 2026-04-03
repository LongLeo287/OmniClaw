---
id: wine-quality-prediction-knowledge
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.338669
---

# KNOWLEDGE EXTRACT: Wine-Quality-Prediction
> **Extracted on:** 2026-03-29 20:56:38
> **Source:** Wine-Quality-Prediction

---

## File: `.gitignore`
```
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
winevenv

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
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load your pre-trained regression model
        model = pickle.load(open("model.pkl", "rb"))

        # Get input values from the form
        fixed_acidity = float(request.form['fixed_acidity'])
        volatile_acidity = float(request.form['volatile_acidity'])
        citric_acid = float(request.form['citric_acid'])
        residual_sugar = float(request.form['residual_sugar'])
        chlorides = float(request.form['chlorides'])
        freesulfurdioxide = int(request.form['freesulfurdioxide'])
        totalsulfurdioxide = int(request.form['totalsulfurdioxide'])
        density = float(request.form['density'])
        ph = float(request.form['ph'])
        sulphates = float(request.form['sulphates'])
        alcohol = float(request.form['alcohol'])

        # Perform prediction
        features = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, freesulfurdioxide, totalsulfurdioxide, density, ph, sulphates, alcohol]).reshape(1, -1)
        prediction = model.predict(features)

        # Return the prediction as a response
        if prediction[0] == 1:
            result = 'Good Quality Wine'
        else:
            result = 'Bad Quality Wine'

        return render_template('index.html', result=result)

    except Exception as e:
        error_message = f"Prediction failed. Error: {str(e)}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
```

## File: `Dockerfile`
```
# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /winequality

# Copy the current directory contents into the container at /app
COPY . /winequality

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt  

# Run streamlit when the container launches
CMD python app.py 
```

## File: `README.md`
```markdown
# Wine-Quality-Prediction
```

## File: `requirements.txt`
```
streamlit
numpy
matplotlib
scikit-learn
seaborn
flask
```

## File: `Wine_Quality_Prediction_Notebook.ipynb`
```
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uBHsHWmumNKn"
      },
      "source": [
        "Importing the Dependencies"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "6mXdf5RGkzlk"
      },
      "outputs": [],
      "source": [
        "import warnings\n",
        "warnings.simplefilter('ignore')\n",
        "\n",
        "import numpy as np  \n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bURpf8bkm7-M"
      },
      "source": [
        "Data Collection"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "cWKcl9eNm6F_"
      },
      "outputs": [],
      "source": [
        "data = pd.read_csv('./Raw_Data/winequality-red.csv')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fixed acidity</th>\n",
              "      <th>volatile acidity</th>\n",
              "      <th>citric acid</th>\n",
              "      <th>residual sugar</th>\n",
              "      <th>chlorides</th>\n",
              "      <th>free sulfur dioxide</th>\n",
              "      <th>total sulfur dioxide</th>\n",
              "      <th>density</th>\n",
              "      <th>pH</th>\n",
              "      <th>sulphates</th>\n",
              "      <th>alcohol</th>\n",
              "      <th>quality</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>7.4</td>\n",
              "      <td>0.700</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.076</td>\n",
              "      <td>11.0</td>\n",
              "      <td>34.0</td>\n",
              "      <td>0.99780</td>\n",
              "      <td>3.51</td>\n",
              "      <td>0.56</td>\n",
              "      <td>9.4</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>7.8</td>\n",
              "      <td>0.880</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.6</td>\n",
              "      <td>0.098</td>\n",
              "      <td>25.0</td>\n",
              "      <td>67.0</td>\n",
              "      <td>0.99680</td>\n",
              "      <td>3.20</td>\n",
              "      <td>0.68</td>\n",
              "      <td>9.8</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>7.8</td>\n",
              "      <td>0.760</td>\n",
              "      <td>0.04</td>\n",
              "      <td>2.3</td>\n",
              "      <td>0.092</td>\n",
              "      <td>15.0</td>\n",
              "      <td>54.0</td>\n",
              "      <td>0.99700</td>\n",
              "      <td>3.26</td>\n",
              "      <td>0.65</td>\n",
              "      <td>9.8</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>11.2</td>\n",
              "      <td>0.280</td>\n",
              "      <td>0.56</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.075</td>\n",
              "      <td>17.0</td>\n",
              "      <td>60.0</td>\n",
              "      <td>0.99800</td>\n",
              "      <td>3.16</td>\n",
              "      <td>0.58</td>\n",
              "      <td>9.8</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>7.4</td>\n",
              "      <td>0.700</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.076</td>\n",
              "      <td>11.0</td>\n",
              "      <td>34.0</td>\n",
              "      <td>0.99780</td>\n",
              "      <td>3.51</td>\n",
              "      <td>0.56</td>\n",
              "      <td>9.4</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1594</th>\n",
              "      <td>6.2</td>\n",
              "      <td>0.600</td>\n",
              "      <td>0.08</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.090</td>\n",
              "      <td>32.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>0.99490</td>\n",
              "      <td>3.45</td>\n",
              "      <td>0.58</td>\n",
              "      <td>10.5</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1595</th>\n",
              "      <td>5.9</td>\n",
              "      <td>0.550</td>\n",
              "      <td>0.10</td>\n",
              "      <td>2.2</td>\n",
              "      <td>0.062</td>\n",
              "      <td>39.0</td>\n",
              "      <td>51.0</td>\n",
              "      <td>0.99512</td>\n",
              "      <td>3.52</td>\n",
              "      <td>0.76</td>\n",
              "      <td>11.2</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1596</th>\n",
              "      <td>6.3</td>\n",
              "      <td>0.510</td>\n",
              "      <td>0.13</td>\n",
              "      <td>2.3</td>\n",
              "      <td>0.076</td>\n",
              "      <td>29.0</td>\n",
              "      <td>40.0</td>\n",
              "      <td>0.99574</td>\n",
              "      <td>3.42</td>\n",
              "      <td>0.75</td>\n",
              "      <td>11.0</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1597</th>\n",
              "      <td>5.9</td>\n",
              "      <td>0.645</td>\n",
              "      <td>0.12</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.075</td>\n",
              "      <td>32.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>0.99547</td>\n",
              "      <td>3.57</td>\n",
              "      <td>0.71</td>\n",
              "      <td>10.2</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1598</th>\n",
              "      <td>6.0</td>\n",
              "      <td>0.310</td>\n",
              "      <td>0.47</td>\n",
              "      <td>3.6</td>\n",
              "      <td>0.067</td>\n",
              "      <td>18.0</td>\n",
              "      <td>42.0</td>\n",
              "      <td>0.99549</td>\n",
              "      <td>3.39</td>\n",
              "      <td>0.66</td>\n",
              "      <td>11.0</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1599 rows × 12 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  \\\n",
              "0               7.4             0.700         0.00             1.9      0.076   \n",
              "1               7.8             0.880         0.00             2.6      0.098   \n",
              "2               7.8             0.760         0.04             2.3      0.092   \n",
              "3              11.2             0.280         0.56             1.9      0.075   \n",
              "4               7.4             0.700         0.00             1.9      0.076   \n",
              "...             ...               ...          ...             ...        ...   \n",
              "1594            6.2             0.600         0.08             2.0      0.090   \n",
              "1595            5.9             0.550         0.10             2.2      0.062   \n",
              "1596            6.3             0.510         0.13             2.3      0.076   \n",
              "1597            5.9             0.645         0.12             2.0      0.075   \n",
              "1598            6.0             0.310         0.47             3.6      0.067   \n",
              "\n",
              "      free sulfur dioxide  total sulfur dioxide  density    pH  sulphates  \\\n",
              "0                    11.0                  34.0  0.99780  3.51       0.56   \n",
              "1                    25.0                  67.0  0.99680  3.20       0.68   \n",
              "2                    15.0                  54.0  0.99700  3.26       0.65   \n",
              "3                    17.0                  60.0  0.99800  3.16       0.58   \n",
              "4                    11.0                  34.0  0.99780  3.51       0.56   \n",
              "...                   ...                   ...      ...   ...        ...   \n",
              "1594                 32.0                  44.0  0.99490  3.45       0.58   \n",
              "1595                 39.0                  51.0  0.99512  3.52       0.76   \n",
              "1596                 29.0                  40.0  0.99574  3.42       0.75   \n",
              "1597                 32.0                  44.0  0.99547  3.57       0.71   \n",
              "1598                 18.0                  42.0  0.99549  3.39       0.66   \n",
              "\n",
              "      alcohol  quality  \n",
              "0         9.4        5  \n",
              "1         9.8        5  \n",
              "2         9.8        5  \n",
              "3         9.8        6  \n",
              "4         9.4        5  \n",
              "...       ...      ...  \n",
              "1594     10.5        5  \n",
              "1595     11.2        6  \n",
              "1596     11.0        6  \n",
              "1597     10.2        5  \n",
              "1598     11.0        6  \n",
              "\n",
              "[1599 rows x 12 columns]"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fixed acidity</th>\n",
              "      <th>volatile acidity</th>\n",
              "      <th>citric acid</th>\n",
              "      <th>residual sugar</th>\n",
              "      <th>chlorides</th>\n",
              "      <th>free sulfur dioxide</th>\n",
              "      <th>total sulfur dioxide</th>\n",
              "      <th>density</th>\n",
              "      <th>pH</th>\n",
              "      <th>sulphates</th>\n",
              "      <th>alcohol</th>\n",
              "      <th>quality</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>7.4</td>\n",
              "      <td>0.70</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.076</td>\n",
              "      <td>11.0</td>\n",
              "      <td>34.0</td>\n",
              "      <td>0.9978</td>\n",
              "      <td>3.51</td>\n",
              "      <td>0.56</td>\n",
              "      <td>9.4</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>7.8</td>\n",
              "      <td>0.88</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.6</td>\n",
              "      <td>0.098</td>\n",
              "      <td>25.0</td>\n",
              "      <td>67.0</td>\n",
              "      <td>0.9968</td>\n",
              "      <td>3.20</td>\n",
              "      <td>0.68</td>\n",
              "      <td>9.8</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>7.8</td>\n",
              "      <td>0.76</td>\n",
              "      <td>0.04</td>\n",
              "      <td>2.3</td>\n",
              "      <td>0.092</td>\n",
              "      <td>15.0</td>\n",
              "      <td>54.0</td>\n",
              "      <td>0.9970</td>\n",
              "      <td>3.26</td>\n",
              "      <td>0.65</td>\n",
              "      <td>9.8</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>11.2</td>\n",
              "      <td>0.28</td>\n",
              "      <td>0.56</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.075</td>\n",
              "      <td>17.0</td>\n",
              "      <td>60.0</td>\n",
              "      <td>0.9980</td>\n",
              "      <td>3.16</td>\n",
              "      <td>0.58</td>\n",
              "      <td>9.8</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>7.4</td>\n",
              "      <td>0.70</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.076</td>\n",
              "      <td>11.0</td>\n",
              "      <td>34.0</td>\n",
              "      <td>0.9978</td>\n",
              "      <td>3.51</td>\n",
              "      <td>0.56</td>\n",
              "      <td>9.4</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  \\\n",
              "0            7.4              0.70         0.00             1.9      0.076   \n",
              "1            7.8              0.88         0.00             2.6      0.098   \n",
              "2            7.8              0.76         0.04             2.3      0.092   \n",
              "3           11.2              0.28         0.56             1.9      0.075   \n",
              "4            7.4              0.70         0.00             1.9      0.076   \n",
              "\n",
              "   free sulfur dioxide  total sulfur dioxide  density    pH  sulphates  \\\n",
              "0                 11.0                  34.0   0.9978  3.51       0.56   \n",
              "1                 25.0                  67.0   0.9968  3.20       0.68   \n",
              "2                 15.0                  54.0   0.9970  3.26       0.65   \n",
              "3                 17.0                  60.0   0.9980  3.16       0.58   \n",
              "4                 11.0                  34.0   0.9978  3.51       0.56   \n",
              "\n",
              "   alcohol  quality  \n",
              "0      9.4        5  \n",
              "1      9.8        5  \n",
              "2      9.8        5  \n",
              "3      9.8        6  \n",
              "4      9.4        5  "
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "data.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fixed acidity</th>\n",
              "      <th>volatile acidity</th>\n",
              "      <th>citric acid</th>\n",
              "      <th>residual sugar</th>\n",
              "      <th>chlorides</th>\n",
              "      <th>free sulfur dioxide</th>\n",
              "      <th>total sulfur dioxide</th>\n",
              "      <th>density</th>\n",
              "      <th>pH</th>\n",
              "      <th>sulphates</th>\n",
              "      <th>alcohol</th>\n",
              "      <th>quality</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1594</th>\n",
              "      <td>6.2</td>\n",
              "      <td>0.600</td>\n",
              "      <td>0.08</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.090</td>\n",
              "      <td>32.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>0.99490</td>\n",
              "      <td>3.45</td>\n",
              "      <td>0.58</td>\n",
              "      <td>10.5</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1595</th>\n",
              "      <td>5.9</td>\n",
              "      <td>0.550</td>\n",
              "      <td>0.10</td>\n",
              "      <td>2.2</td>\n",
              "      <td>0.062</td>\n",
              "      <td>39.0</td>\n",
              "      <td>51.0</td>\n",
              "      <td>0.99512</td>\n",
              "      <td>3.52</td>\n",
              "      <td>0.76</td>\n",
              "      <td>11.2</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1596</th>\n",
              "      <td>6.3</td>\n",
              "      <td>0.510</td>\n",
              "      <td>0.13</td>\n",
              "      <td>2.3</td>\n",
              "      <td>0.076</td>\n",
              "      <td>29.0</td>\n",
              "      <td>40.0</td>\n",
              "      <td>0.99574</td>\n",
              "      <td>3.42</td>\n",
              "      <td>0.75</td>\n",
              "      <td>11.0</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1597</th>\n",
              "      <td>5.9</td>\n",
              "      <td>0.645</td>\n",
              "      <td>0.12</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.075</td>\n",
              "      <td>32.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>0.99547</td>\n",
              "      <td>3.57</td>\n",
              "      <td>0.71</td>\n",
              "      <td>10.2</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1598</th>\n",
              "      <td>6.0</td>\n",
              "      <td>0.310</td>\n",
              "      <td>0.47</td>\n",
              "      <td>3.6</td>\n",
              "      <td>0.067</td>\n",
              "      <td>18.0</td>\n",
              "      <td>42.0</td>\n",
              "      <td>0.99549</td>\n",
              "      <td>3.39</td>\n",
              "      <td>0.66</td>\n",
              "      <td>11.0</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  \\\n",
              "1594            6.2             0.600         0.08             2.0      0.090   \n",
              "1595            5.9             0.550         0.10             2.2      0.062   \n",
              "1596            6.3             0.510         0.13             2.3      0.076   \n",
              "1597            5.9             0.645         0.12             2.0      0.075   \n",
              "1598            6.0             0.310         0.47             3.6      0.067   \n",
              "\n",
              "      free sulfur dioxide  total sulfur dioxide  density    pH  sulphates  \\\n",
              "1594                 32.0                  44.0  0.99490  3.45       0.58   \n",
              "1595                 39.0                  51.0  0.99512  3.52       0.76   \n",
              "1596                 29.0                  40.0  0.99574  3.42       0.75   \n",
              "1597                 32.0                  44.0  0.99547  3.57       0.71   \n",
              "1598                 18.0                  42.0  0.99549  3.39       0.66   \n",
              "\n",
              "      alcohol  quality  \n",
              "1594     10.5        5  \n",
              "1595     11.2        6  \n",
              "1596     11.0        6  \n",
              "1597     10.2        5  \n",
              "1598     11.0        6  "
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "data.tail()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g_My291znM6F",
        "outputId": "4aeed5bd-32b6-4f55-f221-4b58075290a6"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(1599, 12)"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "data.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sm4Tve1gncni",
        "outputId": "6ce110f2-2f70-4904-8d2e-2f3a327176fe"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "fixed acidity           0\n",
              "volatile acidity        0\n",
              "citric acid             0\n",
              "residual sugar          0\n",
              "chlorides               0\n",
              "free sulfur dioxide     0\n",
              "total sulfur dioxide    0\n",
              "density                 0\n",
              "pH                      0\n",
              "sulphates               0\n",
              "alcohol                 0\n",
              "quality                 0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 9,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "data.isnull().sum()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7-MFdFXsoAto"
      },
      "source": [
        "Data Analysis and Visulaization"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 343
        },
        "id": "Y7o-Nl_EnyIE",
        "outputId": "4e4a0e7a-d1f6-406f-dfc2-e346c3b52b04"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fixed acidity</th>\n",
              "      <th>volatile acidity</th>\n",
              "      <th>citric acid</th>\n",
              "      <th>residual sugar</th>\n",
              "      <th>chlorides</th>\n",
              "      <th>free sulfur dioxide</th>\n",
              "      <th>total sulfur dioxide</th>\n",
              "      <th>density</th>\n",
              "      <th>pH</th>\n",
              "      <th>sulphates</th>\n",
              "      <th>alcohol</th>\n",
              "      <th>quality</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "      <td>1599.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>8.319637</td>\n",
              "      <td>0.527821</td>\n",
              "      <td>0.270976</td>\n",
              "      <td>2.538806</td>\n",
              "      <td>0.087467</td>\n",
              "      <td>15.874922</td>\n",
              "      <td>46.467792</td>\n",
              "      <td>0.996747</td>\n",
              "      <td>3.311113</td>\n",
              "      <td>0.658149</td>\n",
              "      <td>10.422983</td>\n",
              "      <td>5.636023</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>1.741096</td>\n",
              "      <td>0.179060</td>\n",
              "      <td>0.194801</td>\n",
              "      <td>1.409928</td>\n",
              "      <td>0.047065</td>\n",
              "      <td>10.460157</td>\n",
              "      <td>32.895324</td>\n",
              "      <td>0.001887</td>\n",
              "      <td>0.154386</td>\n",
              "      <td>0.169507</td>\n",
              "      <td>1.065668</td>\n",
              "      <td>0.807569</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>4.600000</td>\n",
              "      <td>0.120000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.900000</td>\n",
              "      <td>0.012000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>0.990070</td>\n",
              "      <td>2.740000</td>\n",
              "      <td>0.330000</td>\n",
              "      <td>8.400000</td>\n",
              "      <td>3.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>7.100000</td>\n",
              "      <td>0.390000</td>\n",
              "      <td>0.090000</td>\n",
              "      <td>1.900000</td>\n",
              "      <td>0.070000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>22.000000</td>\n",
              "      <td>0.995600</td>\n",
              "      <td>3.210000</td>\n",
              "      <td>0.550000</td>\n",
              "      <td>9.500000</td>\n",
              "      <td>5.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>7.900000</td>\n",
              "      <td>0.520000</td>\n",
              "      <td>0.260000</td>\n",
              "      <td>2.200000</td>\n",
              "      <td>0.079000</td>\n",
              "      <td>14.000000</td>\n",
              "      <td>38.000000</td>\n",
              "      <td>0.996750</td>\n",
              "      <td>3.310000</td>\n",
              "      <td>0.620000</td>\n",
              "      <td>10.200000</td>\n",
              "      <td>6.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>9.200000</td>\n",
              "      <td>0.640000</td>\n",
              "      <td>0.420000</td>\n",
              "      <td>2.600000</td>\n",
              "      <td>0.090000</td>\n",
              "      <td>21.000000</td>\n",
              "      <td>62.000000</td>\n",
              "      <td>0.997835</td>\n",
              "      <td>3.400000</td>\n",
              "      <td>0.730000</td>\n",
              "      <td>11.100000</td>\n",
              "      <td>6.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>15.900000</td>\n",
              "      <td>1.580000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>15.500000</td>\n",
              "      <td>0.611000</td>\n",
              "      <td>72.000000</td>\n",
              "      <td>289.000000</td>\n",
              "      <td>1.003690</td>\n",
              "      <td>4.010000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>14.900000</td>\n",
              "      <td>8.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       fixed acidity  volatile acidity  citric acid  residual sugar  \\\n",
              "count    1599.000000       1599.000000  1599.000000     1599.000000   \n",
              "mean        8.319637          0.527821     0.270976        2.538806   \n",
              "std         1.741096          0.179060     0.194801        1.409928   \n",
              "min         4.600000          0.120000     0.000000        0.900000   \n",
              "25%         7.100000          0.390000     0.090000        1.900000   \n",
              "50%         7.900000          0.520000     0.260000        2.200000   \n",
              "75%         9.200000          0.640000     0.420000        2.600000   \n",
              "max        15.900000          1.580000     1.000000       15.500000   \n",
              "\n",
              "         chlorides  free sulfur dioxide  total sulfur dioxide      density  \\\n",
              "count  1599.000000          1599.000000           1599.000000  1599.000000   \n",
              "mean      0.087467            15.874922             46.467792     0.996747   \n",
              "std       0.047065            10.460157             32.895324     0.001887   \n",
              "min       0.012000             1.000000              6.000000     0.990070   \n",
              "25%       0.070000             7.000000             22.000000     0.995600   \n",
              "50%       0.079000            14.000000             38.000000     0.996750   \n",
              "75%       0.090000            21.000000             62.000000     0.997835   \n",
              "max       0.611000            72.000000            289.000000     1.003690   \n",
              "\n",
              "                pH    sulphates      alcohol      quality  \n",
              "count  1599.000000  1599.000000  1599.000000  1599.000000  \n",
              "mean      3.311113     0.658149    10.422983     5.636023  \n",
              "std       0.154386     0.169507     1.065668     0.807569  \n",
              "min       2.740000     0.330000     8.400000     3.000000  \n",
              "25%       3.210000     0.550000     9.500000     5.000000  \n",
              "50%       3.310000     0.620000    10.200000     6.000000  \n",
              "75%       3.400000     0.730000    11.100000     6.000000  \n",
              "max       4.010000     2.000000    14.900000     8.000000  "
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "data.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1599 entries, 0 to 1598\n",
            "Data columns (total 12 columns):\n",
            " #   Column                Non-Null Count  Dtype  \n",
            "---  ------                --------------  -----  \n",
            " 0   fixed acidity         1599 non-null   float64\n",
            " 1   volatile acidity      1599 non-null   float64\n",
            " 2   citric acid           1599 non-null   float64\n",
            " 3   residual sugar        1599 non-null   float64\n",
            " 4   chlorides             1599 non-null   float64\n",
            " 5   free sulfur dioxide   1599 non-null   float64\n",
            " 6   total sulfur dioxide  1599 non-null   float64\n",
            " 7   density               1599 non-null   float64\n",
            " 8   pH                    1599 non-null   float64\n",
            " 9   sulphates             1599 non-null   float64\n",
            " 10  alcohol               1599 non-null   float64\n",
            " 11  quality               1599 non-null   int64  \n",
            "dtypes: float64(11), int64(1)\n",
            "memory usage: 150.0 KB\n"
          ]
        }
      ],
      "source": [
        "data.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 401
        },
        "id": "B6mep7GEoLNp",
        "outputId": "72d7351e-0d02-48d5-f8a6-2a6072b9a4b2"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.FacetGrid at 0x18b145ad490>"
            ]
          },
          "execution_count": 12,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 500x500 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "sns.catplot(x='quality', data = data, kind = 'count')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 352
        },
        "id": "COy4yhieo0v7",
        "outputId": "e59aeba2-d52c-4422-c642-82b6a4e0f80e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<Axes: xlabel='quality', ylabel='volatile acidity'>"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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f9X48eMtu0mDq/Xt21cZGRnKzs6WJH300Ud67733NHjwYIuTXRl7lC70ySefKDw8XN9//718fX21efNmderUyepYLrNhwwYdPHhQ+/btszqKJfr06aM1a9botttuU25urubMmaN+/frp008/VZMmTayO5xLHjx/X8uXLFR8fr6efflr79u3T5MmT5eXlpbFjx1odz+W2bNmib7/9VuPGjbM6istMnz5dRUVF6tixozw9PVVWVqZ58+Zp9OjRVke7MjtcpqSkxH7kyBH7/v377dOnT7c3b97c/tlnn1kdyyVycnLsLVq0sH/00UeOsf79+9vj4uKsC2Wxb775xu7n52dftWqV1VFcpmHDhvbw8PAKY3/605/s//Ef/2FRImvdd9999t/85jdWx3Cp9evX29u0aWNfv369/eOPP7a/9NJL9mbNmtnXrFljdbQroigtNHDgQPujjz5qdQyX2Lx5s12S3dPT0/GQZLfZbHZPT0/75cuXrY5oiV69etmnT59udQyXCQkJsU+YMKHC2AsvvGBv1aqVRYmsc/LkSbuHh4d9y5YtVkdxqTZt2tiff/75CmNz586133bbbRYl+mUcerVQeXm5SkpKrI7hEgMHDtQnn3xSYSwmJkYdO3bUtGnT5OnpaVEy61y4cEHHjh3Tww8/bHUUl7nzzjt1+PDhCmPZ2dlq27atRYmss3r1arVo0cJxUkt9cfHixQp3hJIkT09PlZeXW5Tol1GULpKQkKDBgwcrJCRE58+f17p167R7927t3LnT6mgu0aRJk0q3Qrvhhht000031ZtbpE2dOlVRUVFq27atvv76ayUlJcnT01MjR460OprLTJkyRX379tX8+fP1u9/9Tnv37tXKlSvr3f1ky8vLtXr1ao0dO7be/UQoKipK8+bNU0hIiDp37qxDhw4pJSVF48ePtzralVm9S1tfjB8/3t62bVu7l5eXPSAgwD5w4ED7m2++aXUsS9W37yijo6PtLVu2tHt5edlbt25tj46Oth89etTqWC736quv2rt06WL39va2d+zY0b5y5UqrI7nczp077ZLshw8ftjqKyxUVFdnj4uLsISEhdh8fH/stt9xinzFjhr2kpMTqaFfEbbYAADDgd5QAABhQlAAAGFCUAAAYUJQAABhQlAAAGFCUAAAYUJQAABhQlAA0e/ZshYWFOV6PGzdOw4cPtywP4E7q17WTAFRLamqqfn4tkgEDBigsLExLly61LhRgEYoSQCX+/v5WRwDcBodeATdXXFysMWPGyNfXVy1bttTixYs1YMAAPf7445Ikm82mLVu2VJhz4403as2aNY7X06ZN06233qrGjRvrlltu0axZs3Tp0qUrfubPD72OGzdO77zzjlJTU2Wz2WSz2XTixAm1b99ezz33XIV5WVlZstlsOnr0aE1sOuAWKErAzT355JN65513tHXrVr355pvavXu3Dh486NQ6mjRpojVr1uj//u//lJqaqrS0NC1ZsqRac1NTUxUeHq7Y2Fjl5uYqNzdXISEhGj9+vFavXl1h2dWrV+vuu+9W+/btncoHuDOKEnBjFy5c0IsvvqjnnntOAwcOVNeuXbV27VpdvnzZqfXMnDlTffv2VWhoqKKiojR16lRt2rSpWnP9/f3l5eWlxo0bKygoSEFBQfL09NS4ceN0+PBh7d27V5J06dIlrVu3zr1vlwRcBb6jBNzYsWPHVFpaqj59+jjGmjVrpttuu82p9WzcuFH/9V//pWPHjunChQu6fPmy/Pz8rilbq1atNHToUKWnp6t379569dVXVVJSohEjRlzTegF3wx4lcJ2z2Wz697vl/fz7x8zMTI0ePVpDhgzRa6+9pkOHDmnGjBkqLS295s9+5JFHtGHDBn333XdavXq1oqOj1bhx42teL+BO2KME3Fi7du3UsGFDffjhhwoJCZEkffPNN8rOzlb//v0lSQEBAcrNzXXMOXLkiC5evOh4vWfPHrVt21YzZsxwjH355ZdO5fDy8lJZWVml8SFDhuiGG27Q8uXLtWPHDv3jH/9war3A9YCiBNyYr6+vJkyYoCeffFI33XSTWrRooRkzZsjD46eDQffee6+ef/55hYeHq6ysTNOmTVPDhg0d73fo0EE5OTnasGGDfvWrX2n79u3avHmzUzlCQ0P14Ycf6uTJk/L19VWzZs3k4eHh+K4yISFBHTp0UHh4eI1tO+AuOPQKuLlnn31W/fr1U1RUlCIiInTXXXepZ8+ejvcXL16s4OBg9evXT6NGjdLUqVMrHP4cNmyYpkyZokmTJiksLEx79uzRrFmznMowdepUeXp6qlOnTgoICFBOTo7jvQkTJqi0tFQxMTHXvrGAG7LZ//3LDQBuz52ulPPuu+9q4MCBOnXqlAIDA62OA9Q4Dr0CuColJSUqKCjQ7NmzNWLECEoSdRaHXgFclfXr16tt27b69ttvtWjRIqvjALWGQ68AABiwRwkAgAFFCQCAAUUJAIABRQkAgAFFCQCAAUUJAIABRQkAgAFFCQCAAUUJAIDB/wei4KuGhoDFzgAAAABJRU5ErkJggg==",
            "text/plain": [
              "<Figure size 500x500 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "plot = plt.figure(figsize=(5,5))\n",
        "sns.barplot(x='quality', y = 'volatile acidity', data = data)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 353
        },
        "id": "C3KRFO91phMV",
        "outputId": "4a5f8751-7211-4bdd-e153-e9e8803e8cc1"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<Axes: xlabel='quality', ylabel='citric acid'>"
            ]
          },
          "execution_count": 14,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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Y2Oz17/66qsOCwcAgNW8PqJctGiRioqKlJWVpbq6OuXl5ennP/+5goKCtHDhwk6ICACAdbwuymeffVYrVqzQnXfeqW7dumnKlCl64oknVFBQoH/84x+dkREAAMt4XZQ1NTUaNmyYJCk8PFx1dXWSpJ/+9Kd6+eWXOzYdAAAW87oozz//fB04cECSNGjQIL3++uuSpC1btshut3dsOgAALOb1xTw/+9nPVFFRofT0dN1666264YYbtHLlSlVVVemOO+7ojIxAl5KbmyuHwyFJioqKUklJicWJAJh4XZSLFy/2PM7KylJ8fLw2btyoIUOGaOLEiR0aDuiKHA6HamtrrY4BoJ1O64YD33XppZfq0ksv7YgsAAJAhFuS3N95DPi3My5KAPBGtstldQTAK9yZBwAAA4oSAAADihIAAAOvi3LLli3atGlTi/FNmzZp69atHRIKAAB/4XVR3nLLLaqurm4xvn//ft1yyy0dEgoAAH/hdVF+9NFHuvjii1uMjxw5Uh999FGHhAIAwF94XZR2u73VL0sfOHBA3brxbRMAQNfidVGOGzdO+fn5npuhS9KRI0d0991366qrrurQcAAAWM3rQ8ClS5fq8ssvV3x8vEaOHClJ2rFjh6Kjo/X00093eEAAAKzkdVEOGDBAO3fu1LPPPqv3339fPXr0UHZ2tqZMmaLu3bt3RkbApy7742Wdun17vV022SRJNfU1nf5+7976bqduH+jqTutDxZ49e+qmm27q6CwAAPiddhXliy++qKuvvlrdu3fXiy++aJx77bXXdkgwAAD8QbuKctKkSaqpqVG/fv00adKkNufZbDa5uOExAKALaVdRNjU1tfoYAICuzquvh5w8eVJjx47Vnj17OisPAAB+xaui7N69u3bu3NlZWQAA8Dte33Dghhtu0MqVKzsjCwAAfsfrr4ecOnVKZWVleuONN5SSkqKePXs2e72oqKjDwgEAYDWvi/KDDz7w3BT9008/7fBA6Npyc3PlcDgkSVFRUSopKbE4EQCYeV2Ub775ZmfkQIBwOByt3lQfAPyV159RzpgxQ0ePHm0x3tDQoBkzZnRIKKArc/dwN1sA+Devi/LJJ5/UiRMnWoyfOHFCTz31VIeEArqyxssb5RzvlHO8U42XN1odB8D3aPep1/r6erndbrndbh09elShoaGe11wul1555RX169evU0IC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sGpra5uN19bWKiYmptV1YmJivJpvt9tlt9ubjfXu3fv0Q3egiIiIgPwP5BuBvv8Sf4NA33+Jv4HV+286kvyGpRfzhISEKCUlRRUVFZ6xpqYmVVRUKCMjo9V1MjIyms2XpL///e9tzgcA4ExYfuo1Ly9P06dPV2pqqtLS0lRcXKyGhgZlZ2dLkqZNm6YBAwaosLBQkpSbm6sxY8booYce0oQJE7R27Vpt3bpVjz/+uJW7AQDooiwvyqysLDkcDhUUFKimpkbJyckqLy/3XLBTVVWloKBvD3xHjRql5557Tr///e919913a8iQIVq/fr0uuugiq3bBa3a7XQsWLGhxSjhQBPr+S/wNAn3/Jf4GZ9P+29zfd10sAAABzPIbDgAA4M8oSgAADChKAAAMKEoAAAwoSh9Zvny5hg8f7vlybUZGhl599VWrY1lm8eLFstlsuv32262O4jMLFy6UzWZrtiQmJlody+f279+vG264Qeeee6569OihYcOGaevWrVbH8pmEhIQW/w5sNptuueUWq6P5hMvl0vz58/WDH/xAPXr00KBBg3Tvvfd+7/1WrWT510MCxfnnn6/FixdryJAhcrvdevLJJ3Xdddfpvffe09ChQ62O51NbtmzRY489puHDh1sdxeeGDh2qN954w/O8W7fA+k/w8OHDuuyyy/TjH/9Yr776qqKiorRnzx6dc845VkfzmS1btsjl+vbHBz744ANdddVVmjx5soWpfGfJkiVavny5nnzySQ0dOlRbt25Vdna2IiMjddttt1kdr1WB9V+phSZOnNjs+f3336/ly5frH//4R0AV5bFjxzR16lStWLFC9913n9VxfK5bt25t3m4xECxZskSxsbFatWqVZ+wHP/iBhYl8LyoqqtnzxYsXa9CgQRozZoxFiXxr48aNuu666zRhwgRJ/zrCXrNmjTZv3mxxsrZx6tUCLpdLa9euVUNDQ8Ddeu+WW27RhAkTlJmZaXUUS+zZs0f9+/fXwIEDNXXqVFVVVVkdyadefPFFpaamavLkyerXr59GjhypFStWWB3LMo2NjXrmmWc0Y8YMy36kwddGjRqliooKffrpp5Kk999/X++8846uvvpqi5O1jSNKH9q1a5cyMjL09ddfKzw8XC+88IKSkpKsjuUza9eu1fbt27Vlyxaro1giPT1dq1ev1gUXXKADBw5o0aJFGj16tD744AP16tXL6ng+8b//+79avny58vLydPfdd2vLli267bbbFBISounTp1sdz+fWr1+vI0eO6MYbb7Q6is/cddddqq+vV2JiooKDg+VyuXT//fdr6tSpVkdrmxs+43Q63Xv27HFv3brVfdddd7n79u3r/vDDD62O5RNVVVXufv36ud9//33P2JgxY9y5ubnWhbLY4cOH3REREe4nnnjC6ig+0717d3dGRkazsVtvvdV96aWXWpTIWuPGjXP/9Kc/tTqGT61Zs8Z9/vnnu9esWePeuXOn+6mnnnL36dPHvXr1aqujtYmitNDYsWPdN910k9UxfOKFF15wS3IHBwd7Fklum83mDg4Odp86dcrqiJZITU1133XXXVbH8Jm4uDj3zJkzm43913/9l7t///4WJbLOvn373EFBQe7169dbHcWnzj//fPejjz7abOzee+91X3DBBRYl+n6cerVQU1OTnE6n1TF8YuzYsdq1a1ezsezsbCUmJmru3LkKDg62KJl1jh07pr179+o3v/mN1VF85rLLLtPu3bubjX366aeKj4+3KJF1Vq1apX79+nkuagkUx48fb/ZDF5IUHByspqYmixJ9P4rSR/Lz83X11VcrLi5OR48e1XPPPacNGzbotddeszqaT/Tq1avFL7z07NlT55577ln1yy9nYvbs2Zo4caLi4+P15ZdfasGCBQoODtaUKVOsjuYzd9xxh0aNGqU//OEP+tWvfqXNmzfr8ccfD7ifyWtqatKqVas0ffr0gPuK0MSJE3X//fcrLi5OQ4cO1XvvvaeioiLNmDHD6mhts/qQNlDMmDHDHR8f7w4JCXFHRUW5x44d63799detjmWpQPuMMisry33eeee5Q0JC3AMGDHBnZWW5P/vsM6tj+dxLL73kvuiii9x2u92dmJjofvzxx62O5HOvvfaaW5J79+7dVkfxufr6endubq47Li7OHRoa6h44cKB73rx5bqfTaXW0NvEzWwAAGPA9SgAADChKAAAMKEoAAAwoSgAADChKAAAMKEoAAAwoSgAADChKAFq4cKGSk5M9z2+88UZNmjTJsjyAPwmseycBaJeSkhJ9914kV1xxhZKTk1VcXGxdKMAiFCWAFiIjI62OAPgNTr0Cfq6hoUHTpk1TeHi4zjvvPD300EO64oordPvtt0uSbDab1q9f32yd3r17a/Xq1Z7nc+fO1Q9/+EOFhYVp4MCBmj9/vk6ePNnme3731OuNN96ot956SyUlJbLZbLLZbPr88881ePBgLV26tNl6O3bskM1m02effdYRuw74BYoS8HNz5szRW2+9pb/+9a96/fXXtWHDBm3fvt2rbfTq1UurV6/WRx99pJKSEq1YsUIPP/xwu9YtKSlRRkaGcnJydODAAR04cEBxcXGaMWOGVq1a1WzuqlWrdPnll2vw4MFe5QP8GUUJ+LFjx45p5cqVWrp0qcaOHathw4bpySef1KlTp7zazu9//3uNGjVKCQkJmjhxombPnq3nn3++XetGRkYqJCREYWFhiomJUUxMjIKDg3XjjTdq9+7d2rx5syTp5MmTeu655/z755KA08BnlIAf27t3rxobG5Wenu4Z69Onjy644AKvtrNu3To98sgj2rt3r44dO6ZTp04pIiLijLL1799fEyZMUFlZmdLS0vTSSy/J6XRq8uTJZ7RdwN9wRAmc5Ww2m/7z1/K++/ljZWWlpk6dqmuuuUZ/+9vf9N5772nevHlqbGw84/f+7W9/q7Vr1+rEiRNatWqVsrKyFBYWdsbbBfwJR5SAHxs0aJC6d++uTZs2KS4uTpJ0+PBhffrppxozZowkKSoqSgcOHPCss2fPHh0/ftzzfOPGjYqPj9e8efM8Y1988YVXOUJCQuRyuVqMX3PNNerZs6eWL1+u8vJyvf32215tFzgbUJSAHwsPD9fMmTM1Z84cnXvuuerXr5/mzZunoKBvTwZdeeWVevTRR5WRkSGXy6W5c+eqe/funteHDBmiqqoqrV27VpdccolefvllvfDCC17lSEhI0KZNm7Rv3z6Fh4erT58+CgoK8nxWmZ+fryFDhigjI6PD9h3wF5x6Bfzcgw8+qNGjR2vixInKzMzUj370I6WkpHhef+ihhxQbG6vRo0fr+uuv1+zZs5ud/rz22mt1xx13aNasWUpOTtbGjRs1f/58rzLMnj1bwcHBSkpKUlRUlKqqqjyvzZw5U42NjcrOzj7znQX8kM39nx9uAPB7/nSnnP/5n//R2LFjVV1drejoaKvjAB2OU68ATovT6ZTD4dDChQs1efJkShJdFqdeAZyWNWvWKD4+XkeOHNEDDzxgdRyg03DqFQAAA44oAQAwoCgBADCgKAEAMKAoAQAwoCgBADCgKAEAMKAoAQAwoCgBADCgKAEAMPj/oOfXotGl6i4AAAAASUVORK5CYII=",
            "text/plain": [
              "<Figure size 500x500 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "# citric acid vs Quality\n",
        "plot = plt.figure(figsize=(5,5))\n",
        "sns.barplot(x='quality', y = 'citric acid', data = data)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jguNai1nqUhZ"
      },
      "source": [
        "Correlation"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xPj4k63cqcOU"
      },
      "source": [
        "1. Positive Correlation\n",
        "2. Negative Correlation"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "9uEI6JRkqAvA"
      },
      "outputs": [],
      "source": [
        "correlation = data.corr()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 649
        },
        "id": "6-wxjoy8qbBG",
        "outputId": "5dc66dc3-a6c1-4dc8-8512-2545db16c85e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "execution_count": 16,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA4QAAANcCAYAAAAHI2F5AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAEAAElEQVR4nOzdd3RUVdfH8e+k94RUAgQSqnRCh9CLdEGs9KqiotIEeQABWxSpdkWpyguK4qOA8CgKIlVKEKTXAAnpvZH2/hGNDkkoGmYG8vusNWtl7px7Z5+5M/dm37PnjCE/Pz8fERERERERKXOszB2AiIiIiIiImIcSQhERERERkTJKCaGIiIiIiEgZpYRQRERERESkjFJCKCIiIiIiUkYpIRQRERERESmjlBCKiIiIiIiUUUoIRUREREREyiglhCIiIiIiImWUEkIREREREZEySgmhiIiIiIjIbfDzzz/Tp08fKlSogMFg4Ouvv77hOlu3bqVx48bY29tTvXp1li1bdltjVEIoIiIiIiJyG6SlpdGwYUPefffdm2p/7tw5evXqRceOHQkLC2PcuHGMHj2azZs337YYDfn5+fm3besiIiIiIiKCwWBg3bp19OvXr8Q2U6ZMYcOGDRw5cqRw2aOPPkpiYiKbNm26LXFphFBEREREROQmZGVlkZycbHTLysoqte3v2rWLLl26GC3r1q0bu3btKrXnuJbNbduyiIiIiIjIP+AYPNbcIRRrSl9vZs+ebbRs5syZzJo1q1S2f+XKFfz8/IyW+fn5kZycTEZGBo6OjqXyPH+nhFBEREREROQmTJ06lQkTJhgts7e3N1M0pUMJoYiIiIiIyE2wt7e/rQlg+fLliYqKMloWFRWFm5vbbRkdBCWEIiIiIiJiaQxlc6qTVq1asXHjRqNl33//Pa1atbptz1k2X2kREREREZHbLDU1lbCwMMLCwoCCn5UICwsjPDwcKChBHTp0aGH7MWPGcPbsWSZPnszx48d57733+Pzzzxk/fvxti1EJoYiIiIiIyG2wb98+goODCQ4OBmDChAkEBwfz4osvAhAZGVmYHAIEBQWxYcMGvv/+exo2bMi8efP4+OOP6dat222LUb9DKCIiIiIiFsWxyXPmDqFYGfsXmTuEUqcRQhERERERkTJKCaGIiIiIiEgZpVlGRURERETEspTRWUbNQa+0iIiIiIhIGaWEUEREREREpIxSyaiIiIiIiFgWg8HcEZQZGiEUEREREREpo5QQioiIiIiIlFEqGRUREREREcuiWUZNRq+0iIiIiIhIGaWEUEREREREpIxSyaiIiIiIiFgWzTJqMhohFBERERERKaOUEIqIiIiIiJRRKhkVERERERHLollGTUavtIiIiIiISBmlhFBERERERKSMUsmoiIiIiIhYFs0yajIaIRQRERERESmjlBCKiIiIiIiUUSoZFRERERERy6JZRk1Gr7SIiIiIiEgZpYRQRERERESkjFLJqIiIiIiIWBbNMmoyGiEUEREREREpo5QQioiIiIiIlFEqGRUREREREcuiWUZNRq+0iIiIiIhIGaWEUEREREREpIxSyaiIiIiIiFgWzTJqMhohFBERERERKaOUEIqIiIiIiJRRKhkVERERERHLollGTUavtIiIiIiISBmlhFBERERERKSMUsmoiIiIiIhYFpWMmoxeaRERERERkTJKCaGIiIiIiEgZpZJRERERERGxLFb6YXpT0QihiIiIiIhIGaWEUEREREREpIxSyaiIiIiIiFgWzTJqMnqlRUREREREyiglhCIiIiIiImWUSkZFRERERMSyGDTLqKlohFBERERERKSMUkIoIiIiIiJSRqlkVERERERELItmGTUZvdIiIiIiIiJllBJCERERERGRMkoloyIiIiIiYlk0y6jJaIRQRERERESkjFJCKCIiIiIiUkapZFRERERERCyLZhk1Gb3SIiIiIiIiZZQSQhERERERkTJKJaMiIiIiImJZNMuoyWiEUEREREREpIxSQigiIiIiIlJGqWRUREREREQsi2YZNRm90iIiIiIiImWUEkIREREREZEySiWjIiIiIiJiWTTLqMlohFBERERERKSMUkIoIiIiIiJSRqlkVERERERELItmGTUZvdIiIiIiIiJllBJCERERERGRMkolo3JbOAaPNXcIperHL14xdwilpm/o/8wdQqka3r+huUMoVbZWd8+sai0ruZs7hFKVmZtr7hBK1dh3dpg7hFJz4YOHzB1CqXru69/NHUKpah3oZu4QSs2RK+nmDqFUvdm7lrlDKJlmGTUZjRCKiIiIiIiUUUoIRUREREREyiiVjIqIiIiIiGXRLKMmo1daRERERESkjFJCKCIiIiIiUkapZFRERERERCyLSkZNRq+0iIiIiIhIGaWEUEREREREpIxSyaiIiIiIiFgW/TC9yWiEUEREREREpIxSQigiIiIiIlJGqWRUREREREQsi2YZNRm90iIiIiIiIrfJu+++S2BgIA4ODrRo0YK9e/det/3ChQupVasWjo6OBAQEMH78eDIzM29bfEoIRUREREREboM1a9YwYcIEZs6cyYEDB2jYsCHdunUjOjq62ParVq3ihRdeYObMmRw7doxPPvmENWvW8J///Oe2xaiEUERERERELIvBYJG3rKwskpOTjW5ZWVkldmP+/Pk89thjjBgxgjp16vDBBx/g5OTEkiVLim2/c+dOQkJCGDhwIIGBgdx7770MGDDghqOK/4YSQhERERERkZsQGhqKu7u70S00NLTYtlevXmX//v106dKlcJmVlRVdunRh165dxa7TunVr9u/fX5gAnj17lo0bN9KzZ8/S78wfNKmMiIiIiIjITZg6dSoTJkwwWmZvb19s29jYWHJzc/Hz8zNa7ufnx/Hjx4tdZ+DAgcTGxtKmTRvy8/PJyclhzJgxKhkVEREREZEyxGBlkTd7e3vc3NyMbiUlhP/E1q1bee2113jvvfc4cOAAX331FRs2bODll18utee41l2fEObn5/P444/j6emJwWAgLCyMDh06MG7cuNv6vLNmzaJRo0a39TkMBgNff/11iY+fP3++sM9Q8AYzGAwkJibe1rhERERERMo6b29vrK2tiYqKMloeFRVF+fLli11nxowZDBkyhNGjR1O/fn3uv/9+XnvtNUJDQ8nLy7stcd71CeGmTZtYtmwZ69evJzIyknr16vHVV1/d1izbVCIjI+nRo8dNt2/dujWRkZG4u7sDsGzZMjw8PG5TdCIiIiIiZZednR1NmjRhy5Ythcvy8vLYsmULrVq1Knad9PR0rKyMUzRra2ugYKDrdrjrv0N45swZ/P39ad26deEyT09PM0ZUekq6slASOzu7W17H3OZNfpBe7etTpYIXLR4J5beTl4ttN6xfKyaN6IqVwcDWX0/yXOgacnJuz1WUf+vK5XA+nv8SKcmJODm7MHr8i1SsUrVIu9PHDrP83TcAyM3NoWadhgwaMxFbWztTh1yiIF8X3hnVHE8Xe5Izsnl2yV5ORCQbtXk0JJDHu9QovO9fzondJ2MY8d5OU4d7Q6kxERz4v4VcTUvG1sGJ4AHjcCtf2ahNenwUB/5vEUmX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c8wdQqmp6H5n/p5zSepUcDZ3CCXyf9yyfvLkT5EfPWDuEEqdxSeEYh6pqalUrFiRpUuX0r9//1teXwmh5VJCaNmUEFouJYSWSwmhZVNCaLmUEN66uzEhvLvO1vKv5eXlERsby7x58/Dw8OC+++4zd0giIiIiInKbKCEUI+Hh4QQFBVGpUiWWLVt205PkiIiIiIiUFs0yajr6b1+MBAYGoipiEREREZGywaJ/mF5ERERERERuH40QioiIiIiIZVHFqMlohFBERERERKSMUkIoIiIiIiJSRqlkVERERERELIpmGTUdjRCKiIiIiIiUUUoIRUREREREyiiVjIqIiIiIiEVRyajpaIRQRERERESkjFJCKCIiIiIiUkapZFRERERERCyKSkZNRyOEIiIiIiIiZZQSQhERERERkTJKJaMiIiIiImJZVDFqMhohFBERERERKaOUEIqIiIiIiJRRKhkVERERERGLollGTUcJodwWfUP/Z+4QStX5bQvMHUKpCWw/3twhlKonZo01dwilKjUzx9whlJrK1dzNHUKpSruaa+4QStXG36LMHUKp+WxoU3OHUKoeXxNm7hBKVZ1Kd8+xICIx09whlKoVAxuYOwSxACoZFRERERERuU3effddAgMDcXBwoEWLFuzdu/e67RMTE3n66afx9/fH3t6emjVrsnHjxtsWn0YIRURERETEotwtJaNr1qxhwoQJfPDBB7Ro0YKFCxfSrVs3Tpw4ga+vb5H2V69epWvXrvj6+rJ27VoqVqzIhQsX8PDwuG0xKiEUERERERG5DebPn89jjz3GiBEjAPjggw/YsGEDS5Ys4YUXXijSfsmSJcTHx7Nz505sbW0BCAwMvK0xqmRURERERETkJmRlZZGcnGx0y8rKKrbt1atX2b9/P126dClcZmVlRZcuXdi1a1ex63zzzTe0atWKp59+Gj8/P+rVq8drr71Gbu7t+x67EkIREREREbEoBoPBIm+hoaG4u7sb3UJDQ4vtQ2xsLLm5ufj5+Rkt9/Pz48qVK8Wuc/bsWdauXUtubi4bN25kxowZzJs3j1deeaXUX+M/qWRURERERETkJkydOpUJEyYYLbO3ty+17efl5eHr68tHH32EtbU1TZo04fLly7z55pvMnDmz1J7n75QQioiIiIiI3AR7e/ubTgC9vb2xtrYmKsr4Z36ioqIoX758sev4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oeVSQmjZlBBaLiWElksJoWVTQmi5lBDeursxIVTJqIiIiIiIWBQrVYyazN0z7CEiIiIiIiK3RAmhiIiIiIhIGaWSURERERERsSiGu/VX4C2QRghFRERERETKKCWEIiIiIiIiZZRKRkVERERExKKoYtR0NEIoIiIiIiJSRikhFBERERERKaNUMioiIiIiIhbFSjWjJqMRQhERERERkTJKCaGIiIiIiEgZpZJRERERERGxKKoYNR2NEIqIiIiIiJRRSghFRERERETKKJWMioiIiIiIRTGoZtRkNEIoIiIiIiJSRikhFBERERERKaNUMioiIiIiIhZFFaOmoxFCERERERGRMkojhHJbtKzkbu4QSlV4coa5Qyg1lavdXftmx7lkc4dQqt54e6K5Qyg1U56ZZ+4QSpVbk/bmDqFUzR7VzNwhlJr/nYs1dwilqktdX3OHUKoupqSbO4RSk5Ofb+4QREqdEkIREREREbEoVqoZNRmVjIqIiIiIiJRRSghFRERERETKKJWMioiIiIiIRVHBqOlohFBERERERKSMUkIoIiIiIiJSRqlkVERERERELIpBs4yajEYIRUREREREyiglhCIiIiIiImWUSkZFRERERMSiWKli1GQ0QigiIiIiIlJGKSEUEREREREpo1QyKiIiIiIiFkWzjJqORghFRERERETKKCWEIiIiIiIiZZRKRkVERERExKKoYtR0NEIoIiIiIiJSRikhFBERERERKaNUMioiIiIiIhZFs4yazr8aIczPz+fxxx/H09MTg8FAWFhYKYVlGgaDga+//rrw/vHjx2nZsiUODg40atTotj//1q1bMRgMJCYmArBs2TI8PDxKbfvnz5+/4X65NgYRERERESk7/tUI4aZNm1i2bBlbt26latWqeHt7l1ZcZjFz5kycnZ05ceIELi4uJn/+Rx55hJ49e5ba9gICAoiMjLzj94uIiIiIiNwe/yohPHPmDP7+/rRu3brENlevXsXOzu7fPI3JnDlzhl69elGlSpV/vI3c3FwMBgNWVrc++Oro6Iijo+M/fu5rWVtbU758+VLbnjnFRF5k9duvkZaShIOTC4+OnUr5gKAi7U4d3s/Gzz4kKzMDAwZqN2lFz0FP/KP9cbskRl3mfx+/SWZqMnaOznQdNRGvioHFtv39503s27iG/Px8Amo3pMPgZ7C2saxK7/grl/j2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S25uLv7+xivj+/v7ExkZWaL3e+GFFyhfvrxRUlnaTLKojIiIiIiISElZ6n3pi7rdWnG3ybtV7777LsuWLWPz5s04ODj8J+8BSghFRERERERKpKjbrRXHx8cHa2troqKM19aIioqiXLly19126tSpvPvuu/zyyy80bNjwX8dbEioZFRERERERKWV2dnY0bdqUDRs2FLx29epVNmzYQGhoaLHbvf/++0yaNIm1a9fSrFmz/zxOzRCKiIiIiIhFMVhqzehNGjNmDEOHDqVZs2a0aNGCmTNnkpaWxvDh+ff5HDJkCBUqVCj4HuJ7773H66+/ztKlSwkKCir4rqGLiwsuLi7/SYxKCEVERERERP4DDz74IDExMbz++utERkYSHBzM2rVrCxaaCQsLw8rqr6LNefPmceXKFe677z6j/bzxxhtG90ovTUoIRURERERE/iMjR45k5MiRRf5s8+bNRs/Pnz//3wf0D0oIRURERETEotwhFaO3BS0qIyIiIiIiUkYpIRQRERERESmjVDIqIiIiIiIWxUo1oyajGUIREREREZEySgmhiIiIiIhIGaWSURERERERsSiqGDUdzRCKiIiIiIiUUUoIRUREREREyiiVjIqIiIiIiEUxqGbUZDRDKCIiIiIiUkYpIRQRERERESmjVDIq/4nM3Fxzh1CqYtKyzR1CqUm7cmcdm6tX88wdQqlKzbpq7hBKjVvT9uYOoVQl79ti7hBKVfSDjc0dQqkJ8rQ3dwilKiL5irlDKFUVXBzNHUKpybnDPnMsmWatTEf/1iIiIiIiImWUEkIREREREZEySiWjIiIiIiJiUbTKqOlohlBERERERKSMUkIoIiIiIiJSRqlkVERERERELIqVKkZNRjOEIiIiIiIiZZQSQhERERERkTJKJaMiIiIiImJRVDJqOpohFBERERERKaOUEIqIiIiIiJRRKhkVERERERGLohvTm45mCEVERERERMooJYQiIiIiIiJllEpGRURERETEomiVUdPRDKGIiIiIiEgZpYRQRERERESkjFLJqIiIiIiIWBQtMmo6Fj1DOGzYMPr37/+f7X/ChAkEBwcXes3f3x+DwcCKFSv+s/f+U4cOHRg9enTB86CgIGbOnFlq+y/Jv+E/YxARERERkbLhpmYIO3ToQHBw8E0nLP92O1M7duwYEydO5Pvvv6dly5Z4enqaPIY9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PDGepbPf4Zdvl2Dv5MyAkX+VDi6b8y71m7ehfos2/Lr6G8JOH+NKViaHd/4KQHCrjnS9r+i/8URuhiHv7/WG8p9KTU3lySef5LvvvsPV1ZWxY8eyevVqgoODmTlzJtnZ2bz11lssXryY8PBwfHx8aNmyJRMnTqRBgwYsXLiQ0aNHk5iYWLDPFStWcPfdd5OXl0dUVBRPPPEEu3btIi4ujoCAAIYOHcobb7yBlZUVEyZMYMWKFRw8eBDIv53EwIED2bFjB6mpqWzatIkOHToUxOrv78+wYcOYM2fOTffV/1HLWnb7Vj0/2DJXw/s31hy+/pfVbzfWVndITck1lXxuv3uFFqdZpTunLwDRqZZRElxaJj8/09whlJqdPxR9U+jb1Wf7LXdF5n9jXLvC99W7XR29nGTuEEpVr3qWU07/Tx/tOG/uEIr0RGiQuUModUoIpUjnz5+nWrVq7NmzhyZNmtz09koILZcSQsumhNByKSG0XEoILZsSQsulhPDm3YkJoUpGxUh2djZxcXG8+uqrtGzZ8l8lgyIiIiIicntQQihGtm/fTseOHalZsybffPONucMRERERkTLI6k5ZZvQ2oIRQjHTo0AFVEYuIiIiIlA26Mb2IiIiIiEgZpRlCERERERGxKKoYNR3NEIqIiIiIiJRRSghFRERERETKKJWMioiIiIiIRdEqo6ajGUIREREREZEySgmhiIiIiIhIGaWSURERERERsSiqGDUdzRCKiIiIiIiUUUoIRUREREREyiiVjIqIiIiIiEXRrJXp6N9aRERERESkjFJCKCIiIiIiUkapZFRERERERCyKQcuMmoxmCEVERERERMooJYQiIiIiIiJllEpGRURERETEoqhg1HSUEMp/4sJH95s7hFL12FeHzB1CqflySDNzh1CqNp6JMncIpaqqm4u5Qyg1P5+LNXcIpSrI097cIZSqnT9MNncIpaZlv5fMHUKpWrl0grlDKFUTfj5p7hBKTbtq7uYOQaTUqWRURERERESkjNIMoYiIiIiIWBQrrTJqMpohFBERERERKaOUEIqIiIiIiJRRKhkVERERERGLooJR09EMoYiIiIiISBmlhFBERERERKSMUsmoiIiIiIhYFC0yajqaIRQRERERESmjlBCKiIiIiIiUUSoZFRERERERi2JQzajJaIZQRERERESkjFJCKCIiIiIiUkap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O4RSp5JRERERERGxKFpl1HRUMioiIiIiIlJGKSEUEREREREpo1QyKiIiIiIiFkUlo6ajGUIREREREREzi4+PZ+DAgbi5ueHh4cEjjzxCamrqdduPGjWKWrVq4ejoSKVKlXjmmWdISkq6qfdVQigiIiIiImJmAwcO5Pfff2f9+vWsWrWKX3/9lccff7zY9hEREURERDB16lSOHj3KwoULWbt2LY888shNva9KRkVERERExKIYytiN6Y8dO8batWvZs2cPzZo1A2D27Nn06tWLqVOnUr58+ULb1K9fn2+//bbgebVq1Xj77bcZNGgQOTk52NiULNXTDKGIiIiIiEgJZGVlkZycbPTIysq65f3u2LEDDw+PgmQQoEuXLlhZWbFr164S7ycpKQk3N7cSJ4OghFBERERERKREJk+ejLu7u9Fj8uTJt7zfyMhI/Pz8jF6zsbHBy8uLyMjIEu0jNjaWSZMmXbfMtChKCEVERERExKJYGSzz8dJLL5GUlGT0eOmll4rtx4svvojBYLju4/jx47f875WcnEzv3r2pW7cuEyZMuKlt9R1CERERERGRErC3t8fe3r7E7ceOHcuwYcOu26Zq1aqUK1eO6Ohoo9dzcnKIj4+nXLly190+JSWFHj164Orqyvfff4+trW2J4wMlhCIiIiIiIv8JX19ffH19b9guNDSUxMRE9u3bR9OmTQHYuHEjV69eJSQkpNjtkpOT6d69O/b29qxcuRIHB4ebjlEloyIiIiIiYlEMFvrff6VOnTr06NGDxx57jN27d7N9+3ZGjhzJQw89VLDCaHh4OLVr12b37t1AfjLYrVs30tLS+Oyzz0hOTiYyMpLIyEhyc3NL/N6aIRQRERERETGzL7/8kpEjR9K5c2esrKy49957+eCDDwp+np2dzYkTJ0hPTwdg//79BSuQVq9e3Whf586dIygoqETvq4RQRERERETEzLy8vFi6dGmxPw8KCiIvL6/geYcOHYye/1tKCEVERERExKIYytZ96c1K3yEUEREREREpo5QQioiIiIiIlFFKCE0kKCiImTNnlrj9+fPnMRgMHDx48D+LSURERETEEpl7NVFTrzJqTkoI73AdOnRg9OjR5g5DREREREQskBaVEYvn52LHsOYVcLGzJiP7Kgv3hnM5OcuoTS1fZ+5u4Ie9jRXkwZHIVL4/EsWtr7tU+iLDw/h0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EBwcDEBiYiKenp5s2rSJDh06EB8fz4gRI9iwYQNOTk48/vjjhIWFkZSUxIoVKwA4efIkQ4cO5dChQ2RkZHDu3DmCgoI4depUQalpVlYWlStXpkePHkyfPp3jx48X29eS+t83v5fWP71FGBZc+FYXt6vJG0+ZO4RS1aXunbX89or9lrNC4a3qYqG3F/m37rTlxiOSb58ZvBvpe4ctw3/XwxPMHUKpGvPOM+YOodScjbG8Cpdb8X9Dgs0dQrG2nbLMC5dtatx5JbuaISyhOnXqsHbt2iJ/Zmtry9y5c41WB/2nP+//93fly5fn559/LrJ9UFBQoe8lenh4GL3m5eVVkPgVp2bNmkb3LvxTjRo1+O6774rc5np9FRERERGRO4cSQhERERERsSh3WFGGRdOiMiIiIiIiImWUZgjNRF/dFBERERERc1NCKCIiIiIiFsVKy4yajEpGRUREREREyiglhCIiIiIiImWUSkZFRERERMSiqGDUdDRDKCIiIiIiUkYpIRQRERERESmjVDIqIiIiIiKWRTWjJqMZQhERERERkTJKCaGIiIiIiEgZpZJRERERERGxKAbVjJqMZghFRERERETKKCWEIiIiIiIiZZRKRkVERERExKIYVDFqMpohFBERERERKaOUEIqIiIiIiJRRKhkVERERERGLoopR09EMoYiIiIiISBmlhFBERERERKSMUsmo/CdaBbmZO4RSlZqdY+4QSk3diu7mDqFUpV+5au4QStVr3WuaO4RSczEl3dwhlKoKLo7mDqFU1Qh2NXcIpWbCzyfNHUKpGvPOM+YOoVRNf/kDc4dQaurcfY+5Qyg7VDNqMpohFBERERERKaOUEIqIiIiIiJRRKhkVERERERGLYlDNqMlohlBERERERKSMUkIoIiIiIiJSRqlkVERERERELIpBFaMmoxlCERERERGRMkoJoYiIiIiISBmlklEREREREbEoqhg1Hc0QioiIiIiIlFFKCEVERERERMoolYyKiIiIiIhlUc2oyWiGUEREREREpIxSQigiIiIiIlJGqWRUREREREQsikE1oyajGUIREREREZEySgmhiIiIiIhIGaWSURERERERsSgGVYyajGYILcz58+cxGAwcPHjQovYXFBTEzJkzSyUmERERERGxDEoIRUREREREyiiVjMptIT7yEj9+9D4ZKUnYOznT53/P41sxqFC7xJhIVn38PlHnT+PuG8Cjkz82fbA3EB1xkSWz3iI1JQlHJ2cGP/MKAZWqFmp34vA+Vi6ZR1ZGBhigftNW3DXkSaysLOc6TmpMBPuWziArLRlbByeaDhiNW0BlozZp8VHsXzqTxPCzOHv502n8B2aK9saSosPZumg6WalJ2Dk602bIGDzLVy7U7uT2dRxetxzyrhJQqxGhA57GytryhtOoiIssmjmJ1OT8c23o6FcpX8S5dvzQXr5fPI+szAwMGKjfrBV3D7Wscw3yx4GVfxsH+l5nHPjxb+PAYxY4DkD+WLBo5lukpSTh4OTMkGdfKfL4nDi8jxWL88cCgwHqNWtFfwsbCy5dvMCUN18lKSkRZxcXxr86iaCq1Qu1O7R/Dy8/9xQVKwcVvPbBJ0uwd3AwYbTX5+dix6MtK+JiZ0NGdi6f7bpERHKWUZvafs7c16gcDjZW5AGHI1L45lAkeeYJ+bpSYiLY8+UMrlwbp5s9PBr3f47TcVHs+ds43fV5yxynpz1/H73bN6ByeW9CHpzM4ZPhRbYb2j+UccO7YmUwsHnPSZ6d/BU5OVdNHO2NBXo58ma/ung42ZKamcMbK49xNibNqE3Tyh7MfrgRF+LSC14b9vk+siywP6VNFaOmYzmfJmXI2rVradOmDR4eHnh7e9OnTx/OnDlTbPvff/+dPn364ObmhqurK23bti1of/XqVd58800qVqyIvb09wcHBrF27ttA+zp49S8eOHXFycqJRo0bs2LHD6Offfvst9erVw97enqCgIKZNm1a6nb5FP302k8Yde/PEtEW07PMQqz5+v8h29o5OtL9/OP2eftnEEZbcsnnv07rbXbwxdxld7xnEkg/eLrKdk4srw8dO5NUPv+SFaZ9z9sRRdm/6ycTRXt+Br+cQFNqdbi9/TM1O97Hv/2YWamNr70SdXoNoPmic6QO8Sb99OZtabXpw78RPadDtfrYtnl6oTUpsJPt/XEKvse9z75ufkZGcyImtlnVc/rR0znu06d6PNz/6im73DmLRzLeKbOfk4sqj499kwpylvDzjc84eP8JOCzvXANZcGweenLaI0D4P8eN1xoEOFj4OACyd+z5tut/FhHnL6HbPIBbPKn4seGTcRF6f8yUvTv+cc8ePssvCjs+s996kV//7WPj1jzw4aDhT3nqt2LYVKwfx8eLlBQ9LSgYBhjavwJYz8by85iRrjsXwSEjFQm3Sr+Ty8W9hvPrTKSauO011HydaVfEwfbAlsP/rOVQN7U6PVz6mVuf72Lt0ZqE2tg5O1O89iJDBlj1Of/fLAToPn8GFiLhi21Qu780bT/Why4gZ1LtrIn7ebjxyTxsTRllyr/auzXf7w7l7zk4W/naBiXfVKbLdhbh0Bnyyp+BRFpJBMS0lhGaQlpbGmDFj2Lt3Lxs2bMDKyoq7776bq1cL/4KHh4fTrl077O3t2bhxI/v27WPEiBHk5OQAMGvWLKZNm8bUqVM5fPgw3bt356677uLUqVNG+3nllVcYN24cBw8epGbNmgwYMKBgH/v27eOBBx7goYce4siRI0yYMIHXXnuNhQsX/uf/FiWRlpTA5bMnqd+mCwC1W7QlOS6G+MjCVwYdXdwIrNUAW3vL+gPjTymJCYSdPk7zDt0BCA7tQEJsNDGXLxVqG1i1Jj7lKgBga2dPxSrViYuONGm815OVkkjixVMENu0IQPlGrchIjCU1JsKonZ2zKz5V62FtocfkTxnJicSFnaJai04AVG7cmrSEWJKjjftzfv82KjUMwcndC4PBQK12vTi7d4s5Qr6u5MR4Lpw+Tsi1c61Jq44kxEYTHVH4XKtUrRa+RudaDeKiLps03hv5cxxocBPjgJ0Fn3N/jgUtrh2fxq06kBgbTfRtOBYkxMdx8tgfdOneG4C2HbsSExVJ+MUwM0d281ztrQnycmTH+UQA9l1KxsvJFj8XO6N2YYmZxKRlA5BzNY+whEx8nO3+uTuzy0xJJCHsFJWa5Y/TFRq1Iv1647Sd5f7OAGzff4bw6MTrtrmnSzCrthwhKi4FgE+/2coDPZqaILqb4+lkS53yrqw5HAXAhmMx+LvbE+jpaObIpCxSQmgG9957L/fccw/Vq1cnODiYzz//nCNHjvDHH38Uajtnzhzc3d1ZtmwZzZo1o2bNmgwfPpxatWoBMHXqVF544QUeeughatWqxXvvvUdwcHChBWDGjRtH7969qVmzJhMnTuTChQucPn0agOnTp9O5c2dee+01atasybBhwxg5ciRTpkwpUX+ysrJITk42emRfybrxhiWUHB+Di6cXVtbWABgMBty8/UiOiy619zCVhNgo3Dy9sb5WXmgwGPDy9Sc+Juq62yUnxHHgt83Ub97KFGGWSHpiLA5uxsfFydOXjMQYM0f276QlxOD4j/44e/qSGh9dqJ2Ll1/Bc1dvf9LiLa/PCbHRuHv5GJ1rnr7+xMdcP5FISojjwG+baNi8tSnCLLE7aRyAoscCT19/Em4wFiRdGwsaNLOcsSAmOgovHx+sbf7qi59/ANHFXFS4HH6RJ4c+wNMjBrDy22WmDPWGvJxsScrI4erfaj/j0rPxcrItdhs3BxuaBbpxKDzFBBHenIxixun0BMsbs0pLYIAXYZfjC55fiIgnsJynGSMqWjl3B2JTssjN++tki0zKopx74aS8oqcjXz7WnCWPNOP+ZhVMGaaUEUoIzeDUqVMMGDCAqlWr4ubmRlBQEABhYYWvph48eJC2bdtia1v4wyg5OZmIiAhatzb+w61169YcO3bM6LWGDRsW/H9AQAAA0dH5f0gdO3asyH2cOnWK3NzcG/Zn8uTJuLu7Gz1WLZxzw+2kZDLS0/jo7efpcvdAKlcvupxEpDRkpKcxd9J4ut0zkMo1dK5Zmoz0NOa99Txdb+PjU71WHf7vh/XMW/Q1E96dwarvl7Pll3XmDutfc7Cx4tm2lfnpeCznEzLMHY7cgY5fTqHnzO0MnL+HsV8f4b6mFeha1+/GG94JDBb6uANZ3ioIZUDfvn2pXLky8+fPp3z58ly9epX69etz5cqVQm0dHUundODvCaXh2o1diipR/TdeeuklxowZY/Ta10dv7ar9ka0/s2vNtwDUa9WR1IR4rubmYmVtTV5eHslx0bh53x4D4q5NP7Hxh/yr4M3adSU5IY7c3BysrW3Iy8sjPiYKL1//IrfNzEhj7sQxNGzRls79HjJl2Dfk5OFDZrLxcUlPiMHRw9fcof0rzp6+ZPyjP/+cDfyzXUrsXzMfKXFROHtZRp93bvyJX66da83bdSEpPtboXEuIicLLt1yR22ampzF7wnM0CmlLl/4DTBl2sQ7fQeMA5B+fjSuvjQVtC48FCTFReBY3FqSn8eGEMTQKsYyxYP2alXyzbAkAHbv2JD42ltycHKxt8vsSHXUZP/+AQts5O7sU/L+vXzk6du3JkUP7ad+lu8liv5749GzcHW2wMlAwS+jtZEt8enahtg42VozpEMSB8GR+PhFr4khLxrGYcdrJ0zLGrP/CxcvxVAn8q3+Vy3txMTLBjBEVLTIpEx9Xe6wNhoJZwnLu9kQmZRq1S7vy14X56JQs1h6NonEld9b/cXtWR4hlUkJoYnFxcZw4cYL58+fTtm1bALZt21Zs+4YNG7Jo0SKys7MLzRK6ublRvnx5tm/fTvv27Qte3759Oy1atChxTHXq1GH79u1Gr23fvp2aNWtifa3M5Hrs7e2xt7c3es3WLqnE71+UBm270aBtt4LnZw7t5ui2X2jYvjvHd2/F1csXr3K3R9lESMeehHTsWfD893072bN5HS079+bgjs14ePviG1B40YKsjHTmThxL3SYh9HhgmAkjLhl7Vw88Klbj4r5NVG7RhYhDv+Ho7oOLb3lzh/avOLp54B1YnTO7N1IjtCsXDmzHycMbNz/j/gQ1bs3qaeMJ7j0QRzdPTvy6hirN2hezV9Nq2aknLTv9da4d3beTXZvX0apzb/b/tgkPHz/8yhc+1zIz0vlgwhjqNWlJrweHmzLk62rYthsN/zEOHNn2C41uw3EACh+f3/fvZPfmdYR27s2B3/LHAr8ixoLMjHQ+nDiWek1C6GkhY0HXXnfRtdddBc/37NjGL+tW0713P7ZuWo+Pnz8VAisV2i4uNgZPL2+srKxIT0tj5/Zf6dn3blOGfl0pWblcSMggNMiD7ecSaVrRjYSMbKJTjS/Y2ttY8Vz7II5cTmXVH5ZbfulwbZwO27uJoJAuhB/6DSeP23ecLonvNxxk44IxvP3RaqLiUnj0vrYsX7fP3GEVkpCezfHLKfRq6M+PhyLpXMeX6OQsLv5jptnHxY641CvkAU521rSt6c0PByzrO95y+1NCaGKenp54e3vzySefEBAQQFhYGC+++GKx7UeOHMns2bN56KGHeOmll3B3d2fnzp20aNGCWrVqMX78eN544w2qVatGcHAwCxYs4ODBg3z55Zcljmns2LE0b96cSZMm8eCDD7Jjxw4+/PBD5s6dWxpdLhU9RzzHqo/f57eVS7FzdKbP43+thLZ6/jRqNAmlZtNWZGdl8tHYYeTkZJOVnsbskQ9Rv00XOj70qBmjNzbgqfEs+eBt1n27BAdHJwaNeqXgZ19+OJkGLdrQsEVbNq1azvlTf5CVmcHBHfmLljRu3Yke9w81V+iFBD/wNPuWzuTEL8uxtXeiyYBnAdi/7AMC6ocQUD+EnCuZrH/nCa7mZJOdmc5PE4ZRqVlH6vWxnH78qdXDo9i6eDqH136FrYMTbYY8B8C2JTOp1LAllRq1xNU3gMZ9BrFmav45WK5mQ2q37Xm93ZrNwKeeZ9Gst1i7fDEOTs4Mfeavc23J7Mk0bNGGRiFt2fjj15w/9QdXsjI5cO1ca9K6I70sJPn4U68Rz/Hj38aBvn8bB1bNn0bNv40D88YOIzcnm8z0ND4Y+RANLGwcAHj4yfEs/uBt1n2TPxYM/tvx+eLa8WkY0pZNPy6/dnwyOLjz2ljQqhM9H7Cc36HRL7zGlLde4/8WfYqTszPjX3mz4GfT3nmD0LYdaNW2I1s3/cKq77/G2tqa3Nxc2nXqSvc+/c0XeBEW7wlnREggvev4kZmTf9sJgGHNK3AwPJmDESl0relNFW8n7G2saFrRDYC9F5MsMjls+sDT7Fk6k+O/LM+/7cS1cXrvsg8oXz+E8tfG6XVvP0HutXF69Rv543SDvpZzjgHMfuUherath7+3GyvnPk1qWhb1+01k7usPs3rLEVZvOcL58DgmzVvNxgX5lUu/7jvFp98Wf+HdnN5efYKJ/eowok0QaVk5TFiZ/3Wf1/rUZsvJWH49GUvnOr7c17QCuVfzsLYy8MuxGH44WDYSQsOdWp9pgQx5eXmWeNucO9ovv/zCM888w9mzZ6lVqxYffPABHTp04Pvvvyc4OJgqVapw4MABgoODATh8+DDjx49n27ZtWFtbExwczMKFC6latSpXr15l0qRJzJ8/n+joaOrWrcu7775Ljx49ADh//nyh/SUmJuLp6cmmTZvo0KEDkH/biddff51Tp04REBDAqFGjGDfurz+2goKCGD16NKNHjy5RHxftvVha/1wWobzznbPq14Zz8TdudBvxcLjxLPbtJKSCh7lDKDUXU9Jv3Og2UsHlzhkHAGr4uZo7hFIz4eeT5g6hVAW429+40W1k+suWeV/Df6PO3feYO4RStf/1TuYOoViHL6aaO4QiNQx0uXGj24wSQvlPKCG0XEoILZsSQsulhNByKSG0bEoILZcSwpt3JyaEKhkVERERERGLYlDFqMnothMiIiIiIiJllBJCERERERGRMkoloyIiIiIiYlFUMWo6miEUEREREREpo5QQioiIiIiIlFEqGRUREREREcuimlGT0QyhiIiIiIhIGaWEUEREREREpIxSyaiIiIiIiFgUg2pGTUYzhCIiIiIiImWUEkIREREREZEySiWjIiIiIiJiUQyqGDUZzRCKiIiIiIiUUUoIRUREREREzCw+Pp6BAwfi5uaGh4cHjzzyCKmpqSXaNi8vj549e2IwGFixYsVNva8SQhERERERsSgGC338lwYOHMjvv//O+vXrWbVqFb/++iuPP/54ibadOXMmhn9ZZ6vvEIqIiIiIiJRAVlYWWVlZRq/Z29tjb29/S/s9duwYa9euZc+ePTRr1gyA2bNn06tXL6ZOnUr58uWL3fbgwYNMmzaNvXv3EhAQcNPvrRlCERERERGREpg8eTLu7u5Gj8mTJ9/yfnfs2IGHh0dBMgjQpUsXrKys2LVrV7Hbpaen8/DDDzNnzhzKlSv3r95bM4QiIiIiImJZLHSV0ZdeeokxY8YYvXars4MAkZGR+Pn5Gb1mY2ODl5cXkZGRxW733HPP0apVK/r16/ev31sJoYiIiIiISAncbHnoiy++yHvvvXfdNseOHftXsaxcuZKNGzdy4MCBf7X9n5QQyn/iaGS6uUMoVc2beJk7hFITkZhp7hBKVblAV3OHUKoSMq+YO4RSk5OXZ+4QSlXO1TurP0cvJ5k7hFLTrpq7uUMoVeuOxZs7hFJV5+57zB1CqTn2/XfmDqF0vd7J3BHc8caOHcuwYcOu26Zq1aqUK1eO6Ohoo9dzcnKIj48vthR048aNnDlzBg8PD6PX7733Xtq2bcvmzZtLFKMSQhERERERsSgGS60ZvUm+vr74+vresF1oaCiJiYns27ePpk2bAvkJ39WrVwkJCSlymxdffJFHH33U6LUGDRowY8YM+vbtW+IYlRCKiIiIiIiYUZ06dejRowePPfYYH330EdnZ2YwcOZKHHnqoYIXR8PBwOnfuzOLFi2nRogXlypUrcvawUqVKVKlSpcTvrVVGRUREREREzOzLL7+kdu3adO7cmV69etGmTRs++eSTgp9nZ2dz4sQJ0tNL96tZmiEUERERERGL8i/vsX5b8/LyYunSpcX+PCgoiLwbfD//Rj8vimYIRUREREREyiglhCIiIiIiImWUSkZFRERERMSilMGKUbPRDKGIiIiIiEgZpYRQRERERESkjFLJqIiIiIiIWBbVjJqMZghFRERERETKKCWEIiIiIiIiZZRKRkVERERExKIYVDNqMpohFBERERERKaOUEIqIiIiIiJRRKhkVERERERGLYlDFqMlohlBERERERKSMUkIoIiIiIiJSmiPEkAAAXS1JREFURqlkVERERERELIoqRk1HM4R3sAkTJhAcHFzwfNiwYfTv399s8YiIiIiIiGXRDGEZMmvWLPLy8gqed+jQgeDgYGbOnGm+oERERERExGyUEJYh7u7u5g7hX0mNieDA/83kSloyto5OBD80GrdylYzapMdHcWDZLJLCz+Lk5U+HsbPMFO2NRVwK44N3Xyc5KRFnZxdGvTCRSlWqFds+Ly+P18f+j7Mnj/Plql9NGOmN+bva8XjLQFztbUjPzmX+zouEJ2UZtanj78wDwQE42FiRlweHIpL5+mAkecXs05wSo8LZ+PlUMlOTsXN0otPwsXhVCCrU7tjWtRz46Wvy8vKoULsRbQeOxNrG8obT2MuXWD5nMmkpSTg4OXP/Uy/iH1ilULuE6Mssn/suEedO4+VXjmemfGaGaG8sPvISqz+eQkZKEvaOzvT633h8KwYVapcUE8nqj6cQdeE0Hr7lGP7Ox6YPtgSiIy7yxQdvk5aciKOzCwNHvUxApaqF2p08vI+VSz4iKzMDgwHqNW1F38FPYGVlOUU+MREXWTr7HdKSE3FwcmHAqJcJqFT4XDt1ZB+rlnxMVmY6GAzUbRpKn0GW1RfIP9dWfTyF9GvnWp9izrXEv51r7r7leMQCz7VyrnY82boyrg7WpF+5ykfbw7iUlGnUpoaPEyNaBgJgYwXHo9NYtDucnKuWN1IHejnyZr+6eDjZkpqZwxsrj3E2Js2oTdPKHsx+uBEX4tILXhv2+T6ycq6aOtzrmvb8ffRu34DK5b0JeXAyh0+GF9luaP9Qxg3vipXBwOY9J3l28lfkWFhf/hOqGTUZyxqBy5C0tDSGDBmCi4sLAQEBTJs2jQ4dOjB69GgADAYDK1asMNrGw8ODhQsXFjx/4YUXqFmzJk5OTlStWpXXXnuN7OzsYt/z7yWjw4YNY8uWLcyaNQuDwYDBYODcuXNUr16dqVOnGm138OBBDAYDp0+fLo2u37TD38yhcsvudH7pI6p3vJeDy2YWamPj4ETtHoNoOnCs6QO8SfOmv0W3Pvcwd8kK7h4wjNnvvXHd9iuXf0m58oEmiu7mDG9ekU2n43l+1QlW/xHDYy0Lx5l+JZe528J4afVJ3lh7iho+zrSu4mmGaG9sy5IPqNuuJw+//RmNezzAxgXTCrVJjolk94rF9H9hKg+/8znpyQkc+3WNGaK9se8/mUaLLn0YN+sL2vcbwPK57xbZzt7JmW4PPcJDz75q4ghvzrrPZxHcsRePT11ISN8HWfPxlCLb2Tk60e7+4dz11MsmjvDmfDVvCq273cVrc5fR+e6BfDn7nSLbObq4MmzsBF6Z/QXjp37GueNH2LN5rYmjvb6vP5pKaNe+vDzn/+h098P8X3F9cXZl8JgJvPjBF4yd8innjx9lr4X1BWDttXPtiakLCe37IKuKOdfsb4Nz7dGWgWw4FceYFcdZeTSKJ1pXKtTmQkIGr64+wUurTvD8yhO4O9jQtZaPGaK9sVd71+a7/eHcPWcnC3+7wMS76hTZ7kJcOgM+2VPwsLRkEOC7Xw7QefgMLkTEFdumcnlv3niqD11GzKDeXRPx83bjkXvamDBKKQuUEJrJ+PHj2bJlCz/88AM///wzmzdvZv/+/Te1D1dXVxYuXMgff/zBrFmzmD9/PjNmzCjRtrNmzSI0NJTHHnuMy5cvc/nyZSpVqsSIESNYsGCBUdsFCxbQrl07qlevflPxlYaslEQSL56mYtMOAAQ0bEVGYiypsRFG7eycXPGuWhdrOweTx3gzEhPiOXPiGO279gIgtF1nYqOjuBweVmT7sHNn2L19E/cMGGbCKEvG1d6aKt6O/HY+AYA9F5PwcrLFz8XOqN2FhExi0q4AkH01jwuJGfj+o40lSE9OJOb8KWq27AxA1aZtSI2PJSnK+Fw78//t3Xlcjen7B/DPad9TlEKpaCjtjH0tYx2GjC1bi0FjmzbLIMvYJgpNZowlhSHbMHbZx4QwbZhoV6ikVCq0nd8ffTu/jhM6Sfd5Ttf7+/J6dZ5zMp/n63R6rue+7+v+9zqMbLpDRVMbPB4PnfoNR+LtqwwSf1hRwUs8TXkEmz5fAQAsuvVDwYvneJH1ROS1KmoaMOpoBQVFyf35KS54iayUBHTqNRAA0OHLPniVl4OXWaJ31JXVNNCmgwXkJfh8XuW/RHryQ3TpNwgAYNOjP16+eI6cTNF/HwOTL9BCrzUAQF5BEa2NTZH7PLNR837Iq/yXyEh+iM7/OxfrHv2Rn1v7ubQx+QIt9FoB+P9zyXue1ah5P6a44CUyUxJg8c57Le897zUDCX6vaSjJwbi5Cv5JyQMA3E4vQHNVebRUF/4MLq3go+J/g4FyMjwoyErm5aGWijzMWqnjTFw2AOBSfA5aairCQEuZcbL6iYhKxtPn+R98jeNAG5y6dg/Zua8AADuPXMe4IZ0bIR1pSiTzJ17KFRUVYdeuXdi4cSMcHBxgaWmJ0NBQlJeXi/X3LF26FD179oSRkRFGjBgBb29vHDp0qE7fq6mpCQUFBaioqEBPTw96enqQlZWFs7MzHj16hNu3bwMAysrKsH//fri6ur7373r79i0KCwuF/pSXlYp1Lu/zOv8FFDW0ISMrC6Bq5FS5mQ5ev8xpkL+/seU+z4JW8xaQla2aXsjj8dCipR5yskUviMrLy/Cr/0+Y5bkEsv87f0nSXEUB+a/LUXNGUW5JGZqryr/3ezSV5PClgSZinhY2QkLxFOflQEVTS+i9pq6tg1d5z4VeV5SXA/XmuoLH6i1aoihP8t6PBbnPod6sudB7rVmLlih48fwj3ymZXuXlQK2Z8GeBRnNdFOZy83xe5mZDU0v430erRUu8zMn+4PcVvsxFzM2rsOjSqzFi1kl+7nNo1HIu+S8+fi6xN6/CvEvPxohZZ4VS9F5rriKP/NdlQp/TL4pL0UJV9KZcC1UFrP+6A7aPt0BJWQXCH71oxKR1o6ephBev3qKiRj+ErIK30NMULcjbaCnjj+++xF63LhjbpXVjxmxQBvraSM/MEzx+/CwPBnqSOcumofEk9H/SiApCBpKTk1FaWopu3boJjmlra6NDhw5i/T0HDx5Er169oKenBzU1NSxduhTp6bWPNNVVq1atMHz4cAQHBwMATp48ibdv32Ls2LHv/Z5169ZBU1NT6E/kYclbR8E1B0O3o3sfexi0FV1TxEVKcjLw6GeEM/E5SM17zToOIZzzuqQY29cuhMMoJxi278g6zid5U1KMnWsXwX7URM6fi7R4UVyKRaceYdbhB5CTkUFXQ272HQCAh5mvMHRzBCbtuAOvQ/fwbefW+Mpc9+PfSEgTJXldEAiAqjuSNTuCAhBaH3jz5k1MmjQJK1euxODBg6GpqYmwsDD4+4uueRLX9OnTMWXKFGzatAm7d+/G+PHjoaKi8t7XL168GJ6enkLHll96/Mk5AEC5WQu8LcxDZUUFZGRlwefz8To/B8paOg3y9zeGK+dP4cThfQCAPg5D8DL3BSoqyiErKwc+n48X2VnQaakn8n0PYv/Fi+dZOHPsICorKvC6pBgzJgzHhm37oNmM/d3B3JJSNFOWgwwPgrvPzVXkkVssuo5VSU4GPgOMEfWkEOceSt5dZwBQ1dZBScFLoffaq7wcqGsLX0SoaeugMOf/p+u9epENNW3JeD9GXTuPf05VzRKw7uWAV/m5Qu+1/BfZ0GzBnYui+9cv4M7ZIwAAsx4DUJQv/FlQmPscGs25cz63r5zFlRMHAQB2fQai4KXwv8/LF9nQ0mlZ6/e+eV2C31Z5wbJrb9h/M6ExY9fqzpVzuHryf+fSeyAKazmXZi3efy6//+QNi6690X8k+3MBgHvXL+D2/95r5lLwXquWW1KGZsryQp/TLVQV8KL4/bN43pZX4mbaS/Qy1sLNtPzGCVpHWQVv0EJdEbI8nmCUUE9TEVnvNMkpLq0QfP381Vucu58NW0NNXPiPe6O8GZl5MDb4/98xbVtpIyPrJcNERBpRQchAu3btIC8vj8jISBgaVi3ufvnyJRISEtCvXz8AgI6ODjIz//+iMzExESUl/98t68aNG2jbti2WLFkiOPb4sXhFmIKCAioqKkSODxs2DKqqqvjtt99w7tw5/P33hztbKioqQlFRUeiYnHzDrBFTVG8GzTbt8OTfqzDs6oDMuBtQ0mwBtRatGuTvbwwDBn+NAYO/FjyOiozAtQtnYD9kJG7+fQnNdXSh31p0kf/awGDB18+znsFj+gRsDzvdKJnr4tXbCqTlvUZPIy38k/oSXxpo4mVJGZ4XCV9oKMrJwHuAMeIyX+HEA8n9Zayi0Qw6hu2QcOsSOvYahJR//4GaVgtothR+r7Xr3BvH1nvhy5GToayhhQfXTqN91/5sQr/Drt9g2PUbLHj8KCYSMdcvoHP/obgfeQ2azXXQQq8Nw4TisejzFSz+twYSAFJi7+BBxEVY9h2MR3euQ127BbT0uDMVrOuAoeg6YKjgcXzULdy9Fo5u9sMQc/MqmjXXgY6+6L/P2/8Vg2a23TB4rHMjJn6/LwcMwZcDhggex0ffwr/XwtHVfhhib16F5gfO5fdVXuho2xWDxk5rzMgfZNnnK1i+8167H3ERVjXea9oceq9VK3xTjrS81+htoo2/k/PQ1VATecVlyH4l/DndUl0BL4pKUcEHZGV4+NJQE+kvJW8mx8uSMjzMfIVhVi1xMjYLDmY6eF74FhnvZG2hpoDcolLwAagoyKLPF83xV7TkrLsVx7FLMbi82xNrtp1Gdu4rTP+2Dw6f/5d1rEbBk87ZmRKJCkIG1NTU4ObmBh8fHzRv3hy6urpYsmSJUNtte3t7BAUFoUePHqioqMDChQshL///a7NMTU2Rnp6OsLAwfPnllzh9+jSOHTsmVg4jIyNERkYiLS0Nampq0NbWhoyMjGAt4eLFi2FqaooePXo02LnXh/W33yM6bAsSLx2GnJIKbCfMAwDEHPwFep26Qs+iG8pL3+Ly+lmoLC9D2ZsShK9yQZvO/WE+XHIuOKq5ey5B4M/LceSPYKioqGLuwhWC57ZuWIUve/ZD11792AUUw+7bTzGjRxuM7KSL12UV2HGrqomEa9c2iH5aiOinhRjUoQVMmqtAUU4GXQyqpiDdTi/ASQksDvtOnYcrwf6IOnMQCkoqGOBSNfJ9JWQTjGy6w9imBzR09PHlN1NwbH1VR9tWHSxh3ncYy9jvNXqGFw5vXY8rx/6AkrIKvv1+keC5o9v8YNalF8y79ELp2zfwnz8ZFWVleFNSjHWzvoVt30EY4jSDYXpRg11/wJntG3DzxAEoKqtg2AwfwXNnd/ijvV0PmHbuibK3b7Dd2wUV5WV4W1KMrXMnwqL3QPQb78Ywvajx7gvwR+AahB/ZAyUVVUya+/+dKvdvXQ/LL3vDsmtvXD11GI8T/0Ppm9eIu3UNAGDTcwAGS1BBNW6WD/b/shYXj+6FoooqJs5ZLHgubOt6WHzZGxZde+Pv00eQnhSP0rdvEHer6majTc8B+Orbqayi12qI6w84tX0DbvzvvTa8xnvtzA5/mNZ4r/3u7YLy/73Xgv73XusvQe+1nbcyMKuXIUZZ6uJ1aSW23ahaWvJdDwNEZRTg3yeF6KSnjiEdW6CSD8jKAPczi3As7sNrQFlZc/oRVn5jBtfeRih+W44VJ+IBAMu+7ohrCS/wd8ILOJjp4NvOrVFRyYesDA8X43PwV4zkFYS/LJmAoX06oWVzDZz4dTaKit/C4puV+NXXCaev3cPpa/eQ9jQXP/12Gpd3V/0++vvfROw8+g/j5ETa8PjvzkskjaKoqAju7u74888/oa6uDi8vL5w+fVqwUfyzZ8/g4uKCiIgItGrVClu2bMHEiROxefNmODs7AwAWLFiA4OBgvH37FsOHD0f37t2xYsUK5OfnAwBWrFiB48ePIyYmBkDVVhP5+fmC7SwSEhIwbdo0xMbG4vXr10hNTYWRkREAICUlBe3atYOfnx98fHwgLp9Tjz7x/yHJ4mLHnVGVj1l/NZl1hAZlZ6DOOkKDMtSQzG6F9ZFf+v5tcLiotSo3Oxm+T4UU/fp/XvLm4y/ikPPxeR9/EYc8SpOe84k/9ifrCA3qdXQQ6wjvlfpCMn+ujVtIz+/palQQSpD+/fsLCkLWrl+/DgcHB2RkZKBly9rXgXwIFYSSiwpCyUYFoeSiglByUUEo2agglFySXBCmSWhBaCSFBSFNGSVC3r59i5ycHKxYsQJjx46tVzFICCGEEEII4QbadoIIOXDgANq2bYv8/Hz4+fmxjkMIIYQQQgj5jGiEUIJcvXqVdQQ4OzsL1igSQgghhBDCBHUZbTQ0QkgIIYQQQgghTRQVhIQQQgghhBDSRNGUUUIIIYQQQohE4dGc0UZDI4SEEEIIIYQQ0kRRQUgIIYQQQgghTRRNGSWEEEIIIYRIFB7NGG00NEJICCGEEEIIIU0UFYSEEEIIIYQQ0kTRlFFCCCGEEEKIRKEZo42HRggJIYQQQgghpImigpAQQgghhBBCmiiaMkoIIYQQQgiRKNRltPHQCCEhhBBCCCGENFFUEBJCCCGEEEJIE0VTRgkhhBBCCCEShuaMNhYaISSEEEIIIYSQJooKQkIIIYQQQghponh8Pp/POgQh9fH27VusW7cOixcvhqKiIus4n0yazkeazgWg85Fk0nQuAJ2PJJOmcwHofCSZNJ3Lp3iaX8o6Qq1aN1NgHaHBUUFIOKuwsBCampooKCiAhoYG6zifTJrOR5rOBaDzkWTSdC4AnY8kk6ZzAeh8JJk0ncunoIKw8dCUUUIIIYQQQghpoqjLKCGEEEIIIUSiUI/RxkMjhIQQQgghhBDSRFFBSDhLUVERy5cvl5oF19J0PtJ0LgCdjySTpnMB6HwkmTSdC0DnI8mk6VwIN1BTGUIIIYQQQohEySyQzKYy+prUVIYQQgghhBBCiJSggpAQQgghhBBCmijqMkoIIYQQQgiRKDzqM9poaISQEEIIIYQQQpooKggJZyxfvhyPHz9mHaPB7N69GyUlJaxjkHeUlZXB1dUVqamprKOQDygtLcWjR49QXl7OOgohhBDCadRllHCGjY0N7t+/j379+sHNzQ1jxozhdEvmli1b4vXr1xg7dizc3NzQs2dP1pHEcuLEiTq/duTIkZ8xScPT1NRETEwMjI2NWUf5LCoqKnDv3j20bdsWWlparOOIpaSkBHPnzkVoaCgAICEhASYmJpg7dy5at26NRYsWMU4ovuTkZOzevRvJycnYsmULdHV1cfbsWRgaGqJTp06s44nlypUrGDBgAOsY5D1ev34NPp8PFRUVAMDjx49x7NgxmJubY9CgQYzTNW0pKSkwMTFhHUOiZBWWsY5QKz0NedYRGhwVhIRToqOjsXv3bhw4cADl5eWYMGECXF1d8eWXX7KOJrby8nKcPHkSISEhOHv2LExMTODi4oJp06ZBT0+PdbyPkpERnmDA4/FQ8+OEx/v/uf8VFRWNlqshTJs2DTY2NvDw8GAdpUH88MMPsLS0hJubGyoqKtCvXz/cuHEDKioqOHXqFPr37886Yp3Nnz8fERER2Lx5M4YMGYK4uDiYmJjgr7/+wooVKxAdHc06oliuXbuGoUOHolevXvj7778RHx8PExMTrF+/Hnfv3sWRI0dYRxSLoqIi2rRpI/gsMzAwYB2J1DBo0CA4Ojpi1qxZyM/PR8eOHSEvL48XL14gICAA7u7urCN+UGBgYJ1fO2/evM+YpOHJyMgIbnh/++23UFJSYh2JOSoIGw8VhISTysrKcPLkSezevRvnz59Hx44d4ebmBmdnZ2hqarKOJ7bs7Gzs27cPoaGhePjwIYYMGQI3NzeMGDFCpPCSRBcvXsTChQuxdu1a9OjRAwBw8+ZNLF26FGvXrsVXX33FOKF4Vq9eDX9/fzg4OKBz585QVVUVep5rFxpt2rTB8ePH0aVLFxw/fhyzZ8/GlStXsHfvXly+fBkRERGsI9ZZ27ZtcfDgQXTv3h3q6uqIjY2FiYkJkpKSYGdnh8LCQtYRxdKjRw+MHTsWnp6eQudz+/ZtODo64smTJ6wjiuXFixfYu3cvQkND8eDBA9jb28PNzQ2jRo2CggK39u7S0tISurH1Pnl5eY2QpmG0aNEC165dQ6dOnbBz50788ssviI6OxtGjR+Hr64v4+HjWET+orrM2eDweUlJSPnOahhUTEyO44V1aWorx48fDzc0NXbt2ZR2NGSoIGw8VhISTSktLcezYMQQHB+Py5cvo2bMnnj17huzsbOzYsQPjx49nHVFskZGRCA4ORmhoKPT19fHy5UtoaWlh9+7dEj+CY2FhgW3btqF3795Cx69fv44ZM2ZI/EXGuz500cHFCw0lJSUkJSWhTZs2mDFjBlRUVLB582akpqbC2tqaU0WUiooK7t+/DxMTE6ECKjY2Fn379kVBQQHriGJRU1PDvXv3YGxsLHQ+aWlp6NixI968ecM6Yr1FRUUJLnABwMnJCW5ubrC2tmacrG6qpyUDAJ/Ph7u7O1atWgVdXV2h102bNq2xo9WbiooKHj58CENDQ4wbNw6dOnXC8uXLkZGRgQ4dOtC6dglQXl6OEydOICQkBOfOncMXX3wBV1dXTJkyBTo6OqzjNapsCS0IW0phQSj5Qw+E1PDvv/9izpw50NfXh4eHB2xtbREfH49r164hMTERa9as4dToTXZ2NjZu3IhOnTqhf//+KCwsxKlTp5CamoqnT59i3LhxnLjYSE5ORrNmzUSOa2pqIi0trdHzfKrU1NT3/uFaMQhUrVf977//UFFRgXPnzglGbEtKSiArK8s4nXi6dOmC06dPCx5Xj+Ds3LlTMDrNJc2aNUNmZqbI8ejoaLRu3ZpBooZjZ2eHxYsXY86cOSgqKkJwcDA6d+6MPn364MGDB6zjfdS0adMEf5ydnSEnJ4cxY8YIHefC53NN7du3x/Hjx5GRkYHz588L1g0+f/4cGhoajNPVH5/Ph7SMb8jJycHR0RGHDx/Gzz//jKSkJHh7e8PAwABTp06t9fOCkE9FBSHhDEtLS3Tv3h2pqanYtWsXMjIysH79erRv317wmokTJyInJ4dhyrobMWIEDAwMEBISgu+++w5Pnz7FgQMHMHDgQACAqqoqvLy8kJGRwTjpx3355Zfw9PREdna24Fh2djZ8fHya9HQXSeHi4oJx48bBwsICPB5P8B6LjIxEx44dGacTz9q1a/Hjjz/C3d0d5eXl2LJlCwYNGoTdu3djzZo1rOOJbcKECVi4cCGysrLA4/FQWVmJiIgIeHt7Y+rUqazj1UtZWRmOHDmCYcOGoW3btjh//jyCgoKQnZ2NpKQktG3bFmPHjmUds0ny9fWFt7c3jIyM0LVrV8FNlPDwcNja2jJOJ749e/bA0tISysrKUFZWhpWVFfbu3cs61ie5e/cuvv/+e+jr6yMgIADe3t5ITk7GhQsX8OzZM3zzzTesIxIpRFNGCWf89NNPcHV15fxd82pubm6YPn36B0c1+Hw+0tPT0bZt20ZMJr6kpCSMHj0aCQkJgiYSGRkZMDU1xfHjx4WKdq548uQJTpw4gfT0dJSWlgo9FxAQwChV/R05cgQZGRkYO3Ys2rRpA6BqSlyzZs04d4GRnJyM9evXIzY2FkVFRbCzs8PChQthaWnJOprYSktLMXv2bISEhKCiogJycnKoqKiAk5MTQkJCODeCO3fuXBw4cAB8Ph9TpkzB9OnTYWFhIfSarKwstGrVCpWVlYxS1k/NKb1clpWVhczMTFhbWwvWqN++fRsaGhqcukEUEBCAZcuWYc6cOejVqxcA4J9//sHWrVuxevVqzjUFCwgIwO7du/Ho0SMMGzYM06dPx7Bhw4T6CDx58gRGRkZNZrud568kc8qorrr0TRmlgpBwxqpVq+Dt7S1ol13t9evX2LBhA3x9fRklq589e/Zg/PjxIltnlJaWIiwsjHOjA3w+HxcuXMDDhw8BAGZmZhg4cGCdmjJImkuXLmHkyJEwMTHBw4cPYWFhgbS0NPD5fNjZ2eHy5cusI9bbmzdvqHudBEpPT8f9+/dRVFQEW1tbmJqaso5ULw4ODpg+fTocHR3fuy1QeXk5IiIi0K9fv0ZO92mkpSAEqm7iJScno2/fvlBWVgafz+fcZ7WxsTFWrlwp8rsyNDQUK1as4NxesqampnB1dYWzszP09fVrfU1paSkOHDjAuanK9UUFYeOhgpBwhqysLDIzM0UW9Ofm5kJXV5dzWxtI2/lIk65du2Lo0KFYuXKl4CJQV1cXkyZNwpAhQyS+Nfu7KioqsHbtWmzbtg3Z2dmCvfuWLVsGIyMjuLm5sY74QeI0veHyOihp8Pfff6Nnz56Qk5MTOl5eXo4bN26gb9++jJKJz9PTU+jx1q1bMXnyZJFO1lyaMZCbm4tx48bhypUr4PF4SExMhImJCVxdXaGlpQV/f3/WEetMSUkJ9+/fF5mBkpiYCEtLS841ZEpLS4OhoaFIZ3E+n4+MjAwYGhoySsYOFYSNR+7jLyFEMrzvDmZsbCy0tbUZJPo07zufJ0+ecGLrjMDAQMyYMQNKSkof3RuKS41+ACA+Pl7QGVFOTg6vX7+GmpoaVq1ahW+++YZzBeGaNWsQGhoKPz8/fPfdd4LjFhYW2Lx5s8QXhM2aNavz6AUXbqS8W2h8CJeKDQAYMGBArTe6CgoKMGDAAE78+1R7d0/Lnj17ijSV4tqomoeHB+Tl5ZGeng4zMzPB8fHjx8PT05NTBWH79u1x6NAh/Pjjj0LHDx48yMkR9nbt2tX6s5OXlwdjY2NO/ew0FB649fPFZVQQEolXvRcUj8fDF198IbLheVFREWbNmsUwoXhsbW0F5+Pg4CB0J72iogKpqakYMmQIw4R1s2nTJkyaNAlKSkrYtGnTe1/H4/E4VxCqqqoK1g3q6+sjOTkZnTp1AlC1zxrX7NmzB9u3b4eDg4PQz4q1tbVgiq8ku3LliuDrtLQ0LFq0CM7OzkJ7XoaGhmLdunWsIorl3UIjKioK5eXl6NChAwAgISEBsrKy6Ny5M4t4n+R9N7pyc3NF9vOUdDXfd9WqJ1VxrRCsFh4ejvPnzwvWEVczNTXF48ePGaWqn5UrV2L8+PH4+++/BWsIIyIicOnSJRw6dIhxOvG9b8JeUVERTfMnnx0VhETibd68GXw+H66urli5cqXQ6JmCggKMjIw41W5+1KhRAKo2oR08eDDU1NQEz1Wfz5gxYxilq7ua6zO4tlbjY7p3745//vkHZmZmGDZsGLy8vHDv3j38+eef6N69O+t4Ynv69GmtjX0qKytRViaZU3JqqrnWbNWqVQgICMDEiRMFx0aOHAlLS0ts376dE2trahYaAQEBUFdXR2hoKLS0tAAAL1++hIuLC/r06cMqotgcHR0BVBVKzs7OQusHKyoqEBcXh549e7KK98l27dqFTZs2ITExEUBVAfXDDz9g+vTpjJOJp7i4WGQdPlA1CvW+NZ+SasyYMYiMjMSmTZtw/PhxAFVr12/fvs2pjqnVMwZ4PB58fX2F/n0qKioQGRkJGxsbRulIU0EFIZF41Rd4xsbG6NmzJ+TluT13e/ny5QAAIyMjjB8/nu78SaCAgAAUFRUBqLoLXVRUJJiGxLUpfABgbm6O69evi3SrPXLkCKcunICq0cBt27aJHO/SpQvnLs4BwN/fH+Hh4YJiEKiaFbF69WoMGjQIXl5eDNPVXfWNOj6fD3V1dSgrKwueU1BQQPfu3YWmK3OJr68vAgICMHfuXKFRaQ8PD6Snp2PVqlWME9Zdnz59sGfPHvz0008AINjqxM/PDwMGDGCcTnydO3fGvn37WMf4JNUzBvh8Pu7duwcFBQXBcwoKCrC2toa3tzereGxxcyCek6ggJBKtsLBQ0CTC1tYWr1+/xuvXr2t9LdeaSXBhJKOuxowZg65du2LhwoVCx/38/HDnzh0cPnyYUbL6qdlFUFVVtdYChEt8fX0xbdo0PH36FJWVlfjzzz/x6NEj7NmzB6dOnWIdTywGBgbYsWMH/Pz8hI7v3LlTsOUJlxQWFta6d2pOTg5evXrFIFH97N69G0DVjS5vb2/OTQ/9kN9++w07duwQGZW2srLC3LlzOVUQ+vn5wcHBAXfv3kVpaSkWLFiABw8eIC8vDxEREazjia2yshJJSUl4/vy5yDYmXGlgVD1jwMXFBVu2bOHctQyRDtRllEi0mp04ZWRkal23Ub1mhQsLrrW1tZGQkIAWLVoI1ka+T15eXiMm+zQ6Ojq4fPmyyD5w9+7dw8CBA4U2rCdsXL9+HatWrRLau8/X1xeDBg1iHU0sZ86cwZgxY9C+fXt069YNQNUeaomJiTh69CiGDRvGOKF4pk6diuvXr8Pf3x9du3YFAERGRsLHxwd9+vRBaGgo44SkWbNmuHPnjkijkoSEBHTt2hX5+flsgtVTQUEBgoKChD4LZs+e/d6tDiTVrVu34OTkhMePH4usv+PKNQH5sJwiydxvUUdN+sbTqCAkEu3atWvo1asX5OTkcO3atQ++lgt7WoWGhmLChAlQVFRESEjIBwtCLo0gKisrIyYmRtAUo9rDhw8FI7tc8r5incfjQUlJCe3bt4ezszNcXFwYpCMZGRn47bffhPa8nDVrFidHCEtKSuDt7Y3g4GDBek45OTm4ublhw4YNnBhps7Ozw6VLl6ClpSVomvU+UVFRjZisYcydOxfy8vIi08W9vb3x+vVrbN26lVEy8aWnp8PAwKDWf6P09HRObW1gY2ODL774AitXroS+vr7IOXGhW7ejoyNCQkKgoaEhWIf7Pn/++WcjpZIcLyS0IGwhhQWh9J0RkSo1izwuFHwfU7PIc3Z2ZhekgVlaWuLgwYPw9fUVOh4WFgZzc3NGqerP19cXa9aswdChQwWjNrdv38a5c+cwe/ZspKamwt3dHeXl5ZxdF8VlBgYGWLt2LesYDUJFRQW//vorNmzYgOTkZABV7ee5UAhW++abbwQNSaqbZkmbXbt2ITw8XNBUKjIyEunp6Zg6darQNiKSvsbY2Nj4vfvfcm1rg8TERBw5cqTWhllcoampKShkuVDAEulFI4REosXFxdX5tVZWVp8xScOQ1g22T548CUdHRzg5OcHe3h4AcOnSJRw4cACHDx/m3EXimDFj8NVXX4lsZ/L7778jPDwcR48exS+//ILt27fj3r17jFJ+2MemJNck6dOT4+LiYGFhARkZmY9+JnDhc4BwS12brfB4PFy+fPkzp/k0MjIyyM7Oho6OjtDxx48fw9zcHMXFxYySic/e3h4LFizgxDZNpH5ohLDxUEFIJFr1usH37W1VExfubL5vHWRtuHA+NZ0+fRpr165FTEwMlJWVYWVlheXLl3NyZFdNTQ0xMTEid56TkpJgY2ODoqIiJCcnw8rKSmIvoGquPcvNzcXq1asxePBgoS6J58+fx7Jly+Dh4cEqZp3IyMggKytLaC1xbb+6uLJuSJqniWVkZIDH4wn2ubt9+zb2798Pc3NzzJgxg3G6pqt6FHPLli347rvvat3aQFZWVuIby9S8IZScnIylS5fCx8cHlpaWIh3I6eYQ9+UWS2ZB2FxV+gpC6TsjIlVq7m8XHR0Nb29v+Pj4CF3U+vv7i3QclFTStsF2TcOHD8fw4cNZx2gQ2traOHnypEihdPLkSWhrawOo2s9LXV2dRbw6qTk9ecyYMVi1ahXmzJkjODZv3jwEBQXh4sWLEl8QpqamCkY0pGHPS2meJubk5IQZM2ZgypQpyMrKwsCBA2FhYYE//vgDWVlZItPKSeOQlq0NbGxsRG4Iubq6Cr6ueQOZCzeHPrbmtiYurr8l3EEjhIQzunbtihUrVoh0ETxz5gyWLVuGf//9l1Gy+nFwcMD06dOFWpkDwP79+7F9+3ZcvXqVTTCCHTt2wN3dHcOGDROsIbxz5w7OnDmDbdu2wc3NDf7+/rh9+zYOHjzIOO3H1WXEUxrUZSYB+by0tLRw69YtdOjQAYGBgTh48CAiIiIQHh6OWbNmISUlhXXEJo3rWxs8fvy4zq99d99VSbRy5co6v7Z6D+OmhEYIGw8VhIQzlJWVERUVBTMzM6Hj8fHxsLOz41wnSxUVFcTGxtbaytzGxgYlJSWMkomvoqICmzZtwqFDh5Ceno7S0lKh5yV9jVptIiIiEBQUhEePHgEAOnTogLlz56Jnz56Mk4mvbdu2mDdvnsgm5/7+/ggMDBTrIos1Z2dnbN26VaTpSlpaGqZMmYLr168zSlY/Dx8+RMeOHWt97vz58xg8eHAjJ/o0ampquH//PoyMjDBy5Ej06tULCxcuRHp6Ojp06MC5z2lCCDt5xZI5yqutKvvZ/u68vDzMnTsXJ0+ehIyMDMaMGYMtW7ZATU3tg9938+ZNLFmyRDD928bGBufPn4eysnKd/rvSV+ISqWVmZoZ169Zh586dgukupaWlWLdunUiRyAXStMH2ypUrsXPnTnh5eWHp0qVYsmQJ0tLScPz4cc5OEevVqxd69erFOkaDWLlyJaZPn46rV68K9u6LjIzEuXPnsGPHDsbpxBMbGwsrKyvs27dPMNU6NDQU8+bNEzQ04hI7Ozts2LABs2fPFhx7+/YtvLy8sHPnTrx584ZhOvF16tQJ27Ztw/Dhw3HhwgX89NNPAIBnz56hefPmjNMRALh79+57b95xbc1qcnIyNm/ejPj4eACAubk55s+fj3bt2jFORkj9TJo0CZmZmbhw4QLKysrg4uKCGTNmYP/+/e/9nps3b2LIkCFYvHgxfvnlF8jJySE2NhYyMjJ1/u/SCCHhjNu3b2PEiBHg8/mCxeJxcXHg8Xg4efKkYGofV0jTBtvt2rVDYGAghg8fDnV1dcTExAiO3bp164MfZJIoPT39g89zaa+uapGRkQgMDBRcOJmZmWHevHmC9x5XlJWV4ccff0RgYCC8vLyQlJSEs2fPIiAggJNbgBw6dAju7u7o1q0bdu/ejczMTDg5OaGyshJ79+7Fl19+yTqiWK5evYrRo0ejsLAQ06ZNQ3BwMADgxx9/xMOHDzlXcEibsLAwTJ06FYMHD0Z4eDgGDRqEhIQEZGdnY/To0di9ezfriHV2/vx5jBw5EjY2NoKbdxEREYiNjcXJkyfx1VdfMU4oHmmcafOpmtoIYXx8PMzNzXHnzh106dIFAHDu3DkMGzYMT548QatWrWr9vu7du+Orr74S3ICrDyoICacUFxfjjz/+ENqQ2snJiVN7dtUkLRtsq6qqIj4+HoaGhtDX18fp06dhZ2eHlJQU2NraoqCggHVEsXysGywXmhVIu+XLl+Onn36CnJwcrl27Jhgt5KInT57AxcUF0dHRKC4uhrOzM/z9/YU6QXJJRUUFCgsLoaWlJTiWlpYGFRUVkf3vSOOysrLCzJkzMXv2bKirqyM2NhbGxsaYOXMm9PX1xVrTxpqtrS0GDx6M9evXCx1ftGgRwsPDOdeExdfX94MzbebNm8c6YqN7WSKZv2tVZMvx9u1boWOKioqC/VjrKzg4GF5eXnj58qXgWHl5OZSUlHD48GGMHj1a5HueP3+Oli1bIjAwEAcOHEBycjI6duyINWvWoHfv3nX+b9OUUcIpqqqqUtW6XFo22G7Tpg0yMzNhaGiIdu3aITw8HHZ2drhz584nf0CyUN2Rr1pZWRmio6MREBCANWvWMEolnsLCQkHjiI/tf8mlBhNlZWVYtGgRtm7disWLF+Off/6Bo6Mjdu3axalR9XeVlpaioqICFRUV0NfXh5KSEutI9SYrKytUDAKAkZERmzBESHJysqAbtIKCAoqLi8Hj8eDh4QF7e3tOFYTx8fE4dOiQyHFXV1ds3ry58QN9oj/++AM7duzA8OHDsWLFCkycOBHt2rWDlZUVbt261SQLQkm1bt06kZ+V5cuXY8WKFZ/091Zvr1STnJwctLW1kZWVVev3VDfqWrFiBTZu3AgbGxvs2bMHDg4OuH//vkifivehgpBItBMnTmDo0KGQl5fHiRMnPvjakSNHNlKq+pPWDbZHjx6NS5cuoVu3bpg7dy4mT56MXbt2IT09XeK3NKiNtbW1yLEuXbqgVatW2LBhw0f3jpMEWlpayMzMhK6uLpo1a1briCeX2rNX69KlC0pKSnD16lV0794dfD4ffn5+cHR0hKurK3799VfWEcUSFhYGd3d39OnTBwkJCYiJiYGLiwvOnz+PvXv3wsTEhHVEsWRnZ8Pb2xuXLl3C8+fPRfaL5NJ7TRppaWnh1atXAIDWrVvj/v37sLS0RH5+PqcamQGAjo4OYmJiRC54Y2JiODkSnZWVBUtLSwBVzZmqZ9Z8/fXXWLZsGcto5B2LFy8W7O1Z7UM3vxctWoSff/75g39n9XIOcVVWVgIAZs6cCRcXFwBVo+eXLl1CcHBwnbcxo4KQSLRRo0YJ7piMGjXqva/jykWtjY2N4Hxq20+pGlfOp1rNKTvjx49H27ZtcePGDZiammLEiBEMkzWsDh064M6dO6xj1Mnly5cFeybW3P+S67p06YLAwEDBNHEej4eFCxdi0KBBmDJlCuN04nNzc8PGjRvh7u4OAPjqq68QFxeHWbNmwcbG5qOju5LG2dkZ6enpWLZsGfT19WkbEAnTt29fXLhwAZaWlhg7dizmz5+Py5cv48KFC3BwcGAdTyzfffcdZsyYgZSUFEH354iICPz8888iF+tcIG0zbaSZuNNDvby84Ozs/MHXmJiYQE9PD8+fPxc6Xl5ejry8POjp6dX6ffr6+gCqGirVZGZm9tF+CDXRGkJCGtHjx49haGgIHo/30Vb/XNhDSVq9exHO5/ORmZmJFStW4OHDh4iJiWETrB7Ky8uxdu1auLq6ok2bNqzjfFZv377l3IXTo0eP0KFDh1qf27t3L+eKXHV1dVy/fh02Njaso5Ba5OXl4c2bN2jVqhUqKyvh5+cnuHm3dOlSkam+kozP52Pz5s3w9/fHs2fPAACtWrWCj48P5s2bx7mbEYsWLYKGhgZ+/PFHHDx4EJMnT4aRkZFgps27ayWbAkldQ6il8nmbyty9exedO3cGAISHh2PIkCHvbSrD5/PRpk0buLq6CjWVsbW1xdChQ+u8LIkKQkIIeUdtTWX4fD4MDAwQFhbGuQYm6urquHfvntSs47p27Ro2btwo1Grex8cHffr0YZys/v7991+h87Gzs2OcqH7Mzc3xxx9/wNbWlnUU0oRUT4NVV1dnnKTh3Lx5Ezdv3pS6mTbiaGoFIQAMHToU2dnZ2LZtm2DbiS5dugi6tT99+hQODg7Ys2ePoLv+5s2bsXz5cuzatQs2NjYIDQ3Fxo0bcf/+/TpvwUJTRglnzJs3D+3btxdZWB0UFISkpCTOLSJft24dWrZsCVdXV6HjwcHByMnJwcKFCxklI+9OsZSRkYGOjg7at28POTnufWza29vj2rVrUlEQ7tu3Dy4uLnB0dBR8FkRERMDBwQEhISFwcnJinFA8z58/x4QJE3D16lU0a9YMAJCfn48BAwYgLCwMOjo6bAOKafPmzVi0aBF+//13qXi/SaPKykokJSXh+fPngvVH1fr27csolfhSU1NRXl4OU1NToUIwMTER8vLynH//9ejRg3M3HxsaxwZ5G8Qff/yBOXPmwMHBQbAxfWBgoOD5srIyPHr0SGjN7w8//IA3b97Aw8MDeXl5sLa2xoULF8Taj5NGCAlntG7dGidOnBAMo1eLiorCyJEj8eTJE0bJ6sfIyAj79+8XrH2oFhkZiQkTJiA1NZVRMiJttm3bhpUrV2LSpEno3LmzyDYtXGjIVM3MzAwzZswQaVYUEBCAHTt21HthPivjx49HSkoK9uzZAzMzMwDAf//9h2nTpqF9+/Y4cOAA44Ti0dLSQklJCcrLy6GiogJ5eXmh55viXmqS5NatW3BycsLjx49F1q9zbe16v3794OrqimnTpgkd37dvH3bu3ImrV6+yCVZPe/bs+eDzU6dObaQkkiP/tWS+H5spf74RQlaoICScoaSkhPv376N9+/ZCx5OSkmBhYYE3b94wSlY/SkpKiI+Ph7GxsdDxlJQUmJubc+58pEloaChatGghaM++YMECbN++Hebm5jhw4ADn1nfKyMi89zmuXQQqKiriwYMHUvM5oKmpiYsXL4psQH/79m0MGjQI+fn5bILVU2ho6Aeff/finTQuGxsbfPHFF1i5cmWtTX80NTUZJROfhoYGoqKiav0s6NKlC+d+dt5dv1lWVoaSkhIoKChARUWlSd5MoYKw8XBv7hNpstq3b49z585hzpw5QsfPnj3LudbsQNUehBERESIFYURERK0LhyXZnTt3UFlZiW7dugkdj4yMhKysLLp06cIoWf2sXbsWv/32G4CqdRxBQUHYvHkzTp06BQ8PD/z555+ME4rn3WlhXGZgYIBLly6JXARevHgRBgYGjFLVX2VlpcgoGgDIy8tz8t+NCj7JlpiYiCNHjoj8/HARj8cTrB2sqaCggFM3uarV3Iy8WmJiItzd3eHj48MgEXs8NME5o4xQQUg4w9PTE3PmzEFOTg7s7e0BAJcuXYK/vz/n1g8CVS2zf/jhB5SVlQmdz4IFC+Dl5cU4nXhmz56NBQsWiBSET58+xc8//4zIyEhGyeonIyNDcMF0/PhxfPvtt5gxYwZ69eqF/v37sw3XxHl5eWHevHmIiYkRajUfEhKCLVu2ME4nPnt7e8yfPx8HDhwQ3Ah6+vQpPDw8OLcNQLXk5GTs3r0bycnJ2LJlC3R1dXH27FkYGhqiU6dOrOM1ad26dUNSUpJUFIR9+/bFunXrcODAAcjKVo3YVFRUYN26dejduzfjdA3D1NQU69evx+TJk/Hw4UPWcYgUo4KQcIarqyvevn2LNWvWCFrrGhkZ4bfffuPk3HofHx/k5ubi+++/R2lpKYCqaaQLFy7E4sWLGacTz3///VdrV0RbW1v8999/DBJ9GjU1NeTm5sLQ0BDh4eGCPa2UlJTw+vVrxunqR1o6c7q7u0NPTw/+/v44dOgQgKp1hQcPHsQ333zDOJ34goKCMHLkSBgZGQlGODMyMmBhYYF9+/YxTie+a9euYejQoejVqxf+/vtvrFmzBrq6uoiNjcWuXbtw5MgR1hGbnLi4OMHXc+fOhZeXl2AT9HdHp62srBo7Xr39/PPP6Nu3Lzp06CD4HLt+/ToKCwtx+fJlxukajpycnGBbDUI+F1pDSDgpJycHysrKUFNTYx3lkxUVFSE+Ph7KysowNTXl3D5qANC8eXOcOnVKpCPajRs3MHz48FqnwkiySZMm4eHDh7C1tcWBAweQnp6O5s2b48SJE/jxxx9x//591hHFUrMzZ69evQBUjaodO3aMk505pQ2fz8fFixcFIwBmZmYYOHAg41T106NHD4wdOxaenp5QV1dHbGwsTExMcPv2bTg6OnKu+Zc0qN5G532Xe9XPcW09MQA8e/YMQUFBiI2NhbKyMqysrDBnzhxoa2uzjia2EydOCD2u3v82KCgIBgYGOHv2LKNk7BS+kcxp8xpK71+Xz1VUEBJCPtnEiRORmZmJv/76S9CUID8/H6NGjYKurq5gJIcr8vPzsXTpUmRkZMDd3R1DhgwBACxfvhwKCgpYsmQJ44TikbbOnERyqamp4d69ezA2NhYqCNPS0tCxY0fONf2RBo8fP67za7nWMEuavNv8i8fjQUdHB/b29vD394e+vj6jZOxQQdh4qCAknHLkyBEcOnQI6enpgmmW1aKiohilqr+7d+++93y41Ljk6dOn6Nu3L3JzcwUbUsfExKBly5a4cOECJ5t9SBOud+bU1tZGQkICWrRoAS0tLZHOiDVxoRNfYGAgZsyYASUlJaH9pWrz7r6rkq5NmzY4dOgQevbsKVQQHjt2DN7e3khOTmYdkXBYzemvH8Ol6a+kdlQQNh5aQ0g4IzAwEEuWLIGzszP++usvuLi4IDk5GXfu3MHs2bNZxxNbWFgYpk6disGDByM8PByDBg1CQkICsrOzMXr0aNbxxNK6dWvExcXhjz/+EEzdcXFxwcSJE2vtoEgaF9c7c27atEmw8TQXG0i9a9OmTZg0aRKUlJSwadOm976Ox+NxriCcMGECFi5ciMOHD4PH46GyshIRERHw9vbm5FpvafTo0SP88ssvgpkBZmZmmDt3Ljp06MA42cfZ2Nh8cPprNS5Of61eq14XAQEBnzGJ5KAeo42HRggJZ3Ts2BHLly/HxIkThe48+/r6Ii8vD0FBQawjisXKygozZ87E7NmzBedjbGyMmTNnQl9fHytXrmQdkUiJ3377DT/88ANcXV1r7cw5c+ZMxgmJtCgtLcXs2bMREhKCiooKyMnJoby8HJMmTUJISIigGyRh4+jRo5gwYQK6dOkiWPN969Yt3LlzB2FhYRgzZgzjhB8mzdNfBwwYgKioKJSXlwuK84SEBMjKygo1bePxeFLVNOdDXknoCKG6FI4QUkFIOENFRQXx8fFo27YtdHV1ceHCBVhbWyMxMRHdu3dHbm4u64hiUVVVxYMHD2BkZITmzZvj6tWrsLS0RHx8POzt7ZGZmck64gedOHECQ4cOhby8vMhi+HeNHDmykVKR9zl27Bj8/f2FRgV8fHw40ZmzsLCwzq/V0ND4jElIXWVkZODevXsoKiqCra0tTE1NWUciANq1a4dJkyZh1apVQseXL1+Offv2cXJK73///Sey7ILH42HEiBEMU4kvICAAV69eRWhoqGCT+pcvX8LFxQV9+vTh3HZUDYEKwsZDBSHhDBMTExw9ehS2trbo0qULvvvuO8ycORPh4eGYMGECJ9YO1dSmTRucPXsWlpaWsLKywuLFizFx4kTcvHkTQ4YMQUFBAeuIHyQjI4OsrCzo6uqKLIaviYtTd4hkqe6SWBdceK9J29QwaTsfaaaiooK4uDiR6eOJiYmwtrZGSUkJo2TiS0lJwejRo3Hv3j2haaTVnxVc+CyoqXXr1ggPDxfZq/P+/fsYNGhQk9x64tVbCS0IFaWvIKQ1hIQz7O3tceLECdja2sLFxQUeHh44cuQI7t69C0dHR9bxxNa3b19cuHABlpaWGDt2LObPn4/Lly/jwoULnNiQurKystavCWloV65cEXydlpaGRYsWwdnZWTDl7ebNmwgNDcW6detYRRRLdHS00OP3TRPr3Lkzi3hik7bzkWb9+/fH9evXRQrCf/75h3N7ks6fPx/Gxsa4dOkSjI2NERkZiby8PHh5eWHjxo2s44mtsLAQOTk5IsdzcnLw6tUrBolIU0IjhIQzKisrUVlZCTm5qvsYYWFhuHHjBkxNTTFz5kwoKCgwTiievLw8vHnzBq1atUJlZSX8/PwE57N06VLBlBFJV1ZWhiFDhmDbtm2cnhZma2tb51EoLnS0/Vg3zpq4NLru4OCA6dOnY+LEiULH9+/fj+3bt+Pq1atsgtWTtE0Tk7bzkTbbtm2Dr68vxo0bh+7duwOoWkN4+PBhrFy5Eq1atRK8VtKn+rdo0QKXL1+GlZUVNDU1cfv2bXTo0AGXL1+Gl5eXyI0KSTd16lRcv34d/v7+6Nq1KwAgMjISPj4+6NOnD0JDQxknbHw0Qth4qCAkhHwyHR0dQTHLVeI08Vm+fPlnTNIwxLl4mDZt2mdM0rBUVFQQGxsr8l5LSEiAjY0Np6a8AdI3TUzazkfafGh6f01cmOqvpaWFqKgoGBsbo127dti5cycGDBiA5ORkWFpacu6zoKSkBN7e3ggODkZZWRkAQE5ODm5ubtiwYQNUVVUZJ2x8RW8ls0RRU5S+/qc0ZZQQ8skmT56MXbt2Yf369ayj1BsXijxxcKnIE4eBgQF27NgBPz8/oeM7d+7kxBYa75K2aWLSdj7SRpqm91tYWAi6c3fr1g1+fn5QUFDA9u3bYWJiwjqe2FRUVPDrr79iw4YNguY+7dq1a5KFIGl8VBASQj5ZeXk5goODcfHiRXTu3FnkFxg1kmCvsrISSUlJeP78uchFYd++fRmlEt+mTZswZswYnD17Ft26dQMA3L59G4mJiTh69CjjdOIbPXo0XFxcap0mxsW10dJ2PkRyLV26FMXFxQCAVatW4euvv0afPn3QvHlzHDx4kHG6+lNVVYWVlRXrGKSJoSmjhJBPNmDAgA8+X7MpCBdUVFRg06ZNOHTokEg7c4Bba+6AqjVCTk5OePz4sciGzlyYGvauJ0+e4LfffhPaQmPWrFmcHCGUtmli0nY+0iAwMLDOr503b95nTPL55eXlibV+mki24lLJLFFUFaTv/UUFISGEvMPX1xc7d+6El5cXli5diiVLliAtLQ3Hjx+Hr68v5y6abGxs8MUXX2DlypXQ19cXuVjS1NRklIxUKy4ulqppYtJ2PlxmbGxcp9fxeDykpKR85jSE1B0VhI2HCkJCGEtKSkJycjL69u0LZWVl8Pl8zt3ddHV1xZYtW6Curi50vLi4GHPnzkVwcDCjZPXTrl07BAYGYvjw4VBXV0dMTIzg2K1bt7B//37WEcWiqqqK2NhYkVbzhBBCiKSigrDxUEFIJJq0bQVQU25uLsaPH4/Lly+Dx+MhMTERJiYmcHV1hZaWFvz9/VlHrDNZWVlkZmZCV1dX6PiLFy+gp6eH8vJyRsnqR1VVFfHx8TA0NIS+vj5Onz4NOzs7pKSkwNbWFgUFBawjisXe3h4LFizAkCFDWEchhBBC6qREQgtCFSksCKmpDJFoo0aNEnz95s0b/PrrrzA3NxdsSH3r1i08ePAA33//PaOE9efh4QE5OTmkp6fDzMxMcHz8+PHw9PTkREFYWFgIPp8PPp+PV69eQUlJSfBcRUUFzpw5I1IkckGbNm2QmZkJQ0NDtGvXDuHh4bCzs8OdO3egqKjIOl6dxMXFCb6eO3cuvLy8kJWVBUtLS8jLywu9lhoYENI0uLq6fvB5rs3mIIQ0DCoIiUSruRXA9OnTMW/ePPz0008ir8nIyGjsaJ8sPDwc58+fR5s2bYSOm5qa4vHjx4xSiadZs2bg8Xjg8Xj44osvRJ7n8Xhi7e8nKUaPHo1Lly6hW7dumDt3rmBbjfT0dHh4eLCOVyc2Njbg8XhCTWRqXgxWP8elpjJ8Ph8ZGRnQ1dUVuvlACKmbly9fCj0uKyvD/fv3kZ+fD3t7e0apCCGs0ZRRwhmampq4e/euyIbUiYmJ6NKlC+em8amrqyMqKgqmpqZQV1dHbGwsTExMcPfuXQwePBi5ubmsI37UtWvXwOfzYW9vj6NHj0JbW1vwnIKCAtq2bYtWrVoxTNgwbt68iZs3b8LU1BQjRoxgHadOxLmp0LZt28+YpOFUVlZCSUkJDx48EPkc4KKysjLMnDkTy5Ytq3PjD0IaWmVlJdzd3dGuXTssWLCAdRxCBErKJLNEUZGXvimjVBASztDT08P69evh7OwsdDwkJAQLFy5EdnY2m2D1NGzYMHTu3Bk//fQT1NXVERcXh7Zt22LChAmorKzEkSNHWEess8ePH8PQ0JBzzXCainXr1qFly5Yi08WCg4ORk5ODhQsXMkomvk6dOmHXrl3o3r076ygNQlNTEzExMVQQEqYePXqE/v37IzMzk3UUQgSoIGw8NGWUcMYPP/wAd3d3REVFCW14HBwcjGXLljFOJz4/Pz84ODjg7t27KC0txYIFC/DgwQPk5eUhIiKCdbyPiouLg4WFBWRkZFBQUIB79+6997VcW6O2Z8+eDz4/derURkrSMH7//fdaO6N26tQJEyZM4FRBuH79evj4+OC3336DhYUF6zifbNSoUTh+/DhnpiIT6ZScnMy55l+EkIZDI4SEUw4dOoQtW7YIbUg9f/58jBs3jnGy+ikoKEBQUBBiY2NRVFQEOzs7zJ49G/r6+qyjfZSMjAyysrKgq6sLGRkZkfVq1bi0Rq2alpaW0OOysjKUlJRAQUEBKioqnNuYXklJCfHx8SKjUCkpKTA3N8ebN28YJROflpYWSkpKUF5eDgUFBSgrKws9z7V/m9WrV8Pf3x8ODg7o3LmzyH59XNvzkkg2T09Pocd8Ph+ZmZk4ffo0pk2bhqCgIEbJCBH1uox1gtopy3/8NVxDBSEhpF5qThP92Ho1rqxR+5DExES4u7vDx8cHgwcPZh1HLKampli+fDkmT54sdHzv3r1Yvnw5pzajDg0N/eDz06ZNa6QkDeNDU0Vpo3DS0AYMGCD0WEZGBjo6OrC3t4erqyvk5GjiGJEcVBA2HioICafk5+fjyJEjSElJgbe3N7S1tREVFYWWLVuidevWrON9VM2tAD6Ga9Msm4K7d+9i8uTJePjwIesoYvHz84Ofnx82bNgg6CR46dIlLFiwAF5eXli8eDHjhISQxlBSUgI+ny8YiU5LS8Px48dhZmbGuRtdRPpRQdh46FYQ4Yy4uDgMHDgQmpqaSEtLw/Tp06GtrY0///wT6enpH133JQlq2wqgNlybZilNTUs+RE5ODs+ePWMdQ2w+Pj7Izc3F999/j9LSUgBV00gXLlzIuWIwPT39g88bGho2UhJCuGfUqFFwdHTErFmzkJ+fj+7du0NeXh4vXrxAQEAA3N3dWUckRID61DUeGiEknDFw4EDY2dnBz89PaJuGGzduwMnJCWlpaawjfpQ0bgUAAEZGRti/fz969uwpdDwyMhITJkxAamoqo2T1c+LECaHH1etsgoKCYGBggLNnzzJK9mmKiooQHx8PZWVlmJqaQlFRkXUksVWvV30fLt1IAWijcNK4WrRogWvXrqFTp07YuXMnfvnlF0RHR+Po0aPw9fUVrM8nRBK8kdA+R0pSOJwmhadEpNWdO3fw+++/ixxv3bo1srKyGCQSH5eKPHFkZWXV2ghHR0eHk23MR40aJfSYx+MJ1tn4+/uzCdUA1NTU8OWXX7KO8Umio6OFHpeVlSE6OhoBAQFYs2YNo1T1RxuFk8ZUUlICdXV1AEB4eDgcHR0hIyOD7t27i3XDkhAiXaggJJyhqKiIwsJCkeMJCQnQ0dFhkEh8J06cwNChQyEvLy8yCvWukSNHNlKqT2dgYICIiAiRBhkRERGc3Ji+srKSdQTyHtbW1iLHunTpglatWmHDhg1wdHRkkKr+jh07JnKs5kbhhDSk9u3b4/jx4xg9ejTOnz8v2O7k+fPn0NDQYJyOEGHSOBInqWjKKOGM6dOnIzc3F4cOHYK2tjbi4uIgKyuLUaNGoW/fvti8eTPriB/17lYN78O1NYTUtISwlpSUBGtraxQXF7OO0iBoo3DyORw5cgROTk6oqKiAg4MDwsPDAVStA//77785Ox2eEPJpqCAknFFQUIBvv/0Wd+/exatXr9CqVStkZWWhR48eOHPmjMj+XaTx8Pl8LFq0CIGBgSJNS3x9fRmnq5t39+f6kICAgM+YhHzIu7MEqtd3rlixAg8fPkRMTAybYA3szJkzmDZtGnJyclhHIVImKysLmZmZsLa2FtyYvH37NjQ0NNCxY0fG6QghLFBBSDgnIiJCaCP3gQMHso5UL3v27MH48eNFGnuUlpYiLCwMU6dOZZSs/rjctOTd/bmioqJQXl6ODh06AKiamiwrK4vOnTvj8uXLLCIS1N5Uhs/nw8DAAGFhYejRowejZPVDG4UTQghhjQpCwhkPHz58793L8+fPc24PJVlZWWRmZkJXV1foeG5uLnR1dTk1ZVTaBAQE4OrVqwgNDYWWlhaAquYfLi4u6NOnD7y8vBgnbLquXbsm9Lh6Y+327dtzclPt/v37CxW4tFE4IYSQxkYFIeEMFRUVbNiwAbNnzxYce/v2Lby8vLBz5068efOGYTrxycjIIDs7W6QhTmxsLAYMGIC8vDxGyUjr1q0RHh6OTp06CR2/f/8+Bg0axMm9CLnMzs4Oly5dgpaWFlatWgVvb2+oqKiwjlVvNZtLEUIIIazRrUfCGSEhIXB3d8fp06exe/duZGZmwsnJCZWVlbh+/TrreHVma2sLHo8HHo8HBwcHoRGAiooKpKamYsiQIQwTksLCwlrXbuXk5ODVq1cMEjVt8fHxKC4uhpaWFlauXAl3d3dOF4SjR49GVlYWdHR03jtTgBBCCGksVBASzhg3bhx69uwJFxcXdOrUCcXFxXB2doa/vz+nLg6r97iLiYnB4MGDoaamJnhOQUEBRkZGGDNmDKN0BKi6YHdxcYG/vz+6du0KAIiMjISPjw/ntjWQBjY2NnBxcUHv3r3B5/OxYcMGoZ+bmrjQxEhHRwe3bt3CiBEjwOfzRdZEEkIIIY2JCkLCOaWlpaioqEBFRQX09fWhpKTEOpJYli9fDgAwMjLC+PHjOZe/Kdi2bRu8vb3h5OSEsrIyAICcnBzc3NywYcMGxumanpCQECxfvhynTp0Cj8fD2bNna11bx+PxOFEQzpo1C998841gpoCent57X0triQkhhHxutIaQcEZYWBjc3d3Rp08f7Nq1CzExMXBxcUHbtm2xd+9emJiYsI5IpExxcTGSk5MBAO3ataOtTSRAzb08uezhw4dISkrCyJEjsXv3bjRr1qzW133zzTeNG4wQQkiTQwUh4QxVVVVs3LgR7u7ugmMvX77EzJkzce7cOZH9ySRdRUUFNm3ahEOHDiE9PV2wf181aipDiPRbuXIlfHx8ODXtnRBCiHShgpBwxqNHjwR7wr1r7969mDJlSiMn+jS+vr7YuXMnvLy8sHTpUixZsgRpaWk4fvw4fH19MW/ePNYRmxRHR0eEhIRAQ0Pjo+sE//zzz0ZKRYCqrpx1NXLkyM+YhBBCCJE+tIaQcMb7ikEAnCsGAeCPP/7Ajh07MHz4cKxYsQITJ05Eu3btYGVlhVu3blFB2Mg0NTUFzT00NTUZpyE1VTdi+hgej8eJNXfVnYbrIioq6jOnIYQQ0tRRQUgkmqenJ3766SeoqqrC09Pzg68NCAhopFQNIysrC5aWlgAANTU1FBQUAAC+/vprLFu2jGW0Jmn37t21fk3Yq6ysZB2hQdW1wCWEEEIaAxWERKJFR0cLujxGRUW99646F9u2t2nTBpmZmTA0NES7du0QHh4OOzs73LlzB4qKiqzjNWmvX78Gn88XrOt6/Pgxjh07BnNzcwwaNIhxOsJ11Z2GCSGEEElAawiJRIuLi4OFhQVkZGRYR2lwixYtgoaGBn788UccPHgQkydPhpGREdLT0+Hh4YH169ezjthkDRo0CI6Ojpg1axby8/PRoUMHKCgo4MWLFwgICBBqbEQa16pVqz74PBe2nSCEEEIkCRWERKLJysoiMzMTurq6MDExwZ07d9C8eXPWsT6Lmzdv4ubNmzA1NcWIESNYx2nSWrRogWvXrqFTp07YuXMnfvnlF0RHR+Po0aPw9fVFfHw864hNlq2trdDjsrIypKamQk5ODu3atePcmjsZGZkPznDgwppIQggh3EZTRolEa9asGVJTU6Grq4u0tDSpW0tUU48ePdCjRw/WMQiAkpISqKurAwDCw8Ph6OgIGRkZdO/eHY8fP2acrmmLjo4WOVZYWAhnZ2eMHj2aQaJPc+zYMaHHZWVliI6ORmhoKFauXMkoFSGEkKaERgiJRJsxYwb27NkDfX19pKeno02bNpCVla31tSkpKY2cTnzUPp8brKysMH36dIwePRoWFhY4d+4cevTogX///RfDhw9HVlYW64jkHffu3cOIESOQlpbGOkqD2L9/Pw4ePIi//vqLdRRCCCFSjkYIiUTbvn07HB0dkZSUhHnz5uG7774TjNxwkbS1z5dWvr6+cHJygoeHB+zt7QUjt+Hh4SJTFolkKCgoEHTqlQbdu3fHjBkzWMcghBDSBNAIIeEMFxcXBAYGcrogJNyRlZWFzMxMWFtbC5oa3b59GxoaGujYsSPjdE1XYGCg0GM+n4/MzEzs3bsX/fr1w/79+xklazivX7/G4sWLcfbsWTx69Ih1HEIIIVKOCkJCCHmPpKQkJCcno2/fvlBWVgafz+fkFifSxNjYWOixjIwMdHR0YG9vj8WLF3PuhpGWlpbQe4rP5+PVq1dQUVHBvn37aOo4IYSQz44KQkIYunbtGjZu3CjoWmlubg4fHx/06dOHcbKmLTc3F+PGjcOVK1fA4/GQmJgIExMTuLq6QktLC/7+/qwjEikREhIiVBBWF7jdunWDlpYWw2SEEEKaCioICWFk3759cHFxgaOjI3r16gUAiIiIwLFjxxASEgInJyfGCZuuqVOn4vnz59i5cyfMzMwQGxsLExMTnD9/Hp6ennjw4AHriOR/CgsLcfnyZXTo0AFmZmas4xBCCCGcQwUhIYyYmZlhxowZ8PDwEDoeEBCAHTt20F53DOnp6eH8+fOwtraGurq6oCBMSUmBlZUVioqKWEdsssaNG4e+fftizpw5eP36NaytrZGWlgY+n4+wsDCMGTOGdUSxnDt3DmpqaujduzcAYOvWrdixYwfMzc2xdetWGiUkhBDy2cmwDkBIU5WSklLrBvQjR45Eamoqg0SkWnFxMVRUVESO5+XlQVFRkUEiUu3vv/8WTKk+duwY+Hw+8vPzERgYiNWrVzNOJz4fHx8UFhYCqNo6w9PTE8OGDUNqaio8PT0ZpyOEENIUUEFICCMGBga4dOmSyPGLFy/CwMCAQSJSrU+fPtizZ4/gMY/HQ2VlJfz8/DBgwACGyUhBQQG0tbUBVI2ujRkzBioqKhg+fDgSExMZpxNfamoqzM3NAQBHjx7FiBEjsHbtWmzduhVnz55lnI4QQkhTQPsQEsKIl5cX5s2bh5iYGPTs2RNA1RrCkJAQbNmyhXG6ps3Pzw8ODg64e/cuSktLsWDBAjx48AB5eXmIiIhgHa9JMzAwwM2bN6GtrY1z584hLCwMAPDy5UsoKSkxTic+BQUFlJSUAKi6GTR16lQAgLa2tmDkkBBCCPmcqCAkhBF3d3fo6enB398fhw4dAlC1rvDgwYP45ptvGKdr2iwsLJCQkICgoCCoq6ujqKgIjo6OmD17NvT19VnHa9J++OEHTJo0CWpqamjbti369+8PoGoqqaWlJdtw9dC7d294enqiV69euH37Ng4ePAgASEhIQJs2bRinI4QQ0hRQUxlCCKmhrKwMQ4YMwbZt22Bqaso6DqnFv//+i/T0dHz11VdQU1MDAJw+fRrNmjUTdOzlivT0dHz//ffIyMjAvHnz4ObmBgDw8PBARUUFAgMDGSckhBAi7aggJISR6dOnY/LkyYIRDiI5dHR0cOPGDSoICSGEECL1qKkMIYzk5ORgyJAhMDAwgI+PD2JiYlhHIv8zefJk7Nq1i3UMQgghhJDPjkYICWHo5cuXOHz4MPbv34/r16+jY8eOmDRpEpycnGBkZMQ6XpM1d+5c7NmzB6ampujcuTNUVVWFng8ICGCUjBBCCCGkYVFBSIiEePLkCQ4cOIDg4GAkJiaivLycdaQm60NbS/B4PFy+fLkR0xBCCCGEfD7UZZQQCVBWVoa7d+8iMjISaWlpaNmyJetITdqVK1dYRyCEEEIIaRS0hpAQhq5cuYLvvvsOLVu2hLOzMzQ0NHDq1Ck8efKEdTRCJNb169cxefJk9OjRA0+fPgUA7N27F//88w/jZIQQQgj30AghIYy0bt0aeXl5GDJkCLZv344RI0ZAUVGRdSxCJNrRo0cxZcoUTJo0CdHR0Xj79i0AoKCgAGvXrsWZM2cYJ/w4R0fHOr/2zz///IxJCCGEECoICWFmxYoVGDt2LJo1a8Y6CiGcsXr1amzbtg1Tp05FWFiY4HivXr2wevVqhsnqTlNTk3UEQgghRICayhBCCOEMFRUV/PfffzAyMoK6ujpiY2NhYmKClJQUmJub482bN6wjEkIIIZxCawgJIYRwhp6eHpKSkkSO//PPPzAxMWGQiBBCCOE2mjJKCCGEM7777jvMnz8fwcHB4PF4ePbsGW7evAlvb28sW7aMdbx6OXLkCA4dOoT09HSUlpYKPRcVFcUoFSGEkKaCRggJIYRwxqJFi+Dk5AQHBwcUFRWhb9++mD59OmbOnIm5c+eyjie2wMBAuLi4oGXLloiOjkbXrl3RvHlzpKSkYOjQoazjEUIIaQJoDSEhhBDOKS0tRVJSEoqKimBubg41NTXWkeqlY8eOWL58OSZOnCi0JtLX1xd5eXkICgpiHZEQQoiUoxFCQgghnJOeno6MjAxYWlpCTU0NXL23mZ6ejp49ewIAlJWV8erVKwDAlClTcODAAZbRCCGENBFUEBJCCOGM3NxcODg44IsvvsCwYcOQmZkJAHBzc4OXlxfjdOLT09NDXl4eAMDQ0BC3bt0CAKSmpnK2yCWEEMItVBASQgjhDA8PD8jLyyM9PR0qKiqC4+PHj8e5c+cYJqsfe3t7nDhxAgDg4uICDw8PfPXVVxg/fjxGjx7NOB0hhJCmgNYQEkII4Qw9PT2cP38e1tbWIvsQWllZoaioiHVEsVRWVqKyshJyclVNv8PCwnDjxg2Ymppi5syZUFBQYJyQEEKItKNtJwghhHBGcXGx0Mhgtby8PCgqKjJI9GmePHkCAwMDweMJEyZgwoQJ4PP5yMjIgKGhIcN0hBBCmgKaMkoIIYQz+vTpgz179gge83g8VFZWws/PDwMGDGCYrH6MjY2Rk5MjcjwvLw/GxsYMEhFCCGlqaISQEEIIZ/j5+cHBwQF3795FaWkpFixYgAcPHiAvLw8RERGs44mNz+eDx+OJHC8qKoKSkhKDRIQQQpoaKggJIYRwhoWFBRISEhAUFAR1dXUUFRXB0dERs2fPhr6+Put4debp6QmgaoRz2bJlQtNgKyoqEBkZCRsbG0bpCCGENCVUEBJCCOGEsrIyDBkyBNu2bcOSJUtYx/kk0dHRAKpGCO/duyfUPEZBQQHW1tbw9vZmFY8QQkgTQgUhIYQQTpCXl0dcXBzrGA3iypUrAKq2mtiyZQs0NDQYJyKEENJU0bYThBBCOMPDwwOKiopYv3496ygN7smTJwCANm3aME5CCCGkKaERQkIIIZxRXl6O4OBgXLx4EZ07d4aqqqrQ8wEBAYyS1U9lZSVWr14Nf39/wR6K6urq8PLywpIlSyAjQ83ACSGEfF5UEBJCCOGM+/fvw87ODgCQkJAg9Fxt3Tol3ZIlS7Br1y6sX78evXr1AgD8888/WLFiBd68eYM1a9YwTkgIIUTa0ZRRQgghEi0uLg4WFhZSOVrWqlUrbNu2DSNHjhQ6/tdff+H777/H06dPGSUjhBDSVEjfb1dCCCFSxdbWFi9evAAAmJiYIDc3l3GihpOXl4eOHTuKHO/YsSPy8vIYJCKEENLUUEFICCFEojVr1gypqakAgLS0NFRWVjJO1HCsra0RFBQkcjwoKAjW1tYMEhFCCGlqaA0hIYQQiTZmzBj069cP+vr64PF46NKlC2RlZWt9bUpKSiOn+zR+fn4YPnw4Ll68iB49egAAbt68iYyMDJw5c4ZxOkIIIU0BrSEkhBAi8c6dO4ekpCTMmzcPq1atgrq6eq2vmz9/fiMn+3TPnj3D1q1b8fDhQwCAmZkZvv/+e7Rq1YpxMkIIIU0BFYSEEEI4w8XFBYGBge8tCLkmPT0dBgYGtXZITU9Ph6GhIYNUhBBCmhIqCAkhhBBGZGVlkZmZCV1dXaHjubm50NXVRUVFBaNkhBBCmgpqKkMIIYQwwufzax0dLCoqgpKSEoNEhBBCmhpqKkMIIYQ0Mk9PTwAAj8fDsmXLoKKiIniuoqICkZGRsLGxYZSOEEJIU0IFISGEENLIoqOjAVSNEN67dw8KCgqC5xQUFGBtbQ1vb29W8QghhDQhtIaQEEIIYcTFxQVbtmyBhoYG6yiEEEKaKCoICSGEEEIIIaSJoqYyhBBCCCGEENJEUUFICCGEEEIIIU0UFYSEEEIIIYQQ0kRRQUgIIYQQQgghTRQVhIQQQgghhBDSRFFBSAghhBBCCCFNFBWEhBBCCCGEENJE/R/h6utJtr6X+QAAAABJRU5ErkJggg==",
            "text/plain": [
              "<Figure size 1000x1000 with 2 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "plt.figure(figsize=(10,10))\n",
        "sns.heatmap(correlation, cbar=True, square=True, fmt = '.1f', annot = True, annot_kws={'size':8}, cmap = 'Blues')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "P8AqGg1zr69_"
      },
      "source": [
        "Data Preprocessing"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "id": "uqi_YdKGrG1P"
      },
      "outputs": [],
      "source": [
        "x = data.drop('quality',axis=1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x510k7kjsMfZ",
        "outputId": "8ebdd146-992e-401a-b9aa-a849d31139df"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fixed acidity</th>\n",
              "      <th>volatile acidity</th>\n",
              "      <th>citric acid</th>\n",
              "      <th>residual sugar</th>\n",
              "      <th>chlorides</th>\n",
              "      <th>free sulfur dioxide</th>\n",
              "      <th>total sulfur dioxide</th>\n",
              "      <th>density</th>\n",
              "      <th>pH</th>\n",
              "      <th>sulphates</th>\n",
              "      <th>alcohol</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>7.4</td>\n",
              "      <td>0.700</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.076</td>\n",
              "      <td>11.0</td>\n",
              "      <td>34.0</td>\n",
              "      <td>0.99780</td>\n",
              "      <td>3.51</td>\n",
              "      <td>0.56</td>\n",
              "      <td>9.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>7.8</td>\n",
              "      <td>0.880</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.6</td>\n",
              "      <td>0.098</td>\n",
              "      <td>25.0</td>\n",
              "      <td>67.0</td>\n",
              "      <td>0.99680</td>\n",
              "      <td>3.20</td>\n",
              "      <td>0.68</td>\n",
              "      <td>9.8</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>7.8</td>\n",
              "      <td>0.760</td>\n",
              "      <td>0.04</td>\n",
              "      <td>2.3</td>\n",
              "      <td>0.092</td>\n",
              "      <td>15.0</td>\n",
              "      <td>54.0</td>\n",
              "      <td>0.99700</td>\n",
              "      <td>3.26</td>\n",
              "      <td>0.65</td>\n",
              "      <td>9.8</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>11.2</td>\n",
              "      <td>0.280</td>\n",
              "      <td>0.56</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.075</td>\n",
              "      <td>17.0</td>\n",
              "      <td>60.0</td>\n",
              "      <td>0.99800</td>\n",
              "      <td>3.16</td>\n",
              "      <td>0.58</td>\n",
              "      <td>9.8</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>7.4</td>\n",
              "      <td>0.700</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.9</td>\n",
              "      <td>0.076</td>\n",
              "      <td>11.0</td>\n",
              "      <td>34.0</td>\n",
              "      <td>0.99780</td>\n",
              "      <td>3.51</td>\n",
              "      <td>0.56</td>\n",
              "      <td>9.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1594</th>\n",
              "      <td>6.2</td>\n",
              "      <td>0.600</td>\n",
              "      <td>0.08</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.090</td>\n",
              "      <td>32.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>0.99490</td>\n",
              "      <td>3.45</td>\n",
              "      <td>0.58</td>\n",
              "      <td>10.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1595</th>\n",
              "      <td>5.9</td>\n",
              "      <td>0.550</td>\n",
              "      <td>0.10</td>\n",
              "      <td>2.2</td>\n",
              "      <td>0.062</td>\n",
              "      <td>39.0</td>\n",
              "      <td>51.0</td>\n",
              "      <td>0.99512</td>\n",
              "      <td>3.52</td>\n",
              "      <td>0.76</td>\n",
              "      <td>11.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1596</th>\n",
              "      <td>6.3</td>\n",
              "      <td>0.510</td>\n",
              "      <td>0.13</td>\n",
              "      <td>2.3</td>\n",
              "      <td>0.076</td>\n",
              "      <td>29.0</td>\n",
              "      <td>40.0</td>\n",
              "      <td>0.99574</td>\n",
              "      <td>3.42</td>\n",
              "      <td>0.75</td>\n",
              "      <td>11.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1597</th>\n",
              "      <td>5.9</td>\n",
              "      <td>0.645</td>\n",
              "      <td>0.12</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.075</td>\n",
              "      <td>32.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>0.99547</td>\n",
              "      <td>3.57</td>\n",
              "      <td>0.71</td>\n",
              "      <td>10.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1598</th>\n",
              "      <td>6.0</td>\n",
              "      <td>0.310</td>\n",
              "      <td>0.47</td>\n",
              "      <td>3.6</td>\n",
              "      <td>0.067</td>\n",
              "      <td>18.0</td>\n",
              "      <td>42.0</td>\n",
              "      <td>0.99549</td>\n",
              "      <td>3.39</td>\n",
              "      <td>0.66</td>\n",
              "      <td>11.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1599 rows × 11 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  \\\n",
              "0               7.4             0.700         0.00             1.9      0.076   \n",
              "1               7.8             0.880         0.00             2.6      0.098   \n",
              "2               7.8             0.760         0.04             2.3      0.092   \n",
              "3              11.2             0.280         0.56             1.9      0.075   \n",
              "4               7.4             0.700         0.00             1.9      0.076   \n",
              "...             ...               ...          ...             ...        ...   \n",
              "1594            6.2             0.600         0.08             2.0      0.090   \n",
              "1595            5.9             0.550         0.10             2.2      0.062   \n",
              "1596            6.3             0.510         0.13             2.3      0.076   \n",
              "1597            5.9             0.645         0.12             2.0      0.075   \n",
              "1598            6.0             0.310         0.47             3.6      0.067   \n",
              "\n",
              "      free sulfur dioxide  total sulfur dioxide  density    pH  sulphates  \\\n",
              "0                    11.0                  34.0  0.99780  3.51       0.56   \n",
              "1                    25.0                  67.0  0.99680  3.20       0.68   \n",
              "2                    15.0                  54.0  0.99700  3.26       0.65   \n",
              "3                    17.0                  60.0  0.99800  3.16       0.58   \n",
              "4                    11.0                  34.0  0.99780  3.51       0.56   \n",
              "...                   ...                   ...      ...   ...        ...   \n",
              "1594                 32.0                  44.0  0.99490  3.45       0.58   \n",
              "1595                 39.0                  51.0  0.99512  3.52       0.76   \n",
              "1596                 29.0                  40.0  0.99574  3.42       0.75   \n",
              "1597                 32.0                  44.0  0.99547  3.57       0.71   \n",
              "1598                 18.0                  42.0  0.99549  3.39       0.66   \n",
              "\n",
              "      alcohol  \n",
              "0         9.4  \n",
              "1         9.8  \n",
              "2         9.8  \n",
              "3         9.8  \n",
              "4         9.4  \n",
              "...       ...  \n",
              "1594     10.5  \n",
              "1595     11.2  \n",
              "1596     11.0  \n",
              "1597     10.2  \n",
              "1598     11.0  \n",
              "\n",
              "[1599 rows x 11 columns]"
            ]
          },
          "execution_count": 18,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "x"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TNLpHsJ5sUnx"
      },
      "source": [
        "Label Binarizaton"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "id": "ZO0UMUbRsNmt"
      },
      "outputs": [],
      "source": [
        "y = data['quality']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Wp_Uzbps9nk",
        "outputId": "4e0fdda4-de8d-4239-df34-c051eed0162a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0       5\n",
              "1       5\n",
              "2       5\n",
              "3       6\n",
              "4       5\n",
              "       ..\n",
              "1594    5\n",
              "1595    6\n",
              "1596    6\n",
              "1597    5\n",
              "1598    6\n",
              "Name: quality, Length: 1599, dtype: int64"
            ]
          },
          "execution_count": 20,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "y"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "W0T7pk6WtDSR"
      },
      "source": [
        "Train & Test Split"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "id": "KXd_4XvCs-sT"
      },
      "outputs": [],
      "source": [
        "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qIlkPlx1ttpR",
        "outputId": "a9625ba8-7974-4724-d3f7-25fb71f126ab"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "(1599,)\n",
            "(1279,)\n",
            "(320,)\n"
          ]
        }
      ],
      "source": [
        "print(y.shape)\n",
        "print(y_train.shape)\n",
        "print(y_test.shape)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "m5MZuPZht60I"
      },
      "source": [
        "Model Training and Testing"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "id": "xLYtbQDht0Uq"
      },
      "outputs": [],
      "source": [
        "model = RandomForestClassifier()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "doympXrQu__E",
        "outputId": "cc55f7f7-36a0-4a8d-aa09-81343494ff2b"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestClassifier()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div></div></div>"
            ],
            "text/plain": [
              "RandomForestClassifier()"
            ]
          },
          "execution_count": 24,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "model.fit(x_train, y_train)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "m1lChonUvS1d"
      },
      "source": [
        "Model Evaluation"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "r-I7bqyLvVJ_"
      },
      "source": [
        "Accuracy Score"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "id": "NsuQMf9cvKmK"
      },
      "outputs": [],
      "source": [
        "# accuracy on test data\n",
        "X_test_prediction = model.predict(x_test)\n",
        "test_data_accuracy = accuracy_score(X_test_prediction, y_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SkyRHd1Dv5gU",
        "outputId": "e710b573-cf50-46d2-e863-00b3a1f862c7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Accuracy :  0.7375\n"
          ]
        }
      ],
      "source": [
        "print('Accuracy : ', test_data_accuracy)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           3       0.00      0.00      0.00         2\n",
            "           4       0.00      0.00      0.00        12\n",
            "           5       0.79      0.83      0.81       138\n",
            "           6       0.71      0.78      0.74       131\n",
            "           7       0.70      0.53      0.60        36\n",
            "           8       0.00      0.00      0.00         1\n",
            "\n",
            "    accuracy                           0.74       320\n",
            "   macro avg       0.37      0.36      0.36       320\n",
            "weighted avg       0.71      0.74      0.72       320\n",
            "\n"
          ]
        }
      ],
      "source": [
        "print(classification_report(y_test, X_test_prediction))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kbptIZOLwMwj"
      },
      "source": [
        "Building a Predictive System"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1_RRHB94v91w",
        "outputId": "9bb5032a-8711-4f3a-a9cc-2df74c5ff210"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Bad Quality Wine\n"
          ]
        }
      ],
      "source": [
        "input_data = (7.5,0.5,0.36,6.1,0.071,17.0,102.0,0.9978,3.35,0.8,10.5)\n",
        "\n",
        "# changing the input data to a numpy array\n",
        "input_data_as_numpy_array = np.asarray(input_data)\n",
        "\n",
        "# reshape the data as we are predicting the label for only one instance\n",
        "input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
        "\n",
        "prediction = model.predict(input_data_reshaped)\n",
        "\n",
        "if (prediction[0]==1):\n",
        "  print('Good Quality Wine')\n",
        "else:\n",
        "  print('Bad Quality Wine')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {},
      "outputs": [],
      "source": [
        "import pickle\n",
        "pickle.dump(model, open(\"model.pkl\", \"wb\"))"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
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
  "nbformat_minor": 0
}
```

## File: `Raw_Data/winequality-red.csv`
```
fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality
7.4,0.7,0.0,1.9,0.076,11.0,34.0,0.9978,3.51,0.56,9.4,5
7.8,0.88,0.0,2.6,0.098,25.0,67.0,0.9968,3.2,0.68,9.8,5
7.8,0.76,0.04,2.3,0.092,15.0,54.0,0.997,3.26,0.65,9.8,5
11.2,0.28,0.56,1.9,0.075,17.0,60.0,0.998,3.16,0.58,9.8,6
7.4,0.7,0.0,1.9,0.076,11.0,34.0,0.9978,3.51,0.56,9.4,5
7.4,0.66,0.0,1.8,0.075,13.0,40.0,0.9978,3.51,0.56,9.4,5
7.9,0.6,0.06,1.6,0.069,15.0,59.0,0.9964,3.3,0.46,9.4,5
7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0,7
7.8,0.58,0.02,2.0,0.073,9.0,18.0,0.9968,3.36,0.57,9.5,7
7.5,0.5,0.36,6.1,0.071,17.0,102.0,0.9978,3.35,0.8,10.5,5
6.7,0.58,0.08,1.8,0.09699999999999999,15.0,65.0,0.9959,3.28,0.54,9.2,5
7.5,0.5,0.36,6.1,0.071,17.0,102.0,0.9978,3.35,0.8,10.5,5
5.6,0.615,0.0,1.6,0.08900000000000001,16.0,59.0,0.9943,3.58,0.52,9.9,5
7.8,0.61,0.29,1.6,0.114,9.0,29.0,0.9974,3.26,1.56,9.1,5
8.9,0.62,0.18,3.8,0.17600000000000002,52.0,145.0,0.9986,3.16,0.88,9.2,5
8.9,0.62,0.19,3.9,0.17,51.0,148.0,0.9986,3.17,0.93,9.2,5
8.5,0.28,0.56,1.8,0.092,35.0,103.0,0.9969,3.3,0.75,10.5,7
8.1,0.56,0.28,1.7,0.368,16.0,56.0,0.9968,3.11,1.28,9.3,5
7.4,0.59,0.08,4.4,0.086,6.0,29.0,0.9974,3.38,0.5,9.0,4
7.9,0.32,0.51,1.8,0.341,17.0,56.0,0.9969,3.04,1.08,9.2,6
8.9,0.22,0.48,1.8,0.077,29.0,60.0,0.9968,3.39,0.53,9.4,6
7.6,0.39,0.31,2.3,0.08199999999999999,23.0,71.0,0.9982,3.52,0.65,9.7,5
7.9,0.43,0.21,1.6,0.106,10.0,37.0,0.9966,3.17,0.91,9.5,5
8.5,0.49,0.11,2.3,0.084,9.0,67.0,0.9968,3.17,0.53,9.4,5
6.9,0.4,0.14,2.4,0.085,21.0,40.0,0.9968,3.43,0.63,9.7,6
6.3,0.39,0.16,1.4,0.08,11.0,23.0,0.9955,3.34,0.56,9.3,5
7.6,0.41,0.24,1.8,0.08,4.0,11.0,0.9962,3.28,0.59,9.5,5
7.9,0.43,0.21,1.6,0.106,10.0,37.0,0.9966,3.17,0.91,9.5,5
7.1,0.71,0.0,1.9,0.08,14.0,35.0,0.9972,3.47,0.55,9.4,5
7.8,0.645,0.0,2.0,0.08199999999999999,8.0,16.0,0.9964,3.38,0.59,9.8,6
6.7,0.675,0.07,2.4,0.08900000000000001,17.0,82.0,0.9958,3.35,0.54,10.1,5
6.9,0.685,0.0,2.5,0.105,22.0,37.0,0.9966,3.46,0.57,10.6,6
8.3,0.655,0.12,2.3,0.083,15.0,113.0,0.9966,3.17,0.66,9.8,5
6.9,0.605,0.12,10.7,0.073,40.0,83.0,0.9993,3.45,0.52,9.4,6
5.2,0.32,0.25,1.8,0.10300000000000001,13.0,50.0,0.9957,3.38,0.55,9.2,5
7.8,0.645,0.0,5.5,0.086,5.0,18.0,0.9986,3.4,0.55,9.6,6
7.8,0.6,0.14,2.4,0.086,3.0,15.0,0.9975,3.42,0.6,10.8,6
8.1,0.38,0.28,2.1,0.066,13.0,30.0,0.9968,3.23,0.73,9.7,7
5.7,1.13,0.09,1.5,0.172,7.0,19.0,0.9940000000000001,3.5,0.48,9.8,4
7.3,0.45,0.36,5.9,0.07400000000000001,12.0,87.0,0.9978,3.33,0.83,10.5,5
7.3,0.45,0.36,5.9,0.07400000000000001,12.0,87.0,0.9978,3.33,0.83,10.5,5
8.8,0.61,0.3,2.8,0.08800000000000001,17.0,46.0,0.9976,3.26,0.51,9.3,4
7.5,0.49,0.2,2.6,0.332,8.0,14.0,0.9968,3.21,0.9,10.5,6
8.1,0.66,0.22,2.2,0.069,9.0,23.0,0.9968,3.3,1.2,10.3,5
6.8,0.67,0.02,1.8,0.05,5.0,11.0,0.9962,3.48,0.52,9.5,5
4.6,0.52,0.15,2.1,0.054000000000000006,8.0,65.0,0.9934,3.9,0.56,13.1,4
7.7,0.935,0.43,2.2,0.114,22.0,114.0,0.997,3.25,0.73,9.2,5
8.7,0.29,0.52,1.6,0.113,12.0,37.0,0.9969,3.25,0.58,9.5,5
6.4,0.4,0.23,1.6,0.066,5.0,12.0,0.9958,3.34,0.56,9.2,5
5.6,0.31,0.37,1.4,0.07400000000000001,12.0,96.0,0.9954,3.32,0.58,9.2,5
8.8,0.66,0.26,1.7,0.07400000000000001,4.0,23.0,0.9971,3.15,0.74,9.2,5
6.6,0.52,0.04,2.2,0.069,8.0,15.0,0.9956,3.4,0.63,9.4,6
6.6,0.5,0.04,2.1,0.068,6.0,14.0,0.9955,3.39,0.64,9.4,6
8.6,0.38,0.36,3.0,0.081,30.0,119.0,0.997,3.2,0.56,9.4,5
7.6,0.51,0.15,2.8,0.11,33.0,73.0,0.9955,3.17,0.63,10.2,6
7.7,0.62,0.04,3.8,0.084,25.0,45.0,0.9978,3.34,0.53,9.5,5
10.2,0.42,0.57,3.4,0.07,4.0,10.0,0.9971,3.04,0.63,9.6,5
7.5,0.63,0.12,5.1,0.111,50.0,110.0,0.9983,3.26,0.77,9.4,5
7.8,0.59,0.18,2.3,0.076,17.0,54.0,0.9975,3.43,0.59,10.0,5
7.3,0.39,0.31,2.4,0.07400000000000001,9.0,46.0,0.9962,3.41,0.54,9.4,6
8.8,0.4,0.4,2.2,0.079,19.0,52.0,0.998,3.44,0.64,9.2,5
7.7,0.69,0.49,1.8,0.115,20.0,112.0,0.9968,3.21,0.71,9.3,5
7.5,0.52,0.16,1.9,0.085,12.0,35.0,0.9968,3.38,0.62,9.5,7
7.0,0.735,0.05,2.0,0.081,13.0,54.0,0.9966,3.39,0.57,9.8,5
7.2,0.725,0.05,4.65,0.086,4.0,11.0,0.9962,3.41,0.39,10.9,5
7.2,0.725,0.05,4.65,0.086,4.0,11.0,0.9962,3.41,0.39,10.9,5
7.5,0.52,0.11,1.5,0.079,11.0,39.0,0.9968,3.42,0.58,9.6,5
6.6,0.705,0.07,1.6,0.076,6.0,15.0,0.9962,3.44,0.58,10.7,5
9.3,0.32,0.57,2.0,0.07400000000000001,27.0,65.0,0.9969,3.28,0.79,10.7,5
8.0,0.705,0.05,1.9,0.07400000000000001,8.0,19.0,0.9962,3.34,0.95,10.5,6
7.7,0.63,0.08,1.9,0.076,15.0,27.0,0.9967,3.32,0.54,9.5,6
7.7,0.67,0.23,2.1,0.08800000000000001,17.0,96.0,0.9962,3.32,0.48,9.5,5
7.7,0.69,0.22,1.9,0.084,18.0,94.0,0.9961,3.31,0.48,9.5,5
8.3,0.675,0.26,2.1,0.084,11.0,43.0,0.9976,3.31,0.53,9.2,4
9.7,0.32,0.54,2.5,0.094,28.0,83.0,0.9984,3.28,0.82,9.6,5
8.8,0.41,0.64,2.2,0.09300000000000001,9.0,42.0,0.9986,3.54,0.66,10.5,5
8.8,0.41,0.64,2.2,0.09300000000000001,9.0,42.0,0.9986,3.54,0.66,10.5,5
6.8,0.785,0.0,2.4,0.10400000000000001,14.0,30.0,0.9966,3.52,0.55,10.7,6
6.7,0.75,0.12,2.0,0.086,12.0,80.0,0.9958,3.38,0.52,10.1,5
8.3,0.625,0.2,1.5,0.08,27.0,119.0,0.9972,3.16,1.12,9.1,4
6.2,0.45,0.2,1.6,0.069,3.0,15.0,0.9958,3.41,0.56,9.2,5
7.8,0.43,0.7,1.9,0.46399999999999997,22.0,67.0,0.9974,3.13,1.28,9.4,5
7.4,0.5,0.47,2.0,0.086,21.0,73.0,0.997,3.36,0.57,9.1,5
7.3,0.67,0.26,1.8,0.401,16.0,51.0,0.9969,3.16,1.14,9.4,5
6.3,0.3,0.48,1.8,0.069,18.0,61.0,0.9959,3.44,0.78,10.3,6
6.9,0.55,0.15,2.2,0.076,19.0,40.0,0.9961,3.41,0.59,10.1,5
8.6,0.49,0.28,1.9,0.11,20.0,136.0,0.9972,2.93,1.95,9.9,6
7.7,0.49,0.26,1.9,0.062,9.0,31.0,0.9966,3.39,0.64,9.6,5
9.3,0.39,0.44,2.1,0.107,34.0,125.0,0.9978,3.14,1.22,9.5,5
7.0,0.62,0.08,1.8,0.076,8.0,24.0,0.9978,3.48,0.53,9.0,5
7.9,0.52,0.26,1.9,0.079,42.0,140.0,0.9964,3.23,0.54,9.5,5
8.6,0.49,0.28,1.9,0.11,20.0,136.0,0.9972,2.93,1.95,9.9,6
8.6,0.49,0.29,2.0,0.11,19.0,133.0,0.9972,2.93,1.98,9.8,5
7.7,0.49,0.26,1.9,0.062,9.0,31.0,0.9966,3.39,0.64,9.6,5
5.0,1.02,0.04,1.4,0.045,41.0,85.0,0.9938,3.75,0.48,10.5,4
4.7,0.6,0.17,2.3,0.057999999999999996,17.0,106.0,0.9932,3.85,0.6,12.9,6
6.8,0.775,0.0,3.0,0.102,8.0,23.0,0.9965,3.45,0.56,10.7,5
7.0,0.5,0.25,2.0,0.07,3.0,22.0,0.9963,3.25,0.63,9.2,5
7.6,0.9,0.06,2.5,0.079,5.0,10.0,0.9967,3.39,0.56,9.8,5
8.1,0.545,0.18,1.9,0.08,13.0,35.0,0.9972,3.3,0.59,9.0,6
8.3,0.61,0.3,2.1,0.084,11.0,50.0,0.9972,3.4,0.61,10.2,6
7.8,0.5,0.3,1.9,0.075,8.0,22.0,0.9959,3.31,0.56,10.4,6
8.1,0.545,0.18,1.9,0.08,13.0,35.0,0.9972,3.3,0.59,9.0,6
8.1,0.575,0.22,2.1,0.077,12.0,65.0,0.9967,3.29,0.51,9.2,5
7.2,0.49,0.24,2.2,0.07,5.0,36.0,0.996,3.33,0.48,9.4,5
8.1,0.575,0.22,2.1,0.077,12.0,65.0,0.9967,3.29,0.51,9.2,5
7.8,0.41,0.68,1.7,0.467,18.0,69.0,0.9973,3.08,1.31,9.3,5
6.2,0.63,0.31,1.7,0.08800000000000001,15.0,64.0,0.9969,3.46,0.79,9.3,5
8.0,0.33,0.53,2.5,0.091,18.0,80.0,0.9976,3.37,0.8,9.6,6
8.1,0.785,0.52,2.0,0.122,37.0,153.0,0.9969,3.21,0.69,9.3,5
7.8,0.56,0.19,1.8,0.10400000000000001,12.0,47.0,0.9964,3.19,0.93,9.5,5
8.4,0.62,0.09,2.2,0.084,11.0,108.0,0.9964,3.15,0.66,9.8,5
8.4,0.6,0.1,2.2,0.085,14.0,111.0,0.9964,3.15,0.66,9.8,5
10.1,0.31,0.44,2.3,0.08,22.0,46.0,0.9988,3.32,0.67,9.7,6
7.8,0.56,0.19,1.8,0.10400000000000001,12.0,47.0,0.9964,3.19,0.93,9.5,5
9.4,0.4,0.31,2.2,0.09,13.0,62.0,0.9966,3.07,0.63,10.5,6
8.3,0.54,0.28,1.9,0.077,11.0,40.0,0.9978,3.39,0.61,10.0,6
7.8,0.56,0.12,2.0,0.08199999999999999,7.0,28.0,0.997,3.37,0.5,9.4,6
8.8,0.55,0.04,2.2,0.11900000000000001,14.0,56.0,0.9962,3.21,0.6,10.9,6
7.0,0.69,0.08,1.8,0.09699999999999999,22.0,89.0,0.9959,3.34,0.54,9.2,6
7.3,1.07,0.09,1.7,0.17800000000000002,10.0,89.0,0.9962,3.3,0.57,9.0,5
8.8,0.55,0.04,2.2,0.11900000000000001,14.0,56.0,0.9962,3.21,0.6,10.9,6
7.3,0.695,0.0,2.5,0.075,3.0,13.0,0.998,3.49,0.52,9.2,5
8.0,0.71,0.0,2.6,0.08,11.0,34.0,0.9976,3.44,0.53,9.5,5
7.8,0.5,0.17,1.6,0.08199999999999999,21.0,102.0,0.996,3.39,0.48,9.5,5
9.0,0.62,0.04,1.9,0.146,27.0,90.0,0.9984,3.16,0.7,9.4,5
8.2,1.33,0.0,1.7,0.081,3.0,12.0,0.9964,3.53,0.49,10.9,5
8.1,1.33,0.0,1.8,0.08199999999999999,3.0,12.0,0.9964,3.54,0.48,10.9,5
8.0,0.59,0.16,1.8,0.065,3.0,16.0,0.9962,3.42,0.92,10.5,7
6.1,0.38,0.15,1.8,0.07200000000000001,6.0,19.0,0.9955,3.42,0.57,9.4,5
8.0,0.745,0.56,2.0,0.11800000000000001,30.0,134.0,0.9968,3.24,0.66,9.4,5
5.6,0.5,0.09,2.3,0.049,17.0,99.0,0.9937,3.63,0.63,13.0,5
5.6,0.5,0.09,2.3,0.049,17.0,99.0,0.9937,3.63,0.63,13.0,5
6.6,0.5,0.01,1.5,0.06,17.0,26.0,0.9952,3.4,0.58,9.8,6
7.9,1.04,0.05,2.2,0.084,13.0,29.0,0.9959,3.22,0.55,9.9,6
8.4,0.745,0.11,1.9,0.09,16.0,63.0,0.9965,3.19,0.82,9.6,5
8.3,0.715,0.15,1.8,0.08900000000000001,10.0,52.0,0.9968,3.23,0.77,9.5,5
7.2,0.415,0.36,2.0,0.081,13.0,45.0,0.9972,3.48,0.64,9.2,5
7.8,0.56,0.19,2.1,0.081,15.0,105.0,0.9962,3.33,0.54,9.5,5
7.8,0.56,0.19,2.0,0.081,17.0,108.0,0.9962,3.32,0.54,9.5,5
8.4,0.745,0.11,1.9,0.09,16.0,63.0,0.9965,3.19,0.82,9.6,5
8.3,0.715,0.15,1.8,0.08900000000000001,10.0,52.0,0.9968,3.23,0.77,9.5,5
5.2,0.34,0.0,1.8,0.05,27.0,63.0,0.9916,3.68,0.79,14.0,6
6.3,0.39,0.08,1.7,0.066,3.0,20.0,0.9954,3.34,0.58,9.4,5
5.2,0.34,0.0,1.8,0.05,27.0,63.0,0.9916,3.68,0.79,14.0,6
8.1,0.67,0.55,1.8,0.11699999999999999,32.0,141.0,0.9968,3.17,0.62,9.4,5
5.8,0.68,0.02,1.8,0.087,21.0,94.0,0.9944,3.54,0.52,10.0,5
7.6,0.49,0.26,1.6,0.23600000000000002,10.0,88.0,0.9968,3.11,0.8,9.3,5
6.9,0.49,0.1,2.3,0.07400000000000001,12.0,30.0,0.9959,3.42,0.58,10.2,6
8.2,0.4,0.44,2.8,0.08900000000000001,11.0,43.0,0.9975,3.53,0.61,10.5,6
7.3,0.33,0.47,2.1,0.077,5.0,11.0,0.9958,3.33,0.53,10.3,6
9.2,0.52,1.0,3.4,0.61,32.0,69.0,0.9996,2.74,2.0,9.4,4
7.5,0.6,0.03,1.8,0.095,25.0,99.0,0.995,3.35,0.54,10.1,5
7.5,0.6,0.03,1.8,0.095,25.0,99.0,0.995,3.35,0.54,10.1,5
7.1,0.43,0.42,5.5,0.07,29.0,129.0,0.9973,3.42,0.72,10.5,5
7.1,0.43,0.42,5.5,0.071,28.0,128.0,0.9973,3.42,0.71,10.5,5
7.1,0.43,0.42,5.5,0.07,29.0,129.0,0.9973,3.42,0.72,10.5,5
7.1,0.43,0.42,5.5,0.071,28.0,128.0,0.9973,3.42,0.71,10.5,5
7.1,0.68,0.0,2.2,0.073,12.0,22.0,0.9969,3.48,0.5,9.3,5
6.8,0.6,0.18,1.9,0.079,18.0,86.0,0.9968,3.59,0.57,9.3,6
7.6,0.95,0.03,2.0,0.09,7.0,20.0,0.9959,3.2,0.56,9.6,5
7.6,0.68,0.02,1.3,0.07200000000000001,9.0,20.0,0.9965,3.17,1.08,9.2,4
7.8,0.53,0.04,1.7,0.076,17.0,31.0,0.9964,3.33,0.56,10.0,6
7.4,0.6,0.26,7.3,0.07,36.0,121.0,0.9982,3.37,0.49,9.4,5
7.3,0.59,0.26,7.2,0.07,35.0,121.0,0.9981,3.37,0.49,9.4,5
7.8,0.63,0.48,1.7,0.1,14.0,96.0,0.9961,3.19,0.62,9.5,5
6.8,0.64,0.1,2.1,0.085,18.0,101.0,0.9956,3.34,0.52,10.2,5
7.3,0.55,0.03,1.6,0.07200000000000001,17.0,42.0,0.9956,3.37,0.48,9.0,4
6.8,0.63,0.07,2.1,0.08900000000000001,11.0,44.0,0.9953,3.47,0.55,10.4,6
7.5,0.705,0.24,1.8,0.36,15.0,63.0,0.9964,3.0,1.59,9.5,5
7.9,0.885,0.03,1.8,0.057999999999999996,4.0,8.0,0.9972,3.36,0.33,9.1,4
8.0,0.42,0.17,2.0,0.073,6.0,18.0,0.9972,3.29,0.61,9.2,6
8.0,0.42,0.17,2.0,0.073,6.0,18.0,0.9972,3.29,0.61,9.2,6
7.4,0.62,0.05,1.9,0.068,24.0,42.0,0.9961,3.42,0.57,11.5,6
7.3,0.38,0.21,2.0,0.08,7.0,35.0,0.9961,3.33,0.47,9.5,5
6.9,0.5,0.04,1.5,0.085,19.0,49.0,0.9958,3.35,0.78,9.5,5
7.3,0.38,0.21,2.0,0.08,7.0,35.0,0.9961,3.33,0.47,9.5,5
7.5,0.52,0.42,2.3,0.087,8.0,38.0,0.9972,3.58,0.61,10.5,6
7.0,0.805,0.0,2.5,0.068,7.0,20.0,0.9969,3.48,0.56,9.6,5
8.8,0.61,0.14,2.4,0.067,10.0,42.0,0.9969,3.19,0.59,9.5,5
8.8,0.61,0.14,2.4,0.067,10.0,42.0,0.9969,3.19,0.59,9.5,5
8.9,0.61,0.49,2.0,0.27,23.0,110.0,0.9972,3.12,1.02,9.3,5
7.2,0.73,0.02,2.5,0.076,16.0,42.0,0.9972,3.44,0.52,9.3,5
6.8,0.61,0.2,1.8,0.077,11.0,65.0,0.9971,3.54,0.58,9.3,5
6.7,0.62,0.21,1.9,0.079,8.0,62.0,0.997,3.52,0.58,9.3,6
8.9,0.31,0.57,2.0,0.111,26.0,85.0,0.9971,3.26,0.53,9.7,5
7.4,0.39,0.48,2.0,0.08199999999999999,14.0,67.0,0.9972,3.34,0.55,9.2,5
7.7,0.705,0.1,2.6,0.084,9.0,26.0,0.9976,3.39,0.49,9.7,5
7.9,0.5,0.33,2.0,0.084,15.0,143.0,0.9968,3.2,0.55,9.5,5
7.9,0.49,0.32,1.9,0.08199999999999999,17.0,144.0,0.9968,3.2,0.55,9.5,5
8.2,0.5,0.35,2.9,0.077,21.0,127.0,0.9976,3.23,0.62,9.4,5
6.4,0.37,0.25,1.9,0.07400000000000001,21.0,49.0,0.9974,3.57,0.62,9.8,6
6.8,0.63,0.12,3.8,0.099,16.0,126.0,0.9969,3.28,0.61,9.5,5
7.6,0.55,0.21,2.2,0.071,7.0,28.0,0.9964,3.28,0.55,9.7,5
7.6,0.55,0.21,2.2,0.071,7.0,28.0,0.9964,3.28,0.55,9.7,5
7.8,0.59,0.33,2.0,0.07400000000000001,24.0,120.0,0.9968,3.25,0.54,9.4,5
7.3,0.58,0.3,2.4,0.07400000000000001,15.0,55.0,0.9968,3.46,0.59,10.2,5
11.5,0.3,0.6,2.0,0.067,12.0,27.0,0.9981,3.11,0.97,10.1,6
5.4,0.835,0.08,1.2,0.046,13.0,93.0,0.9924,3.57,0.85,13.0,7
6.9,1.09,0.06,2.1,0.061,12.0,31.0,0.9948,3.51,0.43,11.4,4
9.6,0.32,0.47,1.4,0.055999999999999994,9.0,24.0,0.99695,3.22,0.82,10.3,7
8.8,0.37,0.48,2.1,0.09699999999999999,39.0,145.0,0.9975,3.04,1.03,9.3,5
6.8,0.5,0.11,1.5,0.075,16.0,49.0,0.99545,3.36,0.79,9.5,5
7.0,0.42,0.35,1.6,0.08800000000000001,16.0,39.0,0.9961,3.34,0.55,9.2,5
7.0,0.43,0.36,1.6,0.08900000000000001,14.0,37.0,0.99615,3.34,0.56,9.2,6
12.8,0.3,0.74,2.6,0.095,9.0,28.0,0.9994,3.2,0.77,10.8,7
12.8,0.3,0.74,2.6,0.095,9.0,28.0,0.9994,3.2,0.77,10.8,7
7.8,0.57,0.31,1.8,0.069,26.0,120.0,0.99625,3.29,0.53,9.3,5
7.8,0.44,0.28,2.7,0.1,18.0,95.0,0.9966,3.22,0.67,9.4,5
11.0,0.3,0.58,2.1,0.054000000000000006,7.0,19.0,0.998,3.31,0.88,10.5,7
9.7,0.53,0.6,2.0,0.039,5.0,19.0,0.99585,3.3,0.86,12.4,6
8.0,0.725,0.24,2.8,0.083,10.0,62.0,0.99685,3.35,0.56,10.0,6
11.6,0.44,0.64,2.1,0.059000000000000004,5.0,15.0,0.998,3.21,0.67,10.2,6
8.2,0.57,0.26,2.2,0.06,28.0,65.0,0.9959,3.3,0.43,10.1,5
7.8,0.735,0.08,2.4,0.092,10.0,41.0,0.9974,3.24,0.71,9.8,6
7.0,0.49,0.49,5.6,0.06,26.0,121.0,0.9974,3.34,0.76,10.5,5
8.7,0.625,0.16,2.0,0.10099999999999999,13.0,49.0,0.9962,3.14,0.57,11.0,5
8.1,0.725,0.22,2.2,0.07200000000000001,11.0,41.0,0.9967,3.36,0.55,9.1,5
7.5,0.49,0.19,1.9,0.076,10.0,44.0,0.9957,3.39,0.54,9.7,5
7.8,0.53,0.33,2.4,0.08,24.0,144.0,0.99655,3.3,0.6,9.5,5
7.8,0.34,0.37,2.0,0.08199999999999999,24.0,58.0,0.9964,3.34,0.59,9.4,6
7.4,0.53,0.26,2.0,0.10099999999999999,16.0,72.0,0.9957,3.15,0.57,9.4,5
6.8,0.61,0.04,1.5,0.057,5.0,10.0,0.99525,3.42,0.6,9.5,5
8.6,0.645,0.25,2.0,0.083,8.0,28.0,0.99815,3.28,0.6,10.0,6
8.4,0.635,0.36,2.0,0.08900000000000001,15.0,55.0,0.99745,3.31,0.57,10.4,4
7.7,0.43,0.25,2.6,0.073,29.0,63.0,0.99615,3.37,0.58,10.5,6
8.9,0.59,0.5,2.0,0.337,27.0,81.0,0.9964,3.04,1.61,9.5,6
9.0,0.82,0.14,2.6,0.08900000000000001,9.0,23.0,0.9984,3.39,0.63,9.8,5
7.7,0.43,0.25,2.6,0.073,29.0,63.0,0.99615,3.37,0.58,10.5,6
6.9,0.52,0.25,2.6,0.081,10.0,37.0,0.99685,3.46,0.5,11.0,5
5.2,0.48,0.04,1.6,0.054000000000000006,19.0,106.0,0.9927,3.54,0.62,12.2,7
8.0,0.38,0.06,1.8,0.078,12.0,49.0,0.99625,3.37,0.52,9.9,6
8.5,0.37,0.2,2.8,0.09,18.0,58.0,0.998,3.34,0.7,9.6,6
6.9,0.52,0.25,2.6,0.081,10.0,37.0,0.99685,3.46,0.5,11.0,5
8.2,1.0,0.09,2.3,0.065,7.0,37.0,0.99685,3.32,0.55,9.0,6
7.2,0.63,0.0,1.9,0.09699999999999999,14.0,38.0,0.99675,3.37,0.58,9.0,6
7.2,0.63,0.0,1.9,0.09699999999999999,14.0,38.0,0.99675,3.37,0.58,9.0,6
7.2,0.645,0.0,1.9,0.09699999999999999,15.0,39.0,0.99675,3.37,0.58,9.2,6
7.2,0.63,0.0,1.9,0.09699999999999999,14.0,38.0,0.99675,3.37,0.58,9.0,6
8.2,1.0,0.09,2.3,0.065,7.0,37.0,0.99685,3.32,0.55,9.0,6
8.9,0.635,0.37,1.7,0.263,5.0,62.0,0.9971,3.0,1.09,9.3,5
12.0,0.38,0.56,2.1,0.09300000000000001,6.0,24.0,0.99925,3.14,0.71,10.9,6
7.7,0.58,0.1,1.8,0.102,28.0,109.0,0.99565,3.08,0.49,9.8,6
15.0,0.21,0.44,2.2,0.075,10.0,24.0,1.00005,3.07,0.84,9.2,7
15.0,0.21,0.44,2.2,0.075,10.0,24.0,1.00005,3.07,0.84,9.2,7
7.3,0.66,0.0,2.0,0.084,6.0,23.0,0.9983,3.61,0.96,9.9,6
7.1,0.68,0.07,1.9,0.075,16.0,51.0,0.99685,3.38,0.52,9.5,5
8.2,0.6,0.17,2.3,0.07200000000000001,11.0,73.0,0.9963,3.2,0.45,9.3,5
7.7,0.53,0.06,1.7,0.07400000000000001,9.0,39.0,0.99615,3.35,0.48,9.8,6
7.3,0.66,0.0,2.0,0.084,6.0,23.0,0.9983,3.61,0.96,9.9,6
10.8,0.32,0.44,1.6,0.063,16.0,37.0,0.9985,3.22,0.78,10.0,6
7.1,0.6,0.0,1.8,0.07400000000000001,16.0,34.0,0.9972,3.47,0.7,9.9,6
11.1,0.35,0.48,3.1,0.09,5.0,21.0,0.9986,3.17,0.53,10.5,5
7.7,0.775,0.42,1.9,0.092,8.0,86.0,0.9959,3.23,0.59,9.5,5
7.1,0.6,0.0,1.8,0.07400000000000001,16.0,34.0,0.9972,3.47,0.7,9.9,6
8.0,0.57,0.23,3.2,0.073,17.0,119.0,0.99675,3.26,0.57,9.3,5
9.4,0.34,0.37,2.2,0.075,5.0,13.0,0.998,3.22,0.62,9.2,5
6.6,0.695,0.0,2.1,0.075,12.0,56.0,0.9968,3.49,0.67,9.2,5
7.7,0.41,0.76,1.8,0.611,8.0,45.0,0.9968,3.06,1.26,9.4,5
10.0,0.31,0.47,2.6,0.085,14.0,33.0,0.99965,3.36,0.8,10.5,7
7.9,0.33,0.23,1.7,0.077,18.0,45.0,0.99625,3.29,0.65,9.3,5
7.0,0.975,0.04,2.0,0.087,12.0,67.0,0.99565,3.35,0.6,9.4,4
8.0,0.52,0.03,1.7,0.07,10.0,35.0,0.99575,3.34,0.57,10.0,5
7.9,0.37,0.23,1.8,0.077,23.0,49.0,0.9963,3.28,0.67,9.3,5
12.5,0.56,0.49,2.4,0.064,5.0,27.0,0.9999,3.08,0.87,10.9,5
11.8,0.26,0.52,1.8,0.071,6.0,10.0,0.9968,3.2,0.72,10.2,7
8.1,0.87,0.0,3.3,0.096,26.0,61.0,1.00025,3.6,0.72,9.8,4
7.9,0.35,0.46,3.6,0.078,15.0,37.0,0.9973,3.35,0.86,12.8,8
6.9,0.54,0.04,3.0,0.077,7.0,27.0,0.9987,3.69,0.91,9.4,6
11.5,0.18,0.51,4.0,0.10400000000000001,4.0,23.0,0.9996,3.28,0.97,10.1,6
7.9,0.545,0.06,4.0,0.087,27.0,61.0,0.9965,3.36,0.67,10.7,6
11.5,0.18,0.51,4.0,0.10400000000000001,4.0,23.0,0.9996,3.28,0.97,10.1,6
10.9,0.37,0.58,4.0,0.071,17.0,65.0,0.99935,3.22,0.78,10.1,5
8.4,0.715,0.2,2.4,0.076,10.0,38.0,0.99735,3.31,0.64,9.4,5
7.5,0.65,0.18,7.0,0.08800000000000001,27.0,94.0,0.99915,3.38,0.77,9.4,5
7.9,0.545,0.06,4.0,0.087,27.0,61.0,0.9965,3.36,0.67,10.7,6
6.9,0.54,0.04,3.0,0.077,7.0,27.0,0.9987,3.69,0.91,9.4,6
11.5,0.18,0.51,4.0,0.10400000000000001,4.0,23.0,0.9996,3.28,0.97,10.1,6
10.3,0.32,0.45,6.4,0.073,5.0,13.0,0.9976,3.23,0.82,12.6,8
8.9,0.4,0.32,5.6,0.087,10.0,47.0,0.9991,3.38,0.77,10.5,7
11.4,0.26,0.44,3.6,0.071,6.0,19.0,0.9986,3.12,0.82,9.3,6
7.7,0.27,0.68,3.5,0.358,5.0,10.0,0.9972,3.25,1.08,9.9,7
7.6,0.52,0.12,3.0,0.067,12.0,53.0,0.9971,3.36,0.57,9.1,5
8.9,0.4,0.32,5.6,0.087,10.0,47.0,0.9991,3.38,0.77,10.5,7
9.9,0.59,0.07,3.4,0.102,32.0,71.0,1.00015,3.31,0.71,9.8,5
9.9,0.59,0.07,3.4,0.102,32.0,71.0,1.00015,3.31,0.71,9.8,5
12.0,0.45,0.55,2.0,0.073,25.0,49.0,0.9997,3.1,0.76,10.3,6
7.5,0.4,0.12,3.0,0.092,29.0,53.0,0.9967,3.37,0.7,10.3,6
8.7,0.52,0.09,2.5,0.091,20.0,49.0,0.9976,3.34,0.86,10.6,7
11.6,0.42,0.53,3.3,0.105,33.0,98.0,1.001,3.2,0.95,9.2,5
8.7,0.52,0.09,2.5,0.091,20.0,49.0,0.9976,3.34,0.86,10.6,7
11.0,0.2,0.48,2.0,0.34299999999999997,6.0,18.0,0.9979,3.3,0.71,10.5,5
10.4,0.55,0.23,2.7,0.091,18.0,48.0,0.9994,3.22,0.64,10.3,6
6.9,0.36,0.25,2.4,0.098,5.0,16.0,0.9964,3.41,0.6,10.1,6
13.3,0.34,0.52,3.2,0.094,17.0,53.0,1.0014,3.05,0.81,9.5,6
10.8,0.5,0.46,2.5,0.073,5.0,27.0,1.0001,3.05,0.64,9.5,5
10.6,0.83,0.37,2.6,0.086,26.0,70.0,0.9981,3.16,0.52,9.9,5
7.1,0.63,0.06,2.0,0.083,8.0,29.0,0.99855,3.67,0.73,9.6,5
7.2,0.65,0.02,2.3,0.094,5.0,31.0,0.9993,3.67,0.8,9.7,5
6.9,0.67,0.06,2.1,0.08,8.0,33.0,0.99845,3.68,0.71,9.6,5
7.5,0.53,0.06,2.6,0.086,20.0,44.0,0.9965,3.38,0.59,10.7,6
11.1,0.18,0.48,1.5,0.068,7.0,15.0,0.9973,3.22,0.64,10.1,6
8.3,0.705,0.12,2.6,0.092,12.0,28.0,0.9994,3.51,0.72,10.0,5
7.4,0.67,0.12,1.6,0.18600000000000003,5.0,21.0,0.996,3.39,0.54,9.5,5
8.4,0.65,0.6,2.1,0.11199999999999999,12.0,90.0,0.9973,3.2,0.52,9.2,5
10.3,0.53,0.48,2.5,0.063,6.0,25.0,0.9998,3.12,0.59,9.3,6
7.6,0.62,0.32,2.2,0.08199999999999999,7.0,54.0,0.9966,3.36,0.52,9.4,5
10.3,0.41,0.42,2.4,0.213,6.0,14.0,0.9994,3.19,0.62,9.5,6
10.3,0.43,0.44,2.4,0.214,5.0,12.0,0.9994,3.19,0.63,9.5,6
7.4,0.29,0.38,1.7,0.062,9.0,30.0,0.9968,3.41,0.53,9.5,6
10.3,0.53,0.48,2.5,0.063,6.0,25.0,0.9998,3.12,0.59,9.3,6
7.9,0.53,0.24,2.0,0.07200000000000001,15.0,105.0,0.996,3.27,0.54,9.4,6
9.0,0.46,0.31,2.8,0.09300000000000001,19.0,98.0,0.99815,3.32,0.63,9.5,6
8.6,0.47,0.3,3.0,0.076,30.0,135.0,0.9976,3.3,0.53,9.4,5
7.4,0.36,0.29,2.6,0.087,26.0,72.0,0.99645,3.39,0.68,11.0,5
7.1,0.35,0.29,2.5,0.096,20.0,53.0,0.9962,3.42,0.65,11.0,6
9.6,0.56,0.23,3.4,0.102,37.0,92.0,0.9996,3.3,0.65,10.1,5
9.6,0.77,0.12,2.9,0.08199999999999999,30.0,74.0,0.99865,3.3,0.64,10.4,6
9.8,0.66,0.39,3.2,0.083,21.0,59.0,0.9989,3.37,0.71,11.5,7
9.6,0.77,0.12,2.9,0.08199999999999999,30.0,74.0,0.99865,3.3,0.64,10.4,6
9.8,0.66,0.39,3.2,0.083,21.0,59.0,0.9989,3.37,0.71,11.5,7
9.3,0.61,0.26,3.4,0.09,25.0,87.0,0.99975,3.24,0.62,9.7,5
7.8,0.62,0.05,2.3,0.079,6.0,18.0,0.99735,3.29,0.63,9.3,5
10.3,0.59,0.42,2.8,0.09,35.0,73.0,0.9990000000000001,3.28,0.7,9.5,6
10.0,0.49,0.2,11.0,0.071,13.0,50.0,1.0015,3.16,0.69,9.2,6
10.0,0.49,0.2,11.0,0.071,13.0,50.0,1.0015,3.16,0.69,9.2,6
11.6,0.53,0.66,3.65,0.121,6.0,14.0,0.9978,3.05,0.74,11.5,7
10.3,0.44,0.5,4.5,0.107,5.0,13.0,0.998,3.28,0.83,11.5,5
13.4,0.27,0.62,2.6,0.08199999999999999,6.0,21.0,1.0002,3.16,0.67,9.7,6
10.7,0.46,0.39,2.0,0.061,7.0,15.0,0.9981,3.18,0.62,9.5,5
10.2,0.36,0.64,2.9,0.122,10.0,41.0,0.998,3.23,0.66,12.5,6
10.2,0.36,0.64,2.9,0.122,10.0,41.0,0.998,3.23,0.66,12.5,6
8.0,0.58,0.28,3.2,0.066,21.0,114.0,0.9973,3.22,0.54,9.4,6
8.4,0.56,0.08,2.1,0.105,16.0,44.0,0.9958,3.13,0.52,11.0,5
7.9,0.65,0.01,2.5,0.078,17.0,38.0,0.9963,3.34,0.74,11.7,7
11.9,0.695,0.53,3.4,0.128,7.0,21.0,0.9992,3.17,0.84,12.2,7
8.9,0.43,0.45,1.9,0.052000000000000005,6.0,16.0,0.9948,3.35,0.7,12.5,6
7.8,0.43,0.32,2.8,0.08,29.0,58.0,0.9974,3.31,0.64,10.3,5
12.4,0.49,0.58,3.0,0.10300000000000001,28.0,99.0,1.0008,3.16,1.0,11.5,6
12.5,0.28,0.54,2.3,0.08199999999999999,12.0,29.0,0.9997,3.11,1.36,9.8,7
12.2,0.34,0.5,2.4,0.066,10.0,21.0,1.0,3.12,1.18,9.2,6
10.6,0.42,0.48,2.7,0.065,5.0,18.0,0.9972,3.21,0.87,11.3,6
10.9,0.39,0.47,1.8,0.11800000000000001,6.0,14.0,0.9982,3.3,0.75,9.8,6
10.9,0.39,0.47,1.8,0.11800000000000001,6.0,14.0,0.9982,3.3,0.75,9.8,6
11.9,0.57,0.5,2.6,0.08199999999999999,6.0,32.0,1.0006,3.12,0.78,10.7,6
7.0,0.685,0.0,1.9,0.067,40.0,63.0,0.9979,3.6,0.81,9.9,5
6.6,0.815,0.02,2.7,0.07200000000000001,17.0,34.0,0.9955,3.58,0.89,12.3,7
13.8,0.49,0.67,3.0,0.09300000000000001,6.0,15.0,0.9986,3.02,0.93,12.0,6
9.6,0.56,0.31,2.8,0.08900000000000001,15.0,46.0,0.9979,3.11,0.92,10.0,6
9.1,0.785,0.0,2.6,0.09300000000000001,11.0,28.0,0.9994,3.36,0.86,9.4,6
10.7,0.67,0.22,2.7,0.107,17.0,34.0,1.0004,3.28,0.98,9.9,6
9.1,0.795,0.0,2.6,0.096,11.0,26.0,0.9994,3.35,0.83,9.4,6
7.7,0.665,0.0,2.4,0.09,8.0,19.0,0.9974,3.27,0.73,9.3,5
13.5,0.53,0.79,4.8,0.12,23.0,77.0,1.0018,3.18,0.77,13.0,5
6.1,0.21,0.4,1.4,0.066,40.5,165.0,0.9912,3.25,0.59,11.9,6
6.7,0.75,0.01,2.4,0.078,17.0,32.0,0.9955,3.55,0.61,12.8,6
11.5,0.41,0.52,3.0,0.08,29.0,55.0,1.0001,3.26,0.88,11.0,5
10.5,0.42,0.66,2.95,0.11599999999999999,12.0,29.0,0.997,3.24,0.75,11.7,7
11.9,0.43,0.66,3.1,0.109,10.0,23.0,1.0,3.15,0.85,10.4,7
12.6,0.38,0.66,2.6,0.08800000000000001,10.0,41.0,1.001,3.17,0.68,9.8,6
8.2,0.7,0.23,2.0,0.099,14.0,81.0,0.9973,3.19,0.7,9.4,5
8.6,0.45,0.31,2.6,0.086,21.0,50.0,0.9982,3.37,0.91,9.9,6
11.9,0.58,0.66,2.5,0.07200000000000001,6.0,37.0,0.9992,3.05,0.56,10.0,5
12.5,0.46,0.63,2.0,0.071,6.0,15.0,0.9988,2.99,0.87,10.2,5
12.8,0.615,0.66,5.8,0.083,7.0,42.0,1.0022,3.07,0.73,10.0,7
10.0,0.42,0.5,3.4,0.107,7.0,21.0,0.9979,3.26,0.93,11.8,6
12.8,0.615,0.66,5.8,0.083,7.0,42.0,1.0022,3.07,0.73,10.0,7
10.4,0.575,0.61,2.6,0.076,11.0,24.0,1.0,3.16,0.69,9.0,5
10.3,0.34,0.52,2.8,0.159,15.0,75.0,0.9998,3.18,0.64,9.4,5
9.4,0.27,0.53,2.4,0.07400000000000001,6.0,18.0,0.9962,3.2,1.13,12.0,7
6.9,0.765,0.02,2.3,0.063,35.0,63.0,0.9975,3.57,0.78,9.9,5
7.9,0.24,0.4,1.6,0.055999999999999994,11.0,25.0,0.9967,3.32,0.87,8.7,6
9.1,0.28,0.48,1.8,0.067,26.0,46.0,0.9967,3.32,1.04,10.6,6
7.4,0.55,0.22,2.2,0.106,12.0,72.0,0.9959,3.05,0.63,9.2,5
14.0,0.41,0.63,3.8,0.08900000000000001,6.0,47.0,1.0014,3.01,0.81,10.8,6
11.5,0.54,0.71,4.4,0.124,6.0,15.0,0.9984,3.01,0.83,11.8,7
11.5,0.45,0.5,3.0,0.078,19.0,47.0,1.0003,3.26,1.11,11.0,6
9.4,0.27,0.53,2.4,0.07400000000000001,6.0,18.0,0.9962,3.2,1.13,12.0,7
11.4,0.625,0.66,6.2,0.08800000000000001,6.0,24.0,0.9988,3.11,0.99,13.3,6
8.3,0.42,0.38,2.5,0.094,24.0,60.0,0.9979,3.31,0.7,10.8,6
8.3,0.26,0.42,2.0,0.08,11.0,27.0,0.9974,3.21,0.8,9.4,6
13.7,0.415,0.68,2.9,0.085,17.0,43.0,1.0014,3.06,0.8,10.0,6
8.3,0.26,0.42,2.0,0.08,11.0,27.0,0.9974,3.21,0.8,9.4,6
8.3,0.26,0.42,2.0,0.08,11.0,27.0,0.9974,3.21,0.8,9.4,6
7.7,0.51,0.28,2.1,0.087,23.0,54.0,0.998,3.42,0.74,9.2,5
7.4,0.63,0.07,2.4,0.09,11.0,37.0,0.9979,3.43,0.76,9.7,6
7.8,0.54,0.26,2.0,0.08800000000000001,23.0,48.0,0.9981,3.41,0.74,9.2,6
8.3,0.66,0.15,1.9,0.079,17.0,42.0,0.9972,3.31,0.54,9.6,6
7.8,0.46,0.26,1.9,0.08800000000000001,23.0,53.0,0.9981,3.43,0.74,9.2,6
9.6,0.38,0.31,2.5,0.096,16.0,49.0,0.9982,3.19,0.7,10.0,7
5.6,0.85,0.05,1.4,0.045,12.0,88.0,0.9924,3.56,0.82,12.9,8
13.7,0.415,0.68,2.9,0.085,17.0,43.0,1.0014,3.06,0.8,10.0,6
9.5,0.37,0.52,2.0,0.08199999999999999,6.0,26.0,0.998,3.18,0.51,9.5,5
8.4,0.665,0.61,2.0,0.11199999999999999,13.0,95.0,0.997,3.16,0.54,9.1,5
12.7,0.6,0.65,2.3,0.063,6.0,25.0,0.9997,3.03,0.57,9.9,5
12.0,0.37,0.76,4.2,0.066,7.0,38.0,1.0004,3.22,0.6,13.0,7
6.6,0.735,0.02,7.9,0.122,68.0,124.0,0.9994,3.47,0.53,9.9,5
11.5,0.59,0.59,2.6,0.087,13.0,49.0,0.9988,3.18,0.65,11.0,6
11.5,0.59,0.59,2.6,0.087,13.0,49.0,0.9988,3.18,0.65,11.0,6
8.7,0.765,0.22,2.3,0.064,9.0,42.0,0.9963,3.1,0.55,9.4,5
6.6,0.735,0.02,7.9,0.122,68.0,124.0,0.9994,3.47,0.53,9.9,5
7.7,0.26,0.3,1.7,0.059000000000000004,20.0,38.0,0.9949,3.29,0.47,10.8,6
12.2,0.48,0.54,2.6,0.085,19.0,64.0,1.0,3.1,0.61,10.5,6
11.4,0.6,0.49,2.7,0.085,10.0,41.0,0.9994,3.15,0.63,10.5,6
7.7,0.69,0.05,2.7,0.075,15.0,27.0,0.9974,3.26,0.61,9.1,5
8.7,0.31,0.46,1.4,0.059000000000000004,11.0,25.0,0.9966,3.36,0.76,10.1,6
9.8,0.44,0.47,2.5,0.063,9.0,28.0,0.9981,3.24,0.65,10.8,6
12.0,0.39,0.66,3.0,0.09300000000000001,12.0,30.0,0.9996,3.18,0.63,10.8,7
10.4,0.34,0.58,3.7,0.174,6.0,16.0,0.997,3.19,0.7,11.3,6
12.5,0.46,0.49,4.5,0.07,26.0,49.0,0.9981,3.05,0.57,9.6,4
9.0,0.43,0.34,2.5,0.08,26.0,86.0,0.9987,3.38,0.62,9.5,6
9.1,0.45,0.35,2.4,0.08,23.0,78.0,0.9987,3.38,0.62,9.5,5
7.1,0.735,0.16,1.9,0.1,15.0,77.0,0.9966,3.27,0.64,9.3,5
9.9,0.4,0.53,6.7,0.09699999999999999,6.0,19.0,0.9986,3.27,0.82,11.7,7
8.8,0.52,0.34,2.7,0.087,24.0,122.0,0.9982,3.26,0.61,9.5,5
8.6,0.725,0.24,6.6,0.11699999999999999,31.0,134.0,1.0014,3.32,1.07,9.3,5
10.6,0.48,0.64,2.2,0.111,6.0,20.0,0.997,3.26,0.66,11.7,6
7.0,0.58,0.12,1.9,0.091,34.0,124.0,0.9956,3.44,0.48,10.5,5
11.9,0.38,0.51,2.0,0.121,7.0,20.0,0.9996,3.24,0.76,10.4,6
6.8,0.77,0.0,1.8,0.066,34.0,52.0,0.9976,3.62,0.68,9.9,5
9.5,0.56,0.33,2.4,0.08900000000000001,35.0,67.0,0.9972,3.28,0.73,11.8,7
6.6,0.84,0.03,2.3,0.059000000000000004,32.0,48.0,0.9952,3.52,0.56,12.3,7
7.7,0.96,0.2,2.0,0.047,15.0,60.0,0.9955,3.36,0.44,10.9,5
10.5,0.24,0.47,2.1,0.066,6.0,24.0,0.9978,3.15,0.9,11.0,7
7.7,0.96,0.2,2.0,0.047,15.0,60.0,0.9955,3.36,0.44,10.9,5
6.6,0.84,0.03,2.3,0.059000000000000004,32.0,48.0,0.9952,3.52,0.56,12.3,7
6.4,0.67,0.08,2.1,0.045,19.0,48.0,0.9949,3.49,0.49,11.4,6
9.5,0.78,0.22,1.9,0.077,6.0,32.0,0.9988,3.26,0.56,10.6,6
9.1,0.52,0.33,1.3,0.07,9.0,30.0,0.9978,3.24,0.6,9.3,5
12.8,0.84,0.63,2.4,0.08800000000000001,13.0,35.0,0.9997,3.1,0.6,10.4,6
10.5,0.24,0.47,2.1,0.066,6.0,24.0,0.9978,3.15,0.9,11.0,7
7.8,0.55,0.35,2.2,0.07400000000000001,21.0,66.0,0.9974,3.25,0.56,9.2,5
11.9,0.37,0.69,2.3,0.078,12.0,24.0,0.9958,3.0,0.65,12.8,6
12.3,0.39,0.63,2.3,0.091,6.0,18.0,1.0004,3.16,0.49,9.5,5
10.4,0.41,0.55,3.2,0.076,22.0,54.0,0.9996,3.15,0.89,9.9,6
12.3,0.39,0.63,2.3,0.091,6.0,18.0,1.0004,3.16,0.49,9.5,5
8.0,0.67,0.3,2.0,0.06,38.0,62.0,0.9958,3.26,0.56,10.2,6
11.1,0.45,0.73,3.2,0.066,6.0,22.0,0.9986,3.17,0.66,11.2,6
10.4,0.41,0.55,3.2,0.076,22.0,54.0,0.9996,3.15,0.89,9.9,6
7.0,0.62,0.18,1.5,0.062,7.0,50.0,0.9951,3.08,0.6,9.3,5
12.6,0.31,0.72,2.2,0.07200000000000001,6.0,29.0,0.9987,2.88,0.82,9.8,8
11.9,0.4,0.65,2.15,0.068,7.0,27.0,0.9988,3.06,0.68,11.3,6
15.6,0.685,0.76,3.7,0.1,6.0,43.0,1.0032,2.95,0.68,11.2,7
10.0,0.44,0.49,2.7,0.077,11.0,19.0,0.9963,3.23,0.63,11.6,7
5.3,0.57,0.01,1.7,0.054000000000000006,5.0,27.0,0.9934,3.57,0.84,12.5,7
9.5,0.735,0.1,2.1,0.079,6.0,31.0,0.9986,3.23,0.56,10.1,6
12.5,0.38,0.6,2.6,0.081,31.0,72.0,0.9996,3.1,0.73,10.5,5
9.3,0.48,0.29,2.1,0.127,6.0,16.0,0.9968,3.22,0.72,11.2,5
8.6,0.53,0.22,2.0,0.1,7.0,27.0,0.9967,3.2,0.56,10.2,6
11.9,0.39,0.69,2.8,0.095,17.0,35.0,0.9994,3.1,0.61,10.8,6
11.9,0.39,0.69,2.8,0.095,17.0,35.0,0.9994,3.1,0.61,10.8,6
8.4,0.37,0.53,1.8,0.413,9.0,26.0,0.9979,3.06,1.06,9.1,6
6.8,0.56,0.03,1.7,0.084,18.0,35.0,0.9968,3.44,0.63,10.0,6
10.4,0.33,0.63,2.8,0.084,5.0,22.0,0.9998,3.26,0.74,11.2,7
7.0,0.23,0.4,1.6,0.063,21.0,67.0,0.9952,3.5,0.63,11.1,5
11.3,0.62,0.67,5.2,0.086,6.0,19.0,0.9988,3.22,0.69,13.4,8
8.9,0.59,0.39,2.3,0.095,5.0,22.0,0.9986,3.37,0.58,10.3,5
9.2,0.63,0.21,2.7,0.09699999999999999,29.0,65.0,0.9988,3.28,0.58,9.6,5
10.4,0.33,0.63,2.8,0.084,5.0,22.0,0.9998,3.26,0.74,11.2,7
11.6,0.58,0.66,2.2,0.07400000000000001,10.0,47.0,1.0008,3.25,0.57,9.0,3
9.2,0.43,0.52,2.3,0.083,14.0,23.0,0.9976,3.35,0.61,11.3,6
8.3,0.615,0.22,2.6,0.087,6.0,19.0,0.9982,3.26,0.61,9.3,5
11.0,0.26,0.68,2.55,0.085,10.0,25.0,0.997,3.18,0.61,11.8,5
8.1,0.66,0.7,2.2,0.098,25.0,129.0,0.9972,3.08,0.53,9.0,5
11.5,0.315,0.54,2.1,0.084,5.0,15.0,0.9987,2.98,0.7,9.2,6
10.0,0.29,0.4,2.9,0.098,10.0,26.0,1.0006,3.48,0.91,9.7,5
10.3,0.5,0.42,2.0,0.069,21.0,51.0,0.9982,3.16,0.72,11.5,6
8.8,0.46,0.45,2.6,0.065,7.0,18.0,0.9947,3.32,0.79,14.0,6
11.4,0.36,0.69,2.1,0.09,6.0,21.0,1.0,3.17,0.62,9.2,6
8.7,0.82,0.02,1.2,0.07,36.0,48.0,0.9952,3.2,0.58,9.8,5
13.0,0.32,0.65,2.6,0.09300000000000001,15.0,47.0,0.9996,3.05,0.61,10.6,5
9.6,0.54,0.42,2.4,0.081,25.0,52.0,0.997,3.2,0.71,11.4,6
12.5,0.37,0.55,2.6,0.083,25.0,68.0,0.9995,3.15,0.82,10.4,6
9.9,0.35,0.55,2.1,0.062,5.0,14.0,0.9971,3.26,0.79,10.6,5
10.5,0.28,0.51,1.7,0.08,10.0,24.0,0.9982,3.2,0.89,9.4,6
9.6,0.68,0.24,2.2,0.087,5.0,28.0,0.9988,3.14,0.6,10.2,5
9.3,0.27,0.41,2.0,0.091,6.0,16.0,0.998,3.28,0.7,9.7,5
10.4,0.24,0.49,1.8,0.075,6.0,20.0,0.9977,3.18,1.06,11.0,6
9.6,0.68,0.24,2.2,0.087,5.0,28.0,0.9988,3.14,0.6,10.2,5
9.4,0.685,0.11,2.7,0.077,6.0,31.0,0.9984,3.19,0.7,10.1,6
10.6,0.28,0.39,15.5,0.069,6.0,23.0,1.0026,3.12,0.66,9.2,5
9.4,0.3,0.56,2.8,0.08,6.0,17.0,0.9964,3.15,0.92,11.7,8
10.6,0.36,0.59,2.2,0.152,6.0,18.0,0.9986,3.04,1.05,9.4,5
10.6,0.36,0.6,2.2,0.152,7.0,18.0,0.9986,3.04,1.06,9.4,5
10.6,0.44,0.68,4.1,0.114,6.0,24.0,0.997,3.06,0.66,13.4,6
10.2,0.67,0.39,1.9,0.054000000000000006,6.0,17.0,0.9976,3.17,0.47,10.0,5
10.2,0.67,0.39,1.9,0.054000000000000006,6.0,17.0,0.9976,3.17,0.47,10.0,5
10.2,0.645,0.36,1.8,0.053,5.0,14.0,0.9982,3.17,0.42,10.0,6
11.6,0.32,0.55,2.8,0.081,35.0,67.0,1.0002,3.32,0.92,10.8,7
9.3,0.39,0.4,2.6,0.073,10.0,26.0,0.9984,3.34,0.75,10.2,6
9.3,0.775,0.27,2.8,0.078,24.0,56.0,0.9984,3.31,0.67,10.6,6
9.2,0.41,0.5,2.5,0.055,12.0,25.0,0.9952,3.34,0.79,13.3,7
8.9,0.4,0.51,2.6,0.052000000000000005,13.0,27.0,0.995,3.32,0.9,13.4,7
8.7,0.69,0.31,3.0,0.086,23.0,81.0,1.0002,3.48,0.74,11.6,6
6.5,0.39,0.23,8.3,0.051,28.0,91.0,0.9952,3.44,0.55,12.1,6
10.7,0.35,0.53,2.6,0.07,5.0,16.0,0.9972,3.15,0.65,11.0,8
7.8,0.52,0.25,1.9,0.081,14.0,38.0,0.9984,3.43,0.65,9.0,6
7.2,0.34,0.32,2.5,0.09,43.0,113.0,0.9966,3.32,0.79,11.1,5
10.7,0.35,0.53,2.6,0.07,5.0,16.0,0.9972,3.15,0.65,11.0,8
8.7,0.69,0.31,3.0,0.086,23.0,81.0,1.0002,3.48,0.74,11.6,6
7.8,0.52,0.25,1.9,0.081,14.0,38.0,0.9984,3.43,0.65,9.0,6
10.4,0.44,0.73,6.55,0.07400000000000001,38.0,76.0,0.9990000000000001,3.17,0.85,12.0,7
10.4,0.44,0.73,6.55,0.07400000000000001,38.0,76.0,0.9990000000000001,3.17,0.85,12.0,7
10.5,0.26,0.47,1.9,0.078,6.0,24.0,0.9976,3.18,1.04,10.9,7
10.5,0.24,0.42,1.8,0.077,6.0,22.0,0.9976,3.21,1.05,10.8,7
10.2,0.49,0.63,2.9,0.07200000000000001,10.0,26.0,0.9968,3.16,0.78,12.5,7
10.4,0.24,0.46,1.8,0.075,6.0,21.0,0.9976,3.25,1.02,10.8,7
11.2,0.67,0.55,2.3,0.084,6.0,13.0,1.0,3.17,0.71,9.5,6
10.0,0.59,0.31,2.2,0.09,26.0,62.0,0.9994,3.18,0.63,10.2,6
13.3,0.29,0.75,2.8,0.084,23.0,43.0,0.9986,3.04,0.68,11.4,7
12.4,0.42,0.49,4.6,0.073,19.0,43.0,0.9978,3.02,0.61,9.5,5
10.0,0.59,0.31,2.2,0.09,26.0,62.0,0.9994,3.18,0.63,10.2,6
10.7,0.4,0.48,2.1,0.125,15.0,49.0,0.998,3.03,0.81,9.7,6
10.5,0.51,0.64,2.4,0.107,6.0,15.0,0.9973,3.09,0.66,11.8,7
10.5,0.51,0.64,2.4,0.107,6.0,15.0,0.9973,3.09,0.66,11.8,7
8.5,0.655,0.49,6.1,0.122,34.0,151.0,1.001,3.31,1.14,9.3,5
12.5,0.6,0.49,4.3,0.1,5.0,14.0,1.001,3.25,0.74,11.9,6
10.4,0.61,0.49,2.1,0.2,5.0,16.0,0.9994,3.16,0.63,8.4,3
10.9,0.21,0.49,2.8,0.08800000000000001,11.0,32.0,0.9972,3.22,0.68,11.7,6
7.3,0.365,0.49,2.5,0.08800000000000001,39.0,106.0,0.9966,3.36,0.78,11.0,5
9.8,0.25,0.49,2.7,0.08800000000000001,15.0,33.0,0.9982,3.42,0.9,10.0,6
7.6,0.41,0.49,2.0,0.08800000000000001,16.0,43.0,0.998,3.48,0.64,9.1,5
8.2,0.39,0.49,2.3,0.099,47.0,133.0,0.9979,3.38,0.99,9.8,5
9.3,0.4,0.49,2.5,0.085,38.0,142.0,0.9978,3.22,0.55,9.4,5
9.2,0.43,0.49,2.4,0.086,23.0,116.0,0.9976,3.23,0.64,9.5,5
10.4,0.64,0.24,2.8,0.105,29.0,53.0,0.9998,3.24,0.67,9.9,5
7.3,0.365,0.49,2.5,0.08800000000000001,39.0,106.0,0.9966,3.36,0.78,11.0,5
7.0,0.38,0.49,2.5,0.09699999999999999,33.0,85.0,0.9962,3.39,0.77,11.4,6
8.2,0.42,0.49,2.6,0.084,32.0,55.0,0.9988,3.34,0.75,8.7,6
9.9,0.63,0.24,2.4,0.077,6.0,33.0,0.9974,3.09,0.57,9.4,5
9.1,0.22,0.24,2.1,0.078,1.0,28.0,0.9990000000000001,3.41,0.87,10.3,6
11.9,0.38,0.49,2.7,0.098,12.0,42.0,1.0004,3.16,0.61,10.3,5
11.9,0.38,0.49,2.7,0.098,12.0,42.0,1.0004,3.16,0.61,10.3,5
10.3,0.27,0.24,2.1,0.07200000000000001,15.0,33.0,0.9956,3.22,0.66,12.8,6
10.0,0.48,0.24,2.7,0.102,13.0,32.0,1.0,3.28,0.56,10.0,6
9.1,0.22,0.24,2.1,0.078,1.0,28.0,0.9990000000000001,3.41,0.87,10.3,6
9.9,0.63,0.24,2.4,0.077,6.0,33.0,0.9974,3.09,0.57,9.4,5
8.1,0.825,0.24,2.1,0.084,5.0,13.0,0.9972,3.37,0.77,10.7,6
12.9,0.35,0.49,5.8,0.066,5.0,35.0,1.0014,3.2,0.66,12.0,7
11.2,0.5,0.74,5.15,0.1,5.0,17.0,0.9996,3.22,0.62,11.2,5
9.2,0.59,0.24,3.3,0.10099999999999999,20.0,47.0,0.9988,3.26,0.67,9.6,5
9.5,0.46,0.49,6.3,0.064,5.0,17.0,0.9988,3.21,0.73,11.0,6
9.3,0.715,0.24,2.1,0.07,5.0,20.0,0.9966,3.12,0.59,9.9,5
11.2,0.66,0.24,2.5,0.085,16.0,53.0,0.9993,3.06,0.72,11.0,6
14.3,0.31,0.74,1.8,0.075,6.0,15.0,1.0008,2.86,0.79,8.4,6
9.1,0.47,0.49,2.6,0.094,38.0,106.0,0.9982,3.08,0.59,9.1,5
7.5,0.55,0.24,2.0,0.078,10.0,28.0,0.9983,3.45,0.78,9.5,6
10.6,0.31,0.49,2.5,0.067,6.0,21.0,0.9987,3.26,0.86,10.7,6
12.4,0.35,0.49,2.6,0.079,27.0,69.0,0.9994,3.12,0.75,10.4,6
9.0,0.53,0.49,1.9,0.171,6.0,25.0,0.9975,3.27,0.61,9.4,6
6.8,0.51,0.01,2.1,0.07400000000000001,9.0,25.0,0.9958,3.33,0.56,9.5,6
9.4,0.43,0.24,2.8,0.092,14.0,45.0,0.998,3.19,0.73,10.0,6
9.5,0.46,0.24,2.7,0.092,14.0,44.0,0.998,3.12,0.74,10.0,6
5.0,1.04,0.24,1.6,0.05,32.0,96.0,0.9934,3.74,0.62,11.5,5
15.5,0.645,0.49,4.2,0.095,10.0,23.0,1.00315,2.92,0.74,11.1,5
15.5,0.645,0.49,4.2,0.095,10.0,23.0,1.00315,2.92,0.74,11.1,5
10.9,0.53,0.49,4.6,0.11800000000000001,10.0,17.0,1.0002,3.07,0.56,11.7,6
15.6,0.645,0.49,4.2,0.095,10.0,23.0,1.00315,2.92,0.74,11.1,5
10.9,0.53,0.49,4.6,0.11800000000000001,10.0,17.0,1.0002,3.07,0.56,11.7,6
13.0,0.47,0.49,4.3,0.085,6.0,47.0,1.0021,3.3,0.68,12.7,6
12.7,0.6,0.49,2.8,0.075,5.0,19.0,0.9994,3.14,0.57,11.4,5
9.0,0.44,0.49,2.4,0.078,26.0,121.0,0.9978,3.23,0.58,9.2,5
9.0,0.54,0.49,2.9,0.094,41.0,110.0,0.9982,3.08,0.61,9.2,5
7.6,0.29,0.49,2.7,0.092,25.0,60.0,0.9971,3.31,0.61,10.1,6
13.0,0.47,0.49,4.3,0.085,6.0,47.0,1.0021,3.3,0.68,12.7,6
12.7,0.6,0.49,2.8,0.075,5.0,19.0,0.9994,3.14,0.57,11.4,5
8.7,0.7,0.24,2.5,0.226,5.0,15.0,0.9991,3.32,0.6,9.0,6
8.7,0.7,0.24,2.5,0.226,5.0,15.0,0.9991,3.32,0.6,9.0,6
9.8,0.5,0.49,2.6,0.25,5.0,20.0,0.9990000000000001,3.31,0.79,10.7,6
6.2,0.36,0.24,2.2,0.095,19.0,42.0,0.9946,3.57,0.57,11.7,6
11.5,0.35,0.49,3.3,0.07,10.0,37.0,1.0003,3.32,0.91,11.0,6
6.2,0.36,0.24,2.2,0.095,19.0,42.0,0.9946,3.57,0.57,11.7,6
10.2,0.24,0.49,2.4,0.075,10.0,28.0,0.9978,3.14,0.61,10.4,5
10.5,0.59,0.49,2.1,0.07,14.0,47.0,0.9991,3.3,0.56,9.6,4
10.6,0.34,0.49,3.2,0.078,20.0,78.0,0.9992,3.19,0.7,10.0,6
12.3,0.27,0.49,3.1,0.079,28.0,46.0,0.9993,3.2,0.8,10.2,6
9.9,0.5,0.24,2.3,0.10300000000000001,6.0,14.0,0.9978,3.34,0.52,10.0,4
8.8,0.44,0.49,2.8,0.083,18.0,111.0,0.9982,3.3,0.6,9.5,5
8.8,0.47,0.49,2.9,0.085,17.0,110.0,0.9982,3.29,0.6,9.8,5
10.6,0.31,0.49,2.2,0.063,18.0,40.0,0.9976,3.14,0.51,9.8,6
12.3,0.5,0.49,2.2,0.08900000000000001,5.0,14.0,1.0002,3.19,0.44,9.6,5
12.3,0.5,0.49,2.2,0.08900000000000001,5.0,14.0,1.0002,3.19,0.44,9.6,5
11.7,0.49,0.49,2.2,0.083,5.0,15.0,1.0,3.19,0.43,9.2,5
12.0,0.28,0.49,1.9,0.07400000000000001,10.0,21.0,0.9976,2.98,0.66,9.9,7
11.8,0.33,0.49,3.4,0.09300000000000001,54.0,80.0,1.0002,3.3,0.76,10.7,7
7.6,0.51,0.24,2.4,0.091,8.0,38.0,0.998,3.47,0.66,9.6,6
11.1,0.31,0.49,2.7,0.094,16.0,47.0,0.9986,3.12,1.02,10.6,7
7.3,0.73,0.24,1.9,0.10800000000000001,18.0,102.0,0.9967,3.26,0.59,9.3,5
5.0,0.42,0.24,2.0,0.06,19.0,50.0,0.9917,3.72,0.74,14.0,8
10.2,0.29,0.49,2.6,0.059000000000000004,5.0,13.0,0.9976,3.05,0.74,10.5,7
9.0,0.45,0.49,2.6,0.084,21.0,75.0,0.9987,3.35,0.57,9.7,5
6.6,0.39,0.49,1.7,0.07,23.0,149.0,0.9922,3.12,0.5,11.5,6
9.0,0.45,0.49,2.6,0.084,21.0,75.0,0.9987,3.35,0.57,9.7,5
9.9,0.49,0.58,3.5,0.094,9.0,43.0,1.0004,3.29,0.58,9.0,5
7.9,0.72,0.17,2.6,0.096,20.0,38.0,0.9978,3.4,0.53,9.5,5
8.9,0.595,0.41,7.9,0.086,30.0,109.0,0.9998,3.27,0.57,9.3,5
12.4,0.4,0.51,2.0,0.059000000000000004,6.0,24.0,0.9994,3.04,0.6,9.3,6
11.9,0.58,0.58,1.9,0.071,5.0,18.0,0.998,3.09,0.63,10.0,6
8.5,0.585,0.18,2.1,0.078,5.0,30.0,0.9967,3.2,0.48,9.8,6
12.7,0.59,0.45,2.3,0.08199999999999999,11.0,22.0,1.0,3.0,0.7,9.3,6
8.2,0.915,0.27,2.1,0.08800000000000001,7.0,23.0,0.9962,3.26,0.47,10.0,4
13.2,0.46,0.52,2.2,0.071,12.0,35.0,1.0006,3.1,0.56,9.0,6
7.7,0.835,0.0,2.6,0.081,6.0,14.0,0.9975,3.3,0.52,9.3,5
13.2,0.46,0.52,2.2,0.071,12.0,35.0,1.0006,3.1,0.56,9.0,6
8.3,0.58,0.13,2.9,0.096,14.0,63.0,0.9984,3.17,0.62,9.1,6
8.3,0.6,0.13,2.6,0.085,6.0,24.0,0.9984,3.31,0.59,9.2,6
9.4,0.41,0.48,4.6,0.07200000000000001,10.0,20.0,0.9973,3.34,0.79,12.2,7
8.8,0.48,0.41,3.3,0.092,26.0,52.0,0.9982,3.31,0.53,10.5,6
10.1,0.65,0.37,5.1,0.11,11.0,65.0,1.0026,3.32,0.64,10.4,6
6.3,0.36,0.19,3.2,0.075,15.0,39.0,0.9956,3.56,0.52,12.7,6
8.8,0.24,0.54,2.5,0.083,25.0,57.0,0.9983,3.39,0.54,9.2,5
13.2,0.38,0.55,2.7,0.081,5.0,16.0,1.0006,2.98,0.54,9.4,5
7.5,0.64,0.0,2.4,0.077,18.0,29.0,0.9965,3.32,0.6,10.0,6
8.2,0.39,0.38,1.5,0.057999999999999996,10.0,29.0,0.9962,3.26,0.74,9.8,5
9.2,0.755,0.18,2.2,0.14800000000000002,10.0,103.0,0.9969,2.87,1.36,10.2,6
9.6,0.6,0.5,2.3,0.079,28.0,71.0,0.9997,3.5,0.57,9.7,5
9.6,0.6,0.5,2.3,0.079,28.0,71.0,0.9997,3.5,0.57,9.7,5
11.5,0.31,0.51,2.2,0.079,14.0,28.0,0.9982,3.03,0.93,9.8,6
11.4,0.46,0.5,2.7,0.122,4.0,17.0,1.0006,3.13,0.7,10.2,5
11.3,0.37,0.41,2.3,0.08800000000000001,6.0,16.0,0.9988,3.09,0.8,9.3,5
8.3,0.54,0.24,3.4,0.076,16.0,112.0,0.9976,3.27,0.61,9.4,5
8.2,0.56,0.23,3.4,0.078,14.0,104.0,0.9976,3.28,0.62,9.4,5
10.0,0.58,0.22,1.9,0.08,9.0,32.0,0.9974,3.13,0.55,9.5,5
7.9,0.51,0.25,2.9,0.077,21.0,45.0,0.9974,3.49,0.96,12.1,6
6.8,0.69,0.0,5.6,0.124,21.0,58.0,0.9997,3.46,0.72,10.2,5
6.8,0.69,0.0,5.6,0.124,21.0,58.0,0.9997,3.46,0.72,10.2,5
8.8,0.6,0.29,2.2,0.098,5.0,15.0,0.9988,3.36,0.49,9.1,5
8.8,0.6,0.29,2.2,0.098,5.0,15.0,0.9988,3.36,0.49,9.1,5
8.7,0.54,0.26,2.5,0.09699999999999999,7.0,31.0,0.9976,3.27,0.6,9.3,6
7.6,0.685,0.23,2.3,0.111,20.0,84.0,0.9964,3.21,0.61,9.3,5
8.7,0.54,0.26,2.5,0.09699999999999999,7.0,31.0,0.9976,3.27,0.6,9.3,6
10.4,0.28,0.54,2.7,0.105,5.0,19.0,0.9988,3.25,0.63,9.5,5
7.6,0.41,0.14,3.0,0.087,21.0,43.0,0.9964,3.32,0.57,10.5,6
10.1,0.935,0.22,3.4,0.105,11.0,86.0,1.001,3.43,0.64,11.3,4
7.9,0.35,0.21,1.9,0.073,46.0,102.0,0.9964,3.27,0.58,9.5,5
8.7,0.84,0.0,1.4,0.065,24.0,33.0,0.9954,3.27,0.55,9.7,5
9.6,0.88,0.28,2.4,0.086,30.0,147.0,0.9979,3.24,0.53,9.4,5
9.5,0.885,0.27,2.3,0.084,31.0,145.0,0.9978,3.24,0.53,9.4,5
7.7,0.915,0.12,2.2,0.14300000000000002,7.0,23.0,0.9964,3.35,0.65,10.2,7
8.9,0.29,0.35,1.9,0.067,25.0,57.0,0.997,3.18,1.36,10.3,6
9.9,0.54,0.45,2.3,0.071,16.0,40.0,0.9991,3.39,0.62,9.4,5
9.5,0.59,0.44,2.3,0.071,21.0,68.0,0.9992,3.46,0.63,9.5,5
9.9,0.54,0.45,2.3,0.071,16.0,40.0,0.9991,3.39,0.62,9.4,5
9.5,0.59,0.44,2.3,0.071,21.0,68.0,0.9992,3.46,0.63,9.5,5
9.9,0.54,0.45,2.3,0.071,16.0,40.0,0.9991,3.39,0.62,9.4,5
7.8,0.64,0.1,6.0,0.115,5.0,11.0,0.9984,3.37,0.69,10.1,7
7.3,0.67,0.05,3.6,0.107,6.0,20.0,0.9972,3.4,0.63,10.1,5
8.3,0.845,0.01,2.2,0.07,5.0,14.0,0.9967,3.32,0.58,11.0,4
8.7,0.48,0.3,2.8,0.066,10.0,28.0,0.9964,3.33,0.67,11.2,7
6.7,0.42,0.27,8.6,0.068,24.0,148.0,0.9948,3.16,0.57,11.3,6
10.7,0.43,0.39,2.2,0.106,8.0,32.0,0.9986,2.89,0.5,9.6,5
9.8,0.88,0.25,2.5,0.10400000000000001,35.0,155.0,1.001,3.41,0.67,11.2,5
15.9,0.36,0.65,7.5,0.096,22.0,71.0,0.9976,2.98,0.84,14.9,5
9.4,0.33,0.59,2.8,0.079,9.0,30.0,0.9976,3.12,0.54,12.0,6
8.6,0.47,0.47,2.4,0.07400000000000001,7.0,29.0,0.9979,3.08,0.46,9.5,5
9.7,0.55,0.17,2.9,0.087,20.0,53.0,1.0004,3.14,0.61,9.4,5
10.7,0.43,0.39,2.2,0.106,8.0,32.0,0.9986,2.89,0.5,9.6,5
12.0,0.5,0.59,1.4,0.073,23.0,42.0,0.998,2.92,0.68,10.5,7
7.2,0.52,0.07,1.4,0.07400000000000001,5.0,20.0,0.9973,3.32,0.81,9.6,6
7.1,0.84,0.02,4.4,0.096,5.0,13.0,0.997,3.41,0.57,11.0,4
7.2,0.52,0.07,1.4,0.07400000000000001,5.0,20.0,0.9973,3.32,0.81,9.6,6
7.5,0.42,0.31,1.6,0.08,15.0,42.0,0.9978,3.31,0.64,9.0,5
7.2,0.57,0.06,1.6,0.076,9.0,27.0,0.9972,3.36,0.7,9.6,6
10.1,0.28,0.46,1.8,0.05,5.0,13.0,0.9974,3.04,0.79,10.2,6
12.1,0.4,0.52,2.0,0.092,15.0,54.0,1.0,3.03,0.66,10.2,5
9.4,0.59,0.14,2.0,0.084,25.0,48.0,0.9981,3.14,0.56,9.7,5
8.3,0.49,0.36,1.8,0.222,6.0,16.0,0.998,3.18,0.6,9.5,6
11.3,0.34,0.45,2.0,0.08199999999999999,6.0,15.0,0.9988,2.94,0.66,9.2,6
10.0,0.73,0.43,2.3,0.059000000000000004,15.0,31.0,0.9966,3.15,0.57,11.0,5
11.3,0.34,0.45,2.0,0.08199999999999999,6.0,15.0,0.9988,2.94,0.66,9.2,6
6.9,0.4,0.24,2.5,0.083,30.0,45.0,0.9959,3.26,0.58,10.0,5
8.2,0.73,0.21,1.7,0.07400000000000001,5.0,13.0,0.9968,3.2,0.52,9.5,5
9.8,1.24,0.34,2.0,0.079,32.0,151.0,0.998,3.15,0.53,9.5,5
8.2,0.73,0.21,1.7,0.07400000000000001,5.0,13.0,0.9968,3.2,0.52,9.5,5
10.8,0.4,0.41,2.2,0.084,7.0,17.0,0.9984,3.08,0.67,9.3,6
9.3,0.41,0.39,2.2,0.064,12.0,31.0,0.9984,3.26,0.65,10.2,5
10.8,0.4,0.41,2.2,0.084,7.0,17.0,0.9984,3.08,0.67,9.3,6
8.6,0.8,0.11,2.3,0.084,12.0,31.0,0.9979,3.4,0.48,9.9,5
8.3,0.78,0.1,2.6,0.081,45.0,87.0,0.9983,3.48,0.53,10.0,5
10.8,0.26,0.45,3.3,0.06,20.0,49.0,0.9972,3.13,0.54,9.6,5
13.3,0.43,0.58,1.9,0.07,15.0,40.0,1.0004,3.06,0.49,9.0,5
8.0,0.45,0.23,2.2,0.094,16.0,29.0,0.9962,3.21,0.49,10.2,6
8.5,0.46,0.31,2.25,0.078,32.0,58.0,0.998,3.33,0.54,9.8,5
8.1,0.78,0.23,2.6,0.059000000000000004,5.0,15.0,0.997,3.37,0.56,11.3,5
9.8,0.98,0.32,2.3,0.078,35.0,152.0,0.998,3.25,0.48,9.4,5
8.1,0.78,0.23,2.6,0.059000000000000004,5.0,15.0,0.997,3.37,0.56,11.3,5
7.1,0.65,0.18,1.8,0.07,13.0,40.0,0.997,3.44,0.6,9.1,5
9.1,0.64,0.23,3.1,0.095,13.0,38.0,0.9998,3.28,0.59,9.7,5
7.7,0.66,0.04,1.6,0.039,4.0,9.0,0.9962,3.4,0.47,9.4,5
8.1,0.38,0.48,1.8,0.157,5.0,17.0,0.9976,3.3,1.05,9.4,5
7.4,1.185,0.0,4.25,0.09699999999999999,5.0,14.0,0.9966,3.63,0.54,10.7,3
9.2,0.92,0.24,2.6,0.087,12.0,93.0,0.9998,3.48,0.54,9.8,5
8.6,0.49,0.51,2.0,0.42200000000000004,16.0,62.0,0.9979,3.03,1.17,9.0,5
9.0,0.48,0.32,2.8,0.084,21.0,122.0,0.9984,3.32,0.62,9.4,5
9.0,0.47,0.31,2.7,0.084,24.0,125.0,0.9984,3.31,0.61,9.4,5
5.1,0.47,0.02,1.3,0.034,18.0,44.0,0.9921,3.9,0.62,12.8,6
7.0,0.65,0.02,2.1,0.066,8.0,25.0,0.9972,3.47,0.67,9.5,6
7.0,0.65,0.02,2.1,0.066,8.0,25.0,0.9972,3.47,0.67,9.5,6
9.4,0.615,0.28,3.2,0.087,18.0,72.0,1.0001,3.31,0.53,9.7,5
11.8,0.38,0.55,2.1,0.071,5.0,19.0,0.9986,3.11,0.62,10.8,6
10.6,1.02,0.43,2.9,0.076,26.0,88.0,0.9984,3.08,0.57,10.1,6
7.0,0.65,0.02,2.1,0.066,8.0,25.0,0.9972,3.47,0.67,9.5,6
7.0,0.64,0.02,2.1,0.067,9.0,23.0,0.997,3.47,0.67,9.4,6
7.5,0.38,0.48,2.6,0.073,22.0,84.0,0.9972,3.32,0.7,9.6,4
9.1,0.765,0.04,1.6,0.078,4.0,14.0,0.998,3.29,0.54,9.7,4
8.4,1.035,0.15,6.0,0.073,11.0,54.0,0.9990000000000001,3.37,0.49,9.9,5
7.0,0.78,0.08,2.0,0.09300000000000001,10.0,19.0,0.9956,3.4,0.47,10.0,5
7.4,0.49,0.19,3.0,0.077,16.0,37.0,0.9966,3.37,0.51,10.5,5
7.8,0.545,0.12,2.5,0.068,11.0,35.0,0.996,3.34,0.61,11.6,6
9.7,0.31,0.47,1.6,0.062,13.0,33.0,0.9983,3.27,0.66,10.0,6
10.6,1.025,0.43,2.8,0.08,21.0,84.0,0.9985,3.06,0.57,10.1,5
8.9,0.565,0.34,3.0,0.09300000000000001,16.0,112.0,0.9998,3.38,0.61,9.5,5
8.7,0.69,0.0,3.2,0.084,13.0,33.0,0.9992,3.36,0.45,9.4,5
8.0,0.43,0.36,2.3,0.075,10.0,48.0,0.9976,3.34,0.46,9.4,5
9.9,0.74,0.28,2.6,0.078,21.0,77.0,0.998,3.28,0.51,9.8,5
7.2,0.49,0.18,2.7,0.069,13.0,34.0,0.9967,3.29,0.48,9.2,6
8.0,0.43,0.36,2.3,0.075,10.0,48.0,0.9976,3.34,0.46,9.4,5
7.6,0.46,0.11,2.6,0.079,12.0,49.0,0.9968,3.21,0.57,10.0,5
8.4,0.56,0.04,2.0,0.08199999999999999,10.0,22.0,0.9976,3.22,0.44,9.6,5
7.1,0.66,0.0,3.9,0.086,17.0,45.0,0.9976,3.46,0.54,9.5,5
8.4,0.56,0.04,2.0,0.08199999999999999,10.0,22.0,0.9976,3.22,0.44,9.6,5
8.9,0.48,0.24,2.85,0.094,35.0,106.0,0.9982,3.1,0.53,9.2,5
7.6,0.42,0.08,2.7,0.084,15.0,48.0,0.9968,3.21,0.59,10.0,5
7.1,0.31,0.3,2.2,0.053,36.0,127.0,0.9965,2.94,1.62,9.5,5
7.5,1.115,0.1,3.1,0.086,5.0,12.0,0.9958,3.54,0.6,11.2,4
9.0,0.66,0.17,3.0,0.077,5.0,13.0,0.9976,3.29,0.55,10.4,5
8.1,0.72,0.09,2.8,0.084,18.0,49.0,0.9994,3.43,0.72,11.1,6
6.4,0.57,0.02,1.8,0.067,4.0,11.0,0.997,3.46,0.68,9.5,5
6.4,0.57,0.02,1.8,0.067,4.0,11.0,0.997,3.46,0.68,9.5,5
6.4,0.865,0.03,3.2,0.071,27.0,58.0,0.995,3.61,0.49,12.7,6
9.5,0.55,0.66,2.3,0.387,12.0,37.0,0.9982,3.17,0.67,9.6,5
8.9,0.875,0.13,3.45,0.08800000000000001,4.0,14.0,0.9994,3.44,0.52,11.5,5
7.3,0.835,0.03,2.1,0.092,10.0,19.0,0.9966,3.39,0.47,9.6,5
7.0,0.45,0.34,2.7,0.08199999999999999,16.0,72.0,0.998,3.55,0.6,9.5,5
7.7,0.56,0.2,2.0,0.075,9.0,39.0,0.9987,3.48,0.62,9.3,5
7.7,0.965,0.1,2.1,0.11199999999999999,11.0,22.0,0.9963,3.26,0.5,9.5,5
7.7,0.965,0.1,2.1,0.11199999999999999,11.0,22.0,0.9963,3.26,0.5,9.5,5
8.2,0.59,0.0,2.5,0.09300000000000001,19.0,58.0,1.0002,3.5,0.65,9.3,6
9.0,0.46,0.23,2.8,0.092,28.0,104.0,0.9983,3.1,0.56,9.2,5
9.0,0.69,0.0,2.4,0.08800000000000001,19.0,38.0,0.9990000000000001,3.35,0.6,9.3,5
8.3,0.76,0.29,4.2,0.075,12.0,16.0,0.9965,3.45,0.68,11.5,6
9.2,0.53,0.24,2.6,0.078,28.0,139.0,0.9978799999999999,3.21,0.57,9.5,5
6.5,0.615,0.0,1.9,0.065,9.0,18.0,0.9972,3.46,0.65,9.2,5
11.6,0.41,0.58,2.8,0.096,25.0,101.0,1.00024,3.13,0.53,10.0,5
11.1,0.39,0.54,2.7,0.095,21.0,101.0,1.0001,3.13,0.51,9.5,5
7.3,0.51,0.18,2.1,0.07,12.0,28.0,0.9976799999999999,3.52,0.73,9.5,6
8.2,0.34,0.38,2.5,0.08,12.0,57.0,0.9978,3.3,0.47,9.0,6
8.6,0.33,0.4,2.6,0.083,16.0,68.0,0.99782,3.3,0.48,9.4,5
7.2,0.5,0.18,2.1,0.071,12.0,31.0,0.99761,3.52,0.72,9.6,6
7.3,0.51,0.18,2.1,0.07,12.0,28.0,0.9976799999999999,3.52,0.73,9.5,6
8.3,0.65,0.1,2.9,0.08900000000000001,17.0,40.0,0.99803,3.29,0.55,9.5,5
8.3,0.65,0.1,2.9,0.08900000000000001,17.0,40.0,0.99803,3.29,0.55,9.5,5
7.6,0.54,0.13,2.5,0.09699999999999999,24.0,66.0,0.99785,3.39,0.61,9.4,5
8.3,0.65,0.1,2.9,0.08900000000000001,17.0,40.0,0.99803,3.29,0.55,9.5,5
7.8,0.48,0.68,1.7,0.415,14.0,32.0,0.99656,3.09,1.06,9.1,6
7.8,0.91,0.07,1.9,0.057999999999999996,22.0,47.0,0.99525,3.51,0.43,10.7,6
6.3,0.98,0.01,2.0,0.057,15.0,33.0,0.9948799999999999,3.6,0.46,11.2,6
8.1,0.87,0.0,2.2,0.084,10.0,31.0,0.99656,3.25,0.5,9.8,5
8.1,0.87,0.0,2.2,0.084,10.0,31.0,0.99656,3.25,0.5,9.8,5
8.8,0.42,0.21,2.5,0.092,33.0,88.0,0.99823,3.19,0.52,9.2,5
9.0,0.58,0.25,2.8,0.075,9.0,104.0,0.99779,3.23,0.57,9.7,5
9.3,0.655,0.26,2.0,0.096,5.0,35.0,0.9973799999999999,3.25,0.42,9.6,5
8.8,0.7,0.0,1.7,0.069,8.0,19.0,0.9970100000000001,3.31,0.53,10.0,6
9.3,0.655,0.26,2.0,0.096,5.0,35.0,0.9973799999999999,3.25,0.42,9.6,5
9.1,0.68,0.11,2.8,0.09300000000000001,11.0,44.0,0.9988799999999999,3.31,0.55,9.5,6
9.2,0.67,0.1,3.0,0.091,12.0,48.0,0.9988799999999999,3.31,0.54,9.5,6
8.8,0.59,0.18,2.9,0.08900000000000001,12.0,74.0,0.9973799999999999,3.14,0.54,9.4,5
7.5,0.6,0.32,2.7,0.10300000000000001,13.0,98.0,0.9993799999999999,3.45,0.62,9.5,5
7.1,0.59,0.02,2.3,0.08199999999999999,24.0,94.0,0.99744,3.55,0.53,9.7,6
7.9,0.72,0.01,1.9,0.076,7.0,32.0,0.9966799999999999,3.39,0.54,9.6,5
7.1,0.59,0.02,2.3,0.08199999999999999,24.0,94.0,0.99744,3.55,0.53,9.7,6
9.4,0.685,0.26,2.4,0.08199999999999999,23.0,143.0,0.9978,3.28,0.55,9.4,5
9.5,0.57,0.27,2.3,0.08199999999999999,23.0,144.0,0.99782,3.27,0.55,9.4,5
7.9,0.4,0.29,1.8,0.157,1.0,44.0,0.9973,3.3,0.92,9.5,6
7.9,0.4,0.3,1.8,0.157,2.0,45.0,0.9972700000000001,3.31,0.91,9.5,6
7.2,1.0,0.0,3.0,0.102,7.0,16.0,0.9958600000000001,3.43,0.46,10.0,5
6.9,0.765,0.18,2.4,0.243,5.5,48.0,0.9961200000000001,3.4,0.6,10.3,6
6.9,0.635,0.17,2.4,0.24100000000000002,6.0,18.0,0.9961,3.4,0.59,10.3,6
8.3,0.43,0.3,3.4,0.079,7.0,34.0,0.9978799999999999,3.36,0.61,10.5,5
7.1,0.52,0.03,2.6,0.076,21.0,92.0,0.99745,3.5,0.6,9.8,5
7.0,0.57,0.0,2.0,0.19,12.0,45.0,0.9967600000000001,3.31,0.6,9.4,6
6.5,0.46,0.14,2.4,0.114,9.0,37.0,0.9973200000000001,3.66,0.65,9.8,5
9.0,0.82,0.05,2.4,0.081,26.0,96.0,0.9981399999999999,3.36,0.53,10.0,5
6.5,0.46,0.14,2.4,0.114,9.0,37.0,0.9973200000000001,3.66,0.65,9.8,5
7.1,0.59,0.01,2.5,0.077,20.0,85.0,0.99746,3.55,0.59,9.8,5
9.9,0.35,0.41,2.3,0.083,11.0,61.0,0.9982,3.21,0.5,9.5,5
9.9,0.35,0.41,2.3,0.083,11.0,61.0,0.9982,3.21,0.5,9.5,5
10.0,0.56,0.24,2.2,0.079,19.0,58.0,0.9991,3.18,0.56,10.1,6
10.0,0.56,0.24,2.2,0.079,19.0,58.0,0.9991,3.18,0.56,10.1,6
8.6,0.63,0.17,2.9,0.099,21.0,119.0,0.998,3.09,0.52,9.3,5
7.4,0.37,0.43,2.6,0.08199999999999999,18.0,82.0,0.99708,3.33,0.68,9.7,6
8.8,0.64,0.17,2.9,0.084,25.0,130.0,0.99818,3.23,0.54,9.6,5
7.1,0.61,0.02,2.5,0.081,17.0,87.0,0.99745,3.48,0.6,9.7,6
7.7,0.6,0.0,2.6,0.055,7.0,13.0,0.99639,3.38,0.56,10.8,5
10.1,0.27,0.54,2.3,0.065,7.0,26.0,0.99531,3.17,0.53,12.5,6
10.8,0.89,0.3,2.6,0.132,7.0,60.0,0.9978600000000001,2.99,1.18,10.2,5
8.7,0.46,0.31,2.5,0.126,24.0,64.0,0.99746,3.1,0.74,9.6,5
9.3,0.37,0.44,1.6,0.038,21.0,42.0,0.99526,3.24,0.81,10.8,7
9.4,0.5,0.34,3.6,0.08199999999999999,5.0,14.0,0.9987,3.29,0.52,10.7,6
9.4,0.5,0.34,3.6,0.08199999999999999,5.0,14.0,0.9987,3.29,0.52,10.7,6
7.2,0.61,0.08,4.0,0.08199999999999999,26.0,108.0,0.99641,3.25,0.51,9.4,5
8.6,0.55,0.09,3.3,0.068,8.0,17.0,0.99735,3.23,0.44,10.0,5
5.1,0.585,0.0,1.7,0.044000000000000004,14.0,86.0,0.99264,3.56,0.94,12.9,7
7.7,0.56,0.08,2.5,0.114,14.0,46.0,0.9971,3.24,0.66,9.6,6
8.4,0.52,0.22,2.7,0.084,4.0,18.0,0.99682,3.26,0.57,9.9,6
8.2,0.28,0.4,2.4,0.052000000000000005,4.0,10.0,0.99356,3.33,0.7,12.8,7
8.4,0.25,0.39,2.0,0.040999999999999995,4.0,10.0,0.9938600000000001,3.27,0.71,12.5,7
8.2,0.28,0.4,2.4,0.052000000000000005,4.0,10.0,0.99356,3.33,0.7,12.8,7
7.4,0.53,0.12,1.9,0.165,4.0,12.0,0.99702,3.26,0.86,9.2,5
7.6,0.48,0.31,2.8,0.07,4.0,15.0,0.9969299999999999,3.22,0.55,10.3,6
7.3,0.49,0.1,2.6,0.068,4.0,14.0,0.9956200000000001,3.3,0.47,10.5,5
12.9,0.5,0.55,2.8,0.07200000000000001,7.0,24.0,1.0001200000000001,3.09,0.68,10.9,6
10.8,0.45,0.33,2.5,0.099,20.0,38.0,0.99818,3.24,0.71,10.8,5
6.9,0.39,0.24,2.1,0.102,4.0,7.0,0.9946200000000001,3.44,0.58,11.4,4
12.6,0.41,0.54,2.8,0.10300000000000001,19.0,41.0,0.99939,3.21,0.76,11.3,6
10.8,0.45,0.33,2.5,0.099,20.0,38.0,0.99818,3.24,0.71,10.8,5
9.8,0.51,0.19,3.2,0.081,8.0,30.0,0.9984,3.23,0.58,10.5,6
10.8,0.29,0.42,1.6,0.084,19.0,27.0,0.99545,3.28,0.73,11.9,6
7.1,0.715,0.0,2.35,0.071,21.0,47.0,0.9963200000000001,3.29,0.45,9.4,5
9.1,0.66,0.15,3.2,0.09699999999999999,9.0,59.0,0.99976,3.28,0.54,9.6,5
7.0,0.685,0.0,1.9,0.099,9.0,22.0,0.9960600000000001,3.34,0.6,9.7,5
4.9,0.42,0.0,2.1,0.048,16.0,42.0,0.99154,3.71,0.74,14.0,7
6.7,0.54,0.13,2.0,0.076,15.0,36.0,0.9973,3.61,0.64,9.8,5
6.7,0.54,0.13,2.0,0.076,15.0,36.0,0.9973,3.61,0.64,9.8,5
7.1,0.48,0.28,2.8,0.068,6.0,16.0,0.99682,3.24,0.53,10.3,5
7.1,0.46,0.14,2.8,0.076,15.0,37.0,0.99624,3.36,0.49,10.7,5
7.5,0.27,0.34,2.3,0.05,4.0,8.0,0.9951,3.4,0.64,11.0,7
7.1,0.46,0.14,2.8,0.076,15.0,37.0,0.99624,3.36,0.49,10.7,5
7.8,0.57,0.09,2.3,0.065,34.0,45.0,0.9941700000000001,3.46,0.74,12.7,8
5.9,0.61,0.08,2.1,0.071,16.0,24.0,0.9937600000000001,3.56,0.77,11.1,6
7.5,0.685,0.07,2.5,0.057999999999999996,5.0,9.0,0.9963200000000001,3.38,0.55,10.9,4
5.9,0.61,0.08,2.1,0.071,16.0,24.0,0.9937600000000001,3.56,0.77,11.1,6
10.4,0.44,0.42,1.5,0.145,34.0,48.0,0.9983200000000001,3.38,0.86,9.9,3
11.6,0.47,0.44,1.6,0.147,36.0,51.0,0.99836,3.38,0.86,9.9,4
8.8,0.685,0.26,1.6,0.08800000000000001,16.0,23.0,0.9969399999999999,3.32,0.47,9.4,5
7.6,0.665,0.1,1.5,0.066,27.0,55.0,0.99655,3.39,0.51,9.3,5
6.7,0.28,0.28,2.4,0.012,36.0,100.0,0.99064,3.26,0.39,11.7,7
6.7,0.28,0.28,2.4,0.012,36.0,100.0,0.99064,3.26,0.39,11.7,7
10.1,0.31,0.35,1.6,0.075,9.0,28.0,0.99672,3.24,0.83,11.2,7
6.0,0.5,0.04,2.2,0.092,13.0,26.0,0.9964700000000001,3.46,0.47,10.0,5
11.1,0.42,0.47,2.65,0.085,9.0,34.0,0.99736,3.24,0.77,12.1,7
6.6,0.66,0.0,3.0,0.115,21.0,31.0,0.99629,3.45,0.63,10.3,5
10.6,0.5,0.45,2.6,0.11900000000000001,34.0,68.0,0.99708,3.23,0.72,10.9,6
7.1,0.685,0.35,2.0,0.08800000000000001,9.0,92.0,0.9963,3.28,0.62,9.4,5
9.9,0.25,0.46,1.7,0.062,26.0,42.0,0.9959,3.18,0.83,10.6,6
6.4,0.64,0.21,1.8,0.081,14.0,31.0,0.9968899999999999,3.59,0.66,9.8,5
6.4,0.64,0.21,1.8,0.081,14.0,31.0,0.9968899999999999,3.59,0.66,9.8,5
7.4,0.68,0.16,1.8,0.078,12.0,39.0,0.9977,3.5,0.7,9.9,6
6.4,0.64,0.21,1.8,0.081,14.0,31.0,0.9968899999999999,3.59,0.66,9.8,5
6.4,0.63,0.21,1.6,0.08,12.0,32.0,0.9968899999999999,3.58,0.66,9.8,5
9.3,0.43,0.44,1.9,0.085,9.0,22.0,0.99708,3.28,0.55,9.5,5
9.3,0.43,0.44,1.9,0.085,9.0,22.0,0.99708,3.28,0.55,9.5,5
8.0,0.42,0.32,2.5,0.08,26.0,122.0,0.9980100000000001,3.22,1.07,9.7,5
9.3,0.36,0.39,1.5,0.08,41.0,55.0,0.9965200000000001,3.47,0.73,10.9,6
9.3,0.36,0.39,1.5,0.08,41.0,55.0,0.9965200000000001,3.47,0.73,10.9,6
7.6,0.735,0.02,2.5,0.071,10.0,14.0,0.9953799999999999,3.51,0.71,11.7,7
9.3,0.36,0.39,1.5,0.08,41.0,55.0,0.9965200000000001,3.47,0.73,10.9,6
8.2,0.26,0.34,2.5,0.073,16.0,47.0,0.9959399999999999,3.4,0.78,11.3,7
11.7,0.28,0.47,1.7,0.054000000000000006,17.0,32.0,0.9968600000000001,3.15,0.67,10.6,7
6.8,0.56,0.22,1.8,0.07400000000000001,15.0,24.0,0.9943799999999999,3.4,0.82,11.2,6
7.2,0.62,0.06,2.7,0.077,15.0,85.0,0.99746,3.51,0.54,9.5,5
5.8,1.01,0.66,2.0,0.039,15.0,88.0,0.9935700000000001,3.66,0.6,11.5,6
7.5,0.42,0.32,2.7,0.067,7.0,25.0,0.9962799999999999,3.24,0.44,10.4,5
7.2,0.62,0.06,2.5,0.078,17.0,84.0,0.99746,3.51,0.53,9.7,5
7.2,0.62,0.06,2.7,0.077,15.0,85.0,0.99746,3.51,0.54,9.5,5
7.2,0.635,0.07,2.6,0.077,16.0,86.0,0.9974799999999999,3.51,0.54,9.7,5
6.8,0.49,0.22,2.3,0.071,13.0,24.0,0.9943799999999999,3.41,0.83,11.3,6
6.9,0.51,0.23,2.0,0.07200000000000001,13.0,22.0,0.9943799999999999,3.4,0.84,11.2,6
6.8,0.56,0.22,1.8,0.07400000000000001,15.0,24.0,0.9943799999999999,3.4,0.82,11.2,6
7.6,0.63,0.03,2.0,0.08,27.0,43.0,0.9957799999999999,3.44,0.64,10.9,6
7.7,0.715,0.01,2.1,0.064,31.0,43.0,0.99371,3.41,0.57,11.8,6
6.9,0.56,0.03,1.5,0.086,36.0,46.0,0.9952200000000001,3.53,0.57,10.6,5
7.3,0.35,0.24,2.0,0.067,28.0,48.0,0.9957600000000001,3.43,0.54,10.0,4
9.1,0.21,0.37,1.6,0.067,6.0,10.0,0.9955200000000001,3.23,0.58,11.1,7
10.4,0.38,0.46,2.1,0.10400000000000001,6.0,10.0,0.99664,3.12,0.65,11.8,7
8.8,0.31,0.4,2.8,0.109,7.0,16.0,0.9961399999999999,3.31,0.79,11.8,7
7.1,0.47,0.0,2.2,0.067,7.0,14.0,0.9951700000000001,3.4,0.58,10.9,4
7.7,0.715,0.01,2.1,0.064,31.0,43.0,0.99371,3.41,0.57,11.8,6
8.8,0.61,0.19,4.0,0.094,30.0,69.0,0.99787,3.22,0.5,10.0,6
7.2,0.6,0.04,2.5,0.076,18.0,88.0,0.99745,3.53,0.55,9.5,5
9.2,0.56,0.18,1.6,0.078,10.0,21.0,0.9957600000000001,3.15,0.49,9.9,5
7.6,0.715,0.0,2.1,0.068,30.0,35.0,0.9953299999999999,3.48,0.65,11.4,6
8.4,0.31,0.29,3.1,0.19399999999999998,14.0,26.0,0.99536,3.22,0.78,12.0,6
7.2,0.6,0.04,2.5,0.076,18.0,88.0,0.99745,3.53,0.55,9.5,5
8.8,0.61,0.19,4.0,0.094,30.0,69.0,0.99787,3.22,0.5,10.0,6
8.9,0.75,0.14,2.5,0.086,9.0,30.0,0.99824,3.34,0.64,10.5,5
9.0,0.8,0.12,2.4,0.083,8.0,28.0,0.99836,3.33,0.65,10.4,6
10.7,0.52,0.38,2.6,0.066,29.0,56.0,0.99577,3.15,0.79,12.1,7
6.8,0.57,0.0,2.5,0.07200000000000001,32.0,64.0,0.9949100000000001,3.43,0.56,11.2,6
10.7,0.9,0.34,6.6,0.11199999999999999,23.0,99.0,1.00289,3.22,0.68,9.3,5
7.2,0.34,0.24,2.0,0.071,30.0,52.0,0.9957600000000001,3.44,0.58,10.1,5
7.2,0.66,0.03,2.3,0.078,16.0,86.0,0.9974299999999999,3.53,0.57,9.7,5
10.1,0.45,0.23,1.9,0.08199999999999999,10.0,18.0,0.99774,3.22,0.65,9.3,6
7.2,0.66,0.03,2.3,0.078,16.0,86.0,0.9974299999999999,3.53,0.57,9.7,5
7.2,0.63,0.03,2.2,0.08,17.0,88.0,0.99745,3.53,0.58,9.8,6
7.1,0.59,0.01,2.3,0.08,27.0,43.0,0.9955,3.42,0.58,10.7,6
8.3,0.31,0.39,2.4,0.078,17.0,43.0,0.99444,3.31,0.77,12.5,7
7.1,0.59,0.01,2.3,0.08,27.0,43.0,0.9955,3.42,0.58,10.7,6
8.3,0.31,0.39,2.4,0.078,17.0,43.0,0.99444,3.31,0.77,12.5,7
8.3,1.02,0.02,3.4,0.084,6.0,11.0,0.99892,3.48,0.49,11.0,3
8.9,0.31,0.36,2.6,0.055999999999999994,10.0,39.0,0.9956200000000001,3.4,0.69,11.8,5
7.4,0.635,0.1,2.4,0.08,16.0,33.0,0.99736,3.58,0.69,10.8,7
7.4,0.635,0.1,2.4,0.08,16.0,33.0,0.99736,3.58,0.69,10.8,7
6.8,0.59,0.06,6.0,0.06,11.0,18.0,0.9962,3.41,0.59,10.8,7
6.8,0.59,0.06,6.0,0.06,11.0,18.0,0.9962,3.41,0.59,10.8,7
9.2,0.58,0.2,3.0,0.081,15.0,115.0,0.998,3.23,0.59,9.5,5
7.2,0.54,0.27,2.6,0.084,12.0,78.0,0.9964,3.39,0.71,11.0,5
6.1,0.56,0.0,2.2,0.079,6.0,9.0,0.9948,3.59,0.54,11.5,6
7.4,0.52,0.13,2.4,0.078,34.0,61.0,0.9952799999999999,3.43,0.59,10.8,6
7.3,0.305,0.39,1.2,0.059000000000000004,7.0,11.0,0.99331,3.29,0.52,11.5,6
9.3,0.38,0.48,3.8,0.132,3.0,11.0,0.99577,3.23,0.57,13.2,6
9.1,0.28,0.46,9.0,0.114,3.0,9.0,0.9990100000000001,3.18,0.6,10.9,6
10.0,0.46,0.44,2.9,0.065,4.0,8.0,0.99674,3.33,0.62,12.2,6
9.4,0.395,0.46,4.6,0.094,3.0,10.0,0.99639,3.27,0.64,12.2,7
7.3,0.305,0.39,1.2,0.059000000000000004,7.0,11.0,0.99331,3.29,0.52,11.5,6
8.6,0.315,0.4,2.2,0.079,3.0,6.0,0.9951200000000001,3.27,0.67,11.9,6
5.3,0.715,0.19,1.5,0.161,7.0,62.0,0.99395,3.62,0.61,11.0,5
6.8,0.41,0.31,8.8,0.084,26.0,45.0,0.99824,3.38,0.64,10.1,6
8.4,0.36,0.32,2.2,0.081,32.0,79.0,0.9964,3.3,0.72,11.0,6
8.4,0.62,0.12,1.8,0.07200000000000001,38.0,46.0,0.9950399999999999,3.38,0.89,11.8,6
9.6,0.41,0.37,2.3,0.091,10.0,23.0,0.9978600000000001,3.24,0.56,10.5,5
8.4,0.36,0.32,2.2,0.081,32.0,79.0,0.9964,3.3,0.72,11.0,6
8.4,0.62,0.12,1.8,0.07200000000000001,38.0,46.0,0.9950399999999999,3.38,0.89,11.8,6
6.8,0.41,0.31,8.8,0.084,26.0,45.0,0.99824,3.38,0.64,10.1,6
8.6,0.47,0.27,2.3,0.055,14.0,28.0,0.99516,3.18,0.8,11.2,5
8.6,0.22,0.36,1.9,0.064,53.0,77.0,0.9960399999999999,3.47,0.87,11.0,7
9.4,0.24,0.33,2.3,0.061,52.0,73.0,0.9978600000000001,3.47,0.9,10.2,6
8.4,0.67,0.19,2.2,0.09300000000000001,11.0,75.0,0.99736,3.2,0.59,9.2,4
8.6,0.47,0.27,2.3,0.055,14.0,28.0,0.99516,3.18,0.8,11.2,5
8.7,0.33,0.38,3.3,0.063,10.0,19.0,0.9946799999999999,3.3,0.73,12.0,7
6.6,0.61,0.01,1.9,0.08,8.0,25.0,0.99746,3.69,0.73,10.5,5
7.4,0.61,0.01,2.0,0.07400000000000001,13.0,38.0,0.9974799999999999,3.48,0.65,9.8,5
7.6,0.4,0.29,1.9,0.078,29.0,66.0,0.9971,3.45,0.59,9.5,6
7.4,0.61,0.01,2.0,0.07400000000000001,13.0,38.0,0.9974799999999999,3.48,0.65,9.8,5
6.6,0.61,0.01,1.9,0.08,8.0,25.0,0.99746,3.69,0.73,10.5,5
8.8,0.3,0.38,2.3,0.06,19.0,72.0,0.9954299999999999,3.39,0.72,11.8,6
8.8,0.3,0.38,2.3,0.06,19.0,72.0,0.9954299999999999,3.39,0.72,11.8,6
12.0,0.63,0.5,1.4,0.071,6.0,26.0,0.9979100000000001,3.07,0.6,10.4,4
7.2,0.38,0.38,2.8,0.068,23.0,42.0,0.99356,3.34,0.72,12.9,7
6.2,0.46,0.17,1.6,0.073,7.0,11.0,0.99425,3.61,0.54,11.4,5
9.6,0.33,0.52,2.2,0.07400000000000001,13.0,25.0,0.9950899999999999,3.36,0.76,12.4,7
9.9,0.27,0.49,5.0,0.08199999999999999,9.0,17.0,0.99484,3.19,0.52,12.5,7
10.1,0.43,0.4,2.6,0.092,13.0,52.0,0.99834,3.22,0.64,10.0,7
9.8,0.5,0.34,2.3,0.094,10.0,45.0,0.99864,3.24,0.6,9.7,7
8.3,0.3,0.49,3.8,0.09,11.0,24.0,0.99498,3.27,0.64,12.1,7
10.2,0.44,0.42,2.0,0.071,7.0,20.0,0.99566,3.14,0.79,11.1,7
10.2,0.44,0.58,4.1,0.092,11.0,24.0,0.99745,3.29,0.99,12.0,7
8.3,0.28,0.48,2.1,0.09300000000000001,6.0,12.0,0.99408,3.26,0.62,12.4,7
8.9,0.12,0.45,1.8,0.075,10.0,21.0,0.9955200000000001,3.41,0.76,11.9,7
8.9,0.12,0.45,1.8,0.075,10.0,21.0,0.9955200000000001,3.41,0.76,11.9,7
8.9,0.12,0.45,1.8,0.075,10.0,21.0,0.9955200000000001,3.41,0.76,11.9,7
8.3,0.28,0.48,2.1,0.09300000000000001,6.0,12.0,0.99408,3.26,0.62,12.4,7
8.2,0.31,0.4,2.2,0.057999999999999996,6.0,10.0,0.99536,3.31,0.68,11.2,7
10.2,0.34,0.48,2.1,0.052000000000000005,5.0,9.0,0.9945799999999999,3.2,0.69,12.1,7
7.6,0.43,0.4,2.7,0.08199999999999999,6.0,11.0,0.9953799999999999,3.44,0.54,12.2,6
8.5,0.21,0.52,1.9,0.09,9.0,23.0,0.9964799999999999,3.36,0.67,10.4,5
9.0,0.36,0.52,2.1,0.111,5.0,10.0,0.9956799999999999,3.31,0.62,11.3,6
9.5,0.37,0.52,2.0,0.08800000000000001,12.0,51.0,0.99613,3.29,0.58,11.1,6
6.4,0.57,0.12,2.3,0.12,25.0,36.0,0.99519,3.47,0.71,11.3,7
8.0,0.59,0.05,2.0,0.08900000000000001,12.0,32.0,0.99735,3.36,0.61,10.0,5
8.5,0.47,0.27,1.9,0.057999999999999996,18.0,38.0,0.99518,3.16,0.85,11.1,6
7.1,0.56,0.14,1.6,0.078,7.0,18.0,0.99592,3.27,0.62,9.3,5
6.6,0.57,0.02,2.1,0.115,6.0,16.0,0.99654,3.38,0.69,9.5,5
8.8,0.27,0.39,2.0,0.1,20.0,27.0,0.99546,3.15,0.69,11.2,6
8.5,0.47,0.27,1.9,0.057999999999999996,18.0,38.0,0.99518,3.16,0.85,11.1,6
8.3,0.34,0.4,2.4,0.065,24.0,48.0,0.99554,3.34,0.86,11.0,6
9.0,0.38,0.41,2.4,0.10300000000000001,6.0,10.0,0.9960399999999999,3.13,0.58,11.9,7
8.5,0.66,0.2,2.1,0.09699999999999999,23.0,113.0,0.9973299999999999,3.13,0.48,9.2,5
9.0,0.4,0.43,2.4,0.068,29.0,46.0,0.9943,3.2,0.6,12.2,6
6.7,0.56,0.09,2.9,0.079,7.0,22.0,0.99669,3.46,0.61,10.2,5
10.4,0.26,0.48,1.9,0.066,6.0,10.0,0.99724,3.33,0.87,10.9,6
10.4,0.26,0.48,1.9,0.066,6.0,10.0,0.99724,3.33,0.87,10.9,6
10.1,0.38,0.5,2.4,0.10400000000000001,6.0,13.0,0.9964299999999999,3.22,0.65,11.6,7
8.5,0.34,0.44,1.7,0.079,6.0,12.0,0.99605,3.52,0.63,10.7,5
8.8,0.33,0.41,5.9,0.073,7.0,13.0,0.9965799999999999,3.3,0.62,12.1,7
7.2,0.41,0.3,2.1,0.083,35.0,72.0,0.997,3.44,0.52,9.4,5
7.2,0.41,0.3,2.1,0.083,35.0,72.0,0.997,3.44,0.52,9.4,5
8.4,0.59,0.29,2.6,0.109,31.0,119.0,0.9980100000000001,3.15,0.5,9.1,5
7.0,0.4,0.32,3.6,0.061,9.0,29.0,0.99416,3.28,0.49,11.3,7
12.2,0.45,0.49,1.4,0.075,3.0,6.0,0.9969,3.13,0.63,10.4,5
9.1,0.5,0.3,1.9,0.065,8.0,17.0,0.99774,3.32,0.71,10.5,6
9.5,0.86,0.26,1.9,0.079,13.0,28.0,0.9971200000000001,3.25,0.62,10.0,5
7.3,0.52,0.32,2.1,0.07,51.0,70.0,0.99418,3.34,0.82,12.9,6
9.1,0.5,0.3,1.9,0.065,8.0,17.0,0.99774,3.32,0.71,10.5,6
12.2,0.45,0.49,1.4,0.075,3.0,6.0,0.9969,3.13,0.63,10.4,5
7.4,0.58,0.0,2.0,0.064,7.0,11.0,0.9956200000000001,3.45,0.58,11.3,6
9.8,0.34,0.39,1.4,0.066,3.0,7.0,0.9947,3.19,0.55,11.4,7
7.1,0.36,0.3,1.6,0.08,35.0,70.0,0.9969299999999999,3.44,0.5,9.4,5
7.7,0.39,0.12,1.7,0.09699999999999999,19.0,27.0,0.9959600000000001,3.16,0.49,9.4,5
9.7,0.295,0.4,1.5,0.073,14.0,21.0,0.99556,3.14,0.51,10.9,6
7.7,0.39,0.12,1.7,0.09699999999999999,19.0,27.0,0.9959600000000001,3.16,0.49,9.4,5
7.1,0.34,0.28,2.0,0.08199999999999999,31.0,68.0,0.9969399999999999,3.45,0.48,9.4,5
6.5,0.4,0.1,2.0,0.076,30.0,47.0,0.99554,3.36,0.48,9.4,6
7.1,0.34,0.28,2.0,0.08199999999999999,31.0,68.0,0.9969399999999999,3.45,0.48,9.4,5
10.0,0.35,0.45,2.5,0.092,20.0,88.0,0.99918,3.15,0.43,9.4,5
7.7,0.6,0.06,2.0,0.079,19.0,41.0,0.99697,3.39,0.62,10.1,6
5.6,0.66,0.0,2.2,0.087,3.0,11.0,0.9937799999999999,3.71,0.63,12.8,7
5.6,0.66,0.0,2.2,0.087,3.0,11.0,0.9937799999999999,3.71,0.63,12.8,7
8.9,0.84,0.34,1.4,0.05,4.0,10.0,0.99554,3.12,0.48,9.1,6
6.4,0.69,0.0,1.65,0.055,7.0,12.0,0.9916200000000001,3.47,0.53,12.9,6
7.5,0.43,0.3,2.2,0.062,6.0,12.0,0.99495,3.44,0.72,11.5,7
9.9,0.35,0.38,1.5,0.057999999999999996,31.0,47.0,0.9967600000000001,3.26,0.82,10.6,7
9.1,0.29,0.33,2.05,0.063,13.0,27.0,0.99516,3.26,0.84,11.7,7
6.8,0.36,0.32,1.8,0.067,4.0,8.0,0.9928,3.36,0.55,12.8,7
8.2,0.43,0.29,1.6,0.081,27.0,45.0,0.99603,3.25,0.54,10.3,5
6.8,0.36,0.32,1.8,0.067,4.0,8.0,0.9928,3.36,0.55,12.8,7
9.1,0.29,0.33,2.05,0.063,13.0,27.0,0.99516,3.26,0.84,11.7,7
9.1,0.3,0.34,2.0,0.064,12.0,25.0,0.99516,3.26,0.84,11.7,7
8.9,0.35,0.4,3.6,0.11,12.0,24.0,0.99549,3.23,0.7,12.0,7
9.6,0.5,0.36,2.8,0.11599999999999999,26.0,55.0,0.9972200000000001,3.18,0.68,10.9,5
8.9,0.28,0.45,1.7,0.067,7.0,12.0,0.99354,3.25,0.55,12.3,7
8.9,0.32,0.31,2.0,0.08800000000000001,12.0,19.0,0.9957,3.17,0.55,10.4,6
7.7,1.005,0.15,2.1,0.102,11.0,32.0,0.9960399999999999,3.23,0.48,10.0,5
7.5,0.71,0.0,1.6,0.092,22.0,31.0,0.99635,3.38,0.58,10.0,6
8.0,0.58,0.16,2.0,0.12,3.0,7.0,0.99454,3.22,0.58,11.2,6
10.5,0.39,0.46,2.2,0.075,14.0,27.0,0.99598,3.06,0.84,11.4,6
8.9,0.38,0.4,2.2,0.068,12.0,28.0,0.9948600000000001,3.27,0.75,12.6,7
8.0,0.18,0.37,0.9,0.049,36.0,109.0,0.9900700000000001,2.89,0.44,12.7,6
8.0,0.18,0.37,0.9,0.049,36.0,109.0,0.9900700000000001,2.89,0.44,12.7,6
7.0,0.5,0.14,1.8,0.078,10.0,23.0,0.99636,3.53,0.61,10.4,5
11.3,0.36,0.66,2.4,0.12300000000000001,3.0,8.0,0.9964200000000001,3.2,0.53,11.9,6
11.3,0.36,0.66,2.4,0.12300000000000001,3.0,8.0,0.9964200000000001,3.2,0.53,11.9,6
7.0,0.51,0.09,2.1,0.062,4.0,9.0,0.99584,3.35,0.54,10.5,5
8.2,0.32,0.42,2.3,0.098,3.0,9.0,0.9950600000000001,3.27,0.55,12.3,6
7.7,0.58,0.01,1.8,0.08800000000000001,12.0,18.0,0.9956799999999999,3.32,0.56,10.5,7
8.6,0.83,0.0,2.8,0.095,17.0,43.0,0.9982200000000001,3.33,0.6,10.4,6
7.9,0.31,0.32,1.9,0.066,14.0,36.0,0.99364,3.41,0.56,12.6,6
6.4,0.795,0.0,2.2,0.065,28.0,52.0,0.9937799999999999,3.49,0.52,11.6,5
7.2,0.34,0.21,2.5,0.075,41.0,68.0,0.9958600000000001,3.37,0.54,10.1,6
7.7,0.58,0.01,1.8,0.08800000000000001,12.0,18.0,0.9956799999999999,3.32,0.56,10.5,7
7.1,0.59,0.0,2.1,0.091,9.0,14.0,0.9948799999999999,3.42,0.55,11.5,7
7.3,0.55,0.01,1.8,0.09300000000000001,9.0,15.0,0.9951399999999999,3.35,0.58,11.0,7
8.1,0.82,0.0,4.1,0.095,5.0,14.0,0.99854,3.36,0.53,9.6,5
7.5,0.57,0.08,2.6,0.08900000000000001,14.0,27.0,0.99592,3.3,0.59,10.4,6
8.9,0.745,0.18,2.5,0.077,15.0,48.0,0.99739,3.2,0.47,9.7,6
10.1,0.37,0.34,2.4,0.085,5.0,17.0,0.9968299999999999,3.17,0.65,10.6,7
7.6,0.31,0.34,2.5,0.08199999999999999,26.0,35.0,0.99356,3.22,0.59,12.5,7
7.3,0.91,0.1,1.8,0.07400000000000001,20.0,56.0,0.99672,3.35,0.56,9.2,5
8.7,0.41,0.41,6.2,0.078,25.0,42.0,0.9953,3.24,0.77,12.6,7
8.9,0.5,0.21,2.2,0.08800000000000001,21.0,39.0,0.99692,3.33,0.83,11.1,6
7.4,0.965,0.0,2.2,0.08800000000000001,16.0,32.0,0.99756,3.58,0.67,10.2,5
6.9,0.49,0.19,1.7,0.079,13.0,26.0,0.9954700000000001,3.38,0.64,9.8,6
8.9,0.5,0.21,2.2,0.08800000000000001,21.0,39.0,0.99692,3.33,0.83,11.1,6
9.5,0.39,0.41,8.9,0.069,18.0,39.0,0.99859,3.29,0.81,10.9,7
6.4,0.39,0.33,3.3,0.046,12.0,53.0,0.9929399999999999,3.36,0.62,12.2,6
6.9,0.44,0.0,1.4,0.07,32.0,38.0,0.9943799999999999,3.32,0.58,11.4,6
7.6,0.78,0.0,1.7,0.076,33.0,45.0,0.9961200000000001,3.31,0.62,10.7,6
7.1,0.43,0.17,1.8,0.08199999999999999,27.0,51.0,0.99634,3.49,0.64,10.4,5
9.3,0.49,0.36,1.7,0.081,3.0,14.0,0.99702,3.27,0.78,10.9,6
9.3,0.5,0.36,1.8,0.084,6.0,17.0,0.9970399999999999,3.27,0.77,10.8,6
7.1,0.43,0.17,1.8,0.08199999999999999,27.0,51.0,0.99634,3.49,0.64,10.4,5
8.5,0.46,0.59,1.4,0.414,16.0,45.0,0.99702,3.03,1.34,9.2,5
5.6,0.605,0.05,2.4,0.073,19.0,25.0,0.9925799999999999,3.56,0.55,12.9,5
8.3,0.33,0.42,2.3,0.07,9.0,20.0,0.99426,3.38,0.77,12.7,7
8.2,0.64,0.27,2.0,0.095,5.0,77.0,0.9974700000000001,3.13,0.62,9.1,6
8.2,0.64,0.27,2.0,0.095,5.0,77.0,0.9974700000000001,3.13,0.62,9.1,6
8.9,0.48,0.53,4.0,0.10099999999999999,3.0,10.0,0.9958600000000001,3.21,0.59,12.1,7
7.6,0.42,0.25,3.9,0.10400000000000001,28.0,90.0,0.99784,3.15,0.57,9.1,5
9.9,0.53,0.57,2.4,0.09300000000000001,30.0,52.0,0.9971,3.19,0.76,11.6,7
8.9,0.48,0.53,4.0,0.10099999999999999,3.0,10.0,0.9958600000000001,3.21,0.59,12.1,7
11.6,0.23,0.57,1.8,0.07400000000000001,3.0,8.0,0.9981,3.14,0.7,9.9,6
9.1,0.4,0.5,1.8,0.071,7.0,16.0,0.9946200000000001,3.21,0.69,12.5,8
8.0,0.38,0.44,1.9,0.098,6.0,15.0,0.9956,3.3,0.64,11.4,6
10.2,0.29,0.65,2.4,0.075,6.0,17.0,0.99565,3.22,0.63,11.8,6
8.2,0.74,0.09,2.0,0.067,5.0,10.0,0.99418,3.28,0.57,11.8,6
7.7,0.61,0.18,2.4,0.083,6.0,20.0,0.9963,3.29,0.6,10.2,6
6.6,0.52,0.08,2.4,0.07,13.0,26.0,0.9935799999999999,3.4,0.72,12.5,7
11.1,0.31,0.53,2.2,0.06,3.0,10.0,0.99572,3.02,0.83,10.9,7
11.1,0.31,0.53,2.2,0.06,3.0,10.0,0.99572,3.02,0.83,10.9,7
8.0,0.62,0.35,2.8,0.086,28.0,52.0,0.997,3.31,0.62,10.8,5
9.3,0.33,0.45,1.5,0.057,19.0,37.0,0.99498,3.18,0.89,11.1,7
7.5,0.77,0.2,8.1,0.098,30.0,92.0,0.99892,3.2,0.58,9.2,5
7.2,0.35,0.26,1.8,0.083,33.0,75.0,0.9968,3.4,0.58,9.5,6
8.0,0.62,0.33,2.7,0.08800000000000001,16.0,37.0,0.9972,3.31,0.58,10.7,6
7.5,0.77,0.2,8.1,0.098,30.0,92.0,0.99892,3.2,0.58,9.2,5
9.1,0.25,0.34,2.0,0.071,45.0,67.0,0.99769,3.44,0.86,10.2,7
9.9,0.32,0.56,2.0,0.073,3.0,8.0,0.99534,3.15,0.73,11.4,6
8.6,0.37,0.65,6.4,0.08,3.0,8.0,0.9981700000000001,3.27,0.58,11.0,5
8.6,0.37,0.65,6.4,0.08,3.0,8.0,0.9981700000000001,3.27,0.58,11.0,5
7.9,0.3,0.68,8.3,0.05,37.5,278.0,0.99316,3.01,0.51,12.3,7
10.3,0.27,0.56,1.4,0.047,3.0,8.0,0.99471,3.16,0.51,11.8,6
7.9,0.3,0.68,8.3,0.05,37.5,289.0,0.99316,3.01,0.51,12.3,7
7.2,0.38,0.3,1.8,0.073,31.0,70.0,0.99685,3.42,0.59,9.5,6
8.7,0.42,0.45,2.4,0.07200000000000001,32.0,59.0,0.9961700000000001,3.33,0.77,12.0,6
7.2,0.38,0.3,1.8,0.073,31.0,70.0,0.99685,3.42,0.59,9.5,6
6.8,0.48,0.08,1.8,0.07400000000000001,40.0,64.0,0.99529,3.12,0.49,9.6,5
8.5,0.34,0.4,4.7,0.055,3.0,9.0,0.9973799999999999,3.38,0.66,11.6,7
7.9,0.19,0.42,1.6,0.057,18.0,30.0,0.9940000000000001,3.29,0.69,11.2,6
11.6,0.41,0.54,1.5,0.095,22.0,41.0,0.99735,3.02,0.76,9.9,7
11.6,0.41,0.54,1.5,0.095,22.0,41.0,0.99735,3.02,0.76,9.9,7
10.0,0.26,0.54,1.9,0.083,42.0,74.0,0.99451,2.98,0.63,11.8,8
7.9,0.34,0.42,2.0,0.086,8.0,19.0,0.99546,3.35,0.6,11.4,6
7.0,0.54,0.09,2.0,0.081,10.0,16.0,0.99479,3.43,0.59,11.5,6
9.2,0.31,0.36,2.2,0.079,11.0,31.0,0.99615,3.33,0.86,12.0,7
6.6,0.725,0.09,5.5,0.11699999999999999,9.0,17.0,0.99655,3.35,0.49,10.8,6
9.4,0.4,0.47,2.5,0.087,6.0,20.0,0.99772,3.15,0.5,10.5,5
6.6,0.725,0.09,5.5,0.11699999999999999,9.0,17.0,0.99655,3.35,0.49,10.8,6
8.6,0.52,0.38,1.5,0.096,5.0,18.0,0.99666,3.2,0.52,9.4,5
8.0,0.31,0.45,2.1,0.21600000000000003,5.0,16.0,0.9935799999999999,3.15,0.81,12.5,7
8.6,0.52,0.38,1.5,0.096,5.0,18.0,0.99666,3.2,0.52,9.4,5
8.4,0.34,0.42,2.1,0.07200000000000001,23.0,36.0,0.99392,3.11,0.78,12.4,6
7.4,0.49,0.27,2.1,0.071,14.0,25.0,0.9938799999999999,3.35,0.63,12.0,6
6.1,0.48,0.09,1.7,0.078,18.0,30.0,0.9940200000000001,3.45,0.54,11.2,6
7.4,0.49,0.27,2.1,0.071,14.0,25.0,0.9938799999999999,3.35,0.63,12.0,6
8.0,0.48,0.34,2.2,0.073,16.0,25.0,0.9936,3.28,0.66,12.4,6
6.3,0.57,0.28,2.1,0.048,13.0,49.0,0.99374,3.41,0.6,12.8,5
8.2,0.23,0.42,1.9,0.069,9.0,17.0,0.9937600000000001,3.21,0.54,12.3,6
9.1,0.3,0.41,2.0,0.068,10.0,24.0,0.99523,3.27,0.85,11.7,7
8.1,0.78,0.1,3.3,0.09,4.0,13.0,0.99855,3.36,0.49,9.5,5
10.8,0.47,0.43,2.1,0.171,27.0,66.0,0.9982,3.17,0.76,10.8,6
8.3,0.53,0.0,1.4,0.07,6.0,14.0,0.99593,3.25,0.64,10.0,6
5.4,0.42,0.27,2.0,0.092,23.0,55.0,0.99471,3.78,0.64,12.3,7
7.9,0.33,0.41,1.5,0.055999999999999994,6.0,35.0,0.9939600000000001,3.29,0.71,11.0,6
8.9,0.24,0.39,1.6,0.07400000000000001,3.0,10.0,0.99698,3.12,0.59,9.5,6
5.0,0.4,0.5,4.3,0.046,29.0,80.0,0.9902,3.49,0.66,13.6,6
7.0,0.69,0.07,2.5,0.091,15.0,21.0,0.99572,3.38,0.6,11.3,6
7.0,0.69,0.07,2.5,0.091,15.0,21.0,0.99572,3.38,0.6,11.3,6
7.0,0.69,0.07,2.5,0.091,15.0,21.0,0.99572,3.38,0.6,11.3,6
7.1,0.39,0.12,2.1,0.065,14.0,24.0,0.9925200000000001,3.3,0.53,13.3,6
5.6,0.66,0.0,2.5,0.066,7.0,15.0,0.99256,3.52,0.58,12.9,5
7.9,0.54,0.34,2.5,0.076,8.0,17.0,0.99235,3.2,0.72,13.1,8
6.6,0.5,0.0,1.8,0.062,21.0,28.0,0.9935200000000001,3.44,0.55,12.3,6
6.3,0.47,0.0,1.4,0.055,27.0,33.0,0.9922,3.45,0.48,12.3,6
10.7,0.4,0.37,1.9,0.081,17.0,29.0,0.99674,3.12,0.65,11.2,6
6.5,0.58,0.0,2.2,0.096,3.0,13.0,0.9955700000000001,3.62,0.62,11.5,4
8.8,0.24,0.35,1.7,0.055,13.0,27.0,0.9939399999999999,3.14,0.59,11.3,7
5.8,0.29,0.26,1.7,0.063,3.0,11.0,0.9915,3.39,0.54,13.5,6
6.3,0.76,0.0,2.9,0.07200000000000001,26.0,52.0,0.99379,3.51,0.6,11.5,6
10.0,0.43,0.33,2.7,0.095,28.0,89.0,0.9984,3.22,0.68,10.0,5
10.5,0.43,0.35,3.3,0.092,24.0,70.0,0.99798,3.21,0.69,10.5,6
9.1,0.6,0.0,1.9,0.057999999999999996,5.0,10.0,0.9977,3.18,0.63,10.4,6
5.9,0.19,0.21,1.7,0.045,57.0,135.0,0.99341,3.32,0.44,9.5,5
7.4,0.36,0.34,1.8,0.075,18.0,38.0,0.9933,3.38,0.88,13.6,7
7.2,0.48,0.07,5.5,0.08900000000000001,10.0,18.0,0.99684,3.37,0.68,11.2,7
8.5,0.28,0.35,1.7,0.061,6.0,15.0,0.99524,3.3,0.74,11.8,7
8.0,0.25,0.43,1.7,0.067,22.0,50.0,0.9946,3.38,0.6,11.9,6
10.4,0.52,0.45,2.0,0.08,6.0,13.0,0.99774,3.22,0.76,11.4,6
10.4,0.52,0.45,2.0,0.08,6.0,13.0,0.99774,3.22,0.76,11.4,6
7.5,0.41,0.15,3.7,0.10400000000000001,29.0,94.0,0.9978600000000001,3.14,0.58,9.1,5
8.2,0.51,0.24,2.0,0.079,16.0,86.0,0.99764,3.34,0.64,9.5,6
7.3,0.4,0.3,1.7,0.08,33.0,79.0,0.9969,3.41,0.65,9.5,6
8.2,0.38,0.32,2.5,0.08,24.0,71.0,0.99624,3.27,0.85,11.0,6
6.9,0.45,0.11,2.4,0.043,6.0,12.0,0.99354,3.3,0.65,11.4,6
7.0,0.22,0.3,1.8,0.065,16.0,20.0,0.99672,3.61,0.82,10.0,6
7.3,0.32,0.23,2.3,0.066,35.0,70.0,0.9958799999999999,3.43,0.62,10.1,5
8.2,0.2,0.43,2.5,0.076,31.0,51.0,0.99672,3.53,0.81,10.4,6
7.8,0.5,0.12,1.8,0.17800000000000002,6.0,21.0,0.996,3.28,0.87,9.8,6
10.0,0.41,0.45,6.2,0.071,6.0,14.0,0.99702,3.21,0.49,11.8,7
7.8,0.39,0.42,2.0,0.086,9.0,21.0,0.99526,3.39,0.66,11.6,6
10.0,0.35,0.47,2.0,0.061,6.0,11.0,0.99585,3.23,0.52,12.0,6
8.2,0.33,0.32,2.8,0.067,4.0,12.0,0.9947299999999999,3.3,0.76,12.8,7
6.1,0.58,0.23,2.5,0.044000000000000004,16.0,70.0,0.9935200000000001,3.46,0.65,12.5,6
8.3,0.6,0.25,2.2,0.11800000000000001,9.0,38.0,0.99616,3.15,0.53,9.8,5
9.6,0.42,0.35,2.1,0.083,17.0,38.0,0.9962200000000001,3.23,0.66,11.1,6
6.6,0.58,0.0,2.2,0.1,50.0,63.0,0.99544,3.59,0.68,11.4,6
8.3,0.6,0.25,2.2,0.11800000000000001,9.0,38.0,0.99616,3.15,0.53,9.8,5
8.5,0.18,0.51,1.75,0.071,45.0,88.0,0.99524,3.33,0.76,11.8,7
5.1,0.51,0.18,2.1,0.042,16.0,101.0,0.9924,3.46,0.87,12.9,7
6.7,0.41,0.43,2.8,0.076,22.0,54.0,0.99572,3.42,1.16,10.6,6
10.2,0.41,0.43,2.2,0.11,11.0,37.0,0.9972799999999999,3.16,0.67,10.8,5
10.6,0.36,0.57,2.3,0.087,6.0,20.0,0.9967600000000001,3.14,0.72,11.1,7
8.8,0.45,0.43,1.4,0.076,12.0,21.0,0.99551,3.21,0.75,10.2,6
8.5,0.32,0.42,2.3,0.075,12.0,19.0,0.99434,3.14,0.71,11.8,7
9.0,0.785,0.24,1.7,0.078,10.0,21.0,0.99692,3.29,0.67,10.0,5
9.0,0.785,0.24,1.7,0.078,10.0,21.0,0.99692,3.29,0.67,10.0,5
8.5,0.44,0.5,1.9,0.369,15.0,38.0,0.99634,3.01,1.1,9.4,5
9.9,0.54,0.26,2.0,0.111,7.0,60.0,0.9970899999999999,2.94,0.98,10.2,5
8.2,0.33,0.39,2.5,0.07400000000000001,29.0,48.0,0.9952799999999999,3.32,0.88,12.4,7
6.5,0.34,0.27,2.8,0.067,8.0,44.0,0.99384,3.21,0.56,12.0,6
7.6,0.5,0.29,2.3,0.086,5.0,14.0,0.9950200000000001,3.32,0.62,11.5,6
9.2,0.36,0.34,1.6,0.062,5.0,12.0,0.9966700000000001,3.2,0.67,10.5,6
7.1,0.59,0.0,2.2,0.078,26.0,44.0,0.9952200000000001,3.42,0.68,10.8,6
9.7,0.42,0.46,2.1,0.07400000000000001,5.0,16.0,0.99649,3.27,0.74,12.3,6
7.6,0.36,0.31,1.7,0.079,26.0,65.0,0.99716,3.46,0.62,9.5,6
7.6,0.36,0.31,1.7,0.079,26.0,65.0,0.99716,3.46,0.62,9.5,6
6.5,0.61,0.0,2.2,0.095,48.0,59.0,0.99541,3.61,0.7,11.5,6
6.5,0.88,0.03,5.6,0.079,23.0,47.0,0.99572,3.58,0.5,11.2,4
7.1,0.66,0.0,2.4,0.052000000000000005,6.0,11.0,0.99318,3.35,0.66,12.7,7
5.6,0.915,0.0,2.1,0.040999999999999995,17.0,78.0,0.99346,3.68,0.73,11.4,5
8.2,0.35,0.33,2.4,0.076,11.0,47.0,0.9959899999999999,3.27,0.81,11.0,6
8.2,0.35,0.33,2.4,0.076,11.0,47.0,0.9959899999999999,3.27,0.81,11.0,6
9.8,0.39,0.43,1.65,0.068,5.0,11.0,0.9947799999999999,3.19,0.46,11.4,5
10.2,0.4,0.4,2.5,0.068,41.0,54.0,0.99754,3.38,0.86,10.5,6
6.8,0.66,0.07,1.6,0.07,16.0,61.0,0.99572,3.29,0.6,9.3,5
6.7,0.64,0.23,2.1,0.08,11.0,119.0,0.9953799999999999,3.36,0.7,10.9,5
7.0,0.43,0.3,2.0,0.085,6.0,39.0,0.99346,3.33,0.46,11.9,6
6.6,0.8,0.03,7.8,0.079,6.0,12.0,0.9963,3.52,0.5,12.2,5
7.0,0.43,0.3,2.0,0.085,6.0,39.0,0.99346,3.33,0.46,11.9,6
6.7,0.64,0.23,2.1,0.08,11.0,119.0,0.9953799999999999,3.36,0.7,10.9,5
8.8,0.955,0.05,1.8,0.075,5.0,19.0,0.99616,3.3,0.44,9.6,4
9.1,0.4,0.57,4.6,0.08,6.0,20.0,0.9965200000000001,3.28,0.57,12.5,6
6.5,0.885,0.0,2.3,0.166,6.0,12.0,0.99551,3.56,0.51,10.8,5
7.2,0.25,0.37,2.5,0.063,11.0,41.0,0.99439,3.52,0.8,12.4,7
6.4,0.885,0.0,2.3,0.166,6.0,12.0,0.99551,3.56,0.51,10.8,5
7.0,0.745,0.12,1.8,0.114,15.0,64.0,0.9958799999999999,3.22,0.59,9.5,6
6.2,0.43,0.22,1.8,0.078,21.0,56.0,0.9963299999999999,3.52,0.6,9.5,6
7.9,0.58,0.23,2.3,0.076,23.0,94.0,0.9968600000000001,3.21,0.58,9.5,6
7.7,0.57,0.21,1.5,0.069,4.0,9.0,0.9945799999999999,3.16,0.54,9.8,6
7.7,0.26,0.26,2.0,0.052000000000000005,19.0,77.0,0.9951,3.15,0.79,10.9,6
7.9,0.58,0.23,2.3,0.076,23.0,94.0,0.9968600000000001,3.21,0.58,9.5,6
7.7,0.57,0.21,1.5,0.069,4.0,9.0,0.9945799999999999,3.16,0.54,9.8,6
7.9,0.34,0.36,1.9,0.065,5.0,10.0,0.99419,3.27,0.54,11.2,7
8.6,0.42,0.39,1.8,0.068,6.0,12.0,0.99516,3.35,0.69,11.7,8
9.9,0.74,0.19,5.8,0.111,33.0,76.0,0.9987799999999999,3.14,0.55,9.4,5
7.2,0.36,0.46,2.1,0.07400000000000001,24.0,44.0,0.99534,3.4,0.85,11.0,7
7.2,0.36,0.46,2.1,0.07400000000000001,24.0,44.0,0.99534,3.4,0.85,11.0,7
7.2,0.36,0.46,2.1,0.07400000000000001,24.0,44.0,0.99534,3.4,0.85,11.0,7
9.9,0.72,0.55,1.7,0.136,24.0,52.0,0.9975200000000001,3.35,0.94,10.0,5
7.2,0.36,0.46,2.1,0.07400000000000001,24.0,44.0,0.99534,3.4,0.85,11.0,7
6.2,0.39,0.43,2.0,0.071,14.0,24.0,0.9942799999999999,3.45,0.87,11.2,7
6.8,0.65,0.02,2.1,0.078,8.0,15.0,0.99498,3.35,0.62,10.4,6
6.6,0.44,0.15,2.1,0.076,22.0,53.0,0.9957,3.32,0.62,9.3,5
6.8,0.65,0.02,2.1,0.078,8.0,15.0,0.99498,3.35,0.62,10.4,6
9.6,0.38,0.42,1.9,0.071,5.0,13.0,0.99659,3.15,0.75,10.5,6
10.2,0.33,0.46,1.9,0.081,6.0,9.0,0.9962799999999999,3.1,0.48,10.4,6
8.8,0.27,0.46,2.1,0.095,20.0,29.0,0.9948799999999999,3.26,0.56,11.3,6
7.9,0.57,0.31,2.0,0.079,10.0,79.0,0.99677,3.29,0.69,9.5,6
8.2,0.34,0.37,1.9,0.057,43.0,74.0,0.99408,3.23,0.81,12.0,6
8.2,0.4,0.31,1.9,0.08199999999999999,8.0,24.0,0.996,3.24,0.69,10.6,6
9.0,0.39,0.4,1.3,0.044000000000000004,25.0,50.0,0.9947799999999999,3.2,0.83,10.9,6
10.9,0.32,0.52,1.8,0.132,17.0,44.0,0.99734,3.28,0.77,11.5,6
10.9,0.32,0.52,1.8,0.132,17.0,44.0,0.99734,3.28,0.77,11.5,6
8.1,0.53,0.22,2.2,0.078,33.0,89.0,0.9967799999999999,3.26,0.46,9.6,6
10.5,0.36,0.47,2.2,0.07400000000000001,9.0,23.0,0.9963799999999999,3.23,0.76,12.0,6
12.6,0.39,0.49,2.5,0.08,8.0,20.0,0.9992,3.07,0.82,10.3,6
9.2,0.46,0.23,2.6,0.091,18.0,77.0,0.9992200000000001,3.15,0.51,9.4,5
7.5,0.58,0.03,4.1,0.08,27.0,46.0,0.99592,3.02,0.47,9.2,5
9.0,0.58,0.25,2.0,0.10400000000000001,8.0,21.0,0.99769,3.27,0.72,9.6,5
5.1,0.42,0.0,1.8,0.044000000000000004,18.0,88.0,0.9915700000000001,3.68,0.73,13.6,7
7.6,0.43,0.29,2.1,0.075,19.0,66.0,0.99718,3.4,0.64,9.5,5
7.7,0.18,0.34,2.7,0.066,15.0,58.0,0.9947,3.37,0.78,11.8,6
7.8,0.815,0.01,2.6,0.07400000000000001,48.0,90.0,0.99621,3.38,0.62,10.8,5
7.6,0.43,0.29,2.1,0.075,19.0,66.0,0.99718,3.4,0.64,9.5,5
10.2,0.23,0.37,2.2,0.057,14.0,36.0,0.9961399999999999,3.23,0.49,9.3,4
7.1,0.75,0.01,2.2,0.059000000000000004,11.0,18.0,0.9924200000000001,3.39,0.4,12.8,6
6.0,0.33,0.32,12.9,0.054000000000000006,6.0,113.0,0.99572,3.3,0.56,11.5,4
7.8,0.55,0.0,1.7,0.07,7.0,17.0,0.99659,3.26,0.64,9.4,6
7.1,0.75,0.01,2.2,0.059000000000000004,11.0,18.0,0.9924200000000001,3.39,0.4,12.8,6
8.1,0.73,0.0,2.5,0.081,12.0,24.0,0.99798,3.38,0.46,9.6,4
6.5,0.67,0.0,4.3,0.057,11.0,20.0,0.9948799999999999,3.45,0.56,11.8,4
7.5,0.61,0.2,1.7,0.076,36.0,60.0,0.9949399999999999,3.1,0.4,9.3,5
9.8,0.37,0.39,2.5,0.079,28.0,65.0,0.99729,3.16,0.59,9.8,5
9.0,0.4,0.41,2.0,0.057999999999999996,15.0,40.0,0.9941399999999999,3.22,0.6,12.2,6
8.3,0.56,0.22,2.4,0.08199999999999999,10.0,86.0,0.9983,3.37,0.62,9.5,5
5.9,0.29,0.25,13.4,0.067,72.0,160.0,0.99721,3.33,0.54,10.3,6
7.4,0.55,0.19,1.8,0.08199999999999999,15.0,34.0,0.99655,3.49,0.68,10.5,5
7.4,0.74,0.07,1.7,0.086,15.0,48.0,0.9950200000000001,3.12,0.48,10.0,5
7.4,0.55,0.19,1.8,0.08199999999999999,15.0,34.0,0.99655,3.49,0.68,10.5,5
6.9,0.41,0.33,2.2,0.081,22.0,36.0,0.9949,3.41,0.75,11.1,6
7.1,0.6,0.01,2.3,0.079,24.0,37.0,0.9951399999999999,3.4,0.61,10.9,6
7.1,0.6,0.01,2.3,0.079,24.0,37.0,0.9951399999999999,3.4,0.61,10.9,6
7.5,0.58,0.14,2.2,0.077,27.0,60.0,0.9963,3.28,0.59,9.8,5
7.1,0.72,0.0,1.8,0.12300000000000001,6.0,14.0,0.9962700000000001,3.45,0.58,9.8,5
7.9,0.66,0.0,1.4,0.096,6.0,13.0,0.99569,3.43,0.58,9.5,5
7.8,0.7,0.06,1.9,0.079,20.0,35.0,0.9962799999999999,3.4,0.69,10.9,5
6.1,0.64,0.02,2.4,0.069,26.0,46.0,0.9935799999999999,3.47,0.45,11.0,5
7.5,0.59,0.22,1.8,0.08199999999999999,43.0,60.0,0.9949899999999999,3.1,0.42,9.2,5
7.0,0.58,0.28,4.8,0.085,12.0,69.0,0.9963299999999999,3.32,0.7,11.0,6
6.8,0.64,0.0,2.7,0.12300000000000001,15.0,33.0,0.9953799999999999,3.44,0.63,11.3,6
6.8,0.64,0.0,2.7,0.12300000000000001,15.0,33.0,0.9953799999999999,3.44,0.63,11.3,6
8.6,0.635,0.68,1.8,0.40299999999999997,19.0,56.0,0.9963200000000001,3.02,1.15,9.3,5
6.3,1.02,0.0,2.0,0.083,17.0,24.0,0.9943700000000001,3.59,0.55,11.2,4
9.8,0.45,0.38,2.5,0.081,34.0,66.0,0.99726,3.15,0.58,9.8,5
8.2,0.78,0.0,2.2,0.08900000000000001,13.0,26.0,0.9978,3.37,0.46,9.6,4
8.5,0.37,0.32,1.8,0.066,26.0,51.0,0.99456,3.38,0.72,11.8,6
7.2,0.57,0.05,2.3,0.081,16.0,36.0,0.99564,3.38,0.6,10.3,6
7.2,0.57,0.05,2.3,0.081,16.0,36.0,0.99564,3.38,0.6,10.3,6
10.4,0.43,0.5,2.3,0.068,13.0,19.0,0.996,3.1,0.87,11.4,6
6.9,0.41,0.31,2.0,0.079,21.0,51.0,0.9966799999999999,3.47,0.55,9.5,6
5.5,0.49,0.03,1.8,0.044000000000000004,28.0,87.0,0.9908,3.5,0.82,14.0,8
5.0,0.38,0.01,1.6,0.048,26.0,60.0,0.9908399999999999,3.7,0.75,14.0,6
7.3,0.44,0.2,1.6,0.049,24.0,64.0,0.9935,3.38,0.57,11.7,6
5.9,0.46,0.0,1.9,0.077,25.0,44.0,0.99385,3.5,0.53,11.2,5
7.5,0.58,0.2,2.0,0.073,34.0,44.0,0.9949399999999999,3.1,0.43,9.3,5
7.8,0.58,0.13,2.1,0.102,17.0,36.0,0.9944,3.24,0.53,11.2,6
8.0,0.715,0.22,2.3,0.075,13.0,81.0,0.9968799999999999,3.24,0.54,9.5,6
8.5,0.4,0.4,6.3,0.05,3.0,10.0,0.99566,3.28,0.56,12.0,4
7.0,0.69,0.0,1.9,0.114,3.0,10.0,0.99636,3.35,0.6,9.7,6
8.0,0.715,0.22,2.3,0.075,13.0,81.0,0.9968799999999999,3.24,0.54,9.5,6
9.8,0.3,0.39,1.7,0.062,3.0,9.0,0.9948,3.14,0.57,11.5,7
7.1,0.46,0.2,1.9,0.077,28.0,54.0,0.9956,3.37,0.64,10.4,6
7.1,0.46,0.2,1.9,0.077,28.0,54.0,0.9956,3.37,0.64,10.4,6
7.9,0.765,0.0,2.0,0.084,9.0,22.0,0.9961899999999999,3.33,0.68,10.9,6
8.7,0.63,0.28,2.7,0.096,17.0,69.0,0.99734,3.26,0.63,10.2,6
7.0,0.42,0.19,2.3,0.071,18.0,36.0,0.9947600000000001,3.39,0.56,10.9,5
11.3,0.37,0.5,1.8,0.09,20.0,47.0,0.99734,3.15,0.57,10.5,5
7.1,0.16,0.44,2.5,0.068,17.0,31.0,0.9932799999999999,3.35,0.54,12.4,6
8.0,0.6,0.08,2.6,0.055999999999999994,3.0,7.0,0.9928600000000001,3.22,0.37,13.0,5
7.0,0.6,0.3,4.5,0.068,20.0,110.0,0.9991399999999999,3.3,1.17,10.2,5
7.0,0.6,0.3,4.5,0.068,20.0,110.0,0.9991399999999999,3.3,1.17,10.2,5
7.6,0.74,0.0,1.9,0.1,6.0,12.0,0.99521,3.36,0.59,11.0,5
8.2,0.635,0.1,2.1,0.073,25.0,60.0,0.9963799999999999,3.29,0.75,10.9,6
5.9,0.395,0.13,2.4,0.055999999999999994,14.0,28.0,0.9936200000000001,3.62,0.67,12.4,6
7.5,0.755,0.0,1.9,0.084,6.0,12.0,0.99672,3.34,0.49,9.7,4
8.2,0.635,0.1,2.1,0.073,25.0,60.0,0.9963799999999999,3.29,0.75,10.9,6
6.6,0.63,0.0,4.3,0.09300000000000001,51.0,77.5,0.9955799999999999,3.2,0.45,9.5,5
6.6,0.63,0.0,4.3,0.09300000000000001,51.0,77.5,0.9955799999999999,3.2,0.45,9.5,5
7.2,0.53,0.14,2.1,0.064,15.0,29.0,0.99323,3.35,0.61,12.1,6
5.7,0.6,0.0,1.4,0.063,11.0,18.0,0.9919100000000001,3.45,0.56,12.2,6
7.6,1.58,0.0,2.1,0.13699999999999998,5.0,9.0,0.9947600000000001,3.5,0.4,10.9,3
5.2,0.645,0.0,2.15,0.08,15.0,28.0,0.99444,3.78,0.61,12.5,6
6.7,0.86,0.07,2.0,0.1,20.0,57.0,0.99598,3.6,0.74,11.7,6
9.1,0.37,0.32,2.1,0.064,4.0,15.0,0.9957600000000001,3.3,0.8,11.2,6
8.0,0.28,0.44,1.8,0.081,28.0,68.0,0.9950100000000001,3.36,0.66,11.2,5
7.6,0.79,0.21,2.3,0.087,21.0,68.0,0.9955,3.12,0.44,9.2,5
7.5,0.61,0.26,1.9,0.073,24.0,88.0,0.9961200000000001,3.3,0.53,9.8,5
9.7,0.69,0.32,2.5,0.08800000000000001,22.0,91.0,0.9979,3.29,0.62,10.1,5
6.8,0.68,0.09,3.9,0.068,15.0,29.0,0.99524,3.41,0.52,11.1,4
9.7,0.69,0.32,2.5,0.08800000000000001,22.0,91.0,0.9979,3.29,0.62,10.1,5
7.0,0.62,0.1,1.4,0.071,27.0,63.0,0.996,3.28,0.61,9.2,5
7.5,0.61,0.26,1.9,0.073,24.0,88.0,0.9961200000000001,3.3,0.53,9.8,5
6.5,0.51,0.15,3.0,0.064,12.0,27.0,0.9929,3.33,0.59,12.8,6
8.0,1.18,0.21,1.9,0.083,14.0,41.0,0.9953200000000001,3.34,0.47,10.5,5
7.0,0.36,0.21,2.3,0.086,20.0,65.0,0.9955799999999999,3.4,0.54,10.1,6
7.0,0.36,0.21,2.4,0.086,24.0,69.0,0.99556,3.4,0.53,10.1,6
7.5,0.63,0.27,2.0,0.083,17.0,91.0,0.99616,3.26,0.58,9.8,6
5.4,0.74,0.0,1.2,0.040999999999999995,16.0,46.0,0.9925799999999999,4.01,0.59,12.5,6
9.9,0.44,0.46,2.2,0.091,10.0,41.0,0.9963799999999999,3.18,0.69,11.9,6
7.5,0.63,0.27,2.0,0.083,17.0,91.0,0.99616,3.26,0.58,9.8,6
9.1,0.76,0.68,1.7,0.414,18.0,64.0,0.9965200000000001,2.9,1.33,9.1,6
9.7,0.66,0.34,2.6,0.094,12.0,88.0,0.9979600000000001,3.26,0.66,10.1,5
5.0,0.74,0.0,1.2,0.040999999999999995,16.0,46.0,0.9925799999999999,4.01,0.59,12.5,6
9.1,0.34,0.42,1.8,0.057999999999999996,9.0,18.0,0.99392,3.18,0.55,11.4,5
9.1,0.36,0.39,1.8,0.06,21.0,55.0,0.99495,3.18,0.82,11.0,7
6.7,0.46,0.24,1.7,0.077,18.0,34.0,0.9948,3.39,0.6,10.6,6
6.7,0.46,0.24,1.7,0.077,18.0,34.0,0.9948,3.39,0.6,10.6,6
6.7,0.46,0.24,1.7,0.077,18.0,34.0,0.9948,3.39,0.6,10.6,6
6.7,0.46,0.24,1.7,0.077,18.0,34.0,0.9948,3.39,0.6,10.6,6
6.5,0.52,0.11,1.8,0.073,13.0,38.0,0.9955,3.34,0.52,9.3,5
7.4,0.6,0.26,2.1,0.083,17.0,91.0,0.99616,3.29,0.56,9.8,6
7.4,0.6,0.26,2.1,0.083,17.0,91.0,0.99616,3.29,0.56,9.8,6
7.8,0.87,0.26,3.8,0.107,31.0,67.0,0.9966799999999999,3.26,0.46,9.2,5
8.4,0.39,0.1,1.7,0.075,6.0,25.0,0.9958100000000001,3.09,0.43,9.7,6
9.1,0.775,0.22,2.2,0.079,12.0,48.0,0.9976,3.18,0.51,9.6,5
7.2,0.835,0.0,2.0,0.166,4.0,11.0,0.99608,3.39,0.52,10.0,5
6.6,0.58,0.02,2.4,0.069,19.0,40.0,0.99387,3.38,0.66,12.6,6
6.0,0.5,0.0,1.4,0.057,15.0,26.0,0.9944799999999999,3.36,0.45,9.5,5
6.0,0.5,0.0,1.4,0.057,15.0,26.0,0.9944799999999999,3.36,0.45,9.5,5
6.0,0.5,0.0,1.4,0.057,15.0,26.0,0.9944799999999999,3.36,0.45,9.5,5
7.5,0.51,0.02,1.7,0.084,13.0,31.0,0.9953799999999999,3.36,0.54,10.5,6
7.5,0.51,0.02,1.7,0.084,13.0,31.0,0.9953799999999999,3.36,0.54,10.5,6
7.5,0.51,0.02,1.7,0.084,13.0,31.0,0.9953799999999999,3.36,0.54,10.5,6
7.6,0.54,0.02,1.7,0.085,17.0,31.0,0.9958899999999999,3.37,0.51,10.4,6
7.5,0.51,0.02,1.7,0.084,13.0,31.0,0.9953799999999999,3.36,0.54,10.5,6
11.5,0.42,0.48,2.6,0.077,8.0,20.0,0.9985200000000001,3.09,0.53,11.0,5
8.2,0.44,0.24,2.3,0.063,10.0,28.0,0.99613,3.25,0.53,10.2,6
6.1,0.59,0.01,2.1,0.055999999999999994,5.0,13.0,0.99472,3.52,0.56,11.4,5
7.2,0.655,0.03,1.8,0.078,7.0,12.0,0.99587,3.34,0.39,9.5,5
7.2,0.655,0.03,1.8,0.078,7.0,12.0,0.99587,3.34,0.39,9.5,5
6.9,0.57,0.0,2.8,0.081,21.0,41.0,0.99518,3.41,0.52,10.8,5
9.0,0.6,0.29,2.0,0.069,32.0,73.0,0.99654,3.34,0.57,10.0,5
7.2,0.62,0.01,2.3,0.065,8.0,46.0,0.9933200000000001,3.32,0.51,11.8,6
7.6,0.645,0.03,1.9,0.086,14.0,57.0,0.9969,3.37,0.46,10.3,5
7.6,0.645,0.03,1.9,0.086,14.0,57.0,0.9969,3.37,0.46,10.3,5
7.2,0.58,0.03,2.3,0.077,7.0,28.0,0.9956799999999999,3.35,0.52,10.0,5
6.1,0.32,0.25,1.8,0.086,5.0,32.0,0.99464,3.36,0.44,10.1,5
6.1,0.34,0.25,1.8,0.084,4.0,28.0,0.99464,3.36,0.44,10.1,5
7.3,0.43,0.24,2.5,0.078,27.0,67.0,0.9964799999999999,3.6,0.59,11.1,6
7.4,0.64,0.17,5.4,0.168,52.0,98.0,0.99736,3.28,0.5,9.5,5
11.6,0.475,0.4,1.4,0.091,6.0,28.0,0.9970399999999999,3.07,0.65,10.0333333333333,6
9.2,0.54,0.31,2.3,0.11199999999999999,11.0,38.0,0.9969899999999999,3.24,0.56,10.9,5
8.3,0.85,0.14,2.5,0.09300000000000001,13.0,54.0,0.99724,3.36,0.54,10.1,5
11.6,0.475,0.4,1.4,0.091,6.0,28.0,0.9970399999999999,3.07,0.65,10.0333333333333,6
8.0,0.83,0.27,2.0,0.08,11.0,63.0,0.9965200000000001,3.29,0.48,9.8,4
7.2,0.605,0.02,1.9,0.096,10.0,31.0,0.995,3.46,0.53,11.8,6
7.8,0.5,0.09,2.2,0.115,10.0,42.0,0.9971,3.18,0.62,9.5,5
7.3,0.74,0.08,1.7,0.094,10.0,45.0,0.9957600000000001,3.24,0.5,9.8,5
6.9,0.54,0.3,2.2,0.08800000000000001,9.0,105.0,0.99725,3.25,1.18,10.5,6
8.0,0.77,0.32,2.1,0.079,16.0,74.0,0.99656,3.27,0.5,9.8,6
6.6,0.61,0.0,1.6,0.069,4.0,8.0,0.9939600000000001,3.33,0.37,10.4,4
8.7,0.78,0.51,1.7,0.415,12.0,66.0,0.99623,3.0,1.17,9.2,5
7.5,0.58,0.56,3.1,0.153,5.0,14.0,0.9947600000000001,3.21,1.03,11.6,6
8.7,0.78,0.51,1.7,0.415,12.0,66.0,0.99623,3.0,1.17,9.2,5
7.7,0.75,0.27,3.8,0.11,34.0,89.0,0.99664,3.24,0.45,9.3,5
6.8,0.815,0.0,1.2,0.267,16.0,29.0,0.99471,3.32,0.51,9.8,3
7.2,0.56,0.26,2.0,0.083,13.0,100.0,0.9958600000000001,3.26,0.52,9.9,5
8.2,0.885,0.2,1.4,0.086,7.0,31.0,0.9946,3.11,0.46,10.0,5
5.2,0.49,0.26,2.3,0.09,23.0,74.0,0.9953,3.71,0.62,12.2,6
7.2,0.45,0.15,2.0,0.078,10.0,28.0,0.9960899999999999,3.29,0.51,9.9,6
7.5,0.57,0.02,2.6,0.077,11.0,35.0,0.9955700000000001,3.36,0.62,10.8,6
7.5,0.57,0.02,2.6,0.077,11.0,35.0,0.9955700000000001,3.36,0.62,10.8,6
6.8,0.83,0.09,1.8,0.07400000000000001,4.0,25.0,0.99534,3.38,0.45,9.6,5
8.0,0.6,0.22,2.1,0.08,25.0,105.0,0.99613,3.3,0.49,9.9,5
8.0,0.6,0.22,2.1,0.08,25.0,105.0,0.99613,3.3,0.49,9.9,5
7.1,0.755,0.15,1.8,0.107,20.0,84.0,0.99593,3.19,0.5,9.5,5
8.0,0.81,0.25,3.4,0.076,34.0,85.0,0.9966799999999999,3.19,0.42,9.2,5
7.4,0.64,0.07,1.8,0.1,8.0,23.0,0.9961,3.3,0.58,9.6,5
7.4,0.64,0.07,1.8,0.1,8.0,23.0,0.9961,3.3,0.58,9.6,5
6.6,0.64,0.31,6.1,0.083,7.0,49.0,0.99718,3.35,0.68,10.3,5
6.7,0.48,0.02,2.2,0.08,36.0,111.0,0.99524,3.1,0.53,9.7,5
6.0,0.49,0.0,2.3,0.068,15.0,33.0,0.99292,3.58,0.59,12.5,6
8.0,0.64,0.22,2.4,0.094,5.0,33.0,0.9961200000000001,3.37,0.58,11.0,5
7.1,0.62,0.06,1.3,0.07,5.0,12.0,0.9942,3.17,0.48,9.8,5
8.0,0.52,0.25,2.0,0.078,19.0,59.0,0.9961200000000001,3.3,0.48,10.2,5
6.4,0.57,0.14,3.9,0.07,27.0,73.0,0.99669,3.32,0.48,9.2,5
8.6,0.685,0.1,1.6,0.092,3.0,12.0,0.99745,3.31,0.65,9.55,6
8.7,0.675,0.1,1.6,0.09,4.0,11.0,0.99745,3.31,0.65,9.55,5
7.3,0.59,0.26,2.0,0.08,17.0,104.0,0.99584,3.28,0.52,9.9,5
7.0,0.6,0.12,2.2,0.083,13.0,28.0,0.9966,3.52,0.62,10.2,7
7.2,0.67,0.0,2.2,0.068,10.0,24.0,0.9956,3.42,0.72,11.1,6
7.9,0.69,0.21,2.1,0.08,33.0,141.0,0.9962,3.25,0.51,9.9,5
7.9,0.69,0.21,2.1,0.08,33.0,141.0,0.9962,3.25,0.51,9.9,5
7.6,0.3,0.42,2.0,0.052000000000000005,6.0,24.0,0.9963,3.44,0.82,11.9,6
7.2,0.33,0.33,1.7,0.061,3.0,13.0,0.996,3.23,1.1,10.0,8
8.0,0.5,0.39,2.6,0.08199999999999999,12.0,46.0,0.9985,3.43,0.62,10.7,6
7.7,0.28,0.3,2.0,0.062,18.0,34.0,0.9952,3.28,0.9,11.3,7
8.2,0.24,0.34,5.1,0.062,8.0,22.0,0.9974,3.22,0.94,10.9,6
6.0,0.51,0.0,2.1,0.064,40.0,54.0,0.995,3.54,0.93,10.7,6
8.1,0.29,0.36,2.2,0.048,35.0,53.0,0.995,3.27,1.01,12.4,7
6.0,0.51,0.0,2.1,0.064,40.0,54.0,0.995,3.54,0.93,10.7,6
6.6,0.96,0.0,1.8,0.08199999999999999,5.0,16.0,0.9936,3.5,0.44,11.9,6
6.4,0.47,0.4,2.4,0.071,8.0,19.0,0.9963,3.56,0.73,10.6,6
8.2,0.24,0.34,5.1,0.062,8.0,22.0,0.9974,3.22,0.94,10.9,6
9.9,0.57,0.25,2.0,0.10400000000000001,12.0,89.0,0.9963,3.04,0.9,10.1,5
10.0,0.32,0.59,2.2,0.077,3.0,15.0,0.9994,3.2,0.78,9.6,5
6.2,0.58,0.0,1.6,0.065,8.0,18.0,0.9966,3.56,0.84,9.4,5
10.0,0.32,0.59,2.2,0.077,3.0,15.0,0.9994,3.2,0.78,9.6,5
7.3,0.34,0.33,2.5,0.064,21.0,37.0,0.9952,3.35,0.77,12.1,7
7.8,0.53,0.01,1.6,0.077,3.0,19.0,0.995,3.16,0.46,9.8,5
7.7,0.64,0.21,2.2,0.077,32.0,133.0,0.9956,3.27,0.45,9.9,5
7.8,0.53,0.01,1.6,0.077,3.0,19.0,0.995,3.16,0.46,9.8,5
7.5,0.4,0.18,1.6,0.079,24.0,58.0,0.9965,3.34,0.58,9.4,5
7.0,0.54,0.0,2.1,0.079,39.0,55.0,0.9956,3.39,0.84,11.4,6
6.4,0.53,0.09,3.9,0.12300000000000001,14.0,31.0,0.9968,3.5,0.67,11.0,4
8.3,0.26,0.37,1.4,0.076,8.0,23.0,0.9974,3.26,0.7,9.6,6
8.3,0.26,0.37,1.4,0.076,8.0,23.0,0.9974,3.26,0.7,9.6,6
7.7,0.23,0.37,1.8,0.046,23.0,60.0,0.9971,3.41,0.71,12.1,6
7.6,0.41,0.33,2.5,0.078,6.0,23.0,0.9957,3.3,0.58,11.2,5
7.8,0.64,0.0,1.9,0.07200000000000001,27.0,55.0,0.9962,3.31,0.63,11.0,5
7.9,0.18,0.4,2.2,0.049,38.0,67.0,0.996,3.33,0.93,11.3,5
7.4,0.41,0.24,1.8,0.066,18.0,47.0,0.9956,3.37,0.62,10.4,5
7.6,0.43,0.31,2.1,0.069,13.0,74.0,0.9958,3.26,0.54,9.9,6
5.9,0.44,0.0,1.6,0.042,3.0,11.0,0.9944,3.48,0.85,11.7,6
6.1,0.4,0.16,1.8,0.069,11.0,25.0,0.9955,3.42,0.74,10.1,7
10.2,0.54,0.37,15.4,0.214,55.0,95.0,1.00369,3.18,0.77,9.0,6
10.2,0.54,0.37,15.4,0.214,55.0,95.0,1.00369,3.18,0.77,9.0,6
10.0,0.38,0.38,1.6,0.16899999999999998,27.0,90.0,0.9991399999999999,3.15,0.65,8.5,5
6.8,0.915,0.29,4.8,0.07,15.0,39.0,0.99577,3.53,0.54,11.1,5
7.0,0.59,0.0,1.7,0.052000000000000005,3.0,8.0,0.996,3.41,0.47,10.3,5
7.3,0.67,0.02,2.2,0.07200000000000001,31.0,92.0,0.99566,3.32,0.68,11.066666666666698,6
7.2,0.37,0.32,2.0,0.062,15.0,28.0,0.9947,3.23,0.73,11.3,7
7.4,0.785,0.19,5.2,0.094,19.0,98.0,0.99713,3.16,0.52,9.56666666666667,6
6.9,0.63,0.02,1.9,0.078,18.0,30.0,0.9971200000000001,3.4,0.75,9.8,5
6.9,0.58,0.2,1.75,0.057999999999999996,8.0,22.0,0.9932200000000001,3.38,0.49,11.7,5
7.3,0.67,0.02,2.2,0.07200000000000001,31.0,92.0,0.99566,3.32,0.68,11.1,6
7.4,0.785,0.19,5.2,0.094,19.0,98.0,0.99713,3.16,0.52,9.6,6
6.9,0.63,0.02,1.9,0.078,18.0,30.0,0.9971200000000001,3.4,0.75,9.8,5
6.8,0.67,0.0,1.9,0.08,22.0,39.0,0.9970100000000001,3.4,0.74,9.7,5
6.9,0.58,0.01,1.9,0.08,40.0,54.0,0.9968299999999999,3.4,0.73,9.7,5
7.2,0.38,0.31,2.0,0.055999999999999994,15.0,29.0,0.99472,3.23,0.76,11.3,8
7.2,0.37,0.32,2.0,0.062,15.0,28.0,0.9947,3.23,0.73,11.3,7
7.8,0.32,0.44,2.7,0.10400000000000001,8.0,17.0,0.9973200000000001,3.33,0.78,11.0,7
6.6,0.58,0.02,2.0,0.062,37.0,53.0,0.99374,3.35,0.76,11.6,7
7.6,0.49,0.33,1.9,0.07400000000000001,27.0,85.0,0.9970600000000001,3.41,0.58,9.0,5
11.7,0.45,0.63,2.2,0.073,7.0,23.0,0.99974,3.21,0.69,10.9,6
6.5,0.9,0.0,1.6,0.052000000000000005,9.0,17.0,0.99467,3.5,0.63,10.9,6
6.0,0.54,0.06,1.8,0.05,38.0,89.0,0.99236,3.3,0.5,10.55,6
7.6,0.49,0.33,1.9,0.07400000000000001,27.0,85.0,0.9970600000000001,3.41,0.58,9.0,5
8.4,0.29,0.4,1.7,0.067,8.0,20.0,0.99603,3.39,0.6,10.5,5
7.9,0.2,0.35,1.7,0.054000000000000006,7.0,15.0,0.9945799999999999,3.32,0.8,11.9,7
6.4,0.42,0.09,2.3,0.054000000000000006,34.0,64.0,0.99724,3.41,0.68,10.4,6
6.2,0.785,0.0,2.1,0.06,6.0,13.0,0.99664,3.59,0.61,10.0,4
6.8,0.64,0.03,2.3,0.075,14.0,31.0,0.99545,3.36,0.58,10.4,6
6.9,0.63,0.01,2.4,0.076,14.0,39.0,0.9952200000000001,3.34,0.53,10.8,6
6.8,0.59,0.1,1.7,0.063,34.0,53.0,0.9958,3.41,0.67,9.7,5
6.8,0.59,0.1,1.7,0.063,34.0,53.0,0.9958,3.41,0.67,9.7,5
7.3,0.48,0.32,2.1,0.062,31.0,54.0,0.9972799999999999,3.3,0.65,10.0,7
6.7,1.04,0.08,2.3,0.067,19.0,32.0,0.9964799999999999,3.52,0.57,11.0,4
7.3,0.48,0.32,2.1,0.062,31.0,54.0,0.9972799999999999,3.3,0.65,10.0,7
7.3,0.98,0.05,2.1,0.061,20.0,49.0,0.99705,3.31,0.55,9.7,3
10.0,0.69,0.11,1.4,0.084,8.0,24.0,0.9957799999999999,2.88,0.47,9.7,5
6.7,0.7,0.08,3.75,0.067,8.0,16.0,0.99334,3.43,0.52,12.6,5
7.6,0.35,0.6,2.6,0.073,23.0,44.0,0.99656,3.38,0.79,11.1,6
6.1,0.6,0.08,1.8,0.071,14.0,45.0,0.99336,3.38,0.54,11.0,5
9.9,0.5,0.5,13.8,0.205,48.0,82.0,1.00242,3.16,0.75,8.8,5
5.3,0.47,0.11,2.2,0.048,16.0,89.0,0.99182,3.54,0.88,13.566666666666698,7
9.9,0.5,0.5,13.8,0.205,48.0,82.0,1.00242,3.16,0.75,8.8,5
5.3,0.47,0.11,2.2,0.048,16.0,89.0,0.99182,3.54,0.88,13.6,7
7.1,0.875,0.05,5.7,0.08199999999999999,3.0,14.0,0.99808,3.4,0.52,10.2,3
8.2,0.28,0.6,3.0,0.10400000000000001,10.0,22.0,0.99828,3.39,0.68,10.6,5
5.6,0.62,0.03,1.5,0.08,6.0,13.0,0.99498,3.66,0.62,10.1,4
8.2,0.28,0.6,3.0,0.10400000000000001,10.0,22.0,0.99828,3.39,0.68,10.6,5
7.2,0.58,0.54,2.1,0.114,3.0,9.0,0.9971899999999999,3.33,0.57,10.3,4
8.1,0.33,0.44,1.5,0.042,6.0,12.0,0.9954200000000001,3.35,0.61,10.7,5
6.8,0.91,0.06,2.0,0.06,4.0,11.0,0.99592,3.53,0.64,10.9,4
7.0,0.655,0.16,2.1,0.07400000000000001,8.0,25.0,0.9960600000000001,3.37,0.55,9.7,5
6.8,0.68,0.21,2.1,0.07,9.0,23.0,0.99546,3.38,0.6,10.3,5
6.0,0.64,0.05,1.9,0.066,9.0,17.0,0.9949600000000001,3.52,0.78,10.6,5
5.6,0.54,0.04,1.7,0.049,5.0,13.0,0.9942,3.72,0.58,11.4,5
6.2,0.57,0.1,2.1,0.048,4.0,11.0,0.9944799999999999,3.44,0.76,10.8,6
7.1,0.22,0.49,1.8,0.039,8.0,18.0,0.99344,3.39,0.56,12.4,6
5.6,0.54,0.04,1.7,0.049,5.0,13.0,0.9942,3.72,0.58,11.4,5
6.2,0.65,0.06,1.6,0.05,6.0,18.0,0.9934799999999999,3.57,0.54,11.95,5
7.7,0.54,0.26,1.9,0.08900000000000001,23.0,147.0,0.99636,3.26,0.59,9.7,5
6.4,0.31,0.09,1.4,0.066,15.0,28.0,0.99459,3.42,0.7,10.0,7
7.0,0.43,0.02,1.9,0.08,15.0,28.0,0.99492,3.35,0.81,10.6,6
7.7,0.54,0.26,1.9,0.08900000000000001,23.0,147.0,0.99636,3.26,0.59,9.7,5
6.9,0.74,0.03,2.3,0.054000000000000006,7.0,16.0,0.99508,3.45,0.63,11.5,6
6.6,0.895,0.04,2.3,0.068,7.0,13.0,0.99582,3.53,0.58,10.8,6
6.9,0.74,0.03,2.3,0.054000000000000006,7.0,16.0,0.99508,3.45,0.63,11.5,6
7.5,0.725,0.04,1.5,0.076,8.0,15.0,0.99508,3.26,0.53,9.6,5
7.8,0.82,0.29,4.3,0.083,21.0,64.0,0.9964200000000001,3.16,0.53,9.4,5
7.3,0.585,0.18,2.4,0.078,15.0,60.0,0.9963799999999999,3.31,0.54,9.8,5
6.2,0.44,0.39,2.5,0.077,6.0,14.0,0.99555,3.51,0.69,11.0,6
7.5,0.38,0.57,2.3,0.106,5.0,12.0,0.99605,3.36,0.55,11.4,6
6.7,0.76,0.02,1.8,0.078,6.0,12.0,0.996,3.55,0.63,9.95,3
6.8,0.81,0.05,2.0,0.07,6.0,14.0,0.9956200000000001,3.51,0.66,10.8,6
7.5,0.38,0.57,2.3,0.106,5.0,12.0,0.99605,3.36,0.55,11.4,6
7.1,0.27,0.6,2.1,0.07400000000000001,17.0,25.0,0.9981399999999999,3.38,0.72,10.6,6
7.9,0.18,0.4,1.8,0.062,7.0,20.0,0.9941,3.28,0.7,11.1,5
6.4,0.36,0.21,2.2,0.047,26.0,48.0,0.99661,3.47,0.77,9.7,6
7.1,0.69,0.04,2.1,0.068,19.0,27.0,0.9971200000000001,3.44,0.67,9.8,5
6.4,0.79,0.04,2.2,0.061,11.0,17.0,0.9958799999999999,3.53,0.65,10.4,6
6.4,0.56,0.15,1.8,0.078,17.0,65.0,0.9929399999999999,3.33,0.6,10.5,6
6.9,0.84,0.21,4.1,0.07400000000000001,16.0,65.0,0.9984200000000001,3.53,0.72,9.23333333333333,6
6.9,0.84,0.21,4.1,0.07400000000000001,16.0,65.0,0.9984200000000001,3.53,0.72,9.25,6
6.1,0.32,0.25,2.3,0.071,23.0,58.0,0.9963299999999999,3.42,0.97,10.6,5
6.5,0.53,0.06,2.0,0.063,29.0,44.0,0.9948899999999999,3.38,0.83,10.3,6
7.4,0.47,0.46,2.2,0.114,7.0,20.0,0.9964700000000001,3.32,0.63,10.5,5
6.6,0.7,0.08,2.6,0.106,14.0,27.0,0.99665,3.44,0.58,10.2,5
6.5,0.53,0.06,2.0,0.063,29.0,44.0,0.9948899999999999,3.38,0.83,10.3,6
6.9,0.48,0.2,1.9,0.08199999999999999,9.0,23.0,0.99585,3.39,0.43,9.05,4
6.1,0.32,0.25,2.3,0.071,23.0,58.0,0.9963299999999999,3.42,0.97,10.6,5
6.8,0.48,0.25,2.0,0.076,29.0,61.0,0.9953,3.34,0.6,10.4,5
6.0,0.42,0.19,2.0,0.075,22.0,47.0,0.9952200000000001,3.39,0.78,10.0,6
6.7,0.48,0.08,2.1,0.064,18.0,34.0,0.9955200000000001,3.33,0.64,9.7,5
6.8,0.47,0.08,2.2,0.064,18.0,38.0,0.9955299999999999,3.3,0.65,9.6,6
7.1,0.53,0.07,1.7,0.071,15.0,24.0,0.9951,3.29,0.66,10.8,6
7.9,0.29,0.49,2.2,0.096,21.0,59.0,0.9971399999999999,3.31,0.67,10.1,6
7.1,0.69,0.08,2.1,0.063,42.0,52.0,0.99608,3.42,0.6,10.2,6
6.6,0.44,0.09,2.2,0.063,9.0,18.0,0.99444,3.42,0.69,11.3,6
6.1,0.705,0.1,2.8,0.081,13.0,28.0,0.99631,3.6,0.66,10.2,5
7.2,0.53,0.13,2.0,0.057999999999999996,18.0,22.0,0.9957299999999999,3.21,0.68,9.9,6
8.0,0.39,0.3,1.9,0.07400000000000001,32.0,84.0,0.9971700000000001,3.39,0.61,9.0,5
6.6,0.56,0.14,2.4,0.064,13.0,29.0,0.99397,3.42,0.62,11.7,7
7.0,0.55,0.13,2.2,0.075,15.0,35.0,0.9959,3.36,0.59,9.7,6
6.1,0.53,0.08,1.9,0.077,24.0,45.0,0.9952799999999999,3.6,0.68,10.3,6
5.4,0.58,0.08,1.9,0.059000000000000004,20.0,31.0,0.99484,3.5,0.64,10.2,6
6.2,0.64,0.09,2.5,0.081,15.0,26.0,0.9953799999999999,3.57,0.63,12.0,5
7.2,0.39,0.32,1.8,0.065,34.0,60.0,0.9971399999999999,3.46,0.78,9.9,5
6.2,0.52,0.08,4.4,0.071,11.0,32.0,0.99646,3.56,0.63,11.6,6
7.4,0.25,0.29,2.2,0.054000000000000006,19.0,49.0,0.99666,3.4,0.76,10.9,7
6.7,0.855,0.02,1.9,0.064,29.0,38.0,0.99472,3.3,0.56,10.75,6
11.1,0.44,0.42,2.2,0.064,14.0,19.0,0.9975799999999999,3.25,0.57,10.4,6
8.4,0.37,0.43,2.3,0.063,12.0,19.0,0.9955,3.17,0.81,11.2,7
6.5,0.63,0.33,1.8,0.059000000000000004,16.0,28.0,0.99531,3.36,0.64,10.1,6
7.0,0.57,0.02,2.0,0.07200000000000001,17.0,26.0,0.99575,3.36,0.61,10.2,5
6.3,0.6,0.1,1.6,0.048,12.0,26.0,0.99306,3.55,0.51,12.1,5
11.2,0.4,0.5,2.0,0.099,19.0,50.0,0.9978299999999999,3.1,0.58,10.4,5
7.4,0.36,0.3,1.8,0.07400000000000001,17.0,24.0,0.99419,3.24,0.7,11.4,8
7.1,0.68,0.0,2.3,0.087,17.0,26.0,0.9978299999999999,3.45,0.53,9.5,5
7.1,0.67,0.0,2.3,0.083,18.0,27.0,0.9976799999999999,3.44,0.54,9.4,5
6.3,0.68,0.01,3.7,0.10300000000000001,32.0,54.0,0.9958600000000001,3.51,0.66,11.3,6
7.3,0.735,0.0,2.2,0.08,18.0,28.0,0.99765,3.41,0.6,9.4,5
6.6,0.855,0.02,2.4,0.062,15.0,23.0,0.9962700000000001,3.54,0.6,11.0,6
7.0,0.56,0.17,1.7,0.065,15.0,24.0,0.9951399999999999,3.44,0.68,10.55,7
6.6,0.88,0.04,2.2,0.066,12.0,20.0,0.99636,3.53,0.56,9.9,5
6.6,0.855,0.02,2.4,0.062,15.0,23.0,0.9962700000000001,3.54,0.6,11.0,6
6.9,0.63,0.33,6.7,0.235,66.0,115.0,0.99787,3.22,0.56,9.5,5
7.8,0.6,0.26,2.0,0.08,31.0,131.0,0.9962200000000001,3.21,0.52,9.9,5
7.8,0.6,0.26,2.0,0.08,31.0,131.0,0.9962200000000001,3.21,0.52,9.9,5
7.8,0.6,0.26,2.0,0.08,31.0,131.0,0.9962200000000001,3.21,0.52,9.9,5
7.2,0.695,0.13,2.0,0.076,12.0,20.0,0.99546,3.29,0.54,10.1,5
7.2,0.695,0.13,2.0,0.076,12.0,20.0,0.99546,3.29,0.54,10.1,5
7.2,0.695,0.13,2.0,0.076,12.0,20.0,0.99546,3.29,0.54,10.1,5
6.7,0.67,0.02,1.9,0.061,26.0,42.0,0.9948899999999999,3.39,0.82,10.9,6
6.7,0.16,0.64,2.1,0.059000000000000004,24.0,52.0,0.9949399999999999,3.34,0.71,11.2,6
7.2,0.695,0.13,2.0,0.076,12.0,20.0,0.99546,3.29,0.54,10.1,5
7.0,0.56,0.13,1.6,0.077,25.0,42.0,0.99629,3.34,0.59,9.2,5
6.2,0.51,0.14,1.9,0.055999999999999994,15.0,34.0,0.9939600000000001,3.48,0.57,11.5,6
6.4,0.36,0.53,2.2,0.23,19.0,35.0,0.9934,3.37,0.93,12.4,6
6.4,0.38,0.14,2.2,0.038,15.0,25.0,0.9951399999999999,3.44,0.65,11.1,6
7.3,0.69,0.32,2.2,0.069,35.0,104.0,0.9963200000000001,3.33,0.51,9.5,5
6.0,0.58,0.2,2.4,0.075,15.0,50.0,0.99467,3.58,0.67,12.5,6
5.6,0.31,0.78,13.9,0.07400000000000001,23.0,92.0,0.99677,3.39,0.48,10.5,6
7.5,0.52,0.4,2.2,0.06,12.0,20.0,0.99474,3.26,0.64,11.8,6
8.0,0.3,0.63,1.6,0.081,16.0,29.0,0.9958799999999999,3.3,0.78,10.8,6
6.2,0.7,0.15,5.1,0.076,13.0,27.0,0.9962200000000001,3.54,0.6,11.9,6
6.8,0.67,0.15,1.8,0.11800000000000001,13.0,20.0,0.9954,3.42,0.67,11.3,6
6.2,0.56,0.09,1.7,0.053,24.0,32.0,0.9940200000000001,3.54,0.6,11.3,5
7.4,0.35,0.33,2.4,0.068,9.0,26.0,0.9947,3.36,0.6,11.9,6
6.2,0.56,0.09,1.7,0.053,24.0,32.0,0.9940200000000001,3.54,0.6,11.3,5
6.1,0.715,0.1,2.6,0.053,13.0,27.0,0.9936200000000001,3.57,0.5,11.9,5
6.2,0.46,0.29,2.1,0.07400000000000001,32.0,98.0,0.9957799999999999,3.33,0.62,9.8,5
6.7,0.32,0.44,2.4,0.061,24.0,34.0,0.99484,3.29,0.8,11.6,7
7.2,0.39,0.44,2.6,0.066,22.0,48.0,0.9949399999999999,3.3,0.84,11.5,6
7.5,0.31,0.41,2.4,0.065,34.0,60.0,0.99492,3.34,0.85,11.4,6
5.8,0.61,0.11,1.8,0.066,18.0,28.0,0.9948299999999999,3.55,0.66,10.9,6
7.2,0.66,0.33,2.5,0.068,34.0,102.0,0.9941399999999999,3.27,0.78,12.8,6
6.6,0.725,0.2,7.8,0.073,29.0,79.0,0.9977,3.29,0.54,9.2,5
6.3,0.55,0.15,1.8,0.077,26.0,35.0,0.9931399999999999,3.32,0.82,11.6,6
5.4,0.74,0.09,1.7,0.08900000000000001,16.0,26.0,0.9940200000000001,3.67,0.56,11.6,6
6.3,0.51,0.13,2.3,0.076,29.0,40.0,0.99574,3.42,0.75,11.0,6
6.8,0.62,0.08,1.9,0.068,28.0,38.0,0.99651,3.42,0.82,9.5,6
6.2,0.6,0.08,2.0,0.09,32.0,44.0,0.9949,3.45,0.58,10.5,5
5.9,0.55,0.1,2.2,0.062,39.0,51.0,0.9951200000000001,3.52,0.76,11.2,6
6.3,0.51,0.13,2.3,0.076,29.0,40.0,0.99574,3.42,0.75,11.0,6
5.9,0.645,0.12,2.0,0.075,32.0,44.0,0.9954700000000001,3.57,0.71,10.2,5
6.0,0.31,0.47,3.6,0.067,18.0,42.0,0.99549,3.39,0.66,11.0,6
```

## File: `templates/error.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Error - Wine Quality Prediction</title>
</head>
<body>
    <h1>Error</h1>
    <p>An error occurred while processing your request:</p>
    <p>{{ error_message }}</p>
    <p>Please try again later.</p>
</body>
</html>
```

## File: `templates/index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Wine Quality Prediction</title>
</head>
<body>
    <h1>Wine Quality Prediction</h1>
    <form id="wine-form" method="POST" action="/predict">
        <label for="fixed_acidity">Fixed Acidity:</label>
        <input type="number" id="fixed_acidity" name="fixed_acidity" min="0.0" max="20.0" step="0.1" required><br><br>

        <label for="volatile_acidity">Volatile Acidity:</label>
        <input type="number" id="volatile_acidity" name="volatile_acidity" min="0.0" max="2.0" step="0.01" required><br><br>

        <label for="citric_acid">Citric Acid:</label>
        <input type="number" id="citric_acid" name="citric_acid" min="0.0" max="2.0" step="0.01" required><br><br>

        <label for="residual_sugar">Residual Sugar:</label>
        <input type="number" id="residual_sugar" name="residual_sugar" min="0.0" max="100.0" step="0.1" required><br><br>

        <label for="chlorides">Chlorides:</label>
        <input type="number" id="chlorides" name="chlorides" min="0.0" max="1.0" step="0.01" required><br><br>

        <label for="freesulfurdioxide">Free Sulfur Dioxide:</label>
        <input type="number" id="freesulfurdioxide" name="freesulfurdioxide" min="0" max="300" step="1" required><br><br>

        <label for="totalsulfurdioxide">Total Sulfur Dioxide:</label>
        <input type="number" id="totalsulfurdioxide" name="totalsulfurdioxide" min="0" max="600" step="1" required><br><br>

        <label for="density">Density:</label>
        <input type="number" id="density" name="density" min="0.0" max="2.0" step="0.001" required><br><br>

        <label for="ph">pH:</label>
        <input type="number" id="ph" name="ph" min="0.0" max="14.0" step="0.01" required><br><br>

        <label for="sulphates">Sulphates:</label>
        <input type="number" id="sulphates" name="sulphates" min="0.0" max="2.0" step="0.01" required><br><br>

        <label for="alcohol">Alcohol:</label>
        <input type="number" id="alcohol" name="alcohol" min="0.0" max="20.0" step="0.1" required><br><br>

        <button type="submit">Predict Wine Quality</button>
    </form>

    <!-- Add a div to display the prediction result -->
    <div id="result"></div>

    <!-- Include JavaScript to handle the result display -->
    <script>
        const form = document.getElementById('wine-form');
        const resultDiv = document.getElementById('result');

        form.addEventListener('submit', async (event) => {
            event.preventDefault();

            // Collect form data
            const formData = new FormData(form);

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    body: formData,
                });

                if (!response.ok) {
                    throw new Error('Prediction request failed.');
                }

                const data = await response.json();

                // Display the prediction result in the result <div>
                resultDiv.innerText = `Prediction: ${data.result}`;
            } catch (error) {
                console.error(error);
                resultDiv.innerText = 'Prediction failed. Please try again.';
            }
        });
    </script>
</body>
</html>
```

