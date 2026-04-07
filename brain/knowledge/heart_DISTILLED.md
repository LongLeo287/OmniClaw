---
id: heart
type: knowledge
owner: OA_Triage
---
# heart
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Heart Disease Prediction

- LinkedIn [Hema Kalyan Murapaka](https://www.linkedin.com/in/hemakalyan)
- Medium [KalyanMurapaka274](https://medium.com/@kalyanmurapaka274)


## About The Project


Heart disease prediction is a crucial aspect of preventive healthcare that involves the comprehensive analysis of diverse data points to evaluate an individual's susceptibility to cardiovascular diseases. This process integrates demographic details like age and gender with critical clinical information, including medical and family histories, lifestyle choices, and existing health conditions such as hypertension or diabetes. By examining biomarkers like blood pressure, cholesterol levels, and blood sugar, alongside results from medical tests and imaging studies, predictive models can identify patterns and trends indicative of potential heart issues. Machine learning algorithms play a pivotal role in processing this information, helping stratify individuals into risk categories. The ultimate goal is to enable timely interventions and personalized preventive strategies, empowering individuals to make lifestyle adjustments that can mitigate the risk of heart-related events like heart attacks or strokes. Continuous monitoring and updating of predictive models ensure ongoing accuracy and effectiveness in supporting proactive heart health management.

## About the Dataset

This dataset gives information related to heart disease. The dataset contains 13 columns, target is the class variable which is affected by the other 12 columns. Here the aim is to classify the target variable to (disease\non disease) using different machine learning algorithms and find out which algorithm is suitable for this dataset.
<br><be>

<h3>Attributes:</h3> 

 - Age 
 - Gender 
 - Chest Pain Type
 - Resting Blood Pressure
 - Serum Cholesterol 
 - Fasting Blood Sugar 
 - Resting Electrocardiographic Results
 - Maximum Heart Rate Achieved
 - Exercise-induced angina
 - Depression induced by exercise relative to rest
 - Slope of the Peak Exercise ST Segment
 - Number of Major Vessels Colored by Fluoroscopy
 - Thalassemia
 - Target 

## Built With

 - Pandas
 - Numpy
 - Scikit-Learn
 - Seaborn
 - Matplotlib
 - Flask
 - DVC (Data Version Control)
 - MLFlow
 - Catboost
 - XG Boost

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
     git clone https://github.com/KalyanMurapaka45/Heart-Disease-Prediction.git
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
  
<br><br>
### Option 2: Installation from DockerHub

If you prefer to use Docker, you can install and run the project using a Docker container from DockerHub:

1. **Pull the Docker Image**
   - Open your terminal or command prompt.
   - Run the following command to pull the Docker image from DockerHub:
     ```
     docker pull kalyan45/heart-app
     ```

2. **Run the Docker Container**
   - Start the Docker container by running the following command, and mapping any necessary ports:
     ```
     docker run -p 5000:5000 kalyan45/heart-app
     ```

3. **Access the Project**
   - Open a web browser or the appropriate client to access the project.

## Setup

### MLflow Tracking

We use MLflow to log and track our machine learning experiments. The MLFLOW_TRACKING_URI environment variable is set to the DagsHub repository's MLflow tracking URI.

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/HemaKalyan45/Heart-Disease-Prediction.mlflow

export MLFLOW_TRACKING_USERNAME=HemaKalyan45

export MLFLOW_TRACKING_PASSWORD=f3c9457eb0ff83244e93ac8ee651b80d4b35f07c
```

## Contributing

Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact

Hema Kalyan Murapaka - [@kalyanmurapaka274@gmail.com](kalyanmurapaka274@gmail.com)


## Acknowledgements

We'd like to extend our gratitude to all individuals and organizations who have played a role in the development and success of this project. Your support, whether through contributions, inspiration, or encouragement, has been invaluable. Thank you for being a part of our journey.

```

### File: requirements.txt
```txt
pandas
numpy
scikit-learn
seaborn
ipykernel
matplotlib
flask 
dvc
catboost
xgboost
mlflow==2.2.2

-e .
```

### File: setup.py
```py
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="HeartDiseasePrediction",
    version="0.0.1",
    author="Hema_Kalyan",
    author_email="kalyanmurapaka274@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)
```

### File: app.py
```py
from flask import Flask, request, render_template
from src.Heart.pipeline.Prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

# Define the home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Validate and convert form data to CustomData object
            data = CustomData(
                age=request.form.get("age"),
                sex=request.form.get("sex"),
                cp=(request.form.get("cp")),
                trestbps=(request.form.get("trestbps")),
                chol=(request.form.get("chol")),
                fbs=request.form.get("fbs"),
                restecg=request.form.get("restecg"),
                thalach=(request.form.get("thalach")),
                exang=request.form.get("exang"),
                oldpeak=request.form.get("oldpeak"),
                slope=request.form.get("slope"),
                ca=request.form.get("ca"),
                thal=(request.form.get("thal"))
            )

            final_data = data.get_data_as_dataframe()
            # Make prediction
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_data)
            result = round(pred[0], 2)
            return render_template("result.html", final_result=result)

        except Exception as e:
            # Handle exceptions gracefully
            error_message = f"Error during prediction: {str(e)}"
            return render_template("error.html", error_message=error_message)

    else:
        # Render the initial page
        return render_template("index.html")

# Execution begins
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

```

### File: dvc.yaml
```yaml
stages:
  training:
    cmd: python src/Heart/pipeline/Training_pipeline.py
    deps:
      - src/Heart/pipeline/training_pipeline.py
      - src/Heart/components/Data_ingestion.py
      - src/Heart/components/Data_transformation.py
      - src/Heart/components/Model_trainer.py
      - src/Heart/components/Model_evaluation.py

    outs:
      - Artifacts/raw_data.csv
      - Artifacts/test_data.csv
      - Artifacts/train_data.csv
      - Artifacts/Preprocessor.pkl
      - Artifacts/Model.pkl
```

### File: template.py
```py
import os
from pathlib import Path

package="Heart" 

list_of_files = [
    ".github/workflows/main.yaml",
    "Notebook_Experiments/Data/.gitkeep",
    "Notebook_Experiments/Exploratory_Data_Analysis.ipynb",
    "Notebook_Experiments/Model_Training.ipynb",
    f"src/{package}/__init__.py",
    f"src/{package}/exception.py",
    f"src/{package}/logger.py",
    f"src/{package}/utils/__init__.py",
    f"src/{package}/utils/utils.py",
    f"src/{package}/components/__init__.py",
    f"src/{package}/components/Data_ingestion.py",
    f"src/{package}/components/Data_transformation.py",
    f"src/{package}/components/Model_trainer.py",
    f"src/{package}/components/Model_evaluation.py",
    f"src/{package}/pipeline/__init__.py",
    f"src/{package}/pipeline/Prediction_pipeline.py",
    f"src/{package}/pipeline/Training_pipeline.py",
    "static/styles.css",
    "templates/index.html",
    "templates/result.html",
    ".gitignore",
    "app.py",
    "Dockerfile",
    "README.md",
    ".dvcignore",
    "dvc.yaml",
    "requirements.txt",
    "setup.py"]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
```

### File: static\styles.css
```css
/* static/styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0; /* Light gray background */
    margin: 0;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

.container {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 80%; /* Set a wider width for desktop */
    max-width: 600px; /* Limit maximum width for larger screens */
}

form {
    display: flex;
    flex-direction: column;
    margin-top: 30px; /* Add margin to the top of the form */
}

label {
    margin-bottom: 8px;
    color: #333; /* Dark gray text color */
}

input,
select {
    width: 100%;
    padding: 10px;
    margin-bottom: 16px;
    box-sizing: border-box;
    border: 1px solid #ccc; /* Light gray border */
    border-radius: 4px;
}

button {
    background-color: #4caf50;
    color: #fff;
    padding: 12px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

.result {
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #ddd; /* Light border around the result */
    border-radius: 4px;
    background-color: #f9f9f9; /* Slightly off-white background */
    color: #333; /* Dark gray text color */
}

```

### File: templates\error.html
```html

```

### File: templates\index.html
```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heart Disease Prediction</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container"><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <h1><center>Heart Disease Prediction</center></h1>
        <form method="post">
            <label for="age">Age:</label>
            <input type="text" name="age" required>

            <label for="sex">Sex:</label>
            <select name="sex" required>
                <option value="0">Female</option>
                <option value="1">Male</option>
            </select>

            <label for="cp">Chest Pain Type:</label>
            <select name="cp" required>
                <option value="0">Typical Angina</option>
                <option value="1">Atypical Angina</option>
                <option value="2">Non-Anginal Pain</option>
                <option value="3">Asymptomatic</option>
            </select>

            <label for="trestbps">Resting Blood Pressure (mm Hg):</label>
            <input type="text" name="trestbps" required>

            <label for="chol">Serum Cholesterol (mg/dl):</label>
            <input type="text" name="chol" required>

            <label for="fbs">Fasting Blood Sugar > 120 mg/dl:</label>
            <select name="fbs" required>
                <option value="0">No</option>
                <option value="1">Yes</option>
            </select>

            <label for="restecg">Resting Electrocardiographic Results:</label>
            <select name="restecg" required>
                <option value="0">Normal</option>
                <option value="1">ST-T Wave Abnormality</option>
                <option value="2">Left Ventricular Hypertrophy</option>
            </select>

            <label for="thalach">Maximum Heart Rate Achieved:</label>
            <input type="text" name="thalach" required>

            <label for="exang">Exercise Induced Angina:</label>
            <select name="exang" required>
                <option value="0">No</option>
                <option value="1">Yes</option>
            </select>

            <label for="oldpeak">Oldpeak:</label>
            <input type="text" name="oldpeak" required>

            <label for="slope">Slope of the Peak Exercise ST Segment:</label>
            <select name="slope" required>
                <option value="0">Upsloping</option>
                <option value="1">Flat</option>
                <option value="2">Downsloping</option>
            </select>

            <label for="ca">Number of Major Vessels Colored by Fluoroscopy:</label>
            <select name="ca" required>
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </select>

            <label for="thal">Thalassemia:</label>
            <select name="thal" required>
                <option value="0">Normal</option>
                <option value="1">Fixed Defect</option>
                <option value="2">Reversible Defect</option>
            </select>

            <button type="submit">Predict</button>
        </form>
    </div>
</body>
</html>

```

### File: templates\result.html
```html
{% if final_result is defined %}
<div class="result">
    {% if final_result == 0 %}
        <center><h1><p>No heart disease detected</p></h1></center>
    {% else %}
        <center><h1><p>Suffering from heart disease</p></h1></center>
    {% endif %}
</div>
{% endif %}
```

### File: .github\workflows\main.yaml
```yaml
name: Build and push image to ECR
on:
  push:
    branches:
      - main



jobs:
  build-and-push-ecr-image:
    name: Build Image
    runs-on: ubuntu-latest
    steps:
    - name: Check out code
      uses: actions/checkout@v2
    - name: Install Utilities
      run: |
        sudo apt-get update
        sudo apt-get install -y jq unzip
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1
    - name: Login to Amazon ECR
      id: login-ecr
      uses: aws-actions/amazon-ecr-login@v1
    - name: Build, tag, and push image to Amazon ECR
      env:
        ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
        ECR_REPOSITORY: heartdiseaseprediction
        IMAGE_TAG: latest
      run: |
        docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
        docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG

```

