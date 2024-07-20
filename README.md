# Named Entity Recognition (NER) for Email Subject Lines

This project demonstrates how to use spaCy and Streamlit to perform Named Entity Recognition (NER) on a set of email subject lines. The application allows users to upload a CSV file containing subject lines, processes the text to extract named entities, and displays the results interactively.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/KaileJie/NER.git
   cd ner-subjectlines

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt

4. **Download the spaCy language model:**
    ```sh
    python -m spacy download en_core_web_sm

## Usage

1. **Run the Streamlit app:**
    ```sh
    streamlit run spacyner.py

2. **Upload your CSV file containing email subject lines:**

The CSV file should have a column named SUBJECT_LINE with the subject lines to process.

3. **View the NER results:**

The app will display the subject lines along with the extracted named entities.

## Project Structure
The directory structure of the Named Entity Recognition (NER) for Email Subject Lines project is outlined below:

~~~plaintext
ner-subjectlines/
│
├── spacyner.py               # Main application file that contains the Streamlit interface and NER processing
├── requirements.txt     # Dependencies file listing required Python packages
├── README.md            # Detailed project documentation
└── subjectlines.csv     # Sample CSV file with example subject lines for testing
~~~

## Example
Here’s an example of how the subject lines and extracted entities are displayed:
### NER Results:

**Subject Line:** Meeting with Dr. John at 6 PM
  - Dr. John (PERSON)
  - 6 PM (TIME)

**Subject Line:** Reminder: Project deadline on July 17th
  - July 17th (DATE)

**Subject Line:** Invitation: William's wedding on September 27th
  - William (PERSON)
  - September 27th (DATE)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any changes.

## License
This project is licensed under the MIT License.

### Python Code (spacyner.py)

~~~python
import pandas as pd
import streamlit as st
import spacy

# Load the spaCy model
nlp_model = spacy.load('en_core_web_sm')

# Function to run NER
def run_ner(nlp, lines):
    st.write("### NER Results:")
    for line in lines:
        doc = nlp(line)
        st.write(f"**Subject Line:** {line}")
        if doc.ents:
            for ent in doc.ents:
                st.write(f"  - {ent.text} ({ent.label_})")
        else:
            st.write("  - No named entities found")
        st.write("\n")

# Streamlit app
st.write("This application demonstrates the use of NER on a set of subject lines")

# CSV file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(df.head())

    if st.button('Run NER on Subject Lines'):
        run_ner(nlp_model, df['SUBJECT_LINE'].tolist())

if __name__ == "__main__":
    st.write("Click the button above to process the subject lines")
~~~

## Contact
If you have any questions or suggestions, feel free to open an issue or contact the repository owner.

