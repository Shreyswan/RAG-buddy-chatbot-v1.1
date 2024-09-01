###############################################################################################
# Filename: Streamlit_component
# Owner: Shreyas Sawant
# Purpose of code: Following code handles the front-end component via streamlit library.
# Copyright (c) 2024 by Shreyas Sawant All Rights Reserved
# Last modified: 03-06-2024
###############################################################################################

import confidentiality_handler as conf
import RAG_backend as rb
import streamlit as st
import config as cfg

# Web Page configuration.
st.set_page_config(
    page_title = "RAG buddy",
    page_icon = "💯",
    layout = "wide",
)

st.markdown(
    """
    # The RAG Buddy chatting interface
    On this page, you shall get to use the RAG Buddy for any of your PDFs. The size limit is 200MB.\n
    Firstly, enter your existing username and then get started.
    You can upload your PDF and chat as much as you want on the context of the PDF. 
    The chatting takes some time to begin based on the size of your PDF, but once it begins, the experience 
    is as fast as ever. 
    """
)

def file_converter(pdf_file):
    with open(pdf_file.name, mode = 'wb') as w:
        w.write(pdf_file.getvalue())
    
    return pdf_file

def main():
    enc = conf.EncDecHandler()
    username = st.text_input("Enter your username to begin")
    dec_dict = enc.decode_dict_keys()
    if username in dec_dict:
        pdf_file = st.file_uploader("Upload your PDF", type = ('pdf'))
        if pdf_file is not None:
            pdf_file_lang = file_converter(pdf_file)
            rag_bot = rb.rag_chatbot(pdf_file_lang)
            bot = conf.For_RAG(pdf_file_lang)

            if cfg.PREV_PDF != pdf_file:
                cfg.PREV_PDF = pdf_file
                try:
                    rag_bot.pdf_preprocessing.clear()
                    rag_bot.create_chain.clear()
            
                except:
                    pass

            rag_bot.pdf_preprocessing()
            retriever_chain = rag_bot.create_chain()

            query = st.chat_input("Ask me a query")
            name_index = enc.get_name_index(username, dec_dict)
            if query is not None:
                response = bot.update_dict_data(username, query, retriever_chain)
                for i, key in enumerate(response.keys()):
                    if i == name_index:
                        for m in range(len(response[key]['query'])):
                            for j in response[key]:
                                if j == 'response':
                                    st.success(response[key][j][m])
                                
                                else:
                                    st.write(response[key][j][m])
    
    elif username and username not in dec_dict: 
        st.success("Oops! Looks like that username doesn't exist 🙁")

if __name__ == '__main__':
    main()