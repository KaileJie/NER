import streamlit as st
import pandas as pd
from transformers import pipeline

# Load BERT NER model
nlp_model = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# Function to run NER on a list of subject lines and display the results
def run_ner(nlp, lines):
    st.write("### NER Results:")
    all_preds = []
    for i, line in enumerate(lines):
        preds = nlp(line)
        all_preds.append(preds)
        st.write(f"**Subject Line:** {line}")
        if preds:
            for ent in preds:
                st.write(f"  - {ent['word']} ({ent['entity']})")
        else:
            st.write("  - No named entities found")
        st.write("\n")

# Streamlit app
st.write("This application demonstrates the use of BERT NER on a set of subject lines")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the DataFrame to ensure it loaded correctly
    st.write("Data Preview:")
    st.write(df.head())

    if st.button('Run NER on Subject Lines'):
        run_ner(nlp_model, df['SUBJECT_LINE'].tolist())

if __name__ == "__main__":
    st.write("Click the button above to process the subject lines")

