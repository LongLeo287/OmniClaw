---
id: spam
type: knowledge
owner: OA_Triage
---
# spam
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Spam Email Classification System

A production-grade machine learning system designed to robustly classify emails as "Spam" or "Ham" (legitimate). This project features a modular pipeline architecture for training and inference, integrated with a modern Streamlit user interface for easy interaction.

## 🚀 Key Features

- **Advanced ML Pipeline**: Modular design separating data ingestion, transformation, and model training.
- **Multiple Model Support**: evaluation of various algorithms including SVM, Logistic Regression, Decision Trees, and Random Forest.
- **Interactive Web UI**: Built with Streamlit for real-time single-email analysis and batch processing.
- **MBOX Support**: Native capability to process and classify entire `mbox` email archives.
- **Detailed Analytics**: Comprehensive logging and performance metrics (Precision, Recall, F1-Score).

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Frontend**: Streamlit
- **ML Framework**: Scikit-learn
- **Data Processing**: Pandas, NumPy, BeautifulSoup4
- **Project Management**: `uv` (recommended) or `pip`

## 📂 Project Structure

```
├── app.py                  # Main Streamlit Web Application
├── requirements.txt        # Project dependencies
├── main.py                 # (Optional) Alternative entry point
├── src/
│   ├── components/         # Core processing modules (Ingestion, Transformation)
│   ├── pipeline/           # Orchestration pipelines (Training, Prediction)
│   ├── config/             # Configuration and parameters
│   └── utils/              # Helper functions, logging, and state management
├── data/                   # Dataset storage (inputs)
├── outputs/                # Training artifacts (models, vectorizers)
└── logs/                   # System runtime logs
```

## ⚡ Installation

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd Spam-Email-Detection
   ```

2. **Set up Environment**
   It is recommended to use a virtual environment.
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

### 1. Running the Web Application
Launch the interactive dashboard to classify emails instantly.

```bash
streamlit run app.py
```

- **Single Email Tab**: Paste email content to get an immediate Spam/Ham prediction with a confidence score.
- **Batch Processing Tab**: Upload an `.mbox` file to process multiple emails at once and download the results as a CSV.

### 2. Training the Model
(Optional) If you wish to retrain the models on new data:

1. Place your dataset in `data/dataset/dataset.csv`.
2. Run the training pipeline:
   ```bash
   python -m src.pipeline.training_pipeline
   ```
3. Artifacts (Model & Vectorizer) will be saved in the `outputs/` directory.
4. **Important**: Update `src/config/config.py` with the new paths to your generated model and vectorizer if they change.

## ⚙️ Configuration

The system is highly configurable via `src/config/config.py`. You can adjust:
- Model hyperparameters (Grid Search configuration)
- Input/Output paths
- Training parameters (Cross-validation folds, etc.)

## 📊 Model Performance

The pipeline automatically evaluates models using 5-fold cross-validation. Metrics including Accuracy, Precision, Recall, and F1-Score are logged for each experiment. By default, the system selects the best performing model (often SVM or Random Forest) for inference.

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

```

### File: requirements.txt
```txt
fastapi==0.115.6
uvicorn[standard]==0.34.0
python-multipart==0.0.20
pandas==2.2.3
beautifulsoup4==4.12.3
scikit-learn==1.6.1
pydantic==2.10.6
streamlit>=1.32.0

```

### File: app.py
```py
import streamlit as st
import pandas as pd
import tempfile
import os
import time
from src.pipeline.prediction_pipeline import PredictionPipeline

# Page configuration
st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

# Initialize pipeline
@st.cache_resource
def get_pipeline():
    return PredictionPipeline(load_models=True)

try:
    pipeline = get_pipeline()
except Exception as e:
    st.error(f"Error loading models: {str(e)}")
    st.stop()

st.title("📧 Spam Email Classifier")
st.markdown("Classify emails as **Spam** or **Ham** (Clean) using Machine Learning.")

# Tabs for different modes
tab1, tab2 = st.tabs(["Single Email", "Batch MBOX Processing"])

with tab1:
    st.header("Check a Single Email")
    email_text = st.text_area("Paste the email content here:", height=200, placeholder="Dear friend, I have a business proposal...")
    
    if st.button("Classify Email", type="primary"):
        if email_text.strip():
            with st.spinner("Analyzing..."):
                try:
                    # Get prediction
                    result = pipeline.predict_single_email(email_text)
                    prediction = result['prediction']
                    confidence = result.get('confidence', 0)
                    
                    # Display result
                    if prediction == "Spam":
                        st.error(f"🚨 This email is **SPAM**")
                    else:
                        st.success(f"✅ This email is **HAM** (Safe)")
                    
                    if confidence:
                        st.info(f"Confidence Score: {confidence:.1f}%")
                        
                except Exception as e:
                    st.error(f"Error analyzing email: {str(e)}")
        else:
            st.warning("Please enter some text to classify.")

with tab2:
    st.header("Process MBOX File")
    uploaded_file = st.file_uploader("Upload an MBOX file", type=['mbox', 'txt'])
    
    if uploaded_file is not None:
        if st.button("Process File"):
            with st.spinner("Processing file... this may take a moment"):
                try:
                    # Save uploaded file to temp
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.mbox') as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_path = tmp_file.name
                    
                    try:
                        # Process file
                        df = pipeline.predict_mbox_file(tmp_path)
                        
                        # Show summary metrics
                        col1, col2 = st.columns(2)
                        spam_count = len(df[df['Prediction'] == 'Spam'])
                        ham_count = len(df[df['Prediction'] == 'Ham'])
                        
                        col1.metric("Total Emails", len(df))
                        col2.metric("Spam Found", spam_count, delta_color="inverse")
                        
                        # Show previews
                        st.subheader("Results Preview")
                        st.dataframe(df[['Time', 'Subject', 'Prediction']].head(10))
                        
                        # Download button
                        csv = df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="Download Full Results (CSV)",
                            data=csv,
                            file_name=f"predictions_{int(time.time())}.csv",
                            mime="text/csv",
                        )
                        
                    finally:
                        # Cleanup temp file
                        if os.path.exists(tmp_path):
                            try:
                                os.unlink(tmp_path)
                            except:
                                pass # Sometimes file lock prevents deletion on Windows
                                
                except Exception as e:
                    st.error(f"Error processing file: {str(e)}")

```

### File: src\__init__.py
```py

```

### File: src\components\data_ingestion.py
```py
import pandas as pd
from src.utils.logger import get_logger
from src.config.config import Config
from src.utils.state import TrainingState

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self):
        self.config = Config()
    
    def load_data(self, state: TrainingState) -> TrainingState:
        try:
            logger.info("Loading data")
            state.training_data = pd.read_csv(self.config.training_data_path)
            logger.info("Data loaded successfully")
            return state
        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            raise e
    
```

### File: src\components\data_transformation.py
```py
from src.utils.logger import get_logger
from src.config.config import Config
from src.utils.state import TrainingState
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

logger = get_logger(__name__)

class DataTransformation:
    def __init__(self):
        self.config = Config()
    
    def transform_data(self, state: TrainingState) -> TrainingState:
        logger.info("Data transformation started")
        try:
            data = state.training_data.copy()
            
            # Encode labels: spam -> 0, ham -> 1
            data.loc[data['Category'] == 'spam', 'Category'] = 0
            data.loc[data['Category'] == 'ham', 'Category'] = 1
            
            # Ensure Category column is integer type
            data['Category'] = data['Category'].astype(int)
            
            logger.info(f"Label encoding completed. Data shape: {data.shape}")
            logger.info(f"Unique labels: {data['Category'].unique()}")
            logger.info(f"Label dtype: {data['Category'].dtype}")
            
            # Split features and target
            X = data['Message']
            y = data['Category']
            
            # Convert y to numpy array of integers to ensure proper type
            import numpy as np
            y = np.array(y, dtype=int)
            
            # Split into train and test sets (70:30 ratio)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.3, random_state=42, stratify=y
            )
            
            logger.info(f"Train/test split completed. Train size: {len(X_train)}, Test size: {len(X_test)}")
            
            # Apply TF-IDF vectorization
            tfidf_vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
            X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
            X_test_tfidf = tfidf_vectorizer.transform(X_test)
            
            logger.info(f"TF-IDF transformation completed. Feature shape: {X_train_tfidf.shape}")
            
            # Save to state
            state.transformed_data = data
            state.X_train = X_train
            state.X_test = X_test
            state.y_train = y_train
            state.y_test = y_test
            state.X_train_tfidf = X_train_tfidf
            state.X_test_tfidf = X_test_tfidf
            state.tfidf_vectorizer = tfidf_vectorizer
            
            logger.info("Data transformation completed")
            return state
        except Exception as e:
            logger.error(f"Failed to transform data: {str(e)}")
            raise e
```

### File: src\components\model_training.py
```py
import os
import time
import json
import pickle
from datetime import datetime

import numpy as np
import pandas as pd

from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

from src.utils.logger import get_logger
from src.utils.state import TrainingState
from src.config.config import Config, ModelConfig

logger = get_logger(__name__)

class ModelTraining:
    def __init__(self):
        self.config = Config()
        self.param_grids = ModelConfig.models
    
    def save_pickle_files(self, state: TrainingState):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_dir = os.path.join(self.config.OUTPUT_BASE_DIR, timestamp)
            models_dir = os.path.join(output_dir, "models")
            observations_dir = os.path.join(output_dir, "observations")
        
            os.makedirs(models_dir, exist_ok=True)
            os.makedirs(observations_dir, exist_ok=True)

            vectorizer_path = os.path.join(models_dir, "vectorizer.pkl")
            with open(vectorizer_path, 'wb') as f:
                pickle.dump(state.tfidf_vectorizer, f)
            logger.info(f"Saved TF-IDF vectorizer: {vectorizer_path}")
        
            best_model_path = os.path.join(models_dir, f"{state.best_model_name}_model.pkl")
            with open(best_model_path, 'wb') as f:
                pickle.dump(state.best_model, f)
            logger.info(f"Saved best model: {state.best_model_name}_model.pkl")
        
            metadata = {
                'timestamp': timestamp,
                'best_model_name': state.best_model_name,
                'best_model_params': str(state.best_params),
                'best_model_metrics': str(state.model_metrics[state.best_model_name]),
                'all_models': ', '.join(list(state.trained_models.keys())),
                'tfidf_features': state.X_train_tfidf.shape[1],
                'train_samples': len(state.y_train),
                'test_samples': len(state.y_test)
            }
            
            metadata_path = os.path.join(observations_dir, "model_metadata.csv")
            pd.DataFrame([metadata]).to_csv(metadata_path, index=False)
            logger.info(f"Saved metadata: {metadata_path}")
            
            return output_dir

        except Exception as e:
            logger.error(f"Failed to save pickle files: {str(e)}")
            raise
    
    def save_metrics_to_csv(self, state: TrainingState, output_dir: str):
        observations_dir = os.path.join(output_dir, "observations")
        os.makedirs(observations_dir, exist_ok=True)
        
        # 1. Model Comparison Summary
        # ----------------------------------------------------------------------
        metrics_data = []
        for model_name, metrics in state.model_metrics.items():
            metrics_data.append({
                'Model': model_name,
                'Accuracy': metrics['accuracy'],
                'Precision': metrics['precision'],
                'Recall': metrics['recall'],
                'F1_Score': metrics['f1_score'],
                'CV_Score': metrics.get('best_cv_score', 'N/A'),
                'Is_Best_Model': '1' if model_name == state.best_model_name else '0'
            })
        
        df_summary = pd.DataFrame(metrics_data)
        df_summary = df_summary.sort_values('Accuracy', ascending=False)
        summary_path = os.path.join(observations_dir, "model_comparison_summary.csv")
        df_summary.to_csv(summary_path, index=False)
        logger.info(f"Saved: model_comparison_summary.csv")
        
        # 2. Best Parameters for Each Model
        # ----------------------------------------------------------------------
        params_data = []
        for model_name, metrics in state.model_metrics.items():
            best_params = metrics.get('best_params', {})
            if isinstance(best_params, dict):
                params_str = json.dumps(best_params, indent=2)
            else:
                params_str = str(best_params)
            
            params_data.append({
                'Model': model_name,
                'Best_Parameters': params_str,
                'CV_Score': metrics.get('best_cv_score', 'N/A')
            })
        
        df_params = pd.DataFrame(params_data)
        params_path = os.path.join(observations_dir, "best_parameters.csv")
        df_params.to_csv(params_path, index=False)
        logger.info(f"Saved: best_parameters.csv")
        
        # 3. Cross-Validation Results Summary
        # ----------------------------------------------------------------------
        if state.cv_results:
            cv_summary = []
            for model_name, cv_data in state.cv_results.items():
                cv_summary.append({
                    'Model': model_name,
                    'Best_CV_Score': cv_data.get('best_score', 'N/A'),
                    'Best_Parameters': json.dumps(cv_data.get('best_params', {}))
                })
            
            df_cv = pd.DataFrame(cv_summary)
            cv_path = os.path.join(observations_dir, "cross_validation_summary.csv")
            df_cv.to_csv(cv_path, index=False)
            logger.info(f"Saved: cross_validation_summary.csv")
        
        # 4. Best Model Information
        # ----------------------------------------------------------------------
        best_model_info = {
            'Attribute': [
                'Best Model Name',
                'Accuracy',
                'Precision',
                'Recall',
                'F1-Score',
                'CV Score',
                'Best Parameters'
            ],
            'Value': [
                state.best_model_name,
                state.model_metrics[state.best_model_name]['accuracy'],
                state.model_metrics[state.best_model_name]['precision'],
                state.model_metrics[state.best_model_name]['recall'],
                state.model_metrics[state.best_model_name]['f1_score'],
                state.model_metrics[state.best_model_name].get('best_cv_score', 'N/A'),
                json.dumps(state.best_params, indent=2) if isinstance(state.best_params, dict) else str(state.best_params)
            ]
        }
        
        df_best = pd.DataFrame(best_model_info)
        best_path = os.path.join(observations_dir, "best_model_info.csv")
        df_best.to_csv(best_path, index=False)
        logger.info(f"Saved: best_model_info.csv")


    def train_models(self, state: TrainingState, cv_folds: int = 5) -> TrainingState:
        logger.info("Model training started")
        logger.info(f"Using GridSearchCV with {cv_folds}-fold CV")
        
        try:
            X_train = state.X_train_tfidf
            X_test = state.X_test_tfidf
            y_train = state.y_train
            y_test = state.y_test
            
            trained_models, model_metrics, cv_results = {}, {}, {}
            
            # Define model instances
            models = {
                'LogisticRegression': LogisticRegression(random_state=42),
                'DecisionTree': DecisionTreeClassifier(random_state=42),
                'SVM': SVC(random_state=42),
                'KNN': KNeighborsClassifier(),
                'RandomForest': RandomForestClassifier(random_state=42)
            }
            
            for model_name, model in models.items():
                start_time = time.time()
                logger.info(f"\n{'='*60}")
                logger.info(f"Training {model_name}...")
                
                param_grid = self.param_grids.get(model_name, {})
                
                search = GridSearchCV(model,
                                    param_grid=param_grid,
                                    cv=cv_folds,
                                    scoring='f1',
                                    n_jobs=-1
                                    )
                
                search.fit(X_train, y_train)
                best_model = search.best_estimator_
                
                y_pred = best_model.predict(X_test)
                
                metrics = {
                    'accuracy': accuracy_score(y_test, y_pred),
                    'precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
                    'recall': recall_score(y_test, y_pred, average='weighted', zero_division=0),
                    'f1_score': f1_score(y_test, y_pred, average='weighted', zero_division=0),
                    'best_params': search.best_params_,
                    'best_cv_score': search.best_score_
                }
                
                trained_models[model_name] = best_model
                model_metrics[model_name] = metrics
                cv_results[model_name] = {
                    'cv_scores': search.cv_results_,
                    'best_params': search.best_params_,
                    'best_score': search.best_score_
                }
                
                end_time = time.time()
                
                logger.info(f"{model_name} - Training time: {end_time - start_time:.2f} seconds")
                logger.info(f"{model_name} - Best Parameters: {search.best_params_}")
                logger.info(f"{model_name} - CV Score: {search.best_score_:.4f}")
                logger.info(f"{model_name} - Test Accuracy: {metrics['accuracy']:.4f}")
                logger.info(f"{model_name} - Test Precision: {metrics['precision']:.4f}")
                logger.info(f"{model_name} - Test Recall: {metrics['recall']:.4f}")
                logger.info(f"{model_name} - Test F1-Score: {metrics['f1_score']:.4f}")
            
            # Find best model based on F1-score
            best_model_name = max(model_metrics, key=lambda x: model_metrics[x]['f1_score'])
            best_model = trained_models[best_model_name]
            best_params = model_metrics[best_model_name]['best_params']
            
            logger.info(f"{'='*60}")
            logger.info(f"BEST MODEL: {best_model_name}")
            logger.info(f"Best F1-Score: {model_metrics[best_model_name]['f1_score']:.4f}")
            logger.info(f"Best Parameters: {best_params}")
            logger.info(f"{'='*60}")
            
            state.trained_models = trained_models
            state.model_metrics = model_metrics
            state.best_model_name = best_model_name
            state.best_model = best_model
            state.best_params = best_params
            state.cv_results = cv_results
            
            output_dir = self.save_pickle_files(state)
            self.save_metrics_to_csv(state, output_dir)
            logger.info("\nModel training completed successfully")
            logger.info(f"All outputs saved to: {output_dir}/")
            return state
            
        except Exception as e:
            logger.error(f"Failed to train models: {str(e)}")
            raise e
```

### File: src\config\config.py
```py
from dataclasses import dataclass

@dataclass
class Config:
    training_data_path: str = "data/dataset/dataset.csv"
    validation_data_path: str = "data/dataset/All_mail_Including_Spam_and_Trash.mbox"
    OUTPUT_BASE_DIR: str = "outputs"
    model_path: str = "outputs/2025-12-25_14-02-05/models/SVM_model.pkl"
    feature_path: str = "outputs/2025-12-25_14-02-05/models/vectorizer.pkl"

class ModelConfig:
    models = {
        'LogisticRegression': {
            'C': [0.01, 0.1, 1, 10, 100],
            'solver': ['lbfgs', 'liblinear'],
            'max_iter': [100, 200, 300]
        },
        'DecisionTree': {
            'criterion': ['gini', 'entropy'],
            'max_depth': [5, 10, 15, 20, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        },
        'SVM': {
            'C': [0.1, 1, 10],
            'kernel': ['linear', 'rbf'],
            'gamma': ['scale', 'auto']
        },
        'KNN': {
            'n_neighbors': [3, 5, 7, 9, 11],
            'weights': ['uniform', 'distance'],
            'metric': ['euclidean', 'manhattan']
        },
        'RandomForest': {
            'n_estimators': [50, 100, 200],
            'max_depth': [10, 20, 30, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'max_features': ['sqrt', 'log2']
        }
    }
```

### File: src\pipeline\prediction_pipeline.py
```py
import mailbox
import pickle
import time
import pandas as pd
from typing import Dict, List, Optional
from pathlib import Path

from src.utils.state import PredictionState
from src.utils.logger import get_logger
from src.config.config import Config
from src.utils.email_utils import extract_body, all_recipients, clean_text

logger = get_logger(__name__)

class PredictionPipeline:
    def __init__(self, load_models: bool = True):
        self.config = Config()
        self.mailbox = None
        self.feature_transformer = None
        self.model = None
        
        if load_models:
            self._load_models()
    
    def _load_models(self) -> None:

        logger.info("Loading models...")
        self.feature_transformer = pickle.load(open(self.config.feature_path, "rb"))
        self.model = pickle.load(open(self.config.model_path, "rb"))
        logger.info("Models loaded successfully")
    
    def predict_single_email(self, email_body: str) -> Dict:
        if self.model is None or self.feature_transformer is None:
            self._load_models()

        cleaned_body = clean_text(email_body)
        features = self.feature_transformer.transform([cleaned_body])
        prediction = self.model.predict(features)
        prediction_label = "Spam" if str(prediction[0]) == "0" else "Ham"
        
        try:
            prediction_proba = self.model.predict_proba(features)
            confidence = float(max(prediction_proba[0])) * 100
        except:
            confidence = None
        
        return {
            'prediction': prediction_label,
            'confidence': confidence,
            'raw_prediction': int(prediction[0])
        }

    def load_mailbox(self, mailbox_path: str) -> None:
        """Load MBOX file"""

        logger.info(f"Loading mailbox from {mailbox_path}")
        self.mailbox = mailbox.mbox(mailbox_path)
        logger.info(f"Loaded mailbox from {mailbox_path}")

    def process_mailbox(self, mailbox_path: Optional[str] = None) -> List[Dict]:
        if mailbox_path:
            self.load_mailbox(mailbox_path)
        
        if self.mailbox is None:
            raise ValueError("No mailbox loaded. Call load_mailbox() first.")
        
        logger.info("Processing mailbox")
        data = []
        
        for message in self.mailbox:
            labels = (message.get("X-Gmail-Labels") or "").lower()
            category = (
                "Spam" if "spam" in labels else
                "Promotions" if "category_promotions" in labels else
                "Social" if "category_social" in labels else
                "Updates" if "category_updates" in labels else
                "Inbox"
            )
            time_str = message.get("Date", "")
            recipients = clean_text(all_recipients(message))
            subject = clean_text(message.get("Subject", ""))
            body = clean_text(extract_body(message))
            direction = "Sent" if "Sent" in (message.get("X-Gmail-Labels") or "") else "Received"
            
            data.append({
                "Time": time_str,
                "Recipients": recipients,
                "Subject": subject,
                "Body": body,
                "Category": category,
                "Direction": direction
            })
        
        logger.info(f"Processed {len(data)} emails from mailbox")
        self.mailbox.close()
        
        return data
    
    def run_prediction(self, mail_data: List[Dict]) -> List[Dict]:
        if self.model is None or self.feature_transformer is None:
            self._load_models()
        
        start_time = time.time()
        logger.info("Running predictions")
        
        for mail in mail_data:
            body_text = mail.get('Body', '')
            features = self.feature_transformer.transform([body_text])
            prediction = self.model.predict(features)
            prediction_label = "Spam" if str(prediction[0]) == "0" else "Ham"
            mail["Prediction"] = prediction_label
        
        end_time = time.time()
        logger.info(f"Prediction completed in {end_time - start_time:.2f} seconds")
        
        return mail_data
    
    def predict_mbox_file(self, mailbox_path: str, output_path: Optional[str] = None) -> pd.DataFrame:
        mail_data = self.process_mailbox(mailbox_path)
        mail_data = self.run_prediction(mail_data)
        df = pd.DataFrame(mail_data)
        if output_path:
            df.to_csv(output_path, index=False)
            logger.info(f"Predictions saved to {output_path}")
        return df


def run_legacy_pipeline(state: PredictionState) -> None:
    pipeline = PredictionPipeline(load_models=False)
    pipeline.load_mailbox(state.mailbox_path)
    mail_data = pipeline.process_mailbox()
    state.mail_data = mail_data
    state.mail_data = pipeline.run_prediction(state.mail_data)
    df = pd.DataFrame(state.mail_data)
    df.to_csv("data/predictions.csv", index=False)
```

### File: src\pipeline\training_pipeline.py
```py
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTraining
from src.utils.state import TrainingState
from src.utils.logger import get_logger

logger = get_logger(__name__)

class TrainingPipeline:
    """Complete training pipeline for spam classification"""
    
    def __init__(self):
        self.state = TrainingState()
        
    def run_pipeline(self, cv_folds: int = 5):
        try:
            logger.info("Initiating training pipeline")
            ingestion = DataIngestion()
            self.state = ingestion.load_data(self.state)
            logger.info(f"Data loaded successfully: {self.state.training_data.shape}")
            logger.info(f"Columns: {self.state.training_data.columns.tolist()}")
            logger.info(f"Sample size: {len(self.state.training_data)} emails")

            transformation = DataTransformation()
            self.state = transformation.transform_data(self.state)
            logger.info(f"Data transformation completed")
            logger.info(f"Training set: {len(self.state.X_train)} samples")
            logger.info(f"Test set: {len(self.state.X_test)} samples")
            logger.info(f"TF-IDF features: {self.state.X_train_tfidf.shape[1]}")
            
            trainer = ModelTraining()
            self.state = trainer.train_models(
                self.state, 
                cv_folds=cv_folds
            )
            
            logger.info("\n" + "="*70)
            logger.info("Training pipeline completed successfully")
            logger.info("="*70)
            logger.info(f"All metrics saved to 'results/' directory")
            logger.info(f"Best model: {self.state.best_model_name}")
            logger.info(f"Best F1-Score: {self.state.model_metrics[self.state.best_model_name]['f1_score']:.4f}")
            
            return self.state
            
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            raise e

if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.run_pipeline(cv_folds=5)
```

### File: src\pipeline\__init__.py
```py

```

### File: src\utils\email_utils.py
```py
import re
from html import unescape
from email.utils import getaddresses
from bs4 import BeautifulSoup

# ----------------------------------------------------------------------------
# Function to extract email body content
# ----------------------------------------------------------------------------
def extract_body(msg):
    texts = []

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ("text/plain", "text/html"):
                payload = part.get_payload(decode=True)
                if payload:
                    text = payload.decode(errors="ignore")
                    text = unescape(text)
                    text = BeautifulSoup(text, "html.parser").get_text(" ")
                    texts.append(text)
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            text = unescape(payload.decode(errors="ignore"))
            text = BeautifulSoup(text, "html.parser").get_text(" ")
            texts.append(text)

    clean = " ".join(texts)
    clean = re.sub(r'\\+', ' ', clean)
    clean = re.sub(r'[\r\n\t]+', ' ', clean)
    clean = re.sub(r'\s+', ' ', clean)
    return clean.strip()

# ----------------------------------------------------------------------------
# Function to extract all recipients from email headers
# ----------------------------------------------------------------------------
def all_recipients(msg):
    fields = []
    for h in ["From", "To", "Cc", "Bcc"]:
        fields.extend(getaddresses([msg.get(h, "")]))
    return ", ".join(sorted(set(addr for _, addr in fields if addr)))

# ----------------------------------------------------------------------------
# Function to clean text for Excel compatibility
# ----------------------------------------------------------------------------
def clean_text(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\u200B\u200C\u200D\u200E\u200F\uFEFF]', '', text)
    text = text.encode("utf-16", "surrogatepass").decode("utf-16", "ignore")
    text = text[:32767]
    if text.startswith(("=", "+", "-", "@")):
        text = "'" + text
    return text
```

### File: src\utils\logger.py
```py
import logging
from pathlib import Path
from datetime import datetime

# Global variable to store the log file path for the current run
_LOG_FILE = None

def get_logger(name: str):
    global _LOG_FILE
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    # Create log file path only once for the entire pipeline run
    if _LOG_FILE is None:
        date_dir = datetime.now().strftime("%Y-%m-%d")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_dir = Path("logs") / date_dir
        log_dir.mkdir(parents=True, exist_ok=True)
        _LOG_FILE = log_dir / f"{timestamp}.log"

    handler = logging.FileHandler(_LOG_FILE, encoding="utf-8")
    formatter = logging.Formatter(
        "[%(asctime)s]: %(filename)s - Line %(lineno)d: %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False
    return logger
```

### File: src\utils\state.py
```py
from typing import Optional, List, Dict, Any
import pandas as pd

class TrainingState:
    training_data_path: Optional[str] = None
    training_data: Optional[pd.DataFrame] = None
    transformed_data: Optional[pd.DataFrame] = None
    X_train: Optional[pd.Series] = None
    X_test: Optional[pd.Series] = None
    y_train: Optional[pd.Series] = None
    y_test: Optional[pd.Series] = None
    X_train_tfidf: Optional[Any] = None
    X_test_tfidf: Optional[Any] = None
    tfidf_vectorizer: Optional[Any] = None
    trained_models: Optional[Dict[str, Any]] = None
    model_metrics: Optional[Dict[str, Dict[str, float]]] = None
    best_model_name: Optional[str] = None
    best_model: Optional[Any] = None
    best_params: Optional[Dict[str, Any]] = None
    cv_results: Optional[Dict[str, Any]] = None

class PredictionState:
    mailbox_path: Optional[str] = None
    mail_data: Optional[List[Dict[str, str]]] = None
```

### File: src\utils\utils.py
```py

```

### File: src\utils\__init__.py
```py

```

