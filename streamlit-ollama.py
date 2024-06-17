import streamlit as st
import ollama
st.title('Small app😎')
def generate_text(input_message):
    message=[{'role': 'user', 'content': input_message}]
    response = ollama.chat(
        model='qwen2',
        messages=message,
##        stream=True,
    )
##    for chunk in stream:
    st.info(response['message']['content'])
with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_text(text)