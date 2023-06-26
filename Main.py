import streamlit as st
import requests


def get_chatbot_response(message):
    url = 'http://localhost:5005/webhooks/rest/webhook'
    payload = {
        'message': message
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        if data:
            reply = data[0]['text']
            if "images" in reply:
                reply = reply.split("images")
                image = reply[1]
                answer = reply[0]
                return answer,image
            return [reply,None]
    return None

def app():
    @st.cache
    def process_prompt(input):
        return get_chatbot_response(input)

   
    st.title("Tutor de xadrez")

 

    s_example = "Quantas peças cada jogador começa no xadrez?"
    input = st.text_input(
        "Faça uma pergunta",
        value=s_example,
        max_chars=150,
    )

    if st.button("Enviar"):
        with st.spinner(text="Rodando"):
            report_text = process_prompt(input)
            answer = report_text[0]
            image = report_text[1]
            st.markdown(answer)
            if image != None:
                st.image("images"+image, caption='Image Caption')
    
