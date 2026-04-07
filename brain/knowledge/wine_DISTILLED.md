---
id: wine
type: knowledge
owner: OA_Triage
---
# wine
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Wine-Quality-Prediction

```

### File: requirements.txt
```txt
streamlit
numpy
matplotlib
scikit-learn
seaborn
flask
```

### File: app.py
```py
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

### File: templates\error.html
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

### File: templates\index.html
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

