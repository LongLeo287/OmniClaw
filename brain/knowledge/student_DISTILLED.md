---
id: student
type: knowledge
owner: OA_Triage
---
# student
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Student Performance Prediction

## About The Project

The primary objective of this project is to develop a predictive model that can forecast the performance of students in their academic projects. The model aims to help educators and institutions identify students who may need additional support or intervention early in the project development process, ultimately enhancing overall student success.

## Built With

 - Pandas
 - Numpy
 - Seaborn
 - Matplotlib
 - Scikit-learn
 - Catboost
 - Flask
 - Dill

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
     git clone https://github.com/KalyanMurapaka45/Student-PerfoRmance-Prediction.git
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
     docker pull kalyan45/student-app
     ```

2. **Run the Docker Container**
   - Start the Docker container by running the following command, and mapping any necessary ports:
     ```
     docker run -p 5000:5000 kalyan45/student-app
     ```

3. **Access the Project**
   - Open a web browser or the appropriate client to access the project.


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

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
seaborn
matplotlib
scikit-learn
catboost
xgboost
Flask
dill
-e .

```

### File: setup.py
```py
from setuptools import find_packages,setup
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
name='StudentPerformance',
version='0.0.1',
author='Kalyan',
author_email='kalyanmurapaka274@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'))
```

### File: app.py
```py
import numpy as np
import pandas as pd
from flask import Flask,request,render_template
from sklearn.preprocessing import StandardScaler
from src.pipeline.Prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')))
        
        pred_df=data.get_data_as_data_frame()
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)        
```

### File: template.py
```py
import os
from pathlib import Path

list_of_files = [
    ".github/workflows/main.yaml",
    "Notebook_Experiments/Data/.gitkeep",
    "Notebook_Experiments/Exploratoey_Data_Analysis.ipynb",
    "Notebook_Experiments/Model_Training.ipynb",
    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    "src/components/__init__.py",
    "src/components/Data_ingestion.py",
    "src/components/Data_transformation.py",
    "src/components/Model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/Prediction_pipeline.py",
    "src/pipeline/Training_pipeline.py",
    "static/styles.css",
    "templates/home.html",
    ".gitignore",
    "app.py",
    "Dockerfile",
    "README.md",
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

### File: src\exception.py
```py
import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    


        
```

### File: src\logger.py
```py
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

```

### File: src\utils.py
```py
import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)

```

### File: src\__init__.py
```py

```

### File: static\styles.css
```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
}

.container {
    max-width: 500px;
    margin: 50px auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

h1, h2 {
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
}

.mb-3 {
    margin-bottom: 15px;
}

.form-label {
    font-weight: bold;
}

.form-control {
    width: 100%;
    max-width: 400px;
    padding: 10px;
    box-sizing: border-box;
    margin: 5px auto;
    border: 1px solid #ccc;
    border-radius: 4px;
    transition: border-color 0.3s;
}

.form-control:focus {
    outline: none;
    border-color: #007bff;
}

.btn-primary {
    background-color: #007bff;
    color: #fff;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.btn-primary:hover {
    background-color: #0056b3;
}

```

### File: templates\home.html
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="static\styles.css">
    <title>Student Performance Prediction</title>
</head>
<body>
    <div class="login">
   
       <form action="{{ url_for('predict_datapoint')}}" method="post">
        <h1>
            <legend>Student Performance Prediction</legend>
        </h1>


        <div class="mb-3">
            <label class="form-label">Gender</label><br>
            <select class="form-control" name="gender" placeholder="Enter you Gender" required>
                <option class="placeholder" selected disabled value="">Select your Gender</option>
                <option value="male">
                    Male
                </option>
                <option value="female">
                    Female
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Race or Ethnicity</label><br>
            <select class="form-control" name="ethnicity" placeholder="Enter you ethnicity" required>
                <option class="placeholder" selected disabled value="">Select Ethnicity</option>
                <option value="group A">
                    GROUP - A
                </option>
                <option value="group B">
                    GROUP - B
                </option>
                <option value="group C">
                    GROUP - C
                </option>
                <option value="group D">
                    GROUP - D
                </option>
                <option value="group E">
                    GROUP - E
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Parental Level of Education</label>
            <select class="form-control" name="parental_level_of_education"
                placeholder="Enter you Parent Education" required>
                <option class="placeholder" selected disabled value="">Select Parent Education</option>
                <option value="associate's degree">
                    Associate's Degree
                </option>
                <option value="bachelor's degree">
                    Bachelor's Degree
                </option>
                <option value="high school">
                    High School
                </option>
                <option value="master's degree">
                    Master's Degree
                </option>
                <option value="some college">
                    Some College
                </option>
                <option value="some high school">
                    Some High School
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Lunch Type</label><br>
            <select class="form-control" name="lunch" placeholder="Enter you Lunch" required>
                <option class="placeholder" selected disabled value="">Select Lunch Type</option>
                <option value="free/reduced">
                    Free / Reduced
                </option>
                <option value="standard">
                    Standard
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Test preparation Course</label>
            <select class="form-control" name="test_preparation_course" placeholder="Enter you Course"
                required>
                <option class="placeholder" selected disabled value="">Select Test_course</option>
                <option value="none">
                    None
                </option>
                <option value="completed">
                    Completed
                </option>
            </select>
        </div>


        <div class="mb-3">
            <label class="form-label">Writing Score out of 100</label>
            <input class="form-control" type="number" name="reading_score"
                placeholder="Enter your Reading score" min='0' max='100' />
        </div>


        <div class="mb-3">
            <label class="form-label">Reading Score out of 100</label>
            <input class="form-control" type="number" name="writing_score"
                placeholder="Enter your Reading Score" min='0' max='100' />
        </div>

        <div class="mb-3">
            <input class="btn btn-primary" type="submit" value="Predict your Maths Score" required />
        </div>
    </form>
    <h2>
       The Prediction is {{results}}
    </h2>
   <body>
</html>
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
        ECR_REPOSITORY: studentprediction
        IMAGE_TAG: latest
      run: |
        docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
        docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG

```

### File: src\components\Data_ingestion.py
```py
import os
import sys
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.exception import CustomException
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('Artifacts',"Train_Data.csv")
    test_data_path: str=os.path.join('Artifacts',"Test_Data.csv")
    raw_data_path: str=os.path.join('Artifacts',"Raw_Data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        try:
            data=pd.read_csv('Notebook_Experiments\Data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Created the raw data file")

            logging.info("Splitting the data into train and test")
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            logging.info("Data Splitting is done")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Created the train and test data files")
            logging.info("Data ingestion completed")

            return (self.ingestion_config.test_data_path,self.ingestion_config.train_data_path)
                
        except Exception as e:
            logging.info("Excpetion occured while ingesting the data")
            raise CustomException(e,sys)
```

### File: src\components\Data_transformation.py
```py
import os
import sys
import numpy as np 
import pandas as pd
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.exception import CustomException
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('Artifacts',"Preprocessor.pkl")

    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = ["gender","race_ethnicity","parental_level_of_education","lunch","test_preparation_course"]
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())]
                )

            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))]
                )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)]
                )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            logging.info(f'Train Data Before Transformation:\n {train_df.head()}')
            logging.info(f'Test Data Before Transformation:\n {test_df.head()}')

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(f'Input Train Data After Transformation: \n {input_feature_train_df.head()}')
            logging.info(f'Input Test Data After Transformation:\n {input_feature_test_df.head()}')
            logging.info(f'Target Train Data After Transformation: \n{target_feature_train_df.head()}')
            logging.info(f'Target Test Data After Transformation:\n {target_feature_test_df.head()}')

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info(f'Input Train Data After Transformation: \n {input_feature_train_arr.shape}')
            logging.info(f'Input Test Data After Transformation:\n {input_feature_test_arr.shape}')

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
```

### File: src\components\Model_trainer.py
```py
import os
import sys
from src.logger import logging
from dataclasses import dataclass
from sklearn.metrics import r2_score
from catboost import CatBoostRegressor
from src.exception import CustomException
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from src.utils import save_object,evaluate_models
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("Artifacts","Model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                } 
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models,param=params)
            
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            logging.info(f'Best Model: {best_model}')
            logging.info(f"R2 score of best model is {r2_square}")
            return r2_square
        
        except Exception as e:
            raise CustomException(e,sys)
```

### File: src\components\__init__.py
```py

```

### File: src\pipeline\Prediction_pipeline.py
```py
import os
import sys
import pandas as pd
from src.utils import load_object
from src.exception import CustomException

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("Artifacts","Model.pkl")
            preprocessor_path=os.path.join('Artifacts','Preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)


```

### File: src\pipeline\Training_pipeline.py
```py
from src.components.Data_ingestion import DataIngestion
from src.components.Data_transformation import DataTransformation
from src.components.Model_trainer import ModelTrainer

obj=DataIngestion()
train_data,test_data=obj.initiate_data_ingestion()

data_transformation=DataTransformation()
train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

modeltrainer=ModelTrainer()
print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

```

### File: src\pipeline\__init__.py
```py

```

