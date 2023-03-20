import streamlit as st
from model import GeneralModel
import nltk
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
nltk.download('stopwords')
nltk.download('punkt')

stopwords = nltk.corpus.stopwords.words('portuguese')

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.body.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)





def pre_processing(sentences):
    for i in range(len(sentences)):
        words = nltk.word_tokenize(sentences[i])
        newwords = [word for word in words if word not in stopwords]
        sentences[i] = ' '.join(newwords)
    sentences = ''.join(sentences)
    return sentences

def app():

   
    pred = GeneralModel()


    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip())

    

   
    st.title("Resumo de paginas na web")

 

    s_example = "https://pt.wikipedia.org/wiki/Tel%C3%B4mero"
    input = st.text_input(
        "Cole a URL",
        value=s_example,
        max_chars=150,
    )

    html = urllib.request.urlopen(input).read()
    text = text_from_html(html)
    sentences = nltk.sent_tokenize(text)
    promp = pre_processing(sentences)
    mid = len(promp) // 2
    promp = promp[:mid]

    if st.button("Enviar"):
        with st.spinner(text="Rodando"):
            report_text = process_prompt(promp)
            st.markdown(report_text)
    
