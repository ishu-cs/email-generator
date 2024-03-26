import streamlit as st
st.set_page_config(
    page_title="Generate Emails",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.header("GENERATE EMAILS")

form_input = st.text_area('Enter the email topic',height=200)

# Creating columns for gui
col1,col2,col3 = st.columns([10,10,5])
with col1:
    email_sender = st.text_input('Sender Name')
with col2:
    email_recipent = st.text_input('Reciepent Name')
with col3:
    email_stylr = st.selectbox("Writing Style",
                               ('Appreciating','Neutral','Formal','Not Satisfied'),index=2)

submit=st.button("Generate")

## When the 'Generate' button is clicked run below code
if submit:
    st.write("Response")