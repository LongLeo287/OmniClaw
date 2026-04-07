---
id: medical
type: knowledge
owner: OA_Triage
---
# medical
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Medical Query Generator

A Flask web application that uses Google's GenerativeAI (Gemini) to generate medical responses based on user input. The application simulates a medical expert providing accurate advice to a patient's query.

## About The Project

The Medical Query Generator is a web application that leverages Google's GenerativeAI to generate detailed and accurate medical responses. Users input medical queries, and the application provides responses adhering to specific guidelines for clarity, accuracy, and informativeness.

## Getting Started

To get started with the project, follow the steps below.

### Prerequisites

- Google API Key
- Google Generativeai
- Flask
- Python Dotenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KalyanMurapaka45/Medical-Assisstant.git
   cd medical-query-generator
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API Key:

   - Create a project on the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the GenerativeAI API.
   - Create an API key and add it to your environment variables or a `.env` file.

4. Run the application:

   ```bash
   python app.py
   ```

   The application will be accessible at [http://localhost:5000/](http://localhost:5000/).

## Usage

1. Open your web browser and navigate to [http://localhost:5000/](http://localhost:5000/).
2. Input a medical query following the provided guidelines.
3. Click the "Generate Response" button to obtain a detailed medical response.

## Contributing

Contributions to the Medical Query Generator are welcome! If you have suggestions, enhancements, or bug fixes, please follow the steps below:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

- Your Name - [kalyanmurapaka274@gmail.com](mailto:kalyanmurapaka274@gmail.com)

Project Link: [https://github.com/KalyanMurapaka45/Medical-Assisstant](https://github.com/KalyanMurapaka45/Medical-Assisstant)

```

### File: requirements.txt
```txt
flask
google-generativeai
python-dotenv
```

### File: app.py
```py
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, render_template, request

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            user_input = request.form['user_input']
        except KeyError:
            user_input = ""

        prompt = f"""Imagine you are a medical expert and you are giving accurate medical advice to a patient. 
        You are presented with a medical query and asked to provide a response with a detailed explanation. 
        Note that dont mention any inaccurate or misleading information.

        Medical Query: {user_input}

        Key Details:
        - Provide precise information related to the patient's medical concern.
        - Indicate if any diagnostic tests or examinations have been performed.
        - Specify the current medications or treatments prescribed.
        - The response should be in a paragraph format but not in point-wise.
        - If only a specific disease name is mentioned, response must contain the symptoms, causes, and treatment of the disease with respective headings.

        Guidelines:
        - Use clear and concise language.
        - The vocabulary should be appropriate for the medical context.
        - Include specific parameters or considerations within the medical context.
        - If the response contains a list of items, convert it into a paragraph format.
        - Avoid using abbreviations or acronyms.
        - Avoid Headings and Sub hheadings just give me the complete response in a paragraph format.
        - Refrain from presenting inaccurate or ambiguous information.
        - Ensure the query is focused and not overly broad."""

        # Get Gemini response
        gemini_response = get_gemini_response(prompt)

        return render_template('index.html', user_input=user_input, response=gemini_response)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### File: static\style.css
```css
/* General styling */
body {
    font-family: Arial, sans-serif;
    font-size: 16px;
    color: #333;
    background-color: #f5f5f5;
    margin: 0;
  }
  
  .container {
    max-width: 800px;
    margin: 30px auto;
    padding: 20px;
    border-radius: 5px;
    background-color: #fff;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  header {
    text-align: center;
    margin-bottom: 30px;
  }
  
  h1 {
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  p.lead {
    font-size: 18px;
    font-weight: 300;
    margin-bottom: 20px;
  }
  
  label {
    font-weight: bold;
    margin-bottom: 5px;
    display: block;
  }
  
  textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    resize: none;
  }
  
  input[type="submit"] {
    background-color: #007bff; /* Primary blue */
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s ease-in-out; /* Add a smooth hover effect */
  }
  
  input[type="submit"]:hover {
    background-color: #0062cc; /* Darker blue on hover */
  }
  
  section.response {
    margin-top: 20px;
    font-size: 18px;
    line-height: 1.5;
  }
  
  footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
  }
  
  
  /* Additional considerations for healthcare context */
  .response p {
    margin-bottom: 15px;
  }
  
  .response strong {
    font-weight: bold;
  }
  
  .response em {
    font-style: italic;
  }
  
  /* Optional: Visual enhancements */
  /* Add a subtle gradient to the container */
  .container {
    background: linear-gradient(to bottom, #f7f7f7, #e9e9e9);
  }
  
  /* Add a touch of color to the submit button */
  input[type="submit"]:hover {
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  }  

```

### File: templates\index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Medical Advisor</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}" />
</head>
<body>
  <div class="container">
    <header>
      <h1>Your Trusted Medical Advisor</h1>
      <p class="lead">Get accurate and reliable medical advice tailored to your concerns.</p>
    </header>

    <form method="post">
      <label for="user_input">Enter Your Medical Query:</label>
      <textarea id="user_input" name="user_input" rows="4" cols="50"></textarea><br /><br />
      <input type="submit" value="Submit" />
    </form>

    {% if user_input %}
    <section class="response">
      <h2>Medical Response</h2>
      <p>{{ response }}</p>
    </section>
    {% endif %}

    <footer>
      <center><p>&copy; 2023 Your Medical Advisor</p></center>
    </footer>
  </div>
</body>
</html>

```

