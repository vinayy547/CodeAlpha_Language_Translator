import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translator")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys())
    )

text = st.text_area("Enter Text")

if st.button("Translate"):
    if text.strip():
        try:
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.text_area(
                "Translated Text",
                translated,
                height=150
            )

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Enter some text")

# To run the code, use the command: streamlit run app.py.

# Make sure to install the required libraries using:
# pip install streamlit deep-translator 

# Note: The GoogleTranslator may have limitations on the number of translations or may require an API key for extensive use. Please refer to the deep-translator documentation for more details.    

# The app allows users to select source and target languages, input text, and get the translated output.
