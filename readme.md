# Eris-AI-Translator

Eris-AI-Translator is an open-source project that utilizes Groq's AI technologies for automatic translation. This project aims to provide quick and accurate translations between various languages.

## Features

-   Real-time translation between multiple languages.
-   Support for a wide range of languages.
-   User-friendly interface.
-   Easy integration with other applications.

## Technologies Used

-   **Python**: Main programming language used for development.
-   **Groq API**: Used for translation services.
-   **Flask**: Web framework used to create the API.
-   **HTML/CSS**: Used to develop the user interface.

## Requirements

-   Python 3.7 or higher
-   Flask
-   Other packages listed in `requirements.txt`

## Installation

1.  Clone the repository:
    
    `git clone https://github.com/horue/Eris-AI-Translator.git` 
    
2.  Navigate to the project directory:
    
    `cd Eris-AI-Translator` 
    
3.  Create and activate a virtual environment:

    ``python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate` `` 
    
4.  Install the dependencies:
    
    `pip install -r requirements.txt` 
    

## Usage

1.  Set up your Groq API key:
    -   Sign up at [Groq's website](https://www.groq.com) to obtain an API key.
    -   Create a file named `.env` in the project root directory and add your API key:
        
        `GROQ_API_KEY=your_api_key_here` 
        
2.  Start the Flask server:
    
    `flask run` 
    
3.  Access the application in your browser:
    
    `http://127.0.0.1:5000/` 
    

## Contributing

Contributions are welcome! To contribute to the project, follow these steps:

1.  Fork the project.
2.  Create a feature branch (`git checkout -b feature/feature-name`).
3.  Commit your changes (`git commit -am 'Added a new feature'`).
4.  Push to the branch (`git push origin feature/feature-name`).
5.  Create a new Pull Request.
