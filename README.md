# Named Entity Recognition (NER) Project

## Overview

This project implements Named Entity Recognition (NER) using different models, specifically spaCy, NLTK, and BERT from the Hugging Face Transformers library. The project is designed to run on a Streamlit web application, allowing users to upload a CSV file containing subject lines to perform NER and visualize the results. The project can be run locally or on Google Colab.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Running on Google Colab](#running-on-google-colab)
- [Contributing](#contributing)
- [License](#license)

## Features

- **NER using spaCy**: Utilize spaCy's pre-trained NER model.
- **NER using NLTK**: Utilize NLTK for Named Entity Recognition.
- **NER using BERT**: Utilize BERT-based NER models from the Hugging Face Transformers library.
- **Streamlit Integration**: User-friendly web application to upload CSV files and visualize NER results.

## Project Structure

The project is organized into three main subfolders:

- **BERT_NER**: Contains the implementation for BERT-based NER.
  - `bertner.py`: The Streamlit app for running BERT-based NER.
  - `requirements.txt`: The dependencies required for running the BERT NER model.
  - `README.md`: Instructions specific to the BERT NER implementation.
  - `subjectlines.csv`: Sample CSV file for testing the BERT NER model.

- **Spacy_NER**: Contains the implementation for spaCy-based NER.
  - `spacyner.py`: The Streamlit app for running spaCy-based NER.
  - `requirements.txt`: The dependencies required for running the spaCy NER model.
  - `README.md`: Instructions specific to the spaCy NER implementation.
  - `subjectlines.csv`: Sample CSV file for testing the spaCy NER model.

- **NLTK_NER**: Contains the implementation for NLTK-based NER.
  - `nltkner.py`: The Streamlit app for running NLTK-based NER.
  - requirements.txt`: The dependencies required for running the NLTK NER model.
  - README.md`: Instructions specific to the NLTK NER implementation.
  - subjectlines.csv`: Sample CSV file for testing the NLTK NER model.

**We found that spaCy and NLTK are our two best models as they provide more accurate results.**
## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/KaileJie/NER.git
   cd NER
   ```

2. **Navigate to the desired model folder:**

   For BERT:
   ```sh
   cd BERT_NER
   ```

   For spaCy:
   ```sh
   cd Spacy_NER
   ```
   
   For NLTK:
   ```sh
   cd NLTK_NER
   ```
3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit application:**

   For BERT:
   ```sh
   streamlit run bertner.py
   ```

   For spaCy:
   ```sh
   streamlit run spacyner.py
   ```

   For NLTK:
   ```sh
   streamlit run nltkner.py
   ```
2. **Upload a CSV file:**
   - The CSV file should contain a column named `SUBJECT_LINE` with the text data.

3. **View NER results:**
   - The application will display the named entities identified in each subject line.

## Running on Google Colab

To run the Streamlit app on Google Colab, follow these steps:

1. **Clone the repository and install necessary packages:**

   ```python
   !git clone https://github.com/KaileJie/NER

   # Install the necessary packages
   !pip install pyngrok
   !pip install -r "/content/NER/Spacy_NER/requirements.txt" #You can change Spacy_NER to BERT_NER or NLTK_NER
   ```

2. **Ensure you have the appropriate Python file ready**: You should have either the `bertner.py`, `spacyner.py`, or `nltkner.py`file in your Colab environment, depending on which model you want to use. If you don't, you can upload it directly to your Colab environment.

3. **Run the Streamlit app using pyngrok:**

   ```python
   import os
   from threading import Thread
   from pyngrok import ngrok

   # Add your ngrok token here
   ngrok.set_auth_token('YOUR_NGROK_TOKEN')

   def run_streamlit():
       os.system('streamlit run /content/NER/Spacy_NER/spacyner.py --server.port 8501')  # or BERT_NER/bertner.py or NLTK_NER/nltkner.py

   # Start a thread to run the Streamlit app
   thread = Thread(target=run_streamlit)
   thread.start()

   # Open a tunnel to the streamlit port 8501
   public_url = ngrok.connect(addr='8501', proto='http', bind_tls=True)
   print('Your Streamlit app is live at:', public_url)
   ```

Replace `'YOUR_NGROK_TOKEN'` with your actual ngrok authentication token.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss improvements, bugs, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.