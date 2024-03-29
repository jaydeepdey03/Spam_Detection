import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()  # step1
    text = nltk.word_tokenize(text)  # tokenize
    y = list()
    # removing special Characters
    for i in text:
        if(i.isalnum()):
            y.append(i)
    text = y.copy()
    y.clear()
    # removing stop words
    for i in text:
        if i not in stopwords.words('english') and i not in punctuation:
            y.append(i)
    text = y.copy()
    y.clear()
    #  stemming
    for i in text:
        y.append(ps.stem(i))
    text = y.copy()
    y.clear()
    return ' '.join(text)


model = pickle.load(open('./Model/model.pkl', 'rb'))
tfidf = pickle.load(open('./Model/vectorizer.pkl', 'rb'))

st.title("Spam Classifier")

input_sms = st.text_input("Enter Message: ")

transform_sms = transform_text(input_sms)
vector_input = tfidf.transform([transform_sms])
result = model.predict(vector_input)[0]

if st.button("Predict"):
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

