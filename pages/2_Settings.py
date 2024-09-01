###############################################################################################
# Filename: Settings
# Owner: Shreyas Sawant
# Purpose of code: Following code provides settings option for the user.
# Copyright (c) 2024 by Shreyas Sawant All Rights Reserved
# Last modified: 05-06-2024
###############################################################################################

import streamlit as st
import confidentiality_handler as conf

# Web Page configuration.
st.set_page_config(
    page_title = "RAG Buddy",
    page_icon = "💯",
    layout = "wide",
)

st.markdown(
    """
    # Settings
    This is the settings page, as of now we have very few things here 😅.
    but more is yet to come!!
    😉 
    """
)

def main():
    enc = conf.EncDecHandler()

    st.write("Delete chat history?")
    delete_button_chat = st.button("Delete history")
    username = st.text_input("What is your username?")
    st.write("""Wanna help the server manage the data better?
                Then delete it!! 😈""")
    
    if delete_button_chat:
        if username:
            enc.delete_hist(username)
            st.success("""Ok! you have clicked the delete button.
                          Your history shall Poof💨!!""")
        else:
            st.success("Heyyy! At least give a username 🤨.")
    
    st.write("Delete account?")
    delete_button_acc = st.button("Delete account")
    username = st.text_input("Enter the username to delete")
    if delete_button_acc:
        if username:
            if enc.delete_acc(username):
                st.success("""Ok! you have clicked the delete button.
                              Your account shall go Poof💨!!""")
            else:
                st.success("""Wait a minute! that username doesn't exist!""")
        else:
            st.success("Heyyy! At least give a username 🤨.")

if __name__ == '__main__':
    main()