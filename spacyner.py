# -*- coding: utf-8 -*-
"""NERnewdata.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zs1RD8iDElhyF46dniKKQjzM8UaIg3TL
"""

import pandas as pd

df = pd.read_csv('subjectlines.csv')

df.head()

import streamlit as st

import spacy

#SpaCy model:

nlp_model = spacy.load('en_core_web_sm')

# Function:

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

# Streamlit app:

st.write("This application demonstrates the use of NER on a set of subject lines")

# CSV file:

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Display the first few rows:

    st.write("Data Preview:")

    st.write(df.head())

    if st.button('Run NER on Subject Lines'):

        run_ner(nlp_model, df['SUBJECT_LINE'].tolist())

if __name__ == "__main__":

    st.write("Click the button above to process the subject lines")

