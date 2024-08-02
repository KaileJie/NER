# NLTK Named Entity Recognition (NER) Project

## Overview

This project implements Named Entity Recognition (NER) using the NLTK library. The application is built using Streamlit and allows users to upload a CSV file containing subject lines to perform NER and visualize the results.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running on Google Colab](#running-on-google-colab)
- [Contributing](#contributing)
- [License](#license)

## Features

- **NER using NLTK**: Utilize the NLTK library for NER.
- **Streamlit Integration**: User-friendly web application to upload CSV files and visualize NER results.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/KaileJie/NER.git
   cd NER
   ```

2. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```


## Usage

1. **Run the Streamlit application:**
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
   !pip install -r "/content/NER/NLTK_NER/requirements.txt"
   ```

2. **Ensure you have the `nltkner.py` file ready**: You should have the `nltkner.py` file in your Colab environment. If you don't, you can upload it directly to your Colab environment.

3. **Run the Streamlit app using pyngrok:**

   ```python
   import os
   from threading import Thread
   from pyngrok import ngrok

   # Add your ngrok token here
   ngrok.set_auth_token('YOUR_NGROK_TOKEN')

   def run_streamlit():
       os.system('streamlit run /content/NER/NLTK_NER/nltkner.py --server.port 8501')

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

---
