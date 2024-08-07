# -*- coding: utf-8 -*-
"""nltknermodel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1my6Zx5uhAAv4v7vdzDoTY0IQXshc8mS8
"""

import streamlit as st
import pandas as pd
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

nltk.download('punkt')

nltk.download('maxent_ne_chunker')

nltk.download('words')

nltk.download('averaged_perceptron_tagger')

# Function:

def run_ner_nltk(lines):
    st.write("### NER Results:")
    for line in lines:
        tokens = word_tokenize(line)
        tagged = pos_tag(tokens)
        entities = ne_chunk(tagged)

        st.write(f"**Subject Line:** {line}")
        st.write(entities)
        st.write("\n")

# Streamlit app:

st.write("This application demonstrates the use of NLTK for NER on a set of subject lines")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("Data Preview:")

    st.write(df.head())

    if st.button('Run NER on Subject Lines'):

        run_ner_nltk(df['SUBJECT_LINE'].tolist())

if __name__ == "__main__":

    st.write("Click the button above to process the subject lines")

