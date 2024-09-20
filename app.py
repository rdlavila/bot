import streamlit as st

with st.sidebar:
    with st.expander("Criar novo Bot"):
        bot_input = st.text_input("Nome do Bot")
    st.title("hypebots")
    st.divider()
    