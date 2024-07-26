import pandas as pd
import streamlit as st
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import torch

# Function to load the BERT NER model
def load_ner_model():
    model_name = "dslim/bert-base-NER"
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    device = 0 if torch.cuda.is_available() else -1  # Use GPU if available
    ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, device=device)
    return ner_pipeline

# Function to run NER on a list of subject lines
def run_ner_on_subject_lines(model, lines):
    results = []
    for line in lines:
        entities = model(line)
        results.append((line, entities))
    return results

# Streamlit app
st.title("BERT NER with Streamlit")
st.write("This application uses a BERT model to perform Named Entity Recognition (NER) on email subject lines.")

# Load the NER model
st.write("Loading the NER model...")
ner_model = load_ner_model()
if ner_model:
    st.write("NER model loaded successfully.")

# CSV file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None and ner_model is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(df.head())

    if 'SUBJECT_LINE' in df.columns:
        subject_lines = df['SUBJECT_LINE'].tolist()
        st.write("Subject lines loaded successfully.")
        
        if st.button('Run NER on Subject Lines'):
            st.write("Running NER on subject lines...")
            ner_results = run_ner_on_subject_lines(ner_model, subject_lines)
            st.write("### NER Results:")
            for line, entities in ner_results:
                st.write(f"**Subject Line:** {line}")
                for entity in entities:
                    st.write(f"  - {entity['word']}: {entity['entity']}")
    else:
        st.write("The CSV file must contain a 'SUBJECT_LINE' column.")
else:
    st.write("Upload a CSV file to process the subject lines.")
