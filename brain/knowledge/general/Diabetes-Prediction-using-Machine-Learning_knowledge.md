---
id: diabetes-prediction-using-machine-learning-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:19.883572
---

# KNOWLEDGE EXTRACT: Diabetes-Prediction-using-Machine-Learning
> **Extracted on:** 2026-03-29 20:30:41
> **Source:** Diabetes-Prediction-using-Machine-Learning

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
brain/knowledge/docs_legacy/_build/

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
#   https://python-poetry.org/brain/knowledge/docs_legacy/basic-usage/#commit-your-poetrylock-file-to-version-control
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

## File: `Diabetes Prediction using Support Vector Machines.ipynb`
```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "a3a811ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.simplefilter('ignore')\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "287a0b31",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"diabetesdata.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "580fd291",
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
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>148</td>\n",
       "      <td>72</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>66</td>\n",
       "      <td>29</td>\n",
       "      <td>0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183</td>\n",
       "      <td>64</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.672</td>\n",
       "      <td>32</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89</td>\n",
       "      <td>66</td>\n",
       "      <td>23</td>\n",
       "      <td>94</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.167</td>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>168</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.288</td>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
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
       "    </tr>\n",
       "    <tr>\n",
       "      <th>763</th>\n",
       "      <td>10</td>\n",
       "      <td>101</td>\n",
       "      <td>76</td>\n",
       "      <td>48</td>\n",
       "      <td>180</td>\n",
       "      <td>32.9</td>\n",
       "      <td>0.171</td>\n",
       "      <td>63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>764</th>\n",
       "      <td>2</td>\n",
       "      <td>122</td>\n",
       "      <td>70</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>36.8</td>\n",
       "      <td>0.340</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>765</th>\n",
       "      <td>5</td>\n",
       "      <td>121</td>\n",
       "      <td>72</td>\n",
       "      <td>23</td>\n",
       "      <td>112</td>\n",
       "      <td>26.2</td>\n",
       "      <td>0.245</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>766</th>\n",
       "      <td>1</td>\n",
       "      <td>126</td>\n",
       "      <td>60</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>30.1</td>\n",
       "      <td>0.349</td>\n",
       "      <td>47</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>767</th>\n",
       "      <td>1</td>\n",
       "      <td>93</td>\n",
       "      <td>70</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "      <td>30.4</td>\n",
       "      <td>0.315</td>\n",
       "      <td>23</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>768 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0              6      148             72             35        0  33.6   \n",
       "1              1       85             66             29        0  26.6   \n",
       "2              8      183             64              0        0  23.3   \n",
       "3              1       89             66             23       94  28.1   \n",
       "4              0      137             40             35      168  43.1   \n",
       "..           ...      ...            ...            ...      ...   ...   \n",
       "763           10      101             76             48      180  32.9   \n",
       "764            2      122             70             27        0  36.8   \n",
       "765            5      121             72             23      112  26.2   \n",
       "766            1      126             60              0        0  30.1   \n",
       "767            1       93             70             31        0  30.4   \n",
       "\n",
       "     DiabetesPedigreeFunction  Age  Outcome  \n",
       "0                       0.627   50        1  \n",
       "1                       0.351   31        0  \n",
       "2                       0.672   32        1  \n",
       "3                       0.167   21        0  \n",
       "4                       2.288   33        1  \n",
       "..                        ...  ...      ...  \n",
       "763                     0.171   63        0  \n",
       "764                     0.340   27        0  \n",
       "765                     0.245   30        0  \n",
       "766                     0.349   47        1  \n",
       "767                     0.315   23        0  \n",
       "\n",
       "[768 rows x 9 columns]"
      ]
     },
     "execution_count": 4,
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
   "execution_count": 5,
   "id": "95c1147f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(768, 9)"
      ]
     },
     "execution_count": 5,
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
   "execution_count": 6,
   "id": "89081bf3",
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
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.845052</td>\n",
       "      <td>120.894531</td>\n",
       "      <td>69.105469</td>\n",
       "      <td>20.536458</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>31.992578</td>\n",
       "      <td>0.471876</td>\n",
       "      <td>33.240885</td>\n",
       "      <td>0.348958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.369578</td>\n",
       "      <td>31.972618</td>\n",
       "      <td>19.355807</td>\n",
       "      <td>15.952218</td>\n",
       "      <td>115.244002</td>\n",
       "      <td>7.884160</td>\n",
       "      <td>0.331329</td>\n",
       "      <td>11.760232</td>\n",
       "      <td>0.476951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.078000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>27.300000</td>\n",
       "      <td>0.243750</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>117.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>30.500000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0.372500</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>140.250000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>127.250000</td>\n",
       "      <td>36.600000</td>\n",
       "      <td>0.626250</td>\n",
       "      <td>41.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>199.000000</td>\n",
       "      <td>122.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>846.000000</td>\n",
       "      <td>67.100000</td>\n",
       "      <td>2.420000</td>\n",
       "      <td>81.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Pregnancies     Glucose  BloodPressure  SkinThickness     Insulin  \\\n",
       "count   768.000000  768.000000     768.000000     768.000000  768.000000   \n",
       "mean      3.845052  120.894531      69.105469      20.536458   79.799479   \n",
       "std       3.369578   31.972618      19.355807      15.952218  115.244002   \n",
       "min       0.000000    0.000000       0.000000       0.000000    0.000000   \n",
       "25%       1.000000   99.000000      62.000000       0.000000    0.000000   \n",
       "50%       3.000000  117.000000      72.000000      23.000000   30.500000   \n",
       "75%       6.000000  140.250000      80.000000      32.000000  127.250000   \n",
       "max      17.000000  199.000000     122.000000      99.000000  846.000000   \n",
       "\n",
       "              BMI  DiabetesPedigreeFunction         Age     Outcome  \n",
       "count  768.000000                768.000000  768.000000  768.000000  \n",
       "mean    31.992578                  0.471876   33.240885    0.348958  \n",
       "std      7.884160                  0.331329   11.760232    0.476951  \n",
       "min      0.000000                  0.078000   21.000000    0.000000  \n",
       "25%     27.300000                  0.243750   24.000000    0.000000  \n",
       "50%     32.000000                  0.372500   29.000000    0.000000  \n",
       "75%     36.600000                  0.626250   41.000000    1.000000  \n",
       "max     67.100000                  2.420000   81.000000    1.000000  "
      ]
     },
     "execution_count": 6,
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
   "execution_count": 7,
   "id": "212a7ded",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 768 entries, 0 to 767\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   Pregnancies               768 non-null    int64  \n",
      " 1   Glucose                   768 non-null    int64  \n",
      " 2   BloodPressure             768 non-null    int64  \n",
      " 3   SkinThickness             768 non-null    int64  \n",
      " 4   Insulin                   768 non-null    int64  \n",
      " 5   BMI                       768 non-null    float64\n",
      " 6   DiabetesPedigreeFunction  768 non-null    float64\n",
      " 7   Age                       768 non-null    int64  \n",
      " 8   Outcome                   768 non-null    int64  \n",
      "dtypes: float64(2), int64(7)\n",
      "memory usage: 54.1 KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a6b8aecc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pregnancies                 0\n",
       "Glucose                     0\n",
       "BloodPressure               0\n",
       "SkinThickness               0\n",
       "Insulin                     0\n",
       "BMI                         0\n",
       "DiabetesPedigreeFunction    0\n",
       "Age                         0\n",
       "Outcome                     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9acd36e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    500\n",
       "1    268\n",
       "Name: Outcome, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Outcome'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1d60d567",
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
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outcome</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.298000</td>\n",
       "      <td>109.980000</td>\n",
       "      <td>68.184000</td>\n",
       "      <td>19.664000</td>\n",
       "      <td>68.792000</td>\n",
       "      <td>30.304200</td>\n",
       "      <td>0.429734</td>\n",
       "      <td>31.190000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.865672</td>\n",
       "      <td>141.257463</td>\n",
       "      <td>70.824627</td>\n",
       "      <td>22.164179</td>\n",
       "      <td>100.335821</td>\n",
       "      <td>35.142537</td>\n",
       "      <td>0.550500</td>\n",
       "      <td>37.067164</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Pregnancies     Glucose  BloodPressure  SkinThickness     Insulin  \\\n",
       "Outcome                                                                      \n",
       "0           3.298000  109.980000      68.184000      19.664000   68.792000   \n",
       "1           4.865672  141.257463      70.824627      22.164179  100.335821   \n",
       "\n",
       "               BMI  DiabetesPedigreeFunction        Age  \n",
       "Outcome                                                  \n",
       "0        30.304200                  0.429734  31.190000  \n",
       "1        35.142537                  0.550500  37.067164  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.groupby('Outcome').mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "83795572",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = data.drop(columns='Outcome',axis=1)\n",
    "\n",
    "y = data['Outcome']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ec60279f",
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
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>148</td>\n",
       "      <td>72</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>66</td>\n",
       "      <td>29</td>\n",
       "      <td>0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183</td>\n",
       "      <td>64</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.672</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89</td>\n",
       "      <td>66</td>\n",
       "      <td>23</td>\n",
       "      <td>94</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.167</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>168</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.288</td>\n",
       "      <td>33</td>\n",
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
       "    </tr>\n",
       "    <tr>\n",
       "      <th>763</th>\n",
       "      <td>10</td>\n",
       "      <td>101</td>\n",
       "      <td>76</td>\n",
       "      <td>48</td>\n",
       "      <td>180</td>\n",
       "      <td>32.9</td>\n",
       "      <td>0.171</td>\n",
       "      <td>63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>764</th>\n",
       "      <td>2</td>\n",
       "      <td>122</td>\n",
       "      <td>70</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>36.8</td>\n",
       "      <td>0.340</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>765</th>\n",
       "      <td>5</td>\n",
       "      <td>121</td>\n",
       "      <td>72</td>\n",
       "      <td>23</td>\n",
       "      <td>112</td>\n",
       "      <td>26.2</td>\n",
       "      <td>0.245</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>766</th>\n",
       "      <td>1</td>\n",
       "      <td>126</td>\n",
       "      <td>60</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>30.1</td>\n",
       "      <td>0.349</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>767</th>\n",
       "      <td>1</td>\n",
       "      <td>93</td>\n",
       "      <td>70</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "      <td>30.4</td>\n",
       "      <td>0.315</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>768 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0              6      148             72             35        0  33.6   \n",
       "1              1       85             66             29        0  26.6   \n",
       "2              8      183             64              0        0  23.3   \n",
       "3              1       89             66             23       94  28.1   \n",
       "4              0      137             40             35      168  43.1   \n",
       "..           ...      ...            ...            ...      ...   ...   \n",
       "763           10      101             76             48      180  32.9   \n",
       "764            2      122             70             27        0  36.8   \n",
       "765            5      121             72             23      112  26.2   \n",
       "766            1      126             60              0        0  30.1   \n",
       "767            1       93             70             31        0  30.4   \n",
       "\n",
       "     DiabetesPedigreeFunction  Age  \n",
       "0                       0.627   50  \n",
       "1                       0.351   31  \n",
       "2                       0.672   32  \n",
       "3                       0.167   21  \n",
       "4                       2.288   33  \n",
       "..                        ...  ...  \n",
       "763                     0.171   63  \n",
       "764                     0.340   27  \n",
       "765                     0.245   30  \n",
       "766                     0.349   47  \n",
       "767                     0.315   23  \n",
       "\n",
       "[768 rows x 8 columns]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "aab78b6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      1\n",
       "1      0\n",
       "2      1\n",
       "3      0\n",
       "4      1\n",
       "      ..\n",
       "763    0\n",
       "764    0\n",
       "765    0\n",
       "766    1\n",
       "767    0\n",
       "Name: Outcome, Length: 768, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "725cd7b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(768, 8)\n"
     ]
    }
   ],
   "source": [
    "print(x.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3d461a4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(768,)\n"
     ]
    }
   ],
   "source": [
    "print(y.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "98e52e7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler = StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "37126403",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = scaler.fit_transform(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "65fa7a37",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.63994726,  0.84832379,  0.14964075, ...,  0.20401277,\n",
       "         0.46849198,  1.4259954 ],\n",
       "       [-0.84488505, -1.12339636, -0.16054575, ..., -0.68442195,\n",
       "        -0.36506078, -0.19067191],\n",
       "       [ 1.23388019,  1.94372388, -0.26394125, ..., -1.10325546,\n",
       "         0.60439732, -0.10558415],\n",
       "       ...,\n",
       "       [ 0.3429808 ,  0.00330087,  0.14964075, ..., -0.73518964,\n",
       "        -0.68519336, -0.27575966],\n",
       "       [-0.84488505,  0.1597866 , -0.47073225, ..., -0.24020459,\n",
       "        -0.37110101,  1.17073215],\n",
       "       [-0.84488505, -0.8730192 ,  0.04624525, ..., -0.20212881,\n",
       "        -0.47378505, -0.87137393]])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "632c3432",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=20,stratify=y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e6504ab4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(768, 8)\n",
      "(614, 8)\n",
      "(154, 8)\n"
     ]
    }
   ],
   "source": [
    "print(x.shape)\n",
    "print(x_train.shape)\n",
    "print(x_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "30981c9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(768,)\n",
      "(614,)\n",
      "(154,)\n"
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
   "cell_type": "code",
   "execution_count": 23,
   "id": "ff2068eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = SVC(kernel='linear')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "27ee1caf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>SVC(kernel=&#x27;linear&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SVC</label><div class=\"sk-toggleable__content\"><pre>SVC(kernel=&#x27;linear&#x27;)</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "SVC(kernel='linear')"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "38428297",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred_train = model.predict(x_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "00955587",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.7736156351791531\n"
     ]
    }
   ],
   "source": [
    "print(accuracy_score(y_pred_train,y_train))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "6d9ae75c",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = model.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "4e7c17ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8051948051948052\n"
     ]
    }
   ],
   "source": [
    "print(accuracy_score(y_pred,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "824e5d46",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Diabetic\n"
     ]
    }
   ],
   "source": [
    "input_data = (6,148,72,35,0,33.6,0.627,50)\n",
    "\n",
    "inputdata = np.asarray(input_data).reshape(1,-1) \n",
    "\n",
    "data = scaler.transform(inputdata)\n",
    "\n",
    "prediction = model.predict(data)\n",
    "\n",
    "if prediction[0]==1:\n",
    "    print(\"Diabetic\")\n",
    "else:\n",
    "    print(\"Non-Diabetic\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4102c251",
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

## File: `diabetesdata.csv`
```
Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
6,148,72,35,0,33.6,0.627,50,1
1,85,66,29,0,26.6,0.351,31,0
8,183,64,0,0,23.3,0.672,32,1
1,89,66,23,94,28.1,0.167,21,0
0,137,40,35,168,43.1,2.288,33,1
5,116,74,0,0,25.6,0.201,30,0
3,78,50,32,88,31,0.248,26,1
10,115,0,0,0,35.3,0.134,29,0
2,197,70,45,543,30.5,0.158,53,1
8,125,96,0,0,0,0.232,54,1
4,110,92,0,0,37.6,0.191,30,0
10,168,74,0,0,38,0.537,34,1
10,139,80,0,0,27.1,1.441,57,0
1,189,60,23,846,30.1,0.398,59,1
5,166,72,19,175,25.8,0.587,51,1
7,100,0,0,0,30,0.484,32,1
0,118,84,47,230,45.8,0.551,31,1
7,107,74,0,0,29.6,0.254,31,1
1,103,30,38,83,43.3,0.183,33,0
1,115,70,30,96,34.6,0.529,32,1
3,126,88,41,235,39.3,0.704,27,0
8,99,84,0,0,35.4,0.388,50,0
7,196,90,0,0,39.8,0.451,41,1
9,119,80,35,0,29,0.263,29,1
11,143,94,33,146,36.6,0.254,51,1
10,125,70,26,115,31.1,0.205,41,1
7,147,76,0,0,39.4,0.257,43,1
1,97,66,15,140,23.2,0.487,22,0
13,145,82,19,110,22.2,0.245,57,0
5,117,92,0,0,34.1,0.337,38,0
5,109,75,26,0,36,0.546,60,0
3,158,76,36,245,31.6,0.851,28,1
3,88,58,11,54,24.8,0.267,22,0
6,92,92,0,0,19.9,0.188,28,0
10,122,78,31,0,27.6,0.512,45,0
4,103,60,33,192,24,0.966,33,0
11,138,76,0,0,33.2,0.42,35,0
9,102,76,37,0,32.9,0.665,46,1
2,90,68,42,0,38.2,0.503,27,1
4,111,72,47,207,37.1,1.39,56,1
3,180,64,25,70,34,0.271,26,0
7,133,84,0,0,40.2,0.696,37,0
7,106,92,18,0,22.7,0.235,48,0
9,171,110,24,240,45.4,0.721,54,1
7,159,64,0,0,27.4,0.294,40,0
0,180,66,39,0,42,1.893,25,1
1,146,56,0,0,29.7,0.564,29,0
2,71,70,27,0,28,0.586,22,0
7,103,66,32,0,39.1,0.344,31,1
7,105,0,0,0,0,0.305,24,0
1,103,80,11,82,19.4,0.491,22,0
1,101,50,15,36,24.2,0.526,26,0
5,88,66,21,23,24.4,0.342,30,0
8,176,90,34,300,33.7,0.467,58,1
7,150,66,42,342,34.7,0.718,42,0
1,73,50,10,0,23,0.248,21,0
7,187,68,39,304,37.7,0.254,41,1
0,100,88,60,110,46.8,0.962,31,0
0,146,82,0,0,40.5,1.781,44,0
0,105,64,41,142,41.5,0.173,22,0
2,84,0,0,0,0,0.304,21,0
8,133,72,0,0,32.9,0.27,39,1
5,44,62,0,0,25,0.587,36,0
2,141,58,34,128,25.4,0.699,24,0
7,114,66,0,0,32.8,0.258,42,1
5,99,74,27,0,29,0.203,32,0
0,109,88,30,0,32.5,0.855,38,1
2,109,92,0,0,42.7,0.845,54,0
1,95,66,13,38,19.6,0.334,25,0
4,146,85,27,100,28.9,0.189,27,0
2,100,66,20,90,32.9,0.867,28,1
5,139,64,35,140,28.6,0.411,26,0
13,126,90,0,0,43.4,0.583,42,1
4,129,86,20,270,35.1,0.231,23,0
1,79,75,30,0,32,0.396,22,0
1,0,48,20,0,24.7,0.14,22,0
7,62,78,0,0,32.6,0.391,41,0
5,95,72,33,0,37.7,0.37,27,0
0,131,0,0,0,43.2,0.27,26,1
2,112,66,22,0,25,0.307,24,0
3,113,44,13,0,22.4,0.14,22,0
2,74,0,0,0,0,0.102,22,0
7,83,78,26,71,29.3,0.767,36,0
0,101,65,28,0,24.6,0.237,22,0
5,137,108,0,0,48.8,0.227,37,1
2,110,74,29,125,32.4,0.698,27,0
13,106,72,54,0,36.6,0.178,45,0
2,100,68,25,71,38.5,0.324,26,0
15,136,70,32,110,37.1,0.153,43,1
1,107,68,19,0,26.5,0.165,24,0
1,80,55,0,0,19.1,0.258,21,0
4,123,80,15,176,32,0.443,34,0
7,81,78,40,48,46.7,0.261,42,0
4,134,72,0,0,23.8,0.277,60,1
2,142,82,18,64,24.7,0.761,21,0
6,144,72,27,228,33.9,0.255,40,0
2,92,62,28,0,31.6,0.13,24,0
1,71,48,18,76,20.4,0.323,22,0
6,93,50,30,64,28.7,0.356,23,0
1,122,90,51,220,49.7,0.325,31,1
1,163,72,0,0,39,1.222,33,1
1,151,60,0,0,26.1,0.179,22,0
0,125,96,0,0,22.5,0.262,21,0
1,81,72,18,40,26.6,0.283,24,0
2,85,65,0,0,39.6,0.93,27,0
1,126,56,29,152,28.7,0.801,21,0
1,96,122,0,0,22.4,0.207,27,0
4,144,58,28,140,29.5,0.287,37,0
3,83,58,31,18,34.3,0.336,25,0
0,95,85,25,36,37.4,0.247,24,1
3,171,72,33,135,33.3,0.199,24,1
8,155,62,26,495,34,0.543,46,1
1,89,76,34,37,31.2,0.192,23,0
4,76,62,0,0,34,0.391,25,0
7,160,54,32,175,30.5,0.588,39,1
4,146,92,0,0,31.2,0.539,61,1
5,124,74,0,0,34,0.22,38,1
5,78,48,0,0,33.7,0.654,25,0
4,97,60,23,0,28.2,0.443,22,0
4,99,76,15,51,23.2,0.223,21,0
0,162,76,56,100,53.2,0.759,25,1
6,111,64,39,0,34.2,0.26,24,0
2,107,74,30,100,33.6,0.404,23,0
5,132,80,0,0,26.8,0.186,69,0
0,113,76,0,0,33.3,0.278,23,1
1,88,30,42,99,55,0.496,26,1
3,120,70,30,135,42.9,0.452,30,0
1,118,58,36,94,33.3,0.261,23,0
1,117,88,24,145,34.5,0.403,40,1
0,105,84,0,0,27.9,0.741,62,1
4,173,70,14,168,29.7,0.361,33,1
9,122,56,0,0,33.3,1.114,33,1
3,170,64,37,225,34.5,0.356,30,1
8,84,74,31,0,38.3,0.457,39,0
2,96,68,13,49,21.1,0.647,26,0
2,125,60,20,140,33.8,0.088,31,0
0,100,70,26,50,30.8,0.597,21,0
0,93,60,25,92,28.7,0.532,22,0
0,129,80,0,0,31.2,0.703,29,0
5,105,72,29,325,36.9,0.159,28,0
3,128,78,0,0,21.1,0.268,55,0
5,106,82,30,0,39.5,0.286,38,0
2,108,52,26,63,32.5,0.318,22,0
10,108,66,0,0,32.4,0.272,42,1
4,154,62,31,284,32.8,0.237,23,0
0,102,75,23,0,0,0.572,21,0
9,57,80,37,0,32.8,0.096,41,0
2,106,64,35,119,30.5,1.4,34,0
5,147,78,0,0,33.7,0.218,65,0
2,90,70,17,0,27.3,0.085,22,0
1,136,74,50,204,37.4,0.399,24,0
4,114,65,0,0,21.9,0.432,37,0
9,156,86,28,155,34.3,1.189,42,1
1,153,82,42,485,40.6,0.687,23,0
8,188,78,0,0,47.9,0.137,43,1
7,152,88,44,0,50,0.337,36,1
2,99,52,15,94,24.6,0.637,21,0
1,109,56,21,135,25.2,0.833,23,0
2,88,74,19,53,29,0.229,22,0
17,163,72,41,114,40.9,0.817,47,1
4,151,90,38,0,29.7,0.294,36,0
7,102,74,40,105,37.2,0.204,45,0
0,114,80,34,285,44.2,0.167,27,0
2,100,64,23,0,29.7,0.368,21,0
0,131,88,0,0,31.6,0.743,32,1
6,104,74,18,156,29.9,0.722,41,1
3,148,66,25,0,32.5,0.256,22,0
4,120,68,0,0,29.6,0.709,34,0
4,110,66,0,0,31.9,0.471,29,0
3,111,90,12,78,28.4,0.495,29,0
6,102,82,0,0,30.8,0.18,36,1
6,134,70,23,130,35.4,0.542,29,1
2,87,0,23,0,28.9,0.773,25,0
1,79,60,42,48,43.5,0.678,23,0
2,75,64,24,55,29.7,0.37,33,0
8,179,72,42,130,32.7,0.719,36,1
6,85,78,0,0,31.2,0.382,42,0
0,129,110,46,130,67.1,0.319,26,1
5,143,78,0,0,45,0.19,47,0
5,130,82,0,0,39.1,0.956,37,1
6,87,80,0,0,23.2,0.084,32,0
0,119,64,18,92,34.9,0.725,23,0
1,0,74,20,23,27.7,0.299,21,0
5,73,60,0,0,26.8,0.268,27,0
4,141,74,0,0,27.6,0.244,40,0
7,194,68,28,0,35.9,0.745,41,1
8,181,68,36,495,30.1,0.615,60,1
1,128,98,41,58,32,1.321,33,1
8,109,76,39,114,27.9,0.64,31,1
5,139,80,35,160,31.6,0.361,25,1
3,111,62,0,0,22.6,0.142,21,0
9,123,70,44,94,33.1,0.374,40,0
7,159,66,0,0,30.4,0.383,36,1
11,135,0,0,0,52.3,0.578,40,1
8,85,55,20,0,24.4,0.136,42,0
5,158,84,41,210,39.4,0.395,29,1
1,105,58,0,0,24.3,0.187,21,0
3,107,62,13,48,22.9,0.678,23,1
4,109,64,44,99,34.8,0.905,26,1
4,148,60,27,318,30.9,0.15,29,1
0,113,80,16,0,31,0.874,21,0
1,138,82,0,0,40.1,0.236,28,0
0,108,68,20,0,27.3,0.787,32,0
2,99,70,16,44,20.4,0.235,27,0
6,103,72,32,190,37.7,0.324,55,0
5,111,72,28,0,23.9,0.407,27,0
8,196,76,29,280,37.5,0.605,57,1
5,162,104,0,0,37.7,0.151,52,1
1,96,64,27,87,33.2,0.289,21,0
7,184,84,33,0,35.5,0.355,41,1
2,81,60,22,0,27.7,0.29,25,0
0,147,85,54,0,42.8,0.375,24,0
7,179,95,31,0,34.2,0.164,60,0
0,140,65,26,130,42.6,0.431,24,1
9,112,82,32,175,34.2,0.26,36,1
12,151,70,40,271,41.8,0.742,38,1
5,109,62,41,129,35.8,0.514,25,1
6,125,68,30,120,30,0.464,32,0
5,85,74,22,0,29,1.224,32,1
5,112,66,0,0,37.8,0.261,41,1
0,177,60,29,478,34.6,1.072,21,1
2,158,90,0,0,31.6,0.805,66,1
7,119,0,0,0,25.2,0.209,37,0
7,142,60,33,190,28.8,0.687,61,0
1,100,66,15,56,23.6,0.666,26,0
1,87,78,27,32,34.6,0.101,22,0
0,101,76,0,0,35.7,0.198,26,0
3,162,52,38,0,37.2,0.652,24,1
4,197,70,39,744,36.7,2.329,31,0
0,117,80,31,53,45.2,0.089,24,0
4,142,86,0,0,44,0.645,22,1
6,134,80,37,370,46.2,0.238,46,1
1,79,80,25,37,25.4,0.583,22,0
4,122,68,0,0,35,0.394,29,0
3,74,68,28,45,29.7,0.293,23,0
4,171,72,0,0,43.6,0.479,26,1
7,181,84,21,192,35.9,0.586,51,1
0,179,90,27,0,44.1,0.686,23,1
9,164,84,21,0,30.8,0.831,32,1
0,104,76,0,0,18.4,0.582,27,0
1,91,64,24,0,29.2,0.192,21,0
4,91,70,32,88,33.1,0.446,22,0
3,139,54,0,0,25.6,0.402,22,1
6,119,50,22,176,27.1,1.318,33,1
2,146,76,35,194,38.2,0.329,29,0
9,184,85,15,0,30,1.213,49,1
10,122,68,0,0,31.2,0.258,41,0
0,165,90,33,680,52.3,0.427,23,0
9,124,70,33,402,35.4,0.282,34,0
1,111,86,19,0,30.1,0.143,23,0
9,106,52,0,0,31.2,0.38,42,0
2,129,84,0,0,28,0.284,27,0
2,90,80,14,55,24.4,0.249,24,0
0,86,68,32,0,35.8,0.238,25,0
12,92,62,7,258,27.6,0.926,44,1
1,113,64,35,0,33.6,0.543,21,1
3,111,56,39,0,30.1,0.557,30,0
2,114,68,22,0,28.7,0.092,25,0
1,193,50,16,375,25.9,0.655,24,0
11,155,76,28,150,33.3,1.353,51,1
3,191,68,15,130,30.9,0.299,34,0
3,141,0,0,0,30,0.761,27,1
4,95,70,32,0,32.1,0.612,24,0
3,142,80,15,0,32.4,0.2,63,0
4,123,62,0,0,32,0.226,35,1
5,96,74,18,67,33.6,0.997,43,0
0,138,0,0,0,36.3,0.933,25,1
2,128,64,42,0,40,1.101,24,0
0,102,52,0,0,25.1,0.078,21,0
2,146,0,0,0,27.5,0.24,28,1
10,101,86,37,0,45.6,1.136,38,1
2,108,62,32,56,25.2,0.128,21,0
3,122,78,0,0,23,0.254,40,0
1,71,78,50,45,33.2,0.422,21,0
13,106,70,0,0,34.2,0.251,52,0
2,100,70,52,57,40.5,0.677,25,0
7,106,60,24,0,26.5,0.296,29,1
0,104,64,23,116,27.8,0.454,23,0
5,114,74,0,0,24.9,0.744,57,0
2,108,62,10,278,25.3,0.881,22,0
0,146,70,0,0,37.9,0.334,28,1
10,129,76,28,122,35.9,0.28,39,0
7,133,88,15,155,32.4,0.262,37,0
7,161,86,0,0,30.4,0.165,47,1
2,108,80,0,0,27,0.259,52,1
7,136,74,26,135,26,0.647,51,0
5,155,84,44,545,38.7,0.619,34,0
1,119,86,39,220,45.6,0.808,29,1
4,96,56,17,49,20.8,0.34,26,0
5,108,72,43,75,36.1,0.263,33,0
0,78,88,29,40,36.9,0.434,21,0
0,107,62,30,74,36.6,0.757,25,1
2,128,78,37,182,43.3,1.224,31,1
1,128,48,45,194,40.5,0.613,24,1
0,161,50,0,0,21.9,0.254,65,0
6,151,62,31,120,35.5,0.692,28,0
2,146,70,38,360,28,0.337,29,1
0,126,84,29,215,30.7,0.52,24,0
14,100,78,25,184,36.6,0.412,46,1
8,112,72,0,0,23.6,0.84,58,0
0,167,0,0,0,32.3,0.839,30,1
2,144,58,33,135,31.6,0.422,25,1
5,77,82,41,42,35.8,0.156,35,0
5,115,98,0,0,52.9,0.209,28,1
3,150,76,0,0,21,0.207,37,0
2,120,76,37,105,39.7,0.215,29,0
10,161,68,23,132,25.5,0.326,47,1
0,137,68,14,148,24.8,0.143,21,0
0,128,68,19,180,30.5,1.391,25,1
2,124,68,28,205,32.9,0.875,30,1
6,80,66,30,0,26.2,0.313,41,0
0,106,70,37,148,39.4,0.605,22,0
2,155,74,17,96,26.6,0.433,27,1
3,113,50,10,85,29.5,0.626,25,0
7,109,80,31,0,35.9,1.127,43,1
2,112,68,22,94,34.1,0.315,26,0
3,99,80,11,64,19.3,0.284,30,0
3,182,74,0,0,30.5,0.345,29,1
3,115,66,39,140,38.1,0.15,28,0
6,194,78,0,0,23.5,0.129,59,1
4,129,60,12,231,27.5,0.527,31,0
3,112,74,30,0,31.6,0.197,25,1
0,124,70,20,0,27.4,0.254,36,1
13,152,90,33,29,26.8,0.731,43,1
2,112,75,32,0,35.7,0.148,21,0
1,157,72,21,168,25.6,0.123,24,0
1,122,64,32,156,35.1,0.692,30,1
10,179,70,0,0,35.1,0.2,37,0
2,102,86,36,120,45.5,0.127,23,1
6,105,70,32,68,30.8,0.122,37,0
8,118,72,19,0,23.1,1.476,46,0
2,87,58,16,52,32.7,0.166,25,0
1,180,0,0,0,43.3,0.282,41,1
12,106,80,0,0,23.6,0.137,44,0
1,95,60,18,58,23.9,0.26,22,0
0,165,76,43,255,47.9,0.259,26,0
0,117,0,0,0,33.8,0.932,44,0
5,115,76,0,0,31.2,0.343,44,1
9,152,78,34,171,34.2,0.893,33,1
7,178,84,0,0,39.9,0.331,41,1
1,130,70,13,105,25.9,0.472,22,0
1,95,74,21,73,25.9,0.673,36,0
1,0,68,35,0,32,0.389,22,0
5,122,86,0,0,34.7,0.29,33,0
8,95,72,0,0,36.8,0.485,57,0
8,126,88,36,108,38.5,0.349,49,0
1,139,46,19,83,28.7,0.654,22,0
3,116,0,0,0,23.5,0.187,23,0
3,99,62,19,74,21.8,0.279,26,0
5,0,80,32,0,41,0.346,37,1
4,92,80,0,0,42.2,0.237,29,0
4,137,84,0,0,31.2,0.252,30,0
3,61,82,28,0,34.4,0.243,46,0
1,90,62,12,43,27.2,0.58,24,0
3,90,78,0,0,42.7,0.559,21,0
9,165,88,0,0,30.4,0.302,49,1
1,125,50,40,167,33.3,0.962,28,1
13,129,0,30,0,39.9,0.569,44,1
12,88,74,40,54,35.3,0.378,48,0
1,196,76,36,249,36.5,0.875,29,1
5,189,64,33,325,31.2,0.583,29,1
5,158,70,0,0,29.8,0.207,63,0
5,103,108,37,0,39.2,0.305,65,0
4,146,78,0,0,38.5,0.52,67,1
4,147,74,25,293,34.9,0.385,30,0
5,99,54,28,83,34,0.499,30,0
6,124,72,0,0,27.6,0.368,29,1
0,101,64,17,0,21,0.252,21,0
3,81,86,16,66,27.5,0.306,22,0
1,133,102,28,140,32.8,0.234,45,1
3,173,82,48,465,38.4,2.137,25,1
0,118,64,23,89,0,1.731,21,0
0,84,64,22,66,35.8,0.545,21,0
2,105,58,40,94,34.9,0.225,25,0
2,122,52,43,158,36.2,0.816,28,0
12,140,82,43,325,39.2,0.528,58,1
0,98,82,15,84,25.2,0.299,22,0
1,87,60,37,75,37.2,0.509,22,0
4,156,75,0,0,48.3,0.238,32,1
0,93,100,39,72,43.4,1.021,35,0
1,107,72,30,82,30.8,0.821,24,0
0,105,68,22,0,20,0.236,22,0
1,109,60,8,182,25.4,0.947,21,0
1,90,62,18,59,25.1,1.268,25,0
1,125,70,24,110,24.3,0.221,25,0
1,119,54,13,50,22.3,0.205,24,0
5,116,74,29,0,32.3,0.66,35,1
8,105,100,36,0,43.3,0.239,45,1
5,144,82,26,285,32,0.452,58,1
3,100,68,23,81,31.6,0.949,28,0
1,100,66,29,196,32,0.444,42,0
5,166,76,0,0,45.7,0.34,27,1
1,131,64,14,415,23.7,0.389,21,0
4,116,72,12,87,22.1,0.463,37,0
4,158,78,0,0,32.9,0.803,31,1
2,127,58,24,275,27.7,1.6,25,0
3,96,56,34,115,24.7,0.944,39,0
0,131,66,40,0,34.3,0.196,22,1
3,82,70,0,0,21.1,0.389,25,0
3,193,70,31,0,34.9,0.241,25,1
4,95,64,0,0,32,0.161,31,1
6,137,61,0,0,24.2,0.151,55,0
5,136,84,41,88,35,0.286,35,1
9,72,78,25,0,31.6,0.28,38,0
5,168,64,0,0,32.9,0.135,41,1
2,123,48,32,165,42.1,0.52,26,0
4,115,72,0,0,28.9,0.376,46,1
0,101,62,0,0,21.9,0.336,25,0
8,197,74,0,0,25.9,1.191,39,1
1,172,68,49,579,42.4,0.702,28,1
6,102,90,39,0,35.7,0.674,28,0
1,112,72,30,176,34.4,0.528,25,0
1,143,84,23,310,42.4,1.076,22,0
1,143,74,22,61,26.2,0.256,21,0
0,138,60,35,167,34.6,0.534,21,1
3,173,84,33,474,35.7,0.258,22,1
1,97,68,21,0,27.2,1.095,22,0
4,144,82,32,0,38.5,0.554,37,1
1,83,68,0,0,18.2,0.624,27,0
3,129,64,29,115,26.4,0.219,28,1
1,119,88,41,170,45.3,0.507,26,0
2,94,68,18,76,26,0.561,21,0
0,102,64,46,78,40.6,0.496,21,0
2,115,64,22,0,30.8,0.421,21,0
8,151,78,32,210,42.9,0.516,36,1
4,184,78,39,277,37,0.264,31,1
0,94,0,0,0,0,0.256,25,0
1,181,64,30,180,34.1,0.328,38,1
0,135,94,46,145,40.6,0.284,26,0
1,95,82,25,180,35,0.233,43,1
2,99,0,0,0,22.2,0.108,23,0
3,89,74,16,85,30.4,0.551,38,0
1,80,74,11,60,30,0.527,22,0
2,139,75,0,0,25.6,0.167,29,0
1,90,68,8,0,24.5,1.138,36,0
0,141,0,0,0,42.4,0.205,29,1
12,140,85,33,0,37.4,0.244,41,0
5,147,75,0,0,29.9,0.434,28,0
1,97,70,15,0,18.2,0.147,21,0
6,107,88,0,0,36.8,0.727,31,0
0,189,104,25,0,34.3,0.435,41,1
2,83,66,23,50,32.2,0.497,22,0
4,117,64,27,120,33.2,0.23,24,0
8,108,70,0,0,30.5,0.955,33,1
4,117,62,12,0,29.7,0.38,30,1
0,180,78,63,14,59.4,2.42,25,1
1,100,72,12,70,25.3,0.658,28,0
0,95,80,45,92,36.5,0.33,26,0
0,104,64,37,64,33.6,0.51,22,1
0,120,74,18,63,30.5,0.285,26,0
1,82,64,13,95,21.2,0.415,23,0
2,134,70,0,0,28.9,0.542,23,1
0,91,68,32,210,39.9,0.381,25,0
2,119,0,0,0,19.6,0.832,72,0
2,100,54,28,105,37.8,0.498,24,0
14,175,62,30,0,33.6,0.212,38,1
1,135,54,0,0,26.7,0.687,62,0
5,86,68,28,71,30.2,0.364,24,0
10,148,84,48,237,37.6,1.001,51,1
9,134,74,33,60,25.9,0.46,81,0
9,120,72,22,56,20.8,0.733,48,0
1,71,62,0,0,21.8,0.416,26,0
8,74,70,40,49,35.3,0.705,39,0
5,88,78,30,0,27.6,0.258,37,0
10,115,98,0,0,24,1.022,34,0
0,124,56,13,105,21.8,0.452,21,0
0,74,52,10,36,27.8,0.269,22,0
0,97,64,36,100,36.8,0.6,25,0
8,120,0,0,0,30,0.183,38,1
6,154,78,41,140,46.1,0.571,27,0
1,144,82,40,0,41.3,0.607,28,0
0,137,70,38,0,33.2,0.17,22,0
0,119,66,27,0,38.8,0.259,22,0
7,136,90,0,0,29.9,0.21,50,0
4,114,64,0,0,28.9,0.126,24,0
0,137,84,27,0,27.3,0.231,59,0
2,105,80,45,191,33.7,0.711,29,1
7,114,76,17,110,23.8,0.466,31,0
8,126,74,38,75,25.9,0.162,39,0
4,132,86,31,0,28,0.419,63,0
3,158,70,30,328,35.5,0.344,35,1
0,123,88,37,0,35.2,0.197,29,0
4,85,58,22,49,27.8,0.306,28,0
0,84,82,31,125,38.2,0.233,23,0
0,145,0,0,0,44.2,0.63,31,1
0,135,68,42,250,42.3,0.365,24,1
1,139,62,41,480,40.7,0.536,21,0
0,173,78,32,265,46.5,1.159,58,0
4,99,72,17,0,25.6,0.294,28,0
8,194,80,0,0,26.1,0.551,67,0
2,83,65,28,66,36.8,0.629,24,0
2,89,90,30,0,33.5,0.292,42,0
4,99,68,38,0,32.8,0.145,33,0
4,125,70,18,122,28.9,1.144,45,1
3,80,0,0,0,0,0.174,22,0
6,166,74,0,0,26.6,0.304,66,0
5,110,68,0,0,26,0.292,30,0
2,81,72,15,76,30.1,0.547,25,0
7,195,70,33,145,25.1,0.163,55,1
6,154,74,32,193,29.3,0.839,39,0
2,117,90,19,71,25.2,0.313,21,0
3,84,72,32,0,37.2,0.267,28,0
6,0,68,41,0,39,0.727,41,1
7,94,64,25,79,33.3,0.738,41,0
3,96,78,39,0,37.3,0.238,40,0
10,75,82,0,0,33.3,0.263,38,0
0,180,90,26,90,36.5,0.314,35,1
1,130,60,23,170,28.6,0.692,21,0
2,84,50,23,76,30.4,0.968,21,0
8,120,78,0,0,25,0.409,64,0
12,84,72,31,0,29.7,0.297,46,1
0,139,62,17,210,22.1,0.207,21,0
9,91,68,0,0,24.2,0.2,58,0
2,91,62,0,0,27.3,0.525,22,0
3,99,54,19,86,25.6,0.154,24,0
3,163,70,18,105,31.6,0.268,28,1
9,145,88,34,165,30.3,0.771,53,1
7,125,86,0,0,37.6,0.304,51,0
13,76,60,0,0,32.8,0.18,41,0
6,129,90,7,326,19.6,0.582,60,0
2,68,70,32,66,25,0.187,25,0
3,124,80,33,130,33.2,0.305,26,0
6,114,0,0,0,0,0.189,26,0
9,130,70,0,0,34.2,0.652,45,1
3,125,58,0,0,31.6,0.151,24,0
3,87,60,18,0,21.8,0.444,21,0
1,97,64,19,82,18.2,0.299,21,0
3,116,74,15,105,26.3,0.107,24,0
0,117,66,31,188,30.8,0.493,22,0
0,111,65,0,0,24.6,0.66,31,0
2,122,60,18,106,29.8,0.717,22,0
0,107,76,0,0,45.3,0.686,24,0
1,86,66,52,65,41.3,0.917,29,0
6,91,0,0,0,29.8,0.501,31,0
1,77,56,30,56,33.3,1.251,24,0
4,132,0,0,0,32.9,0.302,23,1
0,105,90,0,0,29.6,0.197,46,0
0,57,60,0,0,21.7,0.735,67,0
0,127,80,37,210,36.3,0.804,23,0
3,129,92,49,155,36.4,0.968,32,1
8,100,74,40,215,39.4,0.661,43,1
3,128,72,25,190,32.4,0.549,27,1
10,90,85,32,0,34.9,0.825,56,1
4,84,90,23,56,39.5,0.159,25,0
1,88,78,29,76,32,0.365,29,0
8,186,90,35,225,34.5,0.423,37,1
5,187,76,27,207,43.6,1.034,53,1
4,131,68,21,166,33.1,0.16,28,0
1,164,82,43,67,32.8,0.341,50,0
4,189,110,31,0,28.5,0.68,37,0
1,116,70,28,0,27.4,0.204,21,0
3,84,68,30,106,31.9,0.591,25,0
6,114,88,0,0,27.8,0.247,66,0
1,88,62,24,44,29.9,0.422,23,0
1,84,64,23,115,36.9,0.471,28,0
7,124,70,33,215,25.5,0.161,37,0
1,97,70,40,0,38.1,0.218,30,0
8,110,76,0,0,27.8,0.237,58,0
11,103,68,40,0,46.2,0.126,42,0
11,85,74,0,0,30.1,0.3,35,0
6,125,76,0,0,33.8,0.121,54,1
0,198,66,32,274,41.3,0.502,28,1
1,87,68,34,77,37.6,0.401,24,0
6,99,60,19,54,26.9,0.497,32,0
0,91,80,0,0,32.4,0.601,27,0
2,95,54,14,88,26.1,0.748,22,0
1,99,72,30,18,38.6,0.412,21,0
6,92,62,32,126,32,0.085,46,0
4,154,72,29,126,31.3,0.338,37,0
0,121,66,30,165,34.3,0.203,33,1
3,78,70,0,0,32.5,0.27,39,0
2,130,96,0,0,22.6,0.268,21,0
3,111,58,31,44,29.5,0.43,22,0
2,98,60,17,120,34.7,0.198,22,0
1,143,86,30,330,30.1,0.892,23,0
1,119,44,47,63,35.5,0.28,25,0
6,108,44,20,130,24,0.813,35,0
2,118,80,0,0,42.9,0.693,21,1
10,133,68,0,0,27,0.245,36,0
2,197,70,99,0,34.7,0.575,62,1
0,151,90,46,0,42.1,0.371,21,1
6,109,60,27,0,25,0.206,27,0
12,121,78,17,0,26.5,0.259,62,0
8,100,76,0,0,38.7,0.19,42,0
8,124,76,24,600,28.7,0.687,52,1
1,93,56,11,0,22.5,0.417,22,0
8,143,66,0,0,34.9,0.129,41,1
6,103,66,0,0,24.3,0.249,29,0
3,176,86,27,156,33.3,1.154,52,1
0,73,0,0,0,21.1,0.342,25,0
11,111,84,40,0,46.8,0.925,45,1
2,112,78,50,140,39.4,0.175,24,0
3,132,80,0,0,34.4,0.402,44,1
2,82,52,22,115,28.5,1.699,25,0
6,123,72,45,230,33.6,0.733,34,0
0,188,82,14,185,32,0.682,22,1
0,67,76,0,0,45.3,0.194,46,0
1,89,24,19,25,27.8,0.559,21,0
1,173,74,0,0,36.8,0.088,38,1
1,109,38,18,120,23.1,0.407,26,0
1,108,88,19,0,27.1,0.4,24,0
6,96,0,0,0,23.7,0.19,28,0
1,124,74,36,0,27.8,0.1,30,0
7,150,78,29,126,35.2,0.692,54,1
4,183,0,0,0,28.4,0.212,36,1
1,124,60,32,0,35.8,0.514,21,0
1,181,78,42,293,40,1.258,22,1
1,92,62,25,41,19.5,0.482,25,0
0,152,82,39,272,41.5,0.27,27,0
1,111,62,13,182,24,0.138,23,0
3,106,54,21,158,30.9,0.292,24,0
3,174,58,22,194,32.9,0.593,36,1
7,168,88,42,321,38.2,0.787,40,1
6,105,80,28,0,32.5,0.878,26,0
11,138,74,26,144,36.1,0.557,50,1
3,106,72,0,0,25.8,0.207,27,0
6,117,96,0,0,28.7,0.157,30,0
2,68,62,13,15,20.1,0.257,23,0
9,112,82,24,0,28.2,1.282,50,1
0,119,0,0,0,32.4,0.141,24,1
2,112,86,42,160,38.4,0.246,28,0
2,92,76,20,0,24.2,1.698,28,0
6,183,94,0,0,40.8,1.461,45,0
0,94,70,27,115,43.5,0.347,21,0
2,108,64,0,0,30.8,0.158,21,0
4,90,88,47,54,37.7,0.362,29,0
0,125,68,0,0,24.7,0.206,21,0
0,132,78,0,0,32.4,0.393,21,0
5,128,80,0,0,34.6,0.144,45,0
4,94,65,22,0,24.7,0.148,21,0
7,114,64,0,0,27.4,0.732,34,1
0,102,78,40,90,34.5,0.238,24,0
2,111,60,0,0,26.2,0.343,23,0
1,128,82,17,183,27.5,0.115,22,0
10,92,62,0,0,25.9,0.167,31,0
13,104,72,0,0,31.2,0.465,38,1
5,104,74,0,0,28.8,0.153,48,0
2,94,76,18,66,31.6,0.649,23,0
7,97,76,32,91,40.9,0.871,32,1
1,100,74,12,46,19.5,0.149,28,0
0,102,86,17,105,29.3,0.695,27,0
4,128,70,0,0,34.3,0.303,24,0
6,147,80,0,0,29.5,0.178,50,1
4,90,0,0,0,28,0.61,31,0
3,103,72,30,152,27.6,0.73,27,0
2,157,74,35,440,39.4,0.134,30,0
1,167,74,17,144,23.4,0.447,33,1
0,179,50,36,159,37.8,0.455,22,1
11,136,84,35,130,28.3,0.26,42,1
0,107,60,25,0,26.4,0.133,23,0
1,91,54,25,100,25.2,0.234,23,0
1,117,60,23,106,33.8,0.466,27,0
5,123,74,40,77,34.1,0.269,28,0
2,120,54,0,0,26.8,0.455,27,0
1,106,70,28,135,34.2,0.142,22,0
2,155,52,27,540,38.7,0.24,25,1
2,101,58,35,90,21.8,0.155,22,0
1,120,80,48,200,38.9,1.162,41,0
11,127,106,0,0,39,0.19,51,0
3,80,82,31,70,34.2,1.292,27,1
10,162,84,0,0,27.7,0.182,54,0
1,199,76,43,0,42.9,1.394,22,1
8,167,106,46,231,37.6,0.165,43,1
9,145,80,46,130,37.9,0.637,40,1
6,115,60,39,0,33.7,0.245,40,1
1,112,80,45,132,34.8,0.217,24,0
4,145,82,18,0,32.5,0.235,70,1
10,111,70,27,0,27.5,0.141,40,1
6,98,58,33,190,34,0.43,43,0
9,154,78,30,100,30.9,0.164,45,0
6,165,68,26,168,33.6,0.631,49,0
1,99,58,10,0,25.4,0.551,21,0
10,68,106,23,49,35.5,0.285,47,0
3,123,100,35,240,57.3,0.88,22,0
8,91,82,0,0,35.6,0.587,68,0
6,195,70,0,0,30.9,0.328,31,1
9,156,86,0,0,24.8,0.23,53,1
0,93,60,0,0,35.3,0.263,25,0
3,121,52,0,0,36,0.127,25,1
2,101,58,17,265,24.2,0.614,23,0
2,56,56,28,45,24.2,0.332,22,0
0,162,76,36,0,49.6,0.364,26,1
0,95,64,39,105,44.6,0.366,22,0
4,125,80,0,0,32.3,0.536,27,1
5,136,82,0,0,0,0.64,69,0
2,129,74,26,205,33.2,0.591,25,0
3,130,64,0,0,23.1,0.314,22,0
1,107,50,19,0,28.3,0.181,29,0
1,140,74,26,180,24.1,0.828,23,0
1,144,82,46,180,46.1,0.335,46,1
8,107,80,0,0,24.6,0.856,34,0
13,158,114,0,0,42.3,0.257,44,1
2,121,70,32,95,39.1,0.886,23,0
7,129,68,49,125,38.5,0.439,43,1
2,90,60,0,0,23.5,0.191,25,0
7,142,90,24,480,30.4,0.128,43,1
3,169,74,19,125,29.9,0.268,31,1
0,99,0,0,0,25,0.253,22,0
4,127,88,11,155,34.5,0.598,28,0
4,118,70,0,0,44.5,0.904,26,0
2,122,76,27,200,35.9,0.483,26,0
6,125,78,31,0,27.6,0.565,49,1
1,168,88,29,0,35,0.905,52,1
2,129,0,0,0,38.5,0.304,41,0
4,110,76,20,100,28.4,0.118,27,0
6,80,80,36,0,39.8,0.177,28,0
10,115,0,0,0,0,0.261,30,1
2,127,46,21,335,34.4,0.176,22,0
9,164,78,0,0,32.8,0.148,45,1
2,93,64,32,160,38,0.674,23,1
3,158,64,13,387,31.2,0.295,24,0
5,126,78,27,22,29.6,0.439,40,0
10,129,62,36,0,41.2,0.441,38,1
0,134,58,20,291,26.4,0.352,21,0
3,102,74,0,0,29.5,0.121,32,0
7,187,50,33,392,33.9,0.826,34,1
3,173,78,39,185,33.8,0.97,31,1
10,94,72,18,0,23.1,0.595,56,0
1,108,60,46,178,35.5,0.415,24,0
5,97,76,27,0,35.6,0.378,52,1
4,83,86,19,0,29.3,0.317,34,0
1,114,66,36,200,38.1,0.289,21,0
1,149,68,29,127,29.3,0.349,42,1
5,117,86,30,105,39.1,0.251,42,0
1,111,94,0,0,32.8,0.265,45,0
4,112,78,40,0,39.4,0.236,38,0
1,116,78,29,180,36.1,0.496,25,0
0,141,84,26,0,32.4,0.433,22,0
2,175,88,0,0,22.9,0.326,22,0
2,92,52,0,0,30.1,0.141,22,0
3,130,78,23,79,28.4,0.323,34,1
8,120,86,0,0,28.4,0.259,22,1
2,174,88,37,120,44.5,0.646,24,1
2,106,56,27,165,29,0.426,22,0
2,105,75,0,0,23.3,0.56,53,0
4,95,60,32,0,35.4,0.284,28,0
0,126,86,27,120,27.4,0.515,21,0
8,65,72,23,0,32,0.6,42,0
2,99,60,17,160,36.6,0.453,21,0
1,102,74,0,0,39.5,0.293,42,1
11,120,80,37,150,42.3,0.785,48,1
3,102,44,20,94,30.8,0.4,26,0
1,109,58,18,116,28.5,0.219,22,0
9,140,94,0,0,32.7,0.734,45,1
13,153,88,37,140,40.6,1.174,39,0
12,100,84,33,105,30,0.488,46,0
1,147,94,41,0,49.3,0.358,27,1
1,81,74,41,57,46.3,1.096,32,0
3,187,70,22,200,36.4,0.408,36,1
6,162,62,0,0,24.3,0.178,50,1
4,136,70,0,0,31.2,1.182,22,1
1,121,78,39,74,39,0.261,28,0
3,108,62,24,0,26,0.223,25,0
0,181,88,44,510,43.3,0.222,26,1
8,154,78,32,0,32.4,0.443,45,1
1,128,88,39,110,36.5,1.057,37,1
7,137,90,41,0,32,0.391,39,0
0,123,72,0,0,36.3,0.258,52,1
1,106,76,0,0,37.5,0.197,26,0
6,190,92,0,0,35.5,0.278,66,1
2,88,58,26,16,28.4,0.766,22,0
9,170,74,31,0,44,0.403,43,1
9,89,62,0,0,22.5,0.142,33,0
10,101,76,48,180,32.9,0.171,63,0
2,122,70,27,0,36.8,0.34,27,0
5,121,72,23,112,26.2,0.245,30,0
1,126,60,0,0,30.1,0.349,47,1
1,93,70,31,0,30.4,0.315,23,0
```

## File: `LICENSE`
```
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
```

## File: `README.md`
```markdown
# Diabetes-Prediction-using-Machine-Learning
```

