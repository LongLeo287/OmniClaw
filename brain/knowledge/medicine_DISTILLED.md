---
id: medicine
type: knowledge
owner: OA_Triage
---
# medicine
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Medicine-Recognition-System

This Flask web application utilizes Google's Generative AI models to generate detailed medical descriptions for uploaded images. The project, which focuses on medical content generation, incorporates two key models: the Pro-Vision model for in-depth medical descriptions and the Pro model for additional content generation. Upon uploading an image, the application uses the Pro-Vision model to generate comprehensive medical descriptions, ensuring clinical accuracy. Additionally, a validation step with the Pro model ensures that the context is indeed related to the medical field. The user is provided with generated content on successful validation, while the interface prompts for a valid medical image otherwise. The project's user interaction includes uploading images through a simple web form, content generation based on the uploaded images, and a validation step to ensure medical relevance. To maintain security, the application loads the required Google API key from environment variables. Further improvements could involve enhanced error handling, a more user-friendly interface, and thorough documentation for future development and maintenance.

## Built With

 - Google-GenerativeAI
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
     git clone https://github.com/KalyanMurapaka45/--------------------.git
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
   - Open a web browser or the appropriate client to access the project.<br>

### Option 2: Installation from DockerHub

If you prefer to use Docker, you can install and run the project using a Docker container from DockerHub:

1. **Pull the Docker Image**
   - Open your terminal or command prompt.
   - Run the following command to pull the Docker image from DockerHub:
     ```
     docker pull kalyan45/movierecommend-app
     ```
     This command downloads the Docker image from the DockerHub.

2. **Run the Docker Container**
   - Start the Docker container by running the following command. Adjust the port mapping as needed:
     ```
     docker run -p 5000:5000 kalyan45/movierecommend-app
     ```
     This command launches the project within a Docker container.

3. **Access the Project**
   - Open a web browser or the appropriate client to access the project.<br>

   
## API Key Setup

To use this project, you need an API key from Google Gemini Large Language Model. Follow these steps to obtain and set up your API key:

1. **Get API Key:**
   - Visit Alkali App [Click Here](https://makersuite.google.com/app/apikey).
   - Follow the instructions to create an account and obtain your API key.

2. **Set Up API Key:**
   - Create a file named `.env` in the project root.
   - Add your API key to the `.env` file:
     ```dotenv
     GOOGLE_API_KEY=your_api_key_here
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

### File: requirements.txt
```txt
google-generativeai
flask
python-dotenv
Pillow
```

### File: app.py
```py
import os
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, request, render_template, render_template_string, redirect, url_for

# Load environment variables from .env
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))# Configure Google Generative AI

vis_model = genai.GenerativeModel('gemini-pro-vision') # Loaded the Pro-Vision model

text_model = genai.GenerativeModel('gemini-pro') # Loaded the Pro model

app = Flask(__name__)

# Function to generate content
def gen_image(prompt, image):
    response = vis_model.generate_content(image)
    return response.text

def validate(validation_prompt):
    vresponse = text_model.generate_content(validation_prompt)
    return vresponse.text

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_prompt = '''
                - Generate a very detailed medical description for the given image.
                - Identify and describe any relevant medical conditions, anomalies, or abnormalities present in the image.
                - Additionally, provide insights into any potential treatments or recommended actions based on the observed medical features.
                - Please ensure the generated content is accurate and clinically relevant.
                - Please don't provide false and misleading information.
                '''
        
        uploaded_file = request.files['file']
        image = Image.open(uploaded_file)
        response_text = gen_image(image_prompt, image)

        validation_prompt = "Check if the provided context is related to the medical field. Just Reply with 'Yes' or 'No'."
        vans = validate(validation_prompt)

        if vans == "Yes":
            return render_template('index.html', response_text=response_text)
        else:
            return render_template('index.html', response_text="Please provide a valid medical image.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### File: static\style.css
```css
body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

h1 {
    color: #333;
}

form {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
    color: #333;
}

input[type="file"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 5px;
}

input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #45a049;
}

.result {
    margin-top: 20px;
    max-width: 500px;
    word-wrap: break-word;
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.result h2 {
    color: #333;
}

```

### File: templates\index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Image Recognition App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Medical Image Recognition App</h1>
    <form method="post" enctype="multipart/form-data">
        <label for="file">Choose a medical image:</label>
        <input type="file" name="file" accept=".jpg, .jpeg, .png" required>
        <br>
        <input type="submit" value="Generate Medical Description">
    </form>
    
    {% if response_text %}
        <div class="result">
            <p>{{ response_text }}</p>
        </div>
    {% endif %}
</body>
</html>

```

