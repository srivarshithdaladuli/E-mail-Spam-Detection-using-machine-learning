import streamlit as st
import pickle
import nltk 
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)
tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
st.title("EMAIL SPAM CLASSIFIER")
input_email=st.text_area("Enter Message")
if st.button('Predict'):
    transform_txt=transform_text(input_email)
    vector_input=tfidf.transform([transform_txt])#vectorization
    result=model.predict(vector_input)[0]
    if result==1:
        st.header("Spam")
    else:
       st.header("Ham")

