import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get the response back
def getllmresponse(form_input,email_sender,email_recipent,email_style):
    llm=CTransformers(
        model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={'max_new_tokens':256,
                'temperature':0.01}
    )

    #Templete for building the prompt
    templete="""
    Write and email with {style} style and includes the topic : {email_topic}.\n\nSender: {sender}\nRecipent: {recipent}
    \n\nEmail Text : 

    """
    #Creating the final prompt
    prompt = PromptTemplate(
        input_variables=["style","email_topic","sender","recipent"],
        template=templete
    )

    # Generate the response using LLM
    response = llm(prompt.format(email_topic=form_input,sender=email_sender,recipent=email_recipent,style=email_style))
    print(response)
    return response
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
    email_style = st.selectbox("Writing Style",
                               ('Appreciating','Neutral','Formal','Not Satisfied'),index=2)


submit=st.button("Generate")


## When the 'Generate' button is clicked run below code
if submit:
    #st.write("Response")
    st.write(getllmresponse(form_input,email_sender,email_recipent,email_style))