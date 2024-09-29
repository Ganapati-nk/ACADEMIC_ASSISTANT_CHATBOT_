import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="ACADEMIC_ASSISTANT_CHATBOT ")
st.title("ACADEMIC_ASSISTANT_CHATBOT")

try:
    llm = ChatGroq(api_key=groq_api_key, model="Gemma-7b-It")
except Exception as e:
    st.error("Failed to initialize the language model. Please check the API key.")
    st.stop()

prompt = """
You are a helpful and conversational assistant that provides information about books, papers, or articles based on student queries.
Maintain the flow of conversation, keeping context from previous messages.

Here is the conversation so far:
{conversation_history}

Now, the user asks: {question}
Please provide a response that fits with the conversation and the current question.
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=['conversation_history', 'question'],
    template=prompt
)

chain = LLMChain(llm=llm, prompt=prompt_template)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm a conversational BOOK Chatbot! Ask me anything about books, papers, or articles, and I'll help you."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_conversation_history():
    conversation = ""
    for message in st.session_state.messages:
        if message["role"] == "user":
            conversation += f"User: {message['content']}\n"
        else:
            conversation += f"Assistant: {message['content']}\n"
    return conversation

if question := st.chat_input("Type your question here:"):
    st.session_state.messages.append({"role": "user", "content": question})
    
    with st.chat_message("user"):
        st.markdown(question)

    conversation_history = get_conversation_history()

    try:
        response = chain.run({
            "conversation_history": conversation_history,
            "question": question
        })
    except Exception as e:
        response = "Sorry, I couldn't generate a response. Please try again later."

    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.chat_message("assistant"):
        st.markdown(response)
